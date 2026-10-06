---
name: resumo-semanal
description: Gera ou estende o resumo teórico cumulativo em PDF de uma disciplina a partir dos slides colocados em Teoricas/, e as soluções (uma alínea de cada vez) dos exercícios "Pratica agora" no site único SOLUCOES.html (todas as disciplinas, um separador por disciplina). Usar sempre que o Gonçalo adiciona material novo de uma disciplina (teóricas novas) e pede para atualizar o resumo, ou quando começa uma disciplina nova.
---

# Resumo semanal por disciplina

A estrutura de pastas está no `CLAUDE.md`. Aqui ficam o fluxo e as regras.
Os detalhes de consulta ocasional estão em `ref/` e **só se leem quando são
precisos**:

- `ref/formatacao.md`: caixas, bugs do pandoc, paginação, tabelas, figuras;
- `ref/build.md`: erros e AVISOs do build, diagnóstico, captura do site;
- `ref/fontes.md`: `.pptx`, `.cap`, PDFs que não são aulas, código dos
  slides;
- `ref/solucoes.md`: formato do `SOLUCOES_*.md`, Fitch, casos especiais.

## Poupar tokens (obrigatório)

- **Nunca ler o RESUMO inteiro.** Usa o `contexto.sh`, o `grep -n` e o
  `Read` com `offset`/`limit` só no troço que vais mudar.
- **Nunca ler os slides como imagem por defeito.** Usa primeiro o
  `extrair.sh`. Abre com `Read` + `pages` só os slides assinalados cujo
  diagrama, autómato, árvore ou tabela o texto não captou.
- **Editar, nunca reescrever.** Usa o `Edit` para inserir ou substituir um
  troço. Nunca faças `Write` do RESUMO inteiro.
- **Verificação automática primeiro.** Os AVISOs do `build.sh` e o
  `contexto.sh --sol` substituem o olhar para o PDF. Abre como imagem 1–2
  páginas só quando aparece um tipo de caixa, figura ou tabela novo.
  Capturas do site só quando muda o template.
- Uma disciplina por sessão e sem subagentes (cada um volta a ler tudo).

## Passo a passo

**0. Nomes.**
- Slides em `Teoricas/Aula_NN.pdf`. Um PDF com outro nome renomeia-se com
  `git mv` depois de ver a 1.ª página (`extrair.sh <pdf> 1 1`).
- O número é a **ordem em que as aulas foram dadas**, não o que está escrito
  no slide (os slides podem saltar números). Mandam o nome que o Gonçalo
  deu e a sequência já processada. Nunca digas que "falta uma aula" por
  causa de um salto. Na dúvida, pergunta.
- Material de prática fica em `Praticas/Semana_N/`.
- Qualquer `.md` de uma disciplina fica escondido em `.fonte/` (nunca se
  apaga) e só o PDF fica visível.
- Casos especiais (`.pptx`, `.cap`, livros): ver `ref/fontes.md`.

**1. Ver o que é novo.** Corre `bash _shared/template/contexto.sh <Disciplina>`.
- Mostra as aulas por processar, com as páginas, as semanas de prática e o
  índice do RESUMO (títulos e caixas `pratica`, com o número de linha).
- Se o RESUMO ainda não existir, cria-o com o esqueleto abaixo.

**2. Ler a aula nova.** Corre `bash _shared/template/extrair.sh <pdf>`.
- Lê o texto de **todos** os slides, sem saltar nenhum.
- Vê como imagem só os assinalados que precisam (ver "Poupar tokens").
- Um PDF grande lê-se por partes: `extrair.sh <pdf> 1 30`.
- Atenção a definições, algoritmos, exemplos do professor e exercícios.

**3. Encontrar sobreposições.** Faz uma lista dos conceitos-chave da aula e
corre `contexto.sh <Disciplina> termo1 termo2 ...`, que faz grep no RESUMO,
nas SOLUCOES e na REVISAO. Um conceito que já existe é aprofundado
**dentro da secção onde já está** (passo 4). Lê só essas linhas.

**4. Escrever** no `.fonte/RESUMO_<Disciplina>.md`, em português:
- **Compacto, sem palha.** Ficam de fora:
  - histórias, datas, citações e frases de efeito;
  - recapitulações e frases "como vimos em X";
  - comentários sobre gralhas dos slides (corrigem-se em silêncio);
  - curiosidades que não fazem falta nas práticas.

  Cada ideia diz-se uma vez, no sítio certo. Menos páginas é melhor.
- **Não omitir matéria.** Todas as definições, teoremas e algoritmos dos
  slides aparecem, explicados por palavras próprias, com o "porquê" e não
  só o "o quê".
- **Lacunas com †.** O que os slides pressupõem sem explicar, mas faz
  falta, vai no texto normal ou na caixa de definição, marcado com † (no
  título ou depois do primeiro negrito). Não há caixas de "nota adicional".
- **Exemplos resolvidos totalmente explícitos.** Há pelo menos um por cada
  algoritmo ou procedimento.
  - Mostra **cada** caso e cada cálculo intermédio. Nunca escrevas
    "repetindo para os restantes...".
  - Se não couber numa caixa, divide-o em duas caixas `exemplo` seguidas,
    sem cortar detalhe.
  - No fim, relê-o como o Gonçalo: nenhum passo pode exigir "confiar".
  - Código dado nos slides **traça-se com um input concreto, linha a
    linha**. Se puderes, corre-o.
