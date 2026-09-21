---
title: "Compiladores (CC3001) --- Resumo Teórico"
author: "Gonçalo Sousa"
date: "Atualizado: Semana 1 (Aulas 1--3)"
---

<!-- processado: Teoricas/Compiladores1.pdf, Teoricas/Compiladores2.pdf, Teoricas/Compiladores3.pdf -->

# Aula 1 --- Introdução e fases de um compilador

## O que é um compilador

Um **compilador** é um tradutor de programas: recebe um programa escrito
numa linguagem (a *linguagem fonte*) e produz um programa equivalente
noutra linguagem (a *linguagem destino*). Normalmente traduz de uma
linguagem de **alto nível** (ex: C, Java) para uma de **baixo nível**
(código máquina, ou uma representação intermédia como bytecode JVM). É a
principal técnica usada para implementar linguagens de programação —
GCC (C/C++ → código máquina), Javac (Java → bytecode JVM), GHC (Haskell →
código máquina) e Scalac (Scala → bytecode JVM) são todos compiladores.

::: exemplo
Um caso interessante é **elm**, que compila Elm para **JavaScript** — o
destino nem sempre é código máquina; pode ser outra linguagem de alto
nível (a isto também se chama *transpilação*, mas o mecanismo interno é o
mesmo de um compilador).
:::

## Compiladores vs. interpretadores

Em vez de traduzir o programa todo antes de o correr, um **interpretador**
faz a análise lexical e sintática da mesma forma que um compilador, mas
depois **executa diretamente** o programa a partir da árvore sintática
(ou, em alternativa, gera e executa código intermédio à medida que avança,
sem produzir um executável final).

::: {.definicao title="--- Compilação vs. interpretação"}
**Compilação**: traduz o programa fonte inteiro para outra linguagem
*antes* de o executar, produzindo um artefacto (executável) reutilizável.
**Interpretação**: analisa e executa o programa diretamente, sem produzir
um executável separado.
:::

| | Vantagem |
|---|---|
| Interpretação | Mais simples de implementar; mais fácil suportar várias arquiteturas; permite REPL (*read-eval-print-loop*), útil para desenvolvimento interativo. |
| Compilação | O código compilado é normalmente mais eficiente; o executável pode ser distribuído sem depender do compilador. |

::: atencao
Nota adicional: muitas implementações reais **combinam** as duas técnicas
(ex: GHC pode compilar ou interpretar Haskell; OCaml tem `ocaml`
— interpretador/REPL — e `ocamlopt` — compilador). Não penses nelas como
mutuamente exclusivas.
:::

## Fases de um compilador

Um compilador divide-se tradicionalmente em duas grandes partes, ligadas
por uma **representação intermédia** (código intermédio) que é
independente da linguagem fonte e da máquina destino:

![Fases de um compilador: frontend, representação intermédia, backend](figuras/pipeline.pdf){width=95%}

::: {.definicao title="--- Frontend / Backend"}
**Frontend** (depende da linguagem fonte, não da máquina destino):
análise lexical → análise sintática → análise semântica → AST + tabela de
símbolos.

**Backend** (depende da máquina destino, não da linguagem fonte):
seleção de instruções → alocação de registos → assembler & linker.

Entre os dois: **geração de código intermédio**, que não depende nem da
linguagem fonte nem da máquina destino.
:::

Esta separação torna o compilador mais simples e permite **reutilizar
componentes**: o *backend* do GCC serve para compilar C, C++ ou
Objective-C; o *backend* LLVM é partilhado por Clang, Swift, Rust e
(opcionalmente) GHC. Um mesmo *frontend* também pode, em teoria, ser usado
com vários *backends* diferentes.

Este semestre o foco está sobretudo no **frontend** — é aí que entram a
análise lexical (Aulas 2--3, abaixo) e a análise sintática.

## Self-hosting e bootstrapping

::: {.definicao title="--- Self-hosting"}
Um compilador é **self-hosted** quando está escrito na própria linguagem
que compila. Exemplos: GCC é escrito em C, Javac em Java, GHC em Haskell,
Rustc em Rust.
:::

Self-hosting é normalmente visto como prova de maturidade da linguagem e
das suas ferramentas ("*eat your own dog food*") e facilita a comunicação
entre programadores do próprio compilador (só precisam de saber uma
linguagem). O problema óbvio é: **se o compilador de X está escrito em X,
o que compilou a primeira versão?**

