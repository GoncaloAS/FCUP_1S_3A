#!/bin/bash
# Compila só um documento .fonte/<NOME>.md -> <Disciplina>/<NOME>.pdf (GUIAO_*/TRABALHO_*: Trabalho/), no estilo dos resumos
# (o mesmo que o build.sh faz a todos os "outros documentos", sem refazer o RESUMO).
# Uso: _shared/template/doc.sh Redes INFO_Redes
set -euo pipefail
SUBJECT="$1"; DOC="$2"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SUBJECT_DIR="$ROOT/$SUBJECT"; T="$ROOT/_shared/template"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
pandoc "$SUBJECT_DIR/.fonte/$DOC.md" -f markdown-implicit_figures -s -H "$T/preamble-v2.tex" \
  --lua-filter "$T/div-envs.lua" --lua-filter "$T/auto-align.lua" -V lang=pt-PT \
  -M estilo=v2 -V fontsize=10pt -V "geometry:left=2.2cm,right=2.2cm,top=2.1cm,bottom=2.3cm,headsep=14pt" \
  -V mainfont=Charter -V "sansfont=Avenir Next" -V "mathfont=STIX Two Math" \
  --syntax-highlighting=tango -o "$TMP/$DOC.tex"
tectonic -Z search-path="$SUBJECT_DIR" --keep-logs --outdir "$TMP" "$TMP/$DOC.tex" > "$TMP/out" 2>&1 \
  || { grep -v "^warning:\|^note:" "$TMP/out" >&2; exit 1; }
grep -q "Missing character" "$TMP/$DOC.log" && echo "AVISO ($DOC): caracteres sem glifo" >&2
DEST="$SUBJECT_DIR"; case "$DOC" in GUIAO_*|TRABALHO_*) DEST="$SUBJECT_DIR/Trabalho"; mkdir -p "$DEST" ;; esac
cp "$TMP/$DOC.pdf" "$DEST/$DOC.pdf"
echo "Gerado: ${DEST#$ROOT/}/$DOC.pdf"
