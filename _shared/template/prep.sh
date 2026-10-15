#!/bin/bash
# Arranque de uma sessão do resumo-semanal, numa só chamada:
#   1) estado: aulas por processar, ficheiros fora do esquema (com a 1.ª linha
#      do slide 1 e o próximo número livre), práticas, índice compacto;
#   2) extrai cada aula nova para o cache (.fonte/.cache/), sem a imprimir;
#   3) sobreposições: palavras-chave dos títulos dos slides novos -> secções
#      onde já aparecem (REVISAO, RESUMO);
#   4) soluções: as últimas ##/### (numeração a seguir) e práticas que o
#      RESUMO ainda não menciona;
#   5) o .fonte/CONTEXTO_<D>.md (convenções e factos da disciplina).
# Uso: _shared/template/prep.sh <Disciplina>
# Depois: ler o cache de cada aula nova com o Read, uma vez, e escrever.
set -uo pipefail
export LC_ALL=en_US.UTF-8

SUBJECT="$1"
TEMPLATE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$TEMPLATE/../.." && pwd)"
D="$ROOT/$SUBJECT"
MD="$D/.fonte/RESUMO_${SUBJECT}.md"
SOL="$D/.fonte/SOLUCOES_${SUBJECT}.md"
CTX="$D/.fonte/CONTEXTO_${SUBJECT}.md"
[ -d "$D" ] || { echo "Não existe a pasta $SUBJECT" >&2; exit 1; }
# caminhos relativos à raiz (menos texto na saída)
if [ -z "${PREP_INNER:-}" ]; then PREP_INNER=1 bash "$0" "$@" 2>&1 | sed "s|$ROOT/||g"; exit "${PIPESTATUS[0]}"; fi

# 1) estado + índice compacto
bash "$TEMPLATE/contexto.sh" "$SUBJECT" | grep -v '^== Fora do esquema'

PROC="$(grep -m1 -o '<!-- processado:.*-->' "$MD" 2>/dev/null || true)"
NOVAS=(); FORA=()
for f in "$D"/Teoricas/*; do
  [ -e "$f" ] || continue
  case "$f" in *.pdf|*.pptx) ;; *) continue ;; esac
  rel="Teoricas/$(basename "$f")"
  [[ "$PROC" == *"$rel"* ]] && continue
  case "$(basename "$f")" in Aula_*) NOVAS+=("$f") ;; *) FORA+=("$f") ;; esac
done

# 2) extrair (cache) — fora do esquema: só o resumo e a 1.ª linha útil
if [ ${#FORA[@]} -gt 0 ]; then
  ULT="$(ls "$D"/Teoricas/ 2>/dev/null | grep -oE '^Aula_[0-9]+' | sed 's/Aula_//' | sort -n | tail -1)"
  PROX="$(printf 'Aula_%02d' $((10#${ULT:-0} + 1)))"
  echo "== Fora do esquema (próximo número livre: $PROX; manda a ordem em que as aulas foram dadas)"
  for f in "${FORA[@]}"; do
    bash "$TEMPLATE/extrair.sh" "$f" | sed 's/^/  /'
    echo "  1.º slide: $(bash "$TEMPLATE/extrair.sh" "$f" 1 2 | grep -v '^---\|^$' | head -3 | tr '\n' '/' | cut -c1-150)"
  done
fi
for f in ${NOVAS[@]+"${NOVAS[@]}"}; do bash "$TEMPLATE/extrair.sh" "$f"; done

# 3) sobreposições: palavras-chave (>=6 letras, as mais frequentes) dos títulos
#    dos slides novos (1.ª linha de cada slide)
CACHES=()
# (fora do esquema só entra se for do tamanho de uma aula: livros e apontamentos não)
for f in ${NOVAS[@]+"${NOVAS[@]}"} ${FORA[@]+"${FORA[@]}"}; do
  b="$(basename "$f")"; c="$D/.fonte/.cache/${b%.*}.txt"
  [ "$(grep -c '^--- slide' "$c")" -le 100 ] && CACHES+=("$c")
done
if [ ${#CACHES[@]} -gt 0 ] && [ -f "$MD" ]; then
  TERMOS=()
  while IFS= read -r t; do TERMOS+=("$t"); done < <(
    awk '/^--- slide/{ getline; sub(/ │.*/, ""); print }' "${CACHES[@]}" \
    | tr '[:upper:]' '[:lower:]' | tr -cs '[:alpha:]' '\n' \
    | awk 'length($0) >= 6' \
    | grep -vxE 'about|between|through|their|should|exemplo|exemplos|example|examples|question|questions|activity|summary|sumario|sumário|resumo|introducao|introdução|introduction|lecture|module|wrapup|continuacao|continuação|aula|slide|figura|figueira|álvaro' \
    | sort | uniq -c | sort -rn | awk '$1 >= 1 { print $2 }' | head -15)
  if [ ${#TERMOS[@]} -gt 0 ]; then
    echo "== Sobreposições (títulos dos slides novos → secções; faltam termos? contexto.sh <D> --mapa ...)"
    bash "$TEMPLATE/contexto.sh" "$SUBJECT" --mapa "${TERMOS[@]}" | cut -c1-170 \
      | awk '/→ \(nada\)$/ { sub(/ → \(nada\)$/, ""); nada = nada (nada ? ", " : "") $0; next } { print }
             END { if (nada) print "sem ocorrências: " nada }'
  fi
fi

# 4) soluções e práticas
if [ -f "$SOL" ]; then
  echo "== SOLUCOES: últimas secções (continua a numeração)"
  grep -n -E '^#{2,3} ' "$SOL" | tail -4 | sed 's/^/  /'
fi
if [ -d "$D/Praticas" ] && [ -f "$MD" ]; then
  FALTA=""
  while IFS= read -r p; do
    b="$(basename "$p")"; b="${b%.*}"
    grep -qiF -- "$b" "$MD" || FALTA+=" ${p#$D/Praticas/}"
  done < <(find "$D/Praticas" -type f \( -name '*.pdf' -o -name '*.pptx' \) -not -path '*/tests/*' | sort)
  [ -n "$FALTA" ] && echo "== Práticas que o RESUMO não menciona pelo nome (podem já estar usadas):$(echo "$FALTA" | cut -c1-400)"
fi

# 5) convenções da disciplina
if [ -f "$CTX" ]; then echo "== CONTEXTO_${SUBJECT}.md"; cat "$CTX"; fi
