---
name: site
description: Afina o site dos colegas (_site/, GitHub Pages) — HTML dos resumos/revisões, títulos das aulas, ligações partidas, design. Usar só quando o Gonçalo pede explicitamente para mexer no site; nunca como parte do resumo-semanal.
---

# Site (só a pedido)

O site gera-se sozinho no GitHub Actions a cada push (`_shared/site/build_site.py`):
resumo e revisão em HTML (pandoc, os mesmos filtros do PDF) e em PDF; slides,
fichas e testes no `ver.html`. Cada solução acaba com "lê a teoria: <secção>",
calculado sozinho a partir da caixa `pratica` que a liga (escolha múltipla: a
ligação do Quizrama, senão a secção mais parecida). Se o pandoc falhar num documento, fica só o PDF.
Esta skill é para quando o Gonçalo quer o site afinado; poupa tokens como a
`resumo-semanal` (poucas chamadas, nada de ler ficheiros inteiros).

1. `python3 _shared/site/build_site.py --estrito 2>&1 | grep -E "AVISO|ERRO|Gerado|  "`.
   Cada AVISO é para corrigir: pandoc falhado (o problema está no `.md` ou num
   filtro lua: corrige sem estragar o PDF), ligação partida, figura em falta.
2. Títulos: cada slide/ficha sem entrada em `_shared/site/titulos.json` aparece
   como "Aula N". Acrescenta o título em português, lido da 1.ª linha do cache
   (`<D>/.fonte/.cache/<aula>.txt`), sem abrir o PDF.
3. Ver no browser só o que mudou: `_shared/template/site.sh` (porta 8000).
   Design: tokens em `design/tokens.css`, componentes em `site.css`/`doc.css`;
   só modo escuro, sem gradientes nem sombras.
4. Publicar = commit + push (só quando o Gonçalo pedir).
