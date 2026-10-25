# FCUP · 3.º ano

Material de estudo do 3.º ano na FCUP (2026/27): um
resumo cumulativo por disciplina, folhas de revisão, soluções dos exercícios
e quizzes de preparação para os testes. O site (GitHub Pages) gera-se a
partir daqui a cada push.

## Onde está cada coisa

| Pasta | O quê |
|---|---|
| `<Disciplina>/` | `RESUMO_*.pdf` e `REVISAO_*.pdf`; `Teoricas/`, `Praticas/Semana_N/`, `Testes/`, `Trabalho/`, `figuras/` |
| `<Disciplina>/.fonte/` | as fontes em Markdown (resumo, revisão, soluções, convenções) |
| `SOLUCOES.html` | soluções de todas as disciplinas, uma alínea de cada vez |
| `Quizrama/` | quizzes para os testes (Redes, Sistemas de Operações) |
| `_shared/template/` | scripts de build (pandoc + tectonic), preâmbulo e filtros |
| `_shared/site/` | gerador do site |

Disciplinas: Compiladores, IPM, Lógica Computacional, Redes de Comunicação,
Tecnologias Web.

## Gerar

```bash
_shared/template/build.sh <Disciplina>    # RESUMO, REVISAO e outros PDFs + SOLUCOES.html
_shared/template/fechar.sh <Disciplina>   # build + verificações (+ quiz, se houver)
_shared/template/site.sh                  # site em http://localhost:8000
```

Precisa de `pandoc`, `tectonic`, `graphviz` e `poppler`; o Quizrama usa Node
(`cd Quizrama && npm test`).