::: {.atencao title="--- Bootstrapping"}
Resolve-se por **bootstrapping**: escreve-se uma primeira versão do
compilador numa *outra* linguagem, usa-se essa versão para compilar uma
segunda versão já escrita na linguagem-alvo, e repete-se o processo até o
compilador conseguir compilar-se a si próprio.

- **C**: o primeiro compilador de C (1973) foi baseado no compilador de B
  (uma linguagem anterior); o primeiro compilador de B tinha sido escrito
  em TMG (uma linguagem do sistema Multics). O compilador foi depois
  reescrito em B, por estágios, até ser capaz de compilar a si próprio.
- **Rust**: o primeiro compilador (2006--2010) foi escrito em OCaml; a
  partir de 2010 começou a reescrita em Rust (ainda compilada pelo
  compilador OCaml); desde 2011 o compilador de Rust é *self-hosted*.
:::

# Aula 2 --- Análise lexical

## O que faz a análise lexical

O **léxico** de uma linguagem de programação é o conjunto de símbolos e
palavras usados para compor programas — os *tokens*. Há várias categorias
típicas: **identificadores** (nomes de variáveis/funções), **literais**
(números, caracteres, cadeias), **palavras reservadas** (`if`, `else`,
`while`, ...) e **operadores** (`+`, `*`, `=`, ...).

Um **analisador lexical** (também chamado *lexer*, *scanner* ou
*tokenizer*) decompõe o texto de entrada numa sequência de *tokens*. Esta
decomposição facilita a análise sintática seguinte — o *parser* trabalha
sobre uma lista de *tokens* já classificados, não sobre texto em bruto
carácter a carácter.

::: {.definicao title="--- Representação de um token"}
Cada *token* é identificado por uma **etiqueta** (*token type*), e alguns
tipos têm também um **valor** associado:

| Entrada | Etiqueta | Valor |
|---|---|---|
| `if` | `IF` | --- |
| `,` | `COMMA` | --- |
| `!=` | `NOTEQ` | --- |
| `main` | `ID` | `"main"` |
| `71` | `NUM` | `71` |
| `.5` | `REAL` | `0.5` |
:::

::: exemplo
Para o código C `float match0(char *s) { if (!strncmp(s, "0.0", 3)) return 0.0; }`,
o analisador lexical produz a sequência:

`FLOAT, ID("match0"), LPAREN, CHAR, STAR, ID("s"), RPAREN, LBRACE, IF, LPAREN, BANG, ID("strncmp"), LPAREN, ID("s"), COMMA, STRING("0.0"), COMMA, NUM(3), RPAREN, RPAREN, RETURN, REAL(0.0), SEMI, RBRACE, EOF`

Repara que **espaços, mudanças de linha, tabulações e comentários não
geram tokens** — são consumidos e descartados pelo analisador (servem só
para separar tokens). Um token `EOF` marca explicitamente o fim da
entrada.
:::

## Expressões regulares

Escrever um analisador lexical à mão, carácter a carácter (com um `switch`
gigante, por exemplo), é simples mas repetitivo, difícil de manter e fácil
de errar (ex: é preciso ter cuidado com a ordem das condições — `"if"` tem
de ser reconhecido como palavra reservada e não como identificador). A
alternativa é **descrever os tokens de forma declarativa** usando
expressões regulares, e depois gerar automaticamente o analisador a partir
dessa descrição — é isso que os geradores de analisadores (Aula 3) fazem.

::: {.definicao title="--- Expressões regulares (REs)"}
Dado um alfabeto $\Sigma$, uma **linguagem** é um subconjunto
$L \subseteq \Sigma^*$ de palavras formadas a partir de $\Sigma$. As
expressões regulares constroem-se assim:

- $a$ --- uma letra $a \in \Sigma$ (reconhece só a palavra `"a"`)
- $\varepsilon$ --- a palavra vazia
- $M \mid N$ --- **união**: reconhece o que $M$ ou $N$ reconhecem
- $M \cdot N$ --- **concatenação**: palavras $u \cdot v$ tais que $u \in L(M)$ e $v \in L(N)$
- $M^*$ --- **repetição** (fecho de Kleene): concatenação de zero ou mais palavras de $M$
:::

