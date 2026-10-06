---
name: resumo-semanal
description: Gera ou estende o resumo teórico cumulativo em PDF de uma disciplina a partir dos slides colocados em Teoricas/, e as soluções (uma alínea de cada vez) dos exercícios "Pratica agora" no site único SOLUCOES.html (todas as disciplinas, um separador por disciplina). Usar sempre que o Gonçalo adiciona material novo de uma disciplina (teóricas novas) e pede para atualizar o resumo, ou quando começa uma disciplina nova.
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
- **O número da aula é a ordem em que as aulas foram dadas, não o número
  escrito no slide (2026-10-06).** Os slides do professor podem saltar
  números (em Compiladores, a 6.ª aula diz "Aula 7"). O nome do ficheiro
  que o Gonçalo deu (`Compiladores-6.pdf`) e a sequência das aulas já
  processadas mandam. Na dúvida, pergunta. Nunca digas que "falta uma
  aula" só por causa de um salto na numeração dos slides.
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

- **Compacto e sem palha (2026-10-06).** O Gonçalo quer "informação
  legível, compacta e bem resumida, sem informação inútil que vou ler e
  esquecer". Fora do resumo: histórias e datas ("o primeiro compilador de C
  foi em 1973", "Rust foi escrito em OCaml de 2006 a 2010"), citações e
  definições de dicionário, frases de efeito, recapitulações no início de
  cada aula ("a aula anterior mostrou..."), frases "como vimos na secção
  X" que não acrescentam nada, comentários sobre gralhas dos slides
  (corrige-se em silêncio), e curiosidades de ferramentas que não fazem
  falta nas práticas. Uma ideia diz-se **uma vez**, no sítio certo. Um
  exemplo concreto curto (ex.: "o Rust começou escrito em OCaml") pode
  ficar se ilustrar a definição.
- **Não omitir matéria.** Todas as definições, teoremas e algoritmos dos
  slides têm de aparecer, explicados por palavras próprias (não copiar o
  slide telegráfico — desenvolver o raciocínio, o "porquê", não só o "o quê").
  "Compacto" quer dizer sem repetição nem palha, **nunca** saltar matéria
  nem passos dos exemplos resolvidos.
- **Preencher lacunas.** Se um slide assume conhecimento que não explica mas
  que é necessário para as práticas ou para perceber o resto, acrescenta essa
  explicação **no texto normal ou na caixa de definição do tópico**, e
  marca-a com um **†** (no título da caixa ou logo a seguir à primeira
  expressão em negrito do parágrafo). O topo do documento tem a legenda
  "O sinal † marca matéria que não está nos slides mas faz falta para as
  práticas". Nada de caixas "Nota adicional (não estava nos slides)".
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
- **Sem caixas de atenção nem de exame (2026-10-06).** O Gonçalo não as
  quer ("não quero saber disso"). Um aviso que faz falta para perceber a
  matéria ou para as práticas vai para o texto, no sítio onde se aplica;
  o que é só "cuidado com..." ou "isto sai em exame" sai. Instruções de
  instalação de ferramentas para um lab vão para a caixa `pratica` desse
  lab (ex.: "Em C precisas do Bison 3: `brew install bison`").

### 4. Caixas disponíveis

**Estilo v2 (2026-10-06).** As disciplinas listadas em `ESTILO_V2` no
`build.sh` (por agora só Compiladores) usam `_shared/template/preamble-v2.tex`:
Charter (texto), Avenir Next (títulos), Menlo (código, com `∧ ∈ →` e sem
caracteres em branco), 10pt, margens de 2,2cm, caixas leves (linha à
esquerda em vez de caixa cheia), número grande na abertura de cada aula.
Só tem **três** caixas; uma caixa `atencao` ou `exame` faz a compilação
falhar de propósito. Ao converter outra disciplina: tirar as caixas
`atencao`/`exame` (passo 3), juntá-la a `ESTILO_V2` e rever o PDF todo. As
restantes disciplinas usam ainda o `preamble.tex` antigo.

