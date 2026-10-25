#!/usr/bin/env python3
"""Gera o site do Gonçalo em _site/ (publicado no GitHub Pages; o repositório é público).

Um sítio para tudo, sem sair do browser:
  index.html                 painel pessoal (cifrado) + disciplinas, Quizrama, novidades
  agenda.html                agenda completa (cifrada)
  <D>/index.html             info (cifrada), resumo e revisão em PDF, teóricas, práticas, soluções, quiz, testes
  ver.html?f=...#pN          visualizador dentro do site (PDF com PDF.js, código, download)
  estudo.html?f=...&so=...   ficha em PDF à esquerda, as soluções dela à direita
  solucoes/                  o SOLUCOES.html ("lê a teoria" abre o resumo em PDF na página certa)
  quizrama/                  os quizzes

Só publica ficheiros que estão no git e passam as regras de PUBLICAR/EXCLUIR. A parte
pessoal (agenda, tarefas, avisos, INFO) só existe cifrada em _shared/site/pessoal.enc
(feito pelo _shared/template/pessoal.py); nada pessoal em claro entra no site.
No fim verifica as ligações internas (aviso; com --estrito, falha).

Uso: python3 _shared/site/build_site.py [--saida _site] [--lista] [--estrito]
Precisa de pdftotext (poppler).
"""
import argparse
import fnmatch
import html
import json
import re
import shutil
import subprocess
import sys
import time
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit, parse_qs

ROOT = Path(__file__).resolve().parents[2]
SITE = Path(__file__).resolve().parent
TEMPLATE = ROOT / "_shared/template"

# --------------------------------------------------------------------------
# O que se publica (caminhos do repositório; ** apanha subpastas)
# --------------------------------------------------------------------------
PUBLICAR = [
    "*/Teoricas/**", "*/Praticas/**", "*/Testes/**", "*/Trabalho/**",
    "Quizrama/guia_*.pdf",                              # guias dos testes em PDF
]
EXCLUIR = [
    "**/.DS_Store", "**/*.zip", "**/*.md",
    "TecnologiasWeb/Praticas/Semana_1/cv/**",          # CV pessoal
    "TecnologiasWeb/Praticas/Semana_1/homepage_v2/**",  # página pessoal (foto, contactos)
    "**/lex.yy.c",                                     # gerado pelo flex
]
# executáveis sem extensão (Lexer, CLexer) saem pela verificação de binário


QUIZZES = {
    "Redes": [
        ("quizrama/redes.html", "Quiz do 1.º teste", "Capítulos 1–2, com nota /20"),
        ("quizrama/guia_redes_teste1.html", "Guia do 1.º teste", "a matéria, ligada às perguntas"),
        ("ver.html?f=ficheiros/Quizrama/guia_redes_teste1.pdf&d=Redes&t=Guia%20do%201.%C2%BA%20teste",
         "Guia do 1.º teste em PDF", "o mesmo guia, para imprimir"),
    ],
}
QUIZRAMA_EXTRA = [
    ("quizrama/index.html", "Sistemas de Operações — perguntas", "~540 perguntas de exames anteriores"),
    ("quizrama/teste2.html", "Sistemas de Operações — 2.º teste", "treino ao estilo do teste"),
    ("quizrama/guia_estudo_teste2.html", "Sistemas de Operações — guia do 2.º teste", "a matéria"),
]

TEXTO = {".c", ".h", ".l", ".y", ".x", ".hs", ".java", ".py", ".txt", ".flex", ".bison",
         ".js", ".css", ".html", ".mdown", ".sh", ".json", ".xml", ".csv"}
TEXTO_NOMES = {"Makefile", "README"}

DOCS_NOMES = {"RESUMO": ("Resumo teórico", "Toda a matéria das teóricas, com diagramas e exercícios “Pratica agora”."),
              "REVISAO": ("Folha de revisão", "Receitas curtas para rever antes do teste.")}

MESES = ["jan.", "fev.", "mar.", "abr.", "maio", "jun.", "jul.", "ago.", "set.", "out.", "nov.", "dez."]


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def git(*args) -> str:
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, check=True).stdout


def padrao_re(p: str) -> str:
    """Glob com ** (qualquer número de pastas) e * (dentro de uma pasta) -> regex."""
    r = re.escape(p).replace(r"\*\*/", "(?:.*/)?").replace(r"/\*\*", "/.*").replace(r"\*", "[^/]*")
    return r + "$"


def casa(caminho: str, padroes) -> bool:
    return any(re.match(padrao_re(p), caminho) for p in padroes)


def binario(p: Path) -> bool:
    with p.open("rb") as f:
        return b"\0" in f.read(4096)


def tamanho(n: int) -> str:
    if n < 1024:
        return f"{n} B"
    if n < 1024 * 1024:
        return f"{round(n / 1024)} kB"
    return f"{n / 1024 / 1024:.1f} MB".replace(".", ",")


def tipo(p: str) -> str:
    nome = p.rsplit("/", 1)[-1]
    ext = Path(nome).suffix.lower()
    if ext == ".pdf":
        return "pdf"
    if ext in TEXTO or nome in TEXTO_NOMES:
        return "texto"
    return "outro"


def data_curta(d: date) -> str:
    return f"{d.day} {MESES[d.month - 1]}"


def titulo_de(caminho: str, titulos: dict) -> str:
    if caminho in titulos:
        return titulos[caminho]
    nome = Path(caminho).stem if tipo(caminho) == "pdf" else caminho.rsplit("/", 1)[-1]
    m = re.match(r"Aula_(\d+)(?:-(\d+))?$", nome)
    if m:
        a, b = int(m.group(1)), m.group(2)
        return f"Aula {a}" + (f"–{int(b)}" if b else "")
    if tipo(caminho) == "pdf":
        nome = nome.replace("_", " ").replace("-", " ")
        return nome[:1].upper() + nome[1:]
    return nome


def numero_aula(caminho: str) -> str:
    m = re.search(r"Aula_(\d+)(?:-(\d+))?", caminho)
    if not m:
        return "—"
    return f"{int(m.group(1)):02d}" + (f"–{int(m.group(2)):02d}" if m.group(2) else "")


