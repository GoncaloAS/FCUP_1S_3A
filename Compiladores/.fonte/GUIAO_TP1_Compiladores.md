---
title: "Compiladores --- TP1: defesa"
subtitle: "Sexta 13 nov 2026: abrir, demonstrar, explicar o código linha a linha e responder"
---

<!-- Fonte: ~/Downloads/COMP_TP1.zip (11 nov 2026), o mesmo código do
     repositório github.com/matilde938/COMP_TP1 (commit c47731b) clonado em
     ~/Desktop/COMP_TP1 (só o README.pdf difere). Compilado e testado a
     11 nov 2026 com bison 3.8.2 (Homebrew) e flex 2.6.4: todas as saídas
     deste guião são reais. Os números de linha são os do zip. -->

| | |
|:--|:--|
| **Tarefa** | *scanner* + *parser* de um subconjunto de Pascal que **imprime a AST** |
| **Feito em** | C com **Flex + Bison** (7 ficheiros, 669 linhas) |
| **Defesa** | **sexta 13 nov 2026**, na aula prática; o professor pode apontar para **qualquer linha** e perguntar o que faz |
| **Como usar isto** | §1 na sexta de manhã; §2 para perceber compiladores do zero (ler primeiro); §5 o código linha a linha; §6 as perguntas |

# 1. Na sexta: passo a passo

\needspace{10\baselineskip}

## 1.1 Na véspera (no computador que vais levar)

```bash
# 1. Bison 3 (o do macOS é o 2.3 e NÃO compila o parser.bison)
export PATH=/opt/homebrew/opt/bison/bin:$PATH
bison --version          # tem de dizer 3.8.2

# 2. Uma pasta limpa com o código entregue
mkdir -p ~/Desktop/defesa && cd ~/Desktop/defesa
unzip ~/Downloads/COMP_TP1.zip && cd COMP_TP1

# 3. Ensaiar a demonstração toda (§1.3) uma vez
make clean && make && make test
```

Para não ter de escrever o `export` na aula, põe-no no fim do `~/.zshrc`:

```bash
echo 'export PATH=/opt/homebrew/opt/bison/bin:$PATH' >> ~/.zshrc
```

\needspace{10\baselineskip}

## 1.2 Na aula, antes de chamarem

1. Terminal com letra grande (`Cmd +` duas vezes), na pasta `COMP_TP1/`.
2. O editor aberto na mesma pasta (`code .`), com **números de linha
   visíveis** e quatro separadores: `scanner.flex`, `parser.bison`, `ast.h`,
   `printAbsTree.c`. Quando ele disser "linha 87 do parser", `Ctrl G` e o
   número.
3. `make clean` feito, para a compilação aparecer do zero.

\needspace{10\baselineskip}

## 1.3 A demonstração (cerca de 5 minutos)

| # | Escreves | Dizes enquanto corre |
|--:|:---------|:--------------------|
| 1 | --- | **Abertura (30 s):** "Fizemos o *scanner* e o *parser* de um subconjunto de Pascal, em C, com Flex e Bison. O Flex parte o programa em *tokens*; o Bison verifica se a sequência de *tokens* respeita a gramática e, à medida que reconhece cada regra, constrói a árvore sintática abstrata, que no fim imprimimos. Aceita declarações `integer` e `boolean`, atribuições, `if`, `while`, blocos, `read`/`write` e expressões aritméticas, relacionais e booleanas. Se houver um erro diz a linha e sai com código 1." |
| 2 | `make` | "O Makefile corre primeiro o Bison, que gera `parser.c` e `parser.h`; depois o Flex, que gera `scanner.c` e precisa do `parser.h` para saber os códigos dos *tokens*; depois compila os `.c` e junta tudo no executável `pascal`. O aviso que aparece é no `scanner.c`, código gerado pelo Flex, não no nosso." |
| 3 | `make test` | "Corre os 7 ficheiros de `tests/`: os 4 exemplos dão código de saída 0 e os 3 com erros dão 1." |
| 4 | `./pascal tests/exemplo3.pas` | Explicas a árvore (abaixo). |
| 5 | `./pascal tests/exemplo1.pas` | "Em `2 + 3 * 4` o `*` fica mais abaixo, por isso é calculado primeiro: é o efeito das precedências. Em `(x - 1) div 2 mod 3` o `div` fica dentro do `mod`: associam à esquerda. Os parênteses não aparecem na árvore: a forma dela já diz a ordem." |
| 6 | `./pascal tests/exemplo4.pas` | "Maiúsculas (`PROGRAM`, `WriteLn`) funcionam, `''` é uma plica dentro de uma string, comentário `(* *)`, `writeln()` vazio e o *dangling else*: o `else` ficou no `if` de dentro, que é a regra do Pascal." |
| 7 | `./pascal tests/erro_lexico.pas` | "Erro lexical: o `@` não é nenhum *token*. Quem o deteta é o *scanner*." |
| 8 | `./pascal tests/erro.pas` | "Erro de sintaxe: falta o operando depois do `+`. Diz linha 4 e não 3 porque o parser só percebe que falta quando lê o `end`." |
| 9 | `./pascal tests/erro_relacional.pas` | "`a < b < c` é erro: os relacionais não são associativos." |
| 10 | o que ele pedir | Ver §4. |

**A árvore do `exemplo3.pas`** (o que explicar, de cima para baixo):

```
Program Soma                <- a raiz: o nome do programa
  Declaracoes
    Decl integer            <- uma linha "n, i, s : integer;"
      Var n
      Var i
      Var s
  Corpo                     <- os comandos entre begin e end
    Readln                  <- readln(n)
      Var n
    Assign i                <- i := 1
      Int 1
    Assign s
      Int 0
    While                   <- 1.º filho: a condição; 2.º: o corpo
      <=
        Var i
        Var n
      Assign s              <- o begin...end do while não tem nó:
        +                      os comandos do bloco ficam lado a lado
          Var s
          Var i
      Assign i
        +
          Var i
          Int 1
    Writeln
      String 'soma = '
      Var s
```

"Cada nível de indentação (2 espaços) é um nível da árvore: os filhos de
um nó estão logo abaixo dele, mais à direita. Imprimimos em pré-ordem:
primeiro o nó, depois os filhos."

\needspace{10\baselineskip}

## 1.4 Experimentar ao vivo

Se ele pedir para escrever um programa, há duas maneiras:

