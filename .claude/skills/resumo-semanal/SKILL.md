---
name: resumo-semanal
description: Gera ou estende o resumo teórico cumulativo em PDF de uma disciplina a partir dos slides colocados numa pasta Semana_N. Usar sempre que o Gonçalo adiciona material novo de uma disciplina (teóricas novas) e pede para atualizar o resumo, ou quando começa uma disciplina nova.
---

# Resumo semanal por disciplina

Workflow para transformar slides de aulas teóricas num único documento de
estudo em PDF, por disciplina, que se estende ao longo do semestre. Ver
`CLAUDE.md` na raiz do repositório para a visão geral e a estrutura de pastas.

## Quando isto é invocado

- O Gonçalo colocou slides novos em `<Disciplina>/Teoricas/` e pede para
  atualizar o resumo.
- É a primeira vez que se processa uma disciplina (a pasta ainda não tem
  `RESUMO_<Disciplina>.md`) — nesse caso, cria-se a estrutura de raiz.

## Passo a passo

### 1. Descobrir o que é novo

Abre `<Disciplina>/RESUMO_<Disciplina>.md` (se existir) e olha para o
cabeçalho HTML-comment `<!-- processado: ... -->` no topo do ficheiro — lista
os ficheiros de origem já incorporados. Compara com o conteúdo de
`<Disciplina>/Teoricas/`. Processa apenas os PDFs que ainda não constam dessa
lista (evita reprocessar e duplicar secções). Se houver também uma
`Semana_N/` nova com material de prática, não a "processes" para o resumo —
usa-a só para escrever a secção "Ligação com a prática" (passo 8).

Se o ficheiro RESUMO ainda não existir, cria-o com o cabeçalho YAML +
comentário de processados vazio (ver "Esqueleto do ficheiro" abaixo) antes de
começar a escrever conteúdo.

**Antes de escrever, varre o documento inteiro à procura de sobreposição de
tópicos** — não só o cabeçalho de processados (que só diz que ficheiros
já foram incorporados, não onde cada tópico foi parar). Faz uma lista
mental dos conceitos-chave da aula nova (ex: "autómatos", "FIRST/FOLLOW",
"tabela de símbolos") e procura-os no resto do `.md` (`grep -i` pelo termo
chega). Isto é o que permite decidir, no passo 3, se um tópico é
genuinamente novo ou se é uma continuação/aprofundamento de algo já
escrito noutra secção.

### 2. Ler o material de origem por completo

Lê **todas as páginas** de cada PDF novo (usa `pages` do Read por blocos de
até 20 páginas se o PDF for grande — nunca só as primeiras páginas). Não
saltes slides. Presta atenção a: definições formais, algoritmos passo-a-passo,
exemplos que o professor resolveu, diagramas/figuras já existentes, e a
quaisquer exercícios de prática incluídos.

### 3. Escrever/estender o Markdown

Escreve diretamente no `RESUMO_<Disciplina>.md`, em português, denso mas
claro — o objetivo é que o Gonçalo NÃO precise de voltar aos slides. Regras:

- **Não omitir informação.** Todas as definições, teoremas e algoritmos dos
  slides têm de aparecer, explicados por palavras próprias (não copiar o
  slide telegráfico — desenvolver o raciocínio, o "porquê", não só o "o quê").
- **Preencher lacunas.** Se um slide assume conhecimento que não explica mas
  que é necessário para as práticas ou para perceber o resto, acrescenta essa
  explicação. Marca-a claramente, por exemplo dentro de uma caixa `atencao`
  com o prefixo "Nota adicional (não estava explícito nos slides):".
- **Exemplos resolvidos sempre que houver um algoritmo ou procedimento —
  e têm de ficar totalmente explícitos.** Mesmo que o Gonçalo vá resolver
  os exercícios de prática sozinho, o resumo tem de ter pelo menos um
  exemplo completo e resolvido passo-a-passo por conceito processual (ex:
  construir um NFA por Thompson, determinizar, minimizar, calcular
  FIRST/FOLLOW, etc.). **"Totalmente explícito" quer dizer: o Gonçalo lê o
  exemplo e percebe, sem ter de imaginar/reconstruir nenhum passo na
  cabeça.** Nunca escrever coisas como "repetindo o processo para os
  restantes estados obtém-se..." ou "de forma semelhante, os outros casos
  dão..." — mostra **cada** caso, um a um, com o cálculo intermédio visível
  (ex: numa construção de subconjuntos, mostra o `move` e o `closure` de
  **cada** estado novo com **cada** símbolo, não só do primeiro). Se isso
  tornar uma única caixa demasiado longa para uma página, divide em duas
  caixas `exemplo` consecutivas (continuação) em vez de resumir o resto —
  nunca sacrifiques detalhe por causa do tamanho da caixa. Antes de dar o
  exemplo por terminado, relê-o do zero como se fosses o Gonçalo: se algum
  passo exige "confiar" no resultado sem ver como se chegou lá, falta
  trabalho.