::: {.definicao title="--- Convenções e abreviaturas"}
O símbolo de concatenação escreve-se muitas vezes de forma implícita:
$abc = (a \cdot b) \cdot c$ (não é ambíguo, por associatividade). A
prioridade dos operadores é `repetição > concatenação > união`, ou seja
$ab|c = (ab)|c$ e $abb* = ab(b*)$.

Abreviaturas comuns:

| Notação | Significado |
|---|---|
| `M?` | opcional: $M \mid \varepsilon$ |
| `M+` | uma ou mais vezes: $M \cdot M^*$ |
| `[x1x2...xn]` | alternativa entre carateres: $x_1\|x_2\|\dots\|x_n$ |
| `[a-z]` | intervalo de carateres contíguos |
| `[^a-z]` | complementar: qualquer carater fora do intervalo |
| `.` | qualquer carater exceto mudança de linha |
| `"a+"` | cadeia literal (entre aspas, sem interpretar `+` como operador) |
:::

::: exemplo
Descrever os *tokens* de um pequeno analisador em C:

```
if                                palavra reservada (IF)
[_a-zA-Z][_a-zA-Z0-9]*            identificadores (ID)
[0-9]+                            número inteiro (NUM)
([0-9]+"."[0-9]*)|([0-9]*"."[0-9]+)   número fracionário (REAL)
//.*                              comentário até ao final da linha
```

Note-se que `[_a-zA-Z][_a-zA-Z0-9]*` também reconheceria `if` — por isso a
ordem/prioridade importa: as regras dos geradores (Aula 3) tratam este
caso com a regra do "*first match*", colocando `if` antes do padrão de
identificador.
:::

::: atencao
**Nota adicional** (não estava explícito nos slides, mas é a razão pela
qual o Exercício 2(c) do laboratório avisa que os comentários multi-linha
"são mais difíceis do que parece"): à primeira vista pareceria bastar
`"/*" . .* . "*/"` para reconhecer um comentário `/* ... */`. O problema é
que `.` costuma **incluir tudo menos a mudança de linha**, e `.*` é
*greedy* — tentará consumir o máximo de carateres possível. Numa entrada
como `/* a */ x /* b */`, essa expressão reconheceria a linha inteira como
**um único** comentário (desde o primeiro `/*` até ao **último** `*/`), em
vez de dois comentários separados. A técnica geral para "parar no
primeiro terminador" é excluir explicitamente o carácter do terminador do
meio da expressão, por exemplo (usando `<!--`/`-->` como ilustração
diferente do exercício, para não to resolver): um comentário
`<!-- conteúdo -->` descreve-se como `"<!--" . ([^-]|"-"[^-])* . "-->"`
— "qualquer carácter que não seja `-`, ou um `-` que não seja seguido de
outro `-`", até fechar com `-->`. A mesma ideia aplica-se ao `/* ... */`
do exercício, adaptada ao terminador `*/`.
:::

## Autómatos finitos determinísticos (DFA)

As expressões regulares são **descrições declarativas**: dizem o que
reconhecer, não como. Para implementar um analisador precisamos de um
**modelo operacional** — um autómato finito.

::: {.definicao title="--- DFA"}
Um **autómato finito determinístico** é um quíntuplo
$(\Sigma, Q, q_0, F, \delta)$:

- $\Sigma$ --- alfabeto
- $Q$ --- conjunto finito de estados
- $q_0 \in Q$ --- estado inicial (único)
- $F \subseteq Q$ --- conjunto de estados finais (de aceitação)
- $\delta \subseteq Q \times \Sigma \times Q$ --- transições, **determinísticas**: para cada $q \in Q$ e $\sigma \in \Sigma$ existe **no máximo um** $q'$ tal que $(q,\sigma,q') \in \delta$. Também se pode ver $\delta$ como uma função parcial $q' = \delta(q,\sigma)$.

Uma palavra é **aceite** se, partindo de $q_0$ e seguindo as transições
para cada símbolo da palavra, se terminar num estado de $F$.
:::

::: exemplo
DFA equivalente à expressão regular de identificadores
`[_a-zA-Z][_a-zA-Z0-9]*`:

![DFA para identificadores](figuras/dfa_identificadores.pdf){width=60%}

Formalmente: $\Sigma$ = carateres ASCII, $Q=\{1,2\}$, $q_0=1$, $F=\{2\}$, e
$\delta$ contém $(1,\ell,2)$ para toda a letra/underscore $\ell$, e
$(2,\ell,2)$, $(2,d,2)$ para toda a letra/underscore $\ell$ e dígito $d$.

