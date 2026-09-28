---
title: "Compiladores --- Soluções dos exercícios \"Pratica agora\""
subtitle: "Folha laboratorial 2 (Praticas/Semana_1/scanner-c) e Folha laboratorial 3 (Praticas/Semana_2/gramatica). Tenta primeiro sozinho; abre uma alínea só depois de a teres feito."
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
