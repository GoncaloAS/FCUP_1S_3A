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
  REVISAO_<Disciplina>.pdf <- folha de revisão para o exame, 2-3 páginas só com
                              receitas (fonte: .fonte/REVISAO_<Disciplina>.md)
  (.fonte/SOLUCOES_<Disciplina>.md <- fonte das soluções dos exercícios "Pratica
                                agora" desta disciplina; vão para o SOLUCOES.html)
```

O resumo cobre sempre as **teóricas** (`Teoricas/`). O material de
`Praticas/Semana_N/` (labs, enunciados práticos, código) não é reproduzido no
resumo. Serve para escolher os exercícios das caixas "Pratica agora", que
ficam no fim de cada tópico e nunca agrupados no fim. As soluções de todos
eles vão para o **site único `SOLUCOES.html`** (na raiz, um separador por
disciplina, uma alínea de cada vez), a partir de
`.fonte/SOLUCOES_<Disciplina>.md`. Não há um HTML de soluções por
disciplina (ver `SKILL.md`, passo 7).

**Regra do `.md` escondido**: o Gonçalo não gosta de ver ficheiros `.md` —
prefere só PDFs quando navega uma disciplina. Mas o `.md` é a fonte editável
de que o workflow depende para continuar a estender o mesmo documento
semana a semana — nunca apagar, só esconder em `.fonte/`. Isto aplica-se a
**qualquer** `.md` de uma disciplina, não só ao `RESUMO_` — se precisares de
criar outro documento (calendário, enunciado de trabalho, etc.), gera o PDF
com o mesmo pipeline (`_shared/template/`) e esconde a fonte em `.fonte/`
da mesma forma.

_shared/template/
  preamble.tex   <- estilo LaTeX antigo (disciplinas ainda não convertidas)
  preamble-v2.tex <- estilo novo (Charter/Avenir/Menlo, compacto, sem caixas de
                    atenção/exame); ativo para as disciplinas em ESTILO_V2 no build.sh
  div-envs.lua   <- filtro pandoc que converte ::: definicao ::: etc. em caixas
  build.sh       <- script de build: build.sh <Disciplina> (PDF + site de soluções)
  build_solucoes.py <- junta todos os .fonte/SOLUCOES_*.md em SOLUCOES.html
  solucoes.html, solucoes-disciplina.html, solucoes.lua <- página/bloco/filtro do site

SOLUCOES.html    <- site único com as soluções de TODAS as disciplinas (gerado)

.claude/skills/resumo-semanal/SKILL.md  <- workflow detalhado + log de aprendizagens
```

Para começar uma disciplina nova, cria `<Disciplina>/` com a mesma estrutura e
usa o mesmo `_shared/template/`. Não é preciso duplicar preambulo nem filtro.

## Regra de ouro

**Um único documento por disciplina, que se estende.** Nunca criar um PDF por
aula. Quando chega matéria nova: adiciona ao `RESUMO_<Disciplina>.md`
existente; se a matéria nova sobrepõe-se ou clarifica algo já escrito,
**restrutura** essa secção em vez de duplicar. Não omitir matéria dos
slides, mas sem palha: nada de histórias, datas, curiosidades, repetições
nem recapitulações; o resumo é compacto e com o menor número de páginas
possível, sem nunca cortar texto entre páginas. Se faltar algo que os slides
pressupõem mas não explicam (e que é preciso para as práticas), acrescenta
essa explicação no texto e assinala-a com †. Não há caixas de atenção nem
de exame.

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