# --------------------------------------------------------------------------
# Moldura comum
# --------------------------------------------------------------------------
NAV = (("disciplinas", "", "Início"), ("agenda", "agenda.html", "Agenda"), ("solucoes", "solucoes/", "Soluções"),
       ("quizrama", "quizrama/", "Quizrama"))


def pagina(titulo: str, corpo: str, raiz: str, ativo: str = "", cor=None, extra_head: str = "",
           descricao: str = "", larga: bool = False) -> str:
    nav = []
    for chave, href, rotulo in NAV:
        atual = ' aria-current="page"' if chave == ativo else ""
        nav.append(f'<a href="{raiz}{href or "index.html"}"{atual}>{rotulo}</a>')
    cor_attr = f' data-cor="{cor}"' if cor is not None else ""
    desc = f'<meta name="description" content="{esc(descricao)}">' if descricao else ""
    return f"""<!DOCTYPE html>
<html lang="pt-PT"{cor_attr}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<title>{esc(titulo)}</title>
{desc}
<link rel="stylesheet" href="{raiz}assets/site.css">
{extra_head}
</head>
<body>
<div class="pagina{" larga" if larga else ""}">
  <header class="topo">
    <a class="marca" href="{raiz}index.html">FCUP · 3.º ano</a>
    <nav>{"".join(nav)}</nav>
  </header>
{corpo}
  <footer class="rodape">Os slides e os enunciados são dos docentes de cada disciplina; resumos e soluções feitos a partir das aulas.</footer>
</div>
</body>
</html>
"""


def ver_href(raiz: str, caminho: str, disciplina: str, titulo: str) -> str:
    return (f"{raiz}ver.html?f={quote('ficheiros/' + caminho)}"
            f"&d={quote(disciplina)}&t={quote(titulo)}")


# --------------------------------------------------------------------------
# Disciplinas
# --------------------------------------------------------------------------
class Disciplina:
    def __init__(self, pasta: str, cor: int, n: int):
        self.pasta = pasta
        self.cor = cor
        self.n = n
        self.dir = ROOT / pasta
        md = (self.dir / ".fonte" / f"RESUMO_{pasta}.md").read_text()
        m = re.search(r'^title:\s*"?(.*?)\s*(---|—|")', md, re.M)
        nome = m.group(1).strip() if m else pasta
        m2 = re.match(r"(.*?)\s*\(([^)]+)\)$", nome)
        self.nome, self.sigla = (m2.group(1), m2.group(2)) if m2 else (nome, "")
        d = re.search(r'^date:\s*"?Atualizado:\s*([^"(]*)', md, re.M)
        self.atualizado = d.group(1).strip().rstrip(",") if d else ""
        self.docs = []        # (slug, titulo, descricao, href)
        self.teoricas = []    # caminhos
        self.praticas = defaultdict(list)
        self.testes = []
        self.outros = []      # PDFs soltos na pasta da disciplina sem fonte HTML


def descobrir():
    pastas = sorted({p.parent.parent.name for p in ROOT.glob("*/.fonte/RESUMO_*.md")}, key=str.lower)
    return [Disciplina(p, i % 6, i + 1) for i, p in enumerate(pastas)]


def ficheiros_publicados():
    todos = [l for l in git("ls-files").splitlines() if l]
    out = []
    for c in todos:
        if not casa(c, PUBLICAR) or casa(c, EXCLUIR):
            continue
        p = ROOT / c
        if not p.is_file():
            continue
        if tipo(c) == "outro" and not Path(c).suffix and binario(p):
            continue  # executável compilado
        out.append(c)
    return out


# --------------------------------------------------------------------------
# Resumos em PDF: a página de cada secção (para o "lê a teoria" das soluções)
# --------------------------------------------------------------------------
def normaliza(t: str) -> str:
    import unicodedata
    t = unicodedata.normalize("NFD", t.lower())
    return re.sub(r"[^a-z0-9]", "", "".join(c for c in t if unicodedata.category(c) != "Mn"))


def ident_pandoc(t: str) -> str:
    """O id que o pandoc dá a um título (auto_identifiers), para as ligações do guia do Quizrama."""
    t = re.sub(r"[^\w\s.-]", "", t.lower())
    t = re.sub(r"\s+", "-", t.strip())
    return re.sub(r"^[^a-zà-ÿ]+", "", t) or "section"


def etiqueta(bruta: str) -> str:
    """"F2.2(c)" -> "F2.2"; "Ex. 6" -> "Ex.6"; "1.13 d)" -> "1.13" (como nos ids das soluções)."""
    e = re.sub(r"\s+", "", bruta)
    e = re.sub(r"\(.*$", "", e)
    return re.sub(r"(?<=\d)[a-z]\)?$", "", e).rstrip(".,:")


def grupos_solucoes(d) -> list:
    """Ids das alíneas de cada secção "##" do SOLUCOES_<D>.md, por ordem (como o ler_solucoes do
    div-envs.lua: a k-ésima caixa Pratica agora do resumo é a k-ésima secção "##")."""
    f = d.dir / ".fonte" / f"SOLUCOES_{d.pasta}.md"
    if not f.exists():
        return []
    gs, atual, ex_num, n, vistos = [], None, "sol", 0, defaultdict(int)
    for linha in f.read_text().splitlines():
        if linha.startswith("## "):
            atual = []; gs.append(atual)
        elif linha.startswith("### "):
            h3 = linha[4:]
            ex_txt = re.split(r"\s+---|\s+—", h3, maxsplit=1)[0]
            ex_num = re.sub(r"\s+", "", ex_txt.replace("---", "—").replace("--", "–"))
            n = 0
        elif linha.startswith("#### ") and atual is not None:
            n += 1
            h4 = linha[5:]
            m = re.match(r"\((\w+)\)", h4) or re.match(r"(\d+)\.", h4)
            id_ = f"{d.pasta}-{ex_num}-{m.group(1) if m else n}"
            vistos[id_] += 1
            atual.append(id_ if vistos[id_] == 1 else f"{id_}-{vistos[id_]}")
    return gs


