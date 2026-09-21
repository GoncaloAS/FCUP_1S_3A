#!/bin/bash
# Compila RESUMO.md -> RESUMO.pdf para a disciplina passada como argumento.
# Uso: _shared/template/build.sh Compiladores
set -euo pipefail

SUBJECT="$1"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/.."
SUBJECT_DIR="$ROOT/$SUBJECT"
MD="$SUBJECT_DIR/RESUMO_${SUBJECT}.md"
PDF="$SUBJECT_DIR/RESUMO_${SUBJECT}.pdf"
PREAMBLE="$ROOT/_shared/template/preamble.tex"
FILTER="$ROOT/_shared/template/div-envs.lua"

if [ ! -f "$MD" ]; then
  echo "Não encontrei $MD" >&2
  exit 1
fi

pandoc "$MD" \
  -f markdown-implicit_figures \
  --pdf-engine=tectonic \
  -H "$PREAMBLE" \
  --lua-filter "$FILTER" \
  -V lang=pt-PT \
  -V geometry:margin=2.5cm \
  --toc --toc-depth=2 \
  --highlight-style=tango \
  --resource-path="$SUBJECT_DIR" \
  -o "$PDF"

echo "Gerado: $PDF"
