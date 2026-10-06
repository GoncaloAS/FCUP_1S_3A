---
title: "Compiladores --- Folha de revisão"
author: "Gonçalo Sousa"
date: "Aulas 1--6. As receitas do resumo, sem exemplos: para rever antes do exame."
---

## Análise lexical

**Expressões regulares.** $a$, $\varepsilon$, $M\mid N$, $MN$, $M^*$.
Prioridade: $^*$ > concatenação > $\mid$ ($ab|c = (ab)|c$). Abreviaturas:
`M?` $= M\mid\varepsilon$, `M+` $= MM^*$, `[abc]`, `[a-z]`, `[^a-z]`, `.`
(tudo menos `\n`), `"a+"` (literal).

**Parar no primeiro terminador**: proibir o terminador no meio, ex.:
`"<!--" ([^-]|"-"[^-])* "-->"`. Nunca `"/*" .* "*/"` (apanha do primeiro
`/*` ao último `*/`).

**Thompson (ER → NFA)**, um fragmento com uma entrada e uma saída por
sub-expressão:

| | Construção |
|:-----|:------------------------|
| $\sigma$ | entrada $\xrightarrow{\sigma}$ saída |
| $AB$ | saída de $A$ ligada à entrada de $B$ |
| $A\mid B$ | entrada nova $\xrightarrow{\varepsilon}$ $A$ e $B$; saídas de $A$ e $B$ $\xrightarrow{\varepsilon}$ saída nova |
| $A^*$ | entrada nova $\xrightarrow{\varepsilon}$ $A$ e $\xrightarrow{\varepsilon}$ saída nova; saída de $A$ $\xrightarrow{\varepsilon}$ entrada de $A$ e saída nova |

**Subconjuntos (NFA → DFA).**

1. $S_0 = \text{closure}(\{q_0\})$ (tudo o que se alcança só por $\varepsilon$).
2. Para cada estado $S$ ainda não tratado e cada símbolo $\sigma$:
   $\text{move}(S,\sigma)$ = destinos das transições $\sigma$ que saem de
   estados de $S$; depois $\delta'(S,\sigma) = \text{closure}(\text{move})$.
   Vazio: sem transição. Conjunto novo: estado novo.
3. Finais: os conjuntos que contêm um final do NFA.

**Minimização**: estados com as mesmas transições para todos os símbolos e
o mesmo estatuto (final ou não) fundem-se.

**Geradores (Alex/Flex)**: *longest match* primeiro, depois *first match*
→ palavras reservadas **antes** da regra de identificadores. Alex:
`padrão { \s -> Token }`, `alexScanTokens`. Flex: `padrão { ação C }`,
`yytext`, `yylex()`.

## Gramáticas

$G=(\Sigma, N, S, P)$, produções $X\to\alpha$. $L(G) = \{w\in\Sigma^* :
S\Rightarrow^* w\}$. Derivação **mais à esquerda** (LL) / **mais à
direita** (LR, ao contrário). **Ambígua** = uma palavra com **duas
árvores** diferentes (duas derivações não chegam).

**ER → gramática**: $rs$ → um lado direito $r\,s$; $r\mid s$ → $X\to
r\mid s$; $r^*$ → $X\to rX\mid\varepsilon$; $r^+$ → $X\to rX\mid r$.

**Desambiguar expressões**: $E\to E+T\mid T$, $T\to T*F\mid F$,
$F\to\texttt{num}\mid(E)$. Recursão à esquerda → associatividade à
esquerda; um nível por precedência (o mais "fundo" liga mais).

**Dangling else**: o `else` liga ao `if` mais próximo. Gramática com $M$
(*matched*) / $U$ (*unmatched*), ou deixar e fazer *shift* no conflito.

## Análise LR

**Ações**: *shift* (empilha o terminal), *reduce* $X\to\gamma$ (tira
$\gamma$ do topo, empilha $X$). Gramática aumentada $S'\to S\,\$$.

**Tabela**: $s\,q$, $r\,k$, $g\,q$ (só em não-terminais), $a$, vazia =
erro. **Reduce $k$** ($X\to\alpha_1..\alpha_n$): tira $n$ estados, olha
para o estado do topo, empilha o $g$ da coluna $X$ desse estado.

