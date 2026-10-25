"""Refresh semanal do Moodle (skill moodle-refresh).

Correr sempre com:  uv run -q --with reportlab --with pillow python -I _shared/template/moodle.py <cmd>

  js            imprime ref/extrair.js + ref/inventario.js (este com CURSOS e CONHECIDOS preenchidos): colar tal e qual no javascript_tool
  arrumar       abre ~/Downloads/moodle__lote_*.zip; cada moodle__<D>__<destino> -> <D>/<destino>; .md -> PDF (ReportLab) com a fonte em
                <D>/.fonte/moodle/; .zip -> pasta; estado -> .fonte/moodle/estado.novo.json. Nunca sobrescreve:
                se o destino existe, grava <nome>.novo.<ext> e avisa (usar --substituir quando é uma versão nova)
  pdf F.md F.pdf  volta a gerar um PDF a partir de um .md (depois de corrigir o .md à mão)
  fechar        aplica os estados novos, gera INFO_<D>.pdf (pandoc, estilo dos resumos), a AGENDA.pdf
                e o painel pessoal cifrado do site (_shared/site/pessoal.enc, ver pessoal.py)
  agenda        só a AGENDA.pdf (raiz): junta as tabelas "## Datas" dos .fonte/INFO_<D>.md
"""
import json, os, re, shutil, subprocess, sys, zipfile
from datetime import date

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CFG = os.path.join(ROOT, "_shared", "moodle.json")
SKILL_JS = os.path.join(ROOT, ".claude", "skills", "moodle-refresh", "ref", "inventario.js")
DL = os.path.expanduser("~/Downloads")
FONTS = os.path.join(os.path.dirname(__file__), "fonts")


def cursos():
    return json.load(open(CFG, encoding="utf-8"))["cursos"]


def estado_path(D, novo=False):
    return os.path.join(ROOT, D, ".fonte", "moodle", "estado.novo.json" if novo else "estado.json")


# ------------------------------------------------------------------ js
def cmd_js():
    cs = cursos()
    conh = {}
    for c in cs:
        p = estado_path(c["disciplina"])
        conh[c["disciplina"]] = json.load(open(p)) if os.path.exists(p) else {}
    js = open(SKILL_JS, encoding="utf-8").read()
    js = js.replace("const CURSOS = [];", "const CURSOS = " + json.dumps([[c["id"], c["disciplina"]] for c in cs]) + ";", 1)
    js = js.replace("const CONHECIDOS = {};", "const CONHECIDOS = " + json.dumps(conh, separators=(",", ":")) + ";", 1)
    ex = open(os.path.join(os.path.dirname(SKILL_JS), "extrair.js"), encoding="utf-8").read()
    js = "\n".join(l for l in (ex + "\n" + js).splitlines() if not l.lstrip().startswith("//"))  # menos texto a colar
    print("{\n" + js + "\n}")  # bloco: pode correr-se duas vezes na mesma página sem "already declared"


# ------------------------------------------------------------------ PDF a partir de markdown (estilo das fichas)
def _rl():
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib.fonts import addMapping
    for n in ["DejaVuSans", "DejaVuSans-Bold", "DejaVuSans-Oblique", "DejaVuSans-BoldOblique", "DejaVuSansMono", "DejaVuSansMono-Bold"]:
        pdfmetrics.registerFont(TTFont(n, os.path.join(FONTS, n + ".ttf")))
    addMapping("DejaVuSans", 0, 0, "DejaVuSans"); addMapping("DejaVuSans", 1, 0, "DejaVuSans-Bold")
    addMapping("DejaVuSans", 0, 1, "DejaVuSans-Oblique"); addMapping("DejaVuSans", 1, 1, "DejaVuSans-BoldOblique")
    addMapping("DejaVuSansMono", 0, 0, "DejaVuSansMono"); addMapping("DejaVuSansMono", 1, 0, "DejaVuSansMono-Bold")
    addMapping("DejaVuSansMono", 0, 1, "DejaVuSansMono"); addMapping("DejaVuSansMono", 1, 1, "DejaVuSansMono-Bold")