Convertidas pelo filtro `_shared/template/div-envs.lua`. Sintaxe no Markdown:

```
::: definicao
Conteúdo markdown normal aqui (negrito, $math$, etc. funcionam).
:::

::: exemplo
Exemplo resolvido passo-a-passo.
:::

::: pratica
Exercícios sugeridos para o Gonçalo fazer sozinho (sem resposta), no fim
do tópico cuja teoria aplicam --- ver passo 7.
:::

::: {.definicao title="--- Autómato finito"}
Caixa com título extra (aparece como "Definição  Autómato finito"; no v2
o "--- " é tirado e o rótulo separa o tipo do título).
:::
```

**O título vai tal e qual para LaTeX:** nada de `% # & _ $` dentro de
`title="..."` (um `%` comenta o resto da linha e dá um erro confuso numa
caixa seguinte; `\%` também não serve, o pandoc come a barra).

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
as caixas (`definicao`/`exemplo`/`pratica`) são propositadamente
**não-quebráveis** (sem a opção `breakable`) — uma caixa nunca parte entre
duas páginas, o LaTeX empurra-a inteira para a página seguinte se não
couber. E cada `# Aula N` força uma página nova (`\clearpage` antes de
`\section`), para o índice levar sempre a um topo de página. Consequência
prática para quem escreve o Markdown: **uma caixa individual tem de caber
numa única página** — se um exemplo ficar demasiado longo, corta-o em duas
caixas `exemplo` consecutivas em vez de deixar uma caixa gigante (que ou
transborda da página, ou deixa muito espaço em branco na página anterior).

**Nunca texto a meio (2026-10-06, v2).** No estilo v2 o `div-envs.lua` põe
um `\Needspace` antes de cada tabela (até 40 linhas) e de cada bloco de
código (até 20 linhas) fora das caixas, para mudarem de página inteiros.
Código mais comprido parte-se: **divide-o tu em blocos de até ~20 linhas
em fronteiras naturais** (uma `struct`, um grupo de funções, as classes de
uma categoria). Antes de dar o PDF por pronto, revê **todas** as páginas
(não por amostragem): nada de tabelas, blocos de código, listas ou
parágrafos cortados entre páginas, nem uma ou duas linhas sozinhas numa
página. Se a última linha de uma secção cai sozinha na página seguinte,
encurta o texto dessa secção. Menos páginas é melhor, mas nunca à custa de
texto cortado.

### 5. Diagramas

- **Autómatos, grafos, árvores** → gera um `.dot` e compila com
  `dot -Tpdf ficheiro.dot -o <Disciplina>/figuras/nome.pdf` (graphviz já
  instalado via Homebrew). Usa `rankdir=LR` para autómatos ficarem legíveis.
- **Gráficos matemáticos/estatísticos** → só se necessário instalar
  `matplotlib` via pip nesse momento (ainda não está instalado por omissão).
- Guarda sempre os diagramas em `<Disciplina>/figuras/`, com nomes descritivos
  (`nfa_thompson_ab.pdf`, não `fig1.pdf`), para poderes referenciá-los ou
  regenerá-los mais tarde.

### 6. Compilar o PDF (e o site de soluções)

```
bash _shared/template/build.sh <Disciplina>
```

Gera `RESUMO_<Disciplina>.pdf` e, se existir `.fonte/SOLUCOES_<Disciplina>.md`,
reconstrói o site único de soluções `SOLUCOES.html` na raiz, com **todas**
as disciplinas (ver passo 7). Só esse passo:
`python3 _shared/template/build_solucoes.py`. Corre a partir da raiz
do repositório. Confirma que não há erros do tectonic
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

**Verificar o site de soluções (`SOLUCOES.html`):** o Read não abre HTML. Tira uma captura
com o Chrome headless:

```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new \
  --window-size=1000,3000 --virtual-time-budget=3000 --screenshot=<png> "file://<html>"
```

