#!/bin/bash
# Resumo curto do estado de uma disciplina, para não ter de ler o RESUMO inteiro.
# Uso:
#   _shared/template/contexto.sh <Disciplina>            aulas por processar + índice compacto (#, ##, pratica)
#   _shared/template/contexto.sh <Disciplina> --indice   índice completo (com ###)
#   _shared/template/contexto.sh <Disciplina> termo ...  linhas com o termo e a secção (REVISAO, RESUMO, SOLUCOES)
#   _shared/template/contexto.sh <Disciplina> --mapa termo ...  uma linha por termo: as ## onde aparece
#   _shared/template/contexto.sh <Disciplina> --sol      verifica caixas pratica <-> soluções <-> site (diff)
#   _shared/template/contexto.sh <Disciplina> --sol --lista   as três listas completas
# Os termos não distinguem maiúsculas nem acentos ("restricoes" apanha "Restrições").
set -uo pipefail
export LC_ALL=en_US.UTF-8

SUBJECT="$1"; shift
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
D="$ROOT/$SUBJECT"
MD="$D/.fonte/RESUMO_${SUBJECT}.md"
SOL="$D/.fonte/SOLUCOES_${SUBJECT}.md"
REV="$D/.fonte/REVISAO_${SUBJECT}.md"
[ -d "$D" ] || { echo "Não existe a pasta $SUBJECT" >&2; exit 1; }

# alíneas citadas em cada caixa pratica: "linha<TAB>título<TAB>a b c"
caixas() {
  awk '/^::: *\{\.pratica/{ match($0, /title="[^"]*"/); t=substr($0, RSTART+7, RLENGTH-8); n=NR; al=""; inbox=1; next }
       inbox && /^:::/{ print n "\t" t "\t" al; inbox=0; next }
       # alínea = "**(x)**" no início da linha (a meio é um subcaso) ou "Ex. N(x)" em qualquer sítio
       inbox && match($0, /^[ \t]*(- )?\*\*\([a-z]\)\*\*/){ s=substr($0, RSTART, RLENGTH); sub(/.*\(/, "", s); sub(/\).*/, "", s); al = al s " " }
       inbox{ while (match($0, /Ex\. ?[0-9]+(\.[0-9]+)?\([a-z]\)/)) { s=substr($0, RSTART, RLENGTH); sub(/.*\(/, "", s); sub(/\).*/, "", s); al = al s " "; $0 = substr($0, RSTART+RLENGTH) } }' "$MD"
}

if [ "${1:-}" = "--sol" ]; then
  if [ "${2:-}" = "--lista" ]; then
    echo "== Caixas pratica no RESUMO (linha: título; alíneas citadas)"
    caixas | awk -F'\t' '{ print $1 ": " $2 ($3 ? "  [" $3 "]" : "") }'
    echo; echo "== Soluções (SOLUCOES_${SUBJECT}.md, ##/###/####)"
    [ -f "$SOL" ] && grep -n '^##' "$SOL" || echo "(não existe)"
    echo; echo "== Ids gerados no SOLUCOES.html"
    grep -o "details class=\"sol\" id=\"${SUBJECT}-[^\"]*\"" "$ROOT/SOLUCOES.html" \
      | sed -E "s/.*id=\"${SUBJECT}-//; s/\"$//" | tr '\n' ' '; echo
    exit 0
  fi
  [ -f "$SOL" ] || { echo "(não há SOLUCOES_${SUBJECT}.md)"; exit 0; }
  # k-ésima caixa <-> k-ésima ## (como o div-envs.lua); as alíneas citadas na
  # caixa têm de ter #### "(x)" nessa ##; cada #### tem de ter id no site.
  NIDS="$(grep -o "details class=\"sol\" id=\"${SUBJECT}-" "$ROOT/SOLUCOES.html" | wc -l | tr -d ' ')"
  { caixas | sed 's/^/C\t/'; awk '/^## /{ k++; print "S\t" k "\t" substr($0, 4) "\t" } /^#### /{ h=substr($0, 6); if (match(h, /^\([a-z0-9]+\)/)) l=substr(h, 2, RLENGTH-2); else l="*"; print "A\t" k "\t" l }' "$SOL"; } \
  | awk -F'\t' -v nids="$NIDS" '
      $1=="C"{ nc++; cl[nc]=$2; ct[nc]=$3; ca[nc]=$4 }
      $1=="S"{ ns++; st[ns]=$3 }
      $1=="A"{ na++; n4[$2]++; has[$2 "," $3]=1 }
      END {
        bad = 0
        if (nc != ns) { print "FALTA: " nc " caixas pratica mas " ns " ## nas SOLUCOES"; bad++ }
        for (k = 1; k <= nc; k++) {
          if (!n4[k]) { print "FALTA: caixa l." cl[k] " (" ct[k] ") sem nenhuma #### na ## " k " (" st[k] ")"; bad++; continue }
          m = split(ca[k], al, " ")
          for (i = 1; i <= m; i++) if (!has[k "," al[i]]) { print "FALTA: caixa l." cl[k] " (" ct[k] "): alínea (" al[i] ") sem #### na ## " k " (" st[k] ")"; bad++ }
        }
        if (na != nids) { print "FALTA: " na " #### nas SOLUCOES mas " nids " ids no SOLUCOES.html (corre o build)"; bad++ }
        if (!bad) print "OK: " nc " caixas = " ns " ##, " na " alíneas, todas com id no site"
        else print "(detalhe: contexto.sh '"$SUBJECT"' --sol --lista)"
      }'
  exit 0