```bash
./pascal                      # lê do teclado: escreve o programa,
                              # Enter e depois Ctrl-D para acabar
echo 'program P; begin x := -2*3 end.' | ./pascal
```

O resultado de cada experiência provável está na §4.

\needspace{10\baselineskip}

# 2. Compiladores do zero

Esta secção explica as ideias que o professor assume que sabes. Lê-a antes
do código.

\needspace{10\baselineskip}

## 2.1 O que é um compilador

Um compilador traduz um programa escrito numa linguagem (aqui Pascal) para
outra (por exemplo, código máquina). Faz isso em **fases**, cada uma a
passar o resultado à seguinte:

![](figuras/tp1_fases.pdf){width=100%}

| Fase | Pergunta que responde | No TP1 |
|---|---|---|
| **Análise lexical** (*scanner*, *lexer*) | Que "palavras" tem o texto? | **Sim**: `scanner.flex` |
| **Análise sintática** (*parser*) | As palavras estão por uma ordem válida? Qual é a estrutura? | **Sim**: `parser.bison` |
| Construção da **AST** | Uma árvore só com o que importa | **Sim**: `ast.h`, `ast.c`, ações do Bison |
| Análise semântica | Faz sentido? (variáveis declaradas, tipos certos) | Não: é a 2.ª parte |
| Geração de código | Traduzir para a máquina | Não |

Uma comparação com português: a análise lexical separa uma frase em
palavras e diz de que tipo é cada uma; a sintática verifica se
"sujeito verbo complemento" está bem formado; a semântica deteta que "a
mesa comeu a cadeira" está bem escrita mas não faz sentido.

\needspace{10\baselineskip}

## 2.2 Análise lexical: *tokens* e expressões regulares

O *scanner* lê o ficheiro caracter a caracter e agrupa-o em **tokens**.
Um *token* tem um **tipo** (`ID`, `INT`, `PLUS`…) e, às vezes, um
**valor**; o texto exato que o formou chama-se **lexema**. Espaços e
comentários são deitados fora.

```
texto:   x := 2 + 3 * 4;
tokens:  ID("x")  ASSIGN  INT(2)  PLUS  INT(3)  MULT  INT(4)  SEMICOLON
```

Cada tipo de *token* descreve-se com uma **expressão regular** (um padrão
de texto). O mínimo para ler o `scanner.flex`:

| Padrão | Quer dizer | Exemplo |
|---|---|---|
| `"if"` | exatamente este texto | `if` |
| `[0-9]` | um caracter do conjunto | `7` |
| `[a-zA-Z_]` | uma letra ou `_` | `x`, `B` |
| `[^}]` | um caracter que **não** está no conjunto (o `^` nega) | tudo menos `}` |
| `.` | qualquer caracter **exceto** a mudança de linha | |
| `X*` | X zero ou mais vezes | |
| `X+` | X uma ou mais vezes | `[0-9]+` = `42` |
| `X|Y` | X ou Y | |
| `( )` | agrupa | `(ab)*` |
| `\n`, `\t`, `\r` | mudança de linha, tab, *carriage return* | |

**O Flex** recebe uma lista de regras `padrão { código C }` e gera uma
função em C, `yylex()`, que a cada chamada lê o próximo *token* e devolve
o seu código (um número). Quando várias regras servem, decide assim:

1. **Longest match**: ganha a regra que consome **mais caracteres**. Em
   `<=`, a regra `"<="` lê 2 e a `"<"` só 1: ganha `<=`. Em `ifx`, a regra
   do identificador lê 3 e a de `if` só 2: é um identificador.
2. **First match**: se empatarem no comprimento, ganha a que está
   **escrita primeiro**. Em `if`, a regra `"if"` e a do identificador
   leem ambas 2: ganha `"if"` porque está antes. É por isso que as palavras
   reservadas estão escritas antes da regra do `ID`.

Uma regra sem `return` (espaços, comentários) não devolve nada: o Flex
continua a ler até encontrar uma regra que devolva um *token*.

\needspace{10\baselineskip}

## 2.3 Gramáticas

A sintaxe descreve-se com uma **gramática independente de contexto**:

- **Terminais**: os *tokens* (`IF`, `PLUS`, `ID`…), em maiúsculas no Bison.
- **Não-terminais**: categorias (`expr`, `cmd`, `program`…), em minúsculas.
- **Regras** (produções): `cmd: WHILE expr DO cmd` lê-se "um comando
  **pode ser** `while`, seguido de uma expressão, `do` e outro comando".
  As alternativas separam-se com `|`.
- **Símbolo inicial**: o que representa o programa inteiro (`program`).
- `%empty`: a alternativa vazia (não consome nada).

Uma **derivação** é substituir não-terminais pelas suas regras até só
haver *tokens*. Se se consegue chegar à sequência de *tokens* do programa,
ele é sintaticamente válido. Desenhar as substituições dá a **árvore de
derivação** (ou árvore sintática concreta).

**Listas com recursividade.** `ids: ID | ID COMMA ids` diz "uma lista de
identificadores é um `ID`, ou um `ID`, uma vírgula e outra lista". Para
`a, b, c`: `ids` → `a , ids` → `a , b , ids` → `a , b , c`. Uma regra que se
usa a si própria é **recursiva**; aqui à **direita** (o `ids` está no fim).

\needspace{10\baselineskip}

## 2.4 Ambiguidade, precedência e associatividade

Uma gramática é **ambígua** se o mesmo texto tem duas árvores. A nossa
regra `expr: expr PLUS expr | expr MULT expr | …` é ambígua:

```
   2 + 3 * 4  como  2 + (3 * 4)        ou        (2 + 3) * 4

        +                                     *
      /   \                                 /   \
     2     *                               +     4
          / \                             / \
         3   4                           2   3
```

Dão resultados diferentes (14 e 20), por isso é preciso dizer ao Bison qual
escolher:

- **Precedência**: qual operador "agarra" primeiro. `*` tem mais do que
  `+`, logo `3 * 4` fica junto, mais abaixo na árvore. **Mais abaixo =
  calculado primeiro.**
- **Associatividade**: com dois operadores iguais (ou da mesma linha),
  qual vai primeiro. `%left` (à esquerda): `2 - 3 - 4` = `(2 - 3) - 4`.
  `%nonassoc`: não se podem encadear (`a < b < c` é erro).

**Dangling else** ("else pendurado"): em
`if a then if b then x := 1 else x := 2`, o `else` pode ser do `if` de
dentro ou do de fora. O Pascal (e o C, e o Java) diz: do **mais próximo**.

