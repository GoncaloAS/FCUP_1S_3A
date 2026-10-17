# Universidade — 3º Ano — Resumos de estudo

Cada disciplina tem um **PDF de resumo único e cumulativo**, que cresce
semana a semana com as aulas teóricas novas. O Gonçalo usa-o para as
práticas e para o exame sem voltar aos slides: tem de ser completo, bem
explicado e com diagramas quando ajudam. Para atualizar um resumo, invoca
sempre a skill `resumo-semanal` (`.claude/skills/resumo-semanal/SKILL.md`).

## Estrutura

```
<Disciplina>/
  Teoricas/Aula_NN.pdf        slides, um por aula (zero à esquerda)
  Praticas/Semana_N/...       labs/fichas: só servem para escolher os "Pratica agora"
  figuras/                    diagramas gerados (graphviz)
  .fonte/RESUMO_<D>.md        fonte do resumo (escondida; nunca apagar)
  .fonte/REVISAO_<D>.md       fonte da folha de revisão (2-3 páginas de receitas)
  .fonte/SOLUCOES_<D>.md      soluções dos "Pratica agora"
  .fonte/CONTEXTO_<D>.md      convenções e factos desta disciplina (não gera PDF)
  .fonte/.cache/              texto extraído dos slides (gerado, fora do git)
  RESUMO_<D>.pdf, REVISAO_<D>.pdf
_shared/template/             prep.sh, fechar.sh, contexto.sh, extrair.sh, build.sh, preâmbulos, filtros
SOLUCOES.html                 site único de soluções, um separador por disciplina (gerado)
Quizrama/                     quizzes de preparação para testes (redes.html; SO em index.html)
  tools/<d>-guide/            build.py (guia a partir do RESUMO) e perguntas.py (banco; editar aqui)
_shared/site/                 site para os colegas: build_site.py, design/ (tokens.css = design system), titulos.json
_site/                        site gerado (fora do git; o GitHub Actions publica-o no Pages a cada push)
```

## Site

Um site estático junta tudo para quem não usa o terminal: disciplinas →
resumo/revisão em HTML, slides e fichas num visualizador dentro do site,
soluções, quiz. Só modo escuro, design editorial (Charter/Avenir/Menlo, uma
cor por disciplina, sem gradientes nem sombras). Nada sai do site: o
resumo e a revisão aparecem em HTML (pandoc, os mesmos filtros do PDF) e em
PDF, e todos os PDFs abrem no `ver.html`. O site gera-se sozinho no GitHub
Actions a cada push; a skill `resumo-semanal` não lhe toca (só PDFs), e
afiná-lo é com a skill `site`, só quando o Gonçalo pedir. Ver localmente:
`_shared/template/site.sh`. O que se publica
está em `PUBLICAR`/`EXCLUIR` no `build_site.py` (nunca o CV/página pessoal).

**`.md` escondido**: o Gonçalo não quer ver `.md` ao navegar as pastas.
Qualquer documento de uma disciplina gera um PDF com o mesmo pipeline e a
fonte fica em `.fonte/`.

## Regra de ouro

- Um único documento por disciplina, que se estende. Matéria nova que se
  sobrepõe à antiga restrutura a secção existente e não a duplica.
- Não se omite matéria dos slides, mas também não há palha: compacto, com
  o menor número de páginas possível, sem texto cortado entre páginas.
- O que falta nos slides e é preciso para as práticas acrescenta-se e
  marca-se com †.
- Não há caixas de atenção nem de exame.
- Exercícios "Pratica agora" no fim de cada tópico. As soluções vão para o
  `SOLUCOES.html`, uma alínea de cada vez.

## Poupar tokens

- A sessão começa com `_shared/template/prep.sh <D>` (estado, extração dos
  slides para o cache, sobreposições, convenções) e acaba com
  `_shared/template/fechar.sh <D>` (build, verificações, soluções).
- Nunca ler o RESUMO inteiro nem os slides como imagem por defeito; o
  texto dos slides lê-se uma vez, do cache. Para o resto:
  `contexto.sh <D> [--mapa termos | termos | --indice | --sol]`.
- Poucas chamadas (cada uma reenvia o contexto todo): junta numa só
  resposta as que não dependem umas das outras. Edições cirúrgicas
  (`Edit`), uma disciplina por sessão e sem subagentes.

## Auto-melhoria

O feedback do Gonçalo sobre formato, estilo ou profundidade vira uma regra
curta no `SKILL.md` (ou num `ref/`) e passa a aplicar-se a todas as
disciplinas; se só vale para uma, vai para o `.fonte/CONTEXTO_<D>.md` dela.

## Quizrama (quizzes para testes)

O antigo projeto `~/Personal Projects/quizrama` vive agora em `Quizrama/`
(o histórico antigo está no GitHub, GoncaloAS/quizrama). Um quiz de uma
disciplina tem `Quizrama/tools/<d>-guide/`; o `fechar.sh` regenera o guia e
as perguntas e corre o `npm test`. Perguntas só da matéria do teste, ao estilo
do teste, com correção de todas as opções, link para a secção da teoria e a
posição da certa sorteada e equilibrada.