def seccoes_resumo(d) -> list:
    """[(nível, título, texto, [etiquetas], nº de caixas Pratica agora)] do RESUMO_<D>.md, por ordem."""
    md = (d.dir / ".fonte" / f"RESUMO_{d.pasta}.md").read_text()
    md = re.sub(r"^```.*?^```", "", md, flags=re.S | re.M)
    partes = re.split(r"^(#{1,3}) (.+?)\s*(?:\{[^}]*\})?\s*$", md, flags=re.M)
    out = []
    for i in range(1, len(partes), 3):
        corpo = partes[i + 2]
        etqs = []
        for caixa in re.findall(r"^:::+ *\{\.pratica[^}]*\}(.*?)^:::+ *$", corpo, flags=re.S | re.M):
            etqs += [etiqueta(e) for e in re.findall(r"^\s*[-*] \*\*([^*]+)\*\*", caixa, flags=re.M)]
        n_caixas = len(re.findall(r"^:::+ *\{\.pratica", corpo, flags=re.M))
        out.append((len(partes[i]), partes[i + 1].strip(), corpo, [e for e in etqs if e], n_caixas))
    return out


def paginas_pdf(pdf: Path) -> list:
    r = subprocess.run(["pdftotext", "-enc", "UTF-8", str(pdf), "-"], capture_output=True, text=True)
    return [normaliza(p) for p in r.stdout.split("\f")]


# --------------------------------------------------------------------------
# Páginas
# --------------------------------------------------------------------------
FICHAS = {}      # ficha -> prefixo das soluções (fichas.json)
SOL_DE = set()   # disciplinas com soluções


def prefixo_sol(c: str, d) -> str:
    """Prefixo dos ids das soluções de uma ficha ("" = esta ficha não tem soluções no site)."""
    if c in FICHAS:
        return FICHAS[c]
    nome = c.rsplit("/", 1)[-1].lower()
    if d.pasta in SOL_DE and c.split("/")[1] == "Praticas" and tipo(c) == "pdf" \
            and not re.search(r"solu|respost|resolv", nome):
        return f"{d.pasta}-"
    return ""


def estudo_href(raiz: str, caminho: str, disciplina: str, titulo: str, so: str) -> str:
    return (f"{raiz}estudo.html?f={quote('ficheiros/' + caminho)}&d={quote(disciplina)}"
            f"&t={quote(titulo)}&so={quote(so)}")


def lista_ficheiros(itens, d: Disciplina, titulos, raiz="../", numerar=None) -> str:
    li = []
    for c in itens:
        t = titulo_de(c, titulos)
        p = ROOT / c
        k = tipo(c)
        ext = (Path(c).suffix[1:] or c.rsplit("/", 1)[-1]).upper()
        so = prefixo_sol(c, d)
        meta = f"{ext} · {tamanho(p.stat().st_size)}" + (" · com soluções" if so else "")
        num = numerar(c) if numerar else ""
        href = estudo_href(raiz, c, d.pasta, t, so) if so else ver_href(raiz, c, d.pasta, t)
        li.append(f'<li><a href="{esc(href)}"><span class="num">{esc(num)}</span>'
                  f'<span class="titulo">{esc(t)}</span><span class="tipo">{esc(meta)}</span></a></li>')
    return '<ul class="lista">' + "".join(li) + "</ul>"


def pagina_disciplina(d: Disciplina, titulos, solucoes: bool) -> str:
    seccoes, nav = [], []

    def sec(id_, rotulo, conteudo, extra=""):
        nav.append(f'<a href="#{id_}">{rotulo}</a>')
        seccoes.append(f'<section class="seccao" id="{id_}"><h2>{rotulo}{extra}</h2>{conteudo}</section>')

    seccoes.append(f'<section class="seccao so-desbloqueado" id="info" hidden><h2>Info <span class="mono">do Moodle</span></h2>'
                   f'<div class="info-disc" data-info="{esc(d.pasta)}"></div></section>')
    nav.append('<a href="#info" class="so-desbloqueado">Info</a>')
    if d.docs:
        blocos = []
        for slug, t, desc, pdf in d.docs:
            blocos.append(f'<div class="documento"><div><h3><a href="{esc(pdf)}">{esc(t)}</a></h3>'
                          f'<p>{esc(desc)}</p></div><div class="acoes"><a class="etiqueta principal" href="{esc(pdf)}">Abrir</a></div></div>')
        sec("resumo", "Resumo", '<div class="documentos">' + "".join(blocos) + "</div>",
            f' <span class="mono">{esc(d.atualizado)}</span>' if d.atualizado else "")

    if d.teoricas:
        n = sum(1 for c in d.teoricas if c.endswith((".pdf", ".pptx")) and "Aula_" in c)
        sec("teoricas", "Teóricas", lista_ficheiros(d.teoricas, d, titulos, numerar=numero_aula),
            f' <span class="mono">{n} aulas</span>' if n else "")

    if d.praticas:
        partes = []
        for semana in sorted(d.praticas, key=lambda s: -int(re.sub(r"\D", "", s) or 0)):
            fs = d.praticas[semana]
            soltos = [c for c in fs if c.count("/") == 3]
            grupos = defaultdict(list)
            for c in fs:
                if c.count("/") > 3:
                    grupos[c.split("/")[3]].append(c)
            html_ = ""
            principais = soltos + [c for g in grupos.values() for c in g if tipo(c) == "pdf"]
            if principais:
                html_ += lista_ficheiros(principais, d, titulos, numerar=lambda c: "")
            for g, cs in sorted(grupos.items()):
                codigo = [c for c in cs if tipo(c) != "pdf"]
                if codigo:
                    html_ += (f'<details class="codigo-grupo"><summary><span class="mono">{len(codigo)} ficheiros</span> '
                              f'{esc(g)}</summary>'
                              + lista_ficheiros(codigo, d, titulos,
                                                numerar=lambda c: "") + "</details>")
            rot = semana.replace("_", " ")
            partes.append(f'<div class="semana"><h3>{esc(rot)}</h3>{html_}</div>')
        sec("praticas", "Práticas", "".join(partes), f' <span class="mono">{len(d.praticas)} semana{"s" if len(d.praticas) != 1 else ""}</span>')

    if solucoes:
        sec("solucoes", "Soluções",
            f'<p>Os exercícios “Pratica agora” do resumo, resolvidos alínea a alínea. Cada alínea está escondida até a abrires.</p>'
            f'<a class="etiqueta principal" href="../solucoes/#{esc(d.pasta)}">Abrir as soluções de {esc(d.nome)}</a>')

    if d.pasta in QUIZZES:
        li = "".join(f'<li><a href="../{esc(h)}"><span class="num">Q{i + 1}</span><span class="titulo">{esc(t)}</span>'
                     f'<span class="tipo">{esc(s)}</span></a></li>' for i, (h, t, s) in enumerate(QUIZZES[d.pasta]))
        sec("quiz", "Quiz", f'<ul class="lista">{li}</ul>')

    if d.testes:
        sec("testes", "Testes", lista_ficheiros(d.testes, d, titulos, numerar=lambda c: ""))

    if d.outros:
        sec("outros", "Outros", lista_ficheiros(d.outros, d, titulos, numerar=lambda c: ""))

    meta = []
    if d.atualizado:
        meta.append(f"<span>Atualizado: {esc(d.atualizado)}</span>")
    corpo = f"""
  <section class="cabecalho">
    <p class="migalhas"><a href="../index.html">Disciplinas</a> / {d.n:02d}</p>
    <h1>{esc(d.nome)}{f' <small class="mono">{esc(d.sigla)}</small>' if d.sigla else ""}</h1>
    <p class="meta mono">{"".join(meta)}</p>
  </section>
  <nav class="seccoes">{"".join(nav)}</nav>
  {"".join(seccoes)}
  <script src="../assets/seccoes.js" defer></script>
  <script type="module" src="../assets/pessoal.js"></script>"""
    return pagina(d.nome, corpo, "../", "disciplinas", d.cor, descricao=f"Resumos, slides, fichas e soluções de {d.nome}.")


