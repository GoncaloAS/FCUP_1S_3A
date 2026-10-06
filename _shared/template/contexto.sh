#!/bin/bash
# Resumo curto do estado de uma disciplina, para não ter de ler o RESUMO inteiro.
# Uso:
#   _shared/template/contexto.sh <Disciplina>              aulas por processar + índice
#   _shared/template/contexto.sh <Disciplina> termo ...    + grep -n dos termos
#   _shared/template/contexto.sh <Disciplina> --sol        caixas pratica <-> soluções
set -uo pipefail

SUBJECT="$1"; shift
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
D="$ROOT/$SUBJECT"
MD="$D/.fonte/RESUMO_${SUBJECT}.md"
SOL="$D/.fonte/SOLUCOES_${SUBJECT}.md"
REV="$D/.fonte/REVISAO_${SUBJECT}.md"
[ -d "$D" ] || { echo "Não existe a pasta $SUBJECT" >&2; exit 1; }

if [ "${1:-}" = "--sol" ]; then
  echo "== Caixas pratica no RESUMO (linha: título; alíneas citadas)"
  awk '/^::: *\{\.pratica/{ match($0, /title="[^"]*"/); t=substr($0, RSTART+7, RLENGTH-8); n=NR; al=""; inbox=1; next }
       inbox && /^:::/{ print n ": " t (al ? "  [" al "]" : ""); inbox=0; next }
       inbox{ while (match($0, /\*\*\([a-z]\)\*\*|Ex\. ?[0-9]+(\.[0-9]+)?\([a-z]\)/)) { al = al substr($0, RSTART, RLENGTH) " "; $0 = substr($0, RSTART+RLENGTH) } }' "$MD"
  echo
  echo "== Soluções (SOLUCOES_${SUBJECT}.md, ##/###/####)"
  [ -f "$SOL" ] && grep -n '^##' "$SOL" | sed -E 's/^([0-9]+):(#+)/\1:\2/' || echo "(não existe)"
  echo
  echo "== Ids gerados no SOLUCOES.html"
  grep -o "details class=\"sol\" id=\"${SUBJECT}-[^\"]*\"" "$ROOT/SOLUCOES.html" \
    | sed -E "s/.*id=\"${SUBJECT}-//; s/\"$//" | tr '\n' ' '; echo
  exit 0
fi

echo "== Aulas em Teoricas/ ainda por processar"
PROC="$(grep -m1 -o '<!-- processado:.*-->' "$MD" 2>/dev/null || true)"
found=0; SUPL=""
for f in "$D"/Teoricas/*; do
  rel="Teoricas/$(basename "$f")"
  case "$f" in *.pdf|*.pptx) ;; *) continue ;; esac
  case "$(basename "$f")" in Aula_*) ;; *) SUPL+=" $(basename "$f")"; continue ;; esac
  if [[ "$PROC" != *"$rel"* ]]; then
    pags="$(pdfinfo "$f" 2>/dev/null | awk '/^Pages:/{print $2}')"
    echo "  $rel${pags:+ ($pags páginas)}"; found=1
  fi
done
[ $found = 0 ] && echo "  (nenhuma)"
[ -n "$SUPL" ] && echo "== Fora do esquema Aula_NN (se for aula nova: ver a 1.ª página e renomear; se for suplementar: não processar, consultar só as páginas das lacunas):$SUPL"
echo "== Práticas: $(ls "$D/Praticas" 2>/dev/null | tr '\n' ' ')"
[ -f "$MD" ] || { echo "(ainda não há RESUMO_${SUBJECT}.md)"; exit 0; }
echo "== RESUMO_${SUBJECT}.md: $(wc -l < "$MD") linhas. Índice (linha: título):"
grep -n -E '^#{1,3} |^::: *\{\.pratica' "$MD" | grep -v '^[0-9]*:#\{1,3\} *$' \
  | sed -E 's/^([0-9]+):::: *\{\.pratica title="([^"]*)".*/\1:      [pratica] \2/; s/^([0-9]+):### /\1:    /; s/^([0-9]+):## /\1:  /; s/^([0-9]+):# /\1:/'

if [ $# -gt 0 ]; then
  for t in "$@"; do
    echo "== grep -i \"$t\""
    for f in "$MD" "$SOL" "$REV"; do
      [ -f "$f" ] || continue
      grep -n -i -- "$t" "$f" | cut -c1-140 | head -15 | sed "s|^|  $(basename "$f" .md):|"
    done
  done
fi
