---
title: "Compiladores --- Soluções dos exercícios \"Pratica agora\""
subtitle: "Folha laboratorial 2 (Praticas/Semana_1/scanner-c) e exercício dos slides da Aula 4. Tenta primeiro sozinho; abre uma alínea só depois de a teres feito."
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

## Aula 4 --- Ambiguidade

### Exercício dos slides --- programas sequenciais

$S \to S;S \mid \texttt{ident}=E \mid \texttt{ident}{+}{+}$ e
$E \to \texttt{ident} \mid \texttt{num} \mid E+E$.

#### (a) Mostrar a ambiguidade nas instruções ($S \to S;S$)

Frase: `a=1; b=2; c++`. Tem **duas** árvores sintáticas diferentes. Nas
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

#### (b) Mostrar a ambiguidade nas expressões ($E \to E+E$)

Frase: `x = a+b+c`. É o mesmo problema de `E → E+E` do resumo:

- `x = (a+b)+c`: o $E$ de topo é $E+E$ e o seu filho **esquerdo** é
  outro $E+E$.
- `x = a+(b+c)`: o filho **direito** é que é outro $E+E$.

São duas árvores diferentes para a mesma frase.

#### (c) Gramática equivalente não ambígua

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