\needspace{10\baselineskip}

## 2.5 Como o Bison faz o *parsing*: *shift* e *reduce*

O Bison gera a função `yyparse()`, um *parser* **LALR(1)**:

- **L**: lê da esquerda para a direita;
- **R**: constrói a derivação mais à direita, ao contrário, ou seja,
  **ascendente** (*bottom-up*): reconhece primeiro as folhas e vai subindo;
- **(1)**: decide olhando para **1** *token* à frente (o *lookahead*);
- **LA**: *look-ahead*, a forma compacta das tabelas que o Bison usa.

Tem uma **pilha** e duas ações:

- **shift** (empilhar): pede o próximo *token* ao *scanner* e põe-o na pilha;
- **reduce** (reduzir): quando o topo da pilha é o lado direito de uma
  regra, substitui-o pelo lado esquerdo. **É neste momento que corre a
  ação `{ ... }` da regra e se cria o nó da AST.**

Isto é o que o nosso *parser* faz de facto com `x := 2 + 3 * 4`
(rastreio real com `yydebug`):

| Pilha (topo à direita) | Próximo | Ação |
|---|---|---|
| `ID :=` | `2` | *shift* `INT` |
| `ID := INT` | `+` | *reduce* `factor: INT` (cria `Int 2`), depois `expr: factor` |
| `ID := expr` | `+` | *shift* `+` |
| `ID := expr + INT` | `*` | *reduce* até `expr` (cria `Int 3`) |
| `ID := expr + expr` | `*` | **conflito**: reduzir `expr + expr` ou empilhar `*`? `*` tem mais precedência: ***shift*** |
| `ID := expr + expr * INT` | `end` | *reduce* até `expr` (cria `Int 4`) |
| `ID := expr + expr * expr` | `end` | *reduce* `expr MULT expr` (cria o nó `*`) |
| `ID := expr + expr` | `end` | *reduce* `expr PLUS expr` (cria o nó `+`) |
| `ID := expr` | `end` | *reduce* `cmd: ID ASSIGN expr` (cria `Assign x`) |

Repara que os nós são criados **de baixo para cima**: primeiro os números,
depois o `*`, depois o `+`, por fim a atribuição.

**Conflitos.** Quando o *parser* pode fazer duas coisas há um conflito:
*shift/reduce* (empilhar ou reduzir, a linha 5 da tabela) ou
*reduce/reduce* (duas regras para reduzir). As declarações de precedência
resolvem os *shift/reduce*: o Bison compara a precedência da **regra** (a
do seu último terminal; `expr PLUS expr` tem a de `PLUS`) com a do
**token** seguinte. Token com mais → *shift*; com menos → *reduce*; igual →
`%left` reduz, `%right` empilha, `%nonassoc` dá erro. A nossa gramática
compila **sem nenhum conflito** (`bison -Wall` não dá avisos).

\needspace{10\baselineskip}

## 2.6 AST: árvore sintática abstrata

A árvore de derivação tem um nó por cada regra e *token*: `;`, `begin`,
`end`, parênteses, `factor`… A **AST** guarda só o que importa para o
significado do programa:

| Na árvore de derivação | Na AST |
|---|---|
| `( x - 1 )` → `factor` → `expr` → ... | só o nó `-` com `x` e `1` (a forma já dá a ordem) |
| `begin c1; c2 end` | os comandos `c1`, `c2` (o bloco não tem nó) |
| `;`, `:=`, `then`, `do`, `.` | nada |
| `expr: factor`, `factor: INT` | só `Int 2` |

A AST constrói-se nas **ações semânticas** do Bison:
`expr: expr PLUS expr { $$ = ast_operation(PLUS, $1, $3); }`. Aqui `$1` é
o valor do 1.º símbolo do lado direito (a subárvore da esquerda), `$3` o do
3.º (a da direita; o `$2` seria o `+`) e `$$` é o valor que fica associado
ao `expr` do lado esquerdo, o nó novo.

![](figuras/tp1_ast_exemplo.pdf){width=36%}

\needspace{10\baselineskip}

## 2.7 O C que precisas de saber para ler o código

| Coisa | O que é | Onde aparece |
|---|---|---|
| `struct` | um registo com vários campos | os nós da AST (`ast.h`) |
| `union` | vários campos que **partilham a mesma memória**: só um é válido de cada vez | `attr` em `Expr` e `Cmd` |
| `enum` | uma lista de constantes com nome (`E_INTEGER` = 0, `E_BOOLEAN` = 1, …) | o `kind` de cada nó |
| `typedef struct _Expr Expr;` | dá o nome curto `Expr` ao tipo `struct _Expr` | `ast.h` |
| ponteiro `Expr*` | o endereço de um nó; `NULL` = "não há" | filhos dos nós |
| `p->campo` | o campo do registo para onde `p` aponta | `node->kind` |
| `malloc(sizeof(Expr))` | reserva memória para um nó novo | `ast.c` |
| `strdup(s)` | faz uma cópia de uma *string* (com `malloc`) | `scanner.flex` |
| `atoi(s)` | converte o texto `"42"` no inteiro 42 | `scanner.flex` |
| `extern` | "esta variável/função existe noutro ficheiro" | `parser.bison` |
| `#include "x.h"` | copia o *header* para aqui (declarações partilhadas) | todos |
| `stderr` / `stdout` | saída de erros / saída normal | erros / AST |
| `exit(1)` / `return 1` em `main` | termina com código de saída 1 (= erro) | |

**Glossário Flex/Bison** (nomes que o professor vai usar):

| Nome | O que é |
|---|---|
| `yylex()` | função gerada pelo Flex: devolve o código do próximo *token* |
| `yyparse()` | função gerada pelo Bison: faz o *parsing* todo; devolve 0 (ok) ou 1 (erro) |
| `yytext` | o texto do *token* atual (o lexema); é **reescrito** a cada *token* |
| `yylval` | onde o *scanner* põe o **valor** do *token* (o número, o nome) para o *parser* |
| `yylineno` | o número da linha atual (com `%option yylineno`) |
| `yyin` | o ficheiro de onde o *scanner* lê (por omissão o teclado, *stdin*) |
| `yyerror(msg)` | função que **nós** escrevemos e o Bison chama num erro de sintaxe |
| `parser.h` | *header* gerado pelo Bison: os códigos dos *tokens* e o tipo de `yylval` |

\needspace{10\baselineskip}

# 3. O esquema do projeto

