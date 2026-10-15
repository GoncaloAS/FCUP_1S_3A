---
name: resumo-semanal
description: Gera ou estende o resumo teórico cumulativo em PDF de uma disciplina a partir dos slides colocados em Teoricas/, e as soluções (uma alínea de cada vez) dos exercícios "Pratica agora" no site único SOLUCOES.html (todas as disciplinas, um separador por disciplina). Usar sempre que o Gonçalo adiciona material novo de uma disciplina (teóricas novas) e pede para atualizar o resumo, ou quando começa uma disciplina nova.
---

# Resumo semanal por disciplina

A estrutura de pastas está no `CLAUDE.md`. Detalhes em `ref/`, **só quando
são precisos**: `formatacao.md` (caixas, pandoc, figuras), `build.md`
(AVISOs), `fontes.md` (livros, enunciados, disciplina nova), `solucoes.md`
(formato das soluções). O que é de **uma só** disciplina (nomes, numeração,
notação, ferramentas, projeto) está no `.fonte/CONTEXTO_<D>.md`, que o
`prep.sh` mostra; regras novas dessas vão para lá.

## Poupar tokens (obrigatório)

Cada chamada reenvia o contexto inteiro: **poucas chamadas** pesa mais do
que tudo o resto.
- Junta numa só resposta as chamadas independentes (ler o cache + `git mv`;
  `--mapa` + `Read` do troço; escrever RESUMO, SOLUCOES e REVISAO).
- Slides: só o cache, lido uma vez. Depois de um `git mv`, não voltes a
  correr o `prep.sh`: o cache com o nome antigo serve.
- Imagens só quando o texto refere o que não traz (diagrama, árvore,
  autómato, valores de tabela, captura de código); atividades e perguntas à
  turma não. Figuras graphviz não se veem: o `fechar.sh` diz a página e
  avisa se a letra ficar pequena.
- RESUMO nunca inteiro: `Read` com `offset`/`limit` só do troço a mudar.
  PDF grande ou suplementar: `grep -n` no cache e ler só esses troços.
- `Edit` num troço; nunca `Write` do RESUMO. Uma disciplina por sessão, sem
  subagentes. Os AVISOs substituem olhar para o PDF.

## Passo a passo

**1. Arrancar:** `bash _shared/template/prep.sh <D>`. Mostra o que é novo
(ficheiros fora do esquema com a 1.ª linha e o número livre), extrai para o
cache, o índice (`contexto.sh <D> --indice` dá os `###`), o mapa de
sobreposições, a numeração das soluções e o `CONTEXTO_<D>`.

Nomes: slides em `Teoricas/Aula_NN.pdf` (`git mv`). O número é a **ordem
em que as aulas foram dadas**, não o do slide (podem saltar números; nunca
digas que "falta uma aula"). Mandam o nome que o Gonçalo deu e a sequência
já processada; na dúvida, pergunta. Prática em `Praticas/Semana_N/`.
Qualquer `.md` fica em `.fonte/` (nunca se apaga); só o PDF fica visível.

**2. Ler a aula nova:** o cache `.fonte/.cache/<aula>.txt`, inteiro (por
partes com `offset` se for grande), **todos** os slides. Atenção a
definições, algoritmos, exemplos do professor e exercícios.

**3. Sobreposições.** Parte do mapa do `prep.sh`. Para os conceitos que
faltam (em português, se os slides forem noutra língua):
`contexto.sh <D> --mapa termo1 termo2 ...` (sem acentos nem maiúsculas,
REVISAO primeiro; `contexto.sh <D> termo` dá as linhas). Um conceito que já
existe aprofunda-se **dentro da secção onde já está**.

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
  - nada de `% # & _ $` em `title=`;
  - alíneas em negrito, `**(a)**`, no início da linha;
  - uma linha em branco antes de uma lista;
  - imagens `![](figuras/x.pdf){width=N%}` com a legenda em itálico na
    linha a seguir.

  O resto de `ref/formatacao.md` só se lê com um AVISO ou um tipo de caixa,
  tabela ou figura novo.

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
- **Soluções oficiais** (ex. `Praticas/Semana_N/*_resolv.pdf`) são a
  referência de forma e de tamanho: quando aparece uma, compara-a com as
  nossas, grava a forma na `resolver-exercicio` e reescreve as que
  divergem.
- **Testes modelo** (enunciado + resolução) vão para `<D>/Testes/`. Cada
  pergunta de desenvolvimento entra como exercício na caixa do seu tópico
  e a escolha múltipla numa caixa no fim. O formato do teste (duração,
  calculadora, descontos) vai para o `CONTEXTO_<D>` e para a caixa da
  escolha múltipla, não para a REVISAO (que não passa das 3 páginas).
- **Soluções**: cada item de cada caixa tem solução em
  `.fonte/SOLUCOES_<Disciplina>.md`, escrita na mesma passagem e
  verificada. Formato e regras em `ref/solucoes.md`; a numeração e um
  exemplo-modelo estão no `CONTEXTO_<D>`.

**6. Folha de revisão.** Acrescenta as receitas novas ao
`.fonte/REVISAO_<Disciplina>.md`, se existir: 2–3 páginas, só receitas,
regras e tabelas, só `##` (sem `# Aula`).

**7. Fechar:** `bash _shared/template/fechar.sh <D> --aula
Teoricas/Aula_NN.pdf --data "Semana N (...)"`, uma vez. Atualiza o
`<!-- processado -->` e o `date:`, corre Fitch/tableaux (Lógica), mede a
letra das figuras novas, compila tudo (filtrado) e faz o `--sol`.
- **Qualquer AVISO ou FALTA é bloqueante** (caixa cortada, sem glifo, fora
  da margem, markdown por converter, letra < 7 pt, `pratica` ≠ `##`, alínea
  sem `####`; ver `ref/build.md`). Corrige e volta a correr.
- O `date:` das SOLUCOES muda-se à mão, se mudou. Se mudou uma convenção ou
  um facto da disciplina, atualiza o `CONTEXTO_<D>.md`.

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
- Gastar tokens com moderação (2026-10-06, 2026-10-12): seguir a secção
  "Poupar tokens". Quando se descobre um passo repetitivo e caro, o sítio
  dele é um script em `_shared/template/` (`prep.sh`, `fechar.sh`), não
  uma regra para fazer à mão.
