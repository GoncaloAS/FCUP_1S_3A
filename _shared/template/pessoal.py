"""Painel pessoal do site, cifrado (o repositório é público).

Junta agenda, tarefas, o que chegou, avisos e os INFO_<D> num JSON e cifra-o com
AES-256-GCM (chave PBKDF2-SHA256 da palavra-passe) → _shared/site/pessoal.enc.
O site (design/pessoal.js) decifra-o no browser com a mesma palavra-passe.

Palavra-passe: variável FCUP_SITE_PASS ou Keychain do macOS (serviço "fcup-site"):
    security add-generic-password -s fcup-site -a goncalo -w
Correr com: uv run -q --with cryptography python -I _shared/template/pessoal.py
(o `moodle.py fechar` chama-o sozinho).
"""
import base64, hashlib, json, os, re, subprocess, sys
from datetime import date, timedelta

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CFG = os.path.join(ROOT, "_shared", "moodle.json")
SAIDA = os.path.join(ROOT, "_shared", "site", "pessoal.enc")
SAL = os.path.join(ROOT, "_shared", "site", "pessoal.sal")  # público e fixo: a chave guardada no browser continua a servir
ITERACOES = 600_000
NOMES = {"Logica": "Lógica", "TecnologiasWeb": "Tecnologias Web", "IPM": "IPM", "Redes": "Redes", "Compiladores": "Compiladores"}
EVENTO_TAREFA = re.compile(r"entrega|teste|demonstra|defesa|apresenta", re.I)


def disciplinas():
    c = json.load(open(CFG, encoding="utf-8"))
    return [(x["disciplina"], None) for x in c["cursos"]] + [(x["disciplina"], x.get("datas")) for x in c["outras"]]


def seccao(txt, titulo):
    m = re.search(rf"^## {titulo}\s*\n(.*?)(?=^## |\Z)", txt, re.S | re.M)
    return m.group(1) if m else ""


def inline(t):
    """markdown de uma linha -> HTML (negrito, itálico, código, ligações)."""
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    return t


def ident(*partes):
    return hashlib.sha1("|".join(partes).encode()).hexdigest()[:10]


def data_aviso(txt):
    m = re.search(r"(\d{1,2})/(\d{1,2})(?:/(\d{4}))?", txt)
    if not m:
        return ""
    return f"{m.group(3) or date.today().year}-{int(m.group(2)):02d}-{int(m.group(1)):02d}"


def ver_href(D, caminho, titulo):
    from urllib.parse import quote
    return f"ver.html?f={quote('ficheiros/' + D + '/' + caminho)}&d={quote(D)}&t={quote(titulo)}"


def titulo_ficheiro(caminho):
    nome = os.path.splitext(os.path.basename(caminho))[0]
    m = re.match(r"Aula_(\d+)", nome)
    return f"Aula {int(m.group(1))}" if m else nome.replace("_", " ")


