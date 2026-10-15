---
title: "Lógica Computacional --- Resumo Teórico"
author: "Gonçalo Sousa"
date: "Atualizado: Semana 5 (Aulas 1--10)"
---

<!-- processado: Teoricas/Aula_01.pdf, Teoricas/Aula_02.pdf, Teoricas/Aula_03.pdf, Teoricas/Aula_04.pdf, Teoricas/Aula_05-06.pdf, Teoricas/Aula_07.pdf, Teoricas/Aula_08.pdf, Teoricas/Aula_09-10.pdf -->

*O sinal † marca matéria que não está nos slides mas faz falta para as
práticas.*

# Aula 1 --- Introdução à Lógica e Sintaxe da Lógica Proposicional

## O que é a lógica

A **lógica** estuda os princípios que distinguem um raciocínio correto de
um incorreto. O que conta é a **forma** do argumento: "todos os homens são
mortais; Sócrates é homem; logo Sócrates é mortal" é válido, mas "todos os
homens são mortais; Sócrates era mortal; logo todos os homens são
Sócrates" não é, apesar de parecido.

Uma **lógica** tem três partes:

1. uma **linguagem** (sintaxe): um alfabeto e regras para construir
   *fórmulas*;
2. uma **semântica**: o que quer dizer uma fórmula ser verdadeira (pode
   haver várias para a mesma sintaxe);
3. um **sistema de dedução**: regras para obter fórmulas a partir de
   outras. Quer-se **correto** (*sound*: tudo o que se deduz é verdadeiro)
   e, se possível, **completo** (tudo o que é verdadeiro se deduz).

O curso trata a **lógica clássica** (proposicional e de primeira ordem),
em que cada proposição é verdadeira ou falsa, e só uma das duas
(*terceiro excluído*). Há outras: de ordem superior, sub-estruturais
(ex.: a intuicionista, onde $\neg\neg A \not\Leftrightarrow A$) e modais
(a verdade depende de um "mundo", ex.: do tempo). A lógica aparece na
informática em circuitos digitais, inteligência artificial, autómatos,
complexidade, programação lógica (Prolog), sistemas de tipos, verificação
formal, *SAT/SMT solvers* e assistentes de prova (Coq, Isabelle, Agda).

## Proposições

::: {.definicao title="--- Proposição"}
Uma **proposição** é uma frase declarativa à qual se pode atribuir um
valor de verdade, **V** ou **F**, e só um. Perguntas, ordens, expressões
sem verbo e frases com variáveis livres (cujo valor depende de algo não
fixado) **não são proposições**.
:::

::: {.exemplo title="--- Exercício 1.1 (lab, proplogic.pdf), 5 das 8 alíneas"}
**(a)** "O Porto é a capital de Portugal." --- É proposição, **F**.

**(d)** "$1+2+3$" --- **Não é proposição**: é um termo (um número), não
uma afirmação.

**(c)** "Hei de comparar-te a um dia de verão?" --- **Não é proposição**:
é uma pergunta.

**(g)** "$x+y$ é um número par." --- **Não é proposição**: $x$ e $y$ são
**variáveis livres**; é verdade para $x=y=1$ e falso para $x=1,y=2$.

**(h)** "Existe um $x$ tal que $7+x$ é um número par." --- É proposição,
**V** ($x=1$). O quantificador "existe" **fecha** a variável: a frase já
não depende de nenhum $x$ de fora. (A diferença entre variável livre e
quantificada fica formal na lógica de primeira ordem.)

As alíneas (b), (e) e (f) são a mesma ideia de (a).
:::

## Conectivos lógicos

Cada proposição simples é uma **variável proposicional** ($p, q, r,
\dots$); as compostas obtêm-se com **conectivos**:

| Conectivo | Símbolo | Aridade | Outros símbolos |
|---|---|---|---|
| Conjunção ("e") | $\land$ | 2 | `&`, `&&`, $\cdot$ |
| Disjunção ("ou") | $\lor$ | 2 | `|`, `+` |
| Negação ("não") | $\neg$ | 1 | $\sim$, $\bar{\ }$, `!` |
| Implicação ("se...então") | $\to$ | 2 | $\Rightarrow$, $\supset$ |

## Linguagem da lógica proposicional

::: {.definicao title="--- Alfabeto e fórmulas"}
**Alfabeto:** um conjunto **numerável** de variáveis proposicionais
$\mathcal{V}_{Prop} = \{p, q, r, \dots, p_1, \dots\}$, os conectivos
$\land, \lor, \neg, \to$ e os parêntesis `(` e `)`.

O conjunto das **fórmulas** ($\phi, \psi, \theta, \dots$) define-se
indutivamente:

1. uma variável proposicional $p$ é uma fórmula;
2. se $\phi$ é fórmula, $(\neg\phi)$ é fórmula;
3. se $\phi$ e $\psi$ são fórmulas, $(\phi \land \psi)$, $(\phi \lor \psi)$
   e $(\phi \to \psi)$ são fórmulas.

Nada mais é fórmula. Ex.: $((p \land (\neg p)) \to (\neg(p \land (q \lor r))))$.
:::

A definição indutiva dá a **árvore sintática** de uma fórmula: a raiz é o
conectivo principal e os filhos são as fórmulas que ele combina, até às
variáveis (as folhas).

### Convenção para omitir parêntesis

- os parêntesis mais exteriores podem omitir-se;
- prioridade: $\neg$ > $\land$ > $\lor$ > $\to$;
- $\land$ e $\lor$ associam **à esquerda**; $\to$ associa **à direita**.

::: exemplo
- $\phi \land \psi \lor \theta$ abrevia $((\phi \land \psi) \lor \theta)$.
- $p \land \neg p \to \neg(p \land (q \lor r))$ é
  $((p \land (\neg p)) \to (\neg(p \land (q \lor r))))$.
- $p \to q \to r$ é $p \to (q \to r)$.
:::

::: {.definicao title="--- Subfórmula"}
As **subfórmulas imediatas** de $\psi$ são: nenhuma, se $\psi$ é uma
variável; $\phi$, se $\psi = \neg\phi$; $\phi$ e $\psi'$, se
$\psi = \phi \land \psi'$, $\phi \lor \psi'$ ou $\phi \to \psi'$.

$\phi$ é **subfórmula** de $\psi$ se é subfórmula imediata de $\psi$, ou
se é subfórmula de uma subfórmula de $\psi$ (fecho transitivo). Por
convenção, $\psi$ é subfórmula de si própria.
:::

**Método† para a árvore e as subfórmulas.** Primeiro repõem-se os
parêntesis pela convenção, e só depois se desenha a árvore. O conectivo
**principal** (a raiz) é o de **menor prioridade** entre os que estão fora
de parêntesis. As subfórmulas leem-se nos nós da árvore (cada nó é uma;
uma fórmula repetida conta uma vez).

::: {.exemplo title="--- Exercício 1.3(a) (lab, proplogic.pdf)"}
**Fórmula:** $p \land \neg q \to \neg p$.

**Parêntesis.** $\neg$ primeiro: $\neg q$ e $\neg p$. Depois $\land$:
$p \land (\neg q)$. Por fim $\to$, o de menor prioridade, que é a raiz
(apesar de o $\land$ aparecer mais à esquerda):
$$\big(p \land (\neg q)\big) \to (\neg p)$$

::: center
![Árvore sintática de p ∧ ¬q → ¬p](figuras/arvore_1_3a.pdf){height=4.3cm}
:::

**Subfórmulas:** $p \land \neg q \to \neg p$, $p \land \neg q$, $\neg p$,
$p$, $\neg q$, $q$.
:::

::: {.exemplo title="--- Exercício 1.3(c) (lab, proplogic.pdf)"}
**Fórmula:** $\neg(s \to (\neg(p \to (q \lor \neg s))))$. Os parêntesis já
estão explícitos; nomeiam-se as subfórmulas de dentro para fora:
$A = q \lor \neg s$, $B = p \to A$, $C = \neg B$, $D = s \to C$,
$E = \neg D$ (a fórmula toda).

::: center
![Árvore sintática de ¬(s → ¬(p → (q ∨ ¬s)))](figuras/arvore_1_3c.pdf){height=7.6cm}
:::

**Subfórmulas:** $E$, $D = s \to \neg(p \to (q\lor\neg s))$, $s$,
$C = \neg(p \to (q \lor \neg s))$, $B = p \to (q \lor \neg s)$, $p$,
$A = q \lor \neg s$, $q$, $\neg s$. ($s$ aparece em dois nós da árvore,
mas lista-se uma vez.)
:::

::: {.exemplo title="--- Exercício 1.3(e) (lab, proplogic.pdf)"}
**Fórmula:** $(p \to q) \land (\neg r \to (q \lor (\neg p \land r)))$. O
conectivo principal é o $\land$ exterior, com dois ramos:
$L = p \to q$ e $M = \neg r \to M_2$, onde $M_2 = q \lor M_1$ e
$M_1 = \neg p \land r$.

::: center
![Árvore sintática de (p → q) ∧ (¬r → (q ∨ (¬p ∧ r)))](figuras/arvore_1_3e.pdf){height=6.6cm}
:::

**Subfórmulas:** a fórmula toda, $L = p \to q$, $p$, $q$,
$M = \neg r \to (q \lor (\neg p \land r))$, $\neg r$, $r$,
$M_2 = q \lor (\neg p \land r)$, $M_1 = \neg p \land r$, $\neg p$.
:::

