---
name: resumo-semanal
description: Gera ou estende o resumo teórico cumulativo em PDF de uma disciplina a partir dos slides colocados em Teoricas/. Usar sempre que o Gonçalo adiciona material novo de uma disciplina (teóricas novas) e pede para atualizar o resumo, ou quando começa uma disciplina nova.
---

# Resumo semanal por disciplina

Workflow para transformar slides de aulas teóricas num único documento de
estudo em PDF, por disciplina, que se estende ao longo do semestre. Ver
`CLAUDE.md` na raiz do repositório para a visão geral e a estrutura de pastas.

## Quando isto é invocado

- O Gonçalo colocou slides novos em `<Disciplina>/Teoricas/` e pede para
  atualizar o resumo.
- É a primeira vez que se processa uma disciplina (a pasta ainda não tem
  `.fonte/RESUMO_<Disciplina>.md`) — nesse caso, cria-se a estrutura de raiz.

## Passo a passo

### 0. Nomenclatura (aplica-se sempre, disciplina nova ou já existente)

- Slides de teóricas: `<Disciplina>/Teoricas/Aula_NN.pdf` (zero à esquerda,
  não repetir o nome da disciplina — já está na pasta). Ao receberes um PDF
  novo do Gonçalo com outro nome qualquer, **abre a primeira página** para
  confirmar o número/título real da aula (não assumas pela ordem de chegada
  nem pelo nome do ficheiro original) e faz `git mv` para o nome certo antes
  de processar. Se um PDF não for uma aula numerada (ex: um livro/apontamento
  de referência do professor), não o forces no esquema `Aula_NN` — dá-lhe um
  nome descritivo dentro de `Teoricas/` e sinaliza ao Gonçalo que foi uma
  decisão tua.
- Se a aula chegar em **`.pptx`** (não PDF): não há LibreOffice instalado
  para converter, por isso fica como `Aula_NN.pptx` (mesmo esquema de
  nome, extensão original) e lê-se com `python-pptx` num venv no
  scratchpad (`python3 -m venv .../venv && .../venv/bin/pip install
  python-pptx pillow` --- o pip do sistema recusa instalar, PEP 668). Ler
  **texto de cada slide + notas do orador** (as notas trazem informação
  que não está nos slides) e extrair as imagens (`shape.image.blob`) para
  as ver --- slides só com imagem (esboços, diagramas) não têm texto
  nenhum. Nunca instalar LibreOffice sem perguntar (é pesado).
- Material de prática: `<Disciplina>/Praticas/Semana_N/`.
- Fonte do resumo: `<Disciplina>/.fonte/RESUMO_<Disciplina>.md` — **sempre
  escondida** (o Gonçalo não quer ver `.md` nenhum ao navegar a pasta), nunca
  apagada. O PDF compilado (`RESUMO_<Disciplina>.pdf`) fica visível na raiz
  da disciplina. Esta regra aplica-se a qualquer `.md` que cries para uma
  disciplina, não só ao resumo — gera sempre o PDF correspondente e esconde
  a fonte em `.fonte/`.

### 1. Descobrir o que é novo

Abre `<Disciplina>/.fonte/RESUMO_<Disciplina>.md` (se existir) e olha para o
cabeçalho HTML-comment `<!-- processado: ... -->` no topo do ficheiro — lista
os ficheiros de origem já incorporados. Compara com o conteúdo de
`<Disciplina>/Teoricas/`. Processa apenas os PDFs que ainda não constam dessa
lista (evita reprocessar e duplicar secções). Se houver também uma
`Praticas/Semana_N/` nova com material de prática, não a "processes" para o
resumo — usa-a só para saber que exercícios sugerir no fim de cada tópico (caixas `pratica`, passo 7).

