#!/usr/bin/env python3
"""
Gera guia_redes_teste1.html (matéria do 1.º teste de Redes) a partir do resumo
cumulativo (../Redes/.fonte/RESUMO_Redes.md, no mesmo repositório).

- tira as caixas "pratica" (exercícios das fichas; não são matéria);
- converte as figuras PDF para SVG em assets/guia-redes/;
- o pandoc dá um id a cada título (é para esses ids que apontam as dicas do quiz);
- grava a lista de ids em assets/guia-redes/ids.json (usada pelo gerador de perguntas e pelo smoke test);
- gera também guia_redes_teste1.pdf e guia_redes_teste2.pdf (este a partir do guia2.md), com o estilo do resumo, para o site.

Uso: python3 tools/redes-guide/build.py [caminho/para/Redes]
"""
import json, re, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REDES = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / "Redes"   # o Quizrama vive dentro do repositório da universidade
SRC = REDES / ".fonte" / "RESUMO_Redes.md"
OUTDIR = ROOT / "assets" / "guia-redes"
OUT = ROOT / "guia_redes_teste1.html"
OUTDIR.mkdir(parents=True, exist_ok=True)

md = SRC.read_text()
frente = re.match(r"^---\n.*?\n---\n", md, flags=re.S)
md = re.sub(r"^---\n.*?\n---\n", "", md, count=1, flags=re.S)          # front matter (o título vem do template)
md = re.sub(r"<!--.*?-->\n?", "", md, flags=re.S)

# caixas pratica: de "::: {.pratica" até ao ":::" que a fecha
out, skip = [], False
for line in md.splitlines():
    if line.startswith("::: {.pratica"):
        skip = True; continue
    if skip:
        if line.strip() == ":::": skip = False
        continue
    out.append(line)
md = "\n".join(out)
md = md.replace("práticas.*", "práticas. Os exercícios estão no resumo em PDF e no site de soluções.*", 1)

md_pdf = md  # o PDF usa as figuras PDF originais

def fig(stem):
    pdf = REDES / "figuras" / (stem + ".pdf")
    svg = OUTDIR / (pdf.stem + ".svg")
    if not svg.exists() or svg.stat().st_mtime < pdf.stat().st_mtime:
        subprocess.run(["pdftocairo", "-svg", str(pdf), str(svg)], check=True)
    return f"assets/guia-redes/{svg.name}"
md = re.sub(r"figuras/([\w-]+)\.pdf", lambda m: fig(m.group(1)), md)
md = re.sub(r"\{width=\d+%\}", "", md)

tmp = OUTDIR / "_guia.md"
tmp.write_text(md)
subprocess.run(["pandoc", str(tmp), "-f", "markdown", "-t", "html5", "-s", "--toc", "--toc-depth=3",
                "--math-method=mathml", "--template", str(Path(__file__).with_name("template.html")),
                "--metadata", "title=Redes de Comunicação — matéria dos testes (Caps. 1–4)",
                "-o", str(OUT)], check=True)
tmp.unlink()

html = OUT.read_text()
ids = re.findall(r'<h[1-3] id="([^"]+)"', html)
(OUTDIR / "ids.json").write_text(json.dumps(ids, ensure_ascii=False, indent=1))
print(f"{OUT.name}: {len(ids)} secções com id")

# PDFs: o pipeline do resumo (preamble-v2, filtros, tectonic)
TPL = REDES.parent / "_shared" / "template"

def pdf(fonte, nome):
    tmpd = Path(tempfile.mkdtemp())
    (tmpd / "guia.md").write_text(fonte)
    subprocess.run(["pandoc", str(tmpd / "guia.md"), "-f", "markdown-implicit_figures", "-s",
                    "-H", str(TPL / "preamble-v2.tex"),
                    "--lua-filter", str(TPL / "div-envs.lua"), "--lua-filter", str(TPL / "auto-align.lua"),
                    "-V", "lang=pt-PT", "-M", "estilo=v2", "-V", "fontsize=10pt",
                    "-V", "geometry:left=2.2cm,right=2.2cm,top=2.1cm,bottom=2.3cm,headsep=14pt",
                    "-V", "mainfont=Charter", "-V", "sansfont=Avenir Next", "-V", "mathfont=STIX Two Math",
                    "--toc", "--toc-depth=2", "--syntax-highlighting=tango", "-o", str(tmpd / "guia.tex")],
                   check=True, cwd=str(REDES))
    r = subprocess.run(["tectonic", "-Z", f"search-path={REDES}", "--keep-logs", "--outdir", str(tmpd), str(tmpd / "guia.tex")],
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"Erro no PDF {nome}:\n" + r.stderr[-2000:])
    log = (tmpd / "guia.log").read_text(errors="replace")
    for aviso in re.findall(r"Missing character.*|Overfull \\hbox \((?:[2-9]\d|\d{3,})\..*", log):
        print(f"AVISO ({nome}): {aviso}")
    shutil.copy(tmpd / "guia.pdf", ROOT / nome)
    shutil.rmtree(tmpd)
    print(f"{nome} gerado")

# 1.º teste: o mesmo texto do guia HTML, com as figuras PDF originais
cab = re.sub(r'title:.*', 'title: "Redes de Comunicação --- matéria dos testes (Caps. 1--4)"', frente.group(0)) if frente else ""
pdf(cab + md_pdf, "guia_redes_teste1.pdf")
# 2.º teste: guia curto, escrito à parte (guia2.md), em linguagem simples
pdf(Path(__file__).with_name("guia2.md").read_text(), "guia_redes_teste2.pdf")