![](figuras/tp1_pipeline.pdf){width=100%}

1. `main.c` abre o ficheiro (`yyin = fopen(...)`) e chama `yyparse()`.
2. O *parser* pede *tokens* ao *scanner* (`yylex()`), um a um. Para `INT`,
   `ID` e `STR` o *scanner* põe o valor em `yylval`.
3. Sempre que o *parser* reduz uma regra corre a ação dela, que cria o nó
   da AST a partir dos nós dos filhos.
4. A regra `program` guarda a raiz na variável global `root`. Se
   `yyparse()` devolve 0, `main` chama `printProgram(root)`.
5. Erros: o *scanner* escreve a mensagem e faz `exit(1)`; o *parser* chama
   `yyerror` e `yyparse()` devolve 1. Para no primeiro erro.

| Ficheiro | Linhas | O que tem |
|---|--:|---|
| `scanner.flex` | 87 | as expressões regulares dos *tokens* |
| `parser.bison` | 144 | *tokens*, precedências, gramática, ações que criam a AST, `yyerror` |
| `ast.h` | 134 | os tipos dos nós e as declarações das funções |
| `ast.c` | 135 | os construtores `ast_*` (um por tipo de nó) |
| `printAbsTree.c` | 123 | a impressão da árvore |
| `main.c` | 22 | abrir o ficheiro, `yyparse()`, imprimir |
| `Makefile` | 24 | `make`, `make test`, `make clean` |
| `tests/` | --- | 4 programas corretos e 3 com erros |

\needspace{10\baselineskip}

# 4. Testes ao vivo (testados a 11 nov 2026)

Se ele pedir para experimentar algo (dentro de `program P; begin … end.`):

| Programa | Resultado | Porquê |
|---|---|---|
| `program P; begin end.` | `Program P` / `Corpo` | `cmds` aceita o comando vazio |
| `x := -2*3` | `*` com filhos `-(2)` e `3` | o menos unário está no `factor`: liga só ao `2` |
| `x := 2-3-4` | `-` com `-(2,3)` à esquerda | `%left`: associa à esquerda |
| `x := not a and b` | `and` com `not a` e `b` | `not` está no `factor` |
| `x := a < b and c` | `<` com `a` e `and(b,c)` | como em Pascal, `and` tem mais prioridade que `<` |
| `x := a = b = c` | erro "unexpected =" | `%nonassoc` |
| `x := 1;` antes de `end` | aceita | comando vazio |
| `x := 1 y := 2` | "unexpected ID, expecting end - 'y'" | falta `;` |
| `if a then if b then x:=1 else x:=2` | `else` no `if` de dentro | `%precedence THEN` < `ELSE` |
| `while x < 10 do x := x+1; x := 0` | o `x := 0` fica fora do `while` | sem `begin…end` o corpo é um só comando |
| `x := --1` | `-` dentro de `-` | `MINUS factor` é recursivo |
| `x := 1 + + 2` | erro | não há `+` unário |
| `var x : real;` | "unexpected ID, expecting integer or boolean - 'real'" | só esses dois tipos; `real` não é palavra reservada, é um ID |
| `var begin : integer;` | "unexpected begin, expecting ID" | palavras reservadas não são identificadores |
| `writeln('sem fim)` | "caracter invalido - '''" | a plica sozinha não forma *token* |
| `x := 'abc'` | erro "unexpected STR" | *strings* só no `write` |
| `read(x+1)` | erro | o `read` só aceita identificadores |
| `{ comentário sem fim` | "comentario nao fechado - '{'" com a linha onde abriu | regra própria no Flex |
| `(* um (* dois *) x := 1` | aceita, só `x := 1` | os comentários não se aninham (como em Pascal) |
| `x := 99999999999` | `Int 1215752191` | **limitação**: o `atoi` transborda sem aviso |
| `X := x` | `Assign X` / `Var x` | os nomes guardam as maiúsculas (§6.6) |
| `if x then else y := 1` | **igual a** `if x then y := 1` | **limitação da impressão** (§6.6) |

\newpage

# 5. O código linha a linha

Para cada bloco de linhas: o que faz e o que responder se ele apontar para
lá. Os números são os do zip entregue.

\needspace{10\baselineskip}

## 5.1 `Makefile`

| Linhas | O que fazem |
|:--|:--------------------------------|
| 2--5 | Variáveis: os `.o` a juntar (`OBJS`), os ficheiros gerados (`INTERM`), o nome do executável e as opções do compilador. `-g` põe informação de *debug*; `-Wall -Wextra` ligam os avisos. |
| 7 | `all` é o primeiro alvo, por isso `make` sem nada faz `make all`, que precisa do `./pascal`. |
| 9--10 | `scanner.c` faz-se a partir do `scanner.flex` **e** do `parser.h` (o *scanner* usa os códigos dos *tokens*). Por isso o Bison corre antes do Flex. |
| 12--13 | O Bison gera `parser.c` e, com `--defines=parser.h`, o *header* com os códigos dos *tokens* e o `%union`. |
| 16 | Todos os `.o` dependem de `ast.h` e `parser.h`: se mudarem, recompilam. Cada `.o` faz-se do `.c` com o mesmo nome por uma **regra implícita** do `make` (`cc $(CFLAGS) -c x.c`), por isso não está escrita. |
| 18--19 | Ligação (*linking*): junta os 5 `.o` no executável. |
| 20--21 | `make clean` apaga o executável, os `.o` e os ficheiros gerados. |
| 23--24 | `make test`: um ciclo da *shell* por `tests/*.pas`; corre cada um e mostra o código de saída. `$$f` e `$$?` têm dois `$` porque no Makefile o `$` sozinho é das variáveis do `make`; `$$` passa um `$` à *shell*. `$?` é o código de saída do último comando. |

\needspace{10\baselineskip}

## 5.2 `main.c`

| Linhas | O que fazem |
|:--|:--------------------------------|
| 3 | Inclui o `parser.h` para conhecer `yyparse`, `yyin` e `root` (os `extern` do `%code requires`). |
| 5 | **Define** a variável global `root` (a raiz da AST). O `parser.bison` só a **declara** com `extern` (l. 59) e preenche-a na regra `program`. |
| 9 | Salta o nome do programa: `argv[0]` é `./pascal`; depois disto `*argv` é o 1.º argumento. |
| 10--16 | Se houver argumento, abre-o para leitura e põe-no em `yyin`, de onde o Flex lê. Se não abrir, erro e sai com 1. Sem argumento `yyin` fica `NULL` e o Flex lê do *stdin*. |
| 17--20 | `yyparse()` faz tudo (pede os *tokens*, constrói a AST). Se devolver 0 imprime a árvore e sai com 0. |
| 21 | Erro de sintaxe: a mensagem já foi escrita pelo `yyerror`; sai com 1. Os erros lexicais nem chegam aqui (o *scanner* faz `exit(1)`). |