Se o ficheiro RESUMO ainda não existir, cria-o (dentro de `.fonte/`) com o
cabeçalho YAML + comentário de processados vazio (ver "Esqueleto do
ficheiro" abaixo) antes de começar a escrever conteúdo.

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

Escreve diretamente no `.fonte/RESUMO_<Disciplina>.md`, em português, denso mas
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

::: pratica
Exercícios sugeridos para o Gonçalo fazer sozinho (sem resposta), no fim
do tópico cuja teoria aplicam --- ver passo 7.
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

**Outro bug de parsing (apanhado 2026-09-22):** nunca escrevas `(a)`, `(b)`,
`(c)`... **sem negrito** no início de um parágrafo/linha, quando várias
alíneas de um exercício partilham a mesma caixa. O pandoc reconhece isso
como início de **lista ordenada alfabética** e renumera tudo
sequencialmente a partir da primeira letra — se escreveres `(a)`, `(d)`,
`(c)`, `(g)`, `(h)` (porque só selecionaste essas alíneas, saltando as
outras), o PDF mostra `(a)`, `(b)`, `(c)`, `(d)`, `(e)` na ordem em que
apareceram, **não** as letras reais do enunciado — silenciosamente errado,
sem nenhum erro de build. Corrige sempre para `**(a)**`, `**(d)**`,
`**(c)**` (com negrito) — isso já não é reconhecido como marcador de lista
e mantém a letra literal. (Isto já era feito bem na maioria do documento;
só falhou numa caixa nova com múltiplas alíneas legítimas mas não
consecutivas.)

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

**O `build.sh` avisa (AVISO: ...) de três problemas que não dão erro mas
estragam o PDF:** caixa maior que uma página (o fim sai cortado), carácter
sem glifo (sai em branco, ex: `✓` --- usar `$\checkmark$`) e linha a sair
da margem direita (`texttt`/código comprido que não parte). **Qualquer
AVISO é bloqueante:** corrige antes de dar a tarefa por terminada (dividir
a caixa em duas, reduzir a figura, partir a linha).
Figuras **altas** (árvores, autómatos verticais) dentro de caixas: limita
por **altura** (`{height=10cm}`), não por largura --- `width=70%` numa
árvore com 7 níveis deu uma imagem mais alta do que a página.

**Tabelas (alinhamento automático, `_shared/template/auto-align.lua`):**
uma coluna com o separador `|---|` fica **centrada** se todas as células
forem curtas (V/F, números, fórmulas curtas). A 1.ª coluna só fica
centrada se tiver valores e não palavras (rótulos ficam à esquerda). Uma
tabela só de valores curtos usa a largura natural das colunas, em vez de
se esticar à largura da página. Não é preciso escrever `:-:` nas tabelas de
verdade. Continua a ser preciso ajudar à mão quando a tabela mistura
colunas curtas com uma coluna de texto comprido: indica as larguras
relativas com o nº de traços (`|:-:|:----|:----------------|`) para a
coluna comprida ficar com o espaço, e não a coluna "Passo" com um só "1".
Se uma célula de uma tabela de números tiver uma conta comprida, tira a
conta da tabela (explica-a numa frase antes) e deixa só o resultado.

**Um build sem erros não chega.** Depois de compilar, usa o Read sobre o
PDF gerado e inspeciona visualmente pelo menos as páginas com caixas novas
— um fenced div malformado (ex: erro de sintaxe no atributo `title=`) não
causa erro nenhum no tectonic, só faz a caixa sair como texto em bruto
com `:::` literais. Isso só se apanha a olhar para o resultado.

### 7. Ligação com a prática — exercícios POR TÓPICO, nunca no fim

**Regra (2026-09-23, pedido explícito do Gonçalo): os exercícios sugeridos
ficam no fim de cada tópico (`##`), não agrupados no fim da aula nem do
documento.** O Gonçalo lê um tópico e aplica-o logo a seguir; uma lista
"para fazeres sozinho" no fim da aula obriga-o a ler tudo primeiro e,
quando chega aos exercícios, já se esqueceu do que leu. Por isso:

- No fim de **cada** `##` cuja matéria é usada por algum exercício da
  prática (`Praticas/Semana_N/`), acrescenta uma caixa `::: pratica` com
  os exercícios/alíneas que o Gonçalo deve tentar **agora**, cada um com
  uma linha a dizer que técnica usa e, se útil, uma pista (sem a
  resposta). Se o tópico tiver `###` com técnicas muito diferentes e o
  exercício só usar uma delas, podes pôr a caixa no fim desse `###`.
- Um exercício que precisa de **vários** tópicos vai para o fim do
  **último** tópico de que depende (é aí que ele já tem tudo o que
  precisa). Diz na caixa o que mais usa (ex: "usa também a FNN acima").
- A ligação "este exercício usa esta secção" (o antigo parágrafo "Ligação
  com a prática") também é feita aqui, dentro da caixa do tópico --- não
  num parágrafo à parte no fim.
- **Nunca** criar uma secção `## Ligação com a prática` / "Para fazeres
  sozinho" no fim da aula com a lista de tudo. No fim da aula só é
  permitido, no máximo, uma frase a dizer que exercícios do enunciado
  ficam **fora** do resumo por ainda não terem sido dados nas teóricas.
- Exercícios **resolvidos** (caixas `exemplo`) seguem a mesma lógica: ficam
  dentro do tópico que aplicam, antes da caixa `pratica` desse tópico.
- Exercícios sugeridos inventados por ti (quando a prática ainda não tem
  nada para aquele tópico, ou os slides trazem um "exercício para casa")
  também vão numa caixa `pratica` no fim do tópico.

**Soluções de TODOS os exercícios das caixas `pratica` (2026-09-23): noutro
documento, uma alínea de cada vez.** As caixas `pratica` do resumo nunca
têm resposta. A resposta de **cada** exercício/alínea que lá aparece vai
para `<Disciplina>/.fonte/SOLUCOES_<Disciplina>.md`, e o `build.sh` gera
`<Disciplina>/SOLUCOES_<Disciplina>.html` (visível ao lado do PDF). No HTML
cada alínea está fechada e só abre com um clique; abrir uma fecha as
outras, para não haver spoilers. As caixas `pratica` do PDF ganham
automaticamente um rodapé a apontar para o HTML. Convenção do `.md`
(template `_shared/template/solucoes.html` + filtro `solucoes.lua`):

```
## Aula N --- tópico                 (secção; mesmo agrupamento das caixas)
### 1.2 --- título do exercício      (visível: enunciado curto / dados)
#### (a) enunciado da alínea         (fechado; o conteúdo abaixo é a solução)
solução completa, passo a passo...
```

- O `###` tem de começar por "<número> --- ", porque o número dá o id da
  alínea (`#1.2-a`, `#Ex.4-c`). Um exercício sem alíneas leva um único
  `#### Resposta`.
- **Cada item de uma caixa `pratica` tem solução, pela mesma ordem e com
  a mesma numeração.** Quando acrescentares uma caixa `pratica`,
  acrescenta as soluções na mesma passagem.
- As soluções seguem as regras dos exemplos resolvidos: totalmente
  explícitas, com cada cálculo intermédio. **Verifica-as antes de
  escrever:** contas em Python, equivalências por força bruta, código
  compilado e corrido contra os testes do lab. Um gabarito errado é pior
  do que não ter gabarito.
- Exercícios abertos (desenho, IPM) levam uma **resposta-modelo**, dita
  como tal, e não um "gabarito".
- Figuras: SVG (`dot -Tsvg`) em `figuras/sol_*.svg`. Ficam embutidas no
  HTML, que funciona offline (fórmulas em MathML, sem CDN).

**Regra atualizada (2026-09-22, substitui a versão anterior "nunca resolvas
a prática")**: o resumo deve conter uma **mistura** de:
- **Exercícios sugeridos, para o Gonçalo tentar sozinho** — enuncia o
  exercício (ou aponta para ele no enunciado da prática) mas não dás a
  resposta; é para ele aplicar a técnica que acabou de ler.
- **Exercícios totalmente resolvidos** — incluindo, quando isso ajudar a
  fixar o mecanismo, **exercícios reais do próprio enunciado da prática**
  (não só análogos inventados). Cita sempre a origem no título da caixa
  (ex: `title="--- Exercício 1.3(a) (lab, proplogic.pdf)"`), para ficar
  claro que aquilo é mesmo um exercício do lab e não um exemplo genérico.

Não há uma proporção fixa — usa julgamento: um exercício mecânico e
repetitivo (ex: "escreve a expressão regular para X, Y, Z, tal como para
A e B acima") é melhor sugerido para ele tentar; um exercício que introduz
uma dificuldade nova ou ilustra bem um mecanismo (ex: os casos mais
complicados de uma prova de dedução) vale mais a pena resolver por
completo. Sempre que resolveres um exercício real da prática, tenta
manter pelo menos um exercício parecido (do mesmo enunciado) só sugerido,
para ele não ficar com o enunciado inteiro já resolvido.

**Regra adicional (2026-09-22) — não fazer o Gonçalo trabalhar 2 vezes na
mesma coisa.** O tempo dele é limitado. Quando um exercício tem várias
alíneas que testam **a mesma técnica** sem introduzir nada de novo (ex: 8
alíneas todas do tipo "diz se esta frase é uma proposição"; 10 alíneas
todas do tipo "classifica esta fórmula"), **não resolvas nem sugiras todas**
— nem sequer as que ficam "por resolver". Isto aplica-se aos dois lados:

- **Ao resolver**: escolhe só as alíneas que testam uma ideia
  *diferente* umas das outras (ex: uma trivial-base, uma que mostra um erro
  comum, um par que contrasta dois casos parecidos mas com respostas
  opostas). Não resolvas 8 alíneas quando 4-5 já cobrem todas as ideias
  distintas — as restantes são só repetição mecânica da mesma ideia com
  números diferentes.
- **Ao sugerir "tenta sozinho"**: nunca aponta "todas as alíneas restantes"
  de um exercício com muitas alíneas repetitivas. Escolhe 2-3 das
  **mais difíceis ou mais distintas** de entre as que sobraram, e diz
  explicitamente que as outras ficam de fora por serem a mesma técnica
  (ex: "as restantes alíneas são a mesma ideia repetida, não precisas de as
  fazer todas"). Ele aprende a matéria da mesma forma com 3 bem escolhidas
  como com 10 — mais do que isso é desperdiçar o tempo dele, não reforçar a
  aprendizagem.

Isto vale tanto para o que TU resolves como para o que RECOMENDAS — o
objetivo final (resolvido + sugerido, somados) por exercício com muitas
alíneas repetitivas costuma ficar por volta de 4-6 alíneas no total, não o
enunciado inteiro.

### 8. Materiais suplementares em `Teoricas/` (não numerados) — usa como inspiração

Se `Teoricas/` tiver um ficheiro que não é uma aula numerada (ex: apontamentos
de outro docente, um capítulo de referência) — normalmente identificado por
não seguir o padrão `Aula_NN.pdf` (ver `CLAUDE.md`) — **não o ignores**: é
uma fonte extra a consultar sempre que os slides oficiais das aulas
estiverem incompletos, pouco claros, ou passarem por cima de um passo sem
explicar. Usa esse material para preencher essas lacunas (marca a origem
como nota adicional, tal como já fazes noutros casos), mas continua a
seguir a estrutura/terminologia das aulas oficiais como principal — o
suplementar é para desempatar dúvidas, não para substituir o que o
professor da disciplina realmente ensina.

### 9. Atualizar o cabeçalho de processados

Depois de compilar com sucesso, atualiza o comentário no topo do `.md` com os
novos ficheiros de origem incorporados (para a próxima invocação saber o que
já está feito), e atualiza a data no cabeçalho YAML (`date:`).

## Esqueleto do ficheiro (nova disciplina)

Cria em `<Disciplina>/.fonte/RESUMO_<Disciplina>.md` (a pasta `.fonte/` pode
não existir ainda — cria-a):

```markdown
---
title: "<Disciplina> (<código>) --- Resumo Teórico"
author: "Gonçalo Sousa"
date: "Atualizado: Semana N"
---

<!-- processado: Teoricas/Aula_01.pdf, Teoricas/Aula_02.pdf -->

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
- 2026-09-22: Reorganização de nomenclatura em todo o repositório (feedback
  do Gonçalo: "isto está a ficar bastante confuso"). Duas mudanças
  permanentes, aplicadas a Compiladores/IPM/Logica/Redes/TecnologiasWeb:
  (1) slides de teóricas passam a `Teoricas/Aula_NN.pdf` sempre (antes
  havia uma mistura: `Compiladores1.pdf`, `IPM_M01.pdf`, `aula1.pdf`,
  `Cap1.pdf`, `AboutRC.pdf` — cada disciplina com o nome que o professor
  lhe deu); (2) o Gonçalo não quer ver ficheiros `.md` a navegar as pastas,
  mas apagar a fonte do resumo destruiria a capacidade de o continuar a
  estender — resolvido escondendo-a em `<Disciplina>/.fonte/`, nunca
  apagando (ver regra 0 acima e `CLAUDE.md`). `Semana_N/` também passou a
  viver dentro de `Praticas/Semana_N/` em vez de à raiz da disciplina.
  `_shared/template/build.sh` foi atualizado para ler de `.fonte/`. Nota
  para casos como `Logica/nlc-4.pdf` (um livro de apontamentos do
  professor, sem número de aula) e `Redes/AboutRC.pdf` (a apresentação
  inicial, sem capítulo — tratada como Aula 1 por analogia com o padrão já
  usado em Compiladores): quando um PDF de `Teoricas/` não é claramente uma
  aula numerada, abre a primeira página antes de decidir o nome, nunca
  assumas pela ordem alfabética do ficheiro original.
- 2026-09-22: Duas mudanças de comportamento pedidas explicitamente pelo
  Gonçalo (ver regras 7 e 8 acima): (1) o resumo pode e deve resolver
  exercícios reais da prática, não só análogos — desde que também deixe
  outros só sugeridos, para não entregar o enunciado todo feito; (2)
  ficheiros suplementares em `Teoricas/` que não são aulas numeradas (ex:
  apontamentos de outro professor) devem ser consultados como fonte extra
  para preencher lacunas dos slides oficiais, não só arquivados com um nome
  diferente. Também corrigido `TecnologiasWeb/CALENDARIO.md`: o crawl do
  site (pedido numa sessão anterior) trouxe o `.mdown` com o calendário e
  os sumários, mas esses dois ficheiros só continham um `<iframe>` para uma
  Google Sheet publicada — o crawl de HTML nunca chega ao conteúdo da
  folha (é renderizado por JS). Solução: a folha publicada
  (`.../pubhtml?...`) tem sempre um endpoint irmão `.../pub?output=csv`
  que devolve os dados em texto simples, sem JS — troca `pubhtml` por
  `pub?output=csv` no mesmo URL e usa `curl`/`WebFetch` nesse. Padrão geral
  para qualquer disciplina cujo site publique calendário/sumários como
  Google Sheet embutida: não confiar num mirror de HTML estático para esse
  tipo de conteúdo, ir sempre buscar a folha pelo endpoint CSV.
- 2026-09-23: Lógica Aula 3 (formas normais, Horn) + IPM Aula 3 (Módulo 03,
  que chegou em `.pptx` --- ver regra no passo 0). Três lições novas:
  (1) **caracteres Unicode dentro de blocos de código** (`∧`, `∈`, `⊆`,
  `∪`, `→`) saem **em branco** no PDF (a fonte monoespaçada do `listings`
  não os tem) --- silencioso, só se vê a olhar para o PDF. Em
  pseudo-código usar sempre ASCII (`e`, `em`, `->`, `subset`).
  (2) Tabelas pipe com uma coluna de texto comprido e outra curta ficam
  com larguras más (a coluna `#` a ocupar 1/3 da página): controlar as
  larguras relativas com o nº de traços na linha separadora
  (`|--|------------|--------------|`), ou trocar a tabela por uma lista
  quando as células têm fórmulas longas. (3) Quando um módulo novo
  **aparentemente contradiz** um anterior (IPM: M02 "persona não se baseia
  em segmentos de mercado" vs. M03 "segmenta o mercado e escolhe uma
  pessoa por segmento"), não escolher um lado em silêncio nem duplicar:
  fundir na secção existente e acrescentar uma caixa `atencao` que
  explica como os dois se conciliam, marcada como interpretação. Também:
  um módulo que "revisita o processo inteiro" (como o M03 da IPM) deve ser
  **distribuído pelas secções já existentes** de cada etapa, ficando na
  secção da aula nova só o que é realmente novo + uma tabela
  "etapa → onde está explicada", em vez de repetir tudo.
- 2026-09-23: Feedback do Gonçalo: "as sugestões de exercícios só estão no
  final do documento. Quero sugestões para cada capítulo" --- ler tudo e só
  depois aplicar faz com que se esqueça do que leu. Regra 7 reescrita:
  exercícios sugeridos numa caixa nova `::: pratica` ("Pratica agora",
  roxa, definida em `preamble.tex`) no fim de **cada** tópico `##` que
  aplicam; proibidas as listas "Ligação com a prática"/"Para fazeres
  sozinho" agrupadas no fim da aula. Aplicado retroativamente a
  Compiladores, Lógica, Redes e IPM.
- 2026-09-23: O Gonçalo apanhou o Exercício 1.3(c) de Lógica cortado a meio:
  a árvore (`width=70%`) fazia a caixa ser maior que uma página e o fim
  (as subfórmulas) desaparecia sem erro. A inspeção visual "por amostragem"
  não chegou. Por isso o `build.sh` passou a ler o log do LaTeX e a avisar
  de caixas cortadas, caracteres em branco e linhas fora da margem. Na
  primeira passagem apanhou mais 3 caixas cortadas (Tecnologias Web,
  código Node.js), 5 `✓` invisíveis (Lógica) e 2 linhas fora da margem.
  Regra: nenhum AVISO do build pode ficar por resolver.
- 2026-09-23: Pedido do Gonçalo: soluções para **todos** os exercícios
  "Pratica agora", num documento à parte onde se abre só a alínea que se
  quer ("quero ver só a alínea a) e não todas", e ao abrir uma fecham-se
  as outras). Como um PDF não esconde conteúdo, a solução é um HTML por
  disciplina (`SOLUCOES_<Disciplina>.html`), gerado pelo mesmo `build.sh`
  a partir de `.fonte/SOLUCOES_<Disciplina>.md`. Ver a regra no passo 7.
- 2026-09-23: Feedback do Gonçalo: nas tabelas de verdade os V/F saíam
  encostados à esquerda, longe da fórmula do cabeçalho ("fica mal
  visualmente"). Causa: o separador `|---|` dá alinhamento por omissão
  (esquerda) no LaTeX, e nenhuma das 71 tabelas dos resumos estava
  centrada. As tabelas com linhas compridas no `.md` também se esticavam à
  largura da página e partiam os cabeçalhos com fórmulas. Solução geral
  em `auto-align.lua` (ver regra acima), mais duas correções à mão: a
  tabela de tempos LAN/WAN de Redes (contas `máx(...)` tiradas da tabela)
  e o traço do DFA em C de Compiladores (larguras das colunas).
