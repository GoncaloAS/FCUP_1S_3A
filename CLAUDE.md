# Universidade — 3º Ano — Resumos de estudo

Este repositório organiza o material de cada disciplina do semestre e gera, para
cada uma, um **PDF de resumo único e cumulativo** que cresce semana a semana à
medida que novas aulas teóricas são adicionadas. O objetivo é que o Gonçalo
consiga acompanhar as práticas e preparar-se para o exame sem ter de voltar a
abrir os slides originais — o resumo tem de estar completo, bem explicado e
com diagramas/imagens sempre que ajudem a perceber a matéria.

A lógica é igual para todas as disciplinas. Este ficheiro é a "folha de
contexto" partilhada; os detalhes operacionais completos (como processar,
que caixas usar, como compilar) estão na skill `resumo-semanal`
(`.claude/skills/resumo-semanal/SKILL.md`) — invoca-a sempre que fores
atualizar um resumo.

## Estrutura de pastas

Cada disciplina segue esta convenção (adaptada à forma como o Gonçalo
organiza mesmo os ficheiros — segue o que existe, não impõe a tua ordem):

```
<Disciplina>/
  Teoricas/                <- todos os slides das aulas teóricas, um PDF por aula
    Aula_01.pdf               (nome fixo Aula_NN — não repete o nome da disciplina,
    Aula_02.pdf                já está na pasta; numeração com zero à esquerda)
    ...
  Praticas/
    Semana_1/                <- material da prática dessa semana
      <pasta-do-lab>/           (enunciado em PDF, código fornecido, testes, etc.)
    Semana_2/
    ...
  figuras/                 <- diagramas gerados (graphviz/matplotlib) usados no resumo
  .fonte/
    RESUMO_<Disciplina>.md  <- fonte única do resumo (cresce, nunca é substituída;
                                ESCONDIDA de propósito — o Gonçalo não quer ver .md
                                ao navegar a pasta, só o PDF)
  RESUMO_<Disciplina>.pdf  <- compilado a partir do .md acima, sempre visível
  SOLUCOES_<Disciplina>.html <- soluções dos exercícios "Pratica agora", uma
                                alínea de cada vez (fonte: .fonte/SOLUCOES_<Disciplina>.md)
```

O resumo cobre sempre as **teóricas** (`Teoricas/`). O material de
`Praticas/Semana_N/` (labs, enunciados práticos, código) não é reproduzido no
resumo — serve para perceber a que se deve ligar a explicação teórica (ver
regra em `SKILL.md`, secção "Ligação com a prática").

**Regra do `.md` escondido**: o Gonçalo não gosta de ver ficheiros `.md` —
prefere só PDFs quando navega uma disciplina. Mas o `.md` é a fonte editável
de que o workflow depende para continuar a estender o mesmo documento
semana a semana — nunca apagar, só esconder em `.fonte/`. Isto aplica-se a
**qualquer** `.md` de uma disciplina, não só ao `RESUMO_` — se precisares de
criar outro documento (calendário, enunciado de trabalho, etc.), gera o PDF
com o mesmo pipeline (`_shared/template/`) e esconde a fonte em `.fonte/`
da mesma forma.

_shared/template/
  preamble.tex   <- estilo LaTeX partilhado por todas as disciplinas (caixas, cores, fontes)
  div-envs.lua   <- filtro pandoc que converte ::: definicao ::: etc. em caixas
  build.sh       <- script de build: build.sh <Disciplina> (PDF + HTML de soluções)
  solucoes.html, solucoes.lua <- template/filtro do HTML de soluções

.claude/skills/resumo-semanal/SKILL.md  <- workflow detalhado + log de aprendizagens
```

Para começar uma disciplina nova, cria `<Disciplina>/` com a mesma estrutura e
usa o mesmo `_shared/template/`. Não é preciso duplicar preambulo nem filtro.

## Regra de ouro

**Um único documento por disciplina, que se estende.** Nunca criar um PDF por
aula. Quando chega matéria nova: adiciona ao `RESUMO_<Disciplina>.md`
existente; se a matéria nova sobrepõe-se ou clarifica algo já escrito,
**restrutura** essa secção em vez de duplicar. Não omitir informação dos
slides. Se faltar algo que os slides pressupõem mas não explicam (e que é
preciso para as práticas), acrescenta essa explicação e assinala-a como nota
adicional.

## Como pedir uma atualização

Basta dizer, por exemplo: *"atualiza o resumo de Compiladores com a Semana 2"*
ou *"já meti a Semana 3 de Compiladores, atualiza"*. Ver
`.claude/skills/resumo-semanal/SKILL.md` para o processo completo.

## Auto-melhoria

Sempre que o Gonçalo der feedback sobre o formato/estilo/profundidade dos
resumos (ex: "queria mais exemplos resolvidos", "isto ficou confuso", "não
precisas de incluir X"), esse feedback deve ser gravado na secção
"Aprendizagens" no fundo do `SKILL.md`, para se aplicar automaticamente a
todas as disciplinas dali em diante — não só à que originou o feedback.