def novidades(publicados_por_disciplina, disciplinas):
    """Últimos ficheiros mudados no git (o que um colega quer ver primeiro)."""
    try:
        log = git("log", "--since=21 days ago", "--name-only", "--format=@%cs", "--", *[d.pasta for d in disciplinas], "Quizrama", "SOLUCOES.html")
    except subprocess.CalledProcessError:
        return []
    vistos, out, quando = set(), [], None
    por_origem = defaultdict(int)
    nomes = {d.pasta: d for d in disciplinas}
    for linha in log.splitlines():
        if linha.startswith("@"):
            quando = date.fromisoformat(linha[1:])
            continue
        if not linha:
            continue
        partes = linha.split("/")
        if partes[0] == "Quizrama" and len(partes) == 2 and linha.endswith(".html"):
            chave, rot, texto, href, cor = "quiz", "Quizrama", "quizzes atualizados", "quizrama/", None
        elif partes[0] == "SOLUCOES.html":
            chave, texto, href, cor, rot = "sol", "soluções atualizadas", "solucoes/", None, "Soluções"
        elif partes[0] in nomes and len(partes) > 1:
            d = nomes[partes[0]]
            if partes[1] == ".fonte" and partes[-1].startswith("RESUMO_"):
                chave, texto = (d.pasta, "res"), "resumo atualizado"
                href = ver_href("", f"{d.pasta}/RESUMO_{d.pasta}.pdf", d.pasta, "Resumo")
            elif partes[1] == ".fonte" and partes[-1].startswith("SOLUCOES_"):
                chave, texto, href = (d.pasta, "sol"), "novas soluções", f"solucoes/#{d.pasta}"
            elif partes[1] == "Teoricas" and linha in publicados_por_disciplina:
                chave, texto, href = (d.pasta, linha), "teórica nova: " + titulo_de(linha, TITULOS), f"{d.pasta}/index.html#teoricas"
            elif partes[1] == "Praticas" and linha in publicados_por_disciplina and len(partes) > 2:
                chave, texto, href = (d.pasta, partes[2]), f"práticas da {partes[2].replace('_', ' ').lower()}", f"{d.pasta}/index.html#praticas"
            else:
                continue
            cor, rot = d.cor, d.nome.split()[0]
        else:
            continue
        if chave in vistos or por_origem[rot] >= 2:
            continue
        vistos.add(chave)
        por_origem[rot] += 1
        out.append((quando, rot, texto, href, cor))
        if len(out) >= 6:
            break
    return out