\newpage

## 5.3 `scanner.flex`

Um ficheiro Flex tem 3 partes separadas por `%%`: definições e código C
(l. 1--15), regras (l. 18--86), código C final (vazio).

| Linhas | O que fazem |
|:--|:--------------------------------|
| 1--12 | O que está entre `%{` e `%}` é copiado tal e qual para o `scanner.c`. Inclui o `parser.h` para ter os códigos dos *tokens* (`PLUS`, `ID`…) e o `yylval`. |
| 8--11 | `lexError`: escreve no *stderr* "Linha N: mensagem - 'texto'" com o `yylineno` e o `yytext`, e termina com `exit(1)`. `static`: só existe neste ficheiro. |
| 15 | Opções: `noyywrap` (só há um ficheiro de entrada; sem isto teríamos de escrever a função `yywrap`); `yylineno` (o Flex conta as linhas); `caseless` (não distingue maiúsculas: `BEGIN` = `begin`, como em Pascal); `nounput`/`noinput` (não gera duas funções que não usamos, que davam avisos de "não usada"). |
| 18 | Espaços, tabs, `\r` e mudanças de linha: ação vazia, deitados fora. |
| 19 | Comentário `{ … }`: `{`, depois qualquer coisa que não seja `}` (incluindo mudanças de linha), depois `}`. |
| 20 | Comentário `(* … *)`: `"(*"` abre; no meio `([^*]|"*"+[^*)])*`, isto é, caracteres que não são `*`, ou um ou mais `*` seguidos de algo que não é `*` nem `)`; `"*"+")"` fecha com um ou mais `*` e `)`. Assim `(* a ** b *)` funciona e o comentário acaba no **primeiro** `*)`. |
| 21 | Comentário de linha `// …`: o `.` não apanha a mudança de linha, por isso acaba no fim da linha. |
| 22--27 | `{` **sem** `}`: só serve quando a l. 19 não serve (se houver `}`, a l. 19 lê mais um caracter e ganha por *longest match*). O comentário pode ter muitas linhas e o `yylineno` já as contou, por isso o ciclo da l. 24 desconta uma por cada `\n` do `yytext`: a mensagem indica a linha onde o comentário **abriu**. A l. 25 corta o `yytext` depois do 1.º caracter para a mensagem mostrar só `'{'`. |
| 28 | `(*` sem `*)`: se a l. 20 não serve, esta (2 caracteres) ganha à regra do `"("` (1 caracter). |
| 31--52 | Palavras reservadas, cada uma devolve o seu código. Estão **antes** da regra do `ID` (l. 82) para ganharem no empate (*first match*). `BEGIN_T` e não `BEGIN` porque `BEGIN` já é uma macro do Flex (para mudar de estado). |
| 55--58 | Operadores de 2 caracteres. A ordem não importa: em `:=` ganha `":="` a `":"` por ler mais (*longest match*). |
| 59--71 | Operadores e pontuação de 1 caracter. |
| 74--77 | Inteiro: um ou mais dígitos. `atoi` converte o texto no número, que vai em `yylval.intValue` (o campo `intValue` do `%union` do Bison). Devolve `INT`. |
| 78--81 | *String*: plica, depois zero ou mais de (um caracter que não é plica nem `\n`, **ou** duas plicas seguidas `''`), plica. `''` é uma plica dentro do texto, como em Pascal: `'It''s ok'`. Guarda o texto **com** as plicas. |
| 82--85 | Identificador: letra ou `_`, depois letras, dígitos ou `_`. `strdup` porque o `yytext` é reescrito no *token* seguinte: sem a cópia todos os nomes na AST acabariam iguais ao último lido. |
| 86 | `.` apanha qualquer caracter que nenhuma regra apanhou (é a última, por isso só ganha quando nada mais serve): erro "caracter invalido". |

\newpage

## 5.4 `parser.bison`