- **Diagramas sempre que ajudem**, mesmo que não estejam nos slides
  (graphviz, em `figuras/`; ver `ref/formatacao.md`).
- **Uma linha contínua de estudo.** Matéria que aprofunda, corrige ou
  contradiz um tópico já escrito funde-se na secção existente, mesmo que
  seja preciso reescrevê-la ou mudá-la de sítio. Nunca há duas explicações
  do mesmo tópico.
  - Se um módulo revisita o processo inteiro, distribui-se pelas secções de
    cada etapa e a secção nova termina com uma tabela "conteúdo → onde
    está".
  - Se há uma contradição aparente entre aulas, explica no texto como os
    dois pontos se conciliam e marca-o como interpretação.
- `#`/`##`/`###` = Aula / Tópico / Subtópico (`# Aula N --- título`).
- Caixas (`definicao`, `exemplo`, `pratica`) com moderação. **Não há caixas
  de atenção nem de exame.** Um aviso que faz falta vai para o texto.
  Instruções de instalação de um lab vão para a caixa `pratica` desse lab.
- Antes de escrever uma caixa, uma tabela ou uma lista de alíneas, revê os
  bugs do pandoc em `ref/formatacao.md`. Os mais comuns:
  - `title="--- X"`, sem espaço depois das aspas;
  - alíneas em negrito, `**(a)**`;
  - uma linha em branco antes de uma lista.

**5. Prática: caixas `pratica` no fim de CADA tópico, nunca no fim da aula.**
- Ficam no fim do `##` (ou do `###`) cuja matéria aplicam. Cada exercício
  leva a técnica que usa e, se for útil, uma pista, mas nunca a resposta.
- Um exercício que precisa de vários tópicos vai para o último deles, e a
  caixa diz o que mais usa.
- Nunca há secções "Ligação com a prática" ou "Para fazeres sozinho". No
  fim da aula, no máximo uma frase sobre os exercícios que ficam de fora.
- Mistura de **resolvidos** e **sugeridos**:
  - os resolvidos (caixas `exemplo`, antes da `pratica`) podem ser
    exercícios reais do lab, com a origem no título;
  - deixa sempre algum exercício parecido só sugerido.
- **Não repetir trabalho.** Num exercício com muitas alíneas da mesma
  técnica, escolhe só as que trazem ideias diferentes: resolvidas e
  sugeridas somam ~4–6. Diz que as outras são a mesma técnica.
- **Método certo.** Usa o método que o enunciado pede ("using
  equivalences", "truth tables"...), ou o da aula a que o exercício
  pertence. O exercício só aparece **depois** do tópico que ensina esse
  método.
- **Estilo de exame.** Prova formal com a notação do professor, cada passo
  justificado por uma lei ou definição que ele conhece (uma de cada vez,
  com os papéis identificados). Uma lei extra só aparece como atalho
  depois da derivação oficial. Segue a skill `resolver-exercicio`.
- **Soluções**: cada item de cada caixa tem solução em
  `.fonte/SOLUCOES_<Disciplina>.md`, escrita na mesma passagem e
  verificada. Formato e regras em `ref/solucoes.md`.

**6. Compilar.** Corre `bash _shared/template/build.sh <Disciplina>`.
- Gera o RESUMO, a REVISAO se existir, e o `SOLUCOES.html`.
- **Qualquer AVISO é bloqueante**: caixa cortada, sem glifo, fora da
  margem, markdown por converter, contagem de `pratica` ≠ `##`. Ver
  `ref/build.md`.
- Em Lógica, corre antes o `_shared/tools/fitch_check.py` sobre o RESUMO e
  as SOLUCOES.

**7. Folha de revisão.** Acrescenta as receitas novas ao
`.fonte/REVISAO_<Disciplina>.md`, se existir: 2–3 páginas, só receitas,
regras e tabelas, só `##` (sem `# Aula`).

**8. Fechar.**
- `contexto.sh <Disciplina> --sol`: cada alínea das caixas tem de ter o seu
  `####` e o seu id no site. Se faltar alguma, a tarefa não está feita.
- Atualiza o `<!-- processado: ... -->` e o `date:` do RESUMO, e o `date:`
  das SOLUCOES se mudou.

## Esqueleto (disciplina nova)

```markdown
---
title: "<Disciplina> (<código>) --- Resumo Teórico"
author: "Gonçalo Sousa"
date: "Atualizado: Semana N"
---

<!-- processado: Teoricas/Aula_01.pdf -->

# Aula 1 --- <título>
```

Uma disciplina nova entra sozinha no site de soluções quando ganha o seu
`SOLUCOES_*.md`. Junta-a a `ESTILO_V2` no `build.sh`.

## Auto-melhoria

Quando o Gonçalo dá feedback sobre o resultado, transforma-o numa **regra
de uma ou duas linhas**: no passo certo acima se for geral, ou no `ref/`
certo se for um detalhe técnico. Não escrevas a história do episódio. A
lista abaixo só serve para regras que não cabem em nenhum outro sítio.
Aplica-se a todas as disciplinas.

### Aprendizagens

- Depois de um build "com sucesso", o PDF pode estar errado na mesma. Se o
  AVISO automático não cobre o sintoma, acrescenta uma verificação ao
  `build.sh` em vez de passar a inspecionar à mão.
- Gastar tokens com moderação (2026-10-06): seguir a secção "Poupar
  tokens". Quando se descobre um passo repetitivo e caro, o sítio dele é
  um script em `_shared/template/`.
