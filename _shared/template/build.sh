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

# Estilo v2 (preamble-v2.tex: Charter/Avenir/Menlo, compacto, sem caixas de
# atenção/exame). Disciplinas ainda não convertidas ficam no estilo antigo.
ESTILO_V2=" Compiladores TecnologiasWeb Redes Logica IPM "
STYLE_ARGS=(-V geometry:margin=2.5cm)
if [[ "$ESTILO_V2" == *" $SUBJECT "* ]]; then
  PREAMBLE="$ROOT/_shared/template/preamble-v2.tex"
  STYLE_ARGS=(-M estilo=v2 -V fontsize=10pt
    -V "geometry:left=2.2cm,right=2.2cm,top=2.1cm,bottom=2.3cm,headsep=14pt"
    -V mainfont=Charter -V "sansfont=Avenir Next" -V "mathfont=STIX Two Math")
fi
# Índice a duas colunas (v2) quando não cabe numa página (indice-2col.tex).
INDICE_2COL=" TecnologiasWeb "
TOC_ARGS=()
if [[ "$INDICE_2COL" == *" $SUBJECT "* ]]; then
  TOC_ARGS=(-H "$ROOT/_shared/template/indice-2col.tex")
fi

if [ ! -f "$MD" ]; then
  echo "Não encontrei $MD" >&2
  exit 1
fi

SOL_MD="$SUBJECT_DIR/.fonte/SOLUCOES_${SUBJECT}.md"
# As caixas "Pratica agora" do PDF apontam para o site único de soluções
# (SOLUCOES.html, na raiz), já no separador desta disciplina.
SOL_META=()
[ -f "$SOL_MD" ] && SOL_META=(-M "solucoes=../SOLUCOES.html#${SUBJECT}" -M "solucoes_md=$SOL_MD")

TMP="$(mktemp -d)"
trap '[ -n "${KEEP_TMP:-}" ] && echo "TMP=$TMP" || rm -rf "$TMP"' EXIT
TEX="$TMP/RESUMO_${SUBJECT}.tex"

# figuras dos blocos {.tableau}/{.resolucao}, regeneradas a cada build
rm -rf "$SUBJECT_DIR/figuras/auto"

pandoc "$MD" \
  -f markdown-implicit_figures \
  -s \
  -H "$PREAMBLE" \
  ${TOC_ARGS[@]+"${TOC_ARGS[@]}"} \
  --lua-filter "$ROOT/_shared/template/fitch.lua" \
  --lua-filter "$ROOT/_shared/template/tableau.lua" \
  --lua-filter "$FILTER" \
  --lua-filter "$ROOT/_shared/template/auto-align.lua" \
  -V lang=pt-PT \
  "${STYLE_ARGS[@]}" \
  --toc --toc-depth=2 \
  --syntax-highlighting=tango \
  ${SOL_META[@]+"${SOL_META[@]}"} \
  -o "$TEX"

# As imagens são referidas como figuras/x.pdf; o tectonic resolve-as a
# partir da pasta da disciplina.
tectonic -Z search-path="$SUBJECT_DIR" --keep-logs --outdir "$TMP" "$TEX" \
  > "$TMP/tectonic.out" 2>&1 || { grep -v "^warning:\|^note:" "$TMP/tectonic.out" >&2; exit 1; }
cp "$TMP/RESUMO_${SUBJECT}.pdf" "$PDF"

# 4) markdown por converter (fenced div malformado, atributo partido): não dá
#    erro nenhum, a caixa sai como texto com ":::" literais. Também lista
#    colada a um parágrafo sem linha em branco (sai "texto: - item - item"). Substitui a
#    inspeção visual do PDF para este tipo de bug.
check_markup() {
  pdftotext -layout "$1" - 2>/dev/null \
    | grep -n -E '(^|[^:]):::( |$|\{)|\{\.[a-z]+|title="|[[:alpha:]*]: - [[:alpha:]*]' | head -5 \
    | sed "1s|^|AVISO ($2): markdown por converter no PDF (linha do texto extraído):\n|" >&2 || true
}

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
check_markup "$PDF" resumo
echo "Gerado: $PDF"

