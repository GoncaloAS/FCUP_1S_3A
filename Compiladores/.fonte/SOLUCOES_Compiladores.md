---
title: "Compiladores --- Soluções dos exercícios \"Pratica agora\""
subtitle: "Folha laboratorial 2 (Praticas/Semana_1/scanner-c), Folha laboratorial 3 (Praticas/Semana_2/gramatica) Folha laboratorial 4 (Praticas/Semana_3/Parsing) lab. ASTs (Praticas/Semana_4/Abstract_Syntax_Trees) e exercícios da Aula 7 (slides e inventados). Tenta primeiro sozinho; abre uma alínea só depois de a teres feito."
---

## Aula 2 --- Expressões regulares

### Ex. 2 --- Expressões regulares (papel e lápis)

#### (a) Expressões regulares para todos os tokens (incluindo os do Exercício 1)

Com as abreviaturas `letra = [_a-zA-Z]` (o `_` conta como letra, alínea
1(c)) e `digito = [0-9]`:

| Token | Expressão regular |
|:--|:--|
| `IF` | `if` |
| `WHILE` | `while` |
| `FOR` | `for` |
| `INT` | `int` |
| `FLOAT` | `float` |
| `ID` | `letra (letra | digito)*` |
| `NUM` | `digito+` |
| `REAL` | `digito+ \. digito+` |
| `LPAREN`, `RPAREN` | `\(`, `\)` |
| `LBRACE`, `RBRACE` | `\{`, `\}` |
| `COMMA` | `,` |
| `SEMICOLON` | `;` |

As palavras reservadas também são aceites pela expressão de `ID`. A
ambiguidade resolve-se com a regra do *first match*: as palavras
reservadas vêm **antes** de `ID` na lista. O `.`, os parêntesis e as
chavetas levam `\` porque são operadores nas expressões regulares.

#### (b) `REAL` também em notação científica (`12.34e+12`, `1e-12`, `123.4E+9`)

A parte do expoente é `[eE] [+-]? digito+`: um `e` ou `E`, um sinal
opcional e pelo menos um dígito.

O `1e-12` **não tem ponto**. Tornar só o expoente opcional,
`digito+ \. digito+ ([eE][+-]?digito+)?`, não chega. A solução é juntar
dois casos:
```
digito+ \. digito+ ( [eE] [+-]? digito+ )?      -- com ponto, expoente opcional
| digito+ [eE] [+-]? digito+                     -- sem ponto, expoente obrigatório
```

Teste:

| Entrada | É REAL? | Porquê |
|:--|:-:|:--|
| `12.34e+12` | sim | 1.º caso |
| `1e-12` | sim | 2.º caso |
| `123.4E+9` | sim | 1.º caso |
| `42` | **não** | continua a ser `NUM` |
| `1e` | não | o expoente precisa de dígitos |

Não se escreve `digito+ (\. digito+)? ([eE][+-]?digito+)?`, porque essa
expressão também aceita `42` e passaria a haver dois tokens para o mesmo
texto.

#### (c) Comentários `// ...` e `/* ... */`

**Até ao fim da linha:**
```
"//" [^\n]*
```

**Multi-linha**, a expressão "difícil":
```
"/*" ( [^*] | "*"+ [^*/] )* "*"+ "/"
```

Leitura, parte a parte:

- `"/*"` abre o comentário.
- `( [^*] | "*"+ [^*/] )*` é o miolo. Em cada passo aceita um carácter
  que **não** é `*`, **ou** uma série de `*` seguida de um carácter que
  **não** é `*` nem `/`. Assim nunca se consome um `*/`, porque um `*`
  só passa se o que vem a seguir não for `/`.
- `"*"+ "/"` fecha. É `"*"+` e não só `"*"` para aceitar `**/` e `***/`.

Casos que a versão "ingénua" `"/*" .* "*/"` falha e esta acerta:

| Entrada | Ingénua | Correta |
|:--|:--|:--|
| `/* a */ x = 1; /* b */` | engole **tudo** até ao último `*/` (*longest match*) | só `/* a */` |
| `/* a **/` | ok | ok (o `"*"+` final come os dois `*`) |
| `/***/` | ok | ok (miolo vazio, `"*"+` = `**`) |
| `/* linha 1`↵`linha 2 */` | falha: o `.` não aceita `\n` | ok (`[^*]` aceita `\n`) |

## Aula 3 --- Implementação direta de um DFA em C

### Ex. 1 --- Estender `CLexer.c`

A versão completa, que passa os 5 testes de `tests/`, está em
`Praticas/Semana_1/scanner-c/src/CLexer.c`. Abaixo fica só o que cada
alínea acrescenta.

#### (a) Tokens `LBRACE` `{`, `RBRACE` `}` e `SEMICOLON` `;`

São tokens de um carácter só, com o mesmo padrão de `LPAREN`. Basta
acrescentar ao `enum` e ao `switch`:

```c
typedef enum { ID, NUM, REAL, SEMICOLON, COMMA, LPAREN, RPAREN,
               LBRACE, RBRACE, IF, INT, FLOAT, WHILE, FOR, END_OF_FILE } TokenType;
...
switch (c) {
  case '(': return LPAREN;
  case ')': return RPAREN;
  case ',': return COMMA;
  case ';': return SEMICOLON;   /* novo */
  case '{': return LBRACE;      /* novo */
  case '}': return RBRACE;      /* novo */
  ...
```

E também os `case` correspondentes em `printToken()`, para imprimir
`LBRACE`, etc.

#### (b) Palavras reservadas `WHILE`, `FOR`, `INT`, `FLOAT`

**Não** se criam estados novos para cada palavra. Lê-se o identificador
inteiro como já se fazia para `if`, e **no fim** compara-se o texto:

```c
token_value->text[k] = '\0';
if      (strcmp(token_value->text, "if")    == 0) return IF;
else if (strcmp(token_value->text, "for")   == 0) return FOR;
else if (strcmp(token_value->text, "while") == 0) return WHILE;
else if (strcmp(token_value->text, "int")   == 0) return INT;
else if (strcmp(token_value->text, "float") == 0) return FLOAT;
else return ID;
```

Isto implementa o *longest match* sem esforço: `integer` é lido
**inteiro** antes de comparar, e por isso dá `ID(integer)` e não
`INT ID(eger)`. O teste 2 verifica exatamente isso, e também que `WHILE`
em maiúsculas é `ID`.

#### (c) Aceitar `_` como letra

O `isalpha(c)` não aceita `_`. É preciso acrescentá-lo nos **dois**
sítios: no carácter inicial e no ciclo que lê o resto do identificador.

```c
else if (isalpha(c) || c == '_') {                  /* início */
    ...
    while (isalpha(c) || isdigit(c) || c == '_') {  /* resto  */
```

Se só se mudar o primeiro sítio, `a_bc` dá `ID(a)` seguido de `ID(_bc)`.
O teste 3 (`Abc123 a_bc123 _abc123`) apanha os dois erros.

#### (d) Token `REAL` (`0.5`, `123.45`)

Depois de ler os dígitos de um número, **se o carácter seguinte for `.`**,
continua-se no "estado" da parte decimal em vez de devolver `NUM`:

```c
if (isdigit(c)) {
    int val = 0; float fval = 0.0, divisor = 10.0;
    while (isdigit(c)) { val = 10 * val + c - '0'; c = getchar(); }

    if (c == '.') {                       /* estado novo: parte decimal */
        c = getchar();
        while (isdigit(c)) {
            fval += (c - '0') / divisor;
            divisor *= 10.0;
            c = getchar();
        }
        ungetc(c, stdin);
        token_value->fval = val + fval;
        return REAL;
    }
    ungetc(c, stdin);
    token_value->ival = val;
    return NUM;
}
```

**Traço de `123.375`:** `val` fica 1, 12, 123. Aparece o `.`. Depois:

- `3`: `fval` = 3/10 = 0.3
- `7`: `fval` = 0.3 + 7/100 = 0.37
- `5`: `fval` = 0.37 + 5/1000 = 0.375

Resultado: `REAL(123.375000)` $\checkmark$ (teste 4).

#### (e) Ignorar comentários `/* ... */` e `// ...`

Os comentários, tal como os espaços, **não** são tokens. Por isso
salta-se num ciclo, alternadamente, "espaços, comentário, espaços,
comentário...", até aparecer um carácter que começa um token a sério:

```c
for (;;) {
    while (isspace(c)) c = getchar();
    if (c != '/') break;                  /* não é comentário */
    int next = getchar();
    if (next == '*') {                    /* /* ... */
        c = getchar();
        for (;;) {
            while (c != '*' && c != EOF) c = getchar();
            if (c == EOF) { fprintf(stderr, "comentário não fechado\n"); exit(-1); }
            c = getchar();                /* o que vem depois do '*' */
            if (c == '/') { c = getchar(); break; }
            /* se for outro '*' (ex: "**/"), o while volta a testá-lo */
        }
    } else if (next == '/') {             /* // até ao fim da linha */
        c = next;
        while (c != '\n' && c != EOF) c = getchar();
    } else {                              /* '/' sozinho: devolve o next */
        ungetc(next, stdin);
        break;
    }
}
```

É o DFA da expressão regular da 2(c) escrito à mão. O "depois de um `*`,
se vier `/` fecha, senão continua" corresponde ao `"*"+ [^*/]` do miolo.
O `for (;;)` exterior trata `/* a */ // b` e comentários seguidos. O
teste 5 cobre os dois tipos.

#### (f) *Buffer overrun* nos identificadores

`text` tem 255 posições. Um identificador com 300 letras escrevia para
lá do fim do array, o que é comportamento indefinido: pode estragar a
memória ou fazer crashar o programa. A correção é só escrever enquanto
houver espaço, reservando um lugar para o `'\0'`:

```c
int k = 0;
while (isalpha(c) || isdigit(c) || c == '_') {
    if (k < sizeof(token_value->text) - 1) {   /* deixa espaço para o '\0' */
        token_value->text[k] = c;
        k++;
    }
    c = getchar();          /* continua a CONSUMIR o identificador todo */
}
token_value->text[k] = '\0';
```

O `getchar()` fica **fora** do `if`. O identificador é consumido todo
mesmo que não caiba, e só se truncam os caracteres guardados. Se se
parasse de ler, o resto do identificador apareceria como um segundo
token. Outra opção válida é dar erro
(`fprintf(stderr, "identificador demasiado longo")`), mas nunca escrever
fora do array.

## Aula 3 --- Flex

### Ex. 3 --- Reimplementar com `flex`

#### Ficheiro `lexer.l` completo e como testar

```lex
%{
#include <stdio.h>
%}
%option noyywrap
alpha    [_a-zA-Z]
digit    [0-9]
%%
[ \t\n]+                      { }
"("                           { printf("LPAREN "); }
")"                           { printf("RPAREN "); }
","                           { printf("COMMA "); }
";"                           { printf("SEMICOLON "); }
"{"                           { printf("LBRACE "); }
"}"                           { printf("RBRACE "); }
"if"                          { printf("IF "); }
"while"                       { printf("WHILE "); }
"for"                         { printf("FOR "); }
"int"                         { printf("INT "); }
"float"                       { printf("FLOAT "); }
{alpha}({alpha}|{digit})*     { printf("ID(%s) ", yytext); }
[0-9]+                        { printf("NUM(%d) ", atoi(yytext)); }
[0-9]+"."[0-9]*               { printf("REAL(%f) ", atof(yytext)); }
"//".*                        { }
"/*"([^*]|"*"+[^*/])*"*"+"/"  { }
%%
int main(void) {
  yylex();
  printf("\n");
  return 0;
}
```