def pagina_inicio(disciplinas, nov, n_quizzes) -> str:
    entradas = []
    for d in disciplinas:
        meta = []
        if d.atualizado:
            meta.append(f"<span>{esc(d.atualizado)}</span>")
        n_aulas = sum(1 for c in d.teoricas if "Aula_" in c and c.endswith((".pdf", ".pptx")))
        if n_aulas:
            meta.append(f"<span>{n_aulas} aulas</span>")
        if d.praticas:
            n = len(d.praticas)
            meta.append(f"<span>{n} semana{'s' if n != 1 else ''} de práticas</span>")
        if d.pasta in QUIZZES:
            meta.append("<span>quiz</span>")
        sigla = f" <small>{esc(d.sigla)}</small>" if d.sigla else ""
        entradas.append(f"""<li data-cor="{d.cor}"><a class="entrada" href="{esc(d.pasta)}/index.html">
      <span class="n">{d.n:02d}</span>
      <div><h2>{esc(d.nome)}{sigla}</h2></div>
      <div class="meta mono">{"".join(meta)}</div>
    </a></li>""")
    nov_html = "".join(
        f'<li{f" data-cor={c}" if c is not None else ""}><span class="quando">{data_curta(q)}</span>'
        f'<a href="{esc(h)}"><b>{esc(r)}</b> · {esc(t)}</a></li>'
        for q, r, t, h, c in nov) or '<li><span class="quando">—</span><span class="suave">Nada nas últimas três semanas.</span></li>'
    cores = json.dumps({d.pasta: d.cor for d in disciplinas})
    corpo = f"""
  <section class="cabecalho inicio">
    <p class="migalhas">1.º semestre 2026/27 · Ciência de Computadores</p>
    <h1>Bom estudo, Gonçalo.</h1>
  </section>

  <section id="painel" data-cores='{esc(cores)}'>
    <form class="desbloquear so-bloqueado" id="desbloquear" autocomplete="on">
      <input type="text" name="username" value="painel" autocomplete="username" hidden>
      <label for="pp">Painel pessoal (agenda, a fazer, avisos)</label>
      <input id="pp" type="password" autocomplete="current-password" placeholder="palavra-passe" required>
      <button type="submit">Abrir</button>
      <p class="erro" id="pp-erro" hidden></p>
    </form>
    <div class="painel-grelha so-desbloqueado">
      <section class="bloco"><h2>Próximos 14 dias <a href="agenda.html">agenda completa →</a></h2><ol id="p-agenda"></ol></section>
      <section class="bloco"><h2>A fazer</h2>
        <div class="rolar"><ul id="p-tarefas"></ul>
          <details hidden><summary>Feitas</summary><ul id="p-feitas"></ul></details></div>
        <form class="nova-tarefa" id="p-nova"><input type="text" placeholder="+ tarefa tua" aria-label="Nova tarefa">
          <input type="date" aria-label="Prazo"><button type="submit">Juntar</button></form></section>
      <section class="bloco"><h2>Chegou esta semana</h2><ul id="p-chegou"></ul></section>
      <section class="bloco"><h2>Avisos recentes <span class="mono" id="p-gerado"></span>
        <a href="#" id="bloquear">bloquear</a></h2><ul id="p-avisos"></ul></section>
    </div>
  </section>

  <h2 class="rotulo">Disciplinas</h2>
  <ol class="indice">
    {"".join(entradas)}
  </ol>

  <section class="faixa">
    <div>
      <h2>Quizrama</h2>
      <p>Perguntas ao estilo do teste, com a correção de cada opção e ligação para a teoria.</p>
      <a class="etiqueta principal" href="quizrama/">Abrir o Quizrama <span class="mono">{n_quizzes} quizzes</span></a>
    </div>
    <div>
      <h2 class="rotulo" style="margin-top:0">Atualizações do site</h2>
      <ul class="novidades">{nov_html}</ul>
    </div>
  </section>
  <script type="module" src="assets/pessoal.js"></script>"""
    return pagina("FCUP · 3.º ano", corpo, "", "disciplinas", larga=True)


def pagina_agenda() -> str:
    corpo = """
  <section class="cabecalho inicio">
    <p class="migalhas"><a href="index.html">Início</a> / Agenda</p>
    <h1>Agenda</h1>
    <p class="meta mono"><span>Testes, entregas e sessões de todas as disciplinas</span></p>
  </section>
  <p class="so-bloqueado suave">A agenda é pessoal: abre o painel na <a href="index.html">página inicial</a> com a palavra-passe.</p>
  <div id="agenda-pagina"></div>
  <script type="module" src="assets/pessoal.js"></script>"""
    return pagina("Agenda — FCUP · 3.º ano", corpo, "", "agenda")


def pagina_estudo() -> str:
    corpo = """
  <div class="estudo-topo">
    <a id="estudo-voltar" href="index.html">Início</a> <span class="suave">/</span> <b id="estudo-titulo">A abrir…</b>
    <button type="button" class="botao" id="estudo-ficha" hidden>← Voltar à ficha</button>
    <div class="modos" id="estudo-modos" role="group" aria-label="O que mostrar" hidden>
      <button type="button" data-modo="pdf" aria-pressed="true">PDF</button>
      <button type="button" data-modo="lado" aria-pressed="false">Lado a lado</button>
      <button type="button" data-modo="sol" aria-pressed="false">Soluções</button>
    </div>
  </div>
  <div class="estudo" data-modo="pdf">
    <iframe id="estudo-esq" title="PDF"></iframe>
    <iframe id="estudo-dir" title="Soluções"></iframe>
  </div>
  <script src="assets/estudo.js" defer></script>"""
    return pagina("Estudo — FCUP · 3.º ano", corpo, "", "disciplinas", larga=True)


def pagina_quizrama(disciplinas) -> str:
    nomes = {d.pasta: d for d in disciplinas}
    blocos = []
    for pasta, qs in QUIZZES.items():
        d = nomes.get(pasta)
        li = "".join(f'<li><a href="../{esc(h)}"><span class="num">Q{i + 1}</span><span class="titulo">{esc(t)}</span>'
                     f'<span class="tipo">{esc(s)}</span></a></li>' for i, (h, t, s) in enumerate(qs))
        blocos.append(f'<section class="seccao" data-cor="{d.cor if d else 0}"><h2>{esc(d.nome if d else pasta)}</h2><ul class="lista">{li}</ul></section>')
    li = "".join(f'<li><a href="../{esc(h)}"><span class="num">—</span><span class="titulo">{esc(t)}</span>'
                 f'<span class="tipo">{esc(s)}</span></a></li>' for h, t, s in QUIZRAMA_EXTRA)
    blocos.append(f'<section class="seccao"><h2>Arquivo <span class="mono">2.º ano</span></h2><ul class="lista">{li}</ul></section>')
    corpo = f"""
  <section class="cabecalho">
    <p class="migalhas"><a href="../index.html">Início</a> / Quizrama</p>
    <h1>Quizrama</h1>
    <p class="meta mono"><span>Perguntas só da matéria do teste, com a correção de todas as opções</span></p>
  </section>
  {"".join(blocos)}"""
    return pagina("Quizrama — FCUP · 3.º ano", corpo, "../", "quizrama")