**Items LR(0)**: $A\to\beta\bullet\gamma$ ($\beta$ está no topo). Inicial
$A\to\bullet\gamma$; completo $A\to\gamma\bullet$. Comprimento $n$ dá
$n+1$ items; $A\to\varepsilon$ dá só $A\to\bullet$.

**Autómato**: estado inicial $\text{fecho}(\{S'\to\bullet S\,\$\})$.

- **fecho(I)**: para cada item com o ponto antes de um não-terminal $B$,
  junta todos os $B\to\bullet\beta$; repete.
- **goto(I, X)**: items de $I$ com o ponto antes de $X$, avança o ponto,
  aplica o fecho.

**Tabela LR(0)**: terminal $i\xrightarrow{t}j$ → $s\,j$; não-terminal
$i\xrightarrow{X}j$ → $g\,j$; item completo da produção $k$ → $r\,k$ em
**todas** as colunas terminais; $S'\to S\bullet\$$ → $a$ na coluna \$.
Uma entrada com duas ações = **conflito** (shift/reduce ou
reduce/reduce).

**FIRST e FOLLOW.** FIRST($X_1..X_n$) = FIRST($X_1$), mais FIRST($X_2$) se
$X_1$ anulável, etc. FOLLOW: \$ $\in$ FOLLOW($S$); para cada $X\to\alpha
A\beta$: FIRST($\beta$) ⊆ FOLLOW($A$); se $\beta$ vazio ou anulável,
FOLLOW($X$) ⊆ FOLLOW($A$). Repetir até estabilizar.

**SLR(1)**: igual à LR(0), mas o *reduce* de $A\to\gamma\bullet$ só nas
colunas de FOLLOW($A$).

**LR(1)**: items $(A\to\alpha\bullet\beta,\ a)$; a transição-$\varepsilon$
de $(A\to\alpha\bullet B\gamma, a)$ vai para $(B\to\bullet\beta, b)$ com
$b\in$ FIRST($\gamma a$); *reduce* só com o *look-ahead* $a$. **LALR(1)**
= LR(1) com os estados de items LR(0) iguais fundidos (é o que os
geradores usam).

Gramática ambígua ⇒ conflitos sempre. Conflitos ⇏ ambígua.

## Geradores LR (Happy / Bison)

| | Happy | Bison |
|:------|:----------|:----------|
| Ação | expressão: `{ $1 + $3 }` | bloco: `{ $$ = $1 + $3; }` |
| Valor de um terminal | `$$` no padrão de `%token` | o *lexer* põe em `yylval` |
| Tipos diferentes | inferidos | `%union` + `%token <num>` + `%type <exp>` |
| Função | `%name parser`, recebe `[Token]` | `yyparse()`, chama `yylex()` |
| Relatório | `happy -i` → `.info` | `bison --report=all` → `.output` |

`$1`, `$2`, ... = valores do lado direito por ordem. A ação corre no
**reduce**, de baixo para cima na árvore. Terminais de um carácter
(`'+'`) usam o código ASCII (Flex: `return yytext[0];`).

**Conflitos**: por omissão, **shift** (tudo associa à direita, com a mesma
precedência). Declarações antes do `%%`, **cada linha com mais
precedência do que as anteriores**: `%left`, `%right`, `%nonassoc`.

**Regra**: a precedência da regra $R$ é a do seu **último terminal**;
*token* $a$ com mais precedência → *shift*; menos → *reduce*; igual →
`%left` *reduce*, `%right` *shift*, `%nonassoc` erro.

## Sintaxe abstrata

**Concreta**: um nó por símbolo da derivação. **AST**: um nó por
operação, sem parêntesis, palavras reservadas nem não-terminais de
desambiguação; as ações semânticas constroem-na logo.

| | Representação | Distinguir casos |
|:-----|:-----------------|:-----------------|
| Haskell | `data` com um construtor por alternativa | encaixe de padrões |
| C | `struct` com *tag* (`enum`) + `union`; funções `mk_...` | `switch` na *tag* |
| Java | classe abstrata + uma subclasse por alternativa | `instanceof` + *cast* (ou *visitor*) |

Preferir a abordagem funcional: o compilador avisa se faltar um caso.