```
$ flex lexer.l && gcc lex.yy.c -o Lexer
$ ./Lexer < tests/input1.txt
```

Este ficheiro (é o que está em `scanner-c/lexer.l`) dá a saída esperada
nos 5 testes.

**Pontos a verificar:**

- **Ordem (first match):** `"if"` e as outras palavras reservadas estão
  **antes** de `{alpha}(...)*`. Com `if`, as duas regras casam 2
  caracteres e ganha a primeira da lista, que é `IF`.
- **Longest match:** com `iffy`, a regra de `ID` casa 4 caracteres e
  `"if"` só 2. Ganha a mais comprida, e sai `ID(iffy)`, **não**
  `IF ID(fy)`. Testado: `echo "iffy if_" | ./Lexer` dá `ID(iffy) ID(if_)`.
- `"//".*`: no flex o `.` não aceita `\n`, por isso isto pára no fim da
  linha, como se quer.
- O comentário multi-linha é **exatamente** a expressão da 2(c).
- Sem `%option noyywrap` é preciso definir `yywrap()` ou ligar com `-lfl`.
- Esta versão de `REAL` aceita `5.` (zero dígitos depois do ponto) e não
  tem notação científica. `12.5e3` sai como `REAL(12.5) ID(e3)`. Para
  tratar a 2(b), troca a regra de `REAL` pela expressão dessa alínea.

## Aula 4 --- Escrever uma gramática para uma linguagem

### Ex. 1 --- Escrever gramáticas (Folha lab. 3)

Terminais indicados em cada alínea; símbolo inicial $S$.

#### (b) Mesmo número de `a`s e `b`s, por qualquer ordem

$$S \to a\,S\,b\,S \mid b\,S\,a\,S \mid \varepsilon$$

**Porque é que gera todas as palavras certas.** Seja $w$ não vazia com
tantos `a`s como `b`s. Lê-se $w$ da esquerda para a direita, contando
$d = (\text{nº de a's}) - (\text{nº de b's})$ já lidos. No fim $d=0$.

- Se $w$ começa por `a`, $d$ passa a 1. Há um **primeiro** ponto em que
  $d$ volta a 0, e esse passo tem de ser um `b` (só um `b` faz $d$
  descer). Então $w = a\,u\,b\,v$, em que:
  - $u$ (entre o `a` e esse `b`) começa e acaba com $d=1$, logo tem
    tantos `a`s como `b`s;
  - $v$ (o resto) vai de $d=0$ a $d=0$, logo também.

  Isto é exatamente $S\to a\,S\,b\,S$, com o primeiro $S$ a gerar $u$ e o
  segundo a gerar $v$ (por indução, porque são mais curtas).
- Se $w$ começa por `b`, é simétrico: $w = b\,u\,a\,v$, $S\to b\,S\,a\,S$.

**Porque é que não gera palavras erradas.** Cada produção acrescenta um
`a` e um `b` (ou nada), por isso as contagens ficam sempre iguais.

**Exemplo:** `abba`. Começa por `a`; $d$ vale 1, 0 depois de `ab`: $u=\varepsilon$,
$v=$ `ba`.
$$S \Rightarrow a\underline{S}bS \Rightarrow ab\underline{S} \Rightarrow abb\underline{S}aS \Rightarrow abba\underline{S} \Rightarrow abba$$
(o segundo, o quarto e o quinto passos usam $S\to\varepsilon$; o terceiro
usa $S\to bSaS$ para gerar `ba`).

Verificado por força bruta: gera exatamente as palavras certas até
comprimento 8. Também serve $S\to SS\mid aSb\mid bSa\mid\varepsilon$, mas
essa é **ambígua** (por causa de $S\to SS$, como o $S\to S;S$ do Ex. 2).

#### (c) Parêntesis casados

$$S \to (\,S\,)\,S \mid \varepsilon$$

É a mesma ideia da alínea (b), com `(` no papel de `a` e `)` no papel de
`b`, mas **só com a primeira produção**: uma palavra casada nunca pode
começar por `)`. Uma palavra não vazia começa por `(`; esse `(` fecha
num certo `)`. O que está lá dentro é casado (é o primeiro $S$) e o que
vem depois também (é o segundo $S$).

**Exemplo:** `(()(()))`. O primeiro `(` fecha no último `)`: dentro está
`()(())`, depois não há nada.
$$\begin{aligned}
S &\Rightarrow (S)S \Rightarrow ((S)S)S \Rightarrow (()S)S \Rightarrow (()(S)S)S\\
&\Rightarrow (()((S)S)S)S \Rightarrow (()(()S)S)S \Rightarrow (()(())S)S\\
&\Rightarrow (()(()))S \Rightarrow (()(()))
\end{aligned}$$
(derivação mais à esquerda; os passos 3, 6, 7, 8 e 9 usam $S\to\varepsilon$).

As palavras rejeitadas do enunciado não se geram: `)` e `)(` começam por
`)`; `(` e `(()` têm mais `(` do que `)`; `()())` tem mais `)`. Esta é
a gramática que a Aula 5 usa como exemplo para a análise LR.

#### (e) `((0|1)+"."(0|1)*)|((0|1)*"."(0|1)+)`

Terminais `0`, `1` e `.`. Pela tabela "de expressão regular para
gramática" do resumo, um não-terminal por sub-expressão:

$$\begin{aligned}
S &\to P\ .\ Q \mid Q\ .\ P && \text{a alternativa de topo}\\
P &\to D\,P \mid D && (0|1)^+\text{: um ou mais dígitos}\\
Q &\to D\,Q \mid \varepsilon && (0|1)^*\text{: zero ou mais dígitos}\\
D &\to 0 \mid 1 && \text{um dígito}
\end{aligned}$$

- `10.` vem de $S\to P.Q$, com $P$ a gerar `10` e $Q\to\varepsilon$.
- `.1` vem de $S\to Q.P$, com $Q\to\varepsilon$ e $P$ a gerar `1`.
- `.` sozinho não se gera: as duas alternativas precisam de pelo menos
  um dígito ($P$ nunca é vazio).