def _estilos():
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.enums import TA_CENTER
    from reportlab.lib import colors
    base = dict(fontName="DejaVuSans", fontSize=9.5, leading=13)
    return {
        "title": ParagraphStyle("t", fontName="DejaVuSans-Bold", fontSize=15, leading=19, alignment=TA_CENTER, spaceAfter=2),
        "sub": ParagraphStyle("s", fontName="DejaVuSans-Oblique", fontSize=8.5, leading=11, alignment=TA_CENTER,
                              textColor=colors.grey, spaceAfter=12),
        "h2": ParagraphStyle("h2", fontName="DejaVuSans-Bold", fontSize=12, leading=15, spaceBefore=10, spaceAfter=4),
        "h3": ParagraphStyle("h3", fontName="DejaVuSans-Bold", fontSize=10.5, leading=13, spaceBefore=7, spaceAfter=3),
        "p": ParagraphStyle("p", spaceAfter=5, **base),
        "cap": ParagraphStyle("c", fontName="DejaVuSans", fontSize=8.5, leading=11, alignment=TA_CENTER, spaceAfter=6),
        "code": ParagraphStyle("code", fontName="DejaVuSansMono", fontSize=7.6, leading=9.4, leftIndent=8,
                               backColor=colors.Color(.95, .95, .95), borderPadding=5, spaceBefore=4, spaceAfter=8),
        "cell": ParagraphStyle("cell", fontName="DejaVuSans", fontSize=7.8, leading=9.6),
        "cellb": ParagraphStyle("cellb", fontName="DejaVuSans-Bold", fontSize=7.8, leading=9.6),
        "li": lambda nivel, marca: ParagraphStyle(f"li{nivel}", spaceAfter=3, leftIndent=16 + 18 * nivel,
                                                  firstLineIndent=-(6 + 6 * len(marca)), **base),
    }