Percorrendo `x1`: $1 \xrightarrow{x} 2 \xrightarrow{1} 2$. Como
$2 \in F$, a palavra é **aceite**.
:::

## Autómatos finitos não-determinísticos (NFA)

::: {.definicao title="--- NFA"}
Um **NFA** tem a mesma estrutura que um DFA, mas as transições podem ser
**não-determinísticas**: $\delta \subseteq Q \times (\Sigma \cup \{\varepsilon\}) \times Q$.
Isto permite duas coisas que um DFA não tem:

- **várias transições** com o mesmo símbolo a partir do mesmo estado
  (ex: de $1$, duas transições distintas com `a`, para $2$ e para $3$);
- **transições-$\varepsilon$**, que mudam de estado **sem consumir**
  nenhum símbolo de entrada.
:::

Um NFA não se pode implementar diretamente da mesma forma que um DFA
(nunca sabemos, num dado momento, "em que estado estamos" — pode haver
vários possíveis ao mesmo tempo, e as transições-$\varepsilon$ complicam
ainda mais a leitura carácter a carácter). Por isso o percurso normal é:
**expressão regular → NFA (fácil) → DFA equivalente (mais complexo, mas
implementável diretamente)**.

### Construção de Thompson: de expressão regular a NFA

A construção de Thompson traduz uma expressão regular num NFA de forma
composicional: cada sub-expressão vira um **fragmento** de autómato com
uma única entrada e uma única saída, e os fragmentos combinam-se seguindo
a estrutura da expressão.

![Regras de Thompson: concatenação, união e repetição](figuras/thompson_rules.pdf){width=95%}

::: {.definicao title="--- Regras de Thompson"}
- **Símbolo** $\sigma \in \Sigma$: um fragmento com uma única transição
  rotulada $\sigma$ da entrada para a saída (e igual para $\varepsilon$).
- **Concatenação $A \cdot B$**: a saída do fragmento de $A$ liga-se
  diretamente à entrada do fragmento de $B$.
- **União $A \mid B$**: um novo estado de entrada liga-se, por
  $\varepsilon$, às entradas de $A$ e de $B$; as saídas de $A$ e de $B$
  ligam-se, por $\varepsilon$, a um novo estado de saída comum.
- **Repetição $A^*$**: um novo par entrada/saída; a entrada liga-se por
  $\varepsilon$ à entrada de $A$ (para iterar) e diretamente à saída (para
  "saltar" zero repetições); a saída de $A$ liga-se por $\varepsilon$ de
  volta à sua própria entrada (para repetir) e à nova saída (para
  terminar).
:::

::: exemplo
Construir o NFA para $(a\mid b)^* \cdot a \cdot c$ (o exemplo da aula), passo a passo:

1. Fragmento para `a` (estados 3→4) e fragmento para `b` (estados 5→6).
2. **União** `a|b`: novo estado 2 (entrada, $\varepsilon$ para 3 e para 5)
   e novo estado 7 (saída, $\varepsilon$ a partir de 4 e de 6).
3. **Repetição** `(a|b)*`: novo par 1 (entrada) / 8 (saída); $1 \to 2$
   (entrar no corpo), $1 \to 8$ (saltar, zero repetições), $7 \to 2$
   (repetir), $7 \to 8$ (terminar o ciclo).
4. **Concatenação** com `a`: a saída do `*` (estado 8) liga-se por `a` a
   um novo estado 9.
5. **Concatenação** com `c`: o estado 9 liga-se por `c` ao estado final 10.

![NFA de (a|b)*ac obtido por construção de Thompson](figuras/nfa_ab_star_ac.pdf){width=90%}
:::

## Conversão de NFA em DFA: construção de subconjuntos

::: {.definicao title="--- closure e construção de subconjuntos"}
Seja $\mathcal{A} = (\Sigma, Q, q_0, F, \delta)$ um NFA. Define-se

$$\text{closure}(S) = \{\, q' \in Q : \text{existe } q \in S \text{ e um caminho de transições-}\varepsilon \text{ entre } q \text{ e } q' \,\}$$

(ou seja, todos os estados alcançáveis a partir de $S$ **sem consumir
nenhum símbolo**). O NFA transforma-se no DFA equivalente
$\mathcal{A}' = (\Sigma, 2^Q, S_0, F', \delta')$, onde **cada estado do
DFA é um conjunto de estados do NFA**:

$$S_0 = \text{closure}(\{q_0\}) \qquad F' = \{\, S \subseteq Q : S \cap F \neq \emptyset \,\} \qquad \delta'(S,\sigma) = \text{closure}(\{\, q' : q \in S \wedge (q,\sigma,q') \in \delta \,\})$$

Como $\mathcal{A}'$ é determinístico, $\delta'$ pode ver-se como função.
:::

::: exemplo
Aplicando a construção de subconjuntos ao NFA de $(a\mid b)^*ac$ construído
acima. Transições-$\varepsilon$ do NFA (para calcular *closures*):
$1{\to}2$, $1{\to}8$, $2{\to}3$, $2{\to}5$, $4{\to}7$, $6{\to}7$, $7{\to}2$,
$7{\to}8$. Transições com símbolo: $3\xrightarrow{a}4$, $5\xrightarrow{b}6$,
$8\xrightarrow{a}9$, $9\xrightarrow{c}10$.

**Estado inicial**: $S_0 = \text{closure}(\{1\}) = \{1,2,3,5,8\}$ — partindo
de $1$, seguimos só $\varepsilon$: $1\to2$, $2\to3$, $2\to5$, $1\to8$;
nenhum destes ($2,3,5,8$) tem mais $\varepsilon$-saídas, por isso o
*closure* para aqui.

Calculamos agora, **estado a estado**, para onde vai $S_0$ com cada símbolo:

- **$S_0=\{1,2,3,5,8\}$ com `a`**: só os estados $3$ e $8$ (de $S_0$) têm
  transição por `a` ($3\xrightarrow{a}4$ e $8\xrightarrow{a}9$), logo
  $\text{move}=\{4,9\}$. $\text{closure}(\{4,9\})$: de $4$, $\varepsilon$
  para $7$, depois $7\to2$ e $7\to8$, depois $2\to3$ e $2\to5$; de $9$ não
  há mais $\varepsilon$. Total: $\{2,3,4,5,7,8,9\}$ — como este conjunto
  ainda não tinha aparecido, chamamos-lhe $S_1$.
- **$S_0$ com `b`**: só o estado $5$ tem transição por `b`
  ($5\xrightarrow{b}6$), logo $\text{move}=\{6\}$.
  $\text{closure}(\{6\})$: $6\to7$, depois $7\to2,7\to8$, depois
  $2\to3,2\to5$. Total: $\{2,3,5,6,7,8\}$ — novo, chamamos-lhe $S_2$.
- **$S_0$ com `c`**: nenhum estado de $S_0=\{1,2,3,5,8\}$ tem transição por
  `c` (só o estado $9$ tem, e $9 \notin S_0$) — **sem transição definida**.
:::

::: exemplo
Continuando a partir de $S_1=\{2,3,4,5,7,8,9\}$ e $S_2=\{2,3,5,6,7,8\}$:

- **$S_1$ com `a`**: estados de $S_1$ com transição `a`: $3$ e $8$ (os
  mesmos de antes, ambos $\in S_1$) $\Rightarrow \text{move}=\{4,9\}$,
  $\text{closure}=\{2,3,4,5,7,8,9\}=S_1$ — **fica no mesmo estado**
  (*self-loop* em `a`).
- **$S_1$ com `b`**: estado $5\in S_1$ tem transição `b`
  $\Rightarrow \text{move}=\{6\}$, $\text{closure}=\{2,3,5,6,7,8\}=S_2$.
- **$S_1$ com `c`**: estado $9\in S_1$ tem transição `c`
  ($9\xrightarrow{c}10$) $\Rightarrow \text{move}=\{10\}$,
  $\text{closure}(\{10\})=\{10\}$ (o $10$ não tem $\varepsilon$-saídas) —
  novo, chamamos-lhe $S_3$. Como $10$ é o estado final do NFA,
  $S_3 \in F'$.
- **$S_2$ com `a`**: só o estado $3\in S_2$ tem transição `a` (o $8$
  **não** está em $S_2$, por isso desta vez só contamos o $3$)
  $\Rightarrow \text{move}=\{4\}$, $\text{closure}(\{4\})$: $4\to7$,
  $7\to2,7\to8$, $2\to3,2\to5$. Total: $\{2,3,4,5,7,8\}$ — novo,
  chamamos-lhe $S_4$.