def info_html(D, doc):
    p = os.path.join(ROOT, D, ".fonte", f"{doc}.md")
    r = subprocess.run(["pandoc", p, "-f", "markdown", "-t", "html5", "--mathml", "--wrap=none"],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def recolher():
    hoje = date.today()
    agenda, tarefas, avisos, chegou, info, notas = [], [], [], [], {}, {}
    for D, doc in disciplinas():
        doc = doc or f"INFO_{D}"
        p = os.path.join(ROOT, D, ".fonte", f"{doc}.md")
        if not os.path.exists(p):
            continue
        txt = open(p, encoding="utf-8").read()
        for l in seccao(txt, "Datas").splitlines():
            c = [x.strip() for x in l.strip().strip("|").split("|")]
            if len(c) >= 3 and re.fullmatch(r"\d{4}-\d{2}-\d{2}", c[0]):
                ev = {"data": c[0], "hora": c[1], "d": D, "oque": inline(c[2]), "notas": inline(c[3] if len(c) > 3 else "")}
                agenda.append(ev)
                if EVENTO_TAREFA.search(c[2]) and date.fromisoformat(c[0]) >= hoje - timedelta(days=3):
                    tarefas.append({"id": ident(D, c[0], c[2]), "d": D, "prazo": c[0], "texto": inline(c[2]), "origem": "agenda"})
        for l in seccao(txt, "A fazer").splitlines():
            m = re.match(r"\s*- \[( |x)\] (?:(\d{4}-\d{2}-\d{2}) )?(.*)", l)
            if m and m.group(1) == " ":
                tarefas.append({"id": ident(D, m.group(3)), "d": D, "prazo": m.group(2) or "", "texto": inline(m.group(3)), "origem": "aviso"})
        for l in seccao(txt, "Avisos").splitlines():
            if l.startswith("- "):
                avisos.append({"d": D, "data": data_aviso(l[:40]), "html": inline(l[2:])})
        # notas do Gonçalo ("- <componente>: <valor na escala da componente>"; ver design/notas.js)
        for l in seccao(txt, "Notas").splitlines():
            m = re.match(r"\s*- (\w+): ([\d.,]+)", l)
            if m:
                notas.setdefault(D, {})[m.group(1)] = float(m.group(2).replace(",", "."))
        if doc.startswith("INFO_"):
            info[D] = info_html(D, doc)
        # o que o refresh trouxe (registo do moodle.py arrumar)
        reg = os.path.join(ROOT, D, ".fonte", "moodle", "registo.json")
        for r in json.load(open(reg)) if os.path.exists(reg) else []:
            dia = date.fromisoformat(r["data"])
            href = ver_href(D, r["caminho"], titulo_ficheiro(r["caminho"])) if r.get("publico", True) else ""
            if dia >= hoje - timedelta(days=7):
                chegou.append({"data": r["data"], "d": D, "texto": titulo_ficheiro(r["caminho"]), "onde": r["caminho"].split("/")[0], "href": href})
            fichas = r["caminho"].startswith("Praticas/") and r["caminho"].endswith(".pdf") \
                and not re.search(r"solu|respost|resolv", r["caminho"], re.I)
            if fichas and dia >= hoje - timedelta(days=21):
                tarefas.append({"id": ident(D, r["caminho"]), "d": D, "prazo": "", "texto": f"Resolver: {titulo_ficheiro(r['caminho'])}",
                                "origem": "ficha", "href": href})
    # resumos e soluções atualizados (git, últimos 7 dias)
    try:
        log = subprocess.run(["git", "-C", ROOT, "log", "--since=7 days ago", "--name-only", "--format=@%cs"],
                             capture_output=True, text=True).stdout
    except OSError:
        log = ""
    quando, vistos = None, set()
    for l in log.splitlines():
        if l.startswith("@"):
            quando = l[1:]; continue
        m = re.match(r"([^/]+)/\.fonte/(RESUMO|SOLUCOES|REVISAO)_", l)
        if m and (m.group(1), m.group(2)) not in vistos:
            vistos.add((m.group(1), m.group(2)))
            texto = {"RESUMO": "Resumo atualizado", "SOLUCOES": "Soluções novas", "REVISAO": "Revisão atualizada"}[m.group(2)]
            href = "solucoes/#" + m.group(1) if m.group(2) == "SOLUCOES" else \
                ver_href(m.group(1), f"{m.group(2)}_{m.group(1)}.pdf", texto.split()[0])
            chegou.append({"data": quando, "d": m.group(1), "texto": texto, "onde": "Resumo", "href": href})
    return {"gerado": hoje.isoformat(), "nomes": NOMES,
            "agenda": sorted(agenda, key=lambda e: (e["data"], e["hora"])),
            "tarefas": sorted(tarefas, key=lambda t: (t["prazo"] or "9999", t["d"])),
            "avisos": sorted(avisos, key=lambda a: a["data"], reverse=True),
            "chegou": sorted(chegou, key=lambda c: c["data"], reverse=True),
            "info": info, "notas": notas}


def palavra_passe():
    if os.environ.get("FCUP_SITE_PASS"):
        return os.environ["FCUP_SITE_PASS"]
    r = subprocess.run(["security", "find-generic-password", "-s", "fcup-site", "-w"], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def cifrar(dados: dict, pw: str) -> dict:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    if not os.path.exists(SAL):
        open(SAL, "w").write(base64.b64encode(os.urandom(16)).decode())
    sal = base64.b64decode(open(SAL).read())
    chave = hashlib.pbkdf2_hmac("sha256", pw.encode(), sal, ITERACOES, 32)
    iv = os.urandom(12)
    ct = AESGCM(chave).encrypt(iv, json.dumps(dados, ensure_ascii=False).encode(), None)
    b64 = lambda b: base64.b64encode(b).decode()
    return {"v": 1, "sal": b64(sal), "it": ITERACOES, "iv": b64(iv), "ct": b64(ct)}


def main():
    pw = palavra_passe()
    if not pw:
        print("SEM PALAVRA-PASSE: o painel pessoal não foi atualizado. Cria-a uma vez com\n"
              "  security add-generic-password -s fcup-site -a goncalo -w", file=sys.stderr)
        sys.exit(1)
    dados = recolher()
    json.dump(cifrar(dados, pw), open(SAIDA, "w"))
    print(f"pessoal.enc: {len(dados['agenda'])} datas, {len(dados['tarefas'])} tarefas, "
          f"{len(dados['avisos'])} avisos, {len(dados['chegou'])} novidades, {len(dados['info'])} INFO")


if __name__ == "__main__":
    main()
