---
title: "Compiladores --- Guião do Trabalho Prático 1"
author: "Gonçalo Sousa"
date: "Enunciado: Trabalho/Enunciado_TP1.pdf (outubro 2026)"
---

## O que o enunciado pede

| | |
|:--|:--|
| **Tarefa** | *scanner* (análise lexical) + *parser* (análise sintática) para um subconjunto de **Pascal**; o *parser* devolve e **imprime a AST** do programa lido |
| **Subconjunto** | expressões aritméticas e booleanas, `write` (saída) e `read` (entrada); atribuição, `if then else`, ciclo `while` |
| **Grupo** | individual ou 2 alunos **da mesma turma prática** |
| **Prazo** | **8 de novembro de 2026**, até ao fim do dia (o processo de entrega será anunciado) |
| **Entrega** | um **`COMP_TP1.zip`** (só `.zip`) com **todo o código** + **`README.pdf`** (README breve do projeto) |
| **Defesa** | **obrigatória**, na aula prática da semana de **9 de novembro** |

O enunciado não fixa a linguagem: servem **Haskell (Alex + Happy)** ou **C
(Flex + Bison)**, as duas dos labs. A recomendação é **Haskell**: a AST
imprime-se com `deriving Show`, e a 2.ª parte do trabalho (tabela de
símbolos e tipos, Aulas 8--9) faz-se com `Data.Map`, como nos slides. Em C
o molde é o lab de ASTs (`Praticas/Semana_4/Abstract_Syntax_Trees`).

## Decisões a fixar (e a escrever no README)

1. **Forma de um programa.** Em Pascal um programa é
   `program Nome; var ...; begin ... end.` Aceitar este cabeçalho e a
   secção `var` (só `integer` e `boolean`) faz os testes serem Pascal a
   sério; a 2.ª parte vai precisar das declarações.
2. **`write`/`read`.** O enunciado põe-nos nas expressões, mas em Pascal
   são **procedimentos**, usados como comandos: `writeln(e1, 'texto', e2)`
   e `readln(x)`. Tratá-los como comandos e dizê-lo no README (confirmar
   com o professor numa aula). Aceitar `write`/`read` além de
   `writeln`/`readln` custa duas regras.
3. **Maiúsculas.** Pascal não as distingue (`BEGIN` = `begin`): o *scanner*
   reconhece qualquer palavra como identificador e compara-a **em
   minúsculas** com a lista de palavras reservadas.
4. **Divisão.** Em Pascal `/` dá um real; com só inteiros, usar `div` e
   `mod`.
5. **Menos unário.** Em Pascal tem a precedência do `+` (`-a mod 7` =
   `-(a mod 7)`); a solução mais simples dá-lhe a maior precedência. Dizer
   qual se escolheu.

## Passo 1 --- *Scanner*

*Tokens* (uma regra por linha; Flex: *first match*, por isso os de dois
carateres e as palavras reservadas vêm antes do identificador):

| Categoria | *Lexemas* |
|:--|:--|
| ignorar | espaços, `\n`, comentários `{ ... }` e `(* ... *)` |
| palavras reservadas | `program var begin end if then else while do integer boolean true false writeln readln div mod and or not` |
| operadores | `:=` `+` `-` `*` `=` `<>` `<` `<=` `>` `>=` |
| pontuação | `(` `)` `;` `:` `,` `.` |
| literais | inteiro `[0-9]+`; *string* `'[^']*'` (sem as aspas) |
| identificador | `[a-zA-Z][a-zA-Z0-9_]*` |

**Verificar:** imprimir a lista de *tokens* de um programa de teste antes
de passar ao *parser*.

## Passo 2 --- AST

Um construtor por **operação**, sem parêntesis nem `;` (Aula 6):

```haskell
type Ident = String
data Program = Program Ident [(Ident, Type)] Stm
data Type    = TInt | TBool
data Stm     = Assign Ident Expr
             | If Expr Stm (Maybe Stm)        -- else opcional
             | While Expr Stm
             | Block [Stm]                    -- begin ... end
             | Write [Arg] | Read Ident
data Arg     = ArgExpr Expr | ArgStr String
data Expr    = Num Int | BoolLit Bool | Var Ident
             | BinOp BinOp Expr Expr | UnOp UnOp Expr
data BinOp   = Add | Sub | Mul | Div | Mod | And | Or
             | Eq | Ne | Lt | Le | Gt | Ge
data UnOp    = Not | Neg
```

Em C: um `struct` com *tag* + `union` por categoria (`Expr`, `Stm`),
funções `mk_...` e um `print_...` recursivo com `switch` (receita do lab
de ASTs).

## Passo 3 --- Gramática

