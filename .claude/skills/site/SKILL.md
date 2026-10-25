---
name: site
description: Afina o site do Gonçalo (_site/, GitHub Pages) — painel pessoal cifrado, estudo (ficha + soluções), títulos das aulas, ligações partidas, design. Usar só quando o Gonçalo pede explicitamente para mexer no site; nunca como parte do resumo-semanal.
---

# Site (só a pedido)

O site gera-se sozinho no GitHub Actions a cada push (`_shared/site/build_site.py`).
É do Gonçalo: tudo em PDF (`ver.html`, `#pN` salta para a página); fichas com
soluções no `estudo.html` (prefixos em `fichas.json`); painel pessoal decifrado no
browser por `design/pessoal.js` a partir do `pessoal.enc` (feito por
`_shared/template/pessoal.py`; nada pessoal em claro no repositório, que é público).
Cada solução acaba com "lê a teoria: <secção> (p. N)": a k-ésima caixa `pratica`
do resumo é a k-ésima secção `##` das SOLUCOES, e a página vem do `pdftotext` do
RESUMO (escolha múltipla: a ligação do Quizrama, senão a secção mais parecida).
Testar no browser: a aba controlada pelo Claude está oculta, e aí o PDF.js não
desenha (sem `requestAnimationFrame`); confere o PDF com o Gonçalo ou por `pdftoppm`.
Esta skill é para quando o Gonçalo quer o site afinado; poupa tokens como a
`resumo-semanal` (poucas chamadas, nada de ler ficheiros inteiros).

1. `python3 _shared/site/build_site.py --estrito 2>&1 | grep -E "AVISO|ERRO|Gerado|  "`.
   Cada AVISO (ligação partida) é para corrigir.
2. Títulos: cada slide/ficha sem entrada em `_shared/site/titulos.json` aparece
   como "Aula N". Acrescenta o título em português, lido da 1.ª linha do cache
   (`<D>/.fonte/.cache/<aula>.txt`), sem abrir o PDF.
3. Ver no browser só o que mudou: `_shared/template/site.sh` (porta 8000).
   Design: tokens em `design/tokens.css`, componentes em `site.css`;
   só modo escuro, sem gradientes nem sombras.
4. Publicar = commit + push (só quando o Gonçalo pedir).