::: {.pratica title="--- Linguagem e árvores sintáticas (proplogic.pdf)"}
- **1.2** --- traduzir cada fórmula para português. É mecânico: lê cada
  conectivo com a tabela da secção "Conectivos lógicos" ($\to$ = "se...
  então"). Atenção à (d) vs. (e) vs. (f): são três implicações diferentes,
  não digas o mesmo por palavras diferentes.
- **1.3 (b)** e **(d)** --- árvore sintática e subfórmulas, mesma técnica de
  (a)/(c)/(e) acima. Na (b) compara com a (a): os parêntesis mudam o
  conectivo principal.
:::

## Semântica: valorações e tabelas de verdade

::: {.definicao title="--- Valoração"}
Uma **valoração** é uma função $v : \mathcal{V}_{Prop} \to \{V, F\}$.
Estende-se às fórmulas por indução na estrutura:

1. $v(p)$ já está definido, para $p \in \mathcal{V}_{Prop}$;
2. $v(\neg\phi) = V$ sse $v(\phi) = F$;
3. $v(\phi \land \psi) = V$ sse $v(\phi) = V$ e $v(\psi) = V$;
4. $v(\phi \lor \psi) = V$ sse $v(\phi) = V$ ou $v(\psi) = V$;
5. $v(\phi \to \psi) = F$ sse $v(\phi) = V$ e $v(\psi) = F$.
:::

| $\phi$ | $\neg\phi$ | | $\phi$ | $\psi$ | $\phi\land\psi$ | | $\phi$ | $\psi$ | $\phi\lor\psi$ | | $\phi$ | $\psi$ | $\phi\to\psi$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F | V | | F | F | F | | F | F | F | | F | F | V |
| V | F | | F | V | F | | F | V | V | | F | V | V |
| | | | V | F | F | | V | F | V | | V | F | F |
| | | | V | V | V | | V | V | V | | V | V | V |

A implicação só é **falsa** com antecedente verdadeiro e consequente
falso: com antecedente **falso** é sempre verdadeira. Uma fórmula com $n$
variáveis tem $2^n$ valorações; a **tabela de verdade** tem uma linha por
valoração e calcula o valor da fórmula coluna a coluna, das subfórmulas
interiores para a exterior (como na árvore).

::: {.exemplo title="--- Exercício 1.4(b) (lab, proplogic.pdf)"}
$\neg q \land (p \to q)$ (2 variáveis, 4 linhas):

| $p$ | $q$ | $\neg q$ | $p \to q$ | $\neg q \land (p \to q)$ |
|---|---|---|---|---|
| V | V | F | V | F |
| V | F | V | F | F |
| F | V | F | V | F |
| F | F | V | V | **V** |

Só é verdadeira com $p$ e $q$ ambos falsos.
:::

::: {.exemplo title="--- Exercício 1.4(c) (lab, proplogic.pdf)"}
$(p \land q) \to \neg(p \lor q)$:

| $p$ | $q$ | $p\land q$ | $p \lor q$ | $\neg(p\lor q)$ | $(p\land q) \to \neg(p\lor q)$ |
|---|---|---|---|---|---|
| V | V | V | V | F | **F** |
| V | F | F | V | F | **V** |
| F | V | F | V | F | **V** |
| F | F | F | F | V | **V** |

Só é falsa em $p=q=V$: o antecedente é verdadeiro e o consequente falso.
Nas outras linhas o antecedente já é falso, e a implicação é verdadeira.
:::

::: {.pratica title="--- Tabelas de verdade (proplogic.pdf)"}
- **1.4 (a)** e **(d)** --- tabelas de verdade, mesma técnica de (b)/(c)
  acima. Na (d), antes de acabar, repara em que linhas o antecedente é
  verdadeiro: é aí que tudo se decide.
:::

## Satisfazibilidade, tautologias e contradições

::: {.definicao title="--- Satisfazibilidade, tautologia, contradição"}
Uma fórmula $\phi$ é:

- **satisfazível** se existe $v$ com $v(\phi) = V$ (escreve-se
  $\models_v \phi$: $v$ **satisfaz** $\phi$);
- **tautologia** se $v(\phi) = V$ para **todas** as $v$; escreve-se
  $\models \phi$ (ex.: $\models p \lor \neg p$, o terceiro excluído);
- **contradição** se $v(\phi) = F$ para **todas** as $v$; escreve-se
  $\not\models \phi$ (ex.: $\not\models p \land \neg p$).

**Insatisfazível** = contradição. Satisfazível sem ser tautologia diz-se
**contingente**.
:::

# Aula 2 --- Consequência Semântica, Equivalência e Conectivos Completos

## A relação de satisfação $\models_v$

A extensão de $v$ às fórmulas escreve-se como uma relação $\models_v$, a
notação usada daqui em diante:

::: {.definicao title="--- Relação de satisfação"}
Dada uma valoração $v$:

1. $\models_v p$ sse $v(p) = V$;
2. $\models_v \neg\phi$ sse $\not\models_v \phi$;
3. $\models_v \phi \land \psi$ sse $\models_v \phi$ e $\models_v \psi$;
4. $\models_v \phi \lor \psi$ sse $\models_v \phi$ ou $\models_v \psi$;
5. $\models_v \phi \to \psi$ sse $\not\models_v \phi$ ou $\models_v \psi$.
:::

::: exemplo
Com $v(p)=V$, $v(q)=v(r)=F$: $\models_v (p \to (q\lor r)) \lor (r \to \neg p)$,
porque basta **um** lado da disjunção, e $\models_v r \to \neg p$ já que
$\not\models_v r$. Nem é preciso avaliar o lado esquerdo.
:::

::: {.exemplo title="--- Exercício 1.5(b) (lab, proplogic.pdf)"}
Com $v(p) = V$, $v(q) = F$: $\models_v (p \lor \neg q) \land (\neg p \land q)$?

Como $v(p)=V$, $\not\models_v \neg p$, logo $\not\models_v \neg p \land q$.
Uma conjunção precisa dos dois lados, por isso
$\not\models_v (p \lor \neg q) \land (\neg p \land q)$.
:::

::: {.exemplo title="--- Exercício 1.5(e) (lab, proplogic.pdf)"}
Com $v(p) = V$, $v(q) = F$: $\models_v ((p \to q) \to p) \to p$?

- $\models_v p$ e $\not\models_v q$, logo $\not\models_v p \to q$.
- Antecedente não satisfeito: $\models_v (p\to q) \to p$.
- $\models_v (p\to q)\to p$ e $\models_v p$, logo
  $\models_v ((p\to q)\to p)\to p$.

Esta fórmula é a **Lei de Peirce**, e é tautologia: vale para qualquer
$v$, não só para esta.
:::

::: {.pratica title="--- A relação $\models_v$ (proplogic.pdf)"}
- **1.5 (a)**, **(c)** e **(d)** --- com $v(p)=V$, $v(q)=F$, avalia de
  dentro para fora, como em (b)/(e) acima.
:::

## Satisfazibilidade de um conjunto de fórmulas

::: {.definicao title="--- Satisfazibilidade de um conjunto"}
Uma valoração $v$ **satisfaz** um conjunto $\Gamma$ ($\models_v \Gamma$)
se satisfaz **todas** as suas fórmulas: $\forall \psi \in \Gamma,\
\models_v \psi$. $\Gamma$ é **satisfazível** se alguma $v$ o satisfaz.
:::

## Consequência semântica e equivalência

::: {.definicao title="--- Consequência semântica ($\\models$)"}
$\phi$ é **consequência semântica** de $\Gamma$ ($\Gamma \models \phi$) se
**toda** a valoração que satisfaz $\Gamma$ também satisfaz $\phi$.

- $\emptyset \models \phi$ escreve-se $\models \phi$: $\phi$ é tautologia.
- Se $\Gamma = \{\psi\}$, escreve-se $\psi \models \phi$.
- Se $\psi \models \phi$ **e** $\phi \models \psi$, as duas são
  **semanticamente equivalentes**, $\psi \Leftrightarrow \phi$: têm o
  mesmo valor em todas as valorações.
:::

::: {.definicao title="--- Leis de equivalência semântica"}
| Lei | Equivalência |
|---|---|
| Comutatividade | $\phi\land\psi \Leftrightarrow \psi\land\phi$ ; $\phi\lor\psi \Leftrightarrow \psi\lor\phi$ |
| Lei de De Morgan | $\neg(\phi\land\psi) \Leftrightarrow \neg\phi\lor\neg\psi$ ; $\neg(\phi\lor\psi) \Leftrightarrow \neg\phi\land\neg\psi$ |
| Associatividade | $(\phi\land\psi)\land\theta \Leftrightarrow \phi\land(\psi\land\theta)$ ; idem para $\lor$ |
| Idempotência | $\phi\lor\phi \Leftrightarrow \phi$ ; $\phi\land\phi \Leftrightarrow \phi$ |
| Distributividade | $(\phi\land\psi)\lor\theta \Leftrightarrow (\phi\lor\theta)\land(\psi\lor\theta)$ ; $(\phi\lor\psi)\land\theta \Leftrightarrow (\phi\land\theta)\lor(\psi\land\theta)$ |
| Dupla negação | $\neg\neg\phi \Leftrightarrow \phi$ |
| Implicação | $\phi\to\psi \Leftrightarrow \neg\phi\lor\psi$ |
:::

As leis transformam uma fórmula noutra equivalente sem tabela de verdade,
substituindo uma subfórmula de cada vez, como na álgebra.

::: {.definicao title="--- Leis extra para simplificar †"}
Fazem falta para **simplificar** uma fórmula até se ver o que ela é; cada
uma confirma-se com uma tabela de 2 linhas. $V$ e $F$ representam uma
fórmula sempre verdadeira e uma sempre falsa.

| Lei | Equivalência |
|---|---|
| Complementaridade | $\phi\lor\neg\phi \Leftrightarrow V$ ; $\phi\land\neg\phi \Leftrightarrow F$ |
| Elemento neutro | $\phi\lor F \Leftrightarrow \phi$ ; $\phi\land V \Leftrightarrow \phi$ |
| Elemento absorvente | $\phi\lor V \Leftrightarrow V$ ; $\phi\land F \Leftrightarrow F$ |
| Absorção | $\phi\lor(\phi\land\psi) \Leftrightarrow \phi$ ; $\phi\land(\phi\lor\psi) \Leftrightarrow \phi$ |
:::

::: {.exemplo title="--- Exercício 1.6(a) (lab, proplogic.pdf)"}
$\neg(p \to q) \Leftrightarrow p \land \neg q$, pelas leis:

$$\neg(p\to q) \overset{\text{(implicação)}}{\Leftrightarrow} \neg(\neg p \lor q)
\overset{\text{(De Morgan)}}{\Leftrightarrow} \neg\neg p \land \neg q
\overset{\text{(dupla negação)}}{\Leftrightarrow} p \land \neg q$$

Cada passo aplica **uma** lei a uma subfórmula.
:::

::: {.exemplo title="--- Exercício 1.6(e) (lab, proplogic.pdf)"}
$(p \lor q) \to r \Leftrightarrow (p \to r) \land (q \to r)$:

$$(p\lor q) \to r
\overset{\text{(implicação)}}{\Leftrightarrow} \neg(p\lor q) \lor r
\overset{\text{(De Morgan)}}{\Leftrightarrow} (\neg p \land \neg q) \lor r$$

Distributividade $(\phi\land\psi)\lor\theta \Leftrightarrow (\phi\lor\theta)\land(\psi\lor\theta)$,
com $\phi=\neg p$, $\psi=\neg q$, $\theta=r$:

$$(\neg p \land \neg q) \lor r
\overset{\text{(distributividade)}}{\Leftrightarrow} (\neg p \lor r) \land (\neg q \lor r)
\overset{\text{(implicação, 2x)}}{\Leftrightarrow} (p \to r) \land (q \to r)$$
:::

::: {.exemplo title="--- Exercício 1.8(a) e 1.8(b) (lab, proplogic.pdf)"}
**(a) $(p\to q) \land (p\to r) \Leftrightarrow p \to (q\land r)$ --- válida.**
$$(p\to q)\land(p\to r) \Leftrightarrow (\neg p\lor q)\land(\neg p\lor r)
\overset{\text{(distributividade)}}{\Leftrightarrow} \neg p \lor (q\land r)
\Leftrightarrow p \to (q\land r)$$

**(b) $(p\to r) \land (q\to r) \Leftrightarrow (p\land q) \to r$ --- NÃO é
válida.** Contraexemplo: $v(p)=V$, $v(q)=F$, $v(r)=F$.
Esquerda: $p\to r = V\to F = F$, logo $(p\to r)\land(q\to r) = F$.
Direita: $p\land q = F$, logo $(p\land q)\to r = F \to F = V$.

Distribuir $\to$ sobre o $\land$ do **consequente** vale; sobre o do
**antecedente**, não.
:::

### Classificar uma fórmula simplificando-a (Exercício 1.9)

O Exercício 1.9 pede para classificar fórmulas (tautologia, contradição ou
satisfazível) e diz o método: *"You can start by simplifying the formulas
using semantic equivalences"*. Não se faz a tabela de verdade.

::: {.definicao title="--- Método: classificar por equivalências"}
1. **Eliminar as implicações** ($\phi\to\psi \Leftrightarrow \neg\phi\lor\psi$)
   e **empurrar as negações** para dentro (De Morgan, dupla negação).
2. **Simplificar** com as leis (complementaridade, absorção, elemento
   neutro/absorvente) até a fórmula se ler logo.
3. **Ler a classificação**:
   - chegou a $V$ → **tautologia**;
   - chegou a $F$ → **contradição**;
   - chegou a outra coisa (ex.: $p\lor\neg q$) → **satisfazível** (nem
     tautologia nem contradição). O enunciado pede então **uma valoração
     que a torna verdadeira e outra que a torna falsa**: leem-se da forma
     simplificada e **confirmam-se na fórmula original**.
:::

::: {.exemplo title="--- Exercício 1.9(d) (lab, proplogic.pdf) --- tautologia"}
$$\begin{aligned}
&p \to (q \to (p \lor q)) \\
\Leftrightarrow\ & \neg p \lor (\neg q \lor (p \lor q)) && \text{(implicação, 2 vezes)}\\
\Leftrightarrow\ & (\neg p \lor p) \lor (\neg q \lor q) && \text{(associatividade e comutatividade do } \lor\text{)}\\
\Leftrightarrow\ & V \lor V && \text{(complementaridade, 2 vezes)}\\
\Leftrightarrow\ & V && \text{(elemento absorvente)}
\end{aligned}$$

Chegou a $V$: **tautologia**. (Com tudo ligado por $\lor$, os parêntesis
reorganizam-se à vontade; foi isso que juntou $\neg p$ com $p$.)
:::

::: {.exemplo title="--- Exercício 1.9(j) (lab, proplogic.pdf) --- contradição"}
O segundo conjunto é a **negação** do primeiro:
$$\neg(p \lor \neg q) \overset{\text{(De Morgan)}}{\Leftrightarrow} \neg p \land \neg\neg q \overset{\text{(dupla negação)}}{\Leftrightarrow} \neg p \land q$$
Com $X = p\lor\neg q$:
$$(p \lor \neg q) \land (\neg p \land q) \;\Leftrightarrow\; X \land \neg X \;\overset{\text{(complementaridade)}}{\Leftrightarrow}\; F$$

Chegou a $F$: **contradição**.
:::

::: {.exemplo title="--- Exercício 1.9(i) (lab, proplogic.pdf) --- satisfazível"}
$$\begin{aligned}
&(p \lor q) \to (p \land q) \\
\Leftrightarrow\ & \neg(p \lor q) \lor (p \land q) && \text{(implicação)}\\
\Leftrightarrow\ & (\neg p \land \neg q) \lor (p \land q) && \text{(De Morgan)}
\end{aligned}$$

Não simplifica mais: é verdadeira quando $p$ e $q$ são **ambos falsos** ou
**ambos verdadeiros**. **Satisfazível, nem tautologia nem contradição.**

- **Verdadeira** com $p=q=V$: $(V\lor V)\to(V\land V) = V\to V = V$.
- **Falsa** com $p=V, q=F$: $(V\lor F)\to(V\land F) = V\to F = F$.
:::

::: {.pratica title="--- Consequência e equivalência (proplogic.pdf)"}
- **1.6 (b)**, **(c)** e **(d)** --- provar as equivalências, pela tabela
  ou pelas leis (tenta pelas leis: é o que treina para o exame). Na (b),
  usa $\varphi\to\psi \Leftrightarrow \neg\varphi\lor\psi$ dos dois lados.
- **1.8 (c)** --- é válida ou não? Mesma comparação de (a)/(b) acima:
  verifica com as leis de distributividade ou encontra um contraexemplo.
- **1.9 (c)** --- classificar **pelo método acima** (simplificar com as
  leis; nada de tabela). Se não for tautologia nem contradição, dá uma
  valoração que a torna verdadeira e outra que a torna falsa.
- **1.9 (h)** --- o mesmo, com 3 variáveis. Pista: depois de eliminar as
  implicações, procura uma **absorção**.

As restantes alíneas da 1.9 ((a), (b), (e), (f), (g), (k)) são a mesma
simplificação repetida --- não precisas de as fazer todas.
:::

## Propriedades da relação $\models$

Para mostrar que uma afirmação sobre $\models$ é **verdadeira** usa-se a
definição; para mostrar que é **falsa** basta um contraexemplo concreto.

::: {.definicao title="--- Método: provar com a definição de $\\models_v$ †"}
**Para mostrar $\Gamma \models \phi$** (ou $\models \phi$, com
$\Gamma=\emptyset$):

1. "Seja $v$ uma valoração tal que $\models_v \Gamma$." (Para $\models\phi$:
   "seja $v$ uma valoração qualquer".)
2. Abrir cada fórmula pelo **conectivo principal**, com as regras 1--5 de
   $\models_v$. Quando a regra dá um **"ou"**, **separar em casos** e
   fechar cada um.
3. Chegar a $\models_v \phi$ em todos os casos e concluir: "como $v$ é
   arbitrária, $\Gamma \models \phi$." $\blacksquare$

**Por absurdo:** supõe-se $\not\models_v \phi$ e abre-se com as regras da
negação. É a mais curta quando $\phi$ é uma implicação, porque
$\not\models_v \phi\to\psi$ força $\models_v \phi$ **e**
$\not\models_v \psi$. Chegar a $\models_v \theta$ e $\not\models_v \theta$
mostra que essa $v$ não existe.

**Para mostrar que é falso:** dá-se uma **valoração concreta** e
verifica-se com as regras que $\models_v \gamma$ para cada
$\gamma\in\Gamma$ e $\not\models_v \phi$.

Regras da negação (saem das regras 2--5):

- $\not\models_v \phi\land\psi$ sse $\not\models_v \phi$ ou $\not\models_v \psi$
- $\not\models_v \phi\lor\psi$ sse $\not\models_v \phi$ e $\not\models_v \psi$
- $\not\models_v \phi\to\psi$ sse $\models_v \phi$ e $\not\models_v \psi$

*Modus ponens*: se $\models_v \phi$ e $\models_v \phi\to\psi$, então
$\models_v \psi$ (pela regra 5, $\not\models_v\phi$ é impossível).
:::

::: {.exemplo title="--- Exercício 1.16(a), (b) e (f) (lab, proplogic.pdf) --- monotonicidade"}
**(a) Se $\Gamma \models \theta$ e $\Gamma \subseteq \Sigma$, então
$\Sigma \models \theta$ --- VERDADEIRO.**

Seja $v$ tal que $\models_v \Sigma$, isto é, $\models_v \psi$ para todo o
$\psi \in \Sigma$. Seja $\psi \in \Gamma$. Como $\Gamma \subseteq \Sigma$,
$\psi \in \Sigma$, logo $\models_v \psi$. Portanto $\models_v \Gamma$.
Como $\Gamma \models \theta$, tem-se $\models_v \theta$. Como $v$ é
arbitrária, $\Sigma \models \theta$. $\blacksquare$

**Acrescentar premissas nunca destrói** uma consequência
(**monotonicidade**).

**(b) Se $\Sigma \models \theta$ e $\Gamma \subseteq \Sigma$, então
$\Gamma \models \theta$ --- FALSO** (o recíproco de (a)).

Contraexemplo: $\Sigma = \{p,\ p\to q\}$, $\Gamma = \{p\}$, $\theta = q$;
$\Gamma \subseteq \Sigma$.

- $\Sigma \models q$: seja $v$ tal que $\models_v p$ e $\models_v p\to q$.
  Como $\models_v p\to q$ sse $\not\models_v p$ ou $\models_v q$, e
  $\not\models_v p$ é impossível, tem-se $\models_v q$.
- $\Gamma \not\models q$: com $v(p)=V$, $v(q)=F$, $\models_v \Gamma$ mas
  $\not\models_v q$.

**Tirar premissas** pode fazer perder a conclusão.

**(f) Se $\Sigma \models \theta$ e $\Sigma \subseteq \Gamma$, então
$\Sigma \cup \Gamma \models \theta$ --- VERDADEIRO.** Se
$\Sigma \subseteq \Gamma$, então $\Sigma \cup \Gamma = \Gamma$, e a
afirmação é a alínea (a) com $\Gamma$ e $\Sigma$ trocados. $\blacksquare$
:::

::: {.exemplo title="--- Exercício 1.13(a), (b) e (c) (lab, proplogic.pdf)"}
**(a) $\models (p\land\neg p) \to (p\land\neg r)$ --- VERDADEIRO.**

Seja $v$ uma valoração qualquer.
$$\models_v (p\land\neg p)\to(p\land\neg r) \ \text{ sse }\ \not\models_v p\land\neg p \ \text{ ou }\ \models_v p\land\neg r$$
Ora, $\models_v p\land\neg p$ sse $\models_v p$ e $\not\models_v p$, o que
é impossível. Logo $\not\models_v p\land\neg p$ e
$\models_v (p\land\neg p)\to(p\land\neg r)$. Como $v$ é arbitrária,
$\models (p\land\neg p)\to(p\land\neg r)$. $\blacksquare$

**(b) $\models (q\lor\neg r) \to (q\land\neg q)$ --- FALSO.**

Procura-se $v$ com $\models_v q\lor\neg r$ e $\not\models_v q\land\neg q$.
A segunda vale sempre, como em (a). **Contraexemplo:** $v(q)=V$, $v(r)=V$.

- $\models_v q$, logo $\models_v q\lor\neg r$.
- $\models_v q$, logo $\not\models_v \neg q$, logo $\not\models_v q\land\neg q$.
- Então $\not\models_v (q\lor\neg r)\to(q\land\neg q)$: não é tautologia.

**(c) $\{(p\to q)\lor r,\ ((p\to q)\lor r)\to\neg r,\ (p\to q)\to(q\to r)\} \models \neg q$
--- VERDADEIRO.**

Com a tabela de verdade (o método da professora quando o enunciado não a
proíbe), com $A = (p\to q)\lor r$:

| $p$ | $q$ | $r$ | $p\to q$ | $A$ | $\neg r$ | $A\to\neg r$ | $q\to r$ | $(p\to q)\to(q\to r)$ | $\neg q$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| V | V | V | V | V | F | F | V | V | F |
| V | V | F | V | V | V | V | F | F | F |
| V | F | V | F | V | F | F | V | V | V |
| V | F | F | F | F | V | V | V | V | V |
| F | V | V | V | V | F | F | V | V | F |
| F | V | F | V | V | V | V | F | F | F |
| F | F | V | V | V | F | F | V | V | V |
| F | F | F | V | **V** | V | **V** | V | **V** | **V** |

Na única linha em que as três premissas são V (a última), $\neg q$ também
é V. Logo o conjunto $\models \neg q$.
:::

::: {.exemplo title="--- Exercício 1.13(d) (lab, proplogic.pdf)"}
**$\{(p\lor q)\to r\} \models (p\to r)\lor(q\to r)$ --- VERDADEIRO.**
Sem tabela, pela definição de $\models_v$:

Seja $v$ tal que $\models_v (p\lor q)\to r$. Queremos
$\models_v (p\to r)\lor(q\to r)$.
$$\models_v (p\lor q)\to r \ \text{ sse }\ \not\models_v p\lor q \ \text{ ou }\ \models_v r$$

- **Caso 1: $\models_v r$.** Como $\models_v p\to r$ sse $\not\models_v p$
  ou $\models_v r$, tem-se $\models_v p\to r$. Logo
  $\models_v (p\to r)\lor(q\to r)$.
- **Caso 2: $\not\models_v p\lor q$**, isto é, $\not\models_v p$ e
  $\not\models_v q$. Como $\not\models_v p$, $\models_v p\to r$. Logo
  $\models_v (p\to r)\lor(q\to r)$.

Em ambos os casos $\models_v (p\to r)\lor(q\to r)$. Como $v$ é arbitrária,
$\{(p\lor q)\to r\} \models (p\to r)\lor(q\to r)$. $\blacksquare$

Os dois casos estão ligados por um **"ou"**: basta um deles. Não se pode
juntar "$v(r)=V$ **e** $v(p)=F$ **e** $v(q)=F$".
:::

::: {.exemplo title="--- Exercício 1.14(a) e 1.14(d) (lab, proplogic.pdf) --- sem tabela de verdade"}
**(a) $\models p \to (((q\to p)\to p) \to r)$ --- FALSO.**

Seja $v(p)=V$ e $v(r)=F$. De $\models_v p$ segue
$\models_v (q\to p)\to p$; com $\not\models_v r$, fica
$\not\models_v ((q\to p)\to p)\to r$. Como $\models_v p$,
$\not\models_v p \to (((q\to p)\to p)\to r)$: não é tautologia.

**(d) $\models ((p\land q)\to(s\lor t)) \to ((p\to s)\lor(q\to t))$ ---
VERDADEIRO.** Por absurdo: suponha-se $v$ com $\not\models_v$ da fórmula.

1. $\models_v (p\land q)\to(s\lor t)$ e
   $\not\models_v (p\to s)\lor(q\to t)$ (negação de $\to$).
2. $\not\models_v (p\to s)\lor(q\to t)$ sse $\not\models_v p\to s$ e
   $\not\models_v q\to t$: $\models_v p$, $\not\models_v s$,
   $\models_v q$, $\not\models_v t$.
3. De $\models_v p$ e $\models_v q$: $\models_v p\land q$. De
   $\not\models_v s$ e $\not\models_v t$: $\not\models_v s\lor t$.
4. Então $\not\models_v (p\land q)\to(s\lor t)$, o que contradiz 1.

Não existe tal $v$, logo
$\models ((p\land q)\to(s\lor t)) \to ((p\to s)\lor(q\to t))$. $\blacksquare$
:::

::: {.pratica title="--- Propriedades de $\models$ (proplogic.pdf)"}
- **1.15** --- mesma ideia do Exercício 1.16 acima, mas com $\models$ e
  $\Leftrightarrow$ entre fórmulas genéricas $\varphi,\psi,\theta,\gamma$,
  que se tratam como variáveis: verdadeiro → definição de $\models_v$, por
  absurdo, equivalências ou tabela sobre $\varphi,\psi$; falso → uma
  valoração ($v(\varphi)=F$, $v(\psi)=V$, ...) verificada regra a regra.
:::

## Quantas proposições podem ser simultaneamente verdadeiras

::: {.exemplo title="--- Exercício 1.7 (lab, proplogic.pdf)"}
Quantas de $p\lor\neg q,\ \neg p\lor q,\ q\lor r,\ q\lor\neg r,\ \neg q\lor\neg r$
podem ser verdadeiras ao mesmo tempo? Com 3 variáveis, faz-se a tabela (8
linhas) e conta-se:

| $p$ | $q$ | $r$ | $p\lor\neg q$ | $\neg p\lor q$ | $q\lor r$ | $q\lor\neg r$ | $\neg q\lor\neg r$ | nº de V |
|---|---|---|---|---|---|---|---|---|
| V | V | V | V | V | V | V | F | 4 |
| V | V | F | V | V | V | V | V | **5** |
| V | F | V | V | F | V | F | V | 3 |
| V | F | F | V | F | F | V | V | 3 |
| F | V | V | F | V | V | V | F | 3 |
| F | V | F | F | V | V | V | V | 4 |
| F | F | V | V | V | V | F | V | 4 |
| F | F | F | V | V | F | V | V | 4 |

O **máximo** é **5** (todas), em $p=V,q=V,r=F$. O mínimo é 3.
:::

## Conjuntos completos de conectivos

::: {.definicao title="--- Conjunto completo de conectivos"}
Um conjunto de conectivos $C$ é **completo** se, para qualquer função de
verdade $f : \{V,F\}^n \to \{V,F\}$, existe uma fórmula $\phi$ com $n$
variáveis, só com conectivos de $C$, que **induz** $f$: $F_\phi = f$, onde
$F_\phi(x_1,\dots,x_n) = v_\chi(\phi)$ para $v_\chi(p_i)=x_i$. Isto é, $C$
exprime qualquer função booleana.
:::

**$\{\land,\lor,\neg\}$ é completo** (por indução em $n$):

- **Base ($n=1$):** há $2^2=4$ funções de aridade 1, e cada uma tem
  fórmula: "sempre F" $= p\land\neg p$; $\neg p$; $p$; "sempre V"
  $= p\lor\neg p$.
- **Passo:** dada $f:\{V,F\}^{n+1}\to\{V,F\}$, sejam
  $f_1(x_1,\dots,x_n)=f(x_1,\dots,x_n,V)$ e
  $f_2(x_1,\dots,x_n)=f(x_1,\dots,x_n,F)$. Por hipótese de indução há
  $\phi_1,\phi_2$ com $F_{\phi_i}=f_i$. Então
  $\phi = (p_{n+1}\land\phi_1)\lor(\neg p_{n+1}\land\phi_2)$ induz $f$:
  com $x_{n+1}=V$ reduz-se a $\phi_1$, com $x_{n+1}=F$ a $\phi_2$.

Daí, **$\{\neg,\to\}$ também é completo**:
$\phi\land\psi \Leftrightarrow \neg(\phi\to\neg\psi)$ e
$\phi\lor\psi \Leftrightarrow \neg\phi\to\psi$.

::: {.exemplo title="--- Exercício 1.19(a) (lab, proplogic.pdf) --- {negação, disjunção} é completo"}
Escrever $p\to q$, $p\land q$ e $p\leftrightarrow q$ só com $\neg$ e $\lor$:

- $p\to q \Leftrightarrow \neg p \lor q$ (lei da implicação).
- $p\land q \Leftrightarrow \neg\neg(p\land q) \Leftrightarrow \neg(\neg p\lor\neg q)$
  (dupla negação, De Morgan).
- $p\leftrightarrow q \Leftrightarrow (p\to q)\land(q\to p)$. Cada
  implicação dá $\neg p\lor q$ e $\neg q\lor p$, e a conjunção, pelo ponto
  anterior ($\phi\land\psi\Leftrightarrow\neg(\neg\phi\lor\neg\psi)$):
  $$p\leftrightarrow q \;\Leftrightarrow\; \neg\big(\neg(\neg p\lor q)\lor\neg(\neg q\lor p)\big)$$
:::

::: {.exemplo title="--- Exercício 1.19(b) (lab, proplogic.pdf) --- NAND é completo"}
$p\bar\land q \Leftrightarrow \neg(p\land q)$: só é falso com $p=q=V$.
Escrever $\neg p$, $p\land q$ e $p\lor q$ só com $\bar\land$:

**Negação:** $p \bar\land p \Leftrightarrow \neg(p\land p) \Leftrightarrow \neg p$
(idempotência). Logo $\neg p = p\bar\land p$.

**Conjunção:** $\neg(p\bar\land q) \Leftrightarrow p\land q$, e
$\neg X = X\bar\land X$ com $X = p\bar\land q$:
$$p \land q \;=\; (p\bar\land q)\ \bar\land\ (p\bar\land q)$$

**Disjunção:** por De Morgan, $p\lor q \Leftrightarrow \neg(\neg p\land\neg q) \Leftrightarrow \neg p \bar\land \neg q$.
Com $\neg p = p\bar\land p$ e $\neg q = q\bar\land q$:
$$p \lor q \;=\; (p\bar\land p)\ \bar\land\ (q\bar\land q)$$

Como $\{\neg,\land,\lor\}$ é completo, **$\{\bar\land\}$ sozinho é
completo**.
:::

## Aplicação: modelar problemas em lógica proposicional

Nos problemas de cavaleiros (dizem sempre a verdade) e vilões (mentem
sempre), a chave é a **auto-referência**: A é cavaleiro sse o que diz é
verdade ($a \leftrightarrow S$, com $a$ = "A é cavaleiro" e $S$ a frase).
A professora resolve-os **por casos, em frases curtas**: cada caso
impossível viola uma das regras (cavaleiro a mentir ou vilão a dizer a
verdade). Uma tabela de $a\leftrightarrow S$ dá o mesmo resultado.

::: {.exemplo title="--- Exercício 1.10(a) (lab, proplogic.pdf) --- cavaleiros e vilões"}
A diz: "Pelo menos um de nós [A, B] é vilão."

A não pode ser vilão e dizer isto: a frase seria verdadeira e um vilão
estaria a dizer a verdade. Logo **A é cavaleiro**, a frase é verdadeira e,
como A não é vilão, **B é vilão**.
:::

::: {.exemplo title="--- Exercício 1.10(e) (lab, proplogic.pdf) --- três pessoas"}
A diz: "Somos todos vilões." B diz: "Exatamente um de nós é cavaleiro."

A não pode ser cavaleiro e dizer isto (ele próprio seria vilão). Logo
**A é vilão** e a frase é falsa: B ou C é cavaleiro.

- B e C não podem ser os dois cavaleiros: a frase de B seria falsa e B
  um cavaleiro a mentir.
- B vilão e C cavaleiro também não: haveria exatamente um cavaleiro, a
  frase de B seria verdadeira e B um vilão a dizer a verdade.

Logo **B é cavaleiro e C é vilão** (e a frase de B é verdadeira: só B é
cavaleiro).
:::

::: {.exemplo title="--- Exercício 1.11 (lab, proplogic.pdf) --- suspeitos de um crime"}
A: "B é culpado, mas C é inocente." B: "Se A é culpado, então C é
culpado." C: "Eu sou inocente, mas um dos outros dois é culpado."

Com $g_a,g_b,g_c$ = "A/B/C é culpado":
$$S_A = g_b\land\neg g_c \qquad S_B = g_a\to g_c \qquad S_C = \neg g_c\land(g_a\lor g_b)$$

Uma só tabela responde a todas as alíneas:

| $g_a$ | $g_b$ | $g_c$ | $S_A=g_b\land\neg g_c$ | $S_B=g_a\to g_c$ | $S_C=\neg g_c\land(g_a\lor g_b)$ |
|---|---|---|---|---|---|
| V | V | V | F | V | F |
| V | V | F | **V** | F | **V** |
| V | F | V | F | V | F |
| V | F | F | F | F | **V** |
| F | V | V | F | V | F |
| F | V | F | **V** | **V** | **V** |
| F | F | V | F | V | F |
| F | F | F | F | V | F |

**(a) As três declarações são compatíveis?** $\{S_A,S_B,S_C\}$ é
satisfazível? Com $v(g_a)=F$, $v(g_b)=V$, $v(g_c)=F$:
$\models_v S_A$ ($\models_v g_b$, $\not\models_v g_c$),
$\models_v S_B$ ($\not\models_v g_a$) e
$\models_v S_C$ ($\not\models_v g_c$, $\models_v g_b$). **Sim**, e pela
tabela é a **única** valoração que as satisfaz (só B culpado).
:::

::: {.exemplo title="--- Exercício 1.11 (cont.) --- consequência"}
**(b) Alguma declaração é consequência das outras duas?**

*$\{S_A,S_B\}\models S_C$: sim.* Seja $v$ tal que $\models_v S_A$ e
$\models_v S_B$.

- $\models_v g_b\land\neg g_c$ sse $\models_v g_b$ e $\not\models_v g_c$.
- $\models_v g_a\to g_c$ sse $\not\models_v g_a$ ou $\models_v g_c$. Como
  $\not\models_v g_c$, tem-se $\not\models_v g_a$.
- Então $\models_v \neg g_c$ e, como $\models_v g_b$,
  $\models_v g_a\lor g_b$. Logo $\models_v \neg g_c\land(g_a\lor g_b)$,
  isto é, $\models_v S_C$. $\blacksquare$

*$\{S_B,S_C\}\models S_A$: sim.* Seja $v$ tal que $\models_v S_B$ e
$\models_v S_C$.

- $\models_v \neg g_c\land(g_a\lor g_b)$ sse $\not\models_v g_c$ e
  $\models_v g_a\lor g_b$.
- $\models_v g_a\to g_c$ sse $\not\models_v g_a$ ou $\models_v g_c$. Como
  $\not\models_v g_c$, tem-se $\not\models_v g_a$.
- $\models_v g_a\lor g_b$ sse $\models_v g_a$ ou $\models_v g_b$. Como
  $\not\models_v g_a$, tem-se $\models_v g_b$.
- Logo $\models_v g_b\land\neg g_c$, isto é, $\models_v S_A$.
  $\blacksquare$

*$\{S_A,S_C\}\not\models S_B$.* Contraexemplo: $v(g_a)=V$, $v(g_b)=V$,
$v(g_c)=F$ (2.ª linha).

- $\models_v g_b$ e $\not\models_v g_c$, logo $\models_v S_A$.
- $\not\models_v g_c$ e $\models_v g_a$, logo $\models_v S_C$.
- $\models_v g_a$ e $\not\models_v g_c$, logo $\not\models_v g_a\to g_c$,
  isto é, $\not\models_v S_B$.
:::

::: {.exemplo title="--- Exercício 1.11 (cont.) --- hipóteses sobre quem diz a verdade"}
Cada hipótese dá uma resposta diferente; leem-se todas na mesma tabela.

**(c) Se os três são inocentes, quem mentiu?** Linha
$g_a=g_b=g_c=F$: $S_A=F$, $S_B=V$, $S_C=F$. **A e C mentiram; B disse a
verdade.**

**(d) Se os três disseram a verdade, quem é culpado?**
$S_A=S_B=S_C=V$ só na linha de (a): **só B é culpado.**

**(e) Se o inocente disse a verdade e o culpado mentiu?** Cada pessoa é
inocente sse a sua declaração é verdadeira:
$$\Delta = \{\, S_A\leftrightarrow\neg g_a,\ \ S_B\leftrightarrow\neg g_b,\ \ S_C\leftrightarrow\neg g_c \,\}$$
($\models_v \phi\leftrightarrow\psi$ sse ambos valem ou nenhum vale.) Seja
$v$ tal que $\models_v \Delta$.

1. **$\models_v g_a$.** Suponha-se $\not\models_v g_a$. Então
   $\models_v \neg g_a$, logo $\models_v S_A$: $\models_v g_b$ e
   $\not\models_v g_c$. Como $\models_v g_b$, $\not\models_v \neg g_b$,
   logo $\not\models_v S_B$: $\models_v g_a$ e $\not\models_v g_c$.
   Contradição com $\not\models_v g_a$.
2. **$\models_v g_c$.** Por 1, $\not\models_v \neg g_a$, logo
   $\not\models_v S_A$: $\not\models_v g_b$ ou $\models_v g_c$. Suponha-se
   $\not\models_v g_c$. Então $\not\models_v g_b$, logo $\models_v \neg g_b$
   e $\models_v S_B$: $\not\models_v g_a$ ou $\models_v g_c$. Nenhuma vale
   (por 1 e pela suposição). Contradição.
3. **$\not\models_v g_b$.** Suponha-se $\models_v g_b$. Então
   $\not\models_v \neg g_b$, logo $\not\models_v S_B$: $\models_v g_a$ e
   $\not\models_v g_c$. Contradiz 2.

Logo $v(g_a)=V$, $v(g_b)=F$, $v(g_c)=V$. Verificação:

- $\not\models_v S_A$ (porque $\models_v g_c$) e $\not\models_v \neg g_a$. $\checkmark$
- $\models_v S_B$ (porque $\models_v g_c$) e $\models_v \neg g_b$. $\checkmark$
- $\not\models_v S_C$ (porque $\models_v g_c$) e $\not\models_v \neg g_c$. $\checkmark$

**A e C são culpados; B é inocente.**
:::

::: {.pratica title="--- Modelação (proplogic.pdf)"}
- **1.10 (g)** --- raciocínio indireto diferente: não analisas o que A/B
  disseram, mas o que **C disse**.
- **1.10 (j)** --- aqui és tu que **constróis** a pergunta certa (pista do
  enunciado: relaciona, por equivalência, o que queres saber com o tipo
  do habitante).
- **1.12** --- mesma técnica de modelação do Exercício 1.11 (uma variável
  por cadeira, uma fórmula por regra).
- *Opcional:* **1.10 (k)**, que o professor chama "um problema invulgar".

As restantes alíneas de 1.10 ((b), (c), (d), (f), (h), (i), (l)) repetem a
técnica de (a)/(e) --- não precisas de as fazer.
:::

# Aula 3 --- Formas Normais e Satisfazibilidade

Qualquer fórmula pode transformar-se numa fórmula equivalente com uma
**forma normal**, e para algumas dessas formas a satisfazibilidade ou a
validade decide-se só a olhar para a fórmula, sem a tabela de $2^n$
linhas. A negativa, a disjuntiva e a conjuntiva existem para **qualquer**
fórmula; a de Horn só para algumas.

## Literais e forma normal negativa (FNN)

::: {.definicao title="--- Literal e forma normal negativa"}
Um **literal** é uma variável $p$ (literal **positivo**) ou a sua negação
$\neg p$ (literal **negativo**).

Uma fórmula está em **forma normal negativa** se $\neg$ só aparece
aplicada a variáveis. Ex.: $(\neg p \land \neg q) \lor p$ está em FNN;
$\neg(p \lor q)$ não está.
:::

::: {.definicao title="--- Proposição (existência da FNN)"}
Qualquer fórmula só com $\land$, $\lor$ e $\neg$ é equivalente a uma
fórmula em FNN: aplicam-se as **leis de De Morgan** (que empurram cada
$\neg$ para dentro, trocando $\land$ por $\lor$) e a **dupla negação** até
cada $\neg$ ficar encostado a uma variável.

Se a fórmula tiver $\to$ ou $\leftrightarrow$, **eliminam-se primeiro**†:
$\phi\to\psi \Leftrightarrow \neg\phi\lor\psi$ e
$\phi\leftrightarrow\psi \Leftrightarrow (\phi\to\psi)\land(\psi\to\phi)$.
($\neg(p \to q)$ é $p \land \neg q$, não $\neg p \to \neg q$.)
:::

::: {.exemplo title="--- FNN de $\\neg((p \\lor q) \\land \\neg p)$"}
$$\begin{aligned}
&\neg\big((p \lor q) \land \neg p\big) \\
\overset{\text{(De Morgan, no } \land\text{ exterior)}}{\Leftrightarrow}\ & \neg(p \lor q) \lor \neg\neg p \\
\overset{\text{(De Morgan, em } \neg(p\lor q))}{\Leftrightarrow}\ & (\neg p \land \neg q) \lor \neg\neg p \\
\overset{\text{(dupla negação)}}{\Leftrightarrow}\ & (\neg p \land \neg q) \lor p
\end{aligned}$$

Em cada passo o $\neg$ desce um nível na árvore, até ficar encostado às
variáveis.
:::

## Forma normal disjuntiva (FND)

::: {.definicao title="--- Forma normal disjuntiva"}
Uma fórmula está em **forma normal disjuntiva** se é uma **disjunção de
conjunções de literais** ("um *ou* de *e*'s"):
$$(\alpha_{11} \land \dots \land \alpha_{1k_1}) \lor \dots \lor (\alpha_{n1} \land \dots \land \alpha_{nk_n})$$
Ex.: $p \land q$; $p \lor \neg p$; $(p \land q \land \neg r) \lor (\neg p \land r)$.
:::

Obtém-se **a partir da tabela de verdade** ou **a partir da fórmula**,
por equivalências.

### FND a partir da tabela de verdade

::: {.definicao title="--- Lema (toda a função de verdade tem uma FND)"}
Para qualquer $f : \{V,F\}^n \to \{V,F\}$ existe $\phi$ em FND, com $n$
variáveis, tal que $F_\phi = f$. **Prova (é o próprio método):**

- Se $f$ dá sempre $F$, $\phi = p_1 \land \neg p_1$.
- Senão, para cada linha $v$, seja $l_i^v = p_i$ se $v(p_i)=V$ e
  $l_i^v = \neg p_i$ se $v(p_i)=F$, e $\phi_v = l_1^v \land \dots \land l_n^v$.
  Cada $l_i^v$ é verdadeiro em $v$, logo $v(\phi_v)=V$; noutra linha $v'$
  alguma variável muda, esse literal é falso e $\phi_v$ é falsa. Ou seja,
  **$\phi_v$ é verdadeira exatamente na linha $v$.**
- $\phi = \bigvee_{f(v)=V} \phi_v$ é verdadeira exatamente nas linhas em
  que $f$ dá $V$: $F_\phi = f$.

Como $\phi$ só usa $\land$, $\lor$ e $\neg$, isto é outra prova (direta,
linha a linha) de que $\{\land,\lor,\neg\}$ é completo.
:::

::: {.exemplo title="--- FND a partir de uma tabela"}
| linha | $x_1$ | $x_2$ | $x_3$ | $f$ | conjunção $\phi_v$ (só nas linhas com $V$) |
|---|---|---|---|---|---|
| 1 | V | V | V | V | $p_1 \land p_2 \land p_3$ |
| 2 | V | V | F | V | $p_1 \land p_2 \land \neg p_3$ |
| 3 | V | F | V | V | $p_1 \land \neg p_2 \land p_3$ |
| 4 | V | F | F | F | --- |
| 5 | F | V | V | V | $\neg p_1 \land p_2 \land p_3$ |
| 6 | F | V | F | F | --- |
| 7 | F | F | V | F | --- |
| 8 | F | F | F | F | --- |

Variável a $V$ na linha → entra **positiva**; a $F$ → entra **negada**
(linha 3: $x_1=V, x_2=F, x_3=V$ dá $p_1 \land \neg p_2 \land p_3$).
Juntando com $\lor$ as 4 conjunções:
$$(p_1 \land p_2 \land p_3) \lor (p_1 \land p_2 \land \neg p_3) \lor (p_1 \land \neg p_2 \land p_3) \lor (\neg p_1 \land p_2 \land p_3)$$
:::

### FND a partir de uma fórmula

::: {.definicao title="--- Corolário (toda a fórmula tem uma FND equivalente)"}
1. eliminar $\to$ e $\leftrightarrow$;
2. passar para **FNN** (De Morgan + dupla negação);
3. aplicar a **distributividade do $\land$ sobre o $\lor$** até não haver
   $\lor$ dentro de um $\land$:
   $$(\phi \lor \psi) \land \theta \Leftrightarrow (\phi \land \theta) \lor (\psi \land \theta)
   \qquad \theta \land (\phi \lor \psi) \Leftrightarrow (\theta \land \phi) \lor (\theta \land \psi)$$
:::

::: {.exemplo title="--- FND de $(p \\lor r) \\leftrightarrow (q \\land \\neg p)$, passos 1 e 2"}
**Passo 1 --- eliminar $\leftrightarrow$ e $\to$:**
$$\begin{aligned}
&(p \lor r) \leftrightarrow (q \land \neg p) \\
\Leftrightarrow\ & \big((p \lor r) \to (q \land \neg p)\big) \land \big((q \land \neg p) \to (p \lor r)\big) && (\leftrightarrow \text{ como duas implicações})\\
\Leftrightarrow\ & \big(\neg(p \lor r) \lor (q \land \neg p)\big) \land \big(\neg(q \land \neg p) \lor (p \lor r)\big) && (\text{implicação, 2 vezes})
\end{aligned}$$

**Passo 2 --- FNN.** $\neg(p\lor r) \Leftrightarrow \neg p \land \neg r$
(De Morgan) e $\neg(q \land \neg p) \Leftrightarrow \neg q \lor \neg\neg p \Leftrightarrow \neg q \lor p$
(De Morgan + dupla negação):
$$\underbrace{\big((\neg p \land \neg r) \lor (q \land \neg p)\big)}_{X} \land \underbrace{\big((\neg q \lor p) \lor (p \lor r)\big)}_{A \,\lor\, B}$$
com $A = \neg q \lor p$ e $B = p \lor r$. Está em FNN, mas não em FND: há
$\lor$ dentro do $\land$ principal.
:::

::: {.exemplo title="--- FND de $(p \\lor r) \\leftrightarrow (q \\land \\neg p)$, passo 3: distributividade"}
**3a** --- $X \land (A \lor B) \Leftrightarrow (X \land A) \lor (X \land B)$:
$$\big(((\neg p \land \neg r) \lor (q \land \neg p)) \land A\big) \lor \big(((\neg p \land \neg r) \lor (q \land \neg p)) \land B\big)$$

**3b** --- em cada bloco, $X = C_1 \lor C_2$ ($C_1 = \neg p \land \neg r$,
$C_2 = q \land \neg p$) distribui outra vez:
$(C_1 \lor C_2) \land A \Leftrightarrow (C_1 \land A) \lor (C_2 \land A)$, e
o mesmo com $B$:
$$(\neg p \land \neg r \land (\neg q \lor p)) \lor (q \land \neg p \land (\neg q \lor p)) \lor (\neg p \land \neg r \land (p \lor r)) \lor (q \land \neg p \land (p \lor r))$$

**3c** --- cada termo ainda tem um $\lor$; distribui-se
($K \land (a \lor b) \Leftrightarrow (K \land a) \lor (K \land b)$):

- **Termo 1** --- $K = \neg p \land \neg r$, $a \lor b = \neg q \lor p$:
  $(\neg p \land \neg r \land \neg q) \lor (\neg p \land \neg r \land p)$
- **Termo 2** --- $K = q \land \neg p$, $a \lor b = \neg q \lor p$:
  $(q \land \neg p \land \neg q) \lor (q \land \neg p \land p)$
- **Termo 3** --- $K = \neg p \land \neg r$, $a \lor b = p \lor r$:
  $(\neg p \land \neg r \land p) \lor (\neg p \land \neg r \land r)$
- **Termo 4** --- $K = q \land \neg p$, $a \lor b = p \lor r$:
  $(q \land \neg p \land p) \lor (q \land \neg p \land r)$

A FND é a disjunção destas 8 conjunções:
$$(\neg p \land \neg r \land \neg q) \lor (\neg p \land \neg r \land p) \lor (q \land \neg p \land \neg q) \lor (q \land \neg p \land p) \lor (\neg p \land \neg r \land p) \lor (\neg p \land \neg r \land r) \lor (q \land \neg p \land p) \lor (q \land \neg p \land r)$$
:::

## Satisfazibilidade de uma FND

::: {.definicao title="--- Lema e corolário"}
**Lema.** Uma conjunção de literais $l_1 \land \dots \land l_n$ é
satisfazível **sse** não contém um par complementar ($l_i$ e
$l_j = \neg l_i$). Sem par, põe-se cada positivo a $V$ e cada negativo a
$F$; com $p$ e $\neg p$, nunca são ambos verdadeiros.

**Corolário.** Uma FND é satisfazível **sse alguma** das suas conjunções
é satisfazível.
:::

::: exemplo
- $p \land \neg q \land \neg r \land q$: tem $\neg q$ e $q$ → **não** é
  satisfazível.
- $\neg p \land q \land \neg r \land \neg s$: sem par → **é** satisfazível
  ($p=F$, $q=V$, $r=F$, $s=F$).
:::

::: {.exemplo title="--- $(p \\lor r) \\leftrightarrow (q \\land \\neg p)$ é satisfazível?"}
Verifica-se cada uma das 8 conjunções da FND acima:

| # | conjunção | par complementar? | satisfazível? |
|---|---|---|---|
| 1 | $\neg p \land \neg r \land \neg q$ | nenhum | **sim** |
| 2 | $\neg p \land \neg r \land p$ | $\neg p$, $p$ | não |
| 3 | $q \land \neg p \land \neg q$ | $q$, $\neg q$ | não |
| 4 | $q \land \neg p \land p$ | $\neg p$, $p$ | não |
| 5 | $\neg p \land \neg r \land p$ | $\neg p$, $p$ | não |
| 6 | $\neg p \land \neg r \land r$ | $\neg r$, $r$ | não |
| 7 | $q \land \neg p \land p$ | $\neg p$, $p$ | não |
| 8 | $q \land \neg p \land r$ | nenhum | **sim** |

Há uma conjunção satisfazível → a fórmula **é satisfazível**: a 1 dá
$p=q=r=F$; a 8 dá $p=F$, $q=r=V$. As insatisfazíveis são sempre falsas e
podem **apagar-se** ($\phi \lor F \Leftrightarrow \phi$):
$$(p \lor r) \leftrightarrow (q \land \neg p) \;\Leftrightarrow\; (\neg p \land \neg q \land \neg r) \lor (\neg p \land q \land r)$$

**Verificação:** com $p=V$, $p \lor r = V$ e $q \land \neg p = F$, logo a
equivalência é $F$. Com $p=F$ fica $r \leftrightarrow q$, verdadeira só
para $q=r=F$ ou $q=r=V$: as duas conjunções que sobraram. $\checkmark$
:::

**Custo†** (apontamentos de Nelma Moreira, em `Teoricas/`). Numa fórmula
**já** em FND o teste é linear no tamanho da fórmula. Mas *obter* a FND
pode ser caro: cada distributividade duplica parte da fórmula, e no pior
caso a FND tem tamanho exponencial. Não se conhece algoritmo polinomial
para a satisfazibilidade de uma fórmula qualquer (problema **SAT**; um
algoritmo destes resolveria "P = NP?").

## Forma normal conjuntiva (FNC)

::: {.definicao title="--- Forma normal conjuntiva"}
Uma fórmula está em **forma normal conjuntiva** se é uma **conjunção de
disjunções de literais** ("um *e* de *ou*'s"):
$$(\alpha_{11} \lor \dots \lor \alpha_{1k_1}) \land \dots \land (\alpha_{n1} \lor \dots \lor \alpha_{nk_n})$$
Cada disjunção de literais chama-se uma **cláusula**.
:::

::: {.definicao title="--- Lema dual (tautologia de uma FNC)"}
Uma disjunção de literais $l_1 \lor \dots \lor l_n$ é **tautologia sse
contém um par complementar** (com $p \lor \neg p$ é sempre verdadeira;
sem par, pondo cada literal a $F$ falha). Logo uma FNC é **tautologia sse
todas as suas cláusulas o são**.
:::

A FND decide a **satisfazibilidade** (basta **uma** conjunção sem par); a
FNC decide se é **tautologia** (**todas** as cláusulas com par). O
contrário não é fácil: saber se uma FNC é satisfazível é o problema SAT.

A FNC obtém-se pelos mesmos dois caminhos, "ao contrário":

1. **Da tabela**: para cada linha em que $f$ dá **F**, a **disjunção** com
   a variável **negada se está a $V$** e **positiva se está a $F$**; a
   FNC é a **conjunção** dessas disjunções.
2. **Da fórmula**: passos 1 e 2 como na FND; no passo 3, distributividade
   do **$\lor$ sobre o $\land$**:
   $$(\phi \land \psi) \lor \theta \Leftrightarrow (\phi \lor \theta) \land (\psi \lor \theta)
   \qquad \theta \lor (\phi \land \psi) \Leftrightarrow (\theta \lor \phi) \land (\theta \lor \psi)$$

::: {.exemplo title="--- FNC a partir de uma tabela (a mesma função da FND acima)"}
Interessam as linhas com **F** (4, 6, 7, 8). Cada cláusula é **falsa
exatamente nessa linha**: cada literal tem de ser $F$ ali.

| linha | $x_1$ | $x_2$ | $x_3$ | $f$ | cláusula |
|---|---|---|---|---|---|
| 4 | V | F | F | F | $\neg p_1 \lor p_2 \lor p_3$ |
| 6 | F | V | F | F | $p_1 \lor \neg p_2 \lor p_3$ |
| 7 | F | F | V | F | $p_1 \lor p_2 \lor \neg p_3$ |
| 8 | F | F | F | F | $p_1 \lor p_2 \lor p_3$ |

Linha 4: $\neg p_1 \lor p_2 \lor p_3 = F \lor F \lor F = F$, e em
qualquer outra linha algum literal é $V$. A conjunção é $F$ exatamente
nas linhas 4, 6, 7, 8:
$$(\neg p_1 \lor p_2 \lor p_3) \land (p_1 \lor \neg p_2 \lor p_3) \land (p_1 \lor p_2 \lor \neg p_3) \land (p_1 \lor p_2 \lor p_3)$$
:::

::: {.exemplo title="--- FNC de $(p \\lor r) \\leftrightarrow (q \\land \\neg p)$ e é tautologia?"}
Os passos 1 e 2 são os da FND:
$$\big((\neg p \land \neg r) \lor (q \land \neg p)\big) \land \big((\neg q \lor p) \lor (p \lor r)\big)$$
O lado direito já é a cláusula $\neg q \lor p \lor p \lor r$. Falta o
esquerdo, um $\lor$ de $\land$'s.

**3a** --- com $\theta = \neg p \land \neg r$, $\phi = q$, $\psi = \neg p$
em $\theta \lor (\phi \land \psi) \Leftrightarrow (\theta \lor \phi) \land (\theta \lor \psi)$:
$$(\neg p \land \neg r) \lor (q \land \neg p) \Leftrightarrow \big((\neg p \land \neg r) \lor q\big) \land \big((\neg p \land \neg r) \lor \neg p\big)$$

**3b** --- outra vez, com $(a \land b) \lor c \Leftrightarrow (a \lor c) \land (b \lor c)$:

- $(\neg p \land \neg r) \lor q \Leftrightarrow (\neg p \lor q) \land (\neg r \lor q)$
- $(\neg p \land \neg r) \lor \neg p \Leftrightarrow (\neg p \lor \neg p) \land (\neg r \lor \neg p)$

**FNC** (5 cláusulas):
$$(\neg p \lor q) \land (\neg r \lor q) \land (\neg p \lor \neg p) \land (\neg r \lor \neg p) \land (\neg q \lor p \lor p \lor r)$$

**É tautologia? Não**: $\neg p \lor q$ não tem par complementar.
Contraexemplo, pondo os seus literais a $F$: $p=V$, $q=F$; de facto
$p \lor r = V$ e $q \land \neg p = F$. $\checkmark$
:::

**Simplificar.** Uma FND/FNC limpa-se com as leis extra da Aula 2. Acima:
$\neg p \lor \neg p \Leftrightarrow \neg p$ (idempotência) e
$\neg r \lor \neg p$ é absorvida por $\neg p$, ficando
$(\neg p \lor q) \land (\neg r \lor q) \land \neg p \land (\neg q \lor p \lor r)$;
com $p=F$ forçado sobra $(\neg r \lor q) \land (\neg q \lor r)$, isto é,
$q \leftrightarrow r$, como na FND. Uma FND/FNC não é única: qualquer
uma equivalente está certa.

### Aplicação aos exercícios da prática: FND/FNC

::: {.exemplo title="--- Exercício 1.17(a) (lab, proplogic.pdf) --- FND e FNC a partir da tabela"}
A coluna (com $p,q,r$ de $VVV$ a $FFF$) é $V, V, V, V, F, V, V, V$: só a
linha $p=F, q=V, r=V$ dá $F$.

**FNC** (uma cláusula por linha com $F$): $p$ a $F$ entra positivo, $q$ e
$r$ a $V$ entram negados:
$$p \lor \neg q \lor \neg r$$

**FND** (uma conjunção por linha com $V$, sete):

| $p$ | $q$ | $r$ | conjunção |
|---|---|---|---|
| V | V | V | $p \land q \land r$ |
| V | V | F | $p \land q \land \neg r$ |
| V | F | V | $p \land \neg q \land r$ |
| V | F | F | $p \land \neg q \land \neg r$ |
| F | V | F | $\neg p \land q \land \neg r$ |
| F | F | V | $\neg p \land \neg q \land r$ |
| F | F | F | $\neg p \land \neg q \land \neg r$ |

Juntando-as com $\lor$:
$$(p \land q \land r) \lor (p \land q \land \neg r) \lor (p \land \neg q \land r) \lor (p \land \neg q \land \neg r) \lor (\neg p \land q \land \neg r) \lor (\neg p \land \neg q \land r) \lor (\neg p \land \neg q \land \neg r)$$

Com **poucos $F$** a FNC sai mais curta; com **poucos $V$**, a FND.
:::

::: {.exemplo title="--- Exercício 1.18(d) (lab, proplogic.pdf) --- $(p \\to q) \\to (\\neg p \\to \\neg q)$"}
$$\begin{aligned}
&(p \to q) \to (\neg p \to \neg q) \\
\Leftrightarrow\ & \neg(p \to q) \lor (\neg p \to \neg q) && \text{(implicação, na } \to \text{ exterior)}\\
\Leftrightarrow\ & \neg(\neg p \lor q) \lor (\neg\neg p \lor \neg q) && \text{(implicação, nas duas interiores)}\\
\Leftrightarrow\ & (\neg\neg p \land \neg q) \lor (\neg\neg p \lor \neg q) && \text{(De Morgan)}\\
\Leftrightarrow\ & (p \land \neg q) \lor p \lor \neg q && \text{(dupla negação, 2 vezes; associatividade)}
\end{aligned}$$

**FND:** $(p \land \neg q) \lor p \lor \neg q$ já é FND (conjunções
$p \land \neg q$, $p$, $\neg q$). Por absorção
($p \lor (p \land \neg q) \Leftrightarrow p$): $p \lor \neg q$.

**FNC:** distribui-se o $\lor$ sobre o $\land$ em $(p \land \neg q) \lor (p \lor \neg q)$,
com $\theta = p \lor \neg q$:
$$(p \lor p \lor \neg q) \land (\neg q \lor p \lor \neg q) \Leftrightarrow (p \lor \neg q) \land (p \lor \neg q) \Leftrightarrow p \lor \neg q$$
(idempotência duas vezes). $p \lor \neg q$ é ao mesmo tempo FND e FNC.

Não é tautologia (a cláusula não tem par): com $p=F, q=V$, $p \to q = V$
e $\neg p \to \neg q = V \to F = F$. (A alínea (k) é igual a esta.)
:::

::: {.exemplo title="--- Exercício 1.18(h) (lab, proplogic.pdf) --- $(p \\to q) \\land (\\neg q \\to (p \\lor \\neg q))$"}
**Eliminar implicações:** $p \to q \Leftrightarrow \neg p \lor q$ e
$\neg q \to (p \lor \neg q) \Leftrightarrow \neg\neg q \lor p \lor \neg q \Leftrightarrow q \lor p \lor \neg q$:
$$(\neg p \lor q) \land (q \lor p \lor \neg q)$$

**FNC:** já é. A segunda cláusula tem $q$ e $\neg q$: é tautologia e sai
($\phi \land V \Leftrightarrow \phi$). FNC simplificada: $\neg p \lor q$.

**FND** (distribuição toda, para treinar): com $X = q \lor p \lor \neg q$,
$(\neg p \lor q) \land X \Leftrightarrow (\neg p \land X) \lor (q \land X)$,
e cada um distribui sobre os 3 literais de $X$:
$$(\neg p \land q) \lor (\neg p \land p) \lor (\neg p \land \neg q) \lor (q \land q) \lor (q \land p) \lor (q \land \neg q)$$
Apagam-se $\neg p \land p$ e $q \land \neg q$, e $q \land q \Leftrightarrow q$:
$$(\neg p \land q) \lor (\neg p \land \neg q) \lor q \lor (p \land q)$$
Por absorção ($q$ absorve $\neg p \land q$ e $p \land q$) sobra
$(\neg p \land \neg q) \lor q \Leftrightarrow (\neg p \lor q) \land (\neg q \lor q) \Leftrightarrow \neg p \lor q$,
o mesmo da FNC. $\checkmark$

Detetar cedo uma cláusula-tautologia (ou uma conjunção contraditória)
poupa a distribuição.
:::

::: {.pratica title="--- Formas normais (proplogic.pdf)"}
- **1.17 (b)** e **(c)** --- FND e FNC pela tabela. Na (c), olha bem para a
  coluna antes de começar: há uma fórmula muito mais curta escondida (as
  formas canónicas saem longas, mas simplificam-se).
- **1.18 (e)** --- é a Lei de Peirce (Aula 2): o que acontece à FNC de uma
  tautologia?
- **1.18 (l)** --- a mais comprida, boa para treinar a distributividade
  com 4 variáveis.
- **1.20** --- o programa: valoração, tabela, classificação e FNC/FND
  (junta tudo o que viste até aqui).

As restantes alíneas de 1.18 são a mesma técnica; não precisas de as fazer
todas (e repara que (a) = (c) e (d) = (k) no próprio enunciado).
:::

## Fórmulas de Horn

::: {.definicao title="--- Fórmula de Horn"}
Uma **fórmula de Horn** é uma **FNC** em que **cada cláusula tem no
máximo um literal positivo**. Exemplos (nº de positivos por cláusula):

- $p \land \neg q \land (q \lor \neg p)$: 1, 0, 1 → Horn.
- $(\neg p \lor \neg q \lor \neg s \lor p) \land (\neg q \lor \neg r \lor p) \land (\neg p \lor \neg s \lor s)$:
  1, 1, 1 → Horn.
- $(\neg p \lor \neg q \lor \neg s) \land (\neg q \lor \neg r \lor p) \land s$:
  0, 1, 1 → Horn.
- $(p \lor q) \land \neg r$ **não** é Horn: $p \lor q$ tem dois positivos.
:::

Cada cláusula de Horn lê-se como uma **implicação**
($\neg a \lor b \Leftrightarrow a \to b$ e
$\neg p_1 \lor \dots \lor \neg p_n \Leftrightarrow \neg(p_1 \land \dots \land p_n)$):

| forma da cláusula | lida como implicação | nome informal |
|---|---|---|
| $\neg p_1 \lor \dots \lor \neg p_n \lor p$ | $(p_1 \land \dots \land p_n) \to p$ | regra |
| $\neg p_1 \lor \dots \lor \neg p_n$ (sem positivo) | $(p_1 \land \dots \land p_n) \to F$ | restrição |
| $p$ (sem negativos) | $V \to p$ | facto |

Nem todas as fórmulas têm uma fórmula de Horn equivalente (ex.:
$p \lor q$). A vantagem das de Horn é que a satisfazibilidade se decide
com um **algoritmo eficiente** (polinomial).

### Algoritmo de satisfazibilidade para fórmulas de Horn

Começa-se com todas as variáveis por decidir e só se põe uma a $V$ quando
é **obrigatório** (senão uma cláusula ficava falsa). Se as atribuições
obrigatórias tornam uma cláusula $F$, a fórmula é insatisfazível; senão,
as restantes ficam a $F$ e a fórmula fica satisfeita.

::: {.definicao title="--- Algoritmo"}
1. Escrever numa linha as variáveis e a fórmula (uma linha de tabela de
   verdade, vazia).
2. Cada **variável sozinha** na conjunção (um **facto**) fica a $V$: uma
   conjunção só é $V$ se cada elemento o for.
3. Se numa cláusula todos os literais negativos já estão a $F$ (as suas
   variáveis estão a $V$), o **literal positivo** tem de ser $V$ →
   atribuir-lhe $V$.
4. Repetir o passo 3 até nada mudar.
5. Se algum elemento da conjunção ficou $F$ → **não satisfazível**. Senão
   → **satisfazível**: as variáveis restantes ficam a $F$.
:::

::: {.exemplo title="--- $p \\land \\neg q \\land (q \\lor \\neg p)$"}
Cláusulas: $C_1 = p$, $C_2 = \neg q$, $C_3 = q \lor \neg p$ ($p \to q$).

**Passo 1** --- linha vazia:

| $p$ | $q$ | $C_1 = p$ | $C_2 = \neg q$ | $C_3 = q \lor \neg p$ |
|---|---|---|---|---|
| | | | | |

**Passo 2** --- $p$ é um facto → $p = V$:

| $p$ | $q$ | $C_1 = p$ | $C_2 = \neg q$ | $C_3 = q \lor \neg p$ |
|---|---|---|---|---|
| V | | V | | ($\neg p = F$) |

**Passo 3** --- em $C_3$, $\neg p$ é $F$; para $C_3$ ser $V$, $q = V$:

| $p$ | $q$ | $C_1 = p$ | $C_2 = \neg q$ | $C_3 = q \lor \neg p$ |
|---|---|---|---|---|
| V | V | V | | V |

**Passo 4** --- repete-se: $C_2 = \neg q$ com $q = V$ dá $F$:

| $p$ | $q$ | $C_1 = p$ | $C_2 = \neg q$ | $C_3 = q \lor \neg p$ |
|---|---|---|---|---|
| V | V | V | **F** | V |

**Passo 5** --- $C_2$ ficou $F$ → **não é satisfazível** ($p=V$ e $q=V$
foram ambos obrigatórios).
:::

**Porque é que o algoritmo está correto†** (é o Exercício 1.21(b)):

- **"Insatisfazível" está certo:** cada $V$ atribuído foi obrigatório,
  isto é, qualquer valoração que satisfaça a fórmula o tem. Se essas
  atribuições já tornam uma cláusula $F$, nenhuma valoração a satisfaz.
- **"Satisfazível" está certo:** com as marcadas a $V$ e as outras a $F$,
  seja uma cláusula qualquer. Se o seu positivo está marcado, é $V$.
  Senão, algum negativo $\neg x$ tem $x$ **não** marcado (se todos
  estivessem, o passo 3 marcava o positivo ou, sem positivo, a cláusula
  era $F$ e o passo 5 parava); logo $x = F$, $\neg x = V$ e a cláusula é
  $V$.

É aqui que conta "no máximo um positivo": pôr as restantes a $F$ torna
verdadeiros todos os negativos por decidir, e nunca é preciso escolher
entre dois positivos. Nunca há retrocesso.

::: {.exemplo title="--- O algoritmo em pseudo-código (base para o Exercício 1.21(a))"}
Cada cláusula vista como $(p_1 \land \dots \land p_n) \to h$, com $h$ uma
variável ou $F$ ($n = 0$ para factos):

```
marcadas := {}                       -- variáveis que TÊM de ser V
repetir
  mudou := falso
  para cada cláusula (p1 e ... e pn) -> h:
    se p1,...,pn estão todos em marcadas:   -- antecedente todo V
      se h = F: devolver INSATISFAZÍVEL
      se h não está em marcadas:
        acrescentar h a marcadas; mudou := verdadeiro
até não mudou
devolver SATISFAZÍVEL   -- v(x)=V se x em marcadas, senão v(x)=F
```

Cada volta marca uma variável nova (ou pára): no máximo (nº de variáveis
+ 1) voltas, polinomial.
:::

::: {.exemplo title="--- Exercício 1.21(c), 1.ª e 2.ª fórmulas (lab, proplogic.pdf)"}
Os valores escrevem-se por baixo de cada literal, à medida que se
propagam.

**(i) $(\neg p \lor \neg q) \land (\neg q \lor r) \land q$.** $q$ é um
elemento da conjunção, logo $q = V$ (os literais $\neg q$ ficam F):

| $p$ | $q$ | $r$ | $\neg p \lor \neg q$ | $\neg q \lor r$ | $q$ |
|:-:|:-:|:-:|:-:|:-:|:-:|
| | V | | $\cdot$ F | F $\cdot$ | V |

Em $\neg q \lor r$ o único negativo é F, logo $r = V$. Não há mais
propagação, nenhum elemento ficou F, e $p$ fica a F:

| $p$ | $q$ | $r$ | $\neg p \lor \neg q$ | $\neg q \lor r$ | $q$ |
|:-:|:-:|:-:|:-:|:-:|:-:|
| F | V | V | V F | F V | V |

**Satisfazível** para $v(p)=F$, $v(q)=v(r)=V$.

**(ii) $p \land (\neg p \lor q) \land (\neg q \lor p)$.** $p$ é elemento
da conjunção, logo $p = V$; em $\neg p \lor q$ o negativo fica F, logo
$q = V$; $\neg q \lor p$ já tem $p = V$. Não há mais propagação e nenhum
elemento ficou F:

| $p$ | $q$ | $p$ | $\neg p \lor q$ | $\neg q \lor p$ |
|:-:|:-:|:-:|:-:|:-:|
| V | V | V | F V | F V |

**Satisfazível** para $v(p)=v(q)=V$.
:::

::: {.pratica title="--- Horn (proplogic.pdf)"}
- **1.21 (c)**, 3.ª e 4.ª fórmulas: $\neg p \land (\neg p \lor q) \land \neg q$
  (o que acontece quando **não há nenhum facto**?) e
  $p \land (\neg p \lor q) \land \neg r$.
- **1.21 (a)** --- implementar o algoritmo a partir do pseudo-código acima.
:::

# Aula 4 --- Satisfazibilidade: cláusulas e o algoritmo de Davis-Putnam

## O problema SAT

Decidir se uma fórmula é satisfazível é um problema central na
informática, porque muitos problemas se escrevem como uma fórmula e "há
solução?" passa a ser "a fórmula é satisfazível?": otimização
(planeamento, horários), combinatória (coloração de grafos) e teorias da
lógica de primeira ordem (programação linear, aritmética real, *bits*,
apontadores: os ***SMT solvers***).

Fora da FND e de classes fáceis como Horn, **no pior caso** não se conhece
algoritmo que não seja **exponencial** (**SAT é NP-completo**). Mas há
algoritmos muito melhores do que a tabela inteira: em vez de gerar
valorações completas e testar cada uma, **constrói-se uma valoração
parcial**. Fica simples com fórmulas em **FNC**, escritas como conjuntos
de **cláusulas**.

## Cláusulas

::: {.definicao title="--- Cláusula"}
Uma **cláusula** é uma disjunção de literais $l_1 \lor \dots \lor l_n$,
$n \geq 0$, representada pelo **conjunto** $\{l_1, \dots, l_n\}$. Com
$n = 1$ é **unitária**. Uma **FNC** é um **conjunto de cláusulas** (a
conjunção fica implícita). Ex.: $p \lor \neg q \lor \neg p \lor s$ é
$\{p, \neg q, \neg p, s\}$.

Os dois "vazios"† são diferentes:

- **cláusula vazia** ($n = 0$, escreve-se $F$): uma disjunção sem
  literais é **falsa**; um conjunto que a contém é **insatisfazível**;
- **conjunto de cláusulas vazio**: uma conjunção sem termos é
  **verdadeira** (nenhuma cláusula falha); é **satisfazível**.
:::

::: exemplo
$$\neg p \land (q \lor r \lor q) \land (\neg r \lor \neg s) \land (p \lor s) \land (\neg q \lor \neg s)$$
é o conjunto de cláusulas
$$\{\{\neg p\},\ \{q, r\},\ \{\neg r, \neg s\},\ \{p, s\},\ \{\neg q, \neg s\}\}$$
$q \lor r \lor q$ fica $\{q, r\}$: um conjunto não tem repetidos
(idempotência). Pela mesma razão, uma cláusula repetida conta uma vez.
:::

::: {.definicao title="--- Literal complementar"}
$$\tilde{l} = \begin{cases} \neg l, & \text{se } l \text{ é uma variável (positivo)} \\ p, & \text{se } l \text{ é da forma } \neg p \text{ (negativo)} \end{cases}$$
Ex.: $\tilde{p} = \neg p$ e $\widetilde{\neg p} = p$.
:::

Uma cláusula com um par complementar $p$, $\neg p$ é **tautologia** e
**pode retirar-se** sem alterar a satisfazibilidade ($V \land \varphi
\Leftrightarrow \varphi$). Ex.: $\{p, \neg q, \neg p, s\}$ sai.

## Propagação unitária

O algoritmo de **Davis-Putnam** experimenta valores para as variáveis e
simplifica a fórmula com eles até poder concluir. A simplificação
principal é a **propagação unitária**.

::: {.definicao title="--- Propagação unitária"}
Seja $S$ um conjunto de cláusulas. Enquanto $S$ contém uma **cláusula
unitária** $l$:

1. **retiram-se** de $S$ todas as cláusulas que contêm $l$ (incluindo a
   própria $l$);
2. em cada cláusula que contém $\tilde{l}$, **tira-se** $\tilde{l}$
   ($\tilde{l} \lor C'$ passa a $C'$).

**Porquê†.** Qualquer valoração que satisfaça $S$ tem $l = V$ ($l$ é um
elemento da conjunção, como um facto de Horn). Com $l = V$, uma cláusula
com $l$ é $V$ e sai; numa com $\tilde{l}$, esse literal é $F$ e não ajuda
($F \lor C' \Leftrightarrow C'$). Se uma cláusula era só $\tilde{l}$,
fica **vazia** ($F$): $S$ é insatisfazível. Os literais propagados dão os
valores das variáveis numa valoração que satisfaça $S$.
:::

::: {.exemplo title="--- Só com propagação (1/2)"}
$$S = \{p_1,\ \neg p_1 \lor \neg p_2,\ p_3 \lor p_2,\ \neg p_7 \lor p_2,\ \neg p_3 \lor p_4,\ \neg p_3 \lor p_5,$$
$$\neg p_4 \lor \neg p \lor q,\ \neg p_5 \lor \neg p_6 \lor r,\ \neg p \lor \neg q \lor p_6,\ p \lor p_7,\ \neg r \lor p_7\}$$

**Propagar $p_1$.** Sai $p_1$. $\neg p_1 \lor \neg p_2$ fica $\neg p_2$.
$$\{\neg p_2,\ p_3 \lor p_2,\ \neg p_7 \lor p_2,\ \neg p_3 \lor p_4,\ \neg p_3 \lor p_5,\ \neg p_4 \lor \neg p \lor q,\ \neg p_5 \lor \neg p_6 \lor r,\ \neg p \lor \neg q \lor p_6,\ p \lor p_7,\ \neg r \lor p_7\}$$

**Propagar $\neg p_2$.** Sai $\neg p_2$. O complementar é $p_2$:
$p_3 \lor p_2$ fica $p_3$ e $\neg p_7 \lor p_2$ fica $\neg p_7$.
$$\{p_3,\ \neg p_7,\ \neg p_3 \lor p_4,\ \neg p_3 \lor p_5,\ \neg p_4 \lor \neg p \lor q,\ \neg p_5 \lor \neg p_6 \lor r,\ \neg p \lor \neg q \lor p_6,\ p \lor p_7,\ \neg r \lor p_7\}$$

**Propagar $p_3$.** Sai $p_3$. $\neg p_3 \lor p_4$ fica $p_4$;
$\neg p_3 \lor p_5$ fica $p_5$.

**Propagar $\neg p_7$.** Sai $\neg p_7$. $p \lor p_7$ fica $p$;
$\neg r \lor p_7$ fica $\neg r$.
$$\{p_4,\ p_5,\ \neg p_4 \lor \neg p \lor q,\ \neg p_5 \lor \neg p_6 \lor r,\ \neg p \lor \neg q \lor p_6,\ p,\ \neg r\}$$
:::

::: {.exemplo title="--- Só com propagação (2/2)"}
**Propagar $p_4$.** $\neg p_4 \lor \neg p \lor q$ fica $\neg p \lor q$.

**Propagar $p_5$.** $\neg p_5 \lor \neg p_6 \lor r$ fica $\neg p_6 \lor r$.

**Propagar $\neg r$.** $\neg p_6 \lor r$ fica $\neg p_6$.

**Propagar $p$.** Sai $p$. $\neg p \lor q$ fica $q$;
$\neg p \lor \neg q \lor p_6$ fica $\neg q \lor p_6$.
$$\{q,\ \neg p_6,\ \neg q \lor p_6\}$$

**Propagar $q$.** $\neg q \lor p_6$ fica $p_6$: $\{\neg p_6,\ p_6\}$.

**Propagar $\neg p_6$.** Sai $\neg p_6$; $p_6$ perde o único literal e
fica **vazia**:
$$\{F\}$$

**Insatisfazível**, só com propagação. Os slides propagam alguns literais
ao mesmo tempo; a ordem não altera o resultado.
:::

## O algoritmo DLL

Quando a propagação pára sem conclusão (sem unitárias, $S$ não vazio e
sem $F$), **escolhe-se** um literal e experimentam-se os dois valores.

::: {.definicao title="--- Algoritmo de Davis-Putnam (DLL)"}
```
DLL(S)
  input:  conjunto de clausulas S
  output: satisfazivel ou insatisfazivel
  S := propagate(S)
  if S vazio then return satisfazivel
  if S contem F then return insatisfazivel
  l := select_literal(S)
  if DLL(S uniao {l}) = satisfazivel
    then return satisfazivel
    else return DLL(S uniao {~l})       -- ~l: o complementar de l
```

- Acrescentar $\{l\}$ é **supor $l = V$**; a propagação da chamada
  recursiva faz o resto.
- Se dá insatisfazível, **volta-se atrás** (*backtracking*) e supõe-se
  $\tilde{l}$. "Insatisfazível" só quando **os dois ramos** falham.
- Quando responde "satisfazível", os literais **supostos** e
  **propagados** no ramo que teve sucesso formam uma valoração que
  satisfaz $S$†; as variáveis que não apareceram podem ter qualquer valor.
:::

`select_literal` devolve um literal de uma das cláusulas: é um
**parâmetro** do algoritmo, e uma boa escolha torna-o muito mais
eficiente. Critérios: a variável que **ocorre mais vezes**; a que tem o
**produto** das ocorrências de $l$ e de $\tilde{l}$ **máximo**; a que
ocorre mais em **cláusulas de tamanho mínimo**; etc.

::: {.exemplo title="--- É preciso escolher"}
$$S = \{\neg p \lor \neg q,\ \neg p \lor q,\ p \lor \neg q,\ p \lor q\}$$

Sem unitárias: a propagação não faz nada. Escolhe-se **$\neg p$**.

**Ramo $S \cup \{\neg p\}$.** Propagar $\neg p$: saem $\neg p \lor \neg q$
e $\neg p \lor q$; $p \lor \neg q$ fica $\neg q$ e $p \lor q$ fica $q$:
$\{\neg q, q\}$. Propagar $\neg q$: $q$ fica vazia, $\{F\}$. **Falha.**

**Ramo $S \cup \{p\}$.** Propagar $p$: saem $p \lor \neg q$ e $p \lor q$;
$\neg p \lor \neg q$ fica $\neg q$ e $\neg p \lor q$ fica $q$.
$\{\neg q, q\} \Rightarrow \{F\}$. **Falha.**

Os dois ramos falham: **insatisfazível** (as quatro cláusulas proíbem as
quatro combinações de $p$ e $q$).
:::

::: {.exemplo title="--- Exercício 1.22(a) (lab, proplogic.pdf)"}
$$S = \{p \lor q \lor r,\ \neg p \lor \neg q \lor \neg r,\ p \lor \neg q \lor \neg r,\ p \lor q \lor \neg r,\ \neg p \lor q,\ \neg p \lor r,\ p \lor \neg q \lor r\}$$

Não há cláusulas unitárias; escolhe-se $p$ (está nas 7 cláusulas) e
chama-se DLL$(S \cup \{p\})$. A propagação unitária de $p$ (saem as 4
cláusulas com $p$; tira-se $\neg p$ das outras 3) dá
$$S_1 = \{\neg q \lor \neg r,\ q,\ r\}$$
A propagação de $q$ dá $S_2 = \{\neg r,\ r\}$, e a de $r$ dá $\{F\}$.

Volta-se ao último ponto de escolha e chama-se DLL$(S \cup \{\neg p\})$.
A propagação unitária de $\neg p$ dá
$$S_3 = \{q \lor r,\ \neg q \lor \neg r,\ q \lor \neg r,\ \neg q \lor r\}$$
Não há cláusulas unitárias; escolhe-se $q$ e chama-se
DLL$(S_3 \cup \{q\})$. A propagação de $q$ dá $S_4 = \{\neg r,\ r\}$, e a
de $r$ dá $\{F\}$. Volta-se atrás: DLL$(S_3 \cup \{\neg q\})$; a
propagação de $\neg q$ dá $S_5 = \{r,\ \neg r\}$, e a de $r$ dá $\{F\}$.

Todos os ramos falham: $S$ é **insatisfazível**.

![](figuras/dll_arvore_1_22a.pdf){width=62%}
:::

::: {.pratica title="--- Davis-Putnam (proplogic.pdf, 1.22 e 1.23)"}
- **1.22 (c)** $\{p \lor \neg q \lor \neg r,\ \neg p \lor q \lor r,\ \neg p
  \lor q \lor r,\ \neg p \lor q,\ \neg p \lor r\}$. Repara na cláusula
  repetida. Depois de escolher o primeiro literal, a propagação faz o
  resto.
- **1.22 (e)** $\{p \lor \neg q \lor \neg r,\ \neg p \lor q \lor r,\ \neg p
  \lor \neg q \lor \neg r,\ \neg p \lor \neg q \lor r,\ \neg p \lor q \lor
  \neg r,\ p \lor q \lor \neg r\}$. Começa por $p$, como na 1.22(a); aqui
  é preciso voltar atrás antes de encontrar uma valoração. Diz qual é.
- **1.23** Implementar o algoritmo DLL (propagação + escolha + volta
  atrás), a partir do pseudo-código acima.

A 1.22(b) e a 1.22(d) são a mesma técnica com outros conjuntos; não é
preciso fazê-las todas.
:::

# Aulas 5--7 --- Dedução Natural

Falta a terceira parte de uma lógica, o **sistema de dedução**: regras
puramente sintáticas para obter fórmulas a partir de outras, sem falar em
valorações. O sistema é a **dedução natural (DN)**, na **notação de
Fitch**, pedida em todos os exercícios da folha 2 ("All deductions must
use the DN natural deduction system and the Fitch notation given in
class").

## Semântica versus dedução

| | Semântica | Dedução |
|---|---|---|
| Notação | $\Gamma \models \phi$ | $\Gamma \vdash \phi$ |
| Lê-se | $\phi$ é consequência semântica de $\Gamma$ | $\phi$ deduz-se de $\Gamma$ |
| Significa | toda a valoração que satisfaz $\Gamma$ satisfaz $\phi$ | existe uma dedução (sequência de passos, cada um dado por uma regra) de $\phi$ a partir de $\Gamma$ |
| Natureza | fala de valores de verdade | só manipula símbolos (**sintática**) |

$$\begin{aligned}
\Gamma \models \phi \quad &\xrightarrow{\ \text{completude}\ } \quad \Gamma \vdash \phi\\
\Gamma \vdash \phi \quad &\xrightarrow{\ \text{integridade (\emph{soundness})}\ } \quad \Gamma \models \phi
\end{aligned}$$

::: {.definicao title="--- Integridade e completude"}
- Um sistema dedutivo é **íntegro** (*correto*, *sound*) se tudo o que se
  deduz é consequência semântica: se $\Gamma \vdash \phi$ então
  $\Gamma \models \phi$. Em particular, se $\vdash \phi$, $\phi$ é
  tautologia.
- É **completo** se tudo o que é consequência semântica se deduz: se
  $\Gamma \models \phi$ então $\Gamma \vdash \phi$. Em particular, toda a
  tautologia tem uma dedução sem premissas.

DN é **íntegra e completa** para a lógica proposicional:
$\Gamma \vdash \phi$ sse $\Gamma \models \phi$ (provas nas Aulas 9--10).
:::

Um sistema de dedução dá um método automático, ou semi-automático, de
mostrar que uma fórmula é válida ou consequência de outras sem percorrer
as valorações (que na lógica de primeira ordem deixam de ser finitas):
cada passo verifica-se só pela forma das fórmulas.

**Como se mostra $\Gamma \nvdash \phi$.** Não basta não encontrar uma
dedução. Pela **integridade**, se existisse ter-se-ia
$\Gamma \models \phi$; basta por isso um **contraexemplo**, uma valoração
$v$ com $\models_v \gamma$ para todo o $\gamma \in \Gamma$ e
$\not\models_v \phi$ (verificada com as regras de $\models_v$). Então
$\Gamma \not\models \phi$ e, pela integridade de DN, $\Gamma \nvdash \phi$.
É assim que se respondem as alíneas "não é válida" das 2.4, 2.9 e 2.10.

## Raciocínios válidos e contraexemplos

Um **raciocínio** é uma sequência de afirmações em que uma, a
**conclusão**, deve ser consequência das outras, as **premissas**:

| | |
|:-:|:--------------------------------------------|
| 1 | Se o Paulo adormecer e alguém o acordar, ele pragueja |
| 2 | O Paulo adormeceu |
| 3 | Ele não disse palavrões |
| 4 | **Logo:** ninguém o acordou |

Só interessa a estrutura lógica. Com $p$ = "o Paulo adormece", $q$ =
"alguém o acorda" e $r$ = "ele pragueja":
$$(p\land q)\to r,\ \ p,\ \ \neg r \quad\text{logo}\quad \neg q.$$

::: definicao
- O raciocínio é **válido** se a conclusão é **consequência lógica** das
  premissas: verdadeira sempre que as premissas o são (aqui,
  $\{(p\land q)\to r,\ p,\ \neg r\} \models \neg q$).
- Um raciocínio válido com premissas **de facto** verdadeiras é
  **sólido** (*sound*; não confundir com um sistema dedutivo *sound*,
  isto é, íntegro).
- Para mostrar que **não** é válido: um **contraexemplo**, uma situação
  com as premissas verdadeiras e a conclusão falsa.
- Para mostrar que **é**: uma **sucessão de passos**, cada um
  consequência dos anteriores e das premissas. Formalizar isto dá os
  **sistemas de dedução**.
:::

Outro raciocínio válido: "Se chumbas, tens de repetir. Se não estudas,
chumbas. Não estás a repetir. Logo: estudas, ou chumbas, ou as duas." Com
$r$ = "chumbas", $t$ = "repetes" e $e$ = "estudas":
$$r\to t,\ \ \neg e\to r,\ \ \neg t \quad\text{logo}\quad e\lor r\lor(e\land r).$$
A dedução fica como exercício na secção da implicação.

## Sistemas dedutivos axiomáticos

::: {.definicao title="--- Sistema dedutivo axiomático $\\mathcal{D}$ e dedução"}
Um sistema dedutivo $\mathcal{D}$ (à Hilbert) tem **axiomas** (fórmulas de
base que traduzem as propriedades dos conectivos) e **regras de
inferência** (maneiras de obter fórmulas a partir de outras).

Uma **dedução** de $\phi_n$ em $\mathcal{D}$ a partir de $\Sigma$ é uma
sucessão **finita** $\phi_1, \dots, \phi_n$ em que cada $\phi_i$
pertence a $\Sigma$ (premissa), **ou** é um axioma, **ou** resulta de
fórmulas anteriores por uma regra. Escreve-se $\Sigma \vdash_{\mathcal{D}} \phi_n$.

- Se $\Sigma = \emptyset$, $\phi_n$ é um **teorema** ($\vdash_{\mathcal{D}} \phi_n$)
  e a dedução é uma **prova** de $\phi_n$.
- Com $\Sigma = \{\theta_1, \dots, \theta_n\}$ finito, escreve-se
  $\theta_1, \dots, \theta_n \vdash_{\mathcal{D}} \phi$, ou só
  $\theta_1, \dots, \theta_n \vdash \phi$.
:::

Um exemplo concreto, o sistema de Hilbert $\mathcal{H}$, está na Aula 8.

::: {.definicao title="--- Equivalência dedutiva ($\\dashv\\vdash$)"}
(Aula 7; usada nas 2.11 e 2.12.)
$\phi \dashv\vdash \psi$ se $\phi \vdash \psi$ **e** $\psi \vdash \phi$:
são **duas deduções**, uma em cada sentido.
:::

## Dedução natural (DN) e a notação de Fitch

As regras de DN imitam o raciocínio de uma prova matemática. Em relação a
um sistema à Hilbert, DN **não tem axiomas**, só regras, e permite
**introduzir hipóteses a meio** ("suponhamos que..."), que têm de ser
**descartadas** antes do fim. Para cada conectivo ($\land$, $\lor$,
$\neg$, $\mathbf{F}$, $\to$) há regras de **introdução** (como se chega a
uma fórmula com esse conectivo) e de **eliminação** (o que se tira dela).

::: {.exemplo title="--- A ideia, num exemplo informal"}
Porque é que $(p \lor (q\land r)) \to ((p\lor q)\land(p\lor r))$ é
tautologia?

- **Supõe-se** o antecedente, $p\lor(q\land r)$. É uma disjunção, por
  isso há **dois casos**:
    - **caso $p$**: então $p\lor q$ e $p\lor r$, logo $(p\lor q)\land(p\lor r)$;
    - **caso $q\land r$**: então $q$ e $r$; daí $p\lor q$ e $p\lor r$,
      logo $(p\lor q)\land(p\lor r)$.
- Nos dois casos chega-se ao consequente; como **supondo** o antecedente
  se obteve o consequente, conclui-se a implicação.

Cada "então" é uma regra de DN; a prova formal está na secção da
implicação.
:::

**Representação das regras.** "De $\phi_1 \dots \phi_k$ infere-se $\phi$"
desenha-se como uma fração, $\dfrac{\phi_1 \quad \cdots \quad \phi_k}{\phi}$,
e uma dedução como uma **árvore** (folhas = premissas, raiz =
conclusão). Ex.: $p\land q,\ r \vdash q\land r$:
$$\dfrac{\dfrac{p\land q}{q}\,{\scriptstyle\land\mathrm{E}_2} \qquad r}{q\land r}\,{\scriptstyle\land\mathrm{I}}$$
As árvores crescem depressa; por isso usa-se a **notação de Fitch**,
linear:

::: {.definicao title="--- Notação de Fitch"}
- Cada passo numa linha **numerada**, com a **justificação** à direita:
  a regra e os **números das linhas** usadas (ex.: "$\land$E, 1";
  "$\land$I, 3, 2").
- As **premissas** vêm primeiro, sem justificação, com um **traço
  horizontal** por baixo da última.
- A **barra vertical** marca o alcance das hipóteses. Uma
  **sub-dedução** abre uma barra mais à direita, com a hipótese
  sublinhada no topo; quando acaba, a barra fecha.
- Uma regra que usa uma sub-dedução inteira cita o intervalo de linhas
  (ex.: "$\lor$E, 1, 2--3, 4--5").
:::

O exemplo da árvore, em Fitch:

```{.fitch seq="p /\ q, r |- q /\ r"}
p /\ q
r
---
q               ; &E, 1
q /\ r          ; &I, 3, 2
```

A tabela com todas as regras de DN está na última página da folha 2
(`Praticas/Semana_3/proplogicproofs.pdf`).

## Regras da conjunção

::: {.definicao title="--- Introdução e eliminação de $\\land$"}
$$\dfrac{\phi \qquad \psi}{\phi\land\psi}\,{\scriptstyle\land\mathrm{I}}
\qquad\qquad
\dfrac{\phi\land\psi}{\phi}\,{\scriptstyle\land\mathrm{E}_1}
\qquad
\dfrac{\phi\land\psi}{\psi}\,{\scriptstyle\land\mathrm{E}_2}$$

- **$\land$I**: se já se deduziu $\phi$ **e** $\psi$ (em linhas
  anteriores, por qualquer ordem), deduz-se $\phi\land\psi$.
- **$\land$E**: de $\phi\land\psi$ deduz-se $\phi$, e também $\psi$ (em
  Fitch as duas chamam-se "$\land$E").
:::

::: {.exemplo title="--- $(p\land q)\land r \vdash r\land q$"}
Desmonta-se a premissa com $\land$E e monta-se o resultado com $\land$I:

```{.fitch seq="(p /\ q) /\ r |- r /\ q"}
(p /\ q) /\ r
---
p /\ q          ; &E, 1
r               ; &E, 1
q               ; &E, 2
r /\ q          ; &I, 3, 4
```

A linha 5 cita "3, 4": $r$ (linha 3) é o lado esquerdo e $q$ (linha 4) o
direito.
:::

::: {.pratica title="--- Conjunção (proplogicproofs.pdf)"}
- **2.11 (c)** $(\psi\land\phi)\land\delta \dashv\vdash \psi\land(\phi\land\delta)$.
  São duas deduções (uma em cada sentido), só com $\land$E e $\land$I.
:::

## Regras da disjunção

::: {.definicao title="--- Introdução e eliminação de $\\lor$"}
$$\dfrac{\phi}{\phi\lor\psi}\,{\scriptstyle\lor\mathrm{I}_1}
\qquad
\dfrac{\psi}{\phi\lor\psi}\,{\scriptstyle\lor\mathrm{I}_2}
\qquad\qquad
\dfrac{\phi\lor\psi \qquad \begin{array}{c}[\phi]\\ \vdots\\ \gamma\end{array} \qquad \begin{array}{c}[\psi]\\ \vdots\\ \gamma\end{array}}{\gamma}\,{\scriptstyle\lor\mathrm{E}}$$

- **$\lor$I**: de $\phi$ deduz-se **qualquer** disjunção com $\phi$ de um
  dos lados ($\phi\lor\psi$ ou $\psi\lor\phi$).
- **$\lor$E** (**por casos**): se já se deduziu $\phi\lor\psi$, **supondo**
  $\phi$ se deduz $\gamma$ (numa sub-dedução) e **supondo** $\psi$ se
  deduz $\gamma$ (noutra), então deduz-se $\gamma$. $[\phi]$ marca o
  início de uma sub-dedução com a hipótese $\phi$, que só vale lá dentro.

Em Fitch, $\lor$E cita a linha da disjunção e os dois intervalos; as duas
sub-deduções têm de acabar **na mesma fórmula** $\gamma$.
:::

::: {.exemplo title="--- $(p\land q)\lor(q\land r) \vdash q$"}
A premissa é uma disjunção: dois casos, e em cada um tira-se $q$ com
$\land$E.

```{.fitch seq="(p /\ q) \/ (q /\ r) |- q"}
(p /\ q) \/ (q /\ r)
---
|> p /\ q
|  q                 ; &E, 2
|> q /\ r
|  q                 ; &E, 4
q                    ; vE, 1, 2-3, 4-5
```

Linhas 2--3: caso $p\land q$; linhas 4--5: caso $q\land r$. Como as duas
acabam em $q$, $\lor$E dá $q$ na linha 6, **fora** das sub-deduções.
:::

### Repetição

Pode sempre **repetir-se** uma fórmula já obtida e acessível: regra **R**,
$\dfrac{\phi}{\phi}\,{\scriptstyle\mathrm{R}}$. Faz falta quando um caso
de $\lor$E já é a conclusão:

::: {.exemplo title="--- $(p\land q)\lor q \vdash q$"}
```{.fitch seq="(p /\ q) \/ q |- q"}
(p /\ q) \/ q
---
|> p /\ q
|  q                 ; &E, 2
|> q
|  q                 ; R, 4
q                    ; vE, 1, 2-3, 4-5
```

No segundo caso a hipótese já é $q$, mas a sub-dedução tem de terminar em
$q$ com um passo seu: a linha 5 repete a 4.
:::

### Alcance das sub-deduções

::: {.definicao title="--- Alcance das hipóteses"}
Uma sub-dedução começa com **hipóteses novas**, e tudo o que se deduz lá
dentro **depende delas**. Quando acaba, as hipóteses deixam de estar
assumidas: **nem elas nem nada do que se deduziu lá dentro pode ser usado
depois**.

Em Fitch, a linha $k$ pode citar a linha $a$ só se $a < k$ **e** todas
as barras abertas na linha $a$ ainda estão abertas na linha $k$. Uma
sub-dedução inteira ($i$--$j$) só pode ser citada depois do seu fim, ao
nível da barra imediatamente à esquerda.
:::

::: {.exemplo title="--- Uma dedução ERRADA"}
```{.fitch .nocheck}
(p /\ q) \/ (q /\ r)
---
|> p /\ q
|  p                 ; &E, 2
|  q                 ; &E, 2
|> q /\ r
|  q                 ; &E, 5
q                    ; vE, 1, 2-4, 5-6
q /\ p               ; &I, 7, 3
```

O passo 8 está **errado**: usa a linha 3 ($p$), de uma sub-dedução (2--4)
**já terminada**. Esse $p$ só valia no caso $p\land q$.

Nem há correção possível: $q\land p$ não é consequência semântica da
premissa (contraexemplo $v(p)=F$, $v(q)=V$, $v(r)=V$:
$\models_v q\land r$, logo $\models_v (p\land q)\lor(q\land r)$, mas
$\not\models_v p$, logo $\not\models_v q\land p$). Pela integridade, não
existe dedução.
:::

::: {.exemplo title="--- $p\land(q\lor r) \vdash (p\land q)\lor(p\land r)$"}
Tiram-se $p$ e $q\lor r$ da premissa; a disjunção pede $\lor$E com
$\gamma = (p\land q)\lor(p\land r)$.

```{.fitch seq="p /\ (q \/ r) |- (p /\ q) \/ (p /\ r)"}
p /\ (q \/ r)
---
p                    ; &E, 1
q \/ r               ; &E, 1
|> q
|  p /\ q            ; &I, 2, 4
|  (p /\ q) \/ (p /\ r)   ; vI, 5
|> r
|  p /\ r            ; &I, 2, 7
|  (p /\ q) \/ (p /\ r)   ; vI, 8
(p /\ q) \/ (p /\ r) ; vE, 3, 4-6, 7-9
```

A linha 5 usa a linha 2 ($p$): é permitido, porque a barra principal
continua aberta dentro das sub-deduções. O proibido é o contrário.
:::

::: {.exemplo title="--- Exercício 2.4(b) (lab, proplogicproofs.pdf) --- encontrar o passo errado"}
Dedução dada (sem justificações):

```{.fitch .nocheck}
(p /\ q) \/ r
---
|> p /\ q
|  p
|  p \/ r
|> r
|  p \/ r
p /\ r
```

Justificações: 1 premissa; 2 hipótese; 3 $\land$E, 2; 4 $\lor$I, 3;
5 hipótese; 6 $\lor$I, 5. Tudo certo até aqui.

**O passo 7 está errado.** As duas sub-deduções terminam em $p\lor r$,
por isso $\lor$E só dá $p\lor r$. E nenhuma outra regra dá $p\land r$:
$p$ (linha 3) e $r$ (linha 5) estão em sub-deduções fechadas.

**Há dedução correta de $p\land r$?** Não. Contraexemplo: $v(p)=F$,
$v(q)=F$, $v(r)=V$. Então $\models_v r$, logo
$\models_v (p\land q)\lor r$; e $\not\models_v p$, logo
$\not\models_v p\land r$. Assim $(p\land q)\lor r \not\models p\land r$ e,
pela integridade, $(p\land q)\lor r \nvdash p\land r$.

Corrigindo o passo 7, a dedução mostra $p\lor r$:

```{.fitch seq="(p /\ q) \/ r |- p \/ r"}
(p /\ q) \/ r
---
|> p /\ q
|  p                 ; &E, 2
|  p \/ r            ; vI, 3
|> r
|  p \/ r            ; vI, 5
p \/ r               ; vE, 1, 2-4, 5-6
```
:::

::: {.pratica title="--- Disjunção (proplogicproofs.pdf)"}
- **2.4 (a)** A dedução de $p\land q$ a partir de $p\lor q$ é válida? Se
  não, qual o passo errado e existe uma dedução correta? Mesma técnica do
  exemplo 2.4(b) acima.
- **2.11 (h)** $(\delta\lor\phi)\land(\delta\lor\psi) \dashv\vdash
  \delta\lor(\phi\land\psi)$. Pista: no sentido $\vdash$ há um $\lor$E
  **dentro** de outro $\lor$E (no caso $\phi$, abre-se $\delta\lor\psi$).
:::

## Regras da negação e do absurdo ($\mathbf{F}$)

$\mathbf{F}$ representa uma **contradição** (ex.: $\phi\land\neg\phi$).
Semanticamente† é a fórmula sempre falsa ($\not\models_v \mathbf{F}$ para
toda a $v$), a mesma da cláusula vazia do DLL: $\Sigma \models \mathbf{F}$
quer dizer que $\Sigma$ é insatisfazível.

::: {.definicao title="--- Regras de $\\neg$"}
$$\dfrac{\neg\neg\phi}{\phi}\,{\scriptstyle\neg\mathrm{E}}
\qquad\qquad
\dfrac{\begin{array}{c}[\phi]\\ \vdots\\ \mathbf{F}\end{array}}{\neg\phi}\,{\scriptstyle\neg\mathrm{I}}$$

- **$\neg$E** (eliminação da dupla negação): de $\neg\neg\phi$ deduz-se
  $\phi$.
- **$\neg$I** (**por contradição**): se, **supondo** $\phi$, se deduz
  $\mathbf{F}$, deduz-se $\neg\phi$ fora da sub-dedução. Cita-se o
  intervalo: "$\neg$I, $i$--$j$".
:::

::: {.definicao title="--- Regras de $\\mathbf{F}$"}
Se $\mathbf{F}$ não for abreviatura de $\phi\land\neg\phi$, precisa de
regras próprias:
$$\dfrac{\phi \qquad \neg\phi}{\mathbf{F}}\,{\scriptstyle\mathbf{F}\mathrm{I}}
\qquad\qquad
\dfrac{\mathbf{F}}{\phi}\,{\scriptstyle\mathbf{F}\mathrm{E}}$$

- **$\mathbf{F}$I**: de $\phi$ **e** $\neg\phi$ tem-se $\mathbf{F}$ (cita
  as duas linhas, por qualquer ordem).
- **$\mathbf{F}$E**: de $\mathbf{F}$ deduz-se **qualquer** fórmula.

$\Sigma$ é **inconsistente** se $\Sigma \vdash \mathbf{F}$.
:::

É o $\neg$E que torna esta lógica **clássica**† (a intuicionista não
aceita $\neg\neg\phi \vdash \phi$). Por isso, "chegar a $\phi$ por
contradição" em DN são **dois** passos: supor $\neg\phi$, chegar a
$\mathbf{F}$, concluir $\neg\neg\phi$ por $\neg$I e depois $\phi$ por
$\neg$E (ex.: (d) abaixo).

::: {.exemplo title="--- $\\phi \\vdash \\neg\\neg\\phi$"}
Quer-se uma negação, $\neg(\neg\phi)$: supõe-se $\neg\phi$ e procura-se
$\mathbf{F}$.

```{.fitch seq="phi |- ~~phi"}
phi
---
|> ~phi
|  F                 ; FI, 1, 2
~~phi                ; ~I, 2-3
```
:::

::: {.exemplo title="--- Duas negações: (b) e (c)"}
**(b) $\neg p\lor\neg q \vdash \neg(p\land q)$.** O objetivo é uma
negação: supõe-se $p\land q$ e procura-se $\mathbf{F}$, usando a premissa
com $\lor$E e $\gamma = \mathbf{F}$.

```{.fitch seq="~p \/ ~q |- ~(p /\ q)"}
~p \/ ~q
---
|> p /\ q
|  p                 ; &E, 2
|  q                 ; &E, 2
||> ~p
||  F                ; FI, 3, 5
||> ~q
||  F                ; FI, 4, 7
|  F                 ; vE, 1, 5-6, 7-8
~(p /\ q)            ; ~I, 2-9
```

**(c) $\vdash \neg(p\land\neg p)$** (sem premissas). Supõe-se
$p\land\neg p$, que se contradiz a si própria.

```{.fitch seq="|- ~(p /\ ~p)"}
|> p /\ ~p
|  p                 ; &E, 1
|  ~p                ; &E, 1
|  F                 ; FI, 2, 3
~(p /\ ~p)           ; ~I, 1-4
```
:::

::: {.exemplo title="--- (d) $\\neg(\\neg p\\lor q) \\vdash p$"}
$p$ não é negação nem tem conectivo para introduzir: **por contradição**.
Supõe-se $\neg p$; daí sai $\neg p\lor q$, o contrário da premissa.

```{.fitch seq="~(~p \/ q) |- p"}
~(~p \/ q)
---
|> ~p
|  ~p \/ q           ; vI, 2
|  F                 ; FI, 3, 1
~~p                  ; ~I, 2-4
p                    ; ~E, 5
```
:::

::: {.pratica title="--- Negação e F (proplogicproofs.pdf)"}
- **2.4 (c)** A dedução de $q$ a partir de $\neg(p\lor\neg q)$ é válida?
  Se sim, indica a regra de cada passo.
- **2.9 (a)** $\neg\delta,\ \delta\lor\phi \vdash \phi$ é válida? Pista:
  $\lor$E; no caso $\delta$ há uma contradição, e de $\mathbf{F}$ tira-se
  o que se quiser.
- **2.9 (d)** $\delta\lor\psi,\ \neg\psi\lor\phi \vdash \delta\lor\phi$ é
  válida? Pista: dois $\lor$E, um dentro do outro.
- **2.11 (d)** $\neg(\neg\delta_1\land\neg\delta_2) \dashv\vdash
  \delta_1\lor\delta_2$. O sentido $\vdash$ é por contradição (supor
  $\neg(\delta_1\lor\delta_2)$), como no exemplo (d).
:::

## Regras da implicação

::: {.definicao title="--- Eliminação de $\\to$ (\\emph{modus ponens})"}
$$\dfrac{\phi \qquad \phi\to\psi}{\psi}\,{\scriptstyle\to\mathrm{E}}$$
De $\phi$ e $\phi\to\psi$ deduz-se $\psi$ (*modus ponens*). Citam-se as
duas linhas.
:::

::: {.exemplo title="--- $p\\to(q\\to r),\\ p\\to q,\\ p \\vdash r$"}
```{.fitch seq="p -> (q -> r), p -> q, p |- r"}
p -> (q -> r)
p -> q
p
---
q -> r               ; ->E, 1, 3
q                    ; ->E, 2, 3
r                    ; ->E, 4, 5
```
:::

::: {.definicao title="--- Introdução de $\\to$ (regra da dedução)"}
$$\dfrac{\begin{array}{c}[\phi]\\ \vdots\\ \psi\end{array}}{\phi\to\psi}\,{\scriptstyle\to\mathrm{I}}$$
Para deduzir $\phi\to\psi$: **supõe-se** $\phi$ (sub-dedução) e deduz-se
$\psi$; fecha-se a sub-dedução e conclui-se $\phi\to\psi$. Cita-se o
intervalo: "$\to$I, $i$--$j$".
:::

::: {.exemplo title="--- $(p\\lor q)\\to r \\vdash p\\to r$"}
```{.fitch seq="(p \/ q) -> r |- p -> r"}
(p \/ q) -> r
---
|> p
|  p \/ q            ; vI, 2
|  r                 ; ->E, 1, 3
p -> r               ; ->I, 2-4
```
:::

### Deduções sem premissas

Com $\to$I, uma dedução com premissas converte-se numa **sem premissas**:
supõe-se a premissa numa sub-dedução e no fim aplica-se $\to$I. Em Fitch,
uma dedução sem premissas começa logo com uma sub-dedução.

::: {.exemplo title="--- $\\vdash \\phi\\to\\neg\\neg\\phi$"}
É $\phi\vdash\neg\neg\phi$ "embrulhada" numa sub-dedução:

```{.fitch seq="|- phi -> ~~phi"}
|> phi
||> ~phi
||  F                ; FI, 1, 2
|  ~~phi             ; ~I, 2-3
phi -> ~~phi         ; ->I, 1-4
```
:::

::: {.definicao title="--- Lema da dedução †"}
(Apontamentos de Nelma Moreira, Lema 1.4.)
$$\Sigma \cup \{\phi\} \vdash \psi \quad\text{sse}\quad \Sigma \vdash \phi\to\psi.$$

- ($\Rightarrow$) Supõe-se $\phi$ numa sub-dedução, repetem-se lá dentro
  os passos da dedução de $\psi$ e aplica-se $\to$I.
- ($\Leftarrow$) Acrescenta-se $\phi$ às premissas e aplica-se $\to$E.

Logo $\phi_1, \dots, \phi_n \vdash \psi$ sse
$\vdash \phi_1 \to (\phi_2 \to \cdots (\phi_n \to \psi))$.
:::

::: {.exemplo title="--- A tautologia do exemplo informal, agora formal"}
$\vdash (p\lor(q\land r))\to((p\lor q)\land(p\lor r))$: $\to$I por fora,
$\lor$E por dentro e, em cada caso, $\lor$I + $\land$I.

```{.fitch seq="|- (p \/ (q /\ r)) -> ((p \/ q) /\ (p \/ r))"}
|> p \/ (q /\ r)
||> p
||  p \/ q                         ; vI, 2
||  p \/ r                         ; vI, 2
||  (p \/ q) /\ (p \/ r)           ; &I, 3, 4
||> q /\ r
||  q                              ; &E, 6
||  r                              ; &E, 6
||  p \/ q                         ; vI, 7
||  p \/ r                         ; vI, 8
||  (p \/ q) /\ (p \/ r)           ; &I, 9, 10
|  (p \/ q) /\ (p \/ r)            ; vE, 1, 2-5, 6-11
(p \/ (q /\ r)) -> ((p \/ q) /\ (p \/ r))   ; ->I, 1-12
```
:::

::: {.exemplo title="--- O raciocínio do Paulo, deduzido"}
$(p\land q)\to r,\ p,\ \neg r \vdash \neg q$. Objetivo negação: supõe-se
$q$; com $p$ monta-se $p\land q$, que dá $r$, contra $\neg r$.

```{.fitch seq="(p /\ q) -> r, p, ~r |- ~q"}
(p /\ q) -> r
p
~r
---
|> q
|  p /\ q            ; &I, 2, 4
|  r                 ; ->E, 1, 5
|  F                 ; FI, 6, 3
~q                   ; ~I, 4-7
```
:::

::: {.exemplo title="--- Exercício 2.5(a) (lab, proplogicproofs.pdf)"}
$(p\land q)\to r,\ p \vdash q\to r$. A conclusão é uma implicação: supor
$q$, chegar a $r$, $\to$I.

```{.fitch seq="(p /\ q) -> r, p |- q -> r"}
(p /\ q) -> r
p
---
|> q
|  p /\ q            ; &I, 2, 3
|  r                 ; ->E, 1, 4
q -> r               ; ->I, 3-5
```
:::

::: {.exemplo title="--- Exercício 2.5(d) (lab, proplogicproofs.pdf)"}
$p\lor\neg q,\ \neg r\to q,\ r\to\neg s,\ s \vdash p$. A premissa
$p\lor\neg q$ tem $p$ de um lado: $\lor$E com $\gamma = p$.

- **Caso $p$**: repetição.
- **Caso $\neg q$**: mostra-se que é **impossível** ($\mathbf{F}$) e usa-se
  $\mathbf{F}$E. $\neg q$ e $\neg r\to q$ obrigam a $r$ (com $\neg r$
  vinha $q$); $r$ dá $\neg s$, contra $s$.

```{.fitch seq="p \/ ~q, ~r -> q, r -> ~s, s |- p"}
p \/ ~q
~r -> q
r -> ~s
s
---
|> p
|  p                 ; R, 5
|> ~q
||> ~r
||  q                ; ->E, 2, 8
||  F                ; FI, 9, 7
|  ~~r               ; ~I, 8-10
|  r                 ; ~E, 11
|  ~s                ; ->E, 3, 12
|  F                 ; FI, 4, 13
|  p                 ; FE, 14
p                    ; vE, 1, 5-6, 7-15
```
:::

::: {.pratica title="--- Implicação, parte 1 (proplogicproofs.pdf)"}
- **2.4 (d)** e **2.4 (f)** As deduções dadas são válidas? Se não, qual o
  passo errado e existe uma dedução correta? (Ambas têm um passo errado;
  numa delas há dedução correta, e tens de a escrever.)
- **2.5 (b)** $q\to p,\ q\to\neg p \vdash \neg q$.
- **2.5 (e)** $p\to(q\lor r),\ q\to s,\ r\to t \vdash p\to(s\lor t)$.
  Pista: $\to$I por fora, $\lor$E por dentro.
- **2.5 (g)** $(t\to(r\lor p))\to((\neg r\lor k)\land\neg k) \vdash \neg r$.
  Pista: supor $r$; para usar a premissa precisas de $t\to(r\lor p)$, que
  se obtém com $\to$I.
- **Slide 9** Deduz o raciocínio "estudar ou chumbar":
  $r\to t,\ \neg e\to r,\ \neg t \vdash e\lor r\lor(e\land r)$.

As alíneas (c) e (f) da 2.5 são a mesma técnica; não precisas de as
fazer.
:::

::: {.pratica title="--- Implicação, parte 2: deduções sem premissas (proplogicproofs.pdf)"}
- **2.6 (b)** $\vdash (\delta\to\psi)\to((\neg\delta\to\neg\phi)\to(\phi\to\psi))$.
  Três $\to$I encaixados; no fim, para chegar a $\delta$, contradição.
- **2.6 (d)** $\vdash \delta\to(\neg\phi\to\neg(\delta\to\phi))$.
- **2.6 (e)** $\vdash ((\phi\to\delta)\land(\delta\to\phi))\to((\phi\lor\delta)\to(\phi\land\delta))$.
- **2.8 (a)** $\delta\to(\phi\to\psi),\ \neg\psi,\ \delta \vdash \neg\phi$.
- **2.8 (c)** $\vdash (\delta\to(\phi\to\psi))\to(\phi\to(\delta\to\psi))$.
- **2.8 (e)** $\vdash ((\phi\to\delta)\to\delta)\to((\delta\to\phi)\to\phi)$.
  A mais difícil: para usar $(\phi\to\delta)\to\delta$ precisas de
  $\phi\to\delta$; consegue-se dentro de uma contradição sobre $\neg\phi$.
- **2.8 (g)** $\delta,\ \neg\phi \vdash \neg(\delta\to\phi)$.
- **2.9 (e)** e **2.9 (f)** São válidas? Para a que não for, dá um
  contraexemplo e usa a integridade.

Ficam de fora a 2.6 (a), (c) e a 2.8 (b), (d), (f): são as mesmas
técnicas.
:::

## Regras derivadas e estratégias

**Regras derivadas** (Aula 7) são atalhos que correspondem a teoremas de
DN: obtêm-se das regras base e podem "colar-se" noutra dedução. A folha 2
diz "In case you use derived rules, you should prove them separately":
pode usar-se MT, RA, TE ou $\neg\neg$I, mas escrevendo também a dedução
de cada uma (as de baixo). As soluções usam só as regras base.

::: {.definicao title="--- Regras derivadas e as suas deduções"}
**Modus tollens** (MT):
$$\dfrac{\phi\to\psi \qquad \neg\psi}{\neg\phi}\,{\scriptstyle\mathrm{MT}}$$

```{.fitch seq="phi -> psi, ~psi |- ~phi"}
phi -> psi
~psi
---
|> phi
|  psi               ; ->E, 1, 3
|  F                 ; FI, 4, 2
~phi                 ; ~I, 3-5
```

**Introdução da dupla negação** ($\neg\neg$I) e **redução ao absurdo** (RA):
$$\dfrac{\phi}{\neg\neg\phi}\,{\scriptstyle\neg\neg\mathrm{I}}
\qquad\qquad
\dfrac{\begin{array}{c}[\neg\phi]\\ \vdots\\ \mathbf{F}\end{array}}{\phi}\,{\scriptstyle\mathrm{RA}}$$
$\neg\neg$I é $\phi \vdash \neg\neg\phi$ (secção da negação). RA abrevia
"$\neg$I (dá $\neg\neg\phi$) e depois $\neg$E", como no exemplo (d). Nos
slides, RA justifica-se assim: uma dedução de $\mathbf{F}$ a partir de
$\neg\phi$ dá, por $\to$I, $\neg\phi\to\mathbf{F}$; basta então
$\neg\phi\to\mathbf{F} \vdash \phi$:

```{.fitch seq="~phi -> F |- phi"}
~phi -> F
---
|> ~phi
|  F                 ; ->E, 1, 2
~~phi                ; ~I, 2-3
phi                  ; ~E, 4
```
:::

::: {.definicao title="--- Terceiro excluído (TE): $\\vdash \\phi\\lor\\neg\\phi$"}
Supõe-se $\neg(\phi\lor\neg\phi)$ e chega-se a $\mathbf{F}$: $\phi$ é
impossível (daria $\phi\lor\neg\phi$), logo $\neg\phi$; mas $\neg\phi$
também dá $\phi\lor\neg\phi$.

```{.fitch seq="|- phi \/ ~phi"}
|> ~(phi \/ ~phi)
||> phi
||  phi \/ ~phi      ; vI, 2
||  F                ; FI, 3, 1
|  ~phi              ; ~I, 2-4
|  phi \/ ~phi       ; vI, 5
|  F                 ; FI, 6, 1
~~(phi \/ ~phi)      ; ~I, 1-7
phi \/ ~phi          ; ~E, 8
```
:::

::: {.definicao title="--- Contraposição: $\\phi\\to\\psi \\dashv\\vdash \\neg\\psi\\to\\neg\\phi$"}
Sentido $\vdash$ (o outro é igual, com um $\neg$E no fim): MT dentro de
um $\to$I.

```{.fitch seq="phi -> psi |- ~psi -> ~phi"}
phi -> psi
---
|> ~psi
||> phi
||  psi              ; ->E, 1, 3
||  F                ; FI, 4, 2
|  ~phi              ; ~I, 3-5
~psi -> ~phi         ; ->I, 2-6
```
:::

::: {.exemplo title="--- Usar regras derivadas (Aula 7): $\\neg q\\to\\neg p \\vdash p\\to\\neg\\neg q$"}
Conclusão implicação: supor $p$ e chegar a $\neg\neg q$. O MT aplicado a
$\neg q\to\neg p$ precisa de $\neg\neg p$ (a negação do consequente
$\neg p$), que vem de $p$ por $\neg\neg$I. Em exame, MT e $\neg\neg$I
teriam de vir provados à parte (caixa acima).

```{.fitch seq="~q -> ~p |- p -> ~~q"}
~q -> ~p
---
|> p
|  ~~p               ; ~~I, 2
|  ~~q               ; MT, 1, 3
p -> ~~q             ; ->I, 2-4
```
:::

::: {.definicao title="--- Estratégias para encontrar uma dedução (folha 2, página 1)"}
Olha para a **conclusão** que falta e para as **premissas/hipóteses**:

1. Conclusão **implicação** $\psi\to\theta$: supõe $\psi$, deduz $\theta$,
   aplica $\to$I.
2. Conclusão **negação** $\neg\psi$: supõe $\psi$, deduz $\mathbf{F}$,
   aplica $\neg$I.
3. **Por contradição** (quando nada mais serve, ex.: conclusão é uma
   letra ou uma disjunção): supõe $\neg\phi$ e deduz $\mathbf{F}$ (depois
   $\neg$I e $\neg$E). Com uma negação $\neg\psi$ nas premissas, tenta
   deduzir $\psi$ para ter $\mathbf{F}$.
4. Premissa **disjunção** $\phi\lor\psi$ e queres $\gamma$: supõe $\phi$ e
   deduz $\gamma$, supõe $\psi$ e deduz $\gamma$, aplica $\lor$E.
5. Hipótese $\neg\phi$ e queres $\mathbf{F}$: obtém $\phi$ e aplica
   $\mathbf{F}$I.
6. Tens $\phi\to\theta$: deduz $\phi$ e aplica $\to$E para ter $\theta$.

**Cada passo** é uma premissa, uma hipótese ou uma regra (ou repetição)
aplicada a fórmulas acessíveis. **Não se usam equivalências semânticas**
(De Morgan, etc.) como passos: deduzem-se (é o que pedem as 2.11 e 2.12).
:::

::: {.exemplo title="--- Exercício 2.11(e) (lab, proplogicproofs.pdf)"}
$\delta_1\to\delta_2 \dashv\vdash \neg(\delta_1\land\neg\delta_2)$: duas
deduções.

**($\vdash$)** Conclusão negação (estratégia 2): supor
$\delta_1\land\neg\delta_2$, chegar a $\mathbf{F}$.

```{.fitch seq="delta1 -> delta2 |- ~(delta1 /\ ~delta2)"}
delta1 -> delta2
---
|> delta1 /\ ~delta2
|  delta1            ; &E, 2
|  ~delta2           ; &E, 2
|  delta2            ; ->E, 1, 3
|  F                 ; FI, 5, 4
~(delta1 /\ ~delta2) ; ~I, 2-6
```

**($\dashv$)** Conclusão implicação (estratégia 1): supor $\delta_1$,
chegar a $\delta_2$, uma letra: por contradição (estratégia 3), supor
$\neg\delta_2$; com $\delta_1$ monta-se $\delta_1\land\neg\delta_2$,
contra a premissa (estratégia 5).

```{.fitch seq="~(delta1 /\ ~delta2) |- delta1 -> delta2"}
~(delta1 /\ ~delta2)
---
|> delta1
||> ~delta2
||  delta1 /\ ~delta2  ; &I, 2, 3
||  F                ; FI, 4, 1
|  ~~delta2          ; ~I, 3-5
|  delta2            ; ~E, 6
delta1 -> delta2     ; ->I, 2-7
```
:::

::: {.exemplo title="--- Aula 7, slide 9 (a): $\\phi\\to\\psi \\vdash \\neg\\phi\\lor\\psi$"}
Conclusão disjunção, sem nenhuma premissa disjunção: por contradição
(estratégia 3), supor $\neg(\neg\phi\lor\psi)$. Para usar a premissa
($\to$E) falta $\phi$, outra letra: de novo por contradição, supor
$\neg\phi$, que dá $\neg\phi\lor\psi$ por $\lor$I, contra a hipótese
(estratégia 5). Com $\phi$ sai $\psi$ e, outra vez, $\neg\phi\lor\psi$.

```{.fitch seq="phi -> psi |- ~phi \/ psi"}
phi -> psi
---
|> ~(~phi \/ psi)
||> ~phi
||  ~phi \/ psi      ; vI, 3
||  F                ; FI, 4, 2
|  ~~phi             ; ~I, 3-5
|  phi               ; ~E, 6
|  psi               ; ->E, 1, 7
|  ~phi \/ psi       ; vI, 8
|  F                 ; FI, 9, 2
~~(~phi \/ psi)      ; ~I, 2-10
~phi \/ psi          ; ~E, 11
```
:::

::: {.definicao title="--- Formas de raciocínio com nome †"}
(A 2.1 pede para "identificar a regra de inferência".)

| Nome | Forma | Em DN |
|:-------------|:-----------------------|:----------------|
| *Modus ponens* | $\phi\to\psi,\ \phi$ logo $\psi$ | $\to$E |
| *Modus tollens* | $\phi\to\psi,\ \neg\psi$ logo $\neg\phi$ | MT |
| Silogismo hipotético | $\phi\to\psi,\ \psi\to\theta$ logo $\phi\to\theta$ | $\to$I com dois $\to$E |
| Silogismo disjuntivo | $\phi\lor\psi,\ \neg\phi$ logo $\psi$ | $\lor$E (2.9 a) |
| Prova por casos | $\phi\to\theta,\ \neg\phi\to\theta$ logo $\theta$ | TE + $\lor$E |
| Contraposição | $\phi\to\psi$ logo $\neg\psi\to\neg\phi$ | acima |

**Falácias** (parecem válidas mas **não são**): *afirmação do
consequente* ($\phi\to\psi,\ \psi$ logo $\phi$; contraexemplo
$v(\phi)=F$, $v(\psi)=V$) e *negação do antecedente*
($\phi\to\psi,\ \neg\phi$ logo $\neg\psi$; mesmo contraexemplo).
:::

::: {.pratica title="--- Regras derivadas, raciocínios e equivalências (proplogicproofs.pdf)"}
- **2.1 (a)** e **(b)** Escreve a forma lógica; se for válido, diz a
  regra (tabela acima); se não, dá o contraexemplo.
- **2.2** Completa cada argumento com uma conclusão que o torne válido.
- **2.3** Associa cada tautologia (1)--(6) a um dos argumentos (a)--(f).
- **2.7** Formaliza as três hipóteses e deduz "choveu". Pista:
  estratégia 3 (supor que não choveu).
- **2.11 (g)** $(\phi\lor\psi)\to\delta \dashv\vdash (\phi\to\delta)\land(\psi\to\delta)$.
- **Aula 7, slide 9 (b)** $\neg(\phi\land\psi) \vdash \neg\phi\lor\neg\psi$
  (De Morgan, deduzido). Pista: como a (a), mas é preciso obter $\phi$
  **e** $\psi$ para contradizer a premissa.

A 2.12 (sem seta na folha) tem mais equivalências do mesmo tipo (De
Morgan, distributividade...): só se te sobrar tempo.
:::

## Propriedades de $\vdash$

As 2.10 e 2.15 pedem para provar ou refutar afirmações gerais sobre
$\vdash$†:

- **Verdadeira:** constrói-se a dedução pedida **a partir das deduções
  dadas**, copiando as suas linhas (com os números ajustados) e
  acrescentando os passos que faltam. Uma dedução de $\phi$ a partir de
  $\Sigma$ é também dedução de $\phi$ a partir de qualquer
  $\Sigma' \supseteq \Sigma$: as regras não olham para as premissas que
  não usam.
- **Falsa:** instancia-se com fórmulas concretas e, para o "$\nvdash$",
  usa-se um contraexemplo + **integridade**.

::: {.exemplo title="--- Exercício 2.10(a) e (b) (lab, proplogicproofs.pdf)"}
**(a) Se $\vdash\psi$, então $\delta_1, \dots, \delta_n \vdash \psi$ ---
VERDADEIRO.**

Seja $\phi_1, \dots, \phi_m$ ($\phi_m = \psi$) uma dedução de $\psi$ sem
premissas. Escrevem-se $\delta_1, \dots, \delta_n$ como premissas (linhas
$1, \dots, n$) e a seguir $\phi_1, \dots, \phi_m$, somando $n$ aos números
de linha das justificações. Cada $\phi_i$ continua justificado pela mesma
regra, aplicada às mesmas fórmulas, que continuam acessíveis (as
premissas novas estão na barra principal e não fecham nenhuma
sub-dedução). A última linha é $\psi$: $\delta_1, \dots, \delta_n \vdash \psi$.
$\blacksquare$

**(b) Se $\delta_1, \dots, \delta_n \vdash \psi$, então $\vdash\psi$ ---
FALSO.** Contraexemplo: $n=1$, $\delta_1 = p$, $\psi = p$. Tem-se
$p \vdash p$:

```{.fitch seq="p |- p"}
p
---
p                    ; R, 1
```

Mas $\nvdash p$: com $v(p) = F$, $\not\models_v p$, logo $\not\models p$;
se houvesse uma dedução $\vdash p$, pela integridade ter-se-ia
$\models p$. $\blacksquare$
:::

::: {.pratica title="--- Propriedades de $\\vdash$ (proplogicproofs.pdf)"}
- **2.10 (e)** Se $\delta_1,\delta_2 \vdash \phi\to\psi$ e
  $\delta_1 \vdash \phi$, então $\delta_1,\delta_2 \vdash \psi$.
- **2.10 (f)** Se $\delta_1,\delta_2 \vdash \phi\to\psi$ e
  $\delta_1 \vdash \phi$, então $\delta_1 \vdash \psi$. (Compara com a (e):
  só muda o lado direito.)
- **2.10 (g)** Se $\delta_1 \vdash \phi\to\psi$ e $\delta_2 \vdash \phi$,
  então $\delta_1,\delta_2 \vdash \psi$.
- **2.15 (a)** e **(b)** Se para **qualquer** $\delta$ se tem
  $\Sigma\vdash\delta$ ou $\Gamma\vdash\delta$, então $\Sigma$ ou $\Gamma$
  é insatisfazível, e $\Sigma\cup\Gamma$ é insatisfazível. Pista: escolhe
  $\delta = \mathbf{F}$.

As restantes alíneas da 2.10 são a mesma técnica. As 2.13, 2.14 e 2.16
(sem seta) também.
:::


# Aula 8 --- Outros sistemas dedutivos

DN não tem axiomas e tem regras de introdução e eliminação para cada
conectivo. Esta aula apresenta três alternativas: um sistema **à Hilbert**
(só axiomas e *modus ponens*) e dois sistemas **automatizáveis** que
provam por refutação (*tableaux* e resolução).

## O sistema de Hilbert $\mathcal{H}$

::: {.definicao title="--- Sistema $\\mathcal{H}$"}
Usa só o conjunto completo de conectivos $\{\neg,\to\}$ (os outros são
abreviaturas). Tem três **axiomas** e uma **regra**:

- **(A1)** $\phi\to(\psi\to\phi)$
- **(A2)** $(\phi\to(\psi\to\theta))\to((\phi\to\psi)\to(\phi\to\theta))$
- **(A3)** $(\neg\psi\to\neg\phi)\to((\neg\psi\to\phi)\to\psi)$
- ***Modus ponens*** (MP): de $\phi$ e $\phi\to\psi$ infere-se $\psi$.

Os axiomas são **esquemas**†: qualquer fórmula obtida substituindo
$\phi,\psi,\theta$ por fórmulas é um axioma. Uma dedução em $\mathcal{H}$
é uma lista numerada em que cada linha é uma premissa, uma instância de
um axioma (dizendo a substituição) ou resulta de duas linhas anteriores
por MP ($\Sigma\vdash_{\mathcal{H}}\phi$).
:::

::: {.definicao title="--- Resultados sobre $\\mathcal{H}$"}
- **Teorema da dedução:** se $\Sigma\cup\{\psi\}\vdash_{\mathcal{H}}\theta$
  então $\Sigma\vdash_{\mathcal{H}}\psi\to\theta$. (Em DN isto é a própria
  regra $\to$I; em $\mathcal{H}$, sem hipóteses temporárias, é um teorema
  sobre o sistema.)
- **$\Sigma\vdash_{DN}\phi$ sse $\Sigma\vdash_{\mathcal{H}}\phi$.**
  ($\Leftarrow$) os três axiomas são teoremas de DN (provados abaixo e na
  prática) e MP é a regra $\to$E. ($\Rightarrow$) toda a dedução em DN se
  pode traduzir para $\mathcal{H}$ (não se faz na cadeira).
- **Corolário:** $\mathcal{H}$ é íntegro e completo, porque DN o é.
:::

::: {.exemplo title="--- Uma prova em $\\mathcal{H}$: $\\vdash_{\\mathcal{H}} \\phi\\to\\phi$ †"}
Sem $\to$I, nem uma fórmula tão simples se prova supondo $\phi$: é preciso
escolher bem as instâncias dos axiomas e encadear MPs.

| | Fórmula | Justificação |
|:-:|:-----------------------------|:-----------------------|
| 1 | $\phi\to((\phi\to\phi)\to\phi)$ | A1, $\psi:=\phi\to\phi$ |
| 2 | $(\phi\to((\phi\to\phi)\to\phi))\to((\phi\to(\phi\to\phi))\to(\phi\to\phi))$ | A2, $\psi:=\phi\to\phi$, $\theta:=\phi$ |
| 3 | $(\phi\to(\phi\to\phi))\to(\phi\to\phi)$ | MP, 1, 2 |
| 4 | $\phi\to(\phi\to\phi)$ | A1, $\psi:=\phi$ |
| 5 | $\phi\to\phi$ | MP, 4, 3 |

Em DN é uma linha: supor $\phi$ e aplicar $\to$I. É por isso que se
deduz em DN e se usa $\mathcal{H}$ para raciocinar *sobre* o sistema.
:::

::: {.exemplo title="--- A2 é teorema de DN (Aula 7, slide 9 (d))"}
Três implicações encaixadas: supor os três antecedentes e chegar a
$\theta$ com três $\to$E.

```{.fitch seq="|- (phi -> (psi -> theta)) -> ((phi -> psi) -> (phi -> theta))"}
|> phi -> (psi -> theta)
||> phi -> psi
|||> phi
|||  psi             ; ->E, 2, 3
|||  psi -> theta    ; ->E, 1, 3
|||  theta           ; ->E, 5, 4
||  phi -> theta     ; ->I, 3-6
|  (phi -> psi) -> (phi -> theta)  ; ->I, 2-7
(phi -> (psi -> theta)) -> ((phi -> psi) -> (phi -> theta))  ; ->I, 1-8
```
:::

::: {.pratica title="--- Axiomas de $\\mathcal{H}$ em DN (Aula 7, slide 9)"}
- **Aula 7, slide 9 (c)** $\vdash \phi\to(\psi\to\phi)$ (A1). Pista: a
  regra R.
- **Aula 7, slide 9 (e)** $\vdash (\neg\psi\to\neg\phi)\to((\neg\psi\to\phi)\to\psi)$
  (A3). Pista: depois de supor os dois antecedentes, $\psi$ é uma letra:
  por contradição.
:::

## *Tableaux* semânticos

Em DN não é fácil ter um algoritmo que decida se $\phi$ é teorema (a não
ser construir a dedução a partir da tabela de verdade, via completude).
Os sistemas **automatizáveis** têm a propriedade de que, lendo a dedução
da conclusão para as premissas, cada fórmula é **subfórmula** (ou
negação de subfórmula†) de uma fórmula do passo anterior: o espaço de
procura é finito. O *modus ponens* não tem esta propriedade (de $\psi$
não se adivinha o $\phi$ de $\phi$ e $\phi\to\psi$). São exemplos o
**cálculo de sequentes** de Gentzen (variante de DN), os **tableaux**
(mostram que $\neg\phi$ é contradição) e a **resolução** (também por
contradição, com $\neg\phi$ em FNC).

::: {.definicao title="--- Notação uniforme de Smullyan"}
As fórmulas que não são literais dividem-se em **conjuntivas** ($\alpha$,
verdadeiras sse **ambos** os componentes o são) e **disjuntivas**
($\beta$, verdadeiras sse **algum** componente o é):

| $\alpha$ | $\alpha_1$ | $\alpha_2$ | | $\beta$ | $\beta_1$ | $\beta_2$ |
|:-:|:-:|:-:|---|:-:|:-:|:-:|
| $\phi\land\psi$ | $\phi$ | $\psi$ | | $\neg(\phi\land\psi)$ | $\neg\phi$ | $\neg\psi$ |
| $\neg(\phi\lor\psi)$ | $\neg\phi$ | $\neg\psi$ | | $\phi\lor\psi$ | $\phi$ | $\psi$ |
| $\neg(\phi\to\psi)$ | $\phi$ | $\neg\psi$ | | $\phi\to\psi$ | $\neg\phi$ | $\psi$ |

Para toda a valoração $v$: $v(\alpha)=v(\alpha_1)\land v(\alpha_2)$ e
$v(\beta)=v(\beta_1)\lor v(\beta_2)$. As linhas $\neg$ são De Morgan e
$\neg(\phi\to\psi)\Leftrightarrow\phi\land\neg\psi$.
:::

::: {.definicao title="--- Tableau, regras de expansão e ramos fechados"}
Um **tableau** para $\{\phi_1,\dots,\phi_n\}$ é uma árvore de fórmulas:

1. a árvore de um só ramo $\phi_1,\phi_2,\dots,\phi_n$ é um tableau;
2. se $T$ é um tableau para o conjunto e $T^\star$ resulta de $T$ por uma
   regra de expansão, $T^\star$ também é.

**Regras de expansão** de uma fórmula $\psi$ de um ramo $r$ (os nós novos
acrescentam-se no fim de $r$):

$$\dfrac{\neg\neg\phi}{\phi}\qquad
\dfrac{\neg\mathbf{F}}{\mathbf{V}}\qquad
\dfrac{\neg\mathbf{V}}{\mathbf{F}}\qquad
\dfrac{\alpha}{\begin{array}{c}\alpha_1\\ \alpha_2\end{array}}\qquad
\dfrac{\beta}{\beta_1 \mid \beta_2}$$

- $\alpha$: **dois nós seguidos** no mesmo ramo ($\alpha_2$ filho de
  $\alpha_1$): os dois têm de ser verdadeiros.
- $\beta$: o ramo **divide-se em dois** filhos, $\beta_1$ e $\beta_2$:
  basta um ser verdadeiro.

Um ramo é **fechado** se contém $\psi$ e $\neg\psi$ para alguma fórmula
$\psi$ (marca-se $\times$); o tableau é **fechado** se todos os ramos o
são. Um ramo é **satisfazível** se o conjunto das suas fórmulas o é; o
tableau é satisfazível se algum ramo o é.

**Dedução por tableau** de $\phi$: um tableau fechado para $\{\neg\phi\}$.
$\phi$ é **teorema** se tem uma dedução por tableau.
:::

::: {.definicao title="--- Integridade e completude dos tableaux"}
- Aplicar uma regra a um tableau satisfazível dá um tableau satisfazível
  (a valoração que satisfaz um ramo satisfaz $\alpha_1$ e $\alpha_2$, ou
  um dos $\beta_i$, pelas igualdades de Smullyan).
- Se há um tableau fechado para $\Gamma$, $\Gamma$ é **insatisfazível**
  (um ramo fechado nunca é satisfazível; se $\Gamma$ o fosse, algum ramo
  seria).
- **Integridade:** se $\phi$ tem dedução por tableau, $\models\phi$
  ($\{\neg\phi\}$ é insatisfazível).
- **Completude:** se $\models\phi$, $\phi$ tem dedução por tableau.
:::

**Como construir†.** Escreve $\neg\phi$ na raiz e expande uma fórmula de
cada vez, citando o nó expandido (os números à esquerda e entre $[\,]$
nas figuras). Expande primeiro as $\alpha$ e os $\neg\neg$ (não
ramificam) e deixa as $\beta$ para o fim. Uma $\beta$ expande-se em
**todos** os ramos abertos abaixo dela. Fecha um ramo logo que tenha
$\psi$ e $\neg\psi$, para qualquer $\psi$ (não só letras). Um ramo aberto
em que já tudo foi expandido dá uma valoração que satisfaz a raiz: se a
raiz é $\neg\phi$, é um contraexemplo a $\models\phi$.

::: {.exemplo title="--- Tableau para $\\{p\\land(\\neg q\\lor\\neg p)\\}$ (slide 11)"}
$\alpha$ dá $p$ e $\neg q\lor\neg p$; a $\beta$ divide o ramo. O ramo da
direita fecha ($p$ no nó 2 e $\neg p$ no 5); o da esquerda fica aberto:
o tableau **não é fechado**. O ramo aberto $\{p,\neg q\}$ dá $v(p)=V$,
$v(q)=F$, que satisfaz a fórmula.

```{.tableau .aberto}
p /\ (~q \/ ~p)
p                    ; 1
~q \/ ~p             ; 1
[
~q                   ; 3
|
~p                   ; 3
x                    ; 2, 5
]
```
:::

::: {.exemplo title="--- Exercício 2.17(a) / slide 14 (a): $\\neg((p\\lor q)\\land(\\neg p\\land\\neg q))$"}
Raiz: a negação, $\neg\neg((p\lor q)\land(\neg p\land\neg q))$. O
$\neg\neg$ (nó 2) e as duas $\alpha$ (nós 3--6) vêm antes da única $\beta$,
$p\lor q$ (nó 3). Os dois ramos fecham: $\neg p$/$p$ e $\neg q$/$q$.

```{.tableau seq="~((p \\/ q) /\\ (~p /\\ ~q))"}
~~((p \/ q) /\ (~p /\ ~q))
(p \/ q) /\ (~p /\ ~q)   ; 1
p \/ q               ; 2
~p /\ ~q             ; 2
~p                   ; 4
~q                   ; 4
[
p                    ; 3
x                    ; 5, 7
|
q                    ; 3
x                    ; 6, 9
]
```

Tableau fechado para $\{\neg\phi\}$, logo $\phi$ é teorema (e tautologia).
:::

::: {.exemplo title="--- Exercício 2.20 / slide 14 (b), por tableau: $((p\\to q)\\land(q\\to r))\\to\\neg(\\neg r\\land p)$"}
A raiz $\neg(\dots\to\dots)$ é $\alpha$ (nós 2, 3); $\neg\neg$ e duas
$\alpha$ dão os literais $\neg r$, $p$ e as implicações $p\to q$,
$q\to r$ (nós 4--8). Só ficam $\beta$: $p\to q$ (nó 7) divide em
$\neg p$, que fecha com o nó 6, e $q$; neste, $q\to r$ (nó 8) divide em
$\neg q$, que fecha com $q$, e $r$, que fecha com $\neg r$.

```{.tableau seq="((p -> q) /\\ (q -> r)) -> ~(~r /\\ p)"}
~(((p -> q) /\ (q -> r)) -> ~(~r /\ p))
(p -> q) /\ (q -> r) ; 1
~~(~r /\ p)          ; 1
~r /\ p              ; 3
~r                   ; 4
p                    ; 4
p -> q               ; 2
q -> r               ; 2
[
~p                   ; 7
x                    ; 6, 9
|
q                    ; 7
[
~q                   ; 8
x                    ; 11, 12
|
r                    ; 8
x                    ; 5, 14
]
]
```
:::

::: {.pratica title="--- Tableaux (proplogicproofs.pdf)"}
- **2.17 (b)** $((p\to q)\land(q\to r))\to(p\to r)$. Pista: igual ao
  exemplo do 2.20.
- **2.17 (c)** $(\neg p\to q)\to((p\to q)\to q)$.
- **2.17 (d)** $((p\to q)\to p)\to p$ (lei de Peirce). Repara que se
  prova sem $\land$ nem $\lor$.

A 2.22 (tableaux das 2.8 (b)--(e)) é a mesma técnica.
:::

## Resolução

::: {.definicao title="--- Sistema de resolução"}
Também é por **refutação**: para deduzir $\phi$, mostra-se que $\neg\phi$
é contradição. Trabalha com um conjunto $\Sigma$ de **cláusulas**
(conjuntos de literais, lidos como disjunções); a **cláusula vazia**
representa-se por $\mathbf{F}$. Não tem axiomas e tem **uma só regra**:
$$\dfrac{C\cup\{p\} \qquad C'\cup\{\neg p\}}{C\cup C'}$$
$C\cup C'$ é a **resolvente** das premissas. Uma dedução de $\mathbf{F}$ a
partir de um conjunto de cláusulas $\mathcal{C}$ é uma **refutação** de
$\mathcal{C}$. Uma **dedução por resolução** de $\phi$ é uma refutação das
cláusulas da **FNC de $\neg\phi$**.
:::

A regra é válida porque, se $v$ satisfaz as duas premissas, ou
$v(p)=F$ e então algum literal de $C$ é verdadeiro, ou $v(p)=V$ e algum
de $C'$ o é. Cuidados†:

- resolve-se **um só par** $p$/$\neg p$ de cada vez: de $\{p,q\}$ e
  $\{\neg p,\neg q\}$ sai $\{q,\neg q\}$ (ou $\{p,\neg p\}$), **nunca**
  $\mathbf{F}$ (com $v(p)=V$, $v(q)=F$ as duas são verdadeiras);
- a resolvente é um **conjunto**: literais repetidos contam uma vez
  ($\{q,r\}$ e $\{\neg q,r\}$ dão $\{r\}$);
- para ter a FNC de $\neg\phi$, aplica as regras da secção FNC (Aula 3);
  as linhas $\alpha$ de Smullyan dão logo
  $\neg(\phi\to\psi)\Leftrightarrow\phi\land\neg\psi$.

É o mesmo formato de entrada do DLL (Aula 4): o DLL procura uma valoração,
a resolução procura uma refutação.

::: {.definicao title="--- Integridade e completude da resolução"}
Seja $\mathcal{C}=\{C_1,\dots,C_n\}$ um conjunto não vazio de cláusulas.

- **Integridade:** (i) se $R$ é resolvente de $C_i, C_j\in\mathcal{C}$,
  então $\mathcal{C}\models R$; (ii) se $\mathcal{C}\vdash_R\mathbf{F}$,
  $\mathcal{C}$ é insatisfazível.
- **Completude:** se $\mathcal{C}$ é insatisfazível, então
  $\mathcal{C}\vdash_R\mathbf{F}$.
:::

::: {.exemplo title="--- Refutação de um conjunto de cláusulas (slide 16)"}
$\{\{\neg p\},\{q,r\},\{\neg r,\neg s\},\{p,s\},\{\neg q,\neg s\}\}$
(cláusulas 1--5). Cada resolvente cita as duas cláusulas e o literal
eliminado:

- 6: $\{q,\neg s\}$ de 2 e 3 (elimina $r$);
- 7: $\{s\}$ de 4 e 1 (elimina $p$);
- 8: $\{\neg s\}$ de 6 e 5 (elimina $q$);
- 9: $\mathbf{F}$ de 7 e 8 (elimina $s$).

```{.resolucao}
{~p}
{q, r}
{~r, ~s}
{p, s}
{~q, ~s}
{q, ~s}              ; 2, 3
{s}                  ; 4, 1
{~s}                 ; 6, 5
F                    ; 7, 8
```
:::

::: {.exemplo title="--- Exercício 2.20 / slide 14 (b), por resolução"}
$\phi = ((p\to q)\land(q\to r))\to\neg(\neg r\land p)$. **FNC de
$\neg\phi$:**
$$\begin{aligned}
\neg\phi &\Leftrightarrow ((p\to q)\land(q\to r))\land\neg\neg(\neg r\land p)
  && \neg(\phi'\to\psi')\Leftrightarrow\phi'\land\neg\psi'\\
&\Leftrightarrow ((p\to q)\land(q\to r))\land(\neg r\land p)
  && \text{dupla negação}\\
&\Leftrightarrow (\neg p\lor q)\land(\neg q\lor r)\land\neg r\land p
  && \phi'\to\psi'\Leftrightarrow\neg\phi'\lor\psi' \text{ (duas vezes), associatividade}
\end{aligned}$$
**Cláusulas:** 1 $\{\neg p,q\}$, 2 $\{\neg q,r\}$, 3 $\{\neg r\}$,
4 $\{p\}$. **Refutação:** 5 $\{q\}$ de 1 e 4; 6 $\{r\}$ de 2 e 5;
7 $\mathbf{F}$ de 3 e 6.

```{.resolucao de="((p -> q) /\\ (q -> r)) -> ~(~r /\\ p)"}
{~p, q}
{~q, r}
{~r}
{p}
{q}                  ; 1, 4
{r}                  ; 2, 5
F                    ; 3, 6
```
:::

::: {.pratica title="--- Resolução (proplogicproofs.pdf)"}
- **2.18 (a)** Converte $(p\lor\neg q\lor r)\land\neg p\land(q\lor r\lor p)\land(p\lor\neg r)$
  num conjunto de cláusulas.
- **2.18 (b)** Deduz $\mathbf{F}$ desse conjunto só com a regra da
  resolução.
- **2.19** Refuta $\{\{\neg p,\neg q,r\},\{p,r\},\{q,r\},\{\neg r\}\}$.
  Pista: começa pela cláusula unitária.
- **2.21 (a)** $(p\to q)\to((\neg p\to q)\to q)$, por tableau **e** por
  resolução (usa também a secção anterior).
- **2.21 (b)** $q\to(p\to(q\land p))$, pelos dois métodos.
- **2.21 (c)** $q\to(\neg p\to\neg(q\to p))$, pelos dois métodos.

A 2.22 por resolução é a mesma técnica.
:::

# Aulas 9--10 --- Integridade, completude e decidibilidade

Estas aulas provam que DN é **íntegra** e **completa** (definições em
"Semântica versus dedução", Aulas 5--7). Na lógica proposicional as tabelas de verdade já decidem $\models$; um
sistema dedutivo vale a pena porque:

- uma dedução pode ser mais rápida e ocupar menos espaço do que uma tabela
  de $2^n$ linhas;
- uma dedução é um objeto, fácil de manipular e verificar por computador;
- ilustra a noção de dedução, essencial em lógicas com semântica mais
  complexa, onde não há tabelas de verdade (como a de primeira ordem).

## Integridade de DN

::: {.definicao title="--- Integridade de DN"}
Se $\Sigma \vdash \phi$ então $\Sigma \models \phi$. **Corolário:** se
$\vdash \phi$ então $\models \phi$ (todo o teorema é tautologia).
:::

**Prova (por absurdo).** Seja $\phi_1, \dots, \phi_n = \phi$ uma dedução.
Mostra-se que **cada passo** é consequência semântica das premissas e
hipóteses abertas nesse passo. Suponha-se que não, e seja $p$ o
**primeiro** passo cuja fórmula não é consequência das premissas
$\phi_1, \dots, \phi_k$ abertas em $p$. Vê-se, regra a regra, que isso é
impossível:

- **$\to$E** (de $\phi\to\theta$ e $\phi$ obtém-se $\theta$). As premissas
  de $\phi\to\theta$ e de $\phi$ estão entre $\phi_1, \dots, \phi_k$ e,
  como esses passos vêm antes de $p$, ambas são consequência delas. Por
  hipótese há $v$ com $v(\phi_i) = V$ para todo o $i$ e $v(\theta) = F$;
  então também $v(\phi) = v(\phi\to\theta) = V$, o que contradiz a tabela
  da implicação.
- **$\to$I** (da sub-dedução $[\phi]\dots\theta$ obtém-se
  $\phi\to\theta$). As premissas de $\theta$ são algumas de
  $\phi_1, \dots, \phi_k$ e $\phi$, e $\theta$ é consequência delas. Por
  hipótese há $v$ com $v(\phi_i) = V$ e $v(\phi\to\theta) = F$, logo
  $v(\phi) = V$ e $v(\theta) = F$: contradiz $\phi_1, \dots, \phi_k,
  \phi \models \theta$.
- **$\mathbf{F}$E** (de $\mathbf{F}$ obtém-se $\phi$). As premissas de
  $\phi$ são as de $\mathbf{F}$, e $\mathbf{F}$ é consequência delas; isso
  só acontece se $\phi_1, \dots, \phi_k$ forem **insatisfazíveis**. Então
  $\phi$ é consequência delas (vacuamente: não há $v$ que as satisfaça).
- As restantes regras† resolvem-se da mesma maneira, com a tabela do
  conectivo:

| Regra | Porque é que a conclusão é consequência das premissas abertas† |
|:--|:----------------|
| $\land$I, $\land$E | $v(\phi\land\psi)=V$ sse $v(\phi)=V$ e $v(\psi)=V$ |
| $\lor$I | se $v(\phi)=V$, então $v(\phi\lor\psi)=V$ |
| $\lor$E | uma $v$ que satisfaz $\phi\lor\psi$ satisfaz $\phi$ ou $\psi$, e em cada caso a sub-dedução dá $v(\gamma)=V$ |
| $\neg$I | se as premissas mais $\phi$ dão $\mathbf{F}$, nenhuma $v$ que as satisfaz satisfaz $\phi$, logo $v(\neg\phi)=V$ |
| $\neg$E | $v(\neg\neg\phi)=V$ sse $v(\phi)=V$ |
| $\mathbf{F}$I | nenhuma $v$ satisfaz $\phi$ e $\neg\phi$: as premissas são insatisfazíveis |
| R | a fórmula repetida já era consequência (e as premissas abertas só crescem) |

Em todos os casos há contradição, logo esse passo $p$ não existe.

**Uso nas práticas (contraposição).** Se $\Sigma \not\models \psi$ então
$\Sigma \nvdash \psi$. Para mostrar $\phi_1, \dots, \phi_n \nvdash \psi$
basta uma valoração $v$ com $v(\phi_i) = V$ para todo o $i$ e
$v(\psi) = F$.

::: {.exemplo title="--- Afirmar o consequente não se deduz"}
**$p\to q,\ q \nvdash p$.** Seja $v(p)=F$, $v(q)=V$. De $\models_v q$
segue $\models_v p\to q$ e $\models_v q$, mas $\not\models_v p$. Logo
$p\to q,\ q \not\models p$ e, pela integridade de DN,
$p\to q,\ q \nvdash p$.
:::

::: {.pratica title="--- Integridade (Aulas 9-10, slide 11)"}
- **Aulas 9--10, slide 11** Mostra que $\neg p \lor (q \to p) \nvdash
  \neg p \land q$.
:::

## Completude de DN

Toda a consequência semântica se deduz em DN; em particular, toda a
tautologia é teorema. Parece mais difícil (quando todas as valorações
satisfazem $\phi$, tem de haver uma dedução), e a prova constrói-a.

::: {.definicao title="--- A fórmula ψ sob v"}
Para uma valoração $v$ e uma fórmula $\psi$:
$$\psi^v = \begin{cases} \psi & \text{se } v(\psi) = V\\ \neg\psi & \text{se } v(\psi) = F\end{cases}$$
$\psi^v$ é sempre verdadeira em $v$.
:::

::: {.definicao title="--- Lema 1"}
Se as variáveis de $\phi$ são $q_1, \dots, q_n$ e $v$ é uma valoração,
então $q_1^v, \dots, q_n^v \vdash \phi^v$.
:::

Exemplo: $\phi = p\land q$, $v(p) = V$, $v(q) = F$. Então $p^v = p$,
$q^v = \neg q$ e $(p\land q)^v = \neg(p\land q)$, e o lema dá
$p, \neg q \vdash \neg(p\land q)$: uma linha da tabela de verdade
transforma-se numa dedução.

**Prova do Lema 1**, por indução na estrutura de $\phi$ (número de
conectivos):

- $\phi = q_1$: $q_1^v \vdash q_1^v$ (R).
- $\phi = \neg\phi_1$, com $q_1^v, \dots, q_n^v \vdash \phi_1^v$ (hipótese
  de indução). Se $v(\phi) = V$, então $v(\phi_1) = F$ e
  $\phi^v = \neg\phi_1 = \phi_1^v$: já está. Se $v(\phi) = F$, então
  $v(\phi_1) = V$, $\phi_1^v = \phi_1$ e $\phi^v = \neg\neg\phi_1$:
  acrescenta-se $\neg\neg$I à dedução de $\phi_1$.
- $\phi = \phi_1 \circ \phi_2$, com $\circ \in \{\land, \lor, \to\}$. Sejam
  $p_1, \dots, p_l$ e $r_1, \dots, r_k$ as variáveis de $\phi_1$ e
  $\phi_2$ ($\{q_1, \dots, q_n\}$ é a sua união). De
  $p_1^v, \dots, p_l^v \vdash \phi_1^v$ e
  $r_1^v, \dots, r_k^v \vdash \phi_2^v$ obtém-se, por $\land$I,
  $q_1^v, \dots, q_n^v \vdash \phi_1^v \land \phi_2^v$. Falta, em cada
  caso de valores, uma dedução $\phi_1^v \land \phi_2^v \vdash \phi^v$:

| $\circ$ | $v(\phi_1)$ | $v(\phi_2)$ | $\phi^v$ | dedução que falta |
|:-:|:-:|:-:|:-:|:--|
| $\to$ | V | F | $\neg(\phi_1\to\phi_2)$ | $\phi_1\land\neg\phi_2 \vdash \neg(\phi_1\to\phi_2)$ |
| $\to$ | F | F | $\phi_1\to\phi_2$ | $\neg\phi_1\land\neg\phi_2 \vdash \phi_1\to\phi_2$ |
| $\to$ | F | V | $\phi_1\to\phi_2$ | $\neg\phi_1\land\phi_2 \vdash \phi_1\to\phi_2$ |
| $\to$ | V | V | $\phi_1\to\phi_2$ | $\phi_1\land\phi_2 \vdash \phi_1\to\phi_2$ |
| $\land$ | V | V | $\phi_1\land\phi_2$ | nenhuma (já é $\phi^v$) |
| $\land$ | F | V | $\neg(\phi_1\land\phi_2)$ | $\neg\phi_1\land\phi_2 \vdash \neg(\phi_1\land\phi_2)$ |
| $\land$ | V | F | $\neg(\phi_1\land\phi_2)$ | $\phi_1\land\neg\phi_2 \vdash \neg(\phi_1\land\phi_2)$ |
| $\land$ | F | F | $\neg(\phi_1\land\phi_2)$ | $\neg\phi_1\land\neg\phi_2 \vdash \neg(\phi_1\land\phi_2)$ |
| $\lor$ | F | F | $\neg(\phi_1\lor\phi_2)$ | $\neg\phi_1\land\neg\phi_2 \vdash \neg(\phi_1\lor\phi_2)$ |
| $\lor$ | V | V | $\phi_1\lor\phi_2$ | $\phi_1\land\phi_2 \vdash \phi_1\lor\phi_2$ |
| $\lor$ | F | V | $\phi_1\lor\phi_2$ | $\neg\phi_1\land\phi_2 \vdash \phi_1\lor\phi_2$ |
| $\lor$ | V | F | $\phi_1\lor\phi_2$ | $\phi_1\land\neg\phi_2 \vdash \phi_1\lor\phi_2$ |

::: {.exemplo title="--- Um caso do Lema 1 (slide 20)"}
$\phi_1\land\neg\phi_2 \vdash \neg(\phi_1\to\phi_2)$: supõe-se a
implicação e chega-se a $\mathbf{F}$.

```{.fitch seq="phi1 /\ ~phi2 |- ~(phi1 -> phi2)"}
phi1 /\ ~phi2
---
|> phi1 -> phi2
|  phi1              ; &E, 1
|  phi2              ; ->E, 2, 3
|  ~phi2             ; &E, 1
|  F                 ; FI, 4, 5
~(phi1 -> phi2)      ; ~I, 2-6
```
:::

::: {.definicao title="--- Proposição 2: tautologias são teoremas"}
Se $\models \phi$ então $\vdash \phi$.
:::

**Prova.** Sejam $p_1, \dots, p_n$ as variáveis de $\phi$. Como $\phi$ é
tautologia, $v(\phi) = V$ e portanto $\phi^v = \phi$ para **toda** a $v$;
pelo Lema 1, $p_1^v, \dots, p_n^v \vdash \phi$ para toda a $v$. Em
particular, para cada escolha de $p_1^v, \dots, p_{n-1}^v$:
$$p_1^v, \dots, p_{n-1}^v, p_n \vdash \phi \qquad\text{e}\qquad p_1^v, \dots, p_{n-1}^v, \neg p_n \vdash \phi$$
Juntam-se as duas com TE ($\vdash p_n\lor\neg p_n$) e $\lor$E: a primeira
dedução é o caso $p_n$, a segunda o caso $\neg p_n$, e fica
$p_1^v, \dots, p_{n-1}^v \vdash \phi$. Repetindo para
$p_{n-1}, \dots, p_1$, elimina-se uma variável de cada vez até
$\vdash \phi$.

![](figuras/completude_eliminacao.pdf){width=62%}

*Com duas variáveis $p, q$: as 4 deduções do Lema 1 juntam-se duas a duas.*

::: {.exemplo title="--- Proposição 2 para p → p"}
Uma variável, duas valorações. O Lema 1 dá $p \vdash p\to p$ (linhas
2--5) e $\neg p \vdash p\to p$ (linhas 6--10); TE e $\lor$E juntam-nas:

```{.fitch seq="|- p -> p"}
p \/ ~p              ; TE
|> p
||> p
||  p                ; R, 2
|  p -> p            ; ->I, 3-4
|> ~p
||> p
||  F                ; FI, 7, 6
||  p                ; FE, 8
|  p -> p            ; ->I, 7-9
p -> p               ; vE, 1, 2-5, 6-10
```
:::

Para passar das tautologias às consequências com premissas:

::: {.definicao title="--- Lema da dedução e Lema 4"}
- **Lema da dedução:** $\Sigma \cup \{\phi\} \vdash \psi$ sse
  $\Sigma \vdash \phi\to\psi$. ($\Rightarrow$: supõe-se $\phi$, copia-se a
  dedução até $\psi$ e aplica-se $\to$I. $\Leftarrow$: com $\phi$ como
  premissa, à dedução de $\phi\to\psi$ junta-se $\to$E.)
- **Lema 4:** $\phi_1, \dots, \phi_n \models \psi$ sse
  $\models \phi_1\to(\phi_2\to(\dots(\phi_n\to\psi)\dots))$. (Uma $v$ só
  falsifica a implicação encadeada se $v(\phi_i) = V$ para todo o $i$ e
  $v(\psi) = F$, que é exatamente uma $v$ que contradiz
  $\phi_1, \dots, \phi_n \models \psi$.)
:::

::: {.definicao title="--- Proposição 3: completude"}
Se $\phi_1, \dots, \phi_n \models \psi$ então
$\phi_1, \dots, \phi_n \vdash \psi$.
$$\begin{aligned}
\phi_1, \dots, \phi_n \models \psi
&\;\xrightarrow{\text{Lema 4}}\; \models \phi_1\to(\dots(\phi_n\to\psi)\dots)\\
&\;\xrightarrow{\text{Prop. 2}}\; \vdash \phi_1\to(\dots(\phi_n\to\psi)\dots)\\
&\;\xrightarrow{\text{lema da dedução, } n \text{ vezes}}\; \phi_1, \dots, \phi_n \vdash \psi
\end{aligned}$$
O resultado vale também para $\Sigma$ infinito. Com a integridade: para
qualquer conjunto $\Sigma$, $\Sigma \models \phi$ sse $\Sigma \vdash \phi$.
:::

::: {.pratica title="--- Completude: os casos do Lema 1 (Aulas 9-10, slides 20-22)"}
Deduz em DN (só regras base) os outros casos da tabela do Lema 1. Pista:
para $\to$, supor $\phi_1$; para $\neg(\dots)$, supor o que está negado e
chegar a $\mathbf{F}$.

- **Aulas 9--10, slides 20--22 (a)** $\neg\phi_1\land\neg\phi_2 \vdash \phi_1\to\phi_2$
- **Aulas 9--10, slides 20--22 (b)** $\neg\phi_1\land\phi_2 \vdash \neg(\phi_1\land\phi_2)$
- **Aulas 9--10, slides 20--22 (c)** $\neg\phi_1\land\neg\phi_2 \vdash \neg(\phi_1\lor\phi_2)$
- **Aulas 9--10, slides 20--22 (d)** $\neg\phi_1\land\phi_2 \vdash \phi_1\lor\phi_2$

Os casos restantes da tabela são a mesma técnica.
:::

## Decidibilidade da lógica proposicional

::: {.definicao title="--- Decidibilidade"}
Dados $\Sigma$ (finito†) e $\phi$, é **decidível** se $\Sigma \vdash
\phi$: há um algoritmo que responde sempre sim ou não.
:::

Pela integridade e pela completude, decidir $\Sigma \vdash \phi$ é o
mesmo que decidir $\Sigma \models \phi$. Pelo lema da dedução (e pelo
Lema 4) pode supor-se $\Sigma = \emptyset$. Basta então construir a tabela
de verdade de $\phi$, que é finita, e ver se é tautologia.

**Corolários.** É decidível se uma fórmula é **teorema** (= válida). É
decidível se uma fórmula é **satisfazível**: $\phi$ é satisfazível sse
$\neg\phi$ não é tautologia.