| Linhas | O que fazem |
|:--|:--------------------------------|
| 4--13 | Declara os *tokens*. O texto entre aspas (`END "end"`) é o nome que aparece nas mensagens de erro ("expecting end" em vez de "expecting END"). O Bison dá a cada um um número e escreve-os no `parser.h`. `INT ID STR` não têm alias e aparecem assim nas mensagens. |
| 16--20 | **Precedências.** Cada linha tem **mais** prioridade do que a anterior: os relacionais (`%nonassoc`) têm a menor; depois `+ - or` (`%left`); depois `* / div mod and` (`%left`), a maior. É a ordem do Pascal. `%precedence` dá precedência sem associatividade; `THEN` e `ELSE` só servem para o *dangling else* (§6.3). |
| 23 | O símbolo inicial é `program`. |
| 26 | Mensagens de erro detalhadas: dizem o *token* encontrado e os esperados. Sem isto diria só "syntax error". |
| 29--37 | `%union`: os tipos de valor que um símbolo pode ter. O Bison faz dele o tipo `YYSTYPE` do `yylval` e da pilha de valores. |
| 39--45 | `%type`: qual campo do `%union` usa cada símbolo. `INT` e `type` são `int`; `ID` e `STR` são `char*`; `expr`/`factor`/`arg` são `Expr*`; etc. É isto que dá o tipo C certo a `$$`, `$1`, `$3`. |
| 49--60 | `%code requires`: código que vai para o `parser.c` **e** para o `parser.h`. Precisa do `#include "ast.h"` porque o `%union` usa `Expr*`, `Cmd*`…, e quem inclui o `parser.h` (*scanner*, `main`) tem de conhecer esses tipos. Os `extern` declaram o que é definido noutros ficheiros: `yylex`/`yylineno`/`yytext`/`yyin` no `scanner.c`, `root` no `main.c`, `yyerror` aqui em baixo. |
| 63 | `program`: `PROGRAM`=\$1 `ID`=\$2 `;`=\$3 `decls`=\$4 `begin`=\$5 `cmds`=\$6 `end`=\$7 `.`=\$8. Cria a raiz com o nome, as declarações e o corpo, e guarda-a em `root` (a regra inicial não tem `$$` útil para fora). |
| 67--70 | `decls`: nada (programa sem `var`, `NULL`) ou `VAR` seguido de `decl`. |
| 71--74 | `decl`: uma ou mais linhas `ids : type ;`, recursivo à direita: cada linha é um nó `Decl` que aponta para a seguinte (`$5`). |
| 75--78 | `type`: guarda o **código do token** (`INTEGER` ou `BOOLEAN`) como `int`. |
| 79--82 | `ids`: `a, b, c` vira a lista ligada `a → b → c` (recursiva à direita, fica pela ordem do programa). |
| 85--88 | `cmds`: comandos separados por `;`. Na l. 87, `!$1 ? $3 : !$3 ? $1 : ast_seq($1, $3)` lê-se: se o 1.º comando é vazio (`NULL`), fica só o resto; senão, se o resto é vazio, fica só o 1.º; senão cria uma sequência `C_SEQ` com os dois. Assim os comandos vazios não entram na árvore. |
| 90 | Comando vazio: permite `x := 1; end` (o `;` antes do `end`, comum em Pascal) e `begin end`. |
| 91 | Atribuição: o nome (`$1`) e a expressão (`$3`). |
| 92--93 | `if` sem e com `else`; sem `else` o 3.º campo é `NULL`. A ambiguidade entre as duas é o *dangling else*. |
| 94 | `while`: condição e corpo. |
| 95 | Bloco `begin cmds end`: **não cria nó**, devolve a sequência de dentro (`$2`). |
| 96--99 | `write(...)`, `writeln(...)`, `writeln()` e `writeln` sozinho; o 2.º argumento de `ast_write` é 1 para `writeln` (muda de linha). |
| 100--101 | `read`/`readln`: só identificadores (`ids`), não expressões: lê-se **para** variáveis. |
| 103--110 | Argumentos do `write`: lista de `arg`; um `arg` é uma expressão ou uma *string*. |
| 113--129 | **Expressões.** Gramática ambígua de propósito (`expr OP expr`), compacta; a ambiguidade é resolvida pelas l. 16--20. Cada ação cria um nó `E_OPERATION` com o código do operador e as duas subárvores. A precedência de cada regra é a do seu operador. |
| 131--139 | `factor`: os operandos (inteiro, variável, `true`, `false`, expressão entre parênteses) e os unários. `( expr )` devolve só `$2`: os parênteses não criam nó. `MINUS factor` e `NOT factor` aplicam-se a **um** `factor`: `-2*3` é `(-2)*3`. O menos unário não entra em conflito com o binário porque aparece onde se espera um operando, e o binário depois de uma expressão. |
| 142--144 | `yyerror`: o Bison chama-a num erro de sintaxe com a mensagem (por exemplo "syntax error, unexpected ID, expecting end"); acrescentamos a linha e o texto do *token* que falhou. |

\needspace{10\baselineskip}

## 5.5 `ast.h`

| Linhas | O que fazem |
|:--|:--------------------------------|
| 3--4, 134 | *Include guard*: se o *header* for incluído duas vezes no mesmo `.c` (diretamente e pelo `parser.h`), o 2.º é ignorado. |
| 7--30 | `struct _Expr`: um nó de expressão. `kind` (l. 8--15) diz que tipo de expressão é. `attr` (l. 16--29) é uma `union` com os dados de cada tipo: `value` para inteiros e booleanos, `name` para variáveis, `text` para *strings*, `op` (operador + esquerda + direita) para as binárias, `unary` (operador + filho) para as unárias. Os filhos são `struct _Expr*` porque o `typedef` só vem depois. |
| 32 | `typedef`: escrever `Expr` em vez de `struct _Expr`. |
| 35--48 | Listas ligadas: `ExprList` (argumentos do `write`) e `IdList` (nomes no `read` e nas declarações). `head` é o elemento, `tail` o resto da lista (`NULL` no fim). |
| 51--87 | `struct _Cmd`: o mesmo padrão para comandos. `C_SEQ` (`first`, `second`) liga dois comandos; `ifthen` tem `else_cmd` `NULL` se não houver `else`; `write`/`read` têm a lista e `newline` (1 para `writeln`/`readln`). |
| 92--96 | `Decl`: uma linha de declarações (lista de nomes + tipo) e o ponteiro para a linha seguinte. |
| 101--105 | `Program`: a raiz (nome, declarações, corpo). |
| 110--127 | Os protótipos dos construtores (implementados no `ast.c`). |
| 130--132 | Os protótipos das funções de impressão (no `printAbsTree.c`). |

\needspace{10\baselineskip}

## 5.6 `ast.c`

Todos os construtores seguem o mesmo padrão; basta saber explicar um:

```c
Expr* ast_operation(int operator, Expr* left, Expr* right) {
  Expr* node = (Expr*) malloc(sizeof(Expr)); // reserva memória para 1 nó
  node->kind = E_OPERATION;                 // diz que tipo de nó é
  node->attr.op.operator = operator;        // preenche os campos desse tipo
  node->attr.op.left = left;
  node->attr.op.right = right;
  return node;                              // devolve o endereço do nó
}
```

O `kind` diz que campo da `union` é válido; quem lê o nó (a impressão)
olha primeiro para o `kind` e só depois para o campo certo. Os nomes
recebidos (`char* name`) não se copiam outra vez: já são a cópia feita
pelo `strdup` no *scanner*.

\needspace{10\baselineskip}

## 5.7 `printAbsTree.c`

| Linhas | O que fazem |
|:--|:--------------------------------|
| 5 | Inclui o `parser.h` porque o operador está guardado como código de *token* (`PLUS`…) e precisa dos nomes para os comparar. |
| 7--9 | `indent`: `printf("%*s", level * 2, "")` imprime a *string* vazia com largura `level*2`, ou seja, `level*2` espaços. |
| 12--31 | `opName`: converte o código do operador no seu símbolo para imprimir. |
| 33--58 | `printExpr`: **recursiva**, em **pré-ordem**: indenta, imprime o nó e depois chama-se a si própria para os filhos com `level + 1`. O `switch (exp->kind)` escolhe o caso pelo tipo de nó. |
| 60--65 | `printIds`: percorre a lista ligada (`ids = ids->tail` até `NULL`) e imprime um `Var` por nome. |
| 70 | Comando vazio (`NULL`): não imprime nada. |
| 72--75 | `C_SEQ`: **não imprime nada** para a sequência, só os dois comandos **ao mesmo nível** (`level`, não `level + 1`). É por isso que os comandos de um bloco aparecem lado a lado. |
| 81--87 | `If`: imprime a condição, o *then* e o *else* (se for `NULL`, a l. 70 não imprime nada). |
| 108--123 | `printProgram`: o nome, as declarações (cada `Decl` com o tipo e os nomes, só se houver) e o `Corpo` a partir do nível 2. |

