---
title: "Lógica Computacional --- Resumo Teórico"
author: "Gonçalo Sousa"
date: "Atualizado: Semana 2 (Aulas 1--3)"
---

<!-- processado: Teoricas/Aula_01.pdf, Teoricas/Aula_02.pdf, Teoricas/Aula_03.pdf -->

# Aula 1 --- Introdução à Lógica e Sintaxe da Lógica Proposicional

## O que é a lógica e porque interessa à informática

A **lógica** estuda os métodos e princípios que distinguem um raciocínio
correto de um incorreto. A lógica formal nasce com Aristóteles (silogismos:
regras de inferência como o *modus ponens* — de $A \to B$ e $A$ infere-se
$B$), mas só se torna **lógica matemática** a partir do séc. XIX (Boole,
Frege, Hilbert, Gödel...), associada a problemas de fundamentação da
matemática: teoria de modelos, teoria da dedução (prova) e sistemas
axiomáticos.

::: atencao
Cuidado com silogismos "parecidos" que não são válidos. "Todos os homens são
mortais; Sócrates é homem; logo Sócrates é mortal" é válido. Mas "Todos os
homens são mortais; Sócrates era mortal; logo todos os homens são Sócrates"
**não é válido**, apesar de ter a mesma aparência superficial — a forma do
argumento é que importa, não o facto de as frases "soarem" parecidas.
:::

Uma **lógica** (no sentido abstrato) é composta por três partes:

1. uma **linguagem/sintaxe** — um alfabeto e regras para construir *fórmulas*;
2. uma **semântica** — uma noção do que é verdadeiro (pode haver várias
   interpretações semânticas para a mesma sintaxe);
3. um **sistema de dedução** — um conjunto finito de regras que permite obter
   fórmulas novas a partir de outras (raciocinar). Interessa que seja
   **correto** (*sound*): tudo o que se deduz é verdadeiro; e idealmente
   **completo**: tudo o que é verdadeiro é dedutível (nem sempre é possível
   ter as duas coisas — é isso que o curso vai explorar com os teoremas de
   correção e completude).

Neste curso trabalha-se sobretudo com a **lógica clássica** (proposicional e
de primeira ordem). Há outras famílias de lógica — lógica de ordem superior,
lógicas sub-estruturais (ex: intuicionista, onde $\neg\neg A \not\Leftrightarrow A$,
ao contrário do que veremos aqui) e lógicas modais (onde a verdade é
parametrizada, ex: por tempo — "Hoje é segunda-feira" só é verdade nalguns
"mundos"). É útil ter estas categorias em mente para perceber porque é que a
lógica clássica que vamos estudar faz as suposições que faz (por exemplo,
todas as proposições são verdadeiras ou falsas — nunca as duas nem nenhuma —
o chamado *princípio do terceiro excluído*, que não vale em lógica
intuicionista).

A lógica é relevante para a informática em várias frentes: circuitos digitais
(lógica booleana), inteligência artificial, autómatos finitos (correspondem a
fórmulas de lógica monádica de segunda ordem), XML/documentos estruturados,
classes de complexidade caracterizadas por classes de fórmulas, linguagens de
programação (programação lógica como Prolog; sistemas de tipos = sistemas
dedutivos), verificação e especificação formal (hardware, software, protocolos
de segurança), dedução automática (SAT/SMT solvers) e provadores de teoremas
assistidos (Coq, Isabelle, Agda).

## Proposições

::: {.definicao title="--- Proposição"}
Uma **proposição** é uma frase declarativa à qual se pode atribuir um valor de
verdade, **V** (verdadeiro) ou **F** (falso) — e apenas um dos dois. Frases
que não afirmam nada com um valor de verdade definido (perguntas, ordens,
expressões sem verbo, ou frases com variáveis livres cujo valor de verdade
depende de algo não especificado) **não são proposições**.
:::

::: {.exemplo title="--- Exercício 1.1 (lab, proplogic.pdf) --- 5 das 8 alíneas, escolhidas para não repetir a mesma ideia"}
Para cada frase, indicar se é proposição e, sendo, o seu valor de verdade
(as 8 alíneas do enunciado testam só 5 ideias distintas — ver nota a
seguir à caixa):

**(a)** "O Porto é a capital de Portugal." — É proposição. **F** (a capital é
    Lisboa). *(caso base: frase factual simples, com valor de verdade
    definido.)*

**(d)** "$1+2+3$" — **Não é proposição**: é uma expressão/termo (um número), não
    uma afirmação. Não diz nada que possa ser verdadeiro ou falso.

**(c)** "Hei de comparar-te a um dia de verão?" — **Não é proposição**: é uma
    pergunta (interrogativa), não uma afirmação — não tem valor de verdade
    (nota que isto é um motivo *diferente* do de (d): ali era por não ser
    uma afirmação de todo, aqui é por ser uma pergunta).

**(g)** "$x+y$ é um número par." — **Não é proposição**: $x$ e $y$ são
    *variáveis livres* — o valor de verdade depende de que valores lhes
    atribuirmos (é verdade para $x=1,y=1$, falso para $x=1,y=2$). A frase só
    passa a ter um valor de verdade fixo depois de fixarmos $x$ e $y$.

**(h)** "Existe um $x$ tal que $7+x$ é um número par." — É proposição, e **V**:
    apesar de ter uma variável, o quantificador "existe um $x$" **fecha** a
    variável — a frase inteira já não depende de nenhum $x$ externo (basta
    $x=1$: $7+1=8$ é par). Compara com (g): a diferença entre uma variável
    livre (não é proposição) e uma variável quantificada (é proposição) só
    fica completamente formal em lógica de primeira ordem, mais à frente no
    curso — mas já vale a pena notar a distinção agora.
:::

::: atencao
As alíneas (b), (e) e (f) do Exercício 1.1 ficam de fora de propósito —
testam exatamente a mesma ideia de (a) (frase factual simples, decidir V/F),
só com outro assunto. Não precisas de as fazer; se quiseres confirmar que
percebeste, é literalmente o mesmo passo de (a) com números diferentes.
:::

## Conectivos lógicos

Cada proposição simples é representada por uma **variável proposicional**
($p, q, r, \dots$), e proposições compostas obtêm-se combinando-as com
**conectivos**:

| Conectivo | Símbolo | Aridade | Outros símbolos equivalentes |
|---|---|---|---|
| Conjunção ("e") | $\land$ | 2 | `&`, `&&`, $\cdot$ |
| Disjunção ("ou") | $\lor$ | 2 | `|`, `+` |
| Negação ("não") | $\neg$ | 1 | $\sim$, $\bar{\ }$, `!` |
| Implicação ("se...então") | $\to$ | 2 | $\Rightarrow$, $\supset$ |

## Linguagem da lógica proposicional

::: {.definicao title="--- Alfabeto"}
A linguagem da lógica proposicional é construída a partir dos símbolos
primitivos:

- um conjunto **numerável** de variáveis proposicionais
  $\mathcal{V}_{Prop} = \{p, q, r, \dots, p_1, \dots\}$;
- os conectivos lógicos $\land, \lor, \neg, \to$;
- os parêntesis `(` e `)`.
:::

::: {.definicao title="--- Fórmula bem formada"}
O conjunto das **fórmulas** ($\phi, \psi, \theta, \dots$) é definido
indutivamente:

1. uma variável proposicional $p$ é uma fórmula;
2. se $\phi$ é fórmula, então $(\neg\phi)$ é fórmula;
3. se $\phi$ e $\psi$ são fórmulas, então $(\phi \land \psi)$, $(\phi \lor \psi)$
   e $(\phi \to \psi)$ são fórmulas.

Nada mais é fórmula. Exemplo: $((p \land (\neg p)) \to (\neg(p \land (q \lor r))))$.
:::

Esta definição indutiva é o que permite desenhar a **árvore sintática** de
uma fórmula: a raiz é o conectivo principal, e os seus filhos são as
fórmulas que ele combina (recursivamente, até chegar às variáveis, que são
as folhas).

### Convenção para omitir parêntesis

Escrever todos os parêntesis torna as fórmulas ilegíveis, por isso usa-se
uma convenção de precedência (tal como em aritmética, onde $\times$ tem
prioridade sobre $+$):

- os parêntesis mais exteriores podem ser omitidos;
- $\neg$ tem prioridade sobre $\land$;
- $\land$ tem prioridade sobre $\lor$;
- $\lor$ tem prioridade sobre $\to$;
- $\land$ e $\lor$ são **associativos à esquerda**;
- $\to$ é **associativo à direita**.

::: exemplo
- $\phi \land \psi \lor \theta$ abrevia $((\phi \land \psi) \lor \theta)$
  (o $\land$ "agarra" primeiro).
- $p \land \neg p \to \neg(p \land (q \lor r))$ corresponde a
  $((p \land (\neg p)) \to (\neg(p \land (q \lor r))))$.
- $p \to q \to r$ corresponde a $p \to (q \to r)$ (associatividade à
  direita do $\to$: lê-se "de dentro para fora", começando pelo lado
  direito).
:::

::: {.definicao title="--- Subfórmula"}
Uma **subfórmula imediata** de $\psi$ é: (1) nenhuma, se $\psi$ é uma
variável; (2) $\phi$, se $\psi = \neg\phi$; (3) $\phi$ e $\psi'$, se
$\psi = \phi \land \psi'$, $\phi \lor \psi'$ ou $\phi \to \psi'$.

$\phi$ é **subfórmula** de $\psi$ se $\phi$ é subfórmula imediata de $\psi$,
ou se existe $\theta$ tal que $\phi$ é subfórmula de $\theta$ e $\theta$ é
subfórmula de $\psi$ (fecho transitivo das subfórmulas imediatas). Por
convenção, $\psi$ é sempre subfórmula de si própria.
:::

O exercício seguinte junta a convenção de precedência, a árvore sintática e a
noção de subfórmula — a melhor forma de treinar os três em conjunto é
desenhar a árvore completa e depois ler as subfórmulas diretamente dos nós
dessa árvore (cada nó interno, incluindo a raiz, é uma subfórmula; as folhas
são as variáveis).

::: {.exemplo title="--- Exercício 1.3(a) (lab, proplogic.pdf)"}
**Fórmula:** $p \land \neg q \to \neg p$.

**Passo 1 — reintroduzir os parêntesis pela convenção de precedência.**
$\neg$ agarra primeiro: $\neg q$ e $\neg p$. Depois $\land$: $p \land (\neg q)$.
Por fim $\to$ (o conectivo de menor prioridade, por isso é a raiz):
$$\big(p \land (\neg q)\big) \to (\neg p)$$

**Passo 2 — árvore sintática** (raiz = conectivo principal, $\to$):

![Árvore sintática de p ∧ ¬q → ¬p](figuras/arvore_1_3a.pdf){width=45%}

**Passo 3 — lista de subfórmulas** (lidas diretamente dos nós da árvore, da
raiz para as folhas): $p \land \neg q \to \neg p$ (a própria fórmula),
$p \land \neg q$, $\neg p$, $p$, $\neg q$, $q$.
:::

::: {.exemplo title="--- Exercício 1.3(c) (lab, proplogic.pdf)"}
**Fórmula:** $\neg(s \to (\neg(p \to (q \lor \neg s))))$.

Aqui os parêntesis já vêm quase todos explícitos no enunciado — só falta
decompor "de fora para dentro" para identificar cada conectivo principal.
Vamos dar um nome a cada subfórmula à medida que aparece, de dentro para
fora (é a ordem inversa da leitura, mas é a ordem em que a árvore se
constrói):

- $A = q \lor \neg s$ (disjunção de $q$ com $\neg s$)
- $B = p \to A$
- $C = \neg B$
- $D = s \to C$
- $E = \neg D$ (a fórmula toda)

**Árvore sintática:**