# barra do site (a mesma das outras páginas) no topo das soluções e do Quizrama
BARRA_SITE = """<style>
.site-topo {{ border-bottom: 1px solid #2c333f; background: #101318; }}
.site-topo > div {{ max-width: 1134px; margin: 0 auto; padding: 16px 24px; display: flex; align-items: baseline; gap: 16px;
  font: 500 0.875rem/1.3 'Avenir Next', Avenir, -apple-system, 'Segoe UI', Roboto, sans-serif; }}
.site-topo a {{ text-decoration: none; color: #9aa2b0; white-space: nowrap; }}
.site-topo a:hover, .site-topo a[aria-current] {{ color: #e4e7ec; }}
.site-topo .marca {{ color: #e4e7ec; font-weight: 700; }}
.site-topo nav {{ display: flex; gap: 16px; margin-left: auto; overflow-x: auto; scrollbar-width: none; }}
</style>
<header class="site-topo"><div><a class="marca" href="{raiz}index.html">FCUP · 3.º ano</a><nav>{nav}</nav></div></header>"""


EMBUTIDO_SOL = """<style>
html.embutido .site-topo, html.embutido .separadores, html.embutido #indice, html.embutido .indice-movel,
html.embutido #abrir-indice, html.embutido aside.lado > h1, html.embutido aside.lado > p,
html.embutido section.disciplina > header.capa .sub { display: none !important; }
html.embutido .mesa { display: block !important; }
</style>
<script>
(function () {  // dentro do estudo.html: só as soluções da ficha; "lê a teoria" troca o PDF ao lado
  var q = new URLSearchParams(location.search);
  if (!q.has("embed")) return;
  document.documentElement.classList.add("embutido");
  var so = q.get("so") || "";
  document.addEventListener("DOMContentLoaded", function () {
    if (so.indexOf("-") < so.length - 1) {
      [].forEach.call(document.querySelectorAll("section.level3"), function (s) {
        var tem = [].some.call(s.querySelectorAll("details.sol"), function (x) { return x.id.indexOf(so) === 0; });
        if (!tem) s.hidden = true;
      });
      [].forEach.call(document.querySelectorAll("section.level2"), function (s) {
        if (!s.querySelector("section.level3:not([hidden])")) s.hidden = true;
      });
    }
  });
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest(".teoria-link a");
    if (a && window.parent !== window) { e.preventDefault(); window.parent.postMessage({ teoria: a.href }, location.origin); }
  });
})();
</script>"""


def com_barra(texto: str, raiz: str, ativo: str) -> str:
    nav = "".join(f'<a href="{raiz}{h}"{" aria-current=\"page\"" if k == ativo else ""}>{t}</a>'
                  for k, h, t in ((k, h or "index.html", t) for k, h, t in NAV))
    barra = BARRA_SITE.format(raiz=raiz, nav=nav)
    return re.sub(r"(<body[^>]*>)", lambda m: m.group(1) + barra, texto, count=1)


TEORIA_CSS = """<style>
.teoria-link { margin: 14px 0 2px; padding-top: 10px; border-top: 1px solid var(--linha);
  font: 500 0.875rem/1.4 var(--ui); color: var(--suave); }
.teoria-link a { color: var(--d); text-decoration: none; font-weight: 600; }
.teoria-link a:hover { text-decoration: underline; text-underline-offset: 3px; }
</style>"""


QUIZ_TEORIA = {}  # disciplina -> {id da pergunta: (href, título)}
TEXTO_SEC = {}  # href da secção -> palavras do texto
SECCOES = defaultdict(list)  # disciplina -> [(href, título)] das secções ## e ### do resumo
VAZIAS = set("como para pelo pela pelos pelas numa num uma dos das nos nas que com sem entre sobre qual quais "
             "porque quando onde este esta isso caracteristica exemplo".split())


def palavras(t: str) -> set:
    import unicodedata
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return {w for w in re.findall(r"[a-z0-9]{3,}", t) if w not in VAZIAS}


ANCORAS = defaultdict(dict)  # disciplina -> {id pandoc do título: (href, título)}


def mapa_teoria(saida: Path, disciplinas) -> dict:
    """id do exercício nas soluções (ex. Redes-F2.2) -> (href, título): a secção do resumo com o
    Pratica agora desse exercício, aberta no PDF na página certa."""
    mapa = {}
    for d in disciplinas:
        pdf = d.dir / f"RESUMO_{d.pasta}.pdf"
        if not pdf.exists():
            continue
        pags = paginas_pdf(pdf)
        secs = seccoes_resumo(d)
        # o índice repete os títulos: começa a procurar depois dele
        principais = [normaliza(t)[:40] for n, t, *_ in secs if n <= 2]
        grupos, caixa = grupos_solucoes(d), 0
        indice = [k for k, pg in enumerate(pags[:10]) if sum(1 for t in principais if t and t in pg) >= 3]
        k = indice[-1] + 1 if indice else 0
        base = ver_href("../", f"{d.pasta}/RESUMO_{d.pasta}.pdf", d.pasta, f"Resumo — {d.nome}")
        atual = None
        for nivel, titulo, corpo, etqs, n_caixas in secs:
            limpo = re.sub(r"^(Aulas?|Tema) [\d–-]+ — ", "", titulo)
            alvo = normaliza(limpo)[:40]
            achada = next((x for x in range(k, len(pags)) if alvo and alvo in pags[x]), None)
            if achada is not None:
                k = achada
            href = f"{base}#p{k + 1}"
            mostra = " ".join(re.sub(r"[*`\\]|\$", "", limpo).split()) + f" (p. {k + 1})"
            ANCORAS[d.pasta].setdefault(ident_pandoc(titulo), (href, mostra))
            if nivel >= 2:
                SECCOES[d.pasta].append((href, mostra))
                TEXTO_SEC[href] = TEXTO_SEC.get(href, set()) | palavras(corpo)
                atual = (href, mostra)
            for _ in range(n_caixas):  # cada alínea da caixa -> esta secção
                for id_ in (grupos[caixa] if caixa < len(grupos) else []):
                    mapa.setdefault(id_, atual or (href, mostra))
                caixa += 1
            for e in etqs:
                mapa.setdefault(f"{d.pasta}-{e}", atual or (href, mostra))
    return mapa