Para ver uma alínea aberta, gera uma cópia temporária com ` open` no
`<details id="...">` dessa alínea. **Não** uses `#id` no URL: com o salto
de scroll, a captura headless sai em branco. O Chrome headless não desce
abaixo de ~485px de largura. Para testar o comportamento, como "abrir uma
fecha as outras", injeta um `<script>` que clica e escreve o resultado num
`<pre>`, e lê-o com `--dump-dom`. Apaga as cópias temporárias no fim.

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
para `<Disciplina>/.fonte/SOLUCOES_<Disciplina>.md`.

**Site único de soluções (2026-10-06, pedido do Gonçalo): todas as soluções
de todas as disciplinas ficam num só site, `SOLUCOES.html` na raiz do
repositório**, com um separador por disciplina. **Já não há**
`<Disciplina>/SOLUCOES_<Disciplina>.html`: não os voltes a criar, nem
escrevas soluções diretamente em HTML. A fonte continua a ser o `.md` de
cada disciplina; o `build.sh` (ou `python3
_shared/template/build_solucoes.py`) junta todos os
`*/.fonte/SOLUCOES_*.md` no site, por isso uma disciplina nova entra
sozinha (separador e cor automáticos, por ordem alfabética da pasta).
No site cada alínea está fechada e só abre com um clique; abrir uma fecha
as outras, para não haver spoilers, e as alíneas já abertas ficam
marcadas como vistas. As caixas `pratica` do PDF ganham automaticamente um
rodapé a apontar para `../SOLUCOES.html#<Disciplina>`. Ficheiros:
`build_solucoes.py` (junta tudo), `solucoes.html` (página: caderno
quadriculado com separadores), `solucoes-disciplina.html` (bloco de cada
disciplina), `solucoes.lua` (alíneas). Convenção do `.md`:

```
## Aula N --- tópico                 (secção; mesmo agrupamento das caixas)
### 1.2 --- título do exercício      (visível: enunciado curto / dados)
#### (a) enunciado da alínea         (fechado; o conteúdo abaixo é a solução)
solução completa, passo a passo...
```

- O `###` tem de começar por "<número> --- ", porque o número dá o id da
  alínea, com a pasta da disciplina à frente (`#Logica-1.2-a`,
  `#Compiladores-Ex.4-c`); no site o número aparece numa etiqueta. Um exercício sem alíneas leva um único
  `#### Resposta`.
- **Cada item de uma caixa `pratica` tem solução, pela mesma ordem e com
  a mesma numeração.** Quando acrescentares uma caixa `pratica`,
  acrescenta as soluções na mesma passagem.
