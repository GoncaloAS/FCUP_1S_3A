#!/bin/bash
# Fecho de uma sessão do resumo-semanal, numa só chamada:
#   1) Lógica: verifica as deduções Fitch e os tableaux (fitch_check.py, tableau.py);
#   2) figuras novas: tamanho de letra efetivo no PDF (AVISO abaixo de 7 pt);
#   3) build.sh filtrado (só AVISO / erro / Gerado) + página de cada figura nova;
#   4) contexto.sh --sol (caixas <-> soluções <-> site);
#   5) opcional: atualiza o <!-- processado --> e o date: do RESUMO;
#   6) se a disciplina tem quiz no Quizrama, regenera o guia e as perguntas e corre os testes.
# Uso: _shared/template/fechar.sh <Disciplina> [--aula Teoricas/Aula_NN.pdf ...] [--data "Semana N (...)"]
# Só se abre uma página como imagem quando este script dá AVISO.
set -uo pipefail

SUBJECT="$1"; shift
TEMPLATE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$TEMPLATE/../.." && pwd)"
D="$ROOT/$SUBJECT"
MD="$D/.fonte/RESUMO_${SUBJECT}.md"
PDF="$D/RESUMO_${SUBJECT}.pdf"
[ -f "$MD" ] || { echo "Não encontrei $MD" >&2; exit 1; }

AULAS=(); DATA=""
while [ $# -gt 0 ]; do
  case "$1" in
    --aula) AULAS+=("$2"); shift 2 ;;
    --data) DATA="$2"; shift 2 ;;
    *) echo "Argumento desconhecido: $1" >&2; exit 1 ;;
  esac
done

# 5) primeiro o cabeçalho, para o build já sair com a data certa
for a in ${AULAS[@]+"${AULAS[@]}"}; do
  if grep -q -- "$a" <(grep -m1 '<!-- processado:' "$MD"); then echo "processado: $a já lá estava"
  else sed -i '' -E "1,/<!-- processado:/ s|^(<!-- processado:.*[^ ]) *-->|\1, $a -->|" "$MD" && echo "processado: + $a"; fi
done
if [ -n "$DATA" ]; then
  esc="$(printf '%s' "$DATA" | sed 's/[&|]/\\&/g')"
  sed -i '' -E "1,8 s|^date: .*|date: \"Atualizado: $esc\"|" "$MD"
  grep -m1 '^date:' "$MD"
fi

# 1) Lógica: deduções Fitch e tableaux/resoluções
if grep -q '```{.fitch' "$D"/.fonte/*.md 2>/dev/null; then
  python3 "$ROOT/_shared/tools/fitch_check.py" "$D"/.fonte/*.md 2>&1 | grep -E "erro|ERRO|falh|verificad" | tail -5
fi
if grep -qE '```\{\.(tableau|resolucao)' "$D"/.fonte/*.md 2>/dev/null; then
  python3 "$ROOT/_shared/tools/tableau.py" check "$D"/.fonte/*.md 2>&1 | grep -E "erro|ERRO|falh|verificad" | tail -5
fi

# 2) figuras novas: mais recentes do que o PDF anterior e usadas em algum .md
LARGURA_PT=470   # \linewidth do estilo v2 (A4 com 2,2 cm de margem)
NOVAS=()
for f in "$D"/figuras/*.pdf; do
  [ -e "$f" ] || continue
  [ -f "$PDF" ] && [ ! "$f" -nt "$PDF" ] && continue
  n="$(basename "$f")"
  ref="$(grep -ho "figuras/$n){[^}]*}" "$D"/.fonte/*.md 2>/dev/null | head -1)"
  [ -n "$ref" ] || continue
  NOVAS+=("$n")
  dot="${f%.pdf}.dot"; fs=14
  [ -f "$dot" ] && fs="$(grep -oE 'fontsize *= *"?[0-9.]+' "$dot" | grep -oE '[0-9.]+$' | sort -n | head -1)"
  [ -n "$fs" ] || fs=14
  read -r W H < <(pdfinfo "$f" | awk '/^Page size:/{print $3, $5}')
  awk -v n="$n" -v fs="$fs" -v W="$W" -v H="$H" -v ref="$ref" -v L="$LARGURA_PT" 'BEGIN {
    esc = 1
    if (match(ref, /width=[0-9.]+%/)) { p = substr(ref, RSTART+6, RLENGTH-7); esc = p / 100 * L / W }
    else if (match(ref, /height=[0-9.]+cm/)) { h = substr(ref, RSTART+7, RLENGTH-9); esc = h * 28.35 / H }
    if (esc * W > L) esc = L / W
    ef = fs * esc
    printf "%s figura %s: letra %.1f pt (fonte %s pt, escala %.2f)\n", (ef < 7 ? "AVISO:" : "      "), n, ef, fs, esc }'
done

# 3) build
FIG_PAGES="${NOVAS[*]:-}" bash "$TEMPLATE/build.sh" "$SUBJECT" 2>&1 | grep -iE "aviso|erro|error|gerado|^FIGURA|^  " | sed "s|$ROOT/_shared/../||; s|$ROOT/||"

# 4) soluções
bash "$TEMPLATE/contexto.sh" "$SUBJECT" --sol

# 6) Quizrama: se a disciplina tem quiz (Quizrama/tools/<disciplina>-guide/), regenera o guia
#    a partir do RESUMO, o banco de perguntas e corre os smoke tests.
G="$ROOT/Quizrama/tools/$(printf '%s' "$SUBJECT" | tr '[:upper:]' '[:lower:]')-guide"
if [ -d "$G" ]; then
  python3 "$G/build.py" 2>&1 | sed 's/^/quiz: /'
  [ -f "$G/perguntas.py" ] && python3 "$G/perguntas.py" 2>&1 | tail -1 | sed 's/^/quiz: /'
  (cd "$ROOT/Quizrama" && npm test 2>&1 | grep -E "FAIL|smoke tests|^  " | sed 's/^/quiz: /')
fi