- Ao escrever um exemplo com código dado nos slides (não escrito por ti),
  **traça a execução real** com um input concreto, linha a linha — não
  assumas o que o código faz só pela leitura; simula-o mentalmente com
  cuidado (isto já apanhou um erro real: um pseudo-código dos slides
  parecia aceitar só no fim do input, mas na verdade fazia
  `return ACCEPT` no primeiro estado final atingido, muito antes disso).
- **Diagramas sempre que ajudarem**, mesmo que não existam nos slides
  (autómatos, árvores sintáticas, diagramas de fases, grafos de dependência).
  Ver secção "Diagramas" abaixo.
- **Se houver sobreposição, aprofundamento ou correção de conteúdo já
  escrito** (a aula nova volta a tocar num conceito de uma aula anterior —
  clarifica-o, contradiz-o, ou simplesmente ensina mais sobre ele),
  **funde tudo numa única secção contínua**, reestruturando a secção antiga
  em vez de criar uma segunda explicação do mesmo tópico noutro sítio do
  documento. O documento tem de se ler como **uma linha contínua de
  estudo**, não como um histórico cronológico de adições — nunca podes ter,
  por exemplo, autómatos DFA explicados de uma maneira na página 1 e o
  mesmo tópico (DFA) explicado outra vez, de forma diferente ou só
  parcialmente sobreposta, na página 20. Se a aula nova ensina mais sobre
  um conceito já presente, o sítio certo para esse conteúdo novo é **dentro
  da secção existente desse conceito** (reescrevendo-a para incorporar
  tudo coerentemente), mesmo que isso signifique mover a secção de posição
  ou reescrevê-la de raiz — nunca acrescentar uma secção nova com o mesmo
  nome ou o mesmo assunto mais à frente no ficheiro.
- Usa `#`/`##`/`###` para Aula / Tópico / Subtópico. Cada aula é uma secção
  `## Aula N — <título>` para o índice ficar navegável.
- Usa as caixas semânticas (ver abaixo) com moderação — só quando o conteúdo
  realmente pede aquele destaque, não em todos os parágrafos.

### 4. Caixas disponíveis

Definidas em `_shared/template/preamble.tex`, convertidas pelo filtro
`_shared/template/div-envs.lua`. Sintaxe no Markdown:

```
::: definicao
Conteúdo markdown normal aqui (negrito, $math$, etc. funcionam).
:::

::: exemplo
Exemplo resolvido passo-a-passo.
:::

::: atencao
Erro comum ou nota adicional preenchida por ti.
:::

::: exame
Algo que o professor sublinhou como importante para o exame, ou que é
claramente um padrão recorrente de exame.
:::

::: {.definicao title="--- Autómato finito"}
Caixa com título extra (aparece como "Definição --- Autómato finito").
:::
```

**Cuidado (bug de parsing do pandoc já apanhado):** no atributo
`title="..."`, o **primeiro caráter a seguir às aspas de abertura não pode
ser um espaço** — `title=" --- X"` faz o pandoc falhar silenciosamente o
parsing do fenced div inteiro (o bloco sai como texto em bruto, incluindo
os `:::` literais, sem erro nenhum). Escreve sempre `title="--- X"` (traço
colado às aspas), nunca `title=" --- X"`.

Não uses `implicit_figures` — uma imagem numa caixa não deve ser a única
coisa do parágrafo com legenda automática (isso parte a compilação, floats
não cabem dentro de tcolorbox). Escreve `![](figuras/x.pdf){width=50%}` sem
depender da legenda automática; se precisares de legenda, escreve-a à mão
como texto em itálico na linha a seguir.