def inl(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\\|", "|")
    t = re.sub(r"`([^`]+)`", r'<font face="DejaVuSansMono" size="8.8">\1</font>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"\^(.+?)\^", r"<super>\1</super>", t)
    t = re.sub(r"\[([^\]]*)\]\((https?://[^)]+)\)", r'<link href="\2" color="#1a4f9c">\1</link>', t)
    t = re.sub(r"\[([^\]]*)\]\((/[^)]*)\)", r'<link href="https://moodle2627.up.pt\2" color="#1a4f9c">\1</link>', t)
    t = re.sub(r"\[([^\]]*)\]\(\)", r"\1", t)
    return t


LI = re.compile(r"^( *)(-|\d+\.|[a-z]\)|[ivx]+\)) +(.*)$")


def md_pdf(md_path, pdf_path):
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted, Image, Table, TableStyle, KeepTogether
    _rl(); S = _estilos()
    base = os.path.dirname(os.path.abspath(md_path))
    L = open(md_path, encoding="utf-8").read().splitlines()
    out, titulo, i = [], os.path.basename(pdf_path), 0
    largura = A4[0] - 4 * cm
    para = []

    def fecha():
        if para:
            out.append(Paragraph(inl("<br/>".join(para)).replace("&lt;br/&gt;", "<br/>"), S["p"])); para.clear()

    while i < len(L):
        l = L[i]; s = l.strip()
        if s.startswith("```"):
            fecha(); j = i + 1; ind = len(l) - len(l.lstrip())
            while j < len(L) and not L[j].strip().startswith("```"): j += 1
            out.append(Preformatted("\n".join(x[ind:] if x[:ind].strip() == "" else x for x in L[i + 1:j]), S["code"])); i = j + 1; continue
        if not s: fecha(); i += 1; continue
        if s.startswith("# ") and not out:
            titulo = s[2:]; out.append(Paragraph(inl(titulo), S["title"]))
            if i + 2 < len(L) and L[i + 2].startswith("*"):
                out.append(Paragraph(inl(L[i + 2].strip("* ")), S["sub"])); i += 3; continue
            i += 1; continue
        m = re.match(r"^(#{2,6}) (.*)", s)
        if m: fecha(); out.append(Paragraph(inl(m.group(2)), S["h2" if len(m.group(1)) == 2 else "h3"])); i += 1; continue
        m = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", s)
        if m:
            fecha(); p = os.path.join(base, m.group(2))
            if os.path.exists(p):
                img = Image(p); w = min(largura * .85, img.imageWidth * .75)
                img.drawHeight = img.imageHeight * w / img.imageWidth; img.drawWidth = w
                out.append(KeepTogether([Spacer(1, 4), img, Spacer(1, 4)]))
            if m.group(1): out.append(Paragraph(inl(m.group(1)), S["cap"]))
            i += 1; continue
        if s.startswith("|"):
            fecha(); rows = []
            while i < len(L) and L[i].strip().startswith("|"):
                c = [x.strip() for x in re.split(r"(?<!\\)\|", L[i].strip())[1:-1]]
                if not all(re.fullmatch(r":?-{2,}:?", x) for x in c if x): rows.append(c)
                i += 1
            n = max(len(r) for r in rows); rows = [r + [""] * (n - len(r)) for r in rows]
            data = [[Paragraph(inl(x), S["cellb" if k == 0 else "cell"]) for x in r] for k, r in enumerate(rows)]
            t = Table(data, colWidths=[largura / n] * n, repeatRows=1)
            t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), .4, colors.grey), ("BACKGROUND", (0, 0), (-1, 0), colors.Color(.9, .9, .9)),
                                   ("VALIGN", (0, 0), (-1, -1), "TOP")]))
            out += [Spacer(1, 3), t, Spacer(1, 6)]; continue
        m = LI.match(l)
        if m:
            fecha(); nivel = len(m.group(1)) // 3; marca = "•" if m.group(2) == "-" else m.group(2)
            txt = [m.group(3)]; i += 1
            while i < len(L) and L[i].strip() and not LI.match(L[i]) and not L[i].strip().startswith(("```", "|", "#", "![")) \
                    and len(L[i]) - len(L[i].lstrip()) > len(m.group(1)):
                txt.append(L[i].strip()); i += 1
            out.append(Paragraph(f"{marca}&nbsp;&nbsp;" + inl("<br/>".join(txt)).replace("&lt;br/&gt;", "<br/>"), S["li"](nivel, marca)))
            continue
        para.append(s); i += 1
    fecha()
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    SimpleDocTemplate(pdf_path, pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm, topMargin=1.8 * cm, bottomMargin=1.8 * cm,
                      title=titulo, author="Moodle FCUP").build(out)


# ------------------------------------------------------------------ arrumar
def regista(D, caminho):
    """O que o refresh trouxe (para o "Chegou esta semana" e as fichas por resolver do painel)."""
    if ".novo." in caminho or caminho.startswith(".fonte/"): return
    p = os.path.join(ROOT, D, ".fonte", "moodle", "registo.json")
    reg = json.load(open(p)) if os.path.exists(p) else []
    reg = [r for r in reg if r["caminho"] != caminho]
    ignorado = subprocess.run(["git", "-C", ROOT, "check-ignore", "-q", f"{D}/{caminho}"]).returncode == 0
    publico = caminho.split("/")[0] in ("Teoricas", "Praticas", "Testes", "Trabalho") and not ignorado
    reg.append({"data": date.today().isoformat(), "caminho": caminho, "publico": publico})
    os.makedirs(os.path.dirname(p), exist_ok=True); json.dump(reg, open(p, "w"), ensure_ascii=False, indent=1)