- **$S_2$ com `b`**: estado $5\in S_2$ $\Rightarrow \text{move}=\{6\}$,
  $\text{closure}=\{2,3,5,6,7,8\}=S_2$ — *self-loop* em `b`.
- **$S_2$ com `c`**: nenhum estado de $S_2$ tem transição `c` — sem
  transição.
- **$S_4=\{2,3,4,5,7,8\}$ com `a`**: estados $3$ e $8 \in S_4$
  $\Rightarrow \text{move}=\{4,9\}$, $\text{closure}=\{2,3,4,5,7,8,9\}=S_1$
  (já conhecido).
- **$S_4$ com `b`**: estado $5\in S_4$ $\Rightarrow \text{move}=\{6\}$,
  $\text{closure}=\{2,3,5,6,7,8\}=S_2$ (já conhecido).
- **$S_4$ com `c`**: nenhum estado de $S_4$ tem transição `c` — sem
  transição.

Todas as transições de $S_4$ vão para estados já conhecidos ($S_1$, $S_2$)
— **não aparece nenhum estado novo**, o processo termina. Resultado final:
5 estados $S_0$ a $S_4$, com $F' = \{S_3\}$ (único conjunto que contém o
estado final $10$ do NFA):

![DFA de (a|b)*ac obtido por construção de subconjuntos](figuras/dfa_ab_star_ac.pdf){width=72%}
:::

## Minimização de autómatos

O DFA obtido pela construção de subconjuntos pode ter **estados
redundantes** — estados diferentes (como conjuntos) mas com exatamente o
mesmo comportamento (as mesmas transições de saída para todo o alfabeto, e
o mesmo estatuto de aceitação). Podemos "fundir" esses estados
equivalentes e obter um **autómato mínimo** equivalente. Os geradores de
analisadores lexicais (Alex, Flex — Aula 3) fazem esta minimização
automaticamente.

::: exame
**Sai frequentemente em exame**: reconhecer estados equivalentes. No
exemplo acima, repara que $S_0=\{1,2,3,5,8\}$ e $S_4=\{2,3,4,5,7,8\}$ têm
exatamente as mesmas transições ($\xrightarrow{a} S_1$,
$\xrightarrow{b} S_2$, sem transição em `c`) — a diferença entre os
conjuntos ($1$ vs. $\{4,7\}$) não afeta o comportamento, porque nenhum
desses estados extra tem transições que consomem símbolos. Logo
$S_0 \equiv S_4$: seriam fundidos na minimização, reduzindo o autómato de
5 para 4 estados. Este é exatamente o tipo de equivalência ($S_0 \equiv
S_2$ no exemplo da aula) que costuma aparecer nos exercícios de exame
sobre minimização.
:::

# Aula 3 --- Geradores de analisadores lexicais

Recapitulando o percurso: **expressão regular → NFA (Thompson) → DFA
(subconjuntos) → implementação**. Esta aula cobre o último passo: como
implementar um analisador a partir de um DFA, e como **gerar** esse
analisador automaticamente a partir das expressões regulares (sem passar
manualmente pelos passos intermédios).

## Implementação direta de um DFA em C

Um DFA pequeno pode implementar-se com uma **tabela de transições**
(`delta[estado][símbolo]`) e um ciclo que lê carateres e segue as
transições:

::: exemplo
Para o DFA de identificadores (secção anterior), com estado `0` reservado
para representar "erro" (ausência de transição válida) e estado final `2`:

```c
#define STATES  3    // estados 0 (erro), 1, 2
#define SYMBOLS 128  // códigos ASCII
const int delta[STATES][SYMBOLS] = {
  /* estado 0 */ { 0, ..., 0, ... },       // erro é absorvente
  /* estado 1 */ { 0, ..., 2, ..., 2, ... 0 },  // letra/_  -> 2
  /* estado 2 */ { 0, ..., 2, ..., 2, ... 0 } };// letra/_/dígito -> 2

int state = 1;         // estado inicial
int c;
while ((c = getchar()) != EOF) {
  state = delta[state][c];
  if (state == 0) return ERROR;   // rejeita
  if (FINAL(state)) return ACCEPT; // aceita (aqui, FINAL(state) é state==2)
}
return ERROR; // fim do input sem atingir estado final
```

**Traçando a execução** com a entrada `"x1"`:

| Passo | `c` lido | `delta[state][c]` | novo `state` | ação |
|---|---|---|---|---|
| 1 | `x` (letra) | `delta[1]['x']` = 2 | 2 | `state != 0` (não rejeita); `FINAL(2)` é verdade → **`return ACCEPT` imediatamente** |

O ciclo **nunca chega a ler o `1`**! Isto revela uma limitação importante
deste pseudo-código, que vale a pena perceber bem: ele aceita assim que
atinge **qualquer** estado final, não espera para ver se consumindo mais
carateres continuaria num estado válido (não implementa *longest match*).
Para este DFA de identificadores em particular isto até não causa erro de
classificação (qualquer prolongamento de um identificador continua a ser
um identificador válido), mas é exatamente o motivo por que os analisadores
lexicais reais (Aula 3, secção "Longest match e first match", abaixo) têm
de **guardar a posição do último estado final visto e continuar a tentar
consumir mais carateres**, só decidindo aceitar quando deixar de haver
transição possível — este pseudo-código simplificado dos slides ilustra a
ideia da tabela de transições, mas não implementa essa regra.

Isto funciona como ilustração da tabela de transições, mas é
**específico de um único DFA** — cada novo token exigiria escrever/combinar
mais tabelas à mão. É exatamente este trabalho mecânico que os geradores
(abaixo) automatizam a partir de expressões regulares.
:::

## Alex (gerador para Haskell)

::: {.definicao title="--- Alex"}
O **Alex** é um gerador de analisadores lexicais para Haskell. Recebe um
ficheiro de descrição (ex: `Lexer.x`) com regras "expressão regular →
ação em Haskell" e definições auxiliares, e produz um ficheiro `Lexer.hs`
que pode ser compilado com o resto do projeto.

$$\texttt{Lexer.x} \xrightarrow{\texttt{alex}} \texttt{Lexer.hs} \xrightarrow{\text{compilador Haskell}} \text{executável}$$
:::

::: exemplo
```
{
module Lexer where
}
%wrapper "basic"
$alpha = [_a-zA-Z]
$digit = [0-9]

tokens :-
$white+                      ;  -- ignorar carateres brancos
if                            { \_ -> IF }
$alpha($alpha|$digit)*        { \s -> ID s }
$digit+                       { \s -> NUM (read s) }
$digit+"."$digit+              { \s -> REAL (read s) }

{
data Token = IF | ID String | NUM Int | REAL Double
}
```

As partes entre `{ }` são código Haskell; o resto são diretivas,
definições e padrões. Cada regra tem a forma `padrão { ação }`, onde o
padrão é uma expressão regular e a ação é uma função `String -> Token`.
Usar: `Lexer.hs` exporta `alexScanTokens :: String -> [Token]`.

```haskell
module Main where
import Lexer
main = do
  txt <- getContents
  print (alexScanTokens txt)
```
:::

O exemplo acima usa a interface `%wrapper "basic"`. Existe também
`%wrapper "posn"`, que associa a cada token a sua **posição** (linha e
coluna) — útil para reportar erros com precisão. Nesse caso, cada ação
passa a ter tipo `AlexPosn -> String -> Token`, com
`data AlexPosn = AlexPn Int Int Int` (posição absoluta, linha, coluna), e
o padrão de cada regra recebe também `pos` (ex: `\pos s -> ID pos s`).

## Flex (gerador para C)

::: {.definicao title="--- Flex"}
O **Flex** é o equivalente do Alex mas para C. Recebe um ficheiro `.l`
(ex: `lexer.l`) e produz `lex.yy.c`, compilável com o resto do projeto C.

$$\texttt{ficheiro.l} \xrightarrow{\texttt{flex}} \texttt{lex.yy.c} \xrightarrow{\text{compilador C}} \text{executável}$$
:::

::: exemplo
```
%{
#include "tokens.h"
%}
%option noyywrap
alpha       [_a-zA-Z]
digit       [0-9]
%%

[ \t\n\r]+                 /* skip whitespace */
if                          { return IF; }
{alpha}({alpha}|{digit})*   { return ID; }
{digit}+                    { yynum = atoi(yytext); return NUM; }
{digit}+"."{digit}+          { yyreal = atof(yytext); return REAL; }
<<EOF>>                     { return EOF; /* end of input */ }
```