def teoria_do_quiz(disciplina: str) -> dict:
    """id da pergunta no Quizrama (ex. M1.3) -> (href, título) da secção da teoria que o quiz já liga."""
    pasta = ROOT / "Quizrama" / "assets" / "js" / "data" / f"questions-{disciplina.lower()}"
    r = {}
    for f in sorted(pasta.glob("*.js")) if pasta.exists() else []:
        for m in re.finditer(r'\["[^"]*", "([^"]+)", .*?href=\\"[^"#]*#([^\\"]+)\\"[^>]*>(?:📖 )?([^<]*)<', f.read_text()):
            alvo = ANCORAS[disciplina].get(unquote(m.group(2)))
            if alvo:
                r[m.group(1)] = alvo
    return r


def melhor_seccao(disciplina: str, enun: str, corpo: str):
    """Secção do resumo mais parecida com a pergunta (palavras raras pesam mais; o título conta a dobrar)."""
    import math
    secs = SECCOES[disciplina]
    if not secs:
        return None
    df = defaultdict(int)
    for h, _ in secs:
        for w in TEXTO_SEC.get(h, ()):
            df[w] += 1
    idf = lambda w: math.log((len(secs) + 1) / (df[w] + 1)) if df[w] else 0
    e, c = palavras(enun), palavras(corpo)
    def nota(h, t):
        ws = TEXTO_SEC.get(h, set())
        # secções enormes (tabelas-resumo) apanham tudo: divide-se pelo tamanho
        return (sum(idf(w) for w in (e | c) & ws) + 2 * sum(idf(w) for w in e & ws)) / max(len(ws), 1) ** 0.4 \
            + 3 * len(e & palavras(t))
    h, t = max(secs, key=lambda x: nota(*x))
    return (h, t) if nota(h, t) > 0 else None


def com_teoria(texto: str, mapa: dict) -> tuple:
    """No fim de cada solução: "Se a solução não chegou, lê a teoria: <secção do resumo>" (como no Quizrama)."""
    exercicio = {}
    for k, v in mapa.items():  # Redes-Ex.3-a -> também serve Redes-Ex.3
        exercicio.setdefault(k.rsplit("-", 1)[0], v)
    n = 0

    def troca(m):
        nonlocal n
        id_ = m.group(2)
        alvo = None
        ex = id_.split("-", 1)[1].rsplit("-", 1)
        intervalo = re.match(r"(.*?)(\d+)–\d+$", ex[0])
        if intervalo and len(ex) == 2:  # escolha múltipla do teste modelo: a ligação do quiz, se houver
            alvo = QUIZ_TEORIA.setdefault(id_.split("-")[0], teoria_do_quiz(id_.split("-")[0])) \
                .get(f"{intervalo.group(1)}{int(intervalo.group(2)) + int(ex[1]) - 1}")
        if not alvo and "–" in id_.split("-", 1)[1]:
            enun = re.search(r'<span class="enun">(.*?)</span>', m.group(1), re.S)
            corpo = m.group(1)[enun.end():] if enun else m.group(1)
            limpa = lambda x: html.unescape(re.sub(r"<annotation.*?</annotation>|<[^>]+>", " ", x, flags=re.S))
            alvo = melhor_seccao(id_.split("-")[0], limpa(enun.group(1)) if enun else "", limpa(corpo))
        alvo = alvo or mapa.get(id_) or mapa.get(id_.rsplit("-", 1)[0]) or exercicio.get(id_.rsplit("-", 1)[0]) \
            or exercicio.get(id_)
        if not alvo:
            return m.group(0)
        n += 1
        return (f'{m.group(1)}<p class="teoria-link">Se a solução não chegou, lê a teoria: '
                f'<a href="{esc(alvo[0])}">{esc(alvo[1])} →</a></p>{m.group(3)}')
    texto = re.sub(r'(<details class="sol" id="([^"]+)">.*?)(</div></details>)', troca, texto, flags=re.S)
    return texto.replace("</head>", TEORIA_CSS + "\n</head>", 1), n


# --------------------------------------------------------------------------
# Verificação de ligações
# --------------------------------------------------------------------------
def verificar_ligacoes(saida: Path) -> list:
    partidas = []
    for p in saida.rglob("*.html"):
        if "quizrama" in p.relative_to(saida).parts[:1]:
            continue  # o Quizrama tem o seu próprio teste (npm test)
        texto = p.read_text(errors="ignore")
        texto = re.sub(r"<(code|pre)\b.*?</\1>", "", texto, flags=re.S)  # exemplos de HTML no texto
        for ref in re.findall(r'(?:href|src)="([^"]+)"', texto):
            ref = html.unescape(ref)
            u = urlsplit(ref)
            if u.scheme or ref.startswith(("#", "//", "mailto:", "data:")):
                continue
            alvo = (p.parent / unquote(u.path)).resolve() if u.path else p
            if alvo.is_dir():
                alvo = alvo / "index.html"
            if not alvo.exists():
                partidas.append(f"{p.relative_to(saida)} -> {ref}")
                continue
            if alvo.name in ("ver.html", "estudo.html"):
                f = parse_qs(u.query).get("f", [""])[0]
                if not (saida / f).is_file():
                    partidas.append(f"{p.relative_to(saida)} -> ver.html?f={f}")
    return partidas


# --------------------------------------------------------------------------
TITULOS = {}


