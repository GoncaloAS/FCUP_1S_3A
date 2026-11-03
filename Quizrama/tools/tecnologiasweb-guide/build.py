#!/usr/bin/env python3
"""
Gera guia_tw_teste1.html (matéria do 1.º teste de Tecnologias Web) a partir do resumo cumulativo
(../TecnologiasWeb/.fonte/RESUMO_TecnologiasWeb.md) e do enunciado do trabalho (TRABALHO_Alquerque.md).

Matéria (aviso do professor no Slack): as linguagens do cliente — HTML, CSS e JavaScript — e a 1.ª fase
do trabalho. No resumo são os Temas 2 a 6 (aulas 3–11); do trabalho entram as regras e a 1.ª entrega (§1–2).

- o pandoc dá um id a cada título (é para esses ids que apontam as dicas do quiz);
- grava a lista de ids em assets/guia-tw/ids.json;
- converte as figuras PDF para SVG em assets/guia-tw/;
- gera também guia_tw_teste1.pdf, com o estilo do resumo (preamble-v2, tectonic), para o site.

Uso: python3 tools/tecnologiasweb-guide/build.py
"""
import json, re, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TW = ROOT.parent / "TecnologiasWeb"
OUTDIR = ROOT / "assets" / "guia-tw"
OUT = ROOT / "guia_tw_teste1.html"
OUTDIR.mkdir(parents=True, exist_ok=True)
TITULO = "Tecnologias Web — matéria do 1.º teste"

res = (TW / ".fonte" / "RESUMO_TecnologiasWeb.md").read_text()
ini, fim = res.index("\n# Tema 2 ---"), res.index("\n# Tema 7 ---")
md = res[ini:fim]
md = re.sub(r"<!--.*?-->\n?", "", md, flags=re.S)

trab = (TW / ".fonte" / "TRABALHO_Alquerque.md").read_text()
macros = re.search(r"```\{=latex\}\n\\newcommand.*?```\n", trab, re.S).group(0)
t_ini, t_fim = trab.index("\n## 1. Regras do Alquerque"), trab.index("\n## 3. Como submeter")
trab = "\n# Trabalho prático --- 1.ª entrega (Alquerque)\n" + trab[t_ini:t_fim]
trab = trab.replace("(ver §4)", "").replace("(abaixo)", "")

md_pdf = "*O sinal † marca matéria que não está nos slides mas faz falta para as práticas.*\n" + md + "\n" + macros + trab
trab_html = re.sub(r"```\{=latex\}\n.*?```\n", "", trab, flags=re.S)   # os diagramas TikZ só existem no PDF
md = "*O sinal † marca matéria que não está nos slides mas faz falta para as práticas.*\n" + md + "\n" + trab_html

def fig(stem):
    pdf = TW / "figuras" / (stem + ".pdf")
    svg = OUTDIR / (pdf.stem + ".svg")
    if not svg.exists() or svg.stat().st_mtime < pdf.stat().st_mtime:
        subprocess.run(["pdftocairo", "-svg", str(pdf), str(svg)], check=True)
    return f"assets/guia-tw/{svg.name}"
md = re.sub(r"figuras/([\w-]+)\.pdf", lambda m: fig(m.group(1)), md)
md = re.sub(r"\{width=\d+%\}", "", md)

tmp = OUTDIR / "_guia.md"
tmp.write_text(md)
subprocess.run(["pandoc", str(tmp), "-f", "markdown", "-t", "html5", "-s", "--toc", "--toc-depth=2",
                "--math-method=mathml", "--template", str(Path(__file__).with_name("template.html")),
                "--metadata", f"title={TITULO}", "-o", str(OUT)], check=True)
tmp.unlink()

html = OUT.read_text()
ids = re.findall(r'<h[1-3] id="([^"]+)"', html)
(OUTDIR / "ids.json").write_text(json.dumps(ids, ensure_ascii=False, indent=1))
print(f"{OUT.name}: {len(ids)} secções com id")

TPL = ROOT.parent / "_shared" / "template"
cab = f'---\ntitle: "{TITULO.replace("—", "---")}"\nauthor: "Gonçalo Sousa"\n---\n'
tmpd = Path(tempfile.mkdtemp())
(tmpd / "guia.md").write_text(cab + md_pdf)
subprocess.run(["pandoc", str(tmpd / "guia.md"), "-f", "markdown-implicit_figures", "-s",
                "-H", str(TPL / "preamble-v2.tex"),
                "--lua-filter", str(TPL / "div-envs.lua"), "--lua-filter", str(TPL / "auto-align.lua"),
                "-V", "lang=pt-PT", "-M", "estilo=v2", "-V", "fontsize=10pt",
                "-V", "geometry:left=2.2cm,right=2.2cm,top=2.1cm,bottom=2.3cm,headsep=14pt",
                "-V", "mainfont=Charter", "-V", "sansfont=Avenir Next", "-V", "mathfont=STIX Two Math",
                "--toc", "--toc-depth=2", "--syntax-highlighting=tango", "-o", str(tmpd / "guia.tex")],
               check=True, cwd=str(TW))
r = subprocess.run(["tectonic", "-Z", f"search-path={TW}", "--keep-logs", "--outdir", str(tmpd), str(tmpd / "guia.tex")],
                   capture_output=True, text=True)
if r.returncode != 0:
    sys.exit("Erro no PDF do guia:\n" + r.stderr[-2000:])
shutil.copy(tmpd / "guia.pdf", ROOT / "guia_tw_teste1.pdf")
shutil.rmtree(tmpd)
print("guia_tw_teste1.pdf gerado")
