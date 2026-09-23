---
title: "Lógica Computacional --- Soluções dos exercícios \"Pratica agora\""
subtitle: "Exercícios de Praticas/Semana_1/proplogic.pdf sugeridos no resumo. Tenta primeiro sozinho; abre uma alínea só depois de a teres feito."
---

## Aula 1 --- Linguagem e árvores sintáticas

### 1.2 --- Traduzir para linguagem natural

$p$ = "Jogo na lotaria", $q$ = "Ganho o jackpot".

#### (a) $\neg p$

"**Não** jogo na lotaria."

#### (b) $p \land q$

"Jogo na lotaria **e** ganho o jackpot."

#### (c) $\neg p \lor \neg q$

"Não jogo na lotaria **ou** não ganho o jackpot."

(Pela Lei de De Morgan é o mesmo que $\neg(p\land q)$: "não é verdade que
jogue e ganhe".)

#### (d) $p \to q$

"**Se** jogo na lotaria, **então** ganho o jackpot."

#### (e) $q \to p$

"**Se** ganho o jackpot, **então** jogo na lotaria." Dito de forma mais
natural: "**só** ganho o jackpot **se** jogar na lotaria".

Repara que **não** é o mesmo que a (d): a (d) promete o prémio a quem
joga; a (e) só diz que jogar é **necessário** para ganhar.

#### (f) $\neg p \to \neg q$

"Se **não** jogo na lotaria, então **não** ganho o jackpot."

É a **contrarrecíproca** da (e): $\neg p \to \neg q \Leftrightarrow q \to
p$. As frases (e) e (f) dizem a mesma coisa por palavras diferentes; a (d)
é que é diferente.

### 1.3 --- Árvores sintáticas e subfórmulas

#### (b) $p \land (\neg q \to \neg p)$

**Passo 1 --- parêntesis.** Os parêntesis explícitos mandam: o $\to$ fica
**dentro** deles, por isso o conectivo principal (a raiz) é o $\land$.
Compara com a 1.3(a) resolvida no resumo, $p \land \neg q \to \neg p$, em
que a raiz era o $\to$: só os parêntesis mudaram.

**Passo 2 --- árvore:**

![Árvore de p ∧ (¬q → ¬p)](figuras/sol_arvore_1_3b.svg){width=220px}

**Passo 3 --- subfórmulas** (um nó da árvore = uma subfórmula):
$p \land (\neg q \to \neg p)$, $p$, $\neg q \to \neg p$, $\neg q$, $q$,
$\neg p$.

O $p$ aparece duas vezes na árvore mas é a mesma fórmula, por isso só se
lista uma vez. São **6** subfórmulas.

#### (d) $p \to (\neg q \lor (q \to p))$

**Passo 1 --- parêntesis.** A raiz é o primeiro $\to$, porque tudo o resto
está dentro de parêntesis. Dentro do parêntesis, o conectivo principal é o
$\lor$, que junta $\neg q$ e $(q\to p)$.

**Passo 2 --- árvore:**

![Árvore de p → (¬q ∨ (q → p))](figuras/sol_arvore_1_3d.svg){width=240px}

**Passo 3 --- subfórmulas:**
$p \to (\neg q \lor (q \to p))$, $p$, $\neg q \lor (q \to p)$, $\neg q$,
$q$, $q \to p$.

$p$ e $q$ aparecem duas vezes cada na árvore e só se listam uma vez. São
**6** subfórmulas.

### 1.4 --- Tabelas de verdade

#### (a) $p \to p$

| $p$ | $p \to p$ |
|:-:|:-:|
| V | V |
| F | V |

Verdadeira em todas as linhas: é uma **tautologia**. Quando $p=F$, a
implicação tem o antecedente falso, e por isso é verdadeira.

#### (d) $\neg(p \lor q) \to (\neg p \land \neg q)$

| $p$ | $q$ | $p\lor q$ | $\neg(p\lor q)$ | $\neg p$ | $\neg q$ | $\neg p\land\neg q$ | fórmula |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| V | V | V | F | F | F | F | **V** |
| V | F | V | F | F | V | F | **V** |
| F | V | V | F | V | F | F | **V** |
| F | F | F | V | V | V | V | **V** |

**Tautologia.** Nas três primeiras linhas o antecedente $\neg(p\lor q)$ é
falso, por isso a implicação é logo verdadeira. Só a última linha decide
alguma coisa, e aí $V \to V = V$.

Não é coincidência: $\neg(p\lor q)$ e $\neg p\land\neg q$ são equivalentes
(Lei de De Morgan). Uma fórmula implica sempre outra que lhe é equivalente.

### 1.9 --- Classificar fórmulas

#### (c) $(p \to q) \to (\neg p \to \neg q)$

| $p$ | $q$ | $p\to q$ | $\neg p \to \neg q$ | fórmula |
|:-:|:-:|:-:|:-:|:-:|
| V | V | V | $F\to F = V$ | **V** |
| V | F | F | $F \to V = V$ | **V** |
| F | V | V | $V \to F = F$ | **F** |
| F | F | V | $V \to V = V$ | **V** |

**Satisfazível, mas não é tautologia.**

- Torna-a **verdadeira**: $p=V, q=V$.
- Torna-a **falsa**: $p=F, q=V$ (a única linha que a torna falsa).

Moral: de "se $p$ então $q$" **não** se segue "se não $p$ então não $q$".
É o erro clássico de negar o antecedente.

#### (h) $(p \to q) \land (\neg r \to (q \lor (\neg p \land r)))$

**Simplificar primeiro** com as equivalências (é o que o enunciado sugere):

- $p \to q \;\Leftrightarrow\; \neg p \lor q$
- $\neg r \to X \;\Leftrightarrow\; r \lor X$. Aqui fica
  $r \lor q \lor (\neg p \land r)$.
- **Absorção:** $r \lor (\neg p \land r) \Leftrightarrow r$. Se $r$ for
  verdadeiro já basta; se for falso, $\neg p \land r$ também é falso. Fica
  $q \lor r$.

Logo a fórmula é equivalente a $(\neg p \lor q) \land (q \lor r)$.

- **Verdadeira**, por exemplo, com $q = V$ (os dois parêntesis ficam
  verdadeiros, seja qual for $p$ e $r$): $p=V,q=V,r=V$.
- **Falsa**, por exemplo, com $p=V, q=F$ (o primeiro parêntesis
  $\neg p\lor q$ fica $F \lor F = F$): $p=V,q=F,r=V$.

**Satisfazível, mas não é tautologia nem contradição.**

Verificação na fórmula original, com $p=V,q=F,r=V$: $p\to q = V \to F =
F$, e a conjunção fica logo $F$ $\checkmark$.

## Aula 2 --- Consequência, equivalência, modelação

### 1.5 --- A relação $\models_v$, com $v(p)=V$ e $v(q)=F$

#### (a) $(p \lor q) \to (p \land q)$

- $p \lor q = V \lor F = V$
- $p \land q = V \land F = F$
- $V \to F = F$

$\not\models_v$: **não** satisfaz.

#### (c) $(p \to q) \land (p \to \neg q)$

- $p \to q = V \to F = F$

A conjunção já é falsa, não é preciso calcular o outro lado. $\not\models_v$:
**não** satisfaz.

(Por curiosidade: $p \to \neg q = V \to V = V$, mas não chega.)

#### (d) $p \to (q \to (p \lor q))$

- de dentro para fora: $p \lor q = V$
- $q \to V = F \to V = V$
- $p \to V = V \to V = V$

$\models_v$: **satisfaz**. Na verdade é uma tautologia: a fórmula só
podia ser falsa com $p = V$ e $q = V$ (para os dois $\to$ terem o
antecedente verdadeiro), mas então $p \lor q = V$ e o último $\to$ também
é verdadeiro.

### 1.6 --- Provar equivalências pelas leis

#### (b) $\neg p \to q \;\Leftrightarrow\; \neg q \to p$

Usa $A \to B \Leftrightarrow \neg A \lor B$ nos dois lados:

- esquerda: $\neg p \to q \Leftrightarrow \neg\neg p \lor q
  \Leftrightarrow p \lor q$ (dupla negação)
- direita: $\neg q \to p \Leftrightarrow \neg\neg q \lor p
  \Leftrightarrow q \lor p$

Pela **comutatividade** do $\lor$, $p \lor q \Leftrightarrow q \lor p$. As
duas fórmulas são equivalentes. $\checkmark$

#### (c) $p \to (q \to r) \;\Leftrightarrow\; q \to (p \to r)$

- esquerda: $p \to (q \to r) \Leftrightarrow \neg p \lor (\neg q \lor r)$
- direita: $q \to (p \to r) \Leftrightarrow \neg q \lor (\neg p \lor r)$

Pela **associatividade** e **comutatividade** do $\lor$, as duas ficam
$\neg p \lor \neg q \lor r$. $\checkmark$

(Intuição: "se $p$, então se $q$ então $r$" é o mesmo que "se $p$ e $q$,
então $r$", e a ordem de $p$ e $q$ não importa.)

#### (d) $(p \to q) \to p \;\Leftrightarrow\; p$

$$
\begin{aligned}
(p \to q) \to p
&\Leftrightarrow \neg(\neg p \lor q) \lor p && \text{(eliminar os dois } \to\text{)}\\
&\Leftrightarrow (\neg\neg p \land \neg q) \lor p && \text{(De Morgan)}\\
&\Leftrightarrow (p \land \neg q) \lor p && \text{(dupla negação)}\\
&\Leftrightarrow p && \text{(absorção: } (p\land X)\lor p \Leftrightarrow p\text{)}
\end{aligned}
$$

$\checkmark$ (Este resultado reaparece na Lei de Peirce, exercício 1.18(e).)

### 1.8 --- Validade

#### (c) $(p \land q) \lor r \;\Leftrightarrow\; (p \lor r) \land (q \lor r)$

**Válida.** É a **distributividade do $\lor$ sobre o $\land$**:
$$(p \land q) \lor r \Leftrightarrow (p \lor r) \land (q \lor r)$$

Confirmação por casos:

- se $r = V$: os dois lados ficam $V$.
- se $r = F$: a esquerda fica $p \land q$ e a direita fica
  $(p \lor F) \land (q \lor F) = p \land q$.

São iguais em todos os casos. $\checkmark$

Ao contrário da 1.8(b), aqui distribuir funciona. A diferença é que a 1.8(b)
distribuía uma implicação sobre o seu **antecedente**, e isso troca o
conectivo.

### 1.15 --- Propriedades de $\models$

#### (a) $\models (\theta \lor \varphi) \to (\neg\theta \to \varphi)$

**Verdadeira.** Pela eliminação da implicação,
$\neg\theta \to \varphi \Leftrightarrow \neg\neg\theta \lor \varphi
\Leftrightarrow \theta \lor \varphi$. A fórmula é então da forma
$X \to X$, com $X = \theta \lor\varphi$.

Para qualquer valoração $v$: se $v(X) = V$, fica $V \to V = V$; se
$v(X)=F$, fica $F \to F = V$. É verdadeira em todas as valorações, logo é
**tautologia**.

#### (b) $\{\varphi \to \psi,\ \psi \to \varphi\} \models (\varphi \lor \psi) \to (\varphi \land \psi)$

**Verdadeira.** Seja $v$ uma valoração que satisfaz as duas premissas.
Então $v(\varphi) = v(\psi)$: se um fosse $V$ e o outro $F$, uma das
implicações seria $V \to F$.

- Se $v(\varphi) = v(\psi) = V$: a conclusão é $V \to V = V$.
- Se $v(\varphi) = v(\psi) = F$: o antecedente $\varphi\lor\psi$ é $F$, logo
  a conclusão é $V$.

Em qualquer caso, $v$ satisfaz a conclusão. $\checkmark$

#### (c) $\{\psi \to (\neg\varphi \lor \gamma),\ \neg\gamma\} \models \neg\varphi \to \neg\psi$

**Falsa.** Um contraexemplo tem de pôr as premissas verdadeiras e a
conclusão falsa.

- Conclusão falsa: $\neg\varphi \to \neg\psi = V \to F$, ou seja
  $\varphi = F$ e $\psi = V$.
- $\neg\gamma$ verdadeira: $\gamma = F$.
- Verificar a 1.ª premissa: $\psi \to (\neg\varphi \lor \gamma) = V \to
  (V \lor F) = V \to V = V$ $\checkmark$.

**Contraexemplo concreto:** $\varphi = p$, $\psi = q$, $\gamma = r$, com
$v(p)=F$, $v(q)=V$, $v(r)=F$. As premissas são verdadeiras e a conclusão é
falsa.

#### (d) Se $\varphi, \psi \models \theta \to \gamma$ e $\varphi \models \theta$, então $\varphi, \psi \models \gamma$

**Verdadeira.** Seja $v$ uma valoração que satisfaz $\varphi$ e $\psi$.

1. Pela 2.ª hipótese, $v$ satisfaz $\varphi$, logo $v(\theta) = V$.
2. Pela 1.ª hipótese, $v$ satisfaz $\varphi$ e $\psi$, logo
   $v(\theta \to \gamma) = V$.
3. Com $v(\theta) = V$ e $v(\theta\to\gamma) = V$, só pode ser
   $v(\gamma) = V$. Se fosse $F$, teríamos $V \to F = F$.

Logo toda a valoração que satisfaz $\{\varphi,\psi\}$ satisfaz $\gamma$.
$\checkmark$ (É o *modus ponens*, na versão semântica.)

### 1.10 --- Cavaleiros e vilões

#### (g) A diz: "B e C são do mesmo tipo." Pergunta-se a C: "A e B são do mesmo tipo?" O que respondeu C?

**Resposta: C disse "sim".**

Variáveis: $A$, $B$, $C$ = "é cavaleiro". A afirmação de A dá
$A \leftrightarrow (B \leftrightarrow C)$. Vê os quatro casos possíveis:

| A | B, C | A e B do mesmo tipo? | C é... | C responde |
|:-:|:-:|:-:|:-:|:-:|
| cav. | B = C = cav. | sim | cav. (diz a verdade) | **sim** |
| cav. | B = C = vil. | não | vil. (mente) | **sim** |
| vil. | B vil., C cav. | sim | cav. | **sim** |
| vil. | B cav., C vil. | não | vil. | **sim** |

Nas linhas em que A é vilão, B e C são de tipos diferentes, porque a frase
de A tem de ser falsa. Em todos os casos C responde "sim", mesmo sem se
saber o tipo de ninguém.

#### (j) Que pergunta de "sim/não" fazer para saber qual caminho leva à cidade?

**Pergunta:** *"O caminho da esquerda leva à cidade **se e só se** tu és
cavaleiro?"*

Seja $K$ = "o habitante é cavaleiro" e $E$ = "a esquerda leva à cidade". A
pergunta é $Q = K \leftrightarrow E$. O habitante responde "sim" se e só
se $K \leftrightarrow Q$: um cavaleiro diz "sim" quando $Q$ é verdade, um
vilão diz "sim" quando $Q$ é falsa. Então:

$$\text{"sim"} \Leftrightarrow K \leftrightarrow (K \leftrightarrow E) \Leftrightarrow E$$

porque $K \leftrightarrow K$ é sempre verdadeiro. A resposta "sim" quer
dizer exatamente que a esquerda leva à cidade, seja quem for o habitante.

| $K$ | $E$ | $Q=K\leftrightarrow E$ | responde |
|:-:|:-:|:-:|:-:|
| V | V | V | sim |
| V | F | F | não |
| F | V | F | mente: **sim** |
| F | F | V | mente: **não** |

A coluna "responde" é igual à coluna $E$. $\checkmark$

(Uma pergunta equivalente muito usada: "Se eu te perguntasse se a esquerda
leva à cidade, dirias que sim?")

#### (k) *(opcional)* "Algum de vós é cavaleiro?" A resposta chegou para saber a resposta à pergunta. O que são os dois?

**O interrogado é vilão e o outro é cavaleiro.**

Seja X o interrogado e Y o outro. Vê o que cada caso responde:

| X | Y | "algum é cavaleiro?" (verdade) | X responde |
|:-:|:-:|:-:|:-:|
| cav. | cav. | sim | sim |
| cav. | vil. | sim | sim |
| vil. | cav. | sim | mente: **não** |
| vil. | vil. | não | mente: **sim** |

Se a resposta fosse "sim", podia ser qualquer uma de três linhas, e o
narrador **não** ficaria a saber se algum é cavaleiro (em duas das linhas
sim, na última não). Como ele diz que ficou a saber, a resposta foi "não",
e isso só acontece na 3.ª linha.

### 1.12 --- Regras de escolha de cadeiras

Variáveis: $G$ = escolhe Computação Gráfica, $N$ = Programação Numérica,
$A$ = Álgebra.

- R1: $G \to (N \lor A)$
- R2: $A \leftrightarrow (G \lor N)$
- R3: $\neg(G \land N \land A) \land (G \lor N \lor A)$
- R4: $\neg A \to (G \land N)$

#### 1. É possível satisfazer as regras?

Verificam-se as 8 valorações. ✗ = regra violada:

| $G$ | $N$ | $A$ | R1 | R2 | R3 | R4 | todas? |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| F | F | F | V | V | ✗ (nenhuma) | ✗ | não |
| F | F | V | V | ✗ ($A$ sem $G\lor N$) | V | V | não |
| F | V | F | V | ✗ | V | V | não |
| F | V | V | V | V | V | V | **sim** |
| V | F | F | ✗ | ✗ | V | ✗ | não |
| V | F | V | V | V | V | V | **sim** |
| V | V | F | V | ✗ | V | V | não |
| V | V | V | V | V | ✗ (as três) | V | não |

**Sim, é possível.** Há duas escolhas válidas: {Numérica, Álgebra} e
{Gráfica, Álgebra}.

#### 2. A regra R4 é mesmo necessária? E a R1?

Uma regra é **desnecessária** se, retirando-a, as escolhas válidas
continuarem as mesmas. Na tabela, isso quer dizer que não há nenhuma linha
em que **só** essa regra falhe.

- **R4:** as linhas onde R4 falha (FFF e VFF) já falham também R3 ou R2.
  **Não é necessária.**
- **R1:** a única linha onde R1 falha (VFF) já falha R2. **Também não é
  necessária.**

R2 e R3 sozinhas já dão as mesmas duas soluções.

#### 3. Uma regra simples equivalente às quatro

"**Escolhe Álgebra e exatamente uma das outras duas.**"

$$A \land (G \leftrightarrow \neg N)$$

($G \leftrightarrow \neg N$ é o "ou exclusivo": uma e só uma das duas.) É
verdadeira exatamente nas linhas FVV e VFV. $\checkmark$

## Aula 3 --- Formas normais

### 1.17 --- FND e FNC a partir da tabela

#### (b) coluna (b): F V F V V V F F (linhas por ordem VVV, VVF, ..., FFF)

**Linhas verdadeiras** (dão a FND, uma conjunção por linha):
VVF, VFF, FVV, FVF.
$$\text{FND: } (p\land q\land\neg r) \lor (p\land\neg q\land\neg r) \lor (\neg p\land q\land r) \lor (\neg p\land q\land\neg r)$$

**Linhas falsas** (dão a FNC, uma cláusula por linha, com cada literal
**negado**): VVV, VFV, FFV, FFF.
$$\text{FNC: } (\neg p\lor\neg q\lor\neg r) \land (\neg p\lor q\lor\neg r) \land (p\lor q\lor\neg r) \land (p\lor q\lor r)$$

**Simplificação** (opcional, mas mostra o que a tabela "quer dizer"):
juntando os pares que só diferem numa variável,

- FND: $(p\land q\land\neg r)\lor(p\land\neg q\land\neg r) = p\land\neg r$ e
  $(\neg p\land q\land r)\lor(\neg p\land q\land\neg r) = \neg p\land q$.
  Fica $(p \land \neg r) \lor (\neg p \land q)$.
- FNC: as duas primeiras cláusulas dão $\neg p\lor\neg r$ e as duas
  últimas dão $p\lor q$. Fica $(\neg p\lor\neg r)\land(p\lor q)$.

Leitura: "se $p$, então o valor é $\neg r$; se não $p$, é $q$".

#### (c) coluna (c): V F V F V F V F

**Olha primeiro para a coluna:** é V exatamente quando $r = V$. A função
é simplesmente $r$.

As formas canónicas, se as fizeres pela regra:

- FND (4 linhas verdadeiras):
  $(p\land q\land r)\lor(p\land\neg q\land r)\lor(\neg p\land q\land r)\lor(\neg p\land\neg q\land r)$
- FNC (4 linhas falsas):
  $(\neg p\lor\neg q\lor r)\land(\neg p\lor q\lor r)\land(p\lor\neg q\lor r)\land(p\lor q\lor r)$

As duas simplificam para $r$, e **$r$ sozinho já é FND e FNC ao mesmo
tempo**: uma conjunção de um literal só, e uma cláusula de um literal só.

### 1.18 --- FND e FNC de uma fórmula

#### (e) $((p \to q) \to p) \to p$ (Lei de Peirce)

1. Pela 1.6(d), $(p \to q) \to p \Leftrightarrow p$.
2. A fórmula fica $p \to p \Leftrightarrow \neg p \lor p$.

**FNC:** $\neg p \lor p$ (uma só cláusula, que é uma tautologia).
**FND:** $\neg p \lor p$ (duas conjunções de um literal cada).

A mesma expressão serve para as duas formas. Resposta à pergunta da caixa:
a FNC de uma tautologia fica só com cláusulas que contêm um literal e a sua
negação ($\neg p \lor p$), ou seja, cláusulas sempre verdadeiras. Se se
retirarem, sobra a conjunção vazia ($\top$).

Sem usar a 1.6(d), eliminando tudo "à força":
$\neg(\neg(\neg p\lor q)\lor p)\lor p \Leftrightarrow ((\neg p\lor q)\land\neg p)\lor p$,
e distribuindo fica $(\neg p\lor q\lor p)\land(\neg p\lor p)$. As duas
cláusulas têm $p$ e $\neg p$, logo são as duas tautologias.

#### (l) $((p \lor q) \to (r \land s)) \to (p \lor \neg r)$

**Passo 1 --- eliminar as implicações.**

- Interior: $(p\lor q) \to (r\land s) \Leftrightarrow \neg(p\lor q) \lor (r\land s)$
- Exterior: $X \to (p\lor\neg r) \Leftrightarrow \neg X \lor p \lor \neg r$

**Passo 2 --- empurrar a negação de $X$ (FNN).**
$$\neg\big(\neg(p\lor q) \lor (r\land s)\big) \Leftrightarrow (p\lor q) \land \neg(r\land s) \Leftrightarrow (p\lor q) \land (\neg r\lor\neg s)$$

A fórmula fica
$$\big[(p\lor q) \land (\neg r\lor\neg s)\big] \lor p \lor \neg r$$

**Passo 3a --- FNC** (distribuir o $\lor$ exterior sobre o $\land$):
$$(p\lor q\lor p\lor\neg r) \land (\neg r\lor\neg s\lor p\lor\neg r)$$
Tirando os literais repetidos:
$$\text{FNC: } (p \lor q \lor \neg r) \land (p \lor \neg r \lor \neg s)$$

**Passo 3b --- FND** (distribuir o $\land$ dentro dos parêntesis
retos):
$$(p\land\neg r)\lor(p\land\neg s)\lor(q\land\neg r)\lor(q\land\neg s)\lor p\lor\neg r$$
Já é FND. Simplificando por **absorção**: $p$ absorve $p\land\neg r$ e
$p\land\neg s$, e $\neg r$ absorve $q\land\neg r$.
$$\text{FND: } p \lor \neg r \lor (q \land \neg s)$$

**Verificação:** a fórmula só é falsa quando $p=F$, $r=V$ e não
$(q\land\neg s)$. Na original, com $p=F, r=V$ o consequente $p\lor\neg r$
é $F$, por isso o antecedente tem de ser $V$ para a fórmula dar $F$. Se
$q=V, s=F$, o antecedente fica $V\to F=F$ e a fórmula é $V$. Bate certo
$\checkmark$.

### 1.20 --- Programa para manipular fórmulas

#### (a) + (b) Uma implementação completa (Python)

Fórmulas representadas como tuplos: `"p"` é uma variável,
`("not", A)`, `("and", A, B)`, `("or", A, B)`, `("imp", A, B)`.

```python
from itertools import product

def variaveis(f):
    if isinstance(f, str):
        return {f}
    return set().union(*(variaveis(g) for g in f[1:]))

def valor(f, v):
    """(a) valor da fórmula na valoração v (dicionário variável -> bool)"""
    if isinstance(f, str):
        return v[f]
    op = f[0]
    if op == "not": return not valor(f[1], v)
    if op == "and": return valor(f[1], v) and valor(f[2], v)
    if op == "or":  return valor(f[1], v) or valor(f[2], v)
    if op == "imp": return (not valor(f[1], v)) or valor(f[2], v)

def valoracoes(vs):
    vs = sorted(vs)
    for bits in product([True, False], repeat=len(vs)):
        yield dict(zip(vs, bits))

def tabela(f):
    """(a) tabela de verdade: lista de (valoração, resultado)"""
    return [(v, valor(f, v)) for v in valoracoes(variaveis(f))]

def classificar(f):
    """(a) tautologia / contradição / satisfazível"""
    res = [r for _, r in tabela(f)]
    if all(res):     return "tautologia"
    if not any(res): return "contradição"
    return "satisfazível (não tautologia)"

# ---- (a) formas normais: os três passos da Aula 3 ----

def sem_imp(f):                       # 1) A -> B  ==  ¬A ∨ B
    if isinstance(f, str): return f
    if f[0] == "not": return ("not", sem_imp(f[1]))
    if f[0] == "imp": return ("or", ("not", sem_imp(f[1])), sem_imp(f[2]))
    return (f[0], sem_imp(f[1]), sem_imp(f[2]))

def fnn(f):                           # 2) empurrar ¬ (De Morgan, ¬¬A = A)
    if isinstance(f, str): return f
    if f[0] == "not":
        g = f[1]
        if isinstance(g, str): return f
        if g[0] == "not": return fnn(g[1])
        if g[0] == "and": return ("or",  fnn(("not", g[1])), fnn(("not", g[2])))
        if g[0] == "or":  return ("and", fnn(("not", g[1])), fnn(("not", g[2])))
    return (f[0], fnn(f[1]), fnn(f[2]))

def distribui(f, dentro, fora):       # 3) distributividade
    if isinstance(f, str) or f[0] == "not": return f
    a, b = distribui(f[1], dentro, fora), distribui(f[2], dentro, fora)
    if f[0] == fora:
        return (fora, a, b)
    if not isinstance(a, str) and a[0] == fora:
        return (fora, distribui((dentro, a[1], b), dentro, fora),
                      distribui((dentro, a[2], b), dentro, fora))
    if not isinstance(b, str) and b[0] == fora:
        return (fora, distribui((dentro, a, b[1]), dentro, fora),
                      distribui((dentro, a, b[2]), dentro, fora))
    return (dentro, a, b)

def fnc(f): return distribui(fnn(sem_imp(f)), "or", "and")   # ∨ desce sob ∧
def fnd(f): return distribui(fnn(sem_imp(f)), "and", "or")   # ∧ desce sob ∨

# ---- (b) consequência e equivalência ----

def consequencia(a, b):
    """a |= b : toda a valoração que satisfaz a também satisfaz b"""
    vs = variaveis(a) | variaveis(b)
    return all(valor(b, v) for v in valoracoes(vs) if valor(a, v))

def equivalentes(a, b):
    return consequencia(a, b) and consequencia(b, a)
```

**Teste** com a 1.18(l):

```python
f = ("imp", ("imp", ("or", "p", "q"), ("and", "r", "s")), ("or", "p", ("not", "r")))
classificar(f)            # 'satisfazível (não tautologia)'
fnc(f)                    # ((p∨q)∨(p∨¬r)) ∧ ((¬r∨¬s)∨(p∨¬r))
equivalentes(f, fnc(f))   # True
```

O resultado é a FNC da 1.18(l) antes de tirar os literais repetidos.
O programa não simplifica, por isso as formas saem mais longas do que as
feitas à mão, mas são equivalentes (confirmado com `equivalentes`).

## Aula 3 --- Fórmulas de Horn

### 1.21 --- Algoritmo de satisfazibilidade de Horn

#### (c) 3.ª fórmula: $\neg p \land (\neg p \lor q) \land \neg q$

**Como implicações:**

- $\neg p$ fica $p \to \bot$
- $\neg p \lor q$ fica $p \to q$
- $\neg q$ fica $q \to \bot$

**Não há nenhum facto** (nenhuma cláusula $\top \to x$). O algoritmo
começa sem nada marcado, e nenhuma cláusula tem o antecedente todo marcado
($p$ e $q$ não estão marcados). Na primeira volta nada muda e o algoritmo
para.

**Satisfazível**, com tudo a falso: $p = F$, $q = F$.
Verificação: $\neg p = V$; $\neg p\lor q = V$; $\neg q = V$ $\checkmark$.

Resposta à pergunta da caixa: sem factos, uma fórmula de Horn é **sempre
satisfazível**, basta pôr tudo a $F$.

#### (c) 4.ª fórmula: $p \land (\neg p \lor q) \land \neg r$

**Como implicações:** $\top \to p$, $p \to q$, $r \to \bot$.

1. Facto $\top \to p$: marca $p$.
2. $p \to q$: $p$ está marcado, marca $q$.
3. $r \to \bot$: $r$ não está marcado, não dispara.
4. Nova volta: nada muda. Nenhuma cláusula $\to\bot$ disparou.

**Satisfazível**, com $p = V$, $q = V$, $r = F$ (as marcadas a V, o resto
a F).
Verificação: $p = V$; $\neg p\lor q = F\lor V = V$; $\neg r = V$ $\checkmark$.

#### (a) Implementação

Cada cláusula de Horn é um par `(antecedentes, consequente)`, e
`consequente = None` representa $\bot$:

```python
def horn_sat(clausulas):
    marcadas = set()                    # variáveis que TÊM de ser V
    mudou = True
    while mudou:
        mudou = False
        for antecedentes, h in clausulas:
            if antecedentes <= marcadas:    # antecedente todo verdadeiro
                if h is None:
                    return None             # V -> ⊥ : INSATISFAZÍVEL
                if h not in marcadas:
                    marcadas.add(h)
                    mudou = True
    return marcadas                     # modelo: marcadas = V, resto = F
```

Um facto $p$ é `(set(), "p")`: o conjunto vazio está sempre contido nas
marcadas, por isso dispara logo. Testes (os quatro da 1.21(c)):

```python
horn_sat([({"p","q"}, None), ({"q"}, "r"), (set(), "q")])  # {'q','r'}
horn_sat([(set(), "p"), ({"p"}, "q"), ({"q"}, "p")])       # {'p','q'}
horn_sat([({"p"}, None), ({"p"}, "q"), ({"q"}, None)])     # set()  -> tudo F
horn_sat([(set(), "p"), ({"p"}, "q"), ({"r"}, None)])      # {'p','q'}
horn_sat([(set(), "p"), ({"p"}, "q"), ({"q"}, None)])      # None -> insatisf.
```

O último teste é extra: mostra o caso **insatisfazível** ($p$, $p\to q$,
$\neg q$).