A gramática é ambígua (`1.0` vem das duas alternativas), tal como a
própria expressão regular; o enunciado não pede mais. Uma versão não
ambígua com a mesma linguagem é $S\to P\,.\,Q \mid .\,P$ ("pelo menos um
dígito antes do ponto" ou "nenhum antes e pelo menos um depois").
Ambas verificadas por força bruta até comprimento 7.

## Aula 4 --- Ambiguidade

### Ex. 2 --- Programas sequenciais (Folha lab. 3, também exercício dos slides)

$S \to S;S \mid \texttt{ident}=E \mid \texttt{ident}{+}{+}$ e
$E \to \texttt{ident} \mid \texttt{num} \mid E+E$.

#### (a) Mostrar que é ambígua (e encontrar mais do que um exemplo)

Há dois sítios diferentes onde a ambiguidade aparece.

**Exemplo 1, nas instruções ($S \to S;S$).** Frase: `a=1; b=2; c++`. Tem **duas** árvores sintáticas diferentes. Nas
duas, a raiz é $S \to S;S$, e o que muda é onde fica o segundo `;`:

- **agrupar à esquerda:** `(a=1; b=2); c++`
  $$S \Rightarrow \underline{S};S \Rightarrow (S;S);S \Rightarrow \dots$$
  O filho esquerdo da raiz é outro $S;S$.
- **agrupar à direita:** `a=1; (b=2; c++)`
  $$S \Rightarrow S;\underline{S} \Rightarrow S;(S;S) \Rightarrow \dots$$
  O filho direito da raiz é outro $S;S$.

Duas árvores diferentes para a mesma frase chegam para a gramática ser
ambígua. (Aqui as duas leituras executam o mesmo, mas a gramática
continua a ser ambígua.)

**Exemplo 2, nas expressões ($E \to E+E$).** Frase: `x = a+b+c`. É o mesmo problema de `E → E+E` do resumo:

- `x = (a+b)+c`: o $E$ de topo é $E+E$ e o seu filho **esquerdo** é
  outro $E+E$.
- `x = a+(b+c)`: o filho **direito** é que é outro $E+E$.

São duas árvores diferentes para a mesma frase.

#### (b) Reescrever a gramática sem ambiguidade

Aplica-se a técnica do resumo (recursão à esquerda, que dá associatividade
à esquerda) **nos dois sítios**, introduzindo um não-terminal novo para
cada nível:

$$
\begin{aligned}
S &\to S\,;\,I \mid I \\
I &\to \texttt{ident} = E \mid \texttt{ident}{+}{+} \\
E &\to E + T \mid T \\
T &\to \texttt{ident} \mid \texttt{num}
\end{aligned}
$$

- $I$ é "uma instrução só". Numa sequência, o lado direito de cada `;` é
  sempre uma instrução, e por isso `a=1; b=2; c++` só tem a leitura
  `(a=1; b=2); c++`.
- $T$ é "uma parcela". O lado direito de cada `+` é sempre uma parcela, e
  por isso `a+b+c` só tem a leitura `(a+b)+c`.

A linguagem é a mesma: continuam a gerar-se todas as sequências de uma ou
mais instruções, e todas as somas de uma ou mais parcelas. Só se retirou
a escolha de agrupamento.

## Aula 5 --- Autómato e tabela LR(0)

### Ex. 4 --- Extensão da gramática de parêntesis (Folha lab. 3)

$E \to (L) \mid \texttt{a}$ e $L \to L,E \mid E$. Produções numeradas,
com a produção nova: (0) $S'\to E\,\$$, (1) $E\to(L)$, (2) $E\to\texttt{a}$,
(3) $L\to L,E$, (4) $L\to E$.

#### (a) Derivação de `((a),a,(a,a))`

A palavra é um $E$ da forma `( L )`, e o $L$ de fora é a lista
`(a)`, `a`, `(a,a)` (três $E$ separados por vírgulas). Derivação mais à
esquerda (sublinhado: o não-terminal que vai ser substituído):

$$\begin{aligned}
\underline{E} &\Rightarrow (\underline{L}) && E\to(L)\\
&\Rightarrow (\underline{L},E) && L\to L,E\\
&\Rightarrow (\underline{L},E,E) && L\to L,E\\
&\Rightarrow (\underline{E},E,E) && L\to E\\
&\Rightarrow ((\underline{L}),E,E) && E\to(L)\\
&\Rightarrow ((\underline{E}),E,E) && L\to E\\
&\Rightarrow ((a),\underline{E},E) && E\to a\\
&\Rightarrow ((a),a,\underline{E}) && E\to a\\
&\Rightarrow ((a),a,(\underline{L})) && E\to(L)\\
&\Rightarrow ((a),a,(\underline{L},E)) && L\to L,E\\
&\Rightarrow ((a),a,(\underline{E},E)) && L\to E\\
&\Rightarrow ((a),a,(a,\underline{E})) && E\to a\\
&\Rightarrow ((a),a,(a,a)) && E\to a
\end{aligned}$$

Repara que uma lista de $n$ elementos usa $L\to L,E$ $(n-1)$ vezes e
depois $L\to E$ uma vez: é a recursão à esquerda a construir a lista da
direita para a esquerda.

#### (b) Autómato LR(0)

**Estado 0** = fecho($\{S'\to\bullet E\,\$\}$). Ponto antes de $E$: entram
$E\to\bullet(L)$ e $E\to\bullet\texttt{a}$ (ponto antes de terminais:
pára). $0 = \{S'\to\bullet E\,\$,\ E\to\bullet(L),\ E\to\bullet\texttt{a}\}$.

- goto(0, `(`) = fecho($\{E\to(\bullet L)\}$). Ponto antes de $L$: entram
  $L\to\bullet L,E$ e $L\to\bullet E$. Em $L\to\bullet L,E$ o ponto está
  outra vez antes de $L$, mas esses items já lá estão. Em $L\to\bullet E$
  o ponto está antes de $E$: entram $E\to\bullet(L)$ e $E\to\bullet\texttt{a}$.
  **Estado 1** $= \{E\to(\bullet L),\ L\to\bullet L,E,\ L\to\bullet E,\
  E\to\bullet(L),\ E\to\bullet\texttt{a}\}$.
- goto(0, `a`) = $\{E\to\texttt{a}\bullet\}$: **estado 2**.
- goto(0, $E$) = $\{S'\to E\bullet\$\}$: **estado 3**.

**Transições de 1:**

- goto(1, `(`): de $E\to\bullet(L)$ vem $E\to(\bullet L)$, cujo fecho é o
  **estado 1**.
- goto(1, `a`) = **estado 2**.
- goto(1, $E$): de $L\to\bullet E$ vem $\{L\to E\bullet\}$: **estado 4**.
- goto(1, $L$): **dois** items têm o ponto antes de $L$: $E\to(\bullet L)$
  e $L\to\bullet L,E$. Avançam os dois: $\{E\to(L\bullet),\ L\to L\bullet,E\}$
  (pontos antes de terminais: o fecho não junta nada). **Estado 5**.

**Transições de 5:**

- goto(5, `)`) = $\{E\to(L)\bullet\}$: **estado 6**.
- goto(5, `,`) = fecho($\{L\to L,\bullet E\}$). Ponto antes de $E$: entram
  $E\to\bullet(L)$ e $E\to\bullet\texttt{a}$. **Estado 7**.

**Transições de 7:** goto(7, `(`) = **estado 1**; goto(7, `a`) = **estado 2**;
goto(7, $E$) = $\{L\to L,E\bullet\}$: **estado 8**.

Os estados 2, 4, 6 e 8 só têm um item completo (sem transições) e o
estado 3 só tem a transição por \$ (accept). Total: estados 0 a 8.

![Autómato LR(0) do Exercício 4](figuras/sol_lr0_dfa_EL.svg){width=100%}

#### (c) É LR(0)? Tabela de *parsing*

**É LR(0).** Um conflito só pode aparecer num estado com um item completo
e mais alguma coisa. Os estados com item completo são 2, 4, 6 e 8, e
cada um tem **só esse item** (nenhum *shift*, nenhum outro *reduce*).
Os estados com *shifts* (0, 1, 5, 7) não têm items completos. Logo não
há conflitos.

Tabela (*reduce* em todas as colunas terminais, porque é LR(0)):

| | ( | ) | a | , | \$ | E | L |
|---|---|---|---|---|---|---|---|
| 0 | s1 | | s2 | | | g3 | |
| 1 | s1 | | s2 | | | g4 | g5 |
| 2 | r2 | r2 | r2 | r2 | r2 | | |
| 3 | | | | | a | | |
| 4 | r4 | r4 | r4 | r4 | r4 | | |
| 5 | | s6 | | s7 | | | |
| 6 | r1 | r1 | r1 | r1 | r1 | | |
| 7 | s1 | | s2 | | | g8 | |
| 8 | r3 | r3 | r3 | r3 | r3 | | |

O estado 5 é o único que podia parecer perigoso (dois items), mas os dois
têm o ponto antes de um terminal diferente (`)` e `,`): são dois *shifts*
em colunas diferentes.

### Ex. 5 --- Declarações de variáveis em C (Folha lab. 3)

Produções numeradas: (0) $S'\to Decl\,\$$, (1) $Decl\to Type\ Varlist\ ;$,
(2) $Type\to\texttt{int}$, (3) $Type\to\texttt{float}$,
(4) $Varlist\to Varlist\,,\,\texttt{ident}$, (5) $Varlist\to\texttt{ident}$.

#### (a) Autómato LR e tabela LR(0)

**Estado 0** = fecho($\{S'\to\bullet Decl\,\$\}$). Ponto antes de $Decl$:
entra $Decl\to\bullet Type\ Varlist\ ;$. Aí o ponto está antes de $Type$:
entram $Type\to\bullet\texttt{int}$ e $Type\to\bullet\texttt{float}$.

- goto(0, `int`) = $\{Type\to\texttt{int}\bullet\}$: **estado 1**.
- goto(0, `float`) = $\{Type\to\texttt{float}\bullet\}$: **estado 2**.
- goto(0, $Decl$) = $\{S'\to Decl\bullet\$\}$: **estado 3**.
- goto(0, $Type$) = fecho($\{Decl\to Type\bullet Varlist\ ;\}$). Ponto
  antes de $Varlist$: entram $Varlist\to\bullet Varlist,\texttt{ident}$ e
  $Varlist\to\bullet\texttt{ident}$. **Estado 4**.

**Transições de 4:**

- goto(4, `ident`) = $\{Varlist\to\texttt{ident}\bullet\}$: **estado 5**.
- goto(4, $Varlist$): avançam $Decl\to Type\bullet Varlist\ ;$ e
  $Varlist\to\bullet Varlist,\texttt{ident}$. **Estado 6** $=
  \{Decl\to Type\ Varlist\bullet ;,\ Varlist\to Varlist\bullet,\texttt{ident}\}$.

**Transições de 6:** goto(6, `,`) = $\{Varlist\to Varlist,\bullet\texttt{ident}\}$:
**estado 7**; goto(6, `;`) = $\{Decl\to Type\ Varlist\ ;\bullet\}$: **estado 8**.

**Transições de 7:** goto(7, `ident`) = $\{Varlist\to Varlist,\texttt{ident}\bullet\}$:
**estado 9**.

![Autómato LR(0) do Exercício 5](figuras/sol_lr0_dfa_Decl.svg){width=100%}

Tabela LR(0) (`id` = `ident`). Os estados com item completo (1, 2, 5, 8,
9) só têm esse item, por isso não há conflitos: a gramática é LR(0).

| | int | float | , | ; | id | \$ | Decl | Type | Varlist |
|---|---|---|---|---|---|---|---|---|---|
| 0 | s1 | s2 | | | | | g3 | g4 | |
| 1 | r2 | r2 | r2 | r2 | r2 | r2 | | | |
| 2 | r3 | r3 | r3 | r3 | r3 | r3 | | | |
| 3 | | | | | | a | | | |
| 4 | | | | | s5 | | | | g6 |
| 5 | r5 | r5 | r5 | r5 | r5 | r5 | | | |
| 6 | | | s7 | s8 | | | | | |
| 7 | | | | | s9 | | | | |
| 8 | r1 | r1 | r1 | r1 | r1 | r1 | | | |
| 9 | r4 | r4 | r4 | r4 | r4 | r4 | | | |

#### (b) Simulação para `int x,y,z;`

O analisador lexical entrega `int id , id , id ;` e acrescenta-se o \$.

| Estados | Símbolos | Entrada | Ação |
|:--|:--|--:|:------------|
| 0 | $\varepsilon$ | `int id,id,id;$` | s1 |
| 0 1 | int | `id,id,id;$` | r2: tira 1, topo 0, (0,Type) = g4 |
| 0 4 | Type | `id,id,id;$` | s5 |
| 0 4 5 | Type id | `,id,id;$` | r5: tira 1, topo 4, (4,Varlist) = g6 |
| 0 4 6 | Type Varlist | `,id,id;$` | s7 |
| 0 4 6 7 | Type Varlist , | `id,id;$` | s9 |
| 0 4 6 7 9 | Type Varlist , id | `,id;$` | r4: tira 3, topo 4, (4,Varlist) = g6 |
| 0 4 6 | Type Varlist | `,id;$` | s7 |
| 0 4 6 7 | Type Varlist , | `id;$` | s9 |
| 0 4 6 7 9 | Type Varlist , id | `;$` | r4: tira 3, topo 4, (4,Varlist) = g6 |
| 0 4 6 | Type Varlist | `;$` | s8 |
| 0 4 6 8 | Type Varlist ; | `$` | r1: tira 3, topo 0, (0,Decl) = g3 |
| 0 3 | Decl | `$` | accept |

Repara no padrão da lista: o primeiro `x` vira $Varlist$ com a regra 5,
e cada `, id` seguinte é "colado" à lista com a regra 4. Os *reduce*
lidos de baixo para cima dão a derivação mais à direita:
$Decl \Rightarrow Type\ Varlist\,; \Rightarrow Type\ Varlist,\texttt{z}\,;
\Rightarrow Type\ Varlist,\texttt{y},\texttt{z}\,; \Rightarrow
Type\ \texttt{x},\texttt{y},\texttt{z}\,; \Rightarrow \texttt{int x,y,z;}$

## Aula 5 --- Análise SLR(1)

### Ex. 3 --- SLR(1) (Folha lab. 3, também Exercício 2 dos slides)

$T\to R$, $T\to aTc$, $R\to\varepsilon$, $R\to bR$. Produções numeradas
como na tabela dos slides: (0) $T'\to T\,\$$, (1) $T\to R$, (2) $T\to aTc$,
(3) $R\to\varepsilon$, (4) $R\to bR$.

#### (b) Autómato, tabela SLR(1) e conflitos LR(0)

**1. Autómato.**

**Estado 0** = fecho($\{T'\to\bullet T\,\$\}$). Ponto antes de $T$: entram
$T\to\bullet R$ e $T\to\bullet aTc$. Em $T\to\bullet R$ o ponto está antes
de $R$: entram $R\to\bullet$ e $R\to\bullet bR$.
$0 = \{T'\to\bullet T\,\$,\ T\to\bullet R,\ T\to\bullet aTc,\ R\to\bullet,\ R\to\bullet bR\}$.

- goto(0, `a`) = fecho($\{T\to a\bullet Tc\}$): ponto antes de $T$, entram
  $T\to\bullet R$, $T\to\bullet aTc$, e por causa do primeiro, $R\to\bullet$
  e $R\to\bullet bR$. **Estado 1**.
- goto(0, `b`) = fecho($\{R\to b\bullet R\}$): ponto antes de $R$, entram
  $R\to\bullet$ e $R\to\bullet bR$. **Estado 2**.
- goto(0, $T$) = $\{T'\to T\bullet\$\}$: **estado 3**.
- goto(0, $R$) = $\{T\to R\bullet\}$: **estado 4**.

**Transições de 1:** goto(1, `a`) = fecho($\{T\to a\bullet Tc\}$) = **estado 1**;
goto(1, `b`) = **estado 2**; goto(1, $T$) = $\{T\to aT\bullet c\}$: **estado 5**;
goto(1, $R$) = $\{T\to R\bullet\}$ = **estado 4**.

**Transições de 2:** goto(2, `b`) = fecho($\{R\to b\bullet R\}$) = **estado 2**;
goto(2, $R$) = $\{R\to bR\bullet\}$: **estado 6**.

**Transições de 5:** goto(5, `c`) = $\{T\to aTc\bullet\}$: **estado 7**.
Os estados 3, 4, 6 e 7 não têm mais transições.

![Autómato LR(0) do Exercício 3(b); a rosa, os estados com conflitos LR(0)](figuras/sol_lr0_dfa_TR.svg){width=100%}

**2. Não é LR(0).** Na tabela LR(0), o item completo $R\to\bullet$
(produção 3) dos estados 0, 1 e 2 põe r3 em **todas** as colunas
terminais, incluindo as que já têm *shifts*:

| | a | b | c | \$ | T | R |
|---|---|---|---|---|---|---|
| 0 | **s1, r3** | **s2, r3** | r3 | r3 | g3 | g4 |
| 1 | **s1, r3** | **s2, r3** | r3 | r3 | g5 | g4 |
| 2 | r3 | **s2, r3** | r3 | r3 | | g6 |
| 3 | | | | a | | |
| 4 | r1 | r1 | r1 | r1 | | |
| 5 | | | s7 | | | |
| 6 | r4 | r4 | r4 | r4 | | |
| 7 | r2 | r2 | r2 | r2 | | |

Há **cinco conflitos shift/reduce**: (0,a), (0,b), (1,a), (1,b), (2,b).
Por exemplo, em (0,a) o analisador não sabe se começa um $aTc$ (*shift*)
ou se declara que o $R$ ali é vazio (*reduce*). Logo **não é LR(0)**.

**3. FOLLOW.** Ocorrências de não-terminais nos lados direitos:

- $T'\to\underline{T}\,\$$: $\$ \in$ FOLLOW($T$).
- $T\to a\underline{T}c$: $c \in$ FOLLOW($T$).
- $T\to\underline{R}$: $R$ no fim, junta FOLLOW($T$) a FOLLOW($R$).
- $R\to b\underline{R}$: $R$ no fim, junta FOLLOW($R$) a FOLLOW($R$) (nada).

Primeira passagem: FOLLOW($T$) = $\{\$, c\}$, e FOLLOW($R$) recebe
FOLLOW($T$) = $\{\$, c\}$. Segunda passagem: nada muda.
**FOLLOW($T$) = FOLLOW($R$) = $\{c, \$\}$.**

**4. Tabela SLR(1).** Os *reduce* só vão para as colunas `c` e \$ (o
FOLLOW do lado esquerdo, que aqui é igual para $T$ e $R$):

| | a | b | c | \$ | T | R |
|---|---|---|---|---|---|---|
| 0 | s1 | s2 | r3 | r3 | g3 | g4 |
| 1 | s1 | s2 | r3 | r3 | g5 | g4 |
| 2 | | s2 | r3 | r3 | | g6 |
| 3 | | | | a | | |
| 4 | | | r1 | r1 | | |
| 5 | | | s7 | | | |
| 6 | | | r4 | r4 | | |
| 7 | | | r2 | r2 | | |

**Sem conflitos: a gramática é SLR(1).** Os conflitos desapareceram
porque `a` e `b` não estão em FOLLOW($R$): se o próximo símbolo é `a` ou
`b`, um $R$ vazio nunca estaria certo ali.

**Comparação com a tabela dos slides.** É a mesma tabela com outra
numeração: os estados 1, 2, 3, 4 daqui são os 3, 4, 1, 2 dos slides
(0, 5, 6, 7 coincidem). É esta a "tabela diferente mas sem conflitos"
de que os slides falam.

## Aula 6 --- Ações semânticas

### Ex. A --- Valores semânticos na pilha (inventado)

Gramática: `Exp : Term | Exp '+' Term` e `Term : num | '(' Exp ')'`.

#### (a) Tabela pilha / entrada / ação / valor para `2+(3+4)`, com as ações do interpretador

Ações: `Exp : Term { $1 }`, `Exp : Exp '+' Term { $1 + $3 }`,
`Term : num { $1 }`, `Term : '(' Exp ')' { $2 }`.

| \# | Pilha | Entrada | Ação | Valor calculado |
|:-:|:--------------|--:|:------------|:------------|
| 1 | | `2+(3+4)` | shift `num` | valor do *token*: 2 |
| 2 | `num:2` | `+(3+4)` | reduce `Term : num` | `$1` = 2 |
| 3 | `Term:2` | `+(3+4)` | reduce `Exp : Term` | `$1` = 2 |
| 4 | `Exp:2` | `+(3+4)` | shift `'+'` | |
| 5 | `Exp:2` `+` | `(3+4)` | shift `'('` | |
| 6 | `Exp:2` `+` `(` | `3+4)` | shift `num` | valor do *token*: 3 |
| 7 | `Exp:2` `+` `(` `num:3` | `+4)` | reduce `Term : num` | `$1` = 3 |
| 8 | `Exp:2` `+` `(` `Term:3` | `+4)` | reduce `Exp : Term` | `$1` = 3 |
| 9 | `Exp:2` `+` `(` `Exp:3` | `+4)` | shift `'+'` | |
| 10 | `Exp:2` `+` `(` `Exp:3` `+` | `4)` | shift `num` | valor do *token*: 4 |
| 11 | `Exp:2` `+` `(` `Exp:3` `+` `num:4` | `)` | reduce `Term : num` | `$1` = 4 |
| 12 | `Exp:2` `+` `(` `Exp:3` `+` `Term:4` | `)` | reduce `Exp : Exp '+' Term` | `$1+$3` = 3+4 = 7 |
| 13 | `Exp:2` `+` `(` `Exp:7` | `)` | shift `')'` | |
| 14 | `Exp:2` `+` `(` `Exp:7` `)` | | reduce `Term : '(' Exp ')'` | `$2` = 7 |
| 15 | `Exp:2` `+` `Term:7` | | reduce `Exp : Exp '+' Term` | `$1+$3` = 2+7 = 9 |
| 16 | `Exp:9` | | accept | resultado: **9** |

Quem são `$1`, `$2`, `$3` em cada *reduce* de três símbolos:

- **Passo 12**: o *reduce* só olha para os **três símbolos do topo**:
  `$1` = `Exp:3`, `$2` = `+`, `$3` = `Term:4`. O `Exp:2 + (` que está
  mais abaixo não é tocado.
- **Passo 14**: `$1` = `(`, `$2` = `Exp:7`, `$3` = `)`. A ação é `$2`.
- **Passo 15**: `$1` = `Exp:2`, `$2` = `+`, `$3` = `Term:7`.

Repara que no passo 4 (pilha `Exp:2`, próximo `+`) o analisador **não**
espera: o `2` já foi reduzido até `Exp` nos passos 2 e 3. Em contraste, no
passo 12 a soma `3+4` só é fechada quando aparece o `)`. Isto é o que faz
os parêntesis agruparem: a soma de dentro é reduzida **antes** da de fora.

#### (b) Valor de `parser` com as ações que constroem a árvore

Ações: `{ $1 }`, `{ Add $1 $3 }`, `{ Num $1 }`, `{ $2 }`. Os
*shift*/*reduce* são os mesmos da alínea (a); mudam só os valores:

- passos 2 e 3: `Num 2`;
- passos 7 e 8: `Num 3`;
- passo 11: `Num 4`;
- passo 12: `Add (Num 3) (Num 4)`;
- passo 14: `Add (Num 3) (Num 4)` (os parêntesis não criam nó);
- passo 15: `Add (Num 2) (Add (Num 3) (Num 4))`.

**Resultado: `Add (Num 2) (Add (Num 3) (Num 4))`.**

Comparação: `(1+2)+3` deu `Add (Add (Num 1) (Num 2)) (Num 3)`, com a soma
aninhada no filho **esquerdo**; aqui a soma aninhada está no filho
**direito**. Os parêntesis desaparecem da AST, mas o agrupamento que
impuseram fica na forma da árvore.

## Aula 6 --- Conflitos, associatividade e precedência

### Ex. B --- Precedências no papel (inventado)

Gramática ambígua `Exp : num | Exp '+' Exp | Exp '-' Exp | Exp '*' Exp
| Exp '<' Exp`. Regra a aplicar em cada conflito: a regra $R$ a reduzir
tem a precedência do seu último terminal (o operador); compara-se com a
do *token* da entrada. Maior → *shift*; menor → *reduce*; igual →
`%left` *reduce*, `%right` *shift*, `%nonassoc` erro.

(Confirmado com o Happy: geradas as gramáticas com estas declarações e
corridas as entradas.)

#### (a) `8-4-2` com `%right '-'`

1. Lê `8`, reduz a `Exp`; *shift* `-`; lê `4`, reduz a `Exp`. Pilha:
   `Exp - Exp`. Próximo: `-`.
2. Conflito: reduzir `Exp - Exp` (precedência do `-`) ou *shift* do `-`
   (precedência do `-`). **Mesma precedência** → associatividade.
   `%right` → ***shift***.
3. Pilha `Exp - Exp -`; lê `2`, reduz a `Exp`. Pilha: `Exp - Exp - Exp`,
   fim da entrada → só se pode reduzir. Reduz o `Exp - Exp` do topo:
   $4-2 = 2$. Pilha `Exp - Exp` (8 e 2). Reduz: $8-2 = 6$.

**Árvore: $8-(4-2)$. Valor: 6.** (Com `%left` seria $(8-4)-2 = 2$, que
é a convenção algébrica; por isso o lab pede `%left`.)

#### (b) `1+2*3` com `%nonassoc '<'`, `%left '*'`, `%left '+' '-'` (por esta ordem)

A ordem das linhas dá as precedências: `<` a mais baixa, depois `*`,
e **`+` e `-` a mais alta**. É a ordem ao contrário da habitual.

1. Lê `1`, reduz; *shift* `+`; lê `2`, reduz. Pilha: `Exp + Exp`.
   Próximo: `*`.
2. Conflito: reduzir `Exp + Exp` (precedência do `+`, a mais alta) ou
   *shift* do `*` (precedência menor). O *token* tem **menos**
   precedência do que a regra → ***reduce***: $1+2 = 3$.
3. Pilha `Exp` (3); *shift* `*`; lê `3`, reduz; fim da entrada → reduz
   `Exp * Exp`: $3 \times 3 = 9$.

**Árvore: $(1+2)\times3$. Valor: 9** (e não 7). É o erro de pôr as
declarações pela ordem errada: a última linha é a que "agarra" primeiro.

#### (c) `1<2+3` e `1<2<3`, com as declarações da (b)

**`1<2+3`.**

1. Lê `1`, reduz; *shift* `<`; lê `2`, reduz. Pilha: `Exp < Exp`.
   Próximo: `+`.
2. Conflito: reduzir `Exp < Exp` (precedência do `<`, a mais baixa) ou
   *shift* do `+` (mais alta). O *token* tem **mais** precedência →
   ***shift***.
3. Lê `3`, reduz. Pilha `Exp < Exp + Exp`, fim da entrada: reduz
   $2+3 = 5$, depois `Exp < Exp`: $1 < 5$ é verdadeiro.

**Árvore: $1 < (2+3)$. Valor: 1.** É o que se quer: os operadores
aritméticos ligam mais do que as comparações.

**`1<2<3`.**

1. Pilha `Exp < Exp` (1 e 2), próximo `<`.
2. Conflito: regra com a precedência do `<`, *token* `<`: **mesma
   precedência**, e o `<` é `%nonassoc` → **erro sintático**.

**`1<2<3` é rejeitado.** (Com o Happy 2.2 o erro aparece como `Internal
Happy parser panic` em vez de chamar a `parseError`; o Bison diz `syntax
error`.)

## Aula 6 --- Calculadora com geradores

### 1 --- Calculadora (Folha lab. 4, `Praticas/Semana_3/Parsing`)

Gramática ambígua $E \to E{+}E \mid E{-}E \mid E{*}E \mid E/E \mid (E)
\mid \texttt{num}$. As duas versões abaixo (C e Haskell) foram compiladas
e passam os 5 testes de `testsC`/`testsHaskell`.

#### (a) Calculadora com as quatro operações, precedência e associatividade

**Ideia.** Dois níveis de precedência, ambos à esquerda:

```
%left '+' '-'        -- precedência mais baixa
%left '*' '/'        -- precedência mais alta
```

Verificação contra os exemplos do enunciado, com a regra da Aula 6:

- `1+2*3`: pilha `E + E`, próximo `*`; o `*` tem mais precedência do que
  a regra do `+` → *shift* → $1+(2\times3) = 7$.
- `1+2/3`: igual, com `/` na linha do `*` → $1+(2/3) \approx 1.667$.
- `1-2-3`: pilha `E - E`, próximo `-`; mesma precedência, `%left` →
  *reduce* → $(1-2)-3 = -4$.
- `1/2/3`: igual com `/` → $(1/2)/3 \approx 0.167$.

**Versão C (Flex + Bison).** `lexer.x`:

```
%{
#include <stdlib.h>
#include "parser.tab.h"
void yyerror(char const *);
%}
%option noyywrap

digit   [0-9]

%%

[ \t\r\n]+               ;  /* ignorar brancos */
{digit}+("."{digit}+)?   { yylval = atof(yytext); return NUM; }
[-+*/()]                 { return yytext[0]; }
.                        { yyerror("caracter invalido"); }
```

- O `num` aceita inteiros e decimais (`1.5`). `yylval` é `float`
  (porque o `parser.y` diz `%define api.value.type {float}`), e o
  `atof` converte o texto.
- Os operadores e parêntesis são devolvidos pelo próprio código do
  carácter (`yytext[0]`), que é o que o Bison espera para `'+'`, `'('`,
  etc. Dentro de `[...]` o `-` vem **primeiro** para não ser lido como
  intervalo.
- O `\n` também é ignorado: os testes têm linhas em branco no fim.

`parser.y` (só as partes a completar; o resto é o fornecido):

```
%token NUM
%left '+' '-'
%left '*' '/'

%%

top : expr                    { printf("%f\n", $1); }
    ;

expr : expr '+' expr          { $$ = $1 + $3; }
     | expr '-' expr          { $$ = $1 - $3; }
     | expr '*' expr          { $$ = $1 * $3; }
     | expr '/' expr          { $$ = $1 / $3; }
     | '(' expr ')'           { $$ = $2; }
     | NUM                    { $$ = $1; }
     ;
```

Compilar e testar (com o Bison 3: o do macOS é o 2.3 e não aceita
`%define api.value.type`; `brew install bison`):

```
export PATH=/opt/homebrew/opt/bison/bin:$PATH
make
for i in 1 2 3 4; do ./calc < ../testsC/input$i.txt | diff - ../testsC/output$i.txt; done
```

**Versão Haskell (Alex + Happy).** `Lexer.x`:

```
{
module Lexer where
}
%wrapper "basic"

$digit = [0-9]

tokens :-

$white+                    ;
$digit+ ("." $digit+)?     { \s -> TOK_NUM (read s) }
"+"                        { \_ -> TOK_PLUS }
"-"                        { \_ -> TOK_MINUS }
"*"                        { \_ -> TOK_TIMES }
"/"                        { \_ -> TOK_DIV }
"("                        { \_ -> TOK_LPAREN }
")"                        { \_ -> TOK_RPAREN }

{
data Token = TOK_NUM Float
           | TOK_PLUS | TOK_MINUS | TOK_TIMES | TOK_DIV
           | TOK_LPAREN | TOK_RPAREN
           deriving (Eq, Show)
}
```

`read s :: Float` aceita tanto `"1"` como `"1.5"`.

`Parser.y` (partes a completar):

```
%token

num      { TOK_NUM $$ }
'+'      { TOK_PLUS }
'-'      { TOK_MINUS }
'*'      { TOK_TIMES }
'/'      { TOK_DIV }
'('      { TOK_LPAREN }
')'      { TOK_RPAREN }

%left '+' '-'
%left '*' '/'

%%

Exp : Exp '+' Exp          { $1 + $3 }
    | Exp '-' Exp          { $1 - $3 }
    | Exp '*' Exp          { $1 * $3 }
    | Exp '/' Exp          { $1 / $3 }
    | '(' Exp ')'          { $2 }
    | num                  { $1 }
```

Compilar e testar:

```
alex Lexer.x && happy --ghc -i Parser.y && ghc -o calc Main.hs Lexer.hs Parser.hs
./calc < ../testsHaskell/input1.txt          # 7.0
```

Com o `-i`, o `Parser.info` deve dizer que **não há conflitos**. Se
retirares as linhas `%left`, aparecem 16 conflitos *shift/reduce* (4
operadores × 4 operadores, em 4 estados).

#### (b) Funções `sqrt`, `exp` e `log`

**Léxico:** três *tokens* novos para as palavras. Não há identificadores
nesta linguagem, por isso não há conflito com nenhuma outra regra, e a
ordem só importaria se mais tarde se acrescentasse um `ID` (aí as
palavras teriam de vir antes, *first match*).

**Sintaxe:** $E \to F(E)$ com $F \to$ `sqrt` | `exp` | `log`. É mais
simples pôr uma produção por função do que um não-terminal $F$, porque
cada uma tem uma ação diferente. Estas produções **não criam conflitos**:
começam por um *token* que nenhuma outra produção usa, e acabam em `)`.

**Versão C.** No `lexer.x`, **antes** da regra dos números:

```
"sqrt"                   { return SQRT; }
"exp"                    { return EXP; }
"log"                    { return LOG; }
```

No `parser.y`: `%token NUM SQRT EXP LOG` e mais três alternativas de
`expr`:

```
     | SQRT '(' expr ')'      { $$ = sqrtf($3); }
     | EXP  '(' expr ')'      { $$ = expf($3); }
     | LOG  '(' expr ')'      { $$ = logf($3); }
```

`$3` é o valor do `expr` dentro dos parêntesis (`$1` é o nome da função,
`$2` o `(`). `sqrtf`/`expf`/`logf` são as versões `float` de `<math.h>`.

**Versão Haskell.** No `Lexer.x`:

```
sqrt                       { \_ -> TOK_SQRT }
exp                        { \_ -> TOK_EXP }
log                        { \_ -> TOK_LOG }
```

e `| TOK_SQRT | TOK_EXP | TOK_LOG` no `data Token`. No `Parser.y`:

```
sqrt     { TOK_SQRT }
exp      { TOK_EXP }
log      { TOK_LOG }
```

em `%token`, e na gramática:

```
    | sqrt '(' Exp ')'     { sqrt $3 }
    | exp '(' Exp ')'      { exp $3 }
    | log '(' Exp ')'      { log $3 }
```

(Os nomes dos terminais do Happy, `sqrt`/`exp`/`log`, não colidem com as
funções Haskell `sqrt`/`exp`/`log` das ações: os primeiros só existem na
gramática.)

**Teste 5:** `sqrt(2)+log(1)+exp(0)` → $1.4142135 + 0 + 1$ →
`2.414214` em C e `2.4142137` em Haskell (o `print` de um `Float` mostra
todos os dígitos significativos; o `%f` do C arredonda a 6 casas).

## Aula 6 --- Representar sintaxe abstrata

### ASTs 2 --- Operadores `-`, `*`, `/`, `%` e `printExpr` (lab. ASTs, `Praticas/Semana_4`)

Tudo foi compilado com o Bison 3.8 e corrido com os `example*.txt`. Começa por
definir o `root` em falta: `Expr* root = NULL;` depois do segundo `%%`
do `parser.bison`.

#### Resposta

**`scanner.flex`**: um *token* por operador, a seguir ao `"+"`:

```c
"-" { return MINUS; }
"*" { return TIMES; }
"/" { return DIV; }
"%" { return MOD; }
```

**`parser.bison`**: os *tokens* novos, a precedência e as regras. Cada
`%left` declarado mais abaixo tem precedência maior, por isso `*`, `/`
e `%` ficam acima de `+` e `-`, e todos são associativos à esquerda:

```
%token INT PLUS MINUS TIMES DIV MOD
%left PLUS MINUS
%left TIMES DIV MOD
...
expr:
    INT              { $$ = ast_integer($1); }
  | expr PLUS expr   { $$ = ast_operation(PLUS, $1, $3); }
  | expr MINUS expr  { $$ = ast_operation(MINUS, $1, $3); }
  | expr TIMES expr  { $$ = ast_operation(TIMES, $1, $3); }
  | expr DIV expr    { $$ = ast_operation(DIV, $1, $3); }
  | expr MOD expr    { $$ = ast_operation(MOD, $1, $3); }
  ;
%%
Expr* root = NULL;
```

**`interpreter.c`**: no `switch` do `eval`, em vez do `TODO`:

```c
      case MINUS: result = vLeft - vRight; break;
      case TIMES: result = vLeft * vRight; break;
      case DIV:   result = vLeft / vRight; break;
      case MOD:   result = vLeft % vRight; break;
```

**`printAbsTree.c`** (novo) e um `printAbsTree.h` com o protótipo
`void printExpr(Expr* exp);`. A árvore imprime-se em pré-ordem, com dois
espaços de indentação por nível:

```c
#include <stdio.h>
#include "parser.h"        // PLUS, MINUS, ... e ast.h
#include "printAbsTree.h"

static void printExprAt(Expr* e, int depth) {
  for (int i = 0; i < depth; i++) printf("  ");
  if (e->kind == E_INTEGER) {
    printf("INT %d\n", e->attr.value);
  } else {
    switch (e->attr.op.operator) {
      case PLUS:  printf("OP +\n"); break;
      case MINUS: printf("OP -\n"); break;
      case TIMES: printf("OP *\n"); break;
      case DIV:   printf("OP /\n"); break;
      case MOD:   printf("OP %%\n"); break;
    }
    printExprAt(e->attr.op.left, depth + 1);
    printExprAt(e->attr.op.right, depth + 1);
  }
}

void printExpr(Expr* exp) { printExprAt(exp, 0); }
```

No `main`, `printExpr(root);` antes do `printf("Result = ...")`, e no
`Makefile`, `OBJS=scanner.o parser.o ast.o printAbsTree.o interpreter.o`.

**Saída real para `example3.txt`** (`900 + 3 * 32 + 2 % 5 + 4 / 2 - 1`):

```
OP -
  OP +
    OP +
      OP +
        INT 900
        OP *
          INT 3
          INT 32
      OP %
        INT 2
        INT 5
    OP /
      INT 4
      INT 2
  INT 1
Result = 999
```

Conta: $3\cdot32 = 96$, $2 \bmod 5 = 2$ e $4/2 = 2$. Depois, da esquerda para
a direita, $900+96 = 996$, $996+2 = 998$, $998+2 = 1000$ e $1000-1 = 999$.

**`4-1` sem espaços** dá `Line 1: syntax error - '-1'`. Depois do `4`,
o Flex tenta as regras em `-1`. A `\-?[0-9]+` apanha 2 caracteres e a `"-"`
só 1, e ganha o *longest match*. Os *tokens* ficam `INT(4) INT(-1)`, e
nenhuma regra aceita dois `INT` seguidos. Com espaços, `4 - -1` dá 5. A
correção habitual é tirar o `\-?` ao `INT` e tratar o menos unário na
gramática.

O `example4.txt` (três expressões seguidas) dá erro de sintaxe na linha
4, porque o `program` só aceita **uma** expressão.

### ASTs 3 --- Expressões booleanas e `printBool` (lab. ASTs)

#### Resposta

**`ast.h`**: um tipo novo, com a mesma estrutura de *tag* e `union`:

```c
struct _BoolExpr {
  enum { B_CONST, B_RELOP } kind;   // 0/1  ou  expr <relop> expr
  union {
    int value;
    struct { int operator; Expr* left; Expr* right; } relop;
  } attr;
};
typedef struct _BoolExpr BoolExpr;

BoolExpr* ast_bool_const(int v);
BoolExpr* ast_relop(int operator, Expr* left, Expr* right);
```

**`ast.c`**:

```c
BoolExpr* ast_bool_const(int v) {
  BoolExpr* node = (BoolExpr*) malloc(sizeof(BoolExpr));
  node->kind = B_CONST;
  node->attr.value = v;
  return node;
}

BoolExpr* ast_relop(int operator, Expr* left, Expr* right) {
  BoolExpr* node = (BoolExpr*) malloc(sizeof(BoolExpr));
  node->kind = B_RELOP;
  node->attr.relop.operator = operator;
  node->attr.relop.left = left;
  node->attr.relop.right = right;
  return node;
}
```

**`scanner.flex`**: os operadores de dois caracteres. O *longest match* já
faz `<=` ganhar a `<` em qualquer ordem, mas pô-los primeiro deixa isso
claro:

```c
"==" { return EQ; }
"!=" { return NE; }
"<=" { return LE; }
">=" { return GE; }
"<"  { return LT; }
">"  { return GT; }
```

**`parser.bison`**: os *tokens* `EQ NE LT GT LE GE`, um campo novo no
`%union` e as regras:

```
%union { int intValue; Expr* exprValue; BoolExpr* boolValue; }
%type <boolValue> bexpr
...
bexpr:
    INT            { $$ = ast_bool_const($1); }
  | expr EQ expr   { $$ = ast_relop(EQ, $1, $3); }
  | expr NE expr   { $$ = ast_relop(NE, $1, $3); }
  | expr LT expr   { $$ = ast_relop(LT, $1, $3); }
  | expr GT expr   { $$ = ast_relop(GT, $1, $3); }
  | expr LE expr   { $$ = ast_relop(LE, $1, $3); }
  | expr GE expr   { $$ = ast_relop(GE, $1, $3); }
  ;
```

Os relacionais **não precisam de `%left`**, porque o `bexpr` não é
recursivo: `1 + 2 < 3` só pode ser `(1+2) < 3`, já que nenhuma regra de
`expr` aceita um `LT` a seguir. O `INT` de `bexpr` e o de `expr` também
não chocam. Depois de `INT`, se o *lookahead* for um relacional ou
aritmético reduz-se a `expr`, e se for o que vem depois de uma condição
(`then`, `{`, ...) reduz-se a `bexpr`. O Bison 3.8 não reporta conflitos.

**`printAbsTree.c`**: o mesmo esquema do `printExpr`, com um nível a mais.
O `indent(depth)` é o ciclo de espaços do `printExprAt`, e o `opName`
devolve o texto de cada operador (`EQ` → `"=="`, etc.):

```c
static void printBoolAt(BoolExpr* b, int depth) {
  indent(depth);
  switch (b->kind) {
    case B_CONST: printf("BOOL %d\n", b->attr.value); break;
    case B_RELOP:
      printf("RELOP %s\n", opName(b->attr.relop.operator));
      printExprAt(b->attr.relop.left, depth + 1);
      printExprAt(b->attr.relop.right, depth + 1);
      break;
  }
}
void printBool(BoolExpr* b) { printBoolAt(b, 0); }
```

Para testar sozinho, basta pôr `program: bexpr` e `BoolExpr* root`. No Ex. 4
a raiz passa a ser um comando, e as condições aparecem dentro do
`if`/`while` (ver a saída abaixo).

### ASTs 4 --- Comandos e `printCmd` (lab. ASTs)

#### Resposta

**Variáveis** †: uma atribuição `x = ...` precisa de um *token* `ID` e
de variáveis nas expressões (senão `x = x - 1` não se escreve). Por isso
o `Expr` ganha a alternativa `E_VAR` (`char* var`, construtor
`ast_var`), e há a regra `expr: ID { $$ = ast_var($1); }`.

**`ast.h`**:

```c
struct _Cmd {
  enum { C_ASSIGN, C_IF, C_WHILE, C_SEQ } kind;
  union {
    struct { char* var; Expr* expr; } assign;
    struct { BoolExpr* cond; struct _Cmd* thenCmd;
             struct _Cmd* elseCmd; } ifCmd;      // elseCmd == NULL: sem else
    struct { BoolExpr* cond; struct _Cmd* body; } whileCmd;
    struct { struct _Cmd* fst; struct _Cmd* snd; } seq;
  } attr;
};
typedef struct _Cmd Cmd;

Cmd* ast_assign(char* var, Expr* expr);
Cmd* ast_if(BoolExpr* cond, Cmd* thenCmd, Cmd* elseCmd);
Cmd* ast_while(BoolExpr* cond, Cmd* body);
Cmd* ast_seq(Cmd* fst, Cmd* snd);
```

**`ast.c`**: os construtores seguem o padrão de sempre, como este:

```c
Cmd* ast_if(BoolExpr* cond, Cmd* thenCmd, Cmd* elseCmd) {
  Cmd* node = (Cmd*) malloc(sizeof(Cmd));
  node->kind = C_IF;
  node->attr.ifCmd.cond = cond;
  node->attr.ifCmd.thenCmd = thenCmd;
  node->attr.ifCmd.elseCmd = elseCmd;
  return node;
}
```

(`ast_assign`, `ast_while` e `ast_seq` são iguais, cada um com os seus
campos.)

**`scanner.flex`**: as palavras reservadas vêm **antes** do `ID`. Em
empate de comprimento ganha a primeira regra (*first match*), por isso
`if` dá `IF` e não `ID`. O nome **copia-se logo aqui**:

```c
"="     { return ASSIGN; }
";"     { return SEMI; }
"{"     { return LBRACE; }
"}"     { return RBRACE; }
"if"    { return IF; }
"then"  { return THEN; }
"else"  { return ELSE; }
"while" { return WHILE; }
[a-zA-Z_][a-zA-Z0-9_]* { yylval.strValue = strdup(yytext); return ID; }
```

Sem o `strdup` (com `yylval.strValue = yytext`), a primeira versão
imprimiu `ASSIGN x = 10;` em vez de `ASSIGN x`. Quando se reduz
`ID ASSIGN expr`, o Flex já leu a expressão toda, e o ponteiro guardado
aponta para o *buffer* sem o `\0` no sítio.

**`parser.bison`**:

```
%token INT ID PLUS MINUS TIMES DIV MOD EQ NE LT GT LE GE
%token ASSIGN SEMI LBRACE RBRACE IF THEN ELSE WHILE

%left SEMI              // precedência mais baixa
%nonassoc THEN WHILE
%nonassoc ELSE
%left PLUS MINUS
%left TIMES DIV MOD

%union { int intValue; char* strValue; Expr* exprValue;
         BoolExpr* boolValue; Cmd* cmdValue; }
%type <strValue> ID
%type <cmdValue> cmd
... (extern Cmd* root; no %code requires)
%%
program: cmd { root = $1; }

cmd:
    ID ASSIGN expr                { $$ = ast_assign($1, $3); }
  | IF bexpr THEN cmd             { $$ = ast_if($2, $4, NULL); }
  | IF bexpr THEN cmd ELSE cmd    { $$ = ast_if($2, $4, $6); }
  | WHILE bexpr cmd               { $$ = ast_while($2, $3); }
  | cmd SEMI cmd                  { $$ = ast_seq($1, $3); }
  | LBRACE cmd RBRACE             { $$ = $2; }
  ;
... (bexpr do Ex. 3; expr do Ex. 2 mais  | ID { $$ = ast_var($1); })
%%
Cmd* root = NULL;
```

As precedências resolvem os três conflitos que a gramática tem:

- **`c1 ; c2 ; c3`**: `%left SEMI` agrupa como `(c1 ; c2) ; c3`.
- **`if b then x = 1 ; y = 2`**: com a pilha `IF bexpr THEN cmd` e o
  *lookahead* `;`, a regra (com a precedência de `THEN`) é **maior** do
  que `SEMI`, por isso reduz-se. Fica `(if b then x = 1) ; y = 2`, como em
  C. O `while b c1 ; c2` funciona da mesma forma (por isso `WHILE` também
  leva precedência).
- **`else` pendente**: com `IF bexpr THEN cmd` e *lookahead* `ELSE`, o
  `ELSE` é maior do que `THEN`, por isso faz-se *shift*. O `else` fica no
  `if` mais interior, como em C.

O Bison 3.8 compila esta gramática **sem conflitos**.

**`printAbsTree.c`**:

```c
static void printCmdAt(Cmd* c, int depth) {
  indent(depth);
  switch (c->kind) {
    case C_ASSIGN:
      printf("ASSIGN %s\n", c->attr.assign.var);
      printExprAt(c->attr.assign.expr, depth + 1);
      break;
    case C_IF:
      printf(c->attr.ifCmd.elseCmd ? "IF-ELSE\n" : "IF\n");
      printBoolAt(c->attr.ifCmd.cond, depth + 1);
      printCmdAt(c->attr.ifCmd.thenCmd, depth + 1);
      if (c->attr.ifCmd.elseCmd) printCmdAt(c->attr.ifCmd.elseCmd, depth + 1);
      break;
    case C_WHILE:
      printf("WHILE\n");
      printBoolAt(c->attr.whileCmd.cond, depth + 1);
      printCmdAt(c->attr.whileCmd.body, depth + 1);
      break;
    case C_SEQ:
      printf("SEQ\n");
      printCmdAt(c->attr.seq.fst, depth + 1);
      printCmdAt(c->attr.seq.snd, depth + 1);
      break;
  }
}
void printCmd(Cmd* command) { printCmdAt(command, 0); }
```

O `main` passa a chamar `printCmd(root)`. O `eval` de expressões já não
chega, porque as variáveis precisam de um ambiente.

**Saída real** para `if 1 then if x < 2 then y = 1 else y = 2`. O `else`
fica no `if` de dentro:

```
IF
  BOOL 1
  IF-ELSE
    RELOP <
      VAR x
      INT 2
    ASSIGN y
      INT 1
    ASSIGN y
      INT 2
```

### Ex. C --- AST de `x = 1; y = x * (2 + 3); x++` (inventado)

Agrupando à direita: `CompoundStm (x = 1) (CompoundStm (y = ...) (x++))`.
A expressão `x * (2 + 3)` é um `OpExp` com `Times`, cujo filho direito é
outro `OpExp` com `Plus` (os parêntesis não aparecem na AST).

#### (a) Valor Haskell

```haskell
prog :: Stm
prog =
  CompoundStm
    (AssignStm "x" (NumExp 1))
    (CompoundStm
       (AssignStm "y"
          (OpExp (IdExp "x")
                 Times
                 (OpExp (NumExp 2) Plus (NumExp 3))))
       (IncrStm "x"))
```

#### (b) Em C, com os construtores `mk_...`

Os três construtores que faltam seguem o padrão de `mk_op`: reservar a
estrutura, pôr a *tag*, preencher os campos **da alternativa certa** da
`union`, e clonar as cadeias (como em `mk_ident`):

```c
static char *clone(char *txt) {
  char *str = malloc(strlen(txt) + 1);
  strcpy(str, txt);
  return str;
}

Stm mk_assign(char *txt, Exp e) {
  Stm s = (Stm) malloc(sizeof(struct _stm));
  s->tag = ASSIGN;
  s->assign.ident = clone(txt);
  s->assign.expr = e;
  return s;
}

Stm mk_incr(char *txt) {
  Stm s = (Stm) malloc(sizeof(struct _stm));
  s->tag = INCR;
  s->ident = clone(txt);          // INCR: só um atributo
  return s;
}

Stm mk_compound(Stm s1, Stm s2) {
  Stm s = (Stm) malloc(sizeof(struct _stm));
  s->tag = COMPOUND;
  s->compound.fst = s1;
  s->compound.snd = s2;
  return s;
}
```

O programa:

```c
Stm prog =
  mk_compound(mk_assign("x", mk_num(1)),
    mk_compound(mk_assign("y", mk_op(TIMES, mk_ident("x"),
                                     mk_op(PLUS, mk_num(2), mk_num(3)))),
                mk_incr("x")));
```

Verificado: compilado com `gcc -Wall -std=c11`, e uma função que imprime
a AST percorrendo-a com `switch` na *tag* mostra
`{x = 1; {y = (x * (2 + 3)); x++}}`.

### Ex. D --- Interpretador para programas sequenciais (inventado)

#### Resposta

```haskell
type Env = [(String, Int)]

evalExp :: Env -> Exp -> Int
evalExp env (IdExp x) = case lookup x env of
  Just v  -> v
  Nothing -> error ("variavel nao definida: " ++ x)
evalExp _   (NumExp n) = n
evalExp env (OpExp e1 op e2) =
  let v1 = evalExp env e1
      v2 = evalExp env e2
  in case op of
       Plus  -> v1 + v2
       Minus -> v1 - v2
       Times -> v1 * v2
       Div   -> v1 `div` v2

-- substitui (ou acrescenta) o valor de x
update :: String -> Int -> Env -> Env
update x v env = (x, v) : filter ((/= x) . fst) env

exec :: Env -> Stm -> Env
exec env (AssignStm x e)     = update x (evalExp env e) env
exec env (IncrStm x)         = update x (evalExp env (IdExp x) + 1) env
exec env (CompoundStm s1 s2) = exec (exec env s1) s2
```

- Um caso por construtor, como no `process` dos slides.
- `CompoundStm s1 s2`: executa `s1` e usa o **ambiente que resulta** para
  executar `s2` (é isso que faz a sequência `;`).
- `IncrStm x` é açúcar sintático para `x = x + 1`: reaproveita o
  `evalExp`.

**Execução com o programa do Ex. C**, `exec [] prog`, passo a passo:

1. `CompoundStm (x = 1) resto`: executa primeiro `x = 1`.
   `evalExp [] (NumExp 1)` = 1. Ambiente: `[("x",1)]`.
2. Executa o `resto` = `CompoundStm (y = ...) (x++)` com `[("x",1)]`.
   Primeiro `y = x * (2 + 3)`: `evalExp` de `OpExp (IdExp "x") Times (...)`
   calcula $v_1$ = valor de `x` = 1 e $v_2$ = `evalExp` de
   `OpExp (NumExp 2) Plus (NumExp 3)` = $2+3 = 5$; `Times` → $1\times5 = 5$.
   Ambiente: `[("y",5),("x",1)]`.
3. `x++`: valor de `x` = 1, mais 1 = 2. `update` tira o `("x",1)` antigo
   e põe `("x",2)`. Ambiente: `[("x",2),("y",5)]`.

**Resultado: `[("x",2),("y",5)]`**, ou seja $x = 2$, $y = 5$ (corrido
com `runghc`). O exemplo dos slides (`a = 5+3; b = a-2`) dá
`[("b",6),("a",8)]`.

## Aula 7 --- Descida recursiva

### Ex. E --- Traçar o analisador Haskell (inventado)

#### (a) `accepted` em `if 1=1 then print 2=3 else begin print 4=4 end`

*Tokens*: `[IF, NUM, EQUAL, NUM, THEN, PRINT, NUM, EQUAL, NUM, ELSE, BEGIN, PRINT, NUM, EQUAL, NUM, END]`.

1. `parseS` vê `IF`: $S\to\texttt{if}\,E\,\texttt{then}\,S\,\texttt{else}\,S$;
   `toks` = `[NUM, EQUAL, NUM, THEN, PRINT, ...]`.
2. `toks1 = parseE toks`: consome `NUM`, `EQUAL`, `NUM`; devolve
   `[THEN, PRINT, NUM, EQUAL, NUM, ELSE, BEGIN, PRINT, NUM, EQUAL, NUM, END]`.
3. `toks2 = consume THEN toks1` = `[PRINT, NUM, EQUAL, NUM, ELSE, BEGIN, PRINT, NUM, EQUAL, NUM, END]`.
4. `toks3 = parseS toks2`: vê `PRINT`, $S\to\texttt{print}\,E$;
   `parseE [NUM, EQUAL, NUM, ELSE, ...]` devolve
   `[ELSE, BEGIN, PRINT, NUM, EQUAL, NUM, END]`.
5. `toks4 = consume ELSE toks3` = `[BEGIN, PRINT, NUM, EQUAL, NUM, END]`.
6. `parseS toks4`: vê `BEGIN`, $S\to\texttt{begin}\,S\,L$;
   `parseS [PRINT, NUM, EQUAL, NUM, END]` vê `PRINT` e o `parseE`
   devolve `[END]`.
7. `parseL [END]`: vê `END`, $L\to\texttt{end}$, devolve `[]`.

O `parseS` inicial devolve `[]`, por isso `accepted` = `null []` = `True`
(saída real do `runghc`: `True`).

#### (b) Onde falha `begin print 1=1 print 2=2 end`

`parseS` vê `BEGIN` e chama `parseS [PRINT, NUM, EQUAL, NUM, PRINT, ...]`,
que consome `print 1=1` e devolve `[PRINT, NUM, EQUAL, NUM, END]`. Esta
lista vai para `parseL`, que só tem casos para `END` ($L\to\texttt{end}$)
e `SEMI` ($L\to\texttt{;}\,S\,L$): o `PRINT` cai no `_` e dá
`error "syntax error"`. Falta o `;` entre as duas instruções. Saída real:
`Desc.hs: syntax error`.

#### (c) `parseS` e `accepted` em `print 1=1 end`

`parseS [PRINT, NUM, EQUAL, NUM, END]` vê `PRINT`, o `parseE` consome
`NUM EQUAL NUM` e devolve **`[END]`**: o `parseS` não dá erro, porque só
reconhece um prefixo. `accepted` = `null [END]` = **`False`**: sobra um
*token*. É para isto que serve o marcador do final.

### Ex. F --- Descida recursiva em C completa (inventado)

#### Resposta

O `getToken` simula o *lexer* lendo de um *array*; `EOF` passa a `EOF_`
(o `stdio.h` define `EOF` como macro).

```c
#include <stdio.h>
#include <stdlib.h>
typedef enum { IF, THEN, ELSE, BEGIN, END, PRINT, SEMI, NUM, EQUAL, EOF_ } Token;
static const char *nome[] = {"IF","THEN","ELSE","BEGIN","END","PRINT","SEMI","NUM","EQUAL","EOF"};

static Token *input; static int pos;
Token getToken(void) { return input[pos++]; }   /* simula o lexer */

Token next;
void advance(void) { next = getToken(); }
void error(const char *msg) { printf("erro: %s (token %s)\n", msg, nome[next]); exit(1); }
void consume(Token t) { if (next == t) advance(); else error("token inesperado"); }

void parse_S(void); void parse_L(void); void parse_E(void);
/* parse_S, parse_E e parse_L exatamente como no resumo */

void accepted(void) { parse_S(); consume(EOF_); printf("aceite\n"); }

int main(int argc, char **argv) {
  Token p1[] = {BEGIN, PRINT, NUM, EQUAL, NUM, SEMI, PRINT, NUM, EQUAL, NUM, END, EOF_};
  Token p2[] = {PRINT, NUM, EQUAL, NUM, END, EOF_};
  input = argc > 1 ? p2 : p1; pos = 0;
  advance();            /* carrega o primeiro token em next */
  accepted();
  return 0;
}
```

Saídas reais (`gcc -Wall`, sem avisos):

```
$ ./desc            # begin print 1=1 ; print 2=3 end
aceite
$ ./desc x          # print 1=1 end
erro: token inesperado (token END)
```

No segundo, `parse_S` reconhece `print 1=1` sem erro e é o
`consume(EOF_)` do `accepted` que falha, porque o próximo é `END`.

## Aula 7 --- Gramáticas LL(1)

### Ex. G --- Descida recursiva para as expressões (Exercício dos slides)

#### Resposta

Uma função por não-terminal; em $E'$ e $T'$ o último caso é a produção
$\varepsilon$, usada com qualquer outro símbolo (como nos slides: "outro
→ $E'\to\varepsilon$").

```haskell
data Token = NUM | PLUS | MINUS | TIMES | DIV | LPAREN | RPAREN
  deriving (Eq, Show)

consume :: Token -> [Token] -> [Token]
consume tok (first:rest) | tok == first = rest
consume tok _ = error ("expected " ++ show tok)

parseE, parseE', parseT, parseT', parseF :: [Token] -> [Token]
parseE toks = parseE' (parseT toks)               -- E  -> T E'

parseE' (PLUS  : toks) = parseE' (parseT toks)    -- E' -> + T E'
parseE' (MINUS : toks) = parseE' (parseT toks)    -- E' -> - T E'
parseE' toks           = toks                     -- E' -> eps

parseT toks = parseT' (parseF toks)               -- T  -> F T'

parseT' (TIMES : toks) = parseT' (parseF toks)    -- T' -> * F T'
parseT' (DIV   : toks) = parseT' (parseF toks)    -- T' -> / F T'
parseT' toks           = toks                     -- T' -> eps

parseF (NUM    : toks) = toks                     -- F  -> num
parseF (LPAREN : toks) = consume RPAREN (parseE toks)  -- F -> ( E )
parseF _               = error "syntax error"

accepted :: [Token] -> Bool
accepted toks = null (parseE toks)
```

Saídas reais (`runghc`):

| Entrada | Resultado |
|:--|:--|
| `1+2*3` | `True` |
| `1*(2-3)/4` | `True` |
| `1+)` | `syntax error` (o `parseF` vê `RPAREN`) |
| `1+` | `syntax error` (o `parseF` vê a lista vazia) |

Em `1+)`, o `+` leva a $E'\to +\,T\,E'$ e o $T$ precisa de um $F$, que
não pode começar por `)`.

### Ex. H --- NULLABLE, FIRST, FOLLOW e tabela das expressões transformadas (inventado)

Gramática: $S'\to E\,\$$, $E\to TE'$,
$E'\to +TE'\mid -TE'\mid\varepsilon$, $T\to FT'$,
$T'\to *FT'\mid /FT'\mid\varepsilon$, $F\to\texttt{num}\mid(E)$.

#### (a) Equações e cálculo iterativo de NULLABLE, FIRST e FOLLOW

**NULLABLE** ($N$):

- $N(S') = N(E)\wedge N(\$) = N(E)\wedge$ False
- $N(E) = N(T)\wedge N(E')$
- $N(E') = (N(+)\wedge\dots)\vee(N(-)\wedge\dots)\vee N(\varepsilon) =$ True
- $N(T) = N(F)\wedge N(T')$
- $N(T') =$ True (mesma razão)
- $N(F) = N(\texttt{num})\vee N((E)) =$ False

Iteração 1 (com a coluna 0, tudo False): $E'$ e $T'$ True, o resto False.
Iteração 2: $N(E)$ = False $\wedge$ True = False, $N(T)$ = False
$\wedge$ True = False; nada muda. **Só $E'$ e $T'$ são anuláveis.**

**FIRST** ($T$ e $F$ não anuláveis, por isso só conta o 1.º símbolo):

- FIRST($S'$) = FIRST($E$); FIRST($E$) = FIRST($T$); FIRST($T$) = FIRST($F$)
- FIRST($E'$) = $\{+\}\cup\{-\}\cup\emptyset$; FIRST($T'$) = $\{*\}\cup\{/\}\cup\emptyset$
- FIRST($F$) = $\{\texttt{num}, (\}$

| | 0 | 1 | 2 | 3 | 4 | 5 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| $S'$ | $\emptyset$ | $\emptyset$ | $\emptyset$ | $\emptyset$ | num ( | num ( |
| $E$ | $\emptyset$ | $\emptyset$ | $\emptyset$ | num ( | num ( | num ( |
| $E'$ | $\emptyset$ | + $-$ | + $-$ | + $-$ | + $-$ | + $-$ |
| $T$ | $\emptyset$ | $\emptyset$ | num ( | num ( | num ( | num ( |
| $T'$ | $\emptyset$ | $*$ / | $*$ / | $*$ / | $*$ / | $*$ / |
| $F$ | $\emptyset$ | num ( | num ( | num ( | num ( | num ( |

**FOLLOW**, ocorrência a ocorrência:

- $S'\to\underline{E}\,\$$: FOLLOW($E$) $\supseteq\{\$\}$.
- $E\to\underline{T}E'$: FOLLOW($T$) $\supseteq$ FIRST($E'$) = $\{+,-\}$;
  $E'$ anulável: FOLLOW($T$) $\supseteq$ FOLLOW($E$).
- $E\to T\underline{E'}$: FOLLOW($E'$) $\supseteq$ FOLLOW($E$).
- $E'\to +\underline{T}E'$ (e $-$): FOLLOW($T$) $\supseteq\{+,-\}$ e
  $\supseteq$ FOLLOW($E'$).
- $E'\to +T\underline{E'}$: FOLLOW($E'$) $\supseteq$ FOLLOW($E'$) (nada).
- $T\to\underline{F}T'$: FOLLOW($F$) $\supseteq\{*,/\}$ e $\supseteq$
  FOLLOW($T$). $T\to F\underline{T'}$: FOLLOW($T'$) $\supseteq$ FOLLOW($T$).
- $T'\to *\underline{F}T'$ (e $/$): FOLLOW($F$) $\supseteq\{*,/\}$ e
  $\supseteq$ FOLLOW($T'$); $T'\to *F\underline{T'}$: nada.
- $F\to(\underline{E})$: FOLLOW($E$) $\supseteq\{)\}$.

Juntando: FOLLOW($E$) $\supseteq\{\$,)\}$; FOLLOW($E'$) $\supseteq$
FOLLOW($E$); FOLLOW($T$) $\supseteq\{+,-\}\cup$ FOLLOW($E$) $\cup$
FOLLOW($E'$); FOLLOW($T'$) $\supseteq$ FOLLOW($T$); FOLLOW($F$)
$\supseteq\{*,/\}\cup$ FOLLOW($T$) $\cup$ FOLLOW($T'$).

| | 0 | 1 | 2 | 3 | 4 |
|:--|:-:|:-:|:-:|:-:|:-:|
| $E$ | $\emptyset$ | \$ ) | \$ ) | \$ ) | \$ ) |
| $E'$ | $\emptyset$ | $\emptyset$ | \$ ) | \$ ) | \$ ) |
| $T$ | $\emptyset$ | + $-$ | + $-$ \$ ) | + $-$ \$ ) | + $-$ \$ ) |
| $T'$ | $\emptyset$ | $\emptyset$ | + $-$ | + $-$ \$ ) | + $-$ \$ ) |
| $F$ | $\emptyset$ | $*$ / | $*$ / + $-$ | $*$ / + $-$ \$ ) | $*$ / + $-$ \$ ) |

Ex.: na 2, FOLLOW($T$) = $\{+,-\}\cup\{\$,)\}$ (FOLLOW($E$) da coluna 1)
$\cup\,\emptyset$ (FOLLOW($E'$) da coluna 1). A 4 repete a 3. (Confirmado
por um programa que aplica as equações.)

#### (b) Tabela de *parsing* preditivo; é LL(1)?

- $S'\to E\,\$$, $E\to TE'$, $T\to FT'$: FIRST = $\{\texttt{num}, (\}$.
- $E'\to +TE'$ em $+$; $E'\to -TE'$ em $-$; $E'\to\varepsilon$ em
  FOLLOW($E'$) = $\{\$,)\}$.
- $T'\to *FT'$ em $*$; $T'\to /FT'$ em $/$; $T'\to\varepsilon$ em
  FOLLOW($T'$) = $\{+,-,\$,)\}$.
- $F\to\texttt{num}$ em num; $F\to(E)$ em `(`.

| | num | $+$ | $-$ | $*$ | / | ( | ) | \$ |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| $S'$ | $E\,\$$ | | | | | $E\,\$$ | | |
| $E$ | $TE'$ | | | | | $TE'$ | | |
| $E'$ | | $+TE'$ | $-TE'$ | | | | $\varepsilon$ | $\varepsilon$ |
| $T$ | $FT'$ | | | | | $FT'$ | | |
| $T'$ | | $\varepsilon$ | $\varepsilon$ | $*FT'$ | $/FT'$ | | $\varepsilon$ | $\varepsilon$ |
| $F$ | num | | | | | $(E)$ | | |

(cada entrada é o lado direito da produção da linha). No máximo uma
produção por entrada: **é LL(1)**.

### Ex. I --- Parsing de num + num * num com a pilha (inventado)

#### Resposta

Tabela do Ex. H(b); pilha com o topo à esquerda.

| Pilha | Entrada | Ação |
|:--|--:|:--|
| $S'$ | `num+num*num$` | $S'\to E\,\$$ |
| $E\,\$$ | `num+num*num$` | $E\to TE'$ |
| $T\,E'\,\$$ | `num+num*num$` | $T\to FT'$ |
| $F\,T'\,E'\,\$$ | `num+num*num$` | $F\to\texttt{num}$ |
| num $T'\,E'\,\$$ | `num+num*num$` | consumir num |
| $T'\,E'\,\$$ | `+num*num$` | $T'\to\varepsilon$ (coluna $+$) |
| $E'\,\$$ | `+num*num$` | $E'\to +TE'$ |
| $+\,T\,E'\,\$$ | `+num*num$` | consumir $+$ |
| $T\,E'\,\$$ | `num*num$` | $T\to FT'$ |
| $F\,T'\,E'\,\$$ | `num*num$` | $F\to\texttt{num}$ |
| num $T'\,E'\,\$$ | `num*num$` | consumir num |
| $T'\,E'\,\$$ | `*num$` | $T'\to *FT'$ |
| $*\,F\,T'\,E'\,\$$ | `*num$` | consumir $*$ |
| $F\,T'\,E'\,\$$ | `num$` | $F\to\texttt{num}$ |
| num $T'\,E'\,\$$ | `num$` | consumir num |
| $T'\,E'\,\$$ | `$` | $T'\to\varepsilon$ |
| $E'\,\$$ | `$` | $E'\to\varepsilon$ |
| \$ | `$` | consumir \$ |
| $\varepsilon$ | $\varepsilon$ | aceitação |

As produções usadas formam a árvore da figura de `1 + 2 * 3` no resumo.

### Ex. J --- Fatorização à esquerda de S para aSb ou ab (inventado)

#### (a) Não é LL(1)

Com $S'\to S\,\$$: nada é anulável, FIRST($aSb$) = $\{a\}$ e FIRST($ab$)
= $\{a\}$. As duas produções de $S$ vão para a entrada (linha $S$, coluna
$a$): **duas produções na mesma entrada**, logo não é LL(1). Com um só
símbolo de *look-ahead* não se sabe se o `a` abre um $aSb$ ou um $ab$.

#### (b) Fatorizar, mostrar que é LL(1) e fazer o *parsing* de `aabb`

O prefixo comum é $a$: $S\to aX$, $X\to Sb\mid b$ (mesma linguagem,
$a^nb^n$ com $n\ge 1$).

- NULLABLE: tudo False (nenhuma produção $\varepsilon$; cada lado direito
  tem um terminal ou um $S$ não anulável).
- FIRST($S$) = $\{a\}$; FIRST($X$) = FIRST($Sb$) $\cup$ FIRST($b$) =
  $\{a\}\cup\{b\}$ = $\{a,b\}$.
- FOLLOW($S$) $\supseteq\{\$\}$ ($S'\to S\$$) e $\{b\}$ ($X\to Sb$);
  FOLLOW($X$) $\supseteq$ FOLLOW($S$) ($S\to aX$, $X$ no fim):
  ambos $\{b,\$\}$. Sem produções anuláveis, não entram na tabela.

| | $a$ | $b$ | \$ |
|:--|:--|:--|:--|
| $S'$ | $S'\to S\,\$$ | | |
| $S$ | $S\to aX$ | | |
| $X$ | $X\to Sb$ | $X\to b$ | |

FIRST($Sb$) = $\{a\}$ e FIRST($b$) = $\{b\}$ são disjuntos: no máximo
uma produção por entrada, **é LL(1)**.

| Pilha | Entrada | Ação |
|:--|--:|:--|
| $S'$ | `aabb$` | $S'\to S\,\$$ |
| $S\,\$$ | `aabb$` | $S\to aX$ |
| $a\,X\,\$$ | `aabb$` | consumir $a$ |
| $X\,\$$ | `abb$` | $X\to Sb$ (coluna $a$) |
| $S\,b\,\$$ | `abb$` | $S\to aX$ |
| $a\,X\,b\,\$$ | `abb$` | consumir $a$ |
| $X\,b\,\$$ | `bb$` | $X\to b$ (coluna $b$) |
| $b\,b\,\$$ | `bb$` | consumir $b$ |
| $b\,\$$ | `b$` | consumir $b$ |
| \$ | `$` | consumir \$ |
| $\varepsilon$ | $\varepsilon$ | aceitação |