# Página de cada figura nova (FIG_PAGES="a.pdf b.pdf", passado pelo fechar.sh).
# Compila uma cópia do .tex com um \write por figura, sem tocar no PDF gerado.
if [ -n "${FIG_PAGES:-}" ]; then
  FT="$TMP/figs"; mkdir -p "$FT"; SEDS=()
  for fig in $FIG_PAGES; do
    SEDS+=(-e "s|(\\\\includegraphics(\[[^]]*\])?\{figuras/${fig}\})|\1\\\\write16{FIGURA ${fig} PAG \\\\thepage}|g")
  done
  sed -E "${SEDS[@]}" "$TEX" > "$FT/figs.tex"
  tectonic -Z search-path="$SUBJECT_DIR" --keep-logs --outdir "$FT" "$FT/figs.tex" > /dev/null 2>&1 || true
  grep -ho "FIGURA [^ ]* PAG [0-9]*" "$FT/figs.log" 2>/dev/null | sort -u | sed 's/^FIGURA \(.*\) PAG \(.*\)/FIGURA: \1 na página \2/' || true
fi

# Outros documentos (opcional): .fonte/REVISAO_<Disciplina>.md (folha de
# revisão para o exame) e qualquer outro .fonte/*.md que não seja o RESUMO
# nem as SOLUCOES nem o CONTEXTO (calendário, enunciado do trabalho...) -> <nome>.pdf ao lado.
# Mesmo estilo, sem índice, sem página nova por secção.
for DOC_MD in "$SUBJECT_DIR"/.fonte/*.md; do
  DOC="$(basename "$DOC_MD" .md)"
  case "$DOC" in RESUMO_*|SOLUCOES_*|CONTEXTO_*) continue ;; esac
  DOC_TEX="$TMP/$DOC.tex"
  pandoc "$DOC_MD" \
    -f markdown-implicit_figures -s \
    -H "$PREAMBLE" \
    --lua-filter "$ROOT/_shared/template/fitch.lua" \
  --lua-filter "$ROOT/_shared/template/tableau.lua" \
    --lua-filter "$FILTER" \
    --lua-filter "$ROOT/_shared/template/auto-align.lua" \
    -V lang=pt-PT \
    "${STYLE_ARGS[@]}" \
    --syntax-highlighting=tango \
    -o "$DOC_TEX"
  tectonic -Z search-path="$SUBJECT_DIR" --keep-logs --outdir "$TMP" "$DOC_TEX" \
    > "$TMP/tectonic-$DOC.out" 2>&1 || { grep -v "^warning:\|^note:" "$TMP/tectonic-$DOC.out" >&2; exit 1; }
  cp "$TMP/$DOC.pdf" "$SUBJECT_DIR/$DOC.pdf"
  DOC_LOG="$TMP/$DOC.log"
  grep -qF 'has occurred while \output is active' "$DOC_LOG" && echo "AVISO ($DOC): caixa maior que uma página" >&2
  grep -q "Missing character" "$DOC_LOG" && { echo "AVISO ($DOC): caracteres sem glifo:" >&2; grep -o "Missing character: There is no .* in font [^!]*" "$DOC_LOG" | sort | uniq -c >&2; }
  awk '/Overfull \\hbox \(/{ match($0, /\(([0-9.]+)pt/); v=substr($0, RSTART+1, RLENGTH-3); if (v+0 > 20) print "  " $0 }' "$DOC_LOG" \
    | sed "1s/^/AVISO ($DOC): linhas a sair da margem direita:\n/" >&2
  check_markup "$SUBJECT_DIR/$DOC.pdf" "$DOC"
  echo "Gerado: $SUBJECT_DIR/$DOC.pdf"
done

# Soluções dos exercícios "Pratica agora": um só site para todas as
# disciplinas (SOLUCOES.html, na raiz), com cada alínea escondida. É
# reconstruído por inteiro a partir de todos os .fonte/SOLUCOES_*.md.
if [ -f "$SOL_MD" ]; then
  python3 "$ROOT/_shared/template/build_solucoes.py"
fi
