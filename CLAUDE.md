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
  RESUMO_<D>.pdf, REVISAO_<D>.pdf
_shared/template/             build.sh, contexto.sh, extrair.sh, preâmbulos, filtros
SOLUCOES.html                 site único de soluções, um separador por disciplina (gerado)
```

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

- Nunca ler o RESUMO inteiro nem os slides como imagem por defeito. Usa:
  - `_shared/template/contexto.sh <D> [termos | --sol]`: estado, índice e
    greps;
  - `_shared/template/extrair.sh <pdf>`: texto dos slides e os slides a ver
    como imagem.
- Faz edições cirúrgicas (`Edit`), uma disciplina por sessão e sem
  subagentes.

## Auto-melhoria

O feedback do Gonçalo sobre formato, estilo ou profundidade vira uma regra
curta no `SKILL.md` (ou num `ref/`) e passa a aplicar-se a todas as
disciplinas.