\needspace{10\baselineskip}

# 6. Perguntas e respostas

\needspace{10\baselineskip}

## 6.1 Compilação

**P: O que faz o `make`?** Corre
`bison --defines=parser.h -o parser.c parser.bison`,
`flex -o scanner.c scanner.flex`, compila cada `.c` para `.o` com
`-g -Wall -Wextra` e liga tudo no executável `pascal`.

**P: Porque é que o *scanner* depende do `parser.h`?** Os *tokens* são
declarados no `.bison`; o Bison gera os números deles no `parser.h` e o
*scanner* devolve esses números. Os dois têm de concordar.

**P: Para que serve o `%code requires`?** Para os `#include "ast.h"` e os
`extern` irem também para o `parser.h`, porque o `%union` usa os tipos
`Expr*`, `Cmd*`…

**P: Que ficheiros são vossos e quais são gerados?** Nossos: `.flex`,
`.bison`, `ast.h`, `ast.c`, `printAbsTree.c`, `main.c`, `Makefile`.
Gerados: `scanner.c`, `parser.c`, `parser.h` (e os `.o`).

\needspace{10\baselineskip}

## 6.2 *Scanner*

**P: Como distinguem palavras reservadas de identificadores?** As
reservadas estão antes da regra do `ID`. `if` cabe nas duas com o mesmo
comprimento: ganha a primeira (*first match*). Em `ifx` o `ID` lê mais e
ganha (*longest match*).

**P: E `<=` contra `<`?** *Longest match*.

**P: Maiúsculas?** `%option caseless`: `BEGIN`, `Begin` e `begin` dão o
mesmo *token*. O texto dos identificadores fica como foi escrito.

**P: Porque `strdup(yytext)`?** O `yytext` aponta para o *buffer* do Flex,
reescrito a cada *token*. Para o nome ficar na AST tem de ser copiado.

**P: Porque copiam o nome mas não o número?** O número é convertido para
`int` (um valor, não um ponteiro): já é uma cópia.

**P: Como sabem a linha?** `%option yylineno`: o Flex conta os `\n`.

**P: Um caracter inválido?** A última regra, `.`, apanha-o: `lexError`
escreve a linha e o caracter e faz `exit(1)`.

**P: Para que são `noyywrap`, `nounput`, `noinput`?** Ver §5.3, l. 15.

\needspace{10\baselineskip}

## 6.3 Gramática e precedências

**P: Que tipo de *parser* gera o Bison?** LALR(1): ascendente, lê da
esquerda para a direita e decide entre *shift* e *reduce* olhando para 1
*token* à frente (§2.5).

**P: Qual a diferença para um *parser* descendente (LL, recursivo)?** O
descendente começa no símbolo inicial e tenta adivinhar a regra a partir
do próximo *token*; não aceita recursividade à esquerda nem esta gramática
ambígua das expressões. O ascendente (LR) junta *tokens* até reconhecer o
lado direito de uma regra; aceita mais gramáticas e as precedências
resolvem a ambiguidade.

**P: A gramática das expressões é ambígua. Como resolvem?** Com `%left`,
`%nonassoc` e `%precedence` (l. 16--20): num conflito *shift/reduce* o Bison
compara a precedência da regra (a do seu último terminal) com a do *token*
seguinte: *token* com mais → *shift*; com menos → *reduce*; igual →
`%left` reduz, `%nonassoc` dá erro. Em `2 + 3 * 4`, com `expr + expr` na
pilha e `*` à frente, `*` tem mais: *shift*, e o `3 * 4` fica mais abaixo.

**P: Porquê uma gramática ambígua com precedências e não a versão com
`expr`/`termo`/`fator`?** As duas são válidas; a das aulas com níveis
(`expr: expr + termo | termo`…) não é ambígua mas precisa de um
não-terminal por nível de prioridade. Com as precedências a gramática fica
mais curta e legível, e a árvore é a mesma.

**P: Porque é que `a < b and c` dá `a < (b and c)`?** No Pascal o `and` tem
mais prioridade do que os relacionais. É por isso que em Pascal se escreve
`(a > b) and (c > d)` com parênteses (como no `exemplo2.pas`).

**P: E `a < b < c`?** `%nonassoc`: erro. Faz sentido porque `a < b` é
booleano e compará-lo com `c` não tem significado.

**P: Como resolvem o *dangling else*?** Em
`if a then if b then x else y`, depois de `if b then x` vem `else`: o
*parser* pode reduzir `IF expr THEN cmd` (o `else` iria para o `if` de
fora) ou fazer *shift* do `else` (fica no de dentro). A regra sem `else`
tem a precedência do seu último terminal, `THEN`; o *token* é `ELSE`, que
tem mais (l. 17 vem depois da 16): *shift*. O `else` liga-se ao `if` mais
próximo, como em Pascal.

**P: A gramática tem conflitos?** Não: `bison -Wall` não dá conflitos nem
avisos. Sem as precedências haveria dezenas de conflitos *shift/reduce*.

**P: Porque o menos unário e o `not` estão no `factor`?** Para se
aplicarem só ao operando seguinte sem mais uma precedência: `-2*3` é
`(-2)*3`. Em Pascal o menos unário tem a precedência do `+` (`-a*b` seria
`-(a*b)`); o valor é o mesmo, só a árvore muda. Foi uma simplificação.

**P: Porque é que as listas são recursivas à direita?** `ids: ID | ID COMMA
ids` constrói a lista pela ordem do programa sem a inverter. O custo: o
Bison empilha a lista toda antes de reduzir (a pilha cresce com o tamanho
da lista); à esquerda a pilha é constante mas a lista sairia ao contrário.
Para programas pequenos não importa.

**P: O que são `%union` e `%type`?** O `%union` diz que tipos de valor um
símbolo pode ter; o `%type` diz qual usa cada símbolo. Assim `$1`, `$3` e
`$$` têm o tipo C certo.

**P: O que é `$$`, `$1`, `$3`?** `$$` é o valor do lado esquerdo (o nó que
se cria); `$1`, `$2`… os valores dos símbolos do lado direito, por ordem.