```
Program  → program id ; Decls Compound .
Decls    → ε | var DeclList
DeclList → Decl | DeclList Decl
Decl     → IdList : Type ;
IdList   → id | IdList , id
Type     → integer | boolean
Compound → begin StmList end
StmList  → Stm | StmList ; Stm
Stm      → ε | id := Expr | if Expr then Stm | if Expr then Stm else Stm
         | while Expr do Stm | Compound
         | writeln ( Args ) | readln ( id )
Args     → Arg | Args , Arg
Arg      → Expr | string
Expr     → num | true | false | id | ( Expr ) | not Expr | - Expr
         | Expr op Expr          (op: + - * div mod and or = <> < <= > >=)
```

- **`;` separa** comandos (não termina): por isso `Stm → ε`, que deixa
  escrever `...; end` como em Pascal.
- **Precedências** (da menor para a maior), com Pascal: `then` <
  `else` (resolve o ***dangling else***, Aula 6) < relacionais
  `%nonassoc` < `+ - or` `%left` < `* div mod and` `%left` < `not` e
  menos unário. Consequência de Pascal: `a < b and c` lê-se
  `a < (b and c)`, por isso as condições compostas precisam de
  parêntesis: `(n >= 0) and (n < 10)`.
- Com estas declarações a gramática **não tem conflitos** (confirmado com
  Bison 3.8 e com `happy -i`: o `.info` não lista nenhum). Se aparecer um,
  ler o `.info`/`-Wcounterexamples` e corrigir antes de seguir.
- Ações semânticas: cada regra constrói o nó da AST (`Program $2 $4 $5`,
  `BinOp Add $1 $3`, ...). Com `Stm → ε` é cómodo que `Stm` devolva uma
  lista (vazia ou com um comando) e `StmList` as concatene.

## Passo 4 --- Ligar e imprimir

`main` lê o ficheiro (ou a entrada padrão), corre *scanner* → *parser* e
**imprime a AST**. Num erro sintático, uma mensagem com os *tokens* seguintes
(ou a linha, com `%locations` no Bison / *wrapper* `posn` no Alex).
Entrega mais limpa com um *pretty-printer* indentado, mas `print` já
cumpre o enunciado. Saída esperada para o programa de teste abaixo
(abreviada):

```
Program "fatorial" [("n",TInt),("f",TInt),("ok",TBool)] (Block [Read "n",
  Assign "f" (Num 1), Assign "ok" (BinOp And (BinOp Ge (Var "n") (Num 0))
  (UnOp Not (BinOp Gt (Var "n") (Num 12)))), If (Var "ok") (While ...) ...
```

## Passo 5 --- Testes

Uma pasta `testes/` com programas que **cobrem cada regra**, e um *script*
(ou alvo do `Makefile`) que os corre todos.

```pascal
program Fatorial;
var n, f : integer;
    ok : boolean;
begin
  { le n e calcula n! }
  readln(n);
  f := 1;
  ok := (n >= 0) and not (n > 12);
  if ok then
    while n > 1 do
    begin
      f := f * n;
      n := n - 1
    end
  else
    writeln('fora do intervalo');
  writeln('resultado: ', f, -f mod 7 + 2 * 3);
end.
```

Mais casos: precedência (`1 + 2 * 3`, `(1 + 2) * 3`, `10 - 4 - 3` à
esquerda); `if` encaixados com um só `else` (o `else` vai para o `if`
mais próximo); `begin end` vazio e `;` antes de `end`; palavras em
maiúsculas; comentários dos dois tipos. **Erros** que têm de ser
rejeitados: `x := 1 + ;`, `if x then` sem comando seguido de `else else`,
falta do `.` final.

## Passo 6 --- README.pdf e entrega

O README (escrito em Markdown e convertido com
`pandoc README.md -o README.pdf`) diz:

- autores, número e turma prática;
- como compilar e correr (`make`; `./pascal < testes/fatorial.pas`);
- o subconjunto aceite e as **decisões** da secção 2;
- a estrutura dos ficheiros (*scanner*, *parser*, AST, `main`) e o formato
  da AST impressa;
- limitações conhecidas.

Antes de entregar: `make clean`, depois `zip -r COMP_TP1.zip
<pasta-do-projeto> README.pdf`; descompactar noutra pasta e compilar de
novo para confirmar que nada falta.

## Preparar a defesa

Saber explicar, com o vosso código à frente: o que faz o *scanner* e
porque as palavras reservadas vêm antes do identificador; a ordem das
precedências e o que cada `%left`/`%nonassoc` resolve (Aula 6); porque não
há conflito no *dangling else*; a diferença entre a árvore concreta e a
AST que imprimem; como se acrescentaria um comando novo (ex.: `repeat ...
until`, uma regra na gramática + um construtor na AST).

## Calendário sugerido

| Até | Feito |
|:--|:--|
| 28 out | decisões fixadas; *scanner* a listar *tokens* |
| 1 nov | AST + gramática das expressões e atribuição, sem conflitos |
| 4 nov | `if`, `while`, blocos, `writeln`/`readln`; impressão da AST |
| 6 nov | testes todos a passar, mensagens de erro |
| 8 nov | README.pdf, `COMP_TP1.zip` testado e entregue |