fi

# termo -> regex sem acentos nem maiúsculas
regex() {
  echo "$1" | tr '[:upper:]' '[:lower:]' | sed -E \
    -e 's/[aáàâã]/[aáàâãAÁÀÂÃ]/g' -e 's/[eéê]/[eéêEÉÊ]/g' -e 's/[ií]/[iíIÍ]/g' \
    -e 's/[oóôõ]/[oóôõOÓÔÕ]/g' -e 's/[uú]/[uúUÚ]/g' -e 's/[cç]/[cçCÇ]/g'
}
# hits de um termo num ficheiro, com a secção (# / ##) a que pertencem
hits() {
  local f="$1" re="$2" nome; nome="$(basename "$f" .md | sed 's/_.*//')"
  grep -n -i -E -- "$re" "$f" 2>/dev/null | head -5 | cut -c1-110 \
  | awk -F: -v f="$f" -v nome="$nome" '
      BEGIN { while ((getline l < f) > 0) { n++; if (l ~ /^##? /) h[n] = l } }
      { ln = $1; s = ""; for (k = ln; k > 0; k--) if (k in h) { s = h[k]; break }
        txt = $0; sub(/^[0-9]+:/, "", txt)
        printf "  %s l.%s [%s]: %s\n", nome, ln, substr(s, 1, 50), txt }'
}

# --mapa termo ...: uma linha por termo, com as secções (##) onde aparece
if [ "${1:-}" = "--mapa" ]; then
  shift
  for t in "$@"; do
    re="$(regex "$t")"; linha=""
    for f in "$REV" "$MD"; do
      [ -f "$f" ] || continue
      r="$(grep -n -i -E -- "$re" "$f" 2>/dev/null | cut -d: -f1 \
        | awk -v f="$f" 'BEGIN { while ((getline l < f) > 0) { n++; if (l ~ /^##? /) { sub(/^#+ /, "", l); h[n] = substr(l, 1, 40) } } }
            { for (k = $1; k > 0; k--) if (k in h) { if (!(k in vis)) { vis[k] = 1; s = s (s ? "; " : "") "l." $1 " " h[k]; m++ } break }; tot++ }
            END { if (tot) printf "%s", s }' | cut -c1-160)"
      [ -n "$r" ] && linha+="  $(basename "$f" .md | sed 's/_.*//'): $r"
    done
    echo "$t →${linha:- (nada)}"
  done
  exit 0
fi

if [ $# -gt 0 ] && [ "$1" != "--indice" ]; then
  for t in "$@"; do
    re="$(regex "$t")"
    out="$(for f in "$REV" "$MD" "$SOL"; do [ -f "$f" ] && hits "$f" "$re"; done)"
    if [ -n "$out" ]; then echo "== $t"; echo "$out"; else echo "== $t: (nada)"; fi
  done
  exit 0
fi

echo "== Aulas em Teoricas/ ainda por processar"
PROC="$(grep -m1 -o '<!-- processado:.*-->' "$MD" 2>/dev/null || true)"
found=0; SUPL=""
for f in "$D"/Teoricas/*; do
  [ -e "$f" ] || continue
  rel="Teoricas/$(basename "$f")"
  case "$f" in *.pdf|*.pptx) ;; *) continue ;; esac
  case "$(basename "$f")" in Aula_*) ;; *) [[ "$PROC" == *"$rel"* ]] || SUPL+=" $(basename "$f")"; continue ;; esac
  if [[ "$PROC" != *"$rel"* ]]; then
    pags="$(pdfinfo "$f" 2>/dev/null | awk '/^Pages:/{print $2}')"
    echo "  $rel${pags:+ ($pags páginas)}"; found=1
  fi
done
[ $found = 0 ] && echo "  (nenhuma)"
[ -n "$SUPL" ] && echo "== Fora do esquema Aula_NN (se for aula nova: ver a 1.ª página e renomear; se for suplementar: não processar, consultar só as páginas das lacunas):$SUPL"
echo "== Práticas: $(ls "$D/Praticas" 2>/dev/null | tr '\n' ' ')"
[ -f "$MD" ] || { echo "(ainda não há RESUMO_${SUBJECT}.md)"; exit 0; }
NIV='#{1,2}'; [ "${1:-}" = "--indice" ] && NIV='#{1,3}'
echo "== RESUMO_${SUBJECT}.md: $(wc -l < "$MD" | tr -d ' ') linhas. Índice (linha: título):"
grep -n -E "^$NIV |^::: *\{\.pratica" "$MD" | grep -v '^[0-9]*:#\{1,3\} *$' \
  | sed -E 's/^([0-9]+):::: *\{\.pratica title="([^"]*)".*/\1:      [pratica] \2/; s/^([0-9]+):### /\1:    /; s/^([0-9]+):## /\1:  /; s/^([0-9]+):# /\1:/'
