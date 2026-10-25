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
  .fonte/INFO_<D>.md          testes, prazos, avaliação, avisos do Moodle → INFO_<D>.pdf (skill moodle-refresh)
  .fonte/moodle/              estado do Moodle (estado.json) e fonte das páginas passadas a PDF
  .fonte/.cache/              texto extraído dos slides (gerado, fora do git)
  RESUMO_<D>.pdf, REVISAO_<D>.pdf
_shared/template/             prep.sh, fechar.sh, contexto.sh, extrair.sh, build.sh, preâmbulos, filtros
AGENDA.pdf                    datas de todas as disciplinas (testes, entregas), feita pelo moodle.py
_shared/moodle.json           UCs do Moodle seguidas (id do curso → pasta)
SOLUCOES.html                 site único de soluções, um separador por disciplina (gerado)
Quizrama/                     quizzes de preparação para testes (redes.html; SO em index.html)
  tools/<d>-guide/            build.py (guia a partir do RESUMO) e perguntas.py (banco; editar aqui)
_shared/site/                 o site do Gonçalo: build_site.py, design/ (tokens.css; pessoal.js, estudo.js), fichas.json, pessoal.enc
_site/                        site gerado (fora do git; o GitHub Actions publica-o no Pages a cada push)
```

## Site

O site é **do Gonçalo** (feito para as necessidades dele; se servir aos
colegas, melhor). Computador primeiro, só modo escuro, design editorial
(Charter/Avenir/Menlo, uma cor por disciplina). Início = painel pessoal
(próximos 14 dias, a fazer, chegou esta semana, avisos) + disciplinas; tudo em
**PDF** (sem HTML dos resumos) no `ver.html`; cada ficha com soluções abre no
`estudo.html` (PDF à esquerda, as soluções dela à direita; `fichas.json`).
O repositório é **público**: o pessoal (INFO, agenda, tarefas, avisos) só vai
cifrado em `_shared/site/pessoal.enc` (`_shared/template/pessoal.py`,
palavra-passe no Keychain `fcup-site`) e os `.md`/PDF pessoais estão no
`.gitignore`. Gera-se no GitHub Actions a cada push; o `moodle-refresh` e o
`resumo-semanal` acabam com commit + push. Afinar o site é com a skill `site`.
Ver localmente: `_shared/template/site.sh`. O que se publica está em
`PUBLICAR`/`EXCLUIR` no `build_site.py` (nunca o CV/página pessoal).

**`.md` escondido**: o Gonçalo não quer ver `.md` ao navegar as pastas.
Qualquer documento de uma disciplina gera um PDF com o mesmo pipeline e a
fonte fica em `.fonte/`.

## Moodle

O material novo vem do Moodle pela skill `moodle-refresh` (refresh semanal, todas
as disciplinas). Ela traz ficheiros e páginas para `Teoricas/`, `Praticas/`,
`Trabalho/` e `Testes/`, e guarda as datas e os avisos nos `INFO_<D>` e na `AGENDA`.
Não toca nos resumos: teóricas novas → `resumo-semanal`.

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
  Um hook (`.claude/hooks/ler_por_partes.py`) recusa PDFs inteiros e
  ficheiros > 40 KB sem `limit`; as deny rules tapam `_site/`,
  `SOLUCOES.html` e o que é gerado.
- Poucas chamadas (cada uma reenvia o contexto todo): junta numa só
  resposta as que não dependem umas das outras. Edições cirúrgicas
  (`Edit`), uma disciplina por sessão e sem subagentes.
- Uma tarefa por sessão: `/clear` entre disciplinas ou tarefas sem
  relação, `/compact` perto dos 70%. Trabalho mecânico (refresh do
  Moodle, builds) pode ir em Sonnet (`/model`); Opus para resumos e
  soluções.
- Browser: texto (`get_page_text`, JS) em vez de screenshots.
- Há sessões em paralelo nesta árvore: `git add` só por caminho (um hook
  recusa `git add -A`/`.` e o Co-Authored-By do Claude).
- Dúvida que só o Gonçalo decide: pergunta tudo numa só
  `AskUserQuestion` (opção recomendada primeiro) e continua o resto
  enquanto não responde.

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
Objetivo: quem faz o treino chega ao teste modelo e consegue fazer tudo, incluindo
as perguntas de desenvolvimento. Por isso o treino inclui perguntas de resposta aberta
com os exercícios das fichas que usam as mesmas técnicas, e o teste modelo tem as de
desenvolvimento. Enunciado da ficha/teste; resolução tirada do `SOLUCOES_<D>.md`
(a mesma do site); lista em `ABERTAS` no `perguntas.py`.