![Árvore sintática de ¬(s → ¬(p → (q ∨ ¬s)))](figuras/arvore_1_3c.pdf){height=12cm}

**Subfórmulas:** $E$ (a própria fórmula), $D = s \to \neg(p \to (q\lor\neg s))$,
$s$, $C = \neg(p \to (q \lor \neg s))$, $B = p \to (q \lor \neg s)$, $p$,
$A = q \lor \neg s$, $q$, $\neg s$, $s$ (repara que $s$ aparece **duas
vezes** na árvore, como dois nós diferentes — mas é a mesma fórmula, só se
lista uma vez no conjunto de subfórmulas).
:::

::: {.exemplo title="--- Exercício 1.3(e) (lab, proplogic.pdf)"}
**Fórmula:** $(p \to q) \land (\neg r \to (q \lor (\neg p \land r)))$.

De novo os parêntesis já resolvem a ambiguidade; só falta identificar a
estrutura. O conectivo principal é o $\land$ mais exterior, que combina dois
ramos:

- ramo esquerdo: $L = p \to q$
- ramo direito: $M = \neg r \to M_2$, onde $M_2 = q \lor M_1$ e
  $M_1 = \neg p \land r$

**Árvore sintática:**

![Árvore sintática de (p → q) ∧ (¬r → (q ∨ (¬p ∧ r)))](figuras/arvore_1_3e.pdf){width=85%}

**Subfórmulas:** a fórmula toda, $L = p \to q$, $p$, $q$,
$M = \neg r \to (q \lor (\neg p \land r))$, $\neg r$, $r$,
$M_2 = q \lor (\neg p \land r)$, $q$, $M_1 = \neg p \land r$, $\neg p$, $p$, $r$.
:::

::: atencao
Nota adicional (não estava explícito nos slides, mas é essencial para não
errar nos exercícios): quando reconstróis os parêntesis pela convenção de
precedência, faz sempre isso **antes** de tentar desenhar a árvore — tentar
fazer as duas coisas ao mesmo tempo é a fonte mais comum de erros. Também
repara que o conectivo **principal** de uma fórmula (a raiz da árvore) é
sempre o de **menor prioridade** entre os que aparecem "soltos" (não dentro
de parêntesis explícitos) — por isso em 1.3(a) a raiz é $\to$ e não $\land$,
mesmo aparecendo $\land$ mais à esquerda na leitura da fórmula.
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

::: {.definicao title="--- Valoração (atribuição de valores de verdade)"}
Uma **valoração** é uma função $v : \mathcal{V}_{Prop} \to \{V, F\}$ que
atribui um valor de verdade a cada variável proposicional. Estende-se ao
conjunto das fórmulas por indução na estrutura:

1. $v(p)$ já está definido, para $p \in \mathcal{V}_{Prop}$;
2. $v(\neg\phi) = V$ se $v(\phi) = F$, e $v(\neg\phi) = F$ se $v(\phi) = V$;
3. $v(\phi \land \psi) = V$ sse $v(\phi) = V$ e $v(\psi) = V$ (senão $F$);
4. $v(\phi \lor \psi) = V$ sse $v(\phi) = V$ ou $v(\psi) = V$ (senão $F$);
5. $v(\phi \to \psi) = F$ sse $v(\phi) = V$ e $v(\psi) = F$ (senão $V$).
:::