Estrutura geral de um ficheiro Flex: `%{ declarações %}`, depois
definições auxiliares, `%%`, depois as regras `padrão { ação em C }`, e
opcionalmente mais `%%` seguido de código C auxiliar.

```c
#include "tokens.h"
int main(void) {
  int token;
  while ((token = yylex()) != EOF) {
    switch (token) {
      case IF:   printf("IF ");               break;
      case ID:   printf("ID(%s) ", yytext);    break;
      case NUM:  printf("NUM(%d) ", yynum);    break;
      case REAL: printf("REAL(%f) ", yyreal);  break;
    }
  }
}
```

A função `yylex()` devolve o próximo token (um inteiro, definido num
ficheiro *header*). A variável global `yytext` contém sempre o texto do
token atual — é assim que se acede ao valor (ex: o nome de um
identificador). Os valores de tokens não-textuais (como `NUM`, `REAL`)
costumam guardar-se em variáveis de estado globais (`yynum`, `yyreal`).
:::

::: atencao
Nota adicional: por omissão o Flex **não** guarda a posição de cada token.
Para isso usa-se `%option yylineno`, que mantém a variável global
`yylineno` com o número da linha atual — mas é **responsabilidade do
programador** ir guardando essa posição à medida que os tokens são
consumidos (ao contrário do Alex com `%wrapper "posn"`, que já entrega a
posição em cada ação).
:::

## Longest match e first match

::: {.definicao title="--- Regras de desambiguação"}
Tanto o Alex como o Flex (e geradores semelhantes) usam duas regras, por
esta ordem, para decidir qual regra aplicar quando várias expressões
regulares poderiam casar com o *input*:

1. **Longest match**: escolhe-se a regra que consome o **maior número de
   carateres** de entrada.
2. **First match**: em caso de empate no comprimento, escolhe-se a regra
   que aparece **primeiro** no ficheiro de descrição.
:::

::: exame
Consequência prática (e fonte comum de bugs/perguntas de exame):
identificadores e palavras reservadas partilham o mesmo texto possível
(`if` casa tanto com o padrão literal `if` como com o padrão de
identificador `[_a-zA-Z][_a-zA-Z0-9]*`, com o **mesmo comprimento** — 2
carateres). Por *first match*, a regra que resolve a ambiguidade
corretamente é **colocar os padrões mais específicos (palavras
reservadas) antes dos mais gerais (identificadores)** no ficheiro `.x`/
`.l`. Se a ordem for trocada, `if` seria sempre lido como `ID`, nunca
como `IF`.
:::

## Comparação rápida Alex vs. Flex

| | Alex | Flex |
|---|---|---|
| Linguagem gerada | Haskell (`.hs`) | C (`lex.yy.c`) |
| Ficheiro de entrada | `.x` | `.l` |
| Acesso ao texto do token | argumento da ação (`\s -> ...`) | variável global `yytext` |
| Posição do token | `%wrapper "posn"` (automático, por ação) | `%option yylineno` (manual) |
| Função de arranque | `alexScanTokens :: String -> [Token]` | `yylex()` (chamado em ciclo) |

## Ligação com a prática (Folha laboratorial 2 --- `scanner-c`)

O laboratório desta semana (`Semana_1/scanner-c/`) dá um analisador
lexical em C incompleto (`CLexer.c`) para os tokens `ID`, `NUM`, `LPAREN`,
`RPAREN`, `COMMA`, `IF`, e pede para o completar/re-implementar:

- **Exercício 1** (estender `CLexer.c`): usa diretamente a secção
  "Implementação direta de um DFA em C" acima — o `switch`/`while` do
  ficheiro fornecido segue exatamente o padrão de "ler carácter, decidir
  por casos" descrito ali, só que sem tabela explícita de transições.
  Repara em particular no aviso da Aula 2 sobre a ordem `if` vs. `ID` (a
  alínea sobre `_` como identificador é um caso de expressão regular
  `[_a-zA-Z]` mal transcrita para o `switch` do C — falta o `case '_':`
  a par de `isalpha(c)`).
- **Exercício 2** (expressões regulares, papel e lápis): usa a secção
  "Expressões regulares" — em particular a caixa de atenção sobre
  comentários multi-linha explica a técnica geral necessária para a
  alínea (c).
- **Exercício 3** (reimplementar com `flex`): usa diretamente a secção
  "Flex" acima, incluindo a estrutura do ficheiro `.l` e o exemplo
  completo.