**Paginação (já configurada no `preamble.tex`, não mexer sem motivo):**
as caixas (`definicao`/`exemplo`/`atencao`/`exame`) são propositadamente
**não-quebráveis** (sem a opção `breakable`) — uma caixa nunca parte entre
duas páginas, o LaTeX empurra-a inteira para a página seguinte se não
couber. E cada `# Aula N` força uma página nova (`\clearpage` antes de
`\section`), para o índice levar sempre a um topo de página. Consequência
prática para quem escreve o Markdown: **uma caixa individual tem de caber
numa única página** — se um exemplo ficar demasiado longo, corta-o em duas
caixas `exemplo` consecutivas em vez de deixar uma caixa gigante (que ou
transborda da página, ou deixa muito espaço em branco na página anterior).

### 5. Diagramas

- **Autómatos, grafos, árvores** → gera um `.dot` e compila com
  `dot -Tpdf ficheiro.dot -o <Disciplina>/figuras/nome.pdf` (graphviz já
  instalado via Homebrew). Usa `rankdir=LR` para autómatos ficarem legíveis.
- **Gráficos matemáticos/estatísticos** → só se necessário instalar
  `matplotlib` via pip nesse momento (ainda não está instalado por omissão).
- Guarda sempre os diagramas em `<Disciplina>/figuras/`, com nomes descritivos
  (`nfa_thompson_ab.pdf`, não `fig1.pdf`), para poderes referenciá-los ou
  regenerá-los mais tarde.

### 6. Compilar o PDF

```
bash _shared/template/build.sh <Disciplina>
```

Corre a partir da raiz do repositório. Confirma que não há erros do tectonic
(a primeira compilação por máquina pode demorar mais — vai buscar pacotes
LaTeX à medida que são precisos). Se houver erro de LaTeX, o mais comum é:
- imagem dentro de caixa a gerar `figure` float → falta `-f
  markdown-implicit_figures` (já está no build.sh, não removas);
- pacote a colidir com o que o pandoc já carrega por defeito (ex: babel,
  fontenc) → não adicionar esses pacotes ao `preamble.tex`, o pandoc já trata
  disso via `-V lang=pt-PT` com o motor tectonic/xetex.

**Um build sem erros não chega.** Depois de compilar, usa o Read sobre o
PDF gerado e inspeciona visualmente pelo menos as páginas com caixas novas
— um fenced div malformado (ex: erro de sintaxe no atributo `title=`) não
causa erro nenhum no tectonic, só faz a caixa sair como texto em bruto
com `:::` literais. Isso só se apanha a olhar para o resultado.

### 7. Ligação com a prática (sem resolver a prática)

Se a semana tiver uma pasta `Semana_N/` com enunciado/lab, acrescenta no fim
da secção da(s) aula(s) correspondente(s) um parágrafo curto "Ligação com a
prática" a apontar que exercício usa que conceito (ex: "o Exercício 3 do lab
usa a secção Flex acima"). **Não resolvas os exercícios da prática por ele**
— o Gonçalo prefere tentar sozinho depois de ler o resumo. Se um exercício
pede algo estruturalmente idêntico a um exemplo já resolvido no resumo (ex:
escrever uma expressão regular parecida), usa um exemplo *análogo* com dados
diferentes para ilustrar a técnica, não o mesmo enunciado.

### 8. Atualizar o cabeçalho de processados

Depois de compilar com sucesso, atualiza o comentário no topo do `.md` com os
novos ficheiros de origem incorporados (para a próxima invocação saber o que
já está feito), e atualiza a data no cabeçalho YAML (`date:`).

## Esqueleto do ficheiro (nova disciplina)

```markdown
---
title: "<Disciplina> (<código>) --- Resumo Teórico"
author: "Gonçalo Sousa"
date: "Atualizado: Semana N"
---

<!-- processado: Semana_1/Ficheiro1.pdf, Semana_1/Ficheiro2.pdf -->

# Aula 1 --- <título>

...
```

## Auto-melhoria

Sempre que o Gonçalo der feedback direto sobre o resultado (formato,
profundidade, quantidade de exemplos, tom, etc.), regista aqui uma regra nova
na secção abaixo, com a data, para se aplicar a **todas** as disciplinas a
partir daí — não só à que originou o feedback. Não apagues entradas antigas
a não ser que sejam explicitamente substituídas por feedback mais recente.

### Aprendizagens

- 2026-09-21: Configuração inicial. Motor de PDF: pandoc + tectonic (LaTeX,
  boa tipografia matemática). Diagramas gerados sempre que ajudam à
  compreensão, mesmo sem existirem nos slides. Práticas ficam de fora do
  documento — mas todo o conteúdo processual (algoritmos, construções) deve
  incluir pelo menos um exemplo resolvido passo-a-passo dentro do resumo, para
  o Gonçalo perceber o mecanismo antes de tentar os exercícios sozinho.