def cmd_arrumar(substituir=False):
    for f in sorted(os.listdir(DL)):  # lotes (um .zip por refresh) -> ficheiros soltos moodle__*
        if f.startswith("moodle__lote") and f.endswith(".zip"):
            with zipfile.ZipFile(os.path.join(DL, f)) as z:
                for m in z.namelist():
                    if m.startswith("moodle__") and "/" not in m: z.extract(m, DL)
            os.remove(os.path.join(DL, f)); print(f"lote {f}: aberto")
    nomes = sorted(f for f in os.listdir(DL) if f.startswith("moodle__") and not f.endswith((".crdownload", ".download")))
    if not nomes: print("Nada em ~/Downloads com o prefixo moodle__."); return
    disc = {c["disciplina"] for c in cursos()}
    mds = []
    for f in nomes:
        src = os.path.join(DL, f); partes = f.split("__", 2)
        if partes[1] == "estado":
            D = partes[2].removesuffix(".json")
            os.makedirs(os.path.dirname(estado_path(D)), exist_ok=True)
            shutil.move(src, estado_path(D, novo=True)); print(f"estado {D}: guardado (aplica-se no fechar)"); continue
        D, rel = partes[1], partes[2].replace("~", "/")
        if D not in disc or ".." in rel.split("/"): print(f"IGNORADO (nome inválido): {f}"); continue
        dest = os.path.join(ROOT, D, rel)
        if rel.endswith(".md") and not rel.startswith(".fonte/"):
            fonte = os.path.join(ROOT, D, ".fonte", "moodle", os.path.basename(rel))
            os.makedirs(os.path.dirname(fonte), exist_ok=True); shutil.move(src, fonte)
            mds.append((fonte, os.path.join(ROOT, D, rel[:-3] + ".pdf"))); continue
        if os.path.exists(dest) and not substituir:
            b, e = os.path.splitext(dest); dest = f"{b}.novo{e}"; print(f"JÁ EXISTE {D}/{rel}: gravado como {os.path.relpath(dest, ROOT)}")
        os.makedirs(os.path.dirname(dest), exist_ok=True); shutil.move(src, dest)
        if dest.endswith(".zip"):
            pasta = dest[:-4]
            with zipfile.ZipFile(dest) as z:
                for m in z.namelist():
                    if m.startswith("/") or ".." in m.split("/") or m.startswith("__MACOSX") or m.endswith(".DS_Store"): continue
                    z.extract(m, pasta)
            os.remove(dest)
            dentro = os.listdir(pasta)  # zip com uma só pasta lá dentro (x.zip -> x/x/...): sobe um nível
            if len(dentro) == 1 and os.path.isdir(os.path.join(pasta, dentro[0])):
                os.rename(os.path.join(pasta, dentro[0]), pasta + ".tmp"); os.rmdir(pasta); os.rename(pasta + ".tmp", pasta)
            print(f"{D}/{rel} → pasta {os.path.relpath(pasta, ROOT)}/ ({len(os.listdir(pasta))} entradas)")
            regista(D, os.path.relpath(pasta, os.path.join(ROOT, D)))
        else:
            print(f"{os.path.relpath(dest, ROOT)}  ({os.path.getsize(dest) // 1024}KB)")
            regista(D, os.path.relpath(dest, os.path.join(ROOT, D)))
    for fonte, pdf in mds:
        if os.path.exists(pdf) and not substituir:
            b, e = os.path.splitext(pdf); pdf = f"{b}.novo{e}"; print(f"JÁ EXISTE: PDF gravado como {os.path.relpath(pdf, ROOT)}")
        md_pdf(fonte, pdf)
        regista(os.path.relpath(pdf, ROOT).split("/")[0], os.path.relpath(pdf, ROOT).split("/", 1)[1])
        n = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
        pags = re.search(r"Pages:\s+(\d+)", n)
        print(f"{os.path.relpath(pdf, ROOT)}  ({pags.group(1) if pags else '?'} pág.; fonte {os.path.relpath(fonte, ROOT)})")


# ------------------------------------------------------------------ agenda
def linhas_datas(D, doc=None):
    p = os.path.join(ROOT, D, ".fonte", f"{doc or 'INFO_' + D}.md")
    if not os.path.exists(p): return []
    txt = open(p, encoding="utf-8").read()
    m = re.search(r"^## Datas\s*\n(.*?)(?=^## |\Z)", txt, re.S | re.M)
    if not m: return []
    out = []
    for l in m.group(1).splitlines():
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) >= 3 and re.fullmatch(r"\d{4}-\d{2}-\d{2}", c[0]):
            out.append((c[0], D, c[1], c[2], c[3] if len(c) > 3 else ""))
    return out