**P: Quando corre uma ação?** Quando o *parser* **reduz** a regra, ou seja,
depois de já ter reconhecido todos os símbolos do lado direito. Por isso
os filhos já existem quando o pai é criado (a árvore faz-se de baixo para
cima).

**P: `write`/`read` são comandos ou expressões?** Comandos (em Pascal são
procedimentos).

\needspace{10\baselineskip}

## 6.4 A AST

**P: Como representam a AST?** Como nas aulas: cada categoria é uma
`struct` com uma etiqueta (`kind`, um `enum`), uma `union` com os campos de
cada alternativa (`attr`) e um construtor `ast_*` que faz `malloc` e
preenche os campos.

**P: Porquê uma `union`?** Cada nó só usa os campos da sua alternativa: um
inteiro não precisa de `left`/`right`. A `union` partilha a memória e o
`kind` diz qual campo é válido.

**P: Como guardam o operador?** Pelo código do *token* (`PLUS`, `LT`…); na
impressão o `opName` converte-o no símbolo.

**P: Diferença entre árvore de derivação e AST?** §2.6.

**P: Como representam `c1; c2; c3`?** `C_SEQ` encadeados à direita:
`SEQ(c1, SEQ(c2, c3))`. Na impressão a sequência não aparece.

**P: Porque não separam expressões aritméticas e booleanas na gramática?**
Em `x := a` o *parser* não sabe se `a` é inteira ou booleana. Isso
verifica-se na análise semântica, com a tabela de símbolos (2.ª parte).

**P: Como imprimem a árvore?** Em pré-ordem, recursivamente, com 2 espaços
por nível (§5.7).

**P: A memória é libertada?** Não: a árvore é usada até ao fim e o sistema
operativo liberta tudo quando o programa termina. Num compilador completo
a AST passaria às fases seguintes.

\needspace{10\baselineskip}

## 6.5 Erros

**P: Como mostram os erros de sintaxe?** O Bison chama `yyerror`, que
escreve "Linha N: mensagem - 'texto'". Com `parse.error verbose` a
mensagem diz o *token* inesperado e os esperados.

**P: Porque é que no `erro.pas` o erro aparece na linha 4?** `x := 1 +`
acaba na linha 3, mas o *parser* só sabe que falta o operando quando lê o
*token* seguinte, o `end` da linha 4. A mensagem não diz "expecting"
porque há demasiados *tokens* possíveis (qualquer início de expressão).

**P: Recuperam de erros?** Não: param no primeiro. Recuperar seria
acrescentar regras com o *token* especial `error` do Bison (por exemplo
`cmd: error SEMICOLON`) para saltar até ao próximo `;` e continuar.

**P: Códigos de saída?** 0 se correu bem; 1 se houve erro.

\needspace{10\baselineskip}

## 6.6 Limitações (dizer com calma, antes que ele as encontre)

| Limitação | O que dizer |
|---|---|
| **`if x then else y := 1` imprime igual a `if x then y := 1`** | O *then* vazio é `NULL` e a impressão não o mostra, por isso o *else* aparece no lugar do *then*. A AST está certa (`then_cmd` é `NULL`); só a impressão é ambígua. Correção: no `C_IF` do `printCmd` (l. 81--87), se `then_cmd` é `NULL` e há *else*, imprimir uma linha `Vazio`. |
| Não há análise semântica | `x := true + 1` e variáveis não declaradas passam. É a 2.ª parte: tabela de símbolos. |
| Identificadores distinguem maiúsculas | `X` e `x` ficam nomes diferentes na AST, mas em Pascal são a mesma variável. Na semântica, comparar em minúsculas. |
| Números grandes transbordam | `atoi("99999999999")` dá lixo sem aviso. Correção: `strtol` e erro se passar de `INT_MAX`. |
| *Strings* só no `write` | Não há tipo `string` no subconjunto. |
| `/` tratado como os outros | Em Pascal dá um real; sem `real` só faz sentido `div`. |
| Não se verifica o `malloc` | Se faltasse memória daria `NULL`; para estes programas não acontece. |
| Aviso ao compilar `scanner.c` | Está no código gerado pelo Flex. |

\needspace{10\baselineskip}

## 6.7 "E se…?"

**P: Como acrescentavam o `repeat … until`?** *Tokens* `REPEAT`/`UNTIL` no
*scanner* (antes do `ID`) e no `%token`; regra
`cmd: REPEAT cmds UNTIL expr { $$ = ast_repeat($2, $4); }`; um `C_REPEAT`
no `ast.h`, o construtor no `ast.c` e um `case` no `printCmd`.

**P: E um `for`?** `FOR ID ASSIGN expr TO expr DO cmd`: um nó com a
variável, o início, o fim e o corpo. Mesmos quatro sítios.

**P: E o tipo `real`?** No *scanner* `[0-9]+"."[0-9]+` com `atof` (em `3.5`
o *longest match* escolhe esta à dos inteiros); um `E_REAL` na AST com um
campo `double`; `REAL` em `type`.

**P: Mudar a prioridade do `and` para baixo dos relacionais?** Passar `AND`
para uma linha `%left` **antes** da dos relacionais (l. 18), ou seja, com
menos prioridade.

**P: O que vem a seguir?** Análise semântica: percorrer a AST com uma
tabela de símbolos (nome → tipo) para verificar declarações e tipos; depois
gerar código (por exemplo código de 3 endereços).

**P: Porque C e não Haskell?** *(Dizer a razão verdadeira.)* O Flex e o
Bison são os das aulas práticas e o código de apoio às ASTs era em C.

\needspace{10\baselineskip}

# 7. Quem diz o quê (Gonçalo e Matilde)

O professor pode perguntar a qualquer um sobre qualquer parte; a divisão
serve para cada um responder primeiro na sua. **Os dois leem a §2 e a §6.6.**

| Tema | Matilde | Gonçalo |
|---|:-:|:-:|
| Abertura e compilação (`make`, ficheiros gerados) | **X** | |
| *Scanner* (§5.3, §6.2), erros lexicais | **X** | |
| *Parser*, `%union`/`%type`, `$$`/`$1` (§5.4) | | **X** |
| Precedências, *dangling else*, *shift/reduce* (§2.5, §6.3) | | **X** |
| AST e impressão (§5.5--5.7), erros de sintaxe | | **X** |
| Limitações e "e se" | **X** | **X** |
| Como dividiram o trabalho | *combinar antes e dizer a verdade* | |