::: atencao
O caso mais contra-intuitivo é a implicação: $\phi \to \psi$ só é **falsa**
quando o antecedente é verdadeiro e o consequente é falso. Em particular,
sempre que o antecedente $\phi$ é **falso**, a implicação inteira é
**verdadeira**, independentemente do consequente ("de uma premissa falsa
pode concluir-se o que quiser" — *ex falso quodlibet*). Isto vai ser usado
constantemente nas provas "sem construir a tabela de verdade" (Exercício
1.14, Aula 2).
:::

| $\phi$ | $\neg\phi$ | | $\phi$ | $\psi$ | $\phi\land\psi$ | | $\phi$ | $\psi$ | $\phi\lor\psi$ | | $\phi$ | $\psi$ | $\phi\to\psi$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F | V | | F | F | F | | F | F | F | | F | F | V |
| V | F | | F | V | F | | F | V | V | | F | V | V |
| | | | V | F | F | | V | F | V | | V | F | F |
| | | | V | V | V | | V | V | V | | V | V | V |

Uma fórmula $\phi$ com $n$ variáveis proposicionais tem $2^n$ valorações
possíveis (cada variável pode ser $V$ ou $F$, independentemente das
outras) — constrói-se uma **tabela de verdade** com uma linha por
valoração, calculando o valor de $\phi$ coluna a coluna (dos operadores mais
"internos" para o mais "externo", exatamente como na árvore sintática).

::: {.exemplo title="--- Exercício 1.4(b) (lab, proplogic.pdf)"}
Construir a tabela de verdade de $\neg q \land (p \to q)$ (2 variáveis, logo
4 linhas):

| $p$ | $q$ | $\neg q$ | $p \to q$ | $\neg q \land (p \to q)$ |
|---|---|---|---|---|
| V | V | F | V | F |
| V | F | V | F | F |
| F | V | F | V | F |
| F | F | V | V | **V** |

A fórmula só é verdadeira quando $p$ e $q$ são ambos falsos. Isto não é
coincidência: por equivalências semânticas (ver mais abaixo),
$\neg q \land (p \to q) \Leftrightarrow \neg q \land (\neg p \lor q)
\Leftrightarrow (\neg q \land \neg p) \lor (\neg q \land q)
\Leftrightarrow (\neg p \land \neg q) \lor F \Leftrightarrow \neg p \land \neg q$
— exatamente o que a tabela mostra.
:::

::: {.exemplo title="--- Exercício 1.4(c) (lab, proplogic.pdf)"}
Construir a tabela de verdade de $(p \land q) \to \neg(p \lor q)$:

| $p$ | $q$ | $p\land q$ | $p \lor q$ | $\neg(p\lor q)$ | $(p\land q) \to \neg(p\lor q)$ |
|---|---|---|---|---|---|
| V | V | V | V | F | **F** |
| V | F | F | V | F | **V** |
| F | V | F | V | F | **V** |
| F | F | F | F | V | **V** |

Só é falsa na linha $p=V, q=V$: aí o antecedente $p\land q$ é verdadeiro mas
o consequente $\neg(p\lor q)$ é falso (porque $p \lor q$ é verdadeiro). Em
todas as outras linhas o antecedente $p \land q$ já é falso, o que torna a
implicação automaticamente verdadeira (ver nota acima sobre a implicação).
:::

::: {.pratica title="--- Tabelas de verdade (proplogic.pdf)"}
- **1.4 (a)** e **(d)** --- tabelas de verdade, mesma técnica de (b)/(c)
  acima. Na (d), antes de acabar, repara em que linhas o antecedente é
  verdadeiro: é aí que tudo se decide.
:::

## Satisfazibilidade, tautologias e contradições

::: {.definicao title="--- Satisfazibilidade, tautologia, contradição"}
Uma fórmula $\phi$ é:

- **satisfazível** se existe uma valoração $v$ tal que $v(\phi) = V$ —
  escreve-se $\models_v \phi$ e diz-se que $v$ **satisfaz** $\phi$;
- **tautologia** se **todas** as valorações $v$ dão $v(\phi) = V$ —
  escreve-se $\models \phi$ (ex: $\models p \lor \neg p$, o princípio do
  terceiro excluído);
- **contradição** se **todas** as valorações $v$ dão $v(\phi) = F$ —
  escreve-se $\not\models \phi$ (ex: $\not\models p \land \neg p$).

Uma fórmula é **insatisfazível** sse é uma contradição. Uma fórmula
satisfazível mas não tautologia diz-se por vezes **contingente**: é
verdadeira nalgumas valorações e falsa noutras.
:::

# Aula 2 --- Consequência Semântica, Equivalência e Conectivos Completos

## A relação de satisfação $\models_v$

A extensão de $v$ às fórmulas (aula anterior) pode ser reescrita como uma
relação $\models_v$, definida indutivamente na estrutura da fórmula — é
apenas outra notação para a mesma coisa, mas é a notação usada daqui em
diante:

::: {.definicao title="--- Relação de satisfação"}
Dada uma valoração $v$, a relação $\models_v$ define-se por:

1. $\models_v p$ sse $v(p) = V$;
2. $\models_v \neg\phi$ sse $\not\models_v \phi$;
3. $\models_v \phi \land \psi$ sse $\models_v \phi$ e $\models_v \psi$;
4. $\models_v \phi \lor \psi$ sse $\models_v \phi$ ou $\models_v \psi$;
5. $\models_v \phi \to \psi$ sse $\not\models_v \phi$ ou $\models_v \psi$.

Diz-se que $v$ **satisfaz** $\phi$ se $\models_v \phi$.
:::

::: exemplo
Com $v(p)=V, v(q)=v(r)=F$, para saber se $\models_v (p \to (q\lor r)) \lor (r \to \neg p)$
basta que **um** dos dois lados da disjunção seja satisfeito. O lado direito,
$r \to \neg p$, é satisfeito porque $\not\models_v r$ (implicação com
antecedente falso). Logo $\models_v (p \to (q\lor r)) \lor (r \to \neg p)$ —
nem foi preciso avaliar o lado esquerdo.
:::

::: {.exemplo title="--- Exercício 1.5(b) (lab, proplogic.pdf)"}
Com $v(p) = V$ e $v(q) = F$, verificar se $\models_v (p \lor \neg q) \land (\neg p \land q)$.

O segundo conjunto, $\neg p \land q$: temos $v(p)=V$ logo $\not\models_v \neg p$
(já falha aqui). Como um conjunto ($\land$) precisa dos **dois** lados
satisfeitos e um deles já falha, $\not\models_v \neg p \land q$. Logo, mesmo
sem avaliar o primeiro conjunto, a conjunção inteira falha:
$\not\models_v (p \lor \neg q) \land (\neg p \land q)$.
:::

::: {.exemplo title="--- Exercício 1.5(e) (lab, proplogic.pdf)"}
Com $v(p) = V$ e $v(q) = F$, verificar se $\models_v ((p \to q) \to p) \to p$.

$p \to q$: $v(p)=V, v(q)=F$, logo $\not\models_v p \to q$ (antecedente
verdadeiro, consequente falso — o único caso em que a implicação falha).
$(p\to q) \to p$: antecedente falso ($\not\models_v p\to q$), logo esta
implicação é automaticamente satisfeita: $\models_v (p\to q)\to p$.
Fórmula toda: $((p\to q)\to p) \to p$: antecedente satisfeito
($\models_v (p\to q)\to p$) **e** consequente satisfeito ($\models_v p$,
porque $v(p)=V$) — logo $\models_v ((p\to q)\to p)\to p$.
:::

::: exame
$((p\to q)\to p)\to p$ é a **Lei de Peirce**, e é de facto uma
**tautologia** (é verdadeira para *qualquer* $v$, não só para o $v$ deste
exercício — podes confirmar construindo a tabela completa com as 4
valorações de $p,q$). É um resultado clássico e frequentemente pedido: é um
dos exemplos-padrão de tautologia que **não é válida em lógica
intuicionista** (relembra a nota da Aula 1 sobre lógicas sub-estruturais) —
distingue-a da lógica clássica que estamos a estudar.
:::

::: atencao
Nota adicional — armadilha comum: **não confundir** $(p\to q)\to p$ (que
aparece na Lei de Peirce acima) com $(q\to p)\to p$ (parecida, mas com $p$ e
$q$ trocados no antecedente). Ao contrário da primeira, $(q\to p)\to p$
**não** é tautologia — falha, por exemplo, com $v(p)=F$: nesse caso
$q \to p = \neg q$ (verdadeiro só se $q$ for falso), e se $v(q)=F$ então
$q\to p$ é verdadeiro, tornando $(q\to p)\to p$ igual a $V \to F = F$. A
posição exata de cada variável na fórmula importa — nunca assumas que uma
fórmula "parecida" com uma tautologia conhecida também o é.
:::

::: {.pratica title="--- A relação $\models_v$ (proplogic.pdf)"}
- **1.5 (a)**, **(c)** e **(d)** --- com $v(p)=V$, $v(q)=F$, avalia de
  dentro para fora, como em (b)/(e) acima.
:::

## Satisfazibilidade de um conjunto de fórmulas

::: {.definicao title="--- Satisfazibilidade de um conjunto"}
Seja $\Gamma$ um conjunto de fórmulas. Uma valoração $v$ **satisfaz**
$\Gamma$ (notação $\models_v \Gamma$) se satisfaz **todas** as fórmulas de
$\Gamma$: $\forall \psi \in \Gamma,\ \models_v \psi$. $\Gamma$ é
**satisfazível** se existe alguma valoração que o satisfaz.
:::

## Consequência semântica e equivalência

::: {.definicao title="--- Consequência semântica ($\\models$)"}
$\phi$ é **consequência semântica** de $\Gamma$ (notação $\Gamma \models \phi$)
se **toda** valoração $v$ que satisfaz $\Gamma$ também satisfaz $\phi$.

Casos especiais de notação:

- $\emptyset \models \phi$ escreve-se $\models \phi$ — equivale a $\phi$ ser
  tautologia (nenhuma condição sobre $v$: tem de valer sempre).
- Se $\Gamma = \{\psi\}$, escreve-se $\psi \models \phi$.
- Se $\psi \models \phi$ **e** $\phi \models \psi$, $\psi$ e $\phi$ dizem-se
  **semanticamente equivalentes**, escreve-se $\psi \Leftrightarrow \phi$
  (têm exatamente o mesmo valor de verdade em qualquer valoração).
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

Estas leis funcionam como uma "álgebra booleana": permitem transformar uma
fórmula noutra equivalente sem ter de recorrer à tabela de verdade —
substituindo subfórmulas pelo seu equivalente, passo a passo (tal como se
faz álgebra normal, mas com $\land,\lor,\neg$ em vez de $\times,+$).

::: {.atencao title="--- Leis extra para simplificar"}
Nota adicional (não estão na tabela dos slides nem na do enunciado, mas
são precisas para **simplificar** uma fórmula até se ver o que ela é ---
cada uma confirma-se com uma tabela de 2 linhas). $V$ e $F$ representam
uma fórmula sempre verdadeira e uma sempre falsa:

| Lei | Equivalência |
|---|---|
| Complementaridade | $\phi\lor\neg\phi \Leftrightarrow V$ ; $\phi\land\neg\phi \Leftrightarrow F$ |
| Elemento neutro | $\phi\lor F \Leftrightarrow \phi$ ; $\phi\land V \Leftrightarrow \phi$ |
| Elemento absorvente | $\phi\lor V \Leftrightarrow V$ ; $\phi\land F \Leftrightarrow F$ |
| Absorção | $\phi\lor(\phi\land\psi) \Leftrightarrow \phi$ ; $\phi\land(\phi\lor\psi) \Leftrightarrow \phi$ |
:::

::: {.exemplo title="--- Exercício 1.6(a) (lab, proplogic.pdf)"}
Mostrar que $\neg(p \to q) \Leftrightarrow p \land \neg q$, usando as leis
(sem tabela de verdade):

$$\neg(p\to q) \overset{\text{(implicação)}}{\Leftrightarrow} \neg(\neg p \lor q)
\overset{\text{(De Morgan)}}{\Leftrightarrow} \neg\neg p \land \neg q
\overset{\text{(dupla negação)}}{\Leftrightarrow} p \land \neg q$$

Cada passo substitui uma subfórmula pelo seu equivalente segundo uma única
lei da tabela — é assim que se lê/escreve qualquer prova por equivalências.
:::

::: {.exemplo title="--- Exercício 1.6(e) (lab, proplogic.pdf)"}
Mostrar que $(p \lor q) \to r \Leftrightarrow (p \to r) \land (q \to r)$:

$$(p\lor q) \to r
\overset{\text{(implicação)}}{\Leftrightarrow} \neg(p\lor q) \lor r
\overset{\text{(De Morgan)}}{\Leftrightarrow} (\neg p \land \neg q) \lor r$$

Agora aplica-se a distributividade — $(\phi\land\psi)\lor\theta \Leftrightarrow (\phi\lor\theta)\land(\psi\lor\theta)$
— com $\phi=\neg p$, $\psi=\neg q$, $\theta=r$:

$$(\neg p \land \neg q) \lor r
\overset{\text{(distributividade)}}{\Leftrightarrow} (\neg p \lor r) \land (\neg q \lor r)
\overset{\text{(implicação, 2x)}}{\Leftrightarrow} (p \to r) \land (q \to r)$$
:::

::: atencao
Guarda a equivalência do Exercício 1.6(e) — $(p\lor q)\to r \Leftrightarrow (p\to r)\land(q\to r)$
— porque vai reaparecer, já pronta a reutilizar, no Exercício 1.13(d) mais
abaixo (justificação de consequência semântica sem trabalho extra).
:::

::: {.exemplo title="--- Exercício 1.8(a) e 1.8(b) (lab, proplogic.pdf) --- distribuir a implicação sobre a conjunção"}
**(a) $(p\to q) \land (p\to r) \Leftrightarrow p \to (q\land r)$ — é
válida.** Prova pelas leis:
$$(p\to q)\land(p\to r) \Leftrightarrow (\neg p\lor q)\land(\neg p\lor r)
\overset{\text{(distributividade)}}{\Leftrightarrow} \neg p \lor (q\land r)
\Leftrightarrow p \to (q\land r)$$

**(b) $(p\to r) \land (q\to r) \Leftrightarrow (p\land q) \to r$ — NÃO é
válida.** Contraexemplo: $v(p)=V, v(q)=F, v(r)=F$.
Lado esquerdo: $p\to r = V\to F = F$; logo $(p\to r)\land(q\to r) = F$.
Lado direito: $p\land q = V\land F = F$; logo $(p\land q)\to r = F \to F = V$.
Lado esquerdo é $F$, lado direito é $V$ — **não são equivalentes**.
:::

::: atencao
Compara com atenção (a) e (b): olham parecidas (ambas "distribuem $\to$
sobre $\land$"), mas só a que distribui $\land$ do lado do **consequente**
(a) é válida — distribuir sobre o **antecedente** (b) já não é. É um erro
muito fácil de cometer sem verificar — usa sempre as leis ou um
contraexemplo para confirmar, nunca "por analogia visual".
:::

### Classificar uma fórmula simplificando-a (Exercício 1.9)

As leis servem também para **classificar** uma fórmula (tautologia,
contradição ou satisfazível), que é o que o Exercício 1.9 pede --- e o
enunciado diz o método: *"You can start by simplifying the formulas using
semantic equivalences"*. Não se faz a tabela de verdade.

::: {.definicao title="--- Método: classificar por equivalências"}
1. **Eliminar as implicações** ($\phi\to\psi \Leftrightarrow \neg\phi\lor\psi$)
   e **empurrar as negações** para dentro (De Morgan, dupla negação).
2. **Simplificar** com as leis (complementaridade, absorção, elemento
   neutro/absorvente) até a fórmula ficar numa forma que se lê logo.
3. **Ler a classificação** do resultado:
   - chegou a $V$ → **tautologia**;
   - chegou a $F$ → **contradição**;
   - chegou a outra coisa (ex.: $p\lor\neg q$) → **satisfazível** (nem
     tautologia nem contradição). O enunciado pede então **uma valoração que a
     torna verdadeira e outra que a torna falsa**: lêem-se da forma
     simplificada, e **confirmam-se na fórmula original**.
:::

::: {.exemplo title="--- Exercício 1.9(d) (lab, proplogic.pdf) --- tautologia"}
$$\begin{aligned}
&p \to (q \to (p \lor q)) \\
\Leftrightarrow\ & \neg p \lor (\neg q \lor (p \lor q)) && \text{(implicação, 2 vezes)}\\
\Leftrightarrow\ & (\neg p \lor p) \lor (\neg q \lor q) && \text{(associatividade e comutatividade do } \lor\text{)}\\
\Leftrightarrow\ & V \lor V && \text{(complementaridade, 2 vezes)}\\
\Leftrightarrow\ & V && \text{(elemento absorvente)}
\end{aligned}$$

Chegou a $V$: é **tautologia**. (Com o $\lor$ tudo ao mesmo nível, os
parêntesis podem reorganizar-se à vontade --- foi isso que permitiu juntar
$\neg p$ com $p$ e $\neg q$ com $q$.)
:::

::: {.exemplo title="--- Exercício 1.9(j) (lab, proplogic.pdf) --- contradição"}
Truque: o segundo conjunto é a **negação** do primeiro.
$$\neg(p \lor \neg q) \overset{\text{(De Morgan)}}{\Leftrightarrow} \neg p \land \neg\neg q \overset{\text{(dupla negação)}}{\Leftrightarrow} \neg p \land q$$
Então, chamando $X = p\lor\neg q$:
$$(p \lor \neg q) \land (\neg p \land q) \;\Leftrightarrow\; X \land \neg X \;\overset{\text{(complementaridade)}}{\Leftrightarrow}\; F$$

Chegou a $F$: é **contradição**.
:::

::: {.exemplo title="--- Exercício 1.9(i) (lab, proplogic.pdf) --- satisfazível"}
$$\begin{aligned}
&(p \lor q) \to (p \land q) \\
\Leftrightarrow\ & \neg(p \lor q) \lor (p \land q) && \text{(implicação)}\\
\Leftrightarrow\ & (\neg p \land \neg q) \lor (p \land q) && \text{(De Morgan)}
\end{aligned}$$

Já não simplifica mais: não é $V$ nem $F$. Lê-se diretamente: é verdadeira
quando **$p$ e $q$ são ambos falsos** ou **ambos verdadeiros** (é
"$p \leftrightarrow q$"). Logo é **satisfazível, mas não tautologia nem
contradição**.

- **Verdadeira** com $p=V, q=V$ (o segundo termo, $p\land q$, é $V$).
  Confirmação na original: $(V\lor V)\to(V\land V) = V\to V = V$.
- **Falsa** com $p=V, q=F$ (os dois termos têm um literal falso).
  Confirmação na original: $(V\lor F)\to(V\land F) = V\to F = F$.
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

As afirmações seguintes envolvem $\Gamma \models \theta$ de forma mais
abstrata (sem fixar fórmulas concretas) — testam se percebeste bem a
**definição** de consequência semântica, não cálculo. A técnica geral: para
mostrar que uma afirmação é **verdadeira**, usa diretamente a definição; para
mostrar que é **falsa**, basta um contraexemplo concreto (escolher $\Gamma$,
$\Sigma$, $\theta$ específicos).

::: {.exemplo title="--- Exercício 1.16(a), (b) e (f) (lab, proplogic.pdf) --- monotonicidade"}
**(a) Se $\Gamma \models \theta$ e $\Gamma \subseteq \Sigma$, então
$\Sigma \models \theta$ — VERDADEIRO.** Seja $v$ uma valoração que satisfaz
$\Sigma$. Como $\Gamma \subseteq \Sigma$, $v$ satisfaz em particular todas as
fórmulas de $\Gamma$ (são também fórmulas de $\Sigma$), logo $\models_v \Gamma$.
Por hipótese $\Gamma\models\theta$, logo $\models_v \theta$. Como isto vale
para qualquer $v$ que satisfaça $\Sigma$, conclui-se $\Sigma \models \theta$.
(Intuição: **acrescentar premissas nunca destrói** uma consequência já
válida — chama-se **monotonicidade**.)

**(b) Se $\Sigma \models \theta$ e $\Gamma \subseteq \Sigma$, então
$\Gamma \models \theta$ — FALSO** (é o recíproco de (a), e a monotonicidade
só funciona num sentido). Contraexemplo: $\theta = q$, $\Sigma = \{p, p\to q\}$,
$\Gamma = \{p\} \subseteq \Sigma$. Tem-se $\Sigma \models q$ (modus ponens:
qualquer $v$ que satisfaça $p$ e $p\to q$ satisfaz $q$). Mas
$\Gamma = \{p\} \not\models q$: a valoração $v(p)=V, v(q)=F$ satisfaz
$\Gamma=\{p\}$ mas não satisfaz $q$. **Menos premissas podem já não bastar**
para a mesma conclusão.

**(f) Se $\Sigma \models \theta$ e $\Sigma \subseteq \Gamma$, então
$\Sigma \cup \Gamma \models \theta$ — VERDADEIRO, e trivialmente.** Repara
que, se $\Sigma \subseteq \Gamma$, então $\Sigma \cup \Gamma = \Gamma$ (a
união de um conjunto com um dos seus sobreconjuntos é o sobreconjunto). A
afirmação reduz-se exatamente a "$\Sigma \models \theta$ e
$\Sigma \subseteq \Gamma$, logo $\Gamma \models \theta$" — que é **o mesmo
enunciado da alínea (a)**, com $\Gamma$ e $\Sigma$ trocados de nome. Não é
preciso prova nova.
:::

::: atencao
A lição de (a)/(b)/(f): $\Gamma \models \theta$ é **monótono ao acrescentar
premissas** (mais hipóteses, no máximo, só ajudam a concluir mais coisas —
nunca deixam de valer uma consequência já estabelecida), mas **não é
monótono ao remover premissas** — retirar uma hipótese pode fazer uma
conclusão válida deixar de o ser. Isto explica intuitivamente porque é que
(a) e (f) são verdadeiros (só acrescentam) e (b) é falso (remove).
:::

::: {.exemplo title="--- Exercício 1.13 (lab, proplogic.pdf)"}
**(a) $\models (p\land\neg p) \to (p\land\neg r)$ — VERDADEIRO.** O
antecedente $p\land\neg p$ é sempre falso (contradição), logo a implicação
é sempre verdadeira, qualquer que seja o consequente — é tautologia.

**(b) $\models (q\lor\neg r) \to (q\land\neg q)$ — FALSO.** O consequente
$q\land\neg q$ é sempre falso (contradição). Logo a implicação só é
verdadeira quando o antecedente também é falso. Mas o antecedente
$q\lor\neg r$ **não** é sempre falso: com $v(q)=V,v(r)=V$,
$q\lor\neg r = V \lor F = V$, e então a implicação dá $V \to F = F$. Não é
tautologia (contraexemplo: $q=V,r=V$).

**(c) $\{(p\to q)\lor r,\ ((p\to q)\lor r)\to\neg r,\ (p\to q)\to(q\to r)\} \models \neg q$
— VERDADEIRO.** Seja $v$ uma valoração que satisfaz as três premissas.
Chamando $\varphi_1 = (p\to q)\lor r$: como $\models_v \varphi_1$ e
$\models_v \varphi_1 \to \neg r$, por modus ponens $\models_v \neg r$, ou
seja $v(r)=F$. Com $r=F$, $\varphi_1 = (p\to q)\lor F$, e como
$\models_v \varphi_1$, tem de ser $\models_v p\to q$. Agora a terceira
premissa, $(p\to q)\to(q\to r)$: como $\models_v p\to q$, por modus ponens
$\models_v q\to r$, isto é $q\to F$, que é equivalente a $\neg q$. Logo
$\models_v \neg q$ — exatamente o que queríamos mostrar, para qualquer $v$
que satisfaça as três premissas.

**(d) $\{(p\lor q)\to r\} \models (p\to r)\lor(q\to r)$ — VERDADEIRO.** Já
sabemos do Exercício 1.6(e) que $(p\lor q)\to r \Leftrightarrow (p\to r)\land(q\to r)$.
Ora $(p\to r)\land(q\to r)$ implica trivialmente $(p\to r)\lor(q\to r)$
(uma conjunção implica sempre a disjunção dos mesmos termos: se ambos são
verdadeiros, em particular um deles é). Logo
$(p\lor q)\to r \models (p\to r)\lor(q\to r)$.
:::

::: {.exemplo title="--- Exercício 1.14(a) e 1.14(d) (lab, proplogic.pdf) --- sem tabela de verdade"}
**(a) $\models p \to (((q\to p)\to p) \to r)$ — FALSO.** Analisa-se por
casos em $p$. Se $v(p)=V$: então $q\to p$ é sempre $V$ (consequente
verdadeiro), logo $(q\to p)\to p = V\to V = V$, e a subfórmula
$((q\to p)\to p)\to r$ reduz-se a $V \to r$, ou seja, ao próprio valor de
$r$. Logo, com $p=V$, a fórmula inteira vale exatamente $v(r)$. Escolhendo
$v(r)=F$ (e $v(q)$ arbitrário, por exemplo $V$), a fórmula dá $F$ — não é
tautologia. **Contraexemplo:** $p=V, q=V, r=F$.

**(d) $\models ((p\land q)\to(s\lor t)) \to ((p\to s)\lor(q\to t))$ —
VERDADEIRO.** Em vez de percorrer as 16 linhas da tabela (4 variáveis),
procura-se diretamente uma forma do consequente ser falso. O consequente
$(p\to s)\lor(q\to t)$ só é falso se **ambos** os lados forem falsos:
$p\to s$ falso exige $p=V,s=F$; $q\to t$ falso exige $q=V,t=F$. Ou seja, o
**único** caso em que o consequente poderia falhar é $p=V,q=V,s=F,t=F$.
Mas nesse caso o antecedente $(p\land q)\to(s\lor t)$ vale
$(V\land V)\to(F\lor F) = V \to F = F$ — ou seja, precisamente nesse caso o
antecedente também é falso, o que torna a implicação exterior verdadeira
($F\to\text{algo}=V$). Como não há mais nenhuma forma de o consequente ser
falso, a implicação exterior nunca é falsa: é tautologia.
:::

::: atencao
Nota adicional sobre a técnica "sem tabela de verdade": o método geral é
**tentar construir um contraexemplo** (fixar a fórmula toda a $F$: para uma
implicação, isso força antecedente $V$ e consequente $F$; segue as
consequências obrigatórias passo a passo). Se o processo chega a uma
contradição (como em 1.14(d), onde a única forma de falhar o consequente
também falha o antecedente), a fórmula é tautologia. Se o processo chega a
uma atribuição consistente (como em 1.14(a)), encontraste mesmo um
contraexemplo. É a mesma ideia usada em 1.13, só que aqui aplicada
sistematicamente à procura do contraexemplo. (Na 1.14 o enunciado proíbe a
tabela mas não obriga às leis: a procura do contraexemplo é o método
natural. Na 1.9, pelo contrário, o enunciado manda simplificar pelas
leis.)
:::

::: {.pratica title="--- Propriedades de $\models$ (proplogic.pdf)"}
- **1.15** --- mesma ideia do Exercício 1.16 acima, mas com $\models$ e
  $\Leftrightarrow$ entre fórmulas genéricas $\varphi,\psi,\theta,\gamma$:
  se for verdadeiro, justifica pelas definições; se for falso, dá
  fórmulas concretas como contraexemplo.
:::

## Quantas proposições podem ser simultaneamente verdadeiras

::: {.exemplo title="--- Exercício 1.7 (lab, proplogic.pdf)"}
Atribuindo valores de verdade a $p,q,r$, quantas das cinco disjunções
$p\lor\neg q,\ \neg p\lor q,\ q\lor r,\ q\lor\neg r,\ \neg q\lor\neg r$ podem
ser simultaneamente verdadeiras?

Como há só 3 variáveis, é viável construir a tabela completa (8 linhas) e
contar, em cada linha, quantas das 5 fórmulas são $V$:

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

O **máximo** é **5** (todas simultaneamente verdadeiras), atingido em
$p=V,q=V,r=F$ — por exemplo, verifica-se que $\neg q\lor\neg r$ dá
$F\lor V = V$ porque $r=F$. O **mínimo** ao longo de todas as valorações é
**3** (nunca é possível ter menos de 3 verdadeiras ao mesmo tempo, e isso
acontece em três linhas diferentes da tabela).
:::

## Conjuntos completos de conectivos

::: {.definicao title="--- Conjunto completo de conectivos"}
Um conjunto de conectivos $C$ é **completo** se, para qualquer função de
verdade $f : \{V,F\}^n \to \{V,F\}$, existe uma fórmula $\phi$ com $n$
variáveis, usando só conectivos de $C$, tal que $\phi$ **induz** exatamente
$f$ (isto é, $F_\phi = f$, onde $F_\phi(x_1,\dots,x_n) = v_\chi(\phi)$ para
$v_\chi(p_i)=x_i$). Por outras palavras: $C$ chega para exprimir *qualquer*
função booleana possível.
:::

**Prova de que $\{\land,\lor,\neg\}$ é completo** (dos slides, por indução em
$n$, o número de variáveis):

- **Base ($n=1$):** há exatamente 4 funções de verdade de aridade 1 (uma
  tabela com 2 linhas tem $2^2=4$ combinações possíveis de saída). Para cada
  uma, exibe-se uma fórmula que a realiza: $f_1 = $ "sempre F" $\to \phi_1 = p\land\neg p$;
  $f_2=\neg p \to \phi_2=\neg p$; $f_3=p \to \phi_3=p$;
  $f_4=$ "sempre V" $\to \phi_4 = p\lor\neg p$.
- **Passo indutivo:** assumindo que a propriedade vale para $n$, seja
  $f:\{V,F\}^{n+1}\to\{V,F\}$. Define-se $f_1(x_1,\dots,x_n)=f(x_1,\dots,x_n,V)$
  e $f_2(x_1,\dots,x_n)=f(x_1,\dots,x_n,F)$ (fixando a última variável). Por
  hipótese de indução existem $\phi_1,\phi_2$ com $F_{\phi_i}=f_i$. Toma-se
  $\phi = (p_{n+1}\land\phi_1)\lor(\neg p_{n+1}\land\phi_2)$: quando
  $x_{n+1}=V$, $\phi$ reduz-se a $\phi_1$; quando $x_{n+1}=F$, reduz-se a
  $\phi_2$ — exatamente o comportamento de $f$.

Como consequência imediata (usando as leis de De Morgan e a lei da
implicação para reescrever $\land$ e $\lor$), também $\{\neg,\to\}$ é
completo: $\phi\land\psi \Leftrightarrow \neg(\phi\to\neg\psi)$ e
$\phi\lor\psi \Leftrightarrow \neg\phi\to\psi$.

(Na Aula 3 aparece uma segunda prova, mais direta, do mesmo resultado: a
construção da **forma normal disjuntiva** a partir da tabela de verdade.)

::: {.exemplo title="--- Exercício 1.19(a) (lab, proplogic.pdf) --- {negação, disjunção} é completo"}
Mostrar que $p\to q$, $p\leftrightarrow q$ e $p\land q$ se escrevem só com
$\neg$ e $\lor$ (a mesma técnica da prova acima, mas explicitada
concretamente):

- $p\to q \Leftrightarrow \neg p \lor q$ (é diretamente a lei da implicação).
- $p\land q \Leftrightarrow \neg(\neg p \lor \neg q)$ (De Morgan aplicado ao
  contrário: $\neg\neg(p\land q) \Leftrightarrow \neg(\neg p\lor\neg q)$, e
  $\neg\neg(p\land q)\Leftrightarrow p\land q$).
- $p\leftrightarrow q \Leftrightarrow (p\to q)\land(q\to p)$. Usando os dois
  pontos anteriores para reescrever cada peça só com $\neg,\lor$:
  $p\to q \Leftrightarrow \neg p\lor q$ e $q\to p \Leftrightarrow \neg q\lor p$;
  e a conjunção dessas duas, pelo ponto anterior ($\phi\land\psi\Leftrightarrow\neg(\neg\phi\lor\neg\psi)$),
  fica:
  $$p\leftrightarrow q \;\Leftrightarrow\; \neg\big(\neg(\neg p\lor q)\lor\neg(\neg q\lor p)\big)$$
  — uma fórmula só com $\neg$ e $\lor$, como pedido.
:::

::: {.exemplo title="--- Exercício 1.19(b) (lab, proplogic.pdf) --- NAND é universal"}
Define-se um novo conectivo $\bar\land$ ("NAND") pela tabela: $V\bar\land V=F$;
$V\bar\land F = F\bar\land V = F\bar\land F = V$ (ou seja,
$p\bar\land q \Leftrightarrow \neg(p\land q)$: só é falso quando ambos são
verdadeiros). Mostrar que $\neg p$, $p\land q$ e $p\lor q$ se escrevem só
com $\bar\land$:

**Negação:** $p \bar\land p \Leftrightarrow \neg(p\land p) \Leftrightarrow \neg p$
(idempotência). Logo $\neg p = p\bar\land p$.

**Conjunção:** $p\bar\land q \Leftrightarrow \neg(p\land q)$, logo
$\neg(p\bar\land q) \Leftrightarrow p\land q$. E $\neg X = X\bar\land X$
(pelo caso anterior, com $X = p\bar\land q$), logo:
$$p \land q \;=\; (p\bar\land q)\ \bar\land\ (p\bar\land q)$$

**Disjunção:** por De Morgan, $p\lor q \Leftrightarrow \neg(\neg p\land\neg q) \Leftrightarrow \neg p \bar\land \neg q$
(a própria definição de $\bar\land$ já é a negação de um $\land$). Substituindo
$\neg p = p\bar\land p$ e $\neg q = q\bar\land q$:
$$p \lor q \;=\; (p\bar\land p)\ \bar\land\ (q\bar\land q)$$

Como $\{\neg,\land,\lor\}$ já é completo e todos os três se escrevem só com
$\bar\land$, conclui-se que **$\{\bar\land\}$ sozinho já é um conjunto
completo de conectivos** — é o princípio por trás dos circuitos NAND em
eletrónica digital (qualquer circuito lógico pode ser construído só com
portas NAND).
:::

## Aplicação: modelar problemas em lógica proposicional

Os problemas seguintes não introduzem teoria nova — mostram como usar tudo
o que já foi visto (tradução para fórmulas, tabelas de verdade,
satisfazibilidade de conjuntos) para resolver problemas de raciocínio
"do mundo real". A técnica chave nos problemas de cavaleiros/vilões é a
**auto-referência**: se $a$ representa "A é cavaleiro" (diz sempre a
verdade) e $S$ é a fórmula que traduz a frase que A disse, então tem de
valer $a \leftrightarrow S$ — A é cavaleiro *sse* o que disse é verdade.

::: {.exemplo title="--- Exercício 1.10(a) (lab, proplogic.pdf) --- ilha dos cavaleiros e vilões"}
A diz: "Pelo menos um de nós [A, B] é vilão." O que são A e B?

Seja $a$ = "A é cavaleiro", $b$ = "B é cavaleiro". A frase de A traduz-se
por $S = \neg a \lor \neg b$. A condição de auto-referência é
$a \leftrightarrow S$, isto é $a \leftrightarrow (\neg a\lor\neg b)$.
Testam-se as 4 valorações de $(a,b)$:

| $a$ | $b$ | $S=\neg a\lor\neg b$ | $a\leftrightarrow S$ |
|---|---|---|---|
| V | V | F | F |
| V | F | V | **V** |
| F | V | V | F |
| F | F | V | F |

Só a linha $a=V,b=F$ é consistente (só nessa a biconditional dá $V$; nas
outras a suposição contradiz-se a si própria). **A é cavaleiro, B é vilão.**
:::

::: {.exemplo title="--- Exercício 1.10(e) (lab, proplogic.pdf) --- três pessoas"}
A, B, C. A diz: "Somos todos vilões." B diz: "Exatamente um de nós é
cavaleiro." O que são A, B e C?

Sejam $a,b,c$ os indicadores "é cavaleiro" de A, B, C. Traduzindo:
$S_A = \neg a\land\neg b\land\neg c$ (todos vilões) e
$S_B = (b\land\neg c)\lor(\neg b\land c)$ (exatamente um entre B e C é
cavaleiro — note-se que $S_B$ já não depende de $a$ diretamente, mas a
condição "exatamente um dos três" só se decompõe assim depois de se saber o
valor de $a$; para manter a tabela simples, calcula-se $S_B$ como "exatamente
um de $\{a,b,c\}$" diretamente nas 8 linhas).

Constrói-se a tabela com as duas condições de auto-referência,
$\mathrm{cond}_1 = (a\leftrightarrow S_A)$ e $\mathrm{cond}_2 = (b\leftrightarrow S_B)$,
para as 8 valorações de $(a,b,c)$ — só interessam as linhas onde **ambas**
são $V$:

| $a$ | $b$ | $c$ | $S_A$ | cond$_1$ | $S_B$ (exat. 1 de a,b,c) | cond$_2$ |
|---|---|---|---|---|---|---|
| V | V | V | F | F | F | F |
| V | V | F | F | F | F | F |
| V | F | V | F | F | F | V |
| V | F | F | F | F | V | F |
| F | V | V | F | V | F | F |
| F | V | F | F | V | **V** | **V** |
| F | F | V | F | V | F | F |
| F | F | F | V | F | V | F |

Só a linha $a=F,b=V,c=F$ tem $\mathrm{cond}_1=V$ **e** $\mathrm{cond}_2=V$
simultaneamente. **A é vilão, B é cavaleiro, C é vilão** — e é a única
solução consistente com as duas afirmações.
:::

::: {.exemplo title="--- Exercício 1.11 (lab, proplogic.pdf) --- suspeitos de um crime"}
Três suspeitos, A, B, C, fazem declarações:
A: "B é culpado, mas C é inocente." B: "Se A é culpado, então C é
culpado." C: "Eu sou inocente, mas um dos outros dois é culpado."

Sejam $g_a,g_b,g_c$ = "A/B/C é culpado". Traduzindo cada declaração:
$$S_A = g_b\land\neg g_c \qquad S_B = g_a\to g_c \qquad S_C = \neg g_c\land(g_a\lor g_b)$$

Constrói-se **uma única tabela de verdade** com as 8 combinações de
$(g_a,g_b,g_c)$ e as três colunas $S_A,S_B,S_C$ — e todas as alíneas
seguintes respondem-se lendo linhas/colunas desta mesma tabela, sem repetir
cálculos:

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

**(a) As três declarações são compatíveis?** Procura-se uma linha com
$S_A=S_B=S_C=V$: só a linha $g_a=F,g_b=V,g_c=F$. Sim, são compatíveis, e de
forma **única** (só B culpado).

**(b) Alguma declaração é consequência das outras duas?** $\{S_A,S_B\}\models S_C$?
As linhas com $S_A=V$ e $S_B=V$ simultaneamente: só a linha
$(F,V,F)$ (a segunda linha tem $S_A=V$ mas $S_B=F$, não conta) — e nessa
linha $S_C=V$ também. Logo **sim**, $\{S_A,S_B\}\models S_C$.
Já $\{S_A,S_C\}\models S_B$? As linhas com $S_A=V$ e $S_C=V$: a linha
$(V,V,F)$ e a linha $(F,V,F)$. Na primeira, $S_B=F$ — contraexemplo! Logo
**não**, $\{S_A,S_C\}\not\models S_B$. E $\{S_B,S_C\}\models S_A$? Só a linha
$(F,V,F)$ tem $S_B=S_C=V$ em simultâneo, e aí $S_A=V$. Logo **sim**. (Nota
como a relação de consequência não é simétrica entre os três pares — mais
uma vez, a monotonicidade não "anda para trás".)

**(c) Assumindo que os três são inocentes, quem mentiu?** Linha
$g_a=F,g_b=F,g_c=F$: $S_A=F$ (A mentiu), $S_B=V$ (B disse a verdade),
$S_C=F$ (C mentiu). **A e C mentiram; B disse a verdade.**

**(d) Assumindo que os três disseram a verdade, quem é inocente/culpado?**
Precisa de $S_A=S_B=S_C=V$ — é exatamente a linha de (a):
$g_a=F,g_b=V,g_c=F$. **Só B é culpado; A e C são inocentes.**

**(e) Assumindo que o inocente disse a verdade e o culpado mentiu, quem é
inocente/culpado?** Esta condição traduz-se, para cada pessoa $X$, por
$S_X \leftrightarrow \neg g_X$ (inocente $\Leftrightarrow$ disse verdade).
Percorrendo a tabela e comparando $S_A$ com $\neg g_a$, $S_B$ com $\neg g_b$
e $S_C$ com $\neg g_c$ em cada linha, só a linha $g_a=V,g_b=F,g_c=V$
satisfaz as três condições ao mesmo tempo ($S_A=F=\neg g_a$;
$S_B=V=\neg g_b$; $S_C=F=\neg g_c$). **A e C são culpados; B é inocente.**
:::

::: atencao
Repara como (c), (d) e (e) dão **três respostas diferentes** ao mesmo
enunciado — cada uma corresponde a uma hipótese diferente sobre quem diz a
verdade. É um erro comum tentar decidir "quem é mesmo culpado" sem antes
fixar qual das três hipóteses está a ser assumida; a tabela de verdade
única (com as colunas $S_A,S_B,S_C$) é o que permite responder às três sem
ambiguidade nem trabalho repetido.
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

Até aqui, para saber se uma fórmula é satisfazível ou tautologia, a única
ferramenta geral era a tabela de verdade --- com $2^n$ linhas para $n$
variáveis. Esta aula mostra que qualquer fórmula pode ser **transformada numa
fórmula semanticamente equivalente com uma forma especial** (uma *forma
normal*), e que, para algumas dessas formas, decidir a satisfazibilidade ou
a validade passa a ser trivial (basta "olhar" para a fórmula). Algumas formas
normais existem para **qualquer** fórmula (negativa, disjuntiva, conjuntiva);
outras só existem para certas classes de fórmulas (Horn).

## Literais e forma normal negativa (FNN)

::: {.definicao title="--- Literal e forma normal negativa"}
Um **literal** é uma variável proposicional $p$ ou a sua negação $\neg p$.
($p$ diz-se literal **positivo**, $\neg p$ literal **negativo**.)

Uma fórmula está em **forma normal negativa** se a negação $\neg$ só
aparece aplicada diretamente a variáveis, isto é, só dentro de literais.
Ex: $(\neg p \land \neg q) \lor p$ está em FNN; $\neg(p \lor q)$ não está.
:::

::: {.definicao title="--- Proposição (existência da FNN)"}
Qualquer fórmula que só use os conectivos $\land$, $\lor$ e $\neg$ é
semanticamente equivalente a uma fórmula em forma normal negativa.

**Prova:** basta aplicar repetidamente as **leis de De Morgan** (que
"empurram" cada $\neg$ para dentro de um $\land$/$\lor$, trocando-o pelo
outro) e eliminar as **duplas negações** ($\neg\neg\phi \Leftrightarrow \phi$)
até cada $\neg$ ficar encostado a uma variável.
:::

::: {.exemplo title="--- FNN de $\\neg((p \\lor q) \\land \\neg p)$ (slides)"}
$$\begin{aligned}
&\neg\big((p \lor q) \land \neg p\big) \\
\overset{\text{(De Morgan, no } \land\text{ exterior)}}{\Leftrightarrow}\ & \neg(p \lor q) \lor \neg\neg p \\
\overset{\text{(De Morgan, em } \neg(p\lor q))}{\Leftrightarrow}\ & (\neg p \land \neg q) \lor \neg\neg p \\
\overset{\text{(dupla negação)}}{\Leftrightarrow}\ & (\neg p \land \neg q) \lor p
\end{aligned}$$

Em cada passo o $\neg$ desce um nível na árvore sintática; quando todos os
$\neg$ estão encostados a variáveis, parou-se: está em FNN.
:::

::: atencao
Nota adicional (não estava explícito nos slides): a proposição só fala de
fórmulas com $\land,\lor,\neg$. Se a fórmula tiver $\to$ (ou $\leftrightarrow$),
**elimina-os primeiro**: $\phi\to\psi \Leftrightarrow \neg\phi\lor\psi$ e
$\phi\leftrightarrow\psi \Leftrightarrow (\phi\to\psi)\land(\psi\to\phi)$. Só
depois se empurram as negações. Esquecer este passo é o erro mais comum ---
$\neg(p \to q)$ **não** é "$\neg p \to \neg q$"; é $p \land \neg q$ (ver
Exercício 1.6(a) na Aula 2).
:::

## Forma normal disjuntiva (FND)

::: {.definicao title="--- Forma normal disjuntiva"}
Uma fórmula está em **forma normal disjuntiva** se é uma **disjunção de
conjunções de literais**:
$$(\alpha_{11} \land \dots \land \alpha_{1k_1}) \lor \dots \lor (\alpha_{n1} \land \dots \land \alpha_{nk_n})$$
onde cada $\alpha_{ij}$ é um literal. ("Um *ou* de *e*'s".)

Exemplos: $p \land q$ (uma só conjunção); $p \lor \neg p$ (duas conjunções,
cada uma com um só literal); $(p \land q \land \neg r) \lor (\neg p \land r)$.
:::

Há duas formas de obter uma FND: **a partir da tabela de verdade** (lema
seguinte) ou **a partir da fórmula**, por equivalências.

### FND a partir da tabela de verdade

::: {.definicao title="--- Lema (toda a função de verdade tem uma FND)"}
Para qualquer função $f : \{V,F\}^n \to \{V,F\}$ existe uma fórmula $\phi$ em
FND, com $n$ variáveis, tal que $F_\phi = f$.

**Prova (construtiva --- é o próprio método):**

- Se $f$ dá $F$ em todas as linhas, toma-se $\phi = p_1 \land \neg p_1$
  (sempre falsa).
- Senão, para cada linha (valoração) $v$ da tabela, define-se o literal
  $l_i^v = p_i$ se $v(p_i)=V$ e $l_i^v = \neg p_i$ se $v(p_i)=F$, e a
  conjunção $\phi_v = l_1^v \land \dots \land l_n^v$.
- **Porquê isto funciona:** cada $l_i^v$ é, por construção, verdadeiro em
  $v$, logo $v(\phi_v) = V$. E em qualquer **outra** linha $v'$, pelo menos
  uma variável tem valor diferente, o literal correspondente é falso, e
  $\phi_v$ é falsa. Ou seja: **$\phi_v$ é verdadeira exatamente na linha $v$
  e em mais nenhuma.**
- Toma-se $\phi = \bigvee_{f(v)=V} \phi_v$: a disjunção das $\phi_v$ das
  linhas em que $f$ dá $V$. Então $\phi$ é verdadeira exatamente nessas
  linhas --- ou seja, $F_\phi = f$.
:::

::: {.exemplo title="--- FND a partir de uma tabela (slides)"}
| linha | $x_1$ | $x_2$ | $x_3$ | $f$ | conjunção $\phi_v$ (só para as linhas com $V$) |
|---|---|---|---|---|---|
| 1 | V | V | V | V | $p_1 \land p_2 \land p_3$ |
| 2 | V | V | F | V | $p_1 \land p_2 \land \neg p_3$ |
| 3 | V | F | V | V | $p_1 \land \neg p_2 \land p_3$ |
| 4 | V | F | F | F | --- |
| 5 | F | V | V | V | $\neg p_1 \land p_2 \land p_3$ |
| 6 | F | V | F | F | --- |
| 7 | F | F | V | F | --- |
| 8 | F | F | F | F | --- |

Regra para escrever cada conjunção: variável a $V$ na linha → entra
**positiva**; variável a $F$ → entra **negada**. Ex.: linha 3 tem
$x_1=V, x_2=F, x_3=V$, logo $p_1 \land \neg p_2 \land p_3$.

Juntando com $\lor$ as 4 conjunções das linhas com $V$:
$$(p_1 \land p_2 \land p_3) \lor (p_1 \land p_2 \land \neg p_3) \lor (p_1 \land \neg p_2 \land p_3) \lor (\neg p_1 \land p_2 \land p_3)$$

(Repara: $f$ é a função "maioria" --- é $V$ quando pelo menos duas das três
variáveis são $V$.)
:::

::: atencao
Este lema é **outra prova** de que $\{\land,\lor,\neg\}$ é um conjunto
completo de conectivos (Aula 2, "Conjuntos completos de conectivos"): a
fórmula construída só usa $\land$, $\lor$ e $\neg$ e realiza qualquer $f$.
Lá a prova era por indução no número de variáveis; aqui é direta, linha a
linha. Ambas chegam ao mesmo resultado.
:::

### FND a partir de uma fórmula

::: {.definicao title="--- Corolário (toda a fórmula tem uma FND equivalente)"}
Qualquer fórmula é semanticamente equivalente a uma fórmula em FND. Para a
obter:

1. eliminar $\to$ e $\leftrightarrow$, ficando só com $\land$, $\lor$, $\neg$;
2. passar para **forma normal negativa** (De Morgan + dupla negação);
3. aplicar a **distributividade do $\land$ sobre o $\lor$** até não haver
   nenhum $\lor$ dentro de um $\land$:
   $$(\phi \lor \psi) \land \theta \Leftrightarrow (\phi \land \theta) \lor (\psi \land \theta)
   \qquad \theta \land (\phi \lor \psi) \Leftrightarrow (\theta \land \phi) \lor (\theta \land \psi)$$
:::

::: {.exemplo title="--- FND de $(p \\lor r) \\leftrightarrow (q \\land \\neg p)$, parte 1: passos 1 e 2 (slides)"}
**Passo 1 --- eliminar $\leftrightarrow$ e $\to$:**
$$\begin{aligned}
&(p \lor r) \leftrightarrow (q \land \neg p) \\
\Leftrightarrow\ & \big((p \lor r) \to (q \land \neg p)\big) \land \big((q \land \neg p) \to (p \lor r)\big) && (\leftrightarrow \text{ como duas implicações})\\
\Leftrightarrow\ & \big(\neg(p \lor r) \lor (q \land \neg p)\big) \land \big(\neg(q \land \neg p) \lor (p \lor r)\big) && (\text{implicação, 2 vezes})
\end{aligned}$$

**Passo 2 --- forma normal negativa.** No lado esquerdo,
$\neg(p\lor r) \Leftrightarrow \neg p \land \neg r$ (De Morgan). No lado direito,
$\neg(q \land \neg p) \Leftrightarrow \neg q \lor \neg\neg p \Leftrightarrow \neg q \lor p$
(De Morgan + dupla negação). Fica:
$$\underbrace{\big((\neg p \land \neg r) \lor (q \land \neg p)\big)}_{X} \land \underbrace{\big((\neg q \lor p) \lor (p \lor r)\big)}_{A \,\lor\, B}$$
com $A = \neg q \lor p$ e $B = p \lor r$. Isto já está em FNN, mas **não** em
FND: há $\lor$ dentro do $\land$ principal.
:::

::: {.exemplo title="--- FND de $(p \\lor r) \\leftrightarrow (q \\land \\neg p)$, parte 2: distributividade (slides)"}
**Passo 3a** --- $X \land (A \lor B) \Leftrightarrow (X \land A) \lor (X \land B)$:
$$\big(((\neg p \land \neg r) \lor (q \land \neg p)) \land A\big) \lor \big(((\neg p \land \neg r) \lor (q \land \neg p)) \land B\big)$$

**Passo 3b** --- em cada um dos dois blocos, $X = C_1 \lor C_2$ (com
$C_1 = \neg p \land \neg r$, $C_2 = q \land \neg p$) volta a distribuir:
$(C_1 \lor C_2) \land A \Leftrightarrow (C_1 \land A) \lor (C_2 \land A)$, e o
mesmo com $B$:
$$(\neg p \land \neg r \land (\neg q \lor p)) \lor (q \land \neg p \land (\neg q \lor p)) \lor (\neg p \land \neg r \land (p \lor r)) \lor (q \land \neg p \land (p \lor r))$$

**Passo 3c** --- cada um dos 4 termos ainda tem um $\lor$ lá dentro;
distribui-se cada um ($K \land (a \lor b) \Leftrightarrow (K \land a) \lor (K \land b)$):

- **Termo 1** --- $K = \neg p \land \neg r$, $(a \lor b) = \neg q \lor p$:
  $(\neg p \land \neg r \land \neg q) \lor (\neg p \land \neg r \land p)$
- **Termo 2** --- $K = q \land \neg p$, $(a \lor b) = \neg q \lor p$:
  $(q \land \neg p \land \neg q) \lor (q \land \neg p \land p)$
- **Termo 3** --- $K = \neg p \land \neg r$, $(a \lor b) = p \lor r$:
  $(\neg p \land \neg r \land p) \lor (\neg p \land \neg r \land r)$
- **Termo 4** --- $K = q \land \neg p$, $(a \lor b) = p \lor r$:
  $(q \land \neg p \land p) \lor (q \land \neg p \land r)$

A FND é a disjunção destas 8 conjunções:
$$(\neg p \land \neg r \land \neg q) \lor (\neg p \land \neg r \land p) \lor (q \land \neg p \land \neg q) \lor (q \land \neg p \land p) \lor (\neg p \land \neg r \land p) \lor (\neg p \land \neg r \land r) \lor (q \land \neg p \land p) \lor (q \land \neg p \land r)$$
:::

## Satisfazibilidade de uma FND

::: {.definicao title="--- Lema e corolário"}
**Lema.** Uma conjunção de literais $l_1 \land \dots \land l_n$ é
satisfazível **sse** não contém um par complementar, isto é, para todos os
$i,j$, $l_i$ não é $\neg l_j$. (Se não há par $p$/$\neg p$, basta pôr cada
literal positivo a $V$ e cada negativo a $F$ --- não há conflito. Se há
$p$ e $\neg p$, nunca podem ser ambos verdadeiros.)

**Corolário.** Uma fórmula em FND é satisfazível **sse alguma** das suas
conjunções é satisfazível (uma disjunção é verdadeira se **um** dos termos
for).
:::

::: exemplo
- $p \land \neg q \land \neg r \land q$: contém $\neg q$ e $q$ → **não** é
  satisfazível.
- $\neg p \land q \land \neg r \land \neg s$: nenhum par complementar → **é**
  satisfazível (com $p=F$, $q=V$, $r=F$, $s=F$).
:::

::: {.exemplo title="--- $(p \\lor r) \\leftrightarrow (q \\land \\neg p)$ é satisfazível? (slides)"}
Usa-se a FND obtida acima e verifica-se **cada** uma das 8 conjunções:

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

Há (pelo menos) uma conjunção satisfazível → a fórmula **é satisfazível**. A
conjunção 1 dá a valoração $p=q=r=F$; a 8 dá $p=F$, $q=r=V$.

Como as conjunções insatisfazíveis são sempre falsas, podem ser **apagadas**
da disjunção sem mudar nada ($\phi \lor F \Leftrightarrow \phi$), e fica a FND
simplificada:
$$(p \lor r) \leftrightarrow (q \land \neg p) \;\Leftrightarrow\; (\neg p \land \neg q \land \neg r) \lor (\neg p \land q \land r)$$

**Verificação direta** (para confirmar que não houve engano): se $p=V$, o
lado esquerdo $p \lor r$ é $V$ e o direito $q \land \neg p$ é $F$ → a
equivalência é $F$. Se $p=F$, fica $r \leftrightarrow q$, que é $V$ só para
$q=r=F$ ou $q=r=V$. São exatamente as duas conjunções que sobraram. $\checkmark$
:::

::: atencao
Nota adicional (dos apontamentos da Prof.ª Nelma Moreira, em `Teoricas/`):
se a fórmula **já está** em FND, este teste é **linear** no tamanho da
fórmula --- muito melhor do que os $2^n$ da tabela de verdade. Mas
**atenção**: *obter* a FND pode ser caro --- cada distributividade duplica
parte da fórmula (o exemplo acima passou de uma fórmula pequena para 8
conjunções), e no pior caso a FND tem tamanho exponencial. Não se conhece
nenhum algoritmo polinomial para a satisfazibilidade de uma fórmula
qualquer (problema **SAT**); encontrar um responderia à pergunta
"P = NP?". O que há são classes de fórmulas em que o problema é fácil (FND,
Horn) e algoritmos que na prática funcionam bem para fórmulas em FNC.
:::

## Forma normal conjuntiva (FNC)

::: {.definicao title="--- Forma normal conjuntiva"}
Uma fórmula está em **forma normal conjuntiva** se é uma **conjunção de
disjunções de literais** ("um *e* de *ou*'s"):
$$(\alpha_{11} \lor \dots \lor \alpha_{1k_1}) \land \dots \land (\alpha_{n1} \lor \dots \lor \alpha_{nk_n})$$
Cada disjunção de literais chama-se uma **cláusula**.
:::

::: {.definicao title="--- Lema dual (tautologia de uma FNC)"}
Por **dualidade** com o lema da FND: uma disjunção de literais
$l_1 \lor \dots \lor l_n$ é **tautologia sse contém um par complementar**
(algum $l_i$ é $\neg l_j$: se tem $p \lor \neg p$ lá dentro, é sempre
verdadeira; se não tem, pondo cada literal a $F$ ela falha).

Logo, uma fórmula em FNC é **tautologia sse todas as suas cláusulas são
tautologias** (uma conjunção é sempre verdadeira sse cada termo é sempre
verdadeiro).
:::

::: exame
Guarda a **simetria**: FND serve para decidir **satisfazibilidade** (basta
**uma** conjunção sem par complementar); FNC serve para decidir se é
**tautologia** (**todas** as cláusulas têm de ter um par complementar). O
contrário **não** é fácil: decidir se uma FNC é satisfazível é exatamente o
problema SAT difícil.
:::

Duas formas de obter uma FNC --- as mesmas duas da FND, "ao contrário":

1. **A partir da tabela de verdade**, pelo método dual: escolher as linhas
   em que $f$ dá **F**; para cada uma, formar a **disjunção** em que a
   variável entra **negada se está a $V$** nessa linha e **positiva se está
   a $F$**; tomar a **conjunção** dessas disjunções.
2. **A partir da fórmula**: passos 1 e 2 iguais aos da FND, mas no passo 3 usa-se
   a distributividade do **$\lor$ sobre o $\land$**:
   $$(\phi \land \psi) \lor \theta \Leftrightarrow (\phi \lor \theta) \land (\psi \lor \theta)
   \qquad \theta \lor (\phi \land \psi) \Leftrightarrow (\theta \lor \phi) \land (\theta \lor \psi)$$

::: {.exemplo title="--- FNC a partir de uma tabela (slides; a mesma função da FND acima)"}
Agora interessam as linhas com **F** (4, 6, 7, 8). Para cada uma, a
cláusula é construída para ser **falsa exatamente nessa linha**: cada
literal tem de ser $F$ ali, por isso variável a $V$ → entra **negada**,
variável a $F$ → entra **positiva**.

| linha | $x_1$ | $x_2$ | $x_3$ | $f$ | cláusula |
|---|---|---|---|---|---|
| 4 | V | F | F | F | $\neg p_1 \lor p_2 \lor p_3$ |
| 6 | F | V | F | F | $p_1 \lor \neg p_2 \lor p_3$ |
| 7 | F | F | V | F | $p_1 \lor p_2 \lor \neg p_3$ |
| 8 | F | F | F | F | $p_1 \lor p_2 \lor p_3$ |

Verificação da linha 4: com $x_1=V, x_2=F, x_3=F$, $\neg p_1 \lor p_2 \lor p_3 = F \lor F \lor F = F$;
e em qualquer outra linha pelo menos um literal é $V$. A conjunção das 4
cláusulas é $F$ exatamente nas linhas 4, 6, 7, 8 --- ou seja, realiza $f$:
$$(\neg p_1 \lor p_2 \lor p_3) \land (p_1 \lor \neg p_2 \lor p_3) \land (p_1 \lor p_2 \lor \neg p_3) \land (p_1 \lor p_2 \lor p_3)$$
:::

::: {.exemplo title="--- FNC de $(p \\lor r) \\leftrightarrow (q \\land \\neg p)$ e é tautologia? (slides)"}
Os passos 1 e 2 são **exatamente** os da FND (ver acima), e dão:
$$\big((\neg p \land \neg r) \lor (q \land \neg p)\big) \land \big((\neg q \lor p) \lor (p \lor r)\big)$$

O lado direito já é uma cláusula: $\neg q \lor p \lor p \lor r$
(associatividade). Falta o lado esquerdo, que é um $\lor$ de $\land$'s.

**Passo 3a** --- distribuir com $\theta = \neg p \land \neg r$, $\phi = q$,
$\psi = \neg p$, usando $\theta \lor (\phi \land \psi) \Leftrightarrow (\theta \lor \phi) \land (\theta \lor \psi)$:
$$(\neg p \land \neg r) \lor (q \land \neg p) \Leftrightarrow \big((\neg p \land \neg r) \lor q\big) \land \big((\neg p \land \neg r) \lor \neg p\big)$$

**Passo 3b** --- cada bloco ainda tem um $\land$ dentro de um $\lor$;
distribui-se outra vez ($(a \land b) \lor c \Leftrightarrow (a \lor c) \land (b \lor c)$):

- $(\neg p \land \neg r) \lor q \Leftrightarrow (\neg p \lor q) \land (\neg r \lor q)$
- $(\neg p \land \neg r) \lor \neg p \Leftrightarrow (\neg p \lor \neg p) \land (\neg r \lor \neg p)$

**FNC final** (5 cláusulas):
$$(\neg p \lor q) \land (\neg r \lor q) \land (\neg p \lor \neg p) \land (\neg r \lor \neg p) \land (\neg q \lor p \lor p \lor r)$$

**É tautologia?** Verifica-se cada cláusula: $\neg p \lor q$ não tem par
complementar → já não é tautologia, e a fórmula também **não** é
(resposta dos slides: **Não**). Contraexemplo tirado da própria cláusula
(pôr os seus literais a $F$): $p=V$, $q=F$ --- de facto, com $p=V$ o lado
$p \lor r$ é $V$ e $q \land \neg p$ é $F$, logo a equivalência é $F$. $\checkmark$
:::

::: atencao
Para "limpar" uma FND/FNC usam-se as leis extra da Aula 2
(complementaridade, elemento neutro/absorvente, absorção).
Na FNC acima, por exemplo: $\neg p \lor \neg p \Leftrightarrow \neg p$
(idempotência), e a cláusula $\neg r \lor \neg p$ é absorvida por $\neg p$.
Fica $(\neg p \lor q) \land (\neg r \lor q) \land \neg p \land (\neg q \lor p \lor r)$
--- com $p=F$ forçado, sobra $(\neg r \lor q) \land (\neg q \lor r)$, ou seja
$q \leftrightarrow r$: coerente com a verificação feita na FND. Uma FND/FNC
não é única; qualquer uma equivalente está certa.
:::

### Aplicação aos exercícios da prática: FND/FNC

::: {.exemplo title="--- Exercício 1.17(a) (lab, proplogic.pdf) --- FND e FNC a partir da tabela"}
A função (a) tem esta coluna (na ordem de linhas do enunciado, $p,q,r$ de
$VVV$ até $FFF$): $V, V, V, V, F, V, V, V$. Só **uma** linha dá $F$: a linha
$p=F, q=V, r=V$.

**FNC** (uma cláusula por linha com $F$ --- só há uma): na linha
$p=F,q=V,r=V$, $p$ está a $F$ → entra positivo; $q$ e $r$ estão a $V$ →
entram negados:
$$p \lor \neg q \lor \neg r$$

**FND** (uma conjunção por linha com $V$ --- há sete):

| $p$ | $q$ | $r$ | conjunção |
|---|---|---|---|
| V | V | V | $p \land q \land r$ |
| V | V | F | $p \land q \land \neg r$ |
| V | F | V | $p \land \neg q \land r$ |
| V | F | F | $p \land \neg q \land \neg r$ |
| F | V | F | $\neg p \land q \land \neg r$ |
| F | F | V | $\neg p \land \neg q \land r$ |
| F | F | F | $\neg p \land \neg q \land \neg r$ |

$$(p \land q \land r) \lor (p \land q \land \neg r) \lor (p \land \neg q \land r) \lor (p \land \neg q \land \neg r) \lor (\neg p \land q \land \neg r) \lor (\neg p \land \neg q \land r) \lor (\neg p \land \neg q \land \neg r)$$

**Lição:** quando a tabela tem **poucos $F$**, a FNC sai muito mais curta;
quando tem **poucos $V$**, é a FND. Ambas estão certas --- as duas
representam a mesma função (confirma: a FNC só falha em $p=F,q=V,r=V$, que é
a única linha que falta na FND). Também se podia simplificar a FND de 7
termos, mas não é pedido.
:::

::: {.exemplo title="--- Exercício 1.18(d) (lab, proplogic.pdf) --- FND e FNC de $(p \\to q) \\to (\\neg p \\to \\neg q)$"}
$$\begin{aligned}
&(p \to q) \to (\neg p \to \neg q) \\
\Leftrightarrow\ & \neg(p \to q) \lor (\neg p \to \neg q) && \text{(implicação, na } \to \text{ exterior)}\\
\Leftrightarrow\ & \neg(\neg p \lor q) \lor (\neg\neg p \lor \neg q) && \text{(implicação, nas duas interiores)}\\
\Leftrightarrow\ & (\neg\neg p \land \neg q) \lor (\neg\neg p \lor \neg q) && \text{(De Morgan)}\\
\Leftrightarrow\ & (p \land \neg q) \lor p \lor \neg q && \text{(dupla negação, 2 vezes; associatividade)}
\end{aligned}$$

**FND:** $(p \land \neg q) \lor p \lor \neg q$ já é FND --- três conjunções:
$p \land \neg q$, $p$ (conjunção de um só literal), $\neg q$. Simplificando
por absorção ($p \lor (p \land \neg q) \Leftrightarrow p$):
$$p \lor \neg q$$

**FNC:** distribui-se o $\lor$ sobre o $\land$ em $(p \land \neg q) \lor (p \lor \neg q)$,
com $\theta = p \lor \neg q$:
$$(p \lor p \lor \neg q) \land (\neg q \lor p \lor \neg q) \Leftrightarrow (p \lor \neg q) \land (p \lor \neg q) \Leftrightarrow p \lor \neg q$$
(idempotência duas vezes). Repara que $p \lor \neg q$ é **ao mesmo tempo**
FND (duas conjunções de um literal) e FNC (uma cláusula) --- é normal com
fórmulas pequenas.

Não é tautologia (a cláusula não tem par complementar): com $p=F, q=V$,
$p \to q = V$ e $\neg p \to \neg q = V \to F = F$. (A alínea (k) do enunciado
é **igual** a esta.)
:::

::: {.exemplo title="--- Exercício 1.18(h) (lab, proplogic.pdf) --- FND e FNC de $(p \\to q) \\land (\\neg q \\to (p \\lor \\neg q))$"}
**Eliminar implicações:**
$p \to q \Leftrightarrow \neg p \lor q$; e
$\neg q \to (p \lor \neg q) \Leftrightarrow \neg\neg q \lor p \lor \neg q \Leftrightarrow q \lor p \lor \neg q$.
$$(\neg p \lor q) \land (q \lor p \lor \neg q)$$

**FNC:** isto **já é** uma FNC (conjunção de duas cláusulas). Repara que a
segunda cláusula contém $q$ e $\neg q$: é tautologia, logo vale sempre $V$
e pode sair ($\phi \land V \Leftrightarrow \phi$). FNC simplificada: $\neg p \lor q$.

**FND** (fazendo a distribuição toda, sem simplificar antes, para treinar):
$(\neg p \lor q) \land X$ com $X = q \lor p \lor \neg q$ distribui como
$(\neg p \land X) \lor (q \land X)$, e cada um distribui outra vez sobre os 3
literais de $X$:
$$(\neg p \land q) \lor (\neg p \land p) \lor (\neg p \land \neg q) \lor (q \land q) \lor (q \land p) \lor (q \land \neg q)$$
Apagam-se as conjunções com par complementar ($\neg p \land p$ e
$q \land \neg q$) e $q \land q \Leftrightarrow q$:
$$(\neg p \land q) \lor (\neg p \land \neg q) \lor q \lor (p \land q)$$
Isto é uma FND correta. Simplificando por absorção ($q$ absorve
$\neg p \land q$ e $p \land q$), sobra $(\neg p \land \neg q) \lor q$; e como
$(\neg p \land \neg q) \lor q \Leftrightarrow (\neg p \lor q) \land (\neg q \lor q) \Leftrightarrow \neg p \lor q$,
chega-se ao mesmo $\neg p \lor q$ da FNC --- que também é FND. $\checkmark$

**Lição:** detetar cedo uma cláusula-tautologia (ou uma conjunção
contraditória) poupa imenso trabalho de distribuição.
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
Uma **fórmula de Horn** é uma fórmula em **FNC** em que **cada cláusula tem
no máximo um literal positivo**.

Exemplos (dos slides), com o nº de literais positivos por cláusula:

- $p \land \neg q \land (q \lor \neg p)$: cláusulas $p$ (1), $\neg q$ (0),
  $q \lor \neg p$ (1) → Horn.
- $(\neg p \lor \neg q \lor \neg s \lor p) \land (\neg q \lor \neg r \lor p) \land (\neg p \lor \neg s \lor s)$:
  1, 1, 1 → Horn.
- $(\neg p \lor \neg q \lor \neg s) \land (\neg q \lor \neg r \lor p) \land s$:
  0, 1, 1 → Horn.

Contra-exemplo: $(p \lor q) \land \neg r$ **não** é Horn --- a cláusula
$p \lor q$ tem dois literais positivos.
:::

Cada cláusula de Horn pode ler-se como uma **implicação** (usando
$\neg a \lor b \Leftrightarrow a \to b$ e De Morgan
$\neg p_1 \lor \dots \lor \neg p_n \Leftrightarrow \neg(p_1 \land \dots \land p_n)$):

| forma da cláusula | lida como implicação | nome informal |
|---|---|---|
| $\neg p_1 \lor \dots \lor \neg p_n \lor p$ | $(p_1 \land \dots \land p_n) \to p$ | regra |
| $\neg p_1 \lor \dots \lor \neg p_n$ (sem positivo) | $(p_1 \land \dots \land p_n) \to F$ | restrição ("não podem ser todos $V$") |
| $p$ (sem negativos) | $V \to p$ | facto ($p$ tem de ser $V$) |

::: atencao
**Nem todas as fórmulas têm uma fórmula de Horn equivalente** --- basta que
a sua FNC tenha uma cláusula com mais de um literal positivo que não possa
ser simplificada (ex.: $p \lor q$). A vantagem das fórmulas de Horn é que a
sua satisfazibilidade decide-se com um **algoritmo eficiente** (linear/
polinomial), sem tabela de verdade.
:::

### Algoritmo de satisfazibilidade para fórmulas de Horn

A ideia: começar com todas as variáveis "desconhecidas" e só atribuir $V$ a
uma variável quando **for obrigatório** (quando, sem isso, uma cláusula
ficaria falsa). Se essas atribuições obrigatórias fizerem uma cláusula
ficar $F$, a fórmula é insatisfazível; senão, põem-se todas as restantes
variáveis a $F$ e está encontrada uma valoração que a satisfaz.

::: {.definicao title="--- Algoritmo (versão dos slides)"}
1. Escrever numa linha as variáveis e a fórmula (como numa linha de tabela
   de verdade, ainda vazia).
2. Se alguma **variável sozinha** é um dos elementos da conjunção (um
   **facto**, $V \to p$), atribuir-lhe $V$. **Porquê?** Porque uma
   conjunção só é $V$ se cada elemento for $V$; se $p$ é um elemento, tem de
   ser $p=V$ em qualquer valoração que satisfaça a fórmula.
3. Com os valores já conhecidos, avaliar cada cláusula. Se numa cláusula
   todos os literais negativos já estão a $F$ (as suas variáveis estão a
   $V$), então, para a cláusula ser $V$, o **literal positivo** tem de ser
   $V$ → atribuir $V$ a essa variável.
4. Repetir o passo 3 até nada mais poder ser acrescentado.
5. Se algum elemento da conjunção ficou com valor $F$, a fórmula é $F$ →
   **não satisfazível**. Caso contrário, é **satisfazível**: atribui-se $F$
   a todas as variáveis restantes e a fórmula fica $V$.
:::

::: {.exemplo title="--- $p \\land \\neg q \\land (q \\lor \\neg p)$ (slides)"}
Cláusulas: $C_1 = p$, $C_2 = \neg q$, $C_3 = q \lor \neg p$ (lida como
$p \to q$).

**Passo 1** --- linha vazia:

| $p$ | $q$ | $C_1 = p$ | $C_2 = \neg q$ | $C_3 = q \lor \neg p$ |
|---|---|---|---|---|
| | | | | |

**Passo 2** --- $p$ é um elemento da conjunção (facto) → $p = V$:

| $p$ | $q$ | $C_1 = p$ | $C_2 = \neg q$ | $C_3 = q \lor \neg p$ |
|---|---|---|---|---|
| V | | V | | ($\neg p = F$) |

**Passo 3** --- em $C_3$, o literal negativo $\neg p$ já é $F$; para $C_3$
ser $V$, o positivo $q$ tem de ser $V$ → $q = V$:

| $p$ | $q$ | $C_1 = p$ | $C_2 = \neg q$ | $C_3 = q \lor \neg p$ |
|---|---|---|---|---|
| V | V | V | | V |

**Passo 4** --- repete-se: agora $C_2 = \neg q$ com $q = V$ dá $F$:

| $p$ | $q$ | $C_1 = p$ | $C_2 = \neg q$ | $C_3 = q \lor \neg p$ |
|---|---|---|---|---|
| V | V | V | **F** | V |

**Passo 5** --- um elemento da conjunção ($C_2$) ficou $F$ → a fórmula é
$F$ → **não é satisfazível**. (Não há escolha possível: $p=V$ e $q=V$
foram ambos **obrigatórios**.)
:::

::: atencao
Nota adicional --- **porque é que o algoritmo está correto** (é o
Exercício 1.21(b) do lab; nos slides fica só o "porquê?"):

- **Se diz "insatisfazível", está certo:** cada $V$ atribuído foi
  *obrigatório* --- qualquer valoração que satisfaça a fórmula tem de o ter.
  Se as atribuições obrigatórias já tornam uma cláusula $F$, nenhuma
  valoração satisfaz a fórmula.
- **Se diz "satisfazível", está certo:** com as marcadas a $V$ e as outras a
  $F$, pega-se numa cláusula qualquer. (i) Se o seu literal positivo está
  marcado, ela é $V$. (ii) Senão, algum dos seus literais negativos $\neg x$
  tem $x$ **não** marcado (se todos estivessem marcados, o passo 3 teria
  obrigado a marcar o positivo, ou --- se não houver positivo --- a cláusula
  seria $F$ e o algoritmo teria parado no passo 5); logo $x = F$ e
  $\neg x = V$, e a cláusula é $V$.

É exatamente aqui que se usa "no máximo um literal positivo": pôr as
restantes a $F$ torna verdadeiros **todos** os literais negativos por
decidir, e nunca é preciso "escolher" entre dois positivos. Por isso nunca
há retrocesso (*backtracking*) e o algoritmo é eficiente.
:::

::: {.exemplo title="--- O mesmo algoritmo em pseudo-código (base para o Exercício 1.21(a))"}
Vendo cada cláusula como implicação $(p_1 \land \dots \land p_n) \to h$, com
$h$ uma variável ou $F$ (e $n = 0$ para factos):

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

Cada iteração do `repetir` marca pelo menos uma variável nova (ou pára),
por isso há no máximo (nº de variáveis + 1) iterações --- polinomial.
:::

::: {.exemplo title="--- Exercício 1.21(c), 1.ª e 2.ª fórmulas (lab, proplogic.pdf)"}
**(i) $(\neg p \lor \neg q) \land (\neg q \lor r) \land q$.** Como
implicações: $(p \land q) \to F$, $q \to r$, $V \to q$.

- Facto $q$ → $q = V$.
- $q \to r$: antecedente $q$ marcado → $r = V$.
- $(p \land q) \to F$: antecedente precisa de $p$ **e** $q$; $p$ não está
  marcado → não dispara.
- Nova volta: nada muda. Nenhuma cláusula ficou $F$.

**Satisfazível**, com $q = V$, $r = V$ e a restante $p = F$. Verificação:
$\neg p \lor \neg q = V \lor F = V$; $\neg q \lor r = F \lor V = V$; $q = V$. $\checkmark$

**(ii) $p \land (\neg p \lor q) \land (\neg q \lor p)$.** Como implicações:
$V \to p$, $p \to q$, $q \to p$.

- Facto $p$ → $p = V$.
- $p \to q$: $p$ marcado → $q = V$.
- $q \to p$: $q$ marcado, mas $p$ já estava marcado → nada novo.
- Nova volta: nada muda; nenhuma cláusula ficou $F$.

**Satisfazível**, com $p = q = V$ (não sobram variáveis para pôr a $F$).
Verificação: $p = V$; $\neg p \lor q = F \lor V = V$; $\neg q \lor p = F \lor V = V$. $\checkmark$
:::

::: {.pratica title="--- Horn (proplogic.pdf)"}
- **1.21 (c)**, 3.ª e 4.ª fórmulas: $\neg p \land (\neg p \lor q) \land \neg q$
  (o que acontece quando **não há nenhum facto**?) e
  $p \land (\neg p \lor q) \land \neg r$.
- **1.21 (a)** --- implementar o algoritmo a partir do pseudo-código acima.
:::

Os exercícios **1.22 e 1.23** (algoritmo de Davis-Putnam/DPLL) ficam fora
do resumo até serem dados nas teóricas.
