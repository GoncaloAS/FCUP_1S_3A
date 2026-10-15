#!/bin/bash
# Extrai o texto dos slides (PDF ou PPTX), slide a slide, para um cache
# compacto, e assinala os slides que têm de ser vistos como imagem.
# Uso:
#   _shared/template/extrair.sh <ficheiro>          gera o cache, mostra o resumo
#   _shared/template/extrair.sh <ficheiro> a b      mostra os slides a..b do cache
# O cache fica em <Disciplina>/.fonte/.cache/<nome>.txt e só se refaz quando o
# ficheiro é mais recente. Lê-se com o Read, uma única vez (por partes se for
# grande). Ler o texto é ~10x mais barato do que abrir as páginas com o Read.
#
# Compactação (sem perder texto): espaços nas pontas fora, >=3 espaços = " │ "
# (fronteira de coluna), e linhas repetidas em >=50% das páginas (rodapés,
# cabeçalhos, data) tiradas e anunciadas uma vez no topo.
set -euo pipefail

SRC="$1"
TEMPLATE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
[ -f "$SRC" ] || { echo "Não existe: $SRC" >&2; exit 1; }

# pasta da disciplina = o primeiro antepassado com .fonte/
D="$(cd "$(dirname "$SRC")" && pwd)"
while [ "$D" != "/" ] && [ ! -d "$D/.fonte" ]; do D="$(dirname "$D")"; done
if [ "$D" = "/" ]; then CACHE_DIR="$(cd "$(dirname "$SRC")" && pwd)/.cache"
else CACHE_DIR="$D/.fonte/.cache"; fi
mkdir -p "$CACHE_DIR"
BASE="$(basename "$SRC")"; CACHE="$CACHE_DIR/${BASE%.*}.txt"

gerar_pdf() {
  local N IMGS
  N="$(pdfinfo "$SRC" | awk '/^Pages:/{print $2}')"
  # Páginas com imagens raster próprias. Ignora imagens minúsculas (ícones) e
  # as do modelo dos slides (o mesmo objeto repetido em mais de 3 páginas).
  IMGS="$(pdfimages -list "$SRC" 2>/dev/null | awk '
    NR>2 && $3=="image" && $4*$5 > 40000 { pg[NR]=$1; obj[NR]=$11; seen[$11","$1]=1 }
    END { for (k in seen) { split(k, x, ","); n[x[1]]++ }
          for (r in pg) if (n[obj[r]] <= 3) print pg[r] }' | sort -nu | tr '\n' ' ')"
  pdftotext -layout "$SRC" - 2>/dev/null | awk -v N="$N" -v IMGS=" $IMGS " '
    function norm(s) { sub(/^[ \t]+/, "", s); sub(/[ \t]+$/, "", s); gsub(/ {3,}/, " │ ", s); return s }
    # chave de repetição: algarismos -> "#" (o rodapé "M05 · 7" muda de página para página)
    function chave(s) { gsub(/[0-9]+/, "#", s); return s }
    { n = split($0, parts, "\f")
      for (i = 1; i <= n; i++) {
        if (i > 1) pg++
        l = norm(parts[i]); L[pg+1, ++nl[pg+1]] = l
        c = chave(l)
        if (length(l) >= 8 && l ~ /[[:alnum:]]/ && !((pg+1, c) in vis)) { vis[pg+1, c] = 1; cnt[c]++ }
      } }
    END {
      P = pg + 1; vazia = 1; for (k = 1; k <= nl[P]; k++) if (L[P, k] != "") vazia = 0
      if (vazia) P = pg   # o \f final do pdftotext abre uma página vazia
      lim = (P >= 4) ? P / 2 : P + 1
      for (l in cnt) if (cnt[l] >= lim && cnt[l] >= 3) { rem[l] = 1; print "[rodapé removido: " l "]" }
      for (p = 1; p <= P; p++) {
        # última linha não vazia (para tirar o número de página solto)
        last = 0; for (k = 1; k <= nl[p]; k++) if (L[p, k] != "") last = k
        out = ""; w = 0; prevrem = 0; blank = 1
        for (k = 1; k <= nl[p]; k++) {
          l = L[p, k]
          if (chave(l) in rem) { prevrem = 1; continue }
          if (l ~ /^[0-9]{1,3}$/ && (prevrem || k == last)) { prevrem = 0; continue }
          prevrem = 0
          if (l == "") { if (!blank) out = out "\n"; blank = 1; continue }
          blank = 0; out = out l "\n"; w += split(l, tmp, /[ \t]+/) - gsub(/│/, "│", l)
        }
        marca = ""
        if (index(IMGS, " " p " ")) marca = " [IMAGEM]"
        else if (w < 15) marca = " [POUCO TEXTO]"
        if (marca != "") ver = ver " " p
        printf "--- slide %d%s ---\n%s", p, marca, out
      }
      printf "\n=== %d páginas. Ver como imagem só se o texto não chegar:%s\n", P, (ver == "" ? " nenhuma" : ver)
      print "=== (diagramas vetoriais não são detetados: se o texto falar de uma figura/autómato/árvore, abre esse slide)"
    }'
}

gerar_pptx() {
  local VENV="$TEMPLATE/../.venv"
  if [ ! -x "$VENV/bin/python" ] || ! "$VENV/bin/python" -c 'import pptx' 2>/dev/null; then
    python3 -m venv "$VENV" >&2 && "$VENV/bin/pip" install -q --disable-pip-version-check python-pptx >&2
  fi
  "$VENV/bin/python" -I "$TEMPLATE/extrair_pptx.py" "$SRC"
}

if [ ! -f "$CACHE" ] || [ "$SRC" -nt "$CACHE" ]; then
  case "$SRC" in
    *.pptx) gerar_pptx > "$CACHE.tmp" ;;
    *.pdf)  gerar_pdf  > "$CACHE.tmp" ;;
    *) echo "Formato não suportado: $SRC (ver ref/fontes.md)" >&2; exit 1 ;;
  esac
  mv "$CACHE.tmp" "$CACHE"
fi

if [ $# -ge 3 ]; then
  awk -v a="$2" -v b="$3" '/^--- slide [0-9]+/{ s = $3 + 0 } /^\[rodapé removido/{ next } /^=== /{ s = 0 } s >= a && s <= b' "$CACHE"
  exit 0
fi

echo "== $SRC → $CACHE ($(wc -c < "$CACHE" | tr -d ' ') bytes, $(wc -l < "$CACHE" | tr -d ' ') linhas)"
echo "   rodapés removidos: $(grep -c '^\[rodapé removido' "$CACHE" || true)"
grep '^=== [0-9]' "$CACHE" | sed 's/^=== /   /'
