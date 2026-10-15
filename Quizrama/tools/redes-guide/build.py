#!/usr/bin/env python3
"""
Gera guia_redes_teste1.html (matéria do 1.º teste de Redes) a partir do resumo
cumulativo (../Redes/.fonte/RESUMO_Redes.md, no mesmo repositório).

- tira as caixas "pratica" (exercícios das fichas; não são matéria);
- converte as figuras PDF para SVG em assets/guia-redes/;
- o pandoc dá um id a cada título (é para esses ids que apontam as dicas do quiz);
- grava a lista de ids em assets/guia-redes/ids.json (usada pelo gerador de perguntas e pelo smoke test).

Uso: python3 tools/redes-guide/build.py [caminho/para/Redes]
"""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REDES = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / "Redes"   # o Quizrama vive dentro do repositório da universidade
SRC = REDES / ".fonte" / "RESUMO_Redes.md"
OUTDIR = ROOT / "assets" / "guia-redes"
OUT = ROOT / "guia_redes_teste1.html"
OUTDIR.mkdir(parents=True, exist_ok=True)

md = SRC.read_text()
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
                "--metadata", "title=Redes de Comunicação — matéria do 1.º teste",
                "-o", str(OUT)], check=True)
tmp.unlink()

html = OUT.read_text()
ids = re.findall(r'<h[1-3] id="([^"]+)"', html)
(OUTDIR / "ids.json").write_text(json.dumps(ids, ensure_ascii=False, indent=1))
print(f"{OUT.name}: {len(ids)} secções com id")