def cmd_agenda():
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
    _rl(); S = _estilos()
    ev = sorted(e for c in cursos() + json.load(open(CFG))["outras"] for e in linhas_datas(c["disciplina"], c.get("datas")))
    hoje = date.today().isoformat()
    dias = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
    fmt = lambda d: f"{dias[date.fromisoformat(d).weekday()]} {d[8:]}/{d[5:7]}"
    out = [Paragraph("Agenda — 3.º ano, 1.º semestre", S["title"]),
           Paragraph(f"Gerada a {date.today():%d/%m/%Y} a partir do Moodle (INFO_&lt;D&gt;.pdf de cada disciplina)", S["sub"])]
    for titulo, sel in [("Próximas", [e for e in ev if e[0] >= hoje]), ("Já passaram", [e for e in ev if e[0] < hoje])]:
        if not sel: continue
        out.append(Paragraph(titulo, S["h2"]))
        nome = {"Logica": "Lógica", "TecnologiasWeb": "Tec. Web"}
        rows = [["Data", "Hora", "Disciplina", "O quê", "Notas"]] + [[fmt(d), h, nome.get(D, D), o, n] for d, D, h, o, n in sel]
        t = Table([[Paragraph(inl(x), S["cellb" if k == 0 else "cell"]) for x in r] for k, r in enumerate(rows)],
                  colWidths=[c * cm for c in (1.9, 2.1, 2.4, 5.1, 5.5)], repeatRows=1)
        st = [("GRID", (0, 0), (-1, -1), .4, colors.grey), ("BACKGROUND", (0, 0), (-1, 0), colors.Color(.9, .9, .9)), ("VALIGN", (0, 0), (-1, -1), "TOP")]
        if titulo == "Já passaram": st.append(("TEXTCOLOR", (0, 1), (-1, -1), colors.grey))
        t.setStyle(TableStyle(st)); out += [t, Spacer(1, 8)]
    SimpleDocTemplate(os.path.join(ROOT, "AGENDA.pdf"), pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm, topMargin=1.8 * cm,
                      bottomMargin=1.8 * cm, title="Agenda").build(out)
    print(f"AGENDA.pdf: {len(ev)} datas ({sum(e[0] >= hoje for e in ev)} por vir)")


# ------------------------------------------------------------------ fechar
def cmd_fechar():
    for c in cursos():
        D = c["disciplina"]; n = estado_path(D, novo=True)
        if os.path.exists(n): os.replace(n, estado_path(D)); print(f"estado {D}: aplicado")
        if os.path.exists(os.path.join(ROOT, D, ".fonte", f"INFO_{D}.md")):
            r = subprocess.run(["bash", os.path.join(ROOT, "_shared", "template", "doc.sh"), D, f"INFO_{D}"], capture_output=True, text=True)
            print((r.stdout + r.stderr).strip())
    cmd_agenda()
    r = subprocess.run(["uv", "run", "-q", "--with", "cryptography", "python", "-I",
                        os.path.join(ROOT, "_shared", "template", "pessoal.py")], capture_output=True, text=True)
    print((r.stdout + r.stderr).strip())
    resto = [f for f in os.listdir(DL) if f.startswith("moodle__")]
    if resto: print("AINDA EM ~/Downloads (correr arrumar):", ", ".join(resto))


if __name__ == "__main__":
    a = sys.argv[1:] or ["-h"]
    if a[0] == "js": cmd_js()
    elif a[0] == "arrumar": cmd_arrumar("--substituir" in a)
    elif a[0] == "pdf": md_pdf(a[1], a[2]); print("ok", a[2])
    elif a[0] == "fechar": cmd_fechar()
    elif a[0] == "agenda": cmd_agenda()
    else: print(__doc__)