- **Resolver com o método certo (2026-09-23).** Antes de resolver um
  exercício (no resumo ou nas soluções), lê o enunciado à procura do
  método pedido ("using semantic equivalences", "without building the
  truth table", "construct truth tables", "using the definitions") e usa
  **esse**. Se o enunciado não diz, usa o método da aula a que o exercício
  pertence. Nunca trocar por um método "mais fácil" ou que só chega ao
  mesmo resultado (ex.: tabela de verdade quando se pede simplificação por
  equivalências). E o exercício só pode aparecer **depois** do tópico que
  ensina esse método --- se o método ainda não foi dado, o exercício está
  no sítio errado.
- **Estilo de exame: prova matemática, não palavras (2026-10-01).** Os
  exemplos resolvidos e as soluções escrevem-se como a professora resolve e
  como é aceite em exame: notação das teóricas (em Lógica, `\models_v`,
  `\not\models_v`, "sse"), cada passo justificado por uma definição ou
  lei, divisão em casos quando a definição dá um "ou", e contraexemplo
  explícito, verificado com as regras, quando a afirmação é falsa. Uma
  explicação por palavras só pode aparecer **ao lado** da prova, como
  intuição, e só substitui a prova se o exercício for demasiado simples.
  Os esqueletos por tipo de exercício estão na skill `resolver-exercicio`
  (`.claude/skills/resolver-exercicio/SKILL.md`): segue-os.
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
  exercício (ou aponta para ele no enunciado da prática) numa caixa
  `pratica`, sem a resposta **no resumo**; é para ele aplicar a técnica
  que acabou de ler. A resposta completa vai **sempre** para
  `SOLUCOES_<Disciplina>.md` (ver acima).
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

**Uma secção `##` nas soluções por cada caixa `pratica`, pela mesma ordem
(2026-10-06).** No estilo v2, o rodapé de cada caixa "Pratica agora" tem
uma ligação por alínea, que abre o site já nessa alínea (ex.: "Soluções:
Ex. A (a), Ex. A (b)"). O `div-envs.lua` emparelha a k-ésima caixa
`pratica` do resumo com a k-ésima secção `##` do `SOLUCOES_<Disciplina>.md`.
Por isso: uma caixa nova → uma `##` nova no sítio certo, nunca duas caixas
na mesma `##`. O build avisa se as contagens não baterem.

### 8. Materiais suplementares em `Teoricas/` (não numerados) — usa como inspiração

Se `Teoricas/` tiver um ficheiro que não é uma aula numerada (ex: apontamentos
de outro docente, um capítulo de referência) — normalmente identificado por
não seguir o padrão `Aula_NN.pdf` (ver `CLAUDE.md`) — **não o ignores**: é
uma fonte extra a consultar sempre que os slides oficiais das aulas
estiverem incompletos, pouco claros, ou passarem por cima de um passo sem
explicar. Usa esse material para preencher essas lacunas (marca a origem
com †, tal como já fazes noutros casos), mas continua a
seguir a estrutura/terminologia das aulas oficiais como principal — o
suplementar é para desempatar dúvidas, não para substituir o que o
professor da disciplina realmente ensina.

### 8b. Folha de revisão para o exame (2026-10-06)

Além do resumo, cada disciplina pode ter `.fonte/REVISAO_<Disciplina>.md`
→ `REVISAO_<Disciplina>.pdf` (o `build.sh` gera-a se existir). Tem 2--3
páginas, só com receitas, regras e tabelas de comparação, sem exemplos nem
explicações longas: é para rever na véspera. Usa só `##` (sem `# Aula`),
para não abrir páginas novas. **Quando o resumo ganha matéria nova,
acrescenta à folha as receitas novas** (ex.: um algoritmo novo dá uma
linha ou uma lista curta). Compiladores tem uma; as outras disciplinas
ganham a sua quando forem convertidas ao estilo v2.

### 9. Atualizar o cabeçalho de processados

Depois de compilar com sucesso, atualiza o comentário no topo do `.md` com os
novos ficheiros de origem incorporados (para a próxima invocação saber o que
já está feito), e atualiza a data no cabeçalho YAML (`date:`).

**Antes de dar a tarefa por terminada, confirma as soluções:** cada item
de cada caixa `pratica` (exercício e alínea) tem de ter o seu `####` em
`SOLUCOES_<Disciplina>.md`. Compara a lista das caixas
(`grep -A12 "::: {.pratica" .fonte/RESUMO_*.md`) com os ids gerados
(`grep -o 'details class="sol" id="<Disciplina>-[^"]*"' SOLUCOES.html`). Se faltar
algum, a tarefa não está feita. Atualiza também o `date:` do
`SOLUCOES_…md` se mudou.

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

E, assim que houver a primeira caixa `pratica`,
`<Disciplina>/.fonte/SOLUCOES_<Disciplina>.md`:

```markdown
---
title: "<Disciplina> --- Soluções dos exercícios \"Pratica agora\""
subtitle: "<enunciado de origem>. Tenta primeiro sozinho; abre uma alínea só depois de a teres feito."
---

## Aula 1 --- <tópico da caixa>

### 1.2 --- <título do exercício>

<dados comuns às alíneas, visíveis>

#### (a) <enunciado da alínea>

<solução completa>
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
- 2026-09-23: Feedback do Gonçalo: "as soluções têm que ser resolvidas com
  o método certo, repara que a 1.9 de lógica usaste tabelas de verdade
  coisa que nunca foi pedida". O enunciado da 1.9 manda simplificar com
  equivalências semânticas. A causa de fundo: a 1.9 estava na **Aula 1**,
  antes de as leis de equivalência serem dadas (Aula 2), por isso as
  alíneas resolvidas (d)/(i)/(j) usavam análise de casos e a solução da
  (c) usava tabela. Corrigido: a 1.9 passou para a Aula 2, a seguir às
  leis, com uma caixa de método ("eliminar →, empurrar ¬, simplificar,
  ler a classificação") e as leis extra (complementaridade, elemento
  neutro/absorvente, absorção), e todas as alíneas foram refeitas por
  equivalências. Regra nova no passo 7 ("Resolver com o método certo").
- 2026-09-23: O Gonçalo não percebeu o passo "$(p\land\neg q)\lor p\lor\neg q
  \Leftrightarrow p\lor\neg q$ (absorção)" na solução da 1.9(c). A
  absorção não está na tabela de leis dos slides nem na do enunciado, e o
  passo foi dado de uma vez. Regra: um passo de simplificação tem de usar
  **as leis que ele conhece** (tabela do enunciado/slides), uma de cada vez
  e com os papéis ($\varphi$, $\psi$, $\theta$) identificados. Uma lei extra
  (absorção, complementaridade...) só pode aparecer como **atalho** a
  seguir à derivação feita com as leis oficiais, com uma frase a dizer
  porque é que vale.
- 2026-09-28: Redes Cap. 2 (Camada de aplicação) trouxe **capturas de
  pacotes** (`.cap`) junto aos slides. Não há Wireshark/tshark; lê-se com
  `tcpdump -nn -A -r` ou com um leitor pcap de 30 linhas em Python. As
  capturas dão exemplos reais (diálogo SMTP/FTP, cabeçalhos HTTP) e
  exercícios "Pratica agora" com respostas verificáveis. Nomear como
  `Teoricas/Aula_NN_captura_<proto>.cap`. Também: **correr o código dos
  slides** (há `javac`) apanhou um erro real (o servidor UDP reaproveita o
  buffer e devolve lixo); vai para o resumo como nota adicional. E quando
  a prática trouxer **soluções oficiais**, comparar com as nossas e
  assinalar nas soluções as diferenças de interpretação, sem apagar
  nenhuma das duas. Cuidado ao gerar texto com `$` num heredoc sem aspas
  (`<<EOF`): o shell come `$R`, `$57`, etc. Usar sempre `<<'EOF'`.
- 2026-09-29: IPM recebeu o **enunciado do projeto** (COL), não uma aula.
  Ficou em `Praticas/Semana_2/Enunciado_Projeto_COL.pdf` (é material de
  prática), mas, como descreve o projeto que já tinha uma secção na Aula 1,
  foi **fundido nessa secção** (problema, sistema, estados, regras da sala,
  calendário, conteúdo do R1/PR2) e listado no `<!-- processado -->`.
  Datas do enunciado que contradizem os slides: vale o enunciado, com caixa
  `atencao`. Figuras oficiais do PDF recortadas com `pdftoppm -r 200` +
  `sips -c H W --cropOffset Y X` (não há PIL no sistema). Exercícios
  "Pratica agora" que **são entregáveis avaliados do grupo** (personas,
  missões): como as regras de IA da disciplina proíbem gerar esse
  conteúdo, a "solução" é uma **grelha de verificação** + contraexemplo,
  não uma resposta-modelo pronta a copiar. Os exercícios de compreensão do
  enunciado (autorizações, estados, contas) levam solução completa.
- 2026-10-01: Feedback do Gonçalo sobre a 1.11 e a 1.13 de Lógica: "a
  forma que resolveste não é válida em exame". As soluções em prosa ("como
  C é inocente, A não pode ser culpado...") e os raciocínios com
  `V \to F = F` não são o formato da professora. Ela abre cada fórmula com
  a definição de `\models_v` (ex.: `\models_v (p\lor q)\to r` sse
  `\not\models_v p\lor q` ou `\models_v r`) e trata cada caso do "ou" em
  separado. Criada a skill `resolver-exercicio` com o método e os
  esqueletos, e regra nova no passo 7 ("Estilo de exame"). Foram reescritas
  no resumo e nas soluções de Lógica as provas de consequência/tautologia
  (1.11, 1.13, 1.14, 1.15, 1.16, 1.10 g). Aplica-se a todas as
  disciplinas: resolver sempre na forma matemática do professor, e só em
  palavras quando o exercício é trivial.
- 2026-10-06: Compiladores Aula 6 (geradores Happy/Bison + ASTs). O PDF
  chegou como `Compiladores-6.pdf`, com "Aula 7" escrito na 1.ª página.
  Chamei-lhe Aula 7 e disse que faltava a 6: **errado**. O Gonçalo
  corrigiu: é a 6.ª aula (os slides do professor saltam um número). Ficou
  `Aula_06.pdf` e `# Aula 6`. Ver a regra nova no passo 0. A prática chegou
  como `Praticas/Parsing/`, movida para `Praticas/Semana_3/Parsing/`. Duas lições: (1) o atributo
  `title="..."` das caixas vai **tal e qual** para LaTeX: um `%` no
  título (ex.: `%left`) comenta o resto da linha e dá um erro confuso
  (`Paragraph ended before \verbatim@`) numa caixa *seguinte*. Nada de
  `% # & _ $` em títulos; o `\%` também não serve (o pandoc come a
  barra). (2) Para labs de geradores: o `bison` do macOS é o 2.3 e
  rejeita `%define api.value.type`; usar `brew install bison`
  (`/opt/homebrew/opt/bison/bin`). `happy`/`alex` com
  `cabal install happy alex` (`~/.cabal/bin`). Correr o `happy -i`
  dá relatórios reais (`.info`) para exemplos de conflitos no resumo.
- 2026-10-06: IPM Módulo 04 (`IPM_M04_...pdf`, capa "Module 04 · Lecture 3").
  O nome segue o **número do módulo** (`Aula_04.pdf`), para manter
  Aula N = Módulo N como nas aulas anteriores, e não o "Lecture". Os tópicos
  que aprofundam uma secção antiga foram **fundidos lá** (o "Sketching" foi
  para a secção "Esboçar" da Aula 2), e a Aula 4 termina com uma tabela
  "conteúdo → onde está". Figuras dos slides: `pdfimages -f N -l N -png`
  tira as imagens originais, sem recortes; para composições usar
  `pdftoppm -r 200` + `sips -c`. Captura do HTML de soluções: abrir
  **uma só** alínea por cópia (com duas `open`, o "só uma aberta" fecha
  as duas), e para ver uma secção do fundo da página **cortar o HTML**
  (manter o `<head>` e a parte a partir do `<h2>` dessa secção). O
  `sips --cropOffset` não corta capturas muito altas de forma fiável.
- 2026-10-06: Lógica Aulas 5--6 (dedução natural) chegou como um só PDF
  (`aula56.pdf` → `Teoricas/Aula_05-06.pdf`, uma secção "# Aulas 5--6") e
  a folha 2 (`proplogicproofs.pdf`, "lab classes 3, 4 and 5") foi para
  `Praticas/Semana_3/`. Para as provas em **notação de Fitch** criou-se
  `_shared/template/fitch.lua` (bloco ```` ```{.fitch} ```` em ASCII:
  `|` por nível, `|>` abre hipótese, `---` fecha premissas,
  `; &E, 2` justificação), que desenha a prova no PDF e no HTML, e
  `_shared/tools/fitch_check.py`, que **verifica cada passo** (regra,
  linhas acessíveis, sub-deduções fechadas) e, com `seq="Γ |- φ"`, as
  premissas e a conclusão. Regra: **correr o verificador sobre o RESUMO e
  as SOLUCOES antes de compilar**; nenhuma dedução pode falhar
  (`.nocheck` só para deduções erradas de propósito ou dadas sem
  justificações). Apanhou também gralhas nos apontamentos de Nelma
  Moreira (assinaladas no resumo).
- 2026-10-06: Pedido do Gonçalo: as soluções num **só site** com todas as
  disciplinas, a escolher por separador, e com um design melhor (o HTML
  antigo era "muito feio"). Feito com a skill frontend-design da
  Anthropic: um caderno quadriculado com separadores coloridos por
  disciplina, cada alínea numa tira dobrada que se desdobra ao clicar,
  índice lateral com "vistas x/y" por exercício e o mesmo "só uma aberta
  de cada vez". `SOLUCOES.html` na raiz, gerado por
  `_shared/template/build_solucoes.py` a partir de todos os
  `.fonte/SOLUCOES_*.md`. Os `<Disciplina>/SOLUCOES_<Disciplina>.html`
  foram apagados. Ver o passo 7.
- 2026-10-06: Redes recebeu uma **ficha prática** (Ficha 3, protocolos de
  aplicação) solta em `Praticas/`, sem teórica nova: foi movida para
  `Praticas/Semana_3/` e não gerou secção nova, só caixas "Pratica agora",
  notas adicionais (telnet, `dig`/`host`, STARTTLS, TTL, *root hints*)
  e um exemplo resolvido, tudo **dentro das secções que já existiam**.
  Três lições: (1) quando a ficha traz um exercício igual a um
  **inventado** por nós (aqui, analisar as mesmas capturas), o oficial
  substitui o inventado e só ficam as perguntas do inventado que a ficha
  não faz (renumeradas), para ele não fazer o mesmo duas vezes. (2) Os
  exercícios "corre este comando" (`dig`, `telnet`, `gnutls-cli`) foram
  **corridos de verdade** e as soluções mostram a saída real, com data;
  o que não deu para observar fica marcado como ilustrativo ou
  resposta-modelo. Nunca enviar emails/ações com efeitos por ele (no
  SMTP só se testou `EHLO`/`QUIT`). (3) Os números de pacote das
  capturas tiram-se com `tcpdump -# -nn -r` **sem filtro** (com filtro
  o `-#` numera só os pacotes filtrados e não bate com o Wireshark).
- 2026-10-06: Pedido do Gonçalo depois de ver a amostra do estilo
  `frontend-design`: "fica muito mais fácil de ler", mas (1) "não pode
  ficar texto a meio", (2) cortar as caixas de atenção e de exame em todos
  os PDFs ("não quero saber disso"), (3) tirar informação redundante,
  repetida e inútil ("tou-me a cagar se o gajo nasceu em 1940"), (4) "o
  menos páginas possível". Compiladores convertido primeiro: estilo v2
  (`preamble-v2.tex`, ver passo 4), caixas fundidas no texto, palha
  cortada, de 60 para 42 páginas com a mesma matéria, os mesmos exemplos e
  as mesmas caixas "Pratica agora". O site de soluções passou ao mesmo
  estilo (letras do sistema, sem Google Fonts nem quadrícula). Bugs
  apanhados pelo caminho, todos silenciosos: (a) com o `tocloft`, listas e
  parágrafos ganhavam espaços enormes entre linhas → usa-se o `titletoc`;
  (b) um título de índice com estrutura diferente do das aulas (só
  `{\LARGE #1}`) causava o mesmo sintoma → o índice usa a mesma caixa das
  aulas, sem número (causa não percebida, ver comentário no
  `preamble-v2.tex`); (c) "(1) ... (2) ..." no início de uma linha dentro
  de um exemplo virou lista numerada (o bug do pandoc já conhecido, também
  com números). Diagnosticar espaçamentos estranhos: compilar o `.tex` do
  build (`KEEP_TMP=1 bash build.sh X` guarda a pasta) comentando uma linha
  do preâmbulo de cada vez, e medir pela página onde o índice acaba.