- 2026-09-21: Primeira aplicação real (Compiladores, Aulas 1-3) confirmou a
  estrutura de pastas real que o Gonçalo usa: `Teoricas/` (todos os slides,
  flat) + `Semana_N/<nome-do-lab>/` (material da prática) — já refletido no
  `CLAUDE.md`. Também confirmou o bug de parsing do pandoc documentado acima
  (`title=" ---"` com espaço a seguir às aspas parte o fenced div
  silenciosamente) — foi apanhado só ao inspecionar visualmente o PDF
  gerado, não por nenhum erro de build. Lição: depois de compilar, **lê
  sempre visualmente pelo menos as primeiras páginas do PDF** (não só
  confirmar que o `tectonic` não deu erro) — um build "com sucesso" pode na
  mesma conter caixas por converter.
- 2026-09-21: Feedback direto do Gonçalo depois de ver o PDF da Compiladores:
  (1) os exemplos resolvidos tinham passos implícitos ("repetindo o processo
  para os restantes obtém-se...") que o obrigavam a imaginar o raciocínio —
  quer tudo explícito, sem ter de reconstruir nada na cabeça; (2) caixas
  estavam a partir-se a meio entre duas páginas; (3) uma "Aula" nova podia
  começar a meio de uma página, dificultando saltar para lá a partir do
  índice. Resolvido de forma permanente: preamble.tex deixou de marcar as
  caixas como `breakable` (agora nunca partem — ver secção "Caixas
  disponíveis" acima) e cada `\section` (Aula) passou a forçar
  `\clearpage`. Fica como regra geral, não só para Compiladores. Nota
  meta: isto foi apanhado só depois de gerar o PDF errado uma primeira vez
  — o ideal é já escrever os exemplos ao nível de detalhe pedido (ver regra
  em "Escrever/estender o Markdown" acima) da primeira vez, não como
  correção a posteriori.
- 2026-09-22: Primeira aplicação a IPM (Módulos 01--02) apanhou um novo bug
  de parsing do pandoc, também silencioso (sem erro no build): dentro de
  uma caixa (`::: definicao`/`atencao`/etc.), quando um parágrafo curto que
  termina em ":" (ex: `**Evitar:**`) é imediatamente seguido, **sem linha em
  branco**, por uma lista com `-`, o pandoc não reconhece a lista como bloco
  novo — funde tudo num único parágrafo, e os `-` saem como texto corrido
  ("- Item um. - Item dois.") em vez de bullets. Isto só acontece quando a
  linha anterior é texto solto (um parágrafo); quando a linha anterior é a
  própria abertura do fenced div (`::: {.definicao ...}`) a lista funciona
  bem mesmo sem linha em branco a seguir — só entre "parágrafo → lista" é
  preciso a linha em branco, não entre "abertura de caixa → lista" nem
  entre "item de lista → item de lista seguinte". Regra a aplicar sempre:
  sempre que escrever um mini-título em negrito dentro de uma caixa (ex:
  `**Permitido:**`, `**Evitar:**`) seguido de uma lista, deixar sempre uma
  linha em branco entre os dois. Tal como o bug do `title=" ---"`, isto só
  se apanhou ao inspecionar visualmente o PDF gerado, não por nenhum erro
  de build — reforça a regra já existente de ler sempre o PDF página a
  página antes de dar a tarefa por concluída.
- 2026-09-22: Feedback direto do Gonçalo, ao pedir a atualização de
  Compiladores com a Aula 4: o documento tem de ser **uma linha contínua de
  estudo**, nunca um histórico de adições. Se matéria nova toca num tópico
  já tratado numa aula anterior (mesmo que só o aprofunde, sem o
  contradizer), a secção antiga tem de ser reestruturada/fundida com o
  novo conteúdo — nunca criar uma segunda explicação do mesmo tópico
  noutra parte do documento (ex.: não vale ter autómatos DFA explicados na
  página 1 e autómatos DFA outra vez, de forma diferente, na página 20).
  Isto já estava implícito no processo (secção "Escrever/estender o
  Markdown"), mas o Gonçalo pediu para ficar explícito — ver a regra
  reforçada acima e o novo passo de "varrer o documento à procura de
  sobreposição" antes de escrever (passo 1). Aplica-se a todas as
  disciplinas, não só a Compiladores.
