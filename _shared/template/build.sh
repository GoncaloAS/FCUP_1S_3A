#!/bin/bash
# Compila RESUMO.md -> RESUMO.pdf para a disciplina passada como argumento.
# Uso: _shared/template/build.sh Compiladores
set -euo pipefail

SUBJECT="$1"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/.."
SUBJECT_DIR="$ROOT/$SUBJECT"
MD="$SUBJECT_DIR/.fonte/RESUMO_${SUBJECT}.md"
PDF="$SUBJECT_DIR/RESUMO_${SUBJECT}.pdf"
PREAMBLE="$ROOT/_shared/template/preamble.tex"
FILTER="$ROOT/_shared/template/div-envs.lua"

if [ ! -f "$MD" ]; then
  echo "Não encontrei $MD" >&2
  exit 1
fi

SOL_MD="$SUBJECT_DIR/.fonte/SOLUCOES_${SUBJECT}.md"
SOL_HTML="$SUBJECT_DIR/SOLUCOES_${SUBJECT}.html"
# As caixas "Pratica agora" do PDF apontam para o ficheiro de soluções, se existir.
SOL_META=()
[ -f "$SOL_MD" ] && SOL_META=(-M "solucoes=SOLUCOES_${SUBJECT}.html")

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
TEX="$TMP/RESUMO_${SUBJECT}.tex"

pandoc "$MD" \
  -f markdown-implicit_figures \
  -s \
  -H "$PREAMBLE" \
  --lua-filter "$FILTER" \
  --lua-filter "$ROOT/_shared/template/auto-align.lua" \
  -V lang=pt-PT \
  -V geometry:margin=2.5cm \
  --toc --toc-depth=2 \
  --syntax-highlighting=tango \
  ${SOL_META[@]+"${SOL_META[@]}"} \
  -o "$TEX"

# As imagens são referidas como figuras/x.pdf; o tectonic resolve-as a
# partir da pasta da disciplina.
tectonic -Z search-path="$SUBJECT_DIR" --keep-logs --outdir "$TMP" "$TEX" \
  > "$TMP/tectonic.out" 2>&1 || { grep -v "^warning:\|^note:" "$TMP/tectonic.out" >&2; exit 1; }
cp "$TMP/RESUMO_${SUBJECT}.pdf" "$PDF"

# Problemas que NÃO dão erro de compilação mas estragam o PDF em silêncio.
LOG="$TMP/RESUMO_${SUBJECT}.log"
# 1) caixas não-quebráveis maiores que uma página -> conteúdo cortado
if grep -qF 'has occurred while \output is active' "$LOG"; then
  echo "AVISO: caixa maior que uma página (fim cortado), a seguir à página:" >&2
  grep -oE '\[[0-9]+\]|Overfull \\vbox \([0-9.]+pt too high\) has occurred' "$LOG" \
    | awk '/^\[/{p=$0} /Overfull/{print "  " p}' | sort -u >&2
fi
# 2) caracteres que a fonte não tem -> saem em branco
if grep -q "Missing character" "$LOG"; then
  echo "AVISO: caracteres sem glifo (saem em branco no PDF):" >&2
  grep -o "Missing character: There is no .* in font [^!]*" "$LOG" | sort | uniq -c >&2
fi
# 3) linhas muito mais largas que a página (> 20pt) -> texto/código a sair da margem
awk '/Overfull \\hbox \(/{ match($0, /\(([0-9.]+)pt/); v=substr($0, RSTART+1, RLENGTH-3); if (v+0 > 20) print "  " $0 }' "$LOG" \
  | sed '1s/^/AVISO: linhas a sair da margem direita:\n/' >&2
echo "Gerado: $PDF"

# Soluções dos exercícios "Pratica agora": HTML com cada alínea escondida
# (<details>), para ver uma de cada vez sem spoilers das outras.
if [ -f "$SOL_MD" ]; then
  pandoc "$SOL_MD" \
    -f markdown \
    --template "$ROOT/_shared/template/solucoes.html" \
    --lua-filter "$ROOT/_shared/template/solucoes.lua" \
    --lua-filter "$ROOT/_shared/template/auto-align.lua" \
    --math-method=mathml \
    --toc --toc-depth=3 \
    --embed-resources --standalone \
    --syntax-highlighting=tango \
    --resource-path="$SUBJECT_DIR" \
    -o "$SOL_HTML"
  echo "Gerado: $SOL_HTML"
fi
