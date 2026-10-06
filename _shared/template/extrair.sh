#!/bin/bash
# Extrai o texto de um PDF de slides, slide a slide, e assinala os slides que
# têm de ser vistos como imagem (figuras ou quase sem texto).
# Uso: _shared/template/extrair.sh <Disciplina>/Teoricas/Aula_NN.pdf [primeira última]
# Ler o texto é ~10x mais barato do que abrir as páginas com o Read.
set -euo pipefail

PDF="$1"
N="$(pdfinfo "$PDF" | awk '/^Pages:/{print $2}')"
P1="${2:-1}"; P2="${3:-$N}"

# Páginas com imagens raster próprias. Ignora imagens minúsculas (ícones) e
# as do modelo dos slides (o mesmo objeto repetido em mais de 3 páginas).
IMGS="$(pdfimages -list "$PDF" 2>/dev/null | awk -v a="$P1" -v b="$P2" '
  NR>2 && $3=="image" && $4*$5 > 40000 { pg[NR]=$1; obj[NR]=$11; seen[$11","$1]=1 }
  END { for (k in seen) { split(k, x, ","); n[x[1]]++ }
        for (r in pg) if (n[obj[r]] <= 3 && pg[r]>=a && pg[r]<=b) print pg[r] }' | sort -nu | tr '\n' ' ')"

VER=()
for ((p=P1; p<=P2; p++)); do
  TXT="$(pdftotext -layout -f "$p" -l "$p" "$PDF" - 2>/dev/null | sed -E 's/[[:space:]]+$//' | cat -s)"
  W="$(echo "$TXT" | wc -w | tr -d ' ')"
  MARCA=""
  if [[ " $IMGS " == *" $p "* ]]; then MARCA=" [IMAGEM]"; VER+=("$p")
  elif [ "$W" -lt 15 ]; then MARCA=" [POUCO TEXTO]"; VER+=("$p"); fi
  echo "--- slide $p$MARCA ---"
  echo "$TXT" | sed '/^$/N;/^\n$/D'
done
echo
echo "=== $N páginas. Ver como imagem só se o texto não chegar: ${VER[*]:-nenhuma}"
echo "=== (diagramas vetoriais não são detetados: se o texto falar de uma figura/autómato/árvore, abre esse slide)"