def main():
    global TITULOS
    ap = argparse.ArgumentParser()
    ap.add_argument("--saida", default=str(ROOT / "_site"))
    ap.add_argument("--lista", action="store_true", help="mostra todos os ficheiros publicados")
    ap.add_argument("--estrito", action="store_true", help="ligações partidas fazem falhar o build")
    args = ap.parse_args()
    saida = Path(args.saida).resolve()
    t0 = time.time()

    TITULOS = {k: v for k, v in json.loads((SITE / "titulos.json").read_text()).items() if not k.startswith("_")}
    if saida.exists():
        shutil.rmtree(saida)
    (saida / "assets").mkdir(parents=True)

    # estilos e scripts
    css = (SITE / "design" / "tokens.css").read_text() + "\n" + (SITE / "design" / "site.css").read_text()
    (saida / "assets" / "site.css").write_text(css)
    for f in ("seccoes.js", "ver.js", "pessoal.js", "estudo.js"):
        shutil.copy(SITE / "design" / f, saida / "assets" / f)
    if (SITE / "pessoal.enc").exists():
        shutil.copy(SITE / "pessoal.enc", saida / "assets" / "pessoal.enc")
    global FICHAS, SOL_DE
    FICHAS = {k: v for k, v in json.loads((SITE / "fichas.json").read_text()).items() if not k.startswith("_")}
    SOL_DE = {p.parent.parent.name for p in ROOT.glob("*/.fonte/SOLUCOES_*.md")}

    disciplinas = descobrir()
    nomes = {d.pasta: d for d in disciplinas}
    publicados = ficheiros_publicados()

    for c in publicados:
        destino = saida / "ficheiros" / c
        destino.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / c, destino)
        partes = c.split("/")
        d = nomes.get(partes[0])
        if not d:
            continue
        if partes[1] == "Teoricas":
            d.teoricas.append(c)
        elif partes[1] == "Praticas" and len(partes) > 3:
            d.praticas[partes[2]].append(c)
        elif partes[1] == "Testes":
            d.testes.append(c)
    for d in disciplinas:
        d.teoricas.sort(key=lambda c: (numero_aula(c) == "—", numero_aula(c), c))

    # documentos de cada disciplina (só PDF; o INFO é pessoal e vai cifrado)
    rastreados = set(git("ls-files").splitlines())
    for d in disciplinas:
        (saida / d.pasta).mkdir(exist_ok=True)
        fontes = sorted((d.dir / ".fonte").glob("*.md"))
        ordem = {"RESUMO": 0, "REVISAO": 1}
        fontes.sort(key=lambda p: (ordem.get(p.stem.split("_")[0], 2), p.stem))
        for md in fontes:
            base = md.stem.split("_")[0]
            if base in ("SOLUCOES", "CONTEXTO", "INFO"):
                continue
            if base in DOCS_NOMES:
                slug = base.lower()
                titulo, desc = DOCS_NOMES[base]
            else:
                slug = md.stem.lower()
                primeiro = re.search(r"^#\s+(.+)$", md.read_text(), re.M)
                titulo = re.sub(r"^title:\s*", "", primeiro.group(1)) if primeiro else md.stem.title()
                titulo = re.sub(r"\s*---.*$", "", titulo)
                desc = "Documento da disciplina."
            pdf = f"{d.pasta}/{md.stem}.pdf"
            if (ROOT / pdf).exists() and pdf in rastreados:
                destino = saida / "ficheiros" / pdf
                destino.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / pdf, destino)
                d.docs.append((slug, titulo, desc, ver_href("../", pdf, d.pasta, titulo)))

    # soluções (o mesmo site, já escuro), com a volta para o início
    tem_sol = (ROOT / "SOLUCOES.html").exists()
    if tem_sol:
        (saida / "solucoes").mkdir()
        sol_html, n_teoria = com_teoria((ROOT / "SOLUCOES.html").read_text(), mapa_teoria(saida, disciplinas))
        sol_html = sol_html.replace("</head>", EMBUTIDO_SOL + "\n</head>", 1)
        (saida / "solucoes" / "index.html").write_text(com_barra(sol_html, "../", "solucoes"))
    sol_de = SOL_DE

    # Quizrama
    q = ROOT / "Quizrama"
    (saida / "quizrama").mkdir()
    for f in q.glob("*.html"):
        (saida / "quizrama" / f.name).write_text(com_barra(f.read_text(), "../", "quizrama"))
    shutil.copytree(q / "assets", saida / "quizrama" / "assets")
    for js in q.glob("*.js"):
        shutil.copy2(js, saida / "quizrama" / js.name)
    # o index.html do Quizrama é o quiz de SO: passa a so.html e o index.html é o hub
    (saida / "quizrama" / "so.html").write_text((saida / "quizrama" / "index.html").read_text())
    global QUIZRAMA_EXTRA
    QUIZRAMA_EXTRA = [(h.replace("quizrama/index.html", "quizrama/so.html"), t, s) for h, t, s in QUIZRAMA_EXTRA]
    (saida / "quizrama" / "index.html").write_text(pagina_quizrama(disciplinas))

    # páginas das disciplinas, visualizador e início
    for d in disciplinas:
        (saida / d.pasta / "index.html").write_text(pagina_disciplina(d, TITULOS, d.pasta in sol_de))
    (saida / "ver.html").write_text(pagina_ver())
    (saida / "estudo.html").write_text(pagina_estudo())
    (saida / "agenda.html").write_text(pagina_agenda())
    nov = novidades(set(publicados), disciplinas)
    n_quizzes = sum(len(v) for v in QUIZZES.values()) + len(QUIZRAMA_EXTRA)
    (saida / "index.html").write_text(pagina_inicio(disciplinas, nov, n_quizzes))
    (saida / ".nojekyll").write_text("")

    partidas = verificar_ligacoes(saida)
    if args.lista:
        print("\n".join(publicados))
    total = sum(p.stat().st_size for p in saida.rglob("*") if p.is_file())
    print(f"Gerado: {saida} ({len(publicados)} ficheiros, {len(disciplinas)} disciplinas, "
          f"{total / 1024 / 1024:.0f} MB, {time.time() - t0:.0f} s)")
    if partidas:
        print(f"{'ERRO' if args.estrito else 'AVISO'}: ligações partidas:\n  " + "\n  ".join(partidas[:30]),
              file=sys.stderr)
        if args.estrito:
            sys.exit(1)


def pagina_ver() -> str:
    corpo = """
  <section class="cabecalho ver-cab">
    <p class="migalhas"><a id="voltar" href="index.html">Disciplinas</a></p>
    <h1 id="ver-titulo">A abrir…</h1>
    <p class="meta mono" id="ver-meta"></p>
  </section>
  <div class="ver-barra">
    <span id="ver-paginas" class="mono"></span>
    <button type="button" id="ver-inverter" hidden>Inverter cores</button>
    <a id="ver-descarregar" class="etiqueta" href="#" download>Descarregar</a>
  </div>
  <div id="ver" class="ver"></div>
  <script type="module" src="assets/ver.js"></script>"""
    return pagina("Ver — FCUP · 3.º ano", corpo, "", "disciplinas")


if __name__ == "__main__":
    main()
