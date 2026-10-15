---
title: "Lógica Computacional --- Soluções dos exercícios \"Pratica agora\""
subtitle: "Exercícios de Praticas/Semana_1/proplogic.pdf e Praticas/Semana_3/proplogicproofs.pdf sugeridos no resumo. Tenta primeiro sozinho; abre uma alínea só depois de a teres feito."
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

## Aula 1 --- Tabelas de verdade

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

## Aula 2 --- A relação $\models_v$

### 1.5 --- A relação $\models_v$, com $v(p)=V$ e $v(q)=F$

#### (a) $(p \lor q) \to (p \land q)$

De $v(p)=V$ segue $\models_v p$, logo $\models_v p\lor q$. De $v(q)=F$
segue $\not\models_v q$, logo $\not\models_v p\land q$. Portanto
$\not\models_v (p\lor q)\to(p\land q)$.

#### (c) $(p \to q) \land (p \to \neg q)$

De $v(p)=V$ e $v(q)=F$ segue $\models_v p$ e $\not\models_v q$, logo
$\not\models_v p\to q$. Portanto $\not\models_v (p\to q)\land(p\to\neg q)$.

#### (d) $p \to (q \to (p \lor q))$

De $v(q)=F$ segue $\not\models_v q$, logo $\models_v q\to(p\lor q)$.
Portanto $\models_v p\to(q\to(p\lor q))$.

## Aula 2 --- Consequência e equivalência

### 1.6 --- Provar equivalências pelas leis

#### (b) $\neg p \to q \;\Leftrightarrow\; \neg q \to p$

$$
\begin{aligned}
\neg p \to q
&\Leftrightarrow \neg\neg p \lor q && \text{(por } \varphi\to\psi \Leftrightarrow \neg\varphi\lor\psi\text{)}\\
&\Leftrightarrow p \lor q && \text{(dupla negação)}\\
&\Leftrightarrow q \lor p && \text{(comutatividade)}\\
&\Leftrightarrow \neg\neg q \lor p && \text{(dupla negação)}\\
&\Leftrightarrow \neg q \to p && \text{(por } \varphi\to\psi \Leftrightarrow \neg\varphi\lor\psi\text{)}
\end{aligned}
$$

#### (c) $p \to (q \to r) \;\Leftrightarrow\; q \to (p \to r)$

$$
\begin{aligned}
p \to (q \to r)
&\Leftrightarrow \neg p \lor (\neg q \lor r) && \text{(por } \varphi\to\psi \Leftrightarrow \neg\varphi\lor\psi\text{, 2 vezes)}\\
&\Leftrightarrow (\neg p \lor \neg q) \lor r && \text{(associatividade)}\\
&\Leftrightarrow (\neg q \lor \neg p) \lor r && \text{(comutatividade)}\\
&\Leftrightarrow \neg q \lor (\neg p \lor r) && \text{(associatividade)}\\
&\Leftrightarrow q \to (p \to r) && \text{(por } \varphi\to\psi \Leftrightarrow \neg\varphi\lor\psi\text{, 2 vezes)}
\end{aligned}
$$

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


### 1.8 --- Validade

#### (c) $(p \land q) \lor r \;\Leftrightarrow\; (p \lor r) \land (q \lor r)$

**Válida.** É a lei da distributividade do $\lor$ sobre o $\land$. Uma lei
básica prova-se com a tabela de verdade dos dois lados:

| $p$ | $q$ | $r$ | $p\land q$ | $(p\land q)\lor r$ | $p\lor r$ | $q\lor r$ | $(p\lor r)\land(q\lor r)$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| V | V | V | V | **V** | V | V | **V** |
| V | V | F | V | **V** | V | V | **V** |
| V | F | V | F | **V** | V | V | **V** |
| V | F | F | F | **F** | V | F | **F** |
| F | V | V | F | **V** | V | V | **V** |
| F | V | F | F | **F** | F | V | **F** |
| F | F | V | F | **V** | V | V | **V** |
| F | F | F | F | **F** | F | F | **F** |

As duas colunas a negrito coincidem em todas as linhas, logo
$(p \land q) \lor r \Leftrightarrow (p \lor r) \land (q \lor r)$.

### 1.9 --- Classificar fórmulas

#### (c) $(p \to q) \to (\neg p \to \neg q)$

**Simplificar com as leis** (é o método que o enunciado pede):

$$
\begin{aligned}
(p \to q) \to (\neg p \to \neg q)
&\Leftrightarrow \neg(p \to q) \lor (\neg p \to \neg q) && \text{(implicação, na } \to \text{ exterior)}\\
&\Leftrightarrow \neg(\neg p \lor q) \lor (\neg\neg p \lor \neg q) && \text{(implicação, nas duas interiores)}\\
&\Leftrightarrow (\neg\neg p \land \neg q) \lor (\neg\neg p \lor \neg q) && \text{(De Morgan)}\\
&\Leftrightarrow (p \land \neg q) \lor (p \lor \neg q) && \text{(dupla negação, 2 vezes)}\\
&\Leftrightarrow \big(p \lor (p \lor \neg q)\big) \land \big(\neg q \lor (p \lor \neg q)\big) && \text{(distributividade, } \varphi=p,\ \psi=\neg q,\ \theta=p\lor\neg q\text{)}\\
&\Leftrightarrow (p \lor \neg q) \land (p \lor \neg q) && \text{(associatividade, comutatividade, idempotência)}\\
&\Leftrightarrow p \lor \neg q && \text{(idempotência)}
\end{aligned}
$$

(Atalho: absorção, $(p \land \neg q) \lor p \Leftrightarrow p$.)

**Satisfazível, mas não tautologia.** Com $v(p)=V$, $v(q)=V$:
$\models_v p$, logo $\models_v p\lor\neg q$ e $\models_v$ da fórmula. Com
$v'(p)=F$, $v'(q)=V$: $\not\models_{v'} p$ e $\not\models_{v'} \neg q$,
logo $\not\models_{v'} p\lor\neg q$ e $\not\models_{v'}$ da fórmula.

#### (h) $(p \to q) \land (\neg r \to (q \lor (\neg p \land r)))$

**Simplificar com as leis** (é o método que o enunciado pede):

$$
\begin{aligned}
&(p \to q) \land (\neg r \to (q \lor (\neg p \land r)))\\
\Leftrightarrow\ & (\neg p \lor q) \land (\neg\neg r \lor q \lor (\neg p \land r)) && \text{(implicação, 2 vezes)}\\
\Leftrightarrow\ & (\neg p \lor q) \land (q \lor r \lor (\neg p \land r)) && \text{(dupla negação; comutatividade)}\\
\Leftrightarrow\ & (\neg p \lor q) \land (q \lor r) && \text{(absorção: } r \lor (\neg p \land r) \Leftrightarrow r\text{)}
\end{aligned}
$$

**Satisfazível, mas não tautologia.** Com $v(q)=V$: $\models_v \neg p\lor
q$ e $\models_v q\lor r$, logo $\models_v$ da fórmula. Com $v'(p)=V$,
$v'(q)=F$: $\not\models_{v'} \neg p$ e $\not\models_{v'} q$, logo
$\not\models_{v'} \neg p\lor q$ e $\not\models_{v'}$ da fórmula.

## Aula 2 --- Propriedades de $\models$

### 1.15 --- Propriedades de $\models$

#### (a) $\models (\theta \lor \varphi) \to (\neg\theta \to \varphi)$

**Verdadeira.** Prova por absurdo. Suponha-se que existe $v$ com
$\not\models_v (\theta\lor\varphi)\to(\neg\theta\to\varphi)$. Então:

1. $\models_v \theta\lor\varphi$ e $\not\models_v \neg\theta\to\varphi$
   (regra da negação de $\to$).
2. $\not\models_v \neg\theta\to\varphi$ sse $\models_v \neg\theta$ e
   $\not\models_v \varphi$, isto é, $\not\models_v \theta$ e
   $\not\models_v \varphi$.
3. Por 2, $\not\models_v \theta\lor\varphi$ (regra do $\lor$: nenhum dos
   lados é satisfeito). Isto contradiz 1.

Logo não existe tal $v$, e
$\models (\theta\lor\varphi)\to(\neg\theta\to\varphi)$. $\blacksquare$

#### (b) $\{\varphi \to \psi,\ \psi \to \varphi\} \models (\varphi \lor \psi) \to (\varphi \land \psi)$

**Verdadeira.** Tabela de verdade, com $\varphi$ e $\psi$ no papel de
variáveis:

| $\varphi$ | $\psi$ | $\varphi\to\psi$ | $\psi\to\varphi$ | $\varphi\lor\psi$ | $\varphi\land\psi$ | $(\varphi\lor\psi)\to(\varphi\land\psi)$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| V | V | **V** | **V** | V | V | **V** |
| V | F | F | V | V | F | F |
| F | V | V | F | V | F | F |
| F | F | **V** | **V** | F | F | **V** |

Nas linhas em que $\varphi\to\psi$ e $\psi\to\varphi$ são ambas V (1.ª e
4.ª), a conclusão também é V. Logo a consequência semântica vale.

#### (c) $\{\psi \to (\neg\varphi \lor \gamma),\ \neg\gamma\} \models \neg\varphi \to \neg\psi$

**Falsa.** Seja $v$ tal que $v(\varphi)=F$, $v(\psi)=V$ e $v(\gamma)=F$.
De $\not\models_v \varphi$ segue $\models_v \neg\varphi$, logo
$\models_v \neg\varphi\lor\gamma$ e $\models_v \psi\to(\neg\varphi\lor\gamma)$.
De $\not\models_v \gamma$ segue $\models_v \neg\gamma$. Mas
$\models_v \neg\varphi$ e $\not\models_v \neg\psi$, logo
$\not\models_v \neg\varphi\to\neg\psi$. Portanto
$\{\psi\to(\neg\varphi\lor\gamma),\ \neg\gamma\} \not\models \neg\varphi\to\neg\psi$
(por exemplo com $\varphi=p$, $\psi=q$, $\gamma=r$).

#### (d) Se $\varphi, \psi \models \theta \to \gamma$ e $\varphi \models \theta$, então $\varphi, \psi \models \gamma$

**Verdadeira.** Por absurdo: suponha-se $\varphi,\psi \models
\theta\to\gamma$ e $\varphi \models \theta$, mas $\varphi,\psi
\not\models \gamma$. Então existe $v$ com $\models_v \varphi$,
$\models_v \psi$ e $\not\models_v \gamma$. Da primeira hipótese,
$\models_v \theta\to\gamma$; como $\not\models_v \gamma$, tem-se
$\not\models_v \theta$. Mas $\models_v \varphi$ e $\varphi \models
\theta$ dão $\models_v \theta$: contradição. Logo $\varphi,\psi \models
\gamma$. $\blacksquare$

## Aula 2 --- Modelação

### 1.10 --- Cavaleiros e vilões

#### (g) A diz: "B e C são do mesmo tipo." Pergunta-se a C: "A e B são do mesmo tipo?" O que respondeu C?

**C respondeu "sim".** Há quatro casos compatíveis com a frase de A:

- A é cavaleiro e B, C são cavaleiros: A e B são do mesmo tipo e C diz a
  verdade, logo responde "sim".
- A é cavaleiro e B, C são vilões: A e B não são do mesmo tipo e C mente,
  logo responde "sim".
- A é vilão (B e C de tipos diferentes), B vilão e C cavaleiro: A e B são
  do mesmo tipo e C diz a verdade, logo responde "sim".
- A é vilão, B cavaleiro e C vilão: A e B não são do mesmo tipo e C
  mente, logo responde "sim".

#### (j) Que pergunta de "sim/não" fazer para saber qual caminho leva à cidade?

**Pergunta:** *"O que responderias se eu te perguntasse: o caminho da
direita leva à cidade?"*

- Se a direita leva à cidade: um cavaleiro responderia "sim" à pergunta
  interior e diz a verdade, logo diz "sim". Um vilão responderia "não" à
  pergunta interior; como mente sobre o que responderia, diz "sim".
- Se a direita não leva à cidade: o cavaleiro responderia "não" e diz
  "não"; o vilão responderia "sim" e, mentindo, diz "não".

Em todos os casos a resposta é "sim" exatamente quando a direita leva à
cidade. (Pergunta equivalente: "A direita leva à cidade se e só se tu és
cavaleiro?")

#### (k) *(opcional)* "Algum de vós é cavaleiro?" A resposta chegou para saber a resposta à pergunta. O que são os dois?

**O interrogado é vilão e o outro é cavaleiro.**

Se a resposta fosse "sim", o narrador não ficaria a saber nada: podia ser
um cavaleiro a dizer a verdade ou um vilão a mentir (com os dois vilões).
Logo a resposta foi "não". Um cavaleiro não pode responder "não" (seria
mentira, porque ele próprio é cavaleiro), logo o interrogado é vilão. Como
mente, a resposta verdadeira é "sim": algum é cavaleiro, e só pode ser o
outro.

### 1.12 --- Regras de escolha de cadeiras

Variáveis: $G$ = escolhe Computação Gráfica, $N$ = Programação Numérica,
$A$ = Álgebra.

- R1: $G \to (N \lor A)$
- R2: $A \leftrightarrow (G \lor N)$
- R3: $\neg(G \land N \land A) \land (G \lor N \lor A)$
- R4: $\neg A \to (G \land N)$

#### 1. É possível satisfazer as regras?

**Sim.** Seja $v(G)=V$, $v(N)=F$, $v(A)=V$ (Gráfica e Álgebra).
$\models_v A$, logo $\models_v N\lor A$ e $\models_v$ R1. $\models_v A$ e
$\models_v G\lor N$, logo $\models_v$ R2. $\models_v G\lor N\lor A$ e
$\not\models_v N$, logo $\not\models_v G\land N\land A$ e $\models_v$ R3.
$\not\models_v \neg A$, logo $\models_v$ R4. (Também serve Numérica e
Álgebra.)

#### 2. A regra R4 é mesmo necessária? E a R1?

Uma regra pode tirar-se sse é **consequência semântica** das outras: se
$\Gamma \models \varphi$, então $\Gamma\cup\{\varphi\}$ e $\Gamma$ são
satisfeitos pelas mesmas valorações.

**R1 não é necessária:** $\{R2, R3\} \models R1$. Seja $v$ com
$\models_v$ R2 e $\models_v$ R3. Se $\not\models_v G$, então
$\models_v G\to(N\lor A)$. Se $\models_v G$, então $\models_v G\lor N$ e,
por R2, $\models_v A$; logo $\models_v N\lor A$ e $\models_v$ R1.

**R4 também não é necessária:** $\{R2, R3\} \models R4$. Seja $v$ com
$\models_v$ R2 e $\models_v$ R3. Se $\not\models_v \neg A$, então
$\models_v$ R4. Se $\models_v \neg A$, por R2 $\not\models_v G\lor N$, isto
é, $\not\models_v G$ e $\not\models_v N$; então $\not\models_v G\lor N\lor
A$ e $\not\models_v$ R3, o que é impossível. Logo $\models_v$ R4.

(A folha de soluções diz que R4 não é consequência das restantes, mas a
prova acima, confirmada pelas 8 valorações, mostra que é.)

#### 3. Uma regra simples equivalente às quatro

"**Escolhe Álgebra e uma das outras duas, mas não as três.**"
$$A \land (G\lor N) \land \neg(G\land N)$$
Pelas alíneas anteriores as quatro regras equivalem a $\{R2, R3\}$, e
$\{R2,R3\}$ só é satisfeito por $\{G, A\}$ e $\{N, A\}$, tal como esta
regra.

## Aula 3 --- Formas normais

### 1.17 --- FND e FNC a partir da tabela

#### (b) coluna (b): F V F V V V F F (linhas por ordem VVV, VVF, ..., FFF)

**Linhas verdadeiras** (dão a FND, uma conjunção por linha):
VVF, VFF, FVV, FVF.
$$\text{FND: } (p\land q\land\neg r) \lor (p\land\neg q\land\neg r) \lor (\neg p\land q\land r) \lor (\neg p\land q\land\neg r)$$

**Linhas falsas** (dão a FNC, uma cláusula por linha, com cada literal
**negado**): VVV, VFV, FFV, FFF.
$$\text{FNC: } (\neg p\lor\neg q\lor\neg r) \land (\neg p\lor q\lor\neg r) \land (p\lor q\lor\neg r) \land (p\lor q\lor r)$$

#### (c) coluna (c): V F V F V F V F

Linhas verdadeiras VVV, VFV, FVV, FFV; falsas VVF, VFF, FVF, FFF.
$$\text{FND: } (p\land q\land r)\lor(p\land\neg q\land r)\lor(\neg p\land q\land r)\lor(\neg p\land\neg q\land r)$$
$$\text{FNC: } (\neg p\lor\neg q\lor r)\land(\neg p\lor q\lor r)\land(p\lor\neg q\lor r)\land(p\lor q\lor r)$$

(A coluna é V exatamente quando $r$ é V: as duas simplificam para $r$,
que já é FND e FNC.)

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

Nenhuma variável é um elemento da conjunção (não há factos), por isso
nada é obrigatório e a fórmula satisfaz-se com todas as variáveis a $F$:

| $p$ | $q$ | $\neg p$ | $\neg p \lor q$ | $\neg q$ |
|:-:|:-:|:-:|:-:|:-:|
| F | F | V | V | V |

**Satisfazível** para $v(p)=v(q)=F$. Sem factos, uma fórmula de Horn é
sempre satisfazível.

#### (c) 4.ª fórmula: $p \land (\neg p \lor q) \land \neg r$

$p$ é um elemento da conjunção, logo $p = V$ (o literal $\neg p$ fica F):

| $p$ | $q$ | $r$ | $p$ | $\neg p \lor q$ | $\neg r$ |
|:-:|:-:|:-:|:-:|:-:|:-:|
| V | | | V | F | |

Em $\neg p \lor q$ o único literal negativo já é F, logo $q = V$:

| $p$ | $q$ | $r$ | $p$ | $\neg p \lor q$ | $\neg r$ |
|:-:|:-:|:-:|:-:|:-:|:-:|
| V | V | | V | F V | |

Não há mais propagação e nenhum elemento ficou F; a variável restante fica
a F:

| $p$ | $q$ | $r$ | $p$ | $\neg p \lor q$ | $\neg r$ |
|:-:|:-:|:-:|:-:|:-:|:-:|
| V | V | F | V | F V | V |

**Satisfazível** para $v(p)=v(q)=V$, $v(r)=F$.

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

## Aula 4 --- O algoritmo DLL

### 1.22 --- Algoritmo de Davis-Putnam (DLL)

#### (c) $\{p \lor \neg q \lor \neg r,\ \neg p \lor q \lor r,\ \neg p \lor q \lor r,\ \neg p \lor q,\ \neg p \lor r\}$

Seja (a cláusula repetida conta uma vez)
$$S = \{p \lor \neg q \lor \neg r,\ \neg p \lor q \lor r,\ \neg p \lor q,\ \neg p \lor r\}$$
Não há cláusulas unitárias; escolhe-se $p$ e chama-se DLL$(S \cup \{p\})$.
A propagação unitária de $p$ dá
$$S_1 = \{q \lor r,\ q,\ r\}$$
A propagação unitária de $q$ dá $S_2 = \{r\}$, e a de $r$ dá $\{\ \}$.
Logo $S$ é satisfazível para $v(p)=v(q)=v(r)=V$.

#### (e) $\{p \lor \neg q \lor \neg r,\ \neg p \lor q \lor r,\ \neg p \lor \neg q \lor \neg r,\ \neg p \lor \neg q \lor r,\ \neg p \lor q \lor \neg r,\ p \lor q \lor \neg r\}$

Seja $S$ este conjunto. Não há cláusulas unitárias; escolhe-se $p$ e
chama-se DLL$(S \cup \{p\})$. A propagação unitária de $p$ dá
$$S_1 = \{q \lor r,\ \neg q \lor \neg r,\ \neg q \lor r,\ q \lor \neg r\}$$
Não há cláusulas unitárias; escolhe-se $q$ e chama-se
DLL$(S_1 \cup \{q\})$. A propagação de $q$ dá $S_2 = \{\neg r,\ r\}$, e a
de $\neg r$ dá $\{F\}$.

Volta-se ao último ponto de escolha: DLL$(S_1 \cup \{\neg q\})$. A
propagação de $\neg q$ dá $S_3 = \{r,\ \neg r\}$, e a de $r$ dá $\{F\}$.

Os dois ramos de $q$ falham; volta-se à escolha de $p$:
DLL$(S \cup \{\neg p\})$. A propagação unitária de $\neg p$ dá
$$S_4 = \{\neg q \lor \neg r,\ q \lor \neg r\}$$
Não há cláusulas unitárias; escolhe-se $\neg r$ e chama-se
DLL$(S_4 \cup \{\neg r\})$. A propagação de $\neg r$ dá $\{\ \}$.

Logo $S$ é satisfazível para $v(p)=F$, $v(r)=F$ ($q$ qualquer).
(Escolhendo logo $\neg p$, como na folha de soluções, chega-se aqui sem
voltar atrás.)

### 1.23 --- Implementar o algoritmo DLL

#### Resposta

Resposta-modelo em Python. Um literal é uma string: `"p"` ou `"-p"`. Uma
cláusula é um `frozenset` de literais; o conjunto de cláusulas é uma
lista. A função devolve uma valoração (dicionário) se o conjunto for
satisfazível, e `None` se não for.

```python
def comp(l):
    """Literal complementar: 'p' <-> '-p'."""
    return l[1:] if l.startswith("-") else "-" + l

def propagate(S, modelo):
    """Propagação unitária. S: lista de frozensets. Devolve o novo S
    (pode conter frozenset() = cláusula vazia = F)."""
    while True:
        if frozenset() in S:
            return S
        unit = next((c for c in S if len(c) == 1), None)
        if unit is None:
            return S
        (l,) = unit
        modelo[l.lstrip("-")] = not l.startswith("-")
        novo = []
        for c in S:
            if l in c:                 # 1. cláusula satisfeita: sai
                continue
            if comp(l) in c:           # 2. tira o literal complementar
                c = c - {comp(l)}
            novo.append(c)
        S = novo

def select_literal(S):
    """Critério: a variável que ocorre mais vezes (positiva)."""
    conta = {}
    for c in S:
        for l in c:
            v = l.lstrip("-")
            conta[v] = conta.get(v, 0) + 1
    return max(sorted(conta), key=lambda v: conta[v])

def dll(S, modelo=None):
    """Devolve um modelo (dict) se S é satisfazível, None se não é."""
    modelo = dict(modelo or {})
    S = propagate([frozenset(c) for c in S], modelo)
    if not S:
        return modelo                  # sem cláusulas: satisfazível
    if frozenset() in S:
        return None                    # contém F: insatisfazível
    l = select_literal(S)
    r = dll(S + [frozenset([l])], modelo)
    if r is not None:
        return r
    return dll(S + [frozenset([comp(l)])], modelo)
```

Como corresponde ao pseudo-código dos slides:

- `propagate` aplica as duas regras da propagação unitária até não haver
  cláusulas unitárias (ou aparecer a cláusula vazia), e regista em
  `modelo` o valor de cada literal propagado.
- "S vazio" é `not S`; "S contém F" é `frozenset() in S`.
- `S + [frozenset([l])]` é $S \cup \{l\}$; se falhar, tenta
  $S \cup \{\tilde{l}\}$.
- As variáveis que não estão no modelo devolvido podem ter qualquer valor.

Testes (resultados obtidos a correr o código):

```python
def P(s):  # "p|-q, q" -> [{"p","-q"}, {"q"}]
    return [set(c.strip() for c in cl.split("|")) for cl in s.split(",")]

dll(P("-p|-q, -p|q, p|-q, p|q"))                     # None (slides)
dll(P("p|q|r, -p|-q|-r, p|-q|-r, p|q|-r, -p|q, -p|r, p|-q|r"))
                                                     # None  (1.22 a)
dll(P("-p|q|r, p|q|r, p|q|-r, p|-q|r, p|-q|-r"))    # {'p': True, 'q': True}  (b)
dll(P("p|-q|-r, -p|q|r, -p|q|r, -p|q, -p|r"))       # {'p': True, 'q': True, 'r': True}  (c)
dll(P("p|-q|r, -p|q|r, p|-q|-r, -p|q|-r, -p|-q|-r"))
                                                     # {'p': True, 'q': True, 'r': False}  (d)
dll(P("p|-q|-r, -p|q|r, -p|-q|-r, -p|-q|r, -p|q|-r, p|q|-r"))
                                                     # {'p': False, 'q': True, 'r': False}  (e)
```

Todos os resultados foram confirmados por força bruta (tabela de verdade
completa): os `None` são mesmo insatisfazíveis e cada valoração devolvida
satisfaz todas as cláusulas.

## Aulas 5--6 --- Dedução natural: conjunção

Todas as deduções usam só as regras base de DN, em notação de Fitch, e
foram verificadas passo a passo com um verificador automático.

### 2.11 --- Equivalência dedutiva (só $\land$)

#### (c) $(\psi\land\phi)\land\delta \dashv\vdash \psi\land(\phi\land\delta)$

São duas deduções. Em cada uma desmonta-se a premissa com $\land$E até às
três peças $\psi$, $\phi$, $\delta$ e monta-se a conclusão com $\land$I.

**($\vdash$)**

```{.fitch seq="(psi /\ phi) /\ delta |- psi /\ (phi /\ delta)"}
(psi /\ phi) /\ delta
---
psi /\ phi                ; &E, 1
delta                     ; &E, 1
psi                       ; &E, 2
phi                       ; &E, 2
phi /\ delta              ; &I, 5, 3
psi /\ (phi /\ delta)     ; &I, 4, 6
```

**($\dashv$)**

```{.fitch seq="psi /\ (phi /\ delta) |- (psi /\ phi) /\ delta"}
psi /\ (phi /\ delta)
---
psi                       ; &E, 1
phi /\ delta              ; &E, 1
phi                       ; &E, 3
delta                     ; &E, 3
psi /\ phi                ; &I, 2, 4
(psi /\ phi) /\ delta     ; &I, 6, 5
```

## Aulas 5--6 --- Dedução natural: disjunção

### 2.4 --- Deduções válidas ou não (disjunção)

#### (a) Dedução dada de $p\land q$ a partir de $p\lor q$

```{.fitch .nocheck}
p \/ q
---
|> p
|  p
|> q
|  q
p /\ q
```

Passos 1--5 estão corretos: 1 premissa; 2 hipótese; 3 R, 2; 4 hipótese;
5 R, 4.

**O passo 6 está errado.** As duas sub-deduções terminam em fórmulas
**diferentes** ($p$ e $q$), e $\lor$E exige que terminem na **mesma**
fórmula $\gamma$, que é a que se conclui. Também não é $\land$I, porque
$p$ (linha 3) e $q$ (linha 5) estão em sub-deduções já fechadas e não
podem ser usados na linha 6.

**Não existe dedução correta** de $p\land q$ a partir de $p\lor q$.
Contraexemplo: $v(p)=V$, $v(q)=F$.

- $\models_v p\lor q$ sse $\models_v p$ ou $\models_v q$; como $v(p)=V$,
  $\models_v p$, logo $\models_v p\lor q$.
- $\not\models_v p\land q$ sse $\not\models_v p$ ou $\not\models_v q$;
  como $v(q)=F$, $\not\models_v q$, logo $\not\models_v p\land q$.

Assim $p\lor q \not\models p\land q$ e, pela integridade de DN,
$p\lor q \nvdash p\land q$.

### 2.11 --- Equivalência dedutiva (distributividade)

#### (h) $(\delta\lor\phi)\land(\delta\lor\psi) \dashv\vdash \delta\lor(\phi\land\psi)$

**($\vdash$)** Tiram-se as duas disjunções com $\land$E. A primeira,
$\delta\lor\phi$, dá dois casos: no caso $\delta$ é imediato; no caso
$\phi$ ainda falta $\psi$, por isso abre-se a segunda disjunção
$\delta\lor\psi$ (outro $\lor$E, **dentro** do caso $\phi$).

```{.fitch seq="(delta \/ phi) /\ (delta \/ psi) |- delta \/ (phi /\ psi)"}
(delta \/ phi) /\ (delta \/ psi)
---
delta \/ phi                  ; &E, 1
delta \/ psi                  ; &E, 1
|> delta
|  delta \/ (phi /\ psi)      ; vI, 4
|> phi
||> delta
||  delta \/ (phi /\ psi)     ; vI, 7
||> psi
||  phi /\ psi                ; &I, 6, 9
||  delta \/ (phi /\ psi)     ; vI, 10
|  delta \/ (phi /\ psi)      ; vE, 3, 7-8, 9-11
delta \/ (phi /\ psi)         ; vE, 2, 4-5, 6-12
```

A linha 10 usa a linha 6 ($\phi$): é permitido, porque a sub-dedução 6--12
ainda está aberta na linha 10.

**($\dashv$)** Premissa é disjunção: dois casos, e em cada um monta-se a
conjunção das duas disjunções.

```{.fitch seq="delta \/ (phi /\ psi) |- (delta \/ phi) /\ (delta \/ psi)"}
delta \/ (phi /\ psi)
---
|> delta
|  delta \/ phi                       ; vI, 2
|  delta \/ psi                       ; vI, 2
|  (delta \/ phi) /\ (delta \/ psi)   ; &I, 3, 4
|> phi /\ psi
|  phi                                ; &E, 6
|  psi                                ; &E, 6
|  delta \/ phi                       ; vI, 7
|  delta \/ psi                       ; vI, 8
|  (delta \/ phi) /\ (delta \/ psi)   ; &I, 9, 10
(delta \/ phi) /\ (delta \/ psi)      ; vE, 1, 2-5, 6-11
```

## Aulas 5--6 --- Dedução natural: negação e F

### 2.4 --- Deduções válidas ou não (negação)

#### (c) Dedução dada de $q$ a partir de $\neg(p\lor\neg q)$

**É válida.** As regras de cada passo:

```{.fitch seq="~(p \/ ~q) |- q"}
~(p \/ ~q)
---
|> ~q
|  p \/ ~q            ; vI, 2
|  F                  ; FI, 1, 3
~~q                   ; ~I, 2-4
q                     ; ~E, 5
```

1 premissa; 2 hipótese; 3 $\lor$I (de $\neg q$ obtém-se a disjunção com
$\neg q$ do lado direito); 4 $\mathbf{F}$I com a premissa e a linha 3,
que é a fórmula que a premissa nega; 5 $\neg$I sobre a sub-dedução 2--4;
6 $\neg$E.

### 2.9 --- Deduções válidas ou não

#### (a) $\neg\delta,\ \delta\lor\phi \vdash \phi$

**Válida.** $\lor$E sobre $\delta\lor\phi$ com $\gamma=\phi$. No caso
$\delta$ há contradição com $\neg\delta$, e de $\mathbf{F}$ tira-se $\phi$
($\mathbf{F}$E). No caso $\phi$ é repetição.

```{.fitch seq="~delta, delta \/ phi |- phi"}
~delta
delta \/ phi
---
|> delta
|  F                  ; FI, 3, 1
|  phi                ; FE, 4
|> phi
|  phi                ; R, 6
phi                   ; vE, 2, 3-5, 6-7
```

(É o *silogismo disjuntivo*.)

#### (d) $\delta\lor\psi,\ \neg\psi\lor\phi \vdash \delta\lor\phi$

**Válida.** $\lor$E sobre $\delta\lor\psi$ com $\gamma=\delta\lor\phi$.
Caso $\delta$: $\lor$I. Caso $\psi$: ainda não se tem nada da forma
$\delta\lor\phi$, por isso abre-se a segunda premissa $\neg\psi\lor\phi$
(outro $\lor$E): no caso $\neg\psi$ há contradição com $\psi$
($\mathbf{F}$E); no caso $\phi$, $\lor$I.

```{.fitch seq="delta \/ psi, ~psi \/ phi |- delta \/ phi"}
delta \/ psi
~psi \/ phi
---
|> delta
|  delta \/ phi       ; vI, 3
|> psi
||> ~psi
||  F                 ; FI, 5, 6
||  delta \/ phi      ; FE, 7
||> phi
||  delta \/ phi      ; vI, 9
|  delta \/ phi       ; vE, 2, 6-8, 9-10
delta \/ phi          ; vE, 1, 3-4, 5-11
```

### 2.11 --- Equivalência dedutiva (De Morgan)

#### (d) $\neg(\neg\delta_1\land\neg\delta_2) \dashv\vdash \delta_1\lor\delta_2$

**($\vdash$)** A conclusão é uma disjunção e nenhum dos lados se obtém
diretamente: **por contradição**. Supõe-se $\neg(\delta_1\lor\delta_2)$.
Daí $\delta_1$ é impossível (daria $\delta_1\lor\delta_2$), logo
$\neg\delta_1$; o mesmo para $\neg\delta_2$. Juntas dão
$\neg\delta_1\land\neg\delta_2$, que contradiz a premissa.

```{.fitch seq="~(~delta1 /\ ~delta2) |- delta1 \/ delta2"}
~(~delta1 /\ ~delta2)
---
|> ~(delta1 \/ delta2)
||> delta1
||  delta1 \/ delta2      ; vI, 3
||  F                     ; FI, 4, 2
|  ~delta1                ; ~I, 3-5
||> delta2
||  delta1 \/ delta2      ; vI, 7
||  F                     ; FI, 8, 2
|  ~delta2                ; ~I, 7-9
|  ~delta1 /\ ~delta2     ; &I, 6, 10
|  F                      ; FI, 11, 1
~~(delta1 \/ delta2)      ; ~I, 2-12
delta1 \/ delta2          ; ~E, 13
```

**($\dashv$)** A conclusão é uma negação: supõe-se
$\neg\delta_1\land\neg\delta_2$ e procura-se $\mathbf{F}$, usando a
premissa (disjunção) com $\lor$E e $\gamma=\mathbf{F}$.

```{.fitch seq="delta1 \/ delta2 |- ~(~delta1 /\ ~delta2)"}
delta1 \/ delta2
---
|> ~delta1 /\ ~delta2
|  ~delta1                ; &E, 2
|  ~delta2                ; &E, 2
||> delta1
||  F                     ; FI, 5, 3
||> delta2
||  F                     ; FI, 7, 4
|  F                      ; vE, 1, 5-6, 7-8
~(~delta1 /\ ~delta2)     ; ~I, 2-9
```

## Aulas 5--6 --- Dedução natural: implicação

### 2.4 --- Deduções válidas ou não (implicação)

#### (d) Dedução dada de $\neg p\lor q$ a partir de $p\to q$

```{.fitch .nocheck}
p -> q
---
|> p
|  q
|  ~p \/ q
~p \/ q
```

Passos 1--4 corretos: 1 premissa; 2 hipótese; 3 $\to$E, 1, 2;
4 $\lor$I, 3.

**O passo 5 está errado.** Tira $\neg p\lor q$ de dentro da sub-dedução
2--4, que dependia da hipótese $p$. Não é R (a linha 4 já não é
acessível) e a única regra que fecha uma sub-dedução que começa em $p$ e
acaba em $\neg p\lor q$ é $\to$I, que daria $p\to(\neg p\lor q)$, não
$\neg p\lor q$.

**Existe dedução correta**, porque $p\to q \models \neg p\lor q$ (e DN é
completa). Como a conclusão é uma disjunção sem lado óbvio, faz-se **por
contradição**: supõe-se $\neg(\neg p\lor q)$; daí $\neg p$ é impossível,
logo $p$; com $p$, $q$; e $q$ dá $\neg p\lor q$, contradição.

```{.fitch seq="p -> q |- ~p \/ q"}
p -> q
---
|> ~(~p \/ q)
||> ~p
||  ~p \/ q           ; vI, 3
||  F                 ; FI, 4, 2
|  ~~p                ; ~I, 3-5
|  p                  ; ~E, 6
|  q                  ; ->E, 1, 7
|  ~p \/ q            ; vI, 8
|  F                  ; FI, 9, 2
~~(~p \/ q)           ; ~I, 2-10
~p \/ q               ; ~E, 11
```

#### (f) Dedução dada de $q\to p$ a partir de $\neg p\to\neg q$

```{.fitch .nocheck}
~p -> ~q
---
|> q
|  ~q
|  F
|  p
q -> p
```

**O passo 3 está errado.** $\neg q$ não se obtém de nada: para usar
$\neg p\to\neg q$ com $\to$E era preciso ter $\neg p$, e não há $\neg p$
nenhum (nem como premissa nem como hipótese). Os passos seguintes estariam
bem se o 3 estivesse: 4 $\mathbf{F}$I, 2, 3; 5 $\mathbf{F}$E, 4;
6 $\to$I, 2--5.

**Existe dedução correta.** A ideia certa é supor $\neg p$ (para poder
usar a premissa), chegar a $\mathbf{F}$, e concluir $p$ por contradição:

```{.fitch seq="~p -> ~q |- q -> p"}
~p -> ~q
---
|> q
||> ~p
||  ~q                ; ->E, 1, 3
||  F                 ; FI, 2, 4
|  ~~p                ; ~I, 3-5
|  p                  ; ~E, 6
q -> p                ; ->I, 2-7
```

### 2.5 --- Deduções com premissas

#### (b) $q\to p,\ q\to\neg p \vdash \neg q$

Conclusão é uma negação: supor $q$ e chegar a $\mathbf{F}$. Com $q$, as
duas premissas dão $p$ e $\neg p$.

```{.fitch seq="q -> p, q -> ~p |- ~q"}
q -> p
q -> ~p
---
|> q
|  p                  ; ->E, 1, 3
|  ~p                 ; ->E, 2, 3
|  F                  ; FI, 4, 5
~q                    ; ~I, 3-6
```

#### (e) $p\to(q\lor r),\ q\to s,\ r\to t \vdash p\to(s\lor t)$

Conclusão é uma implicação: supor $p$, chegar a $s\lor t$. Com $p$ tem-se
$q\lor r$, que pede $\lor$E com $\gamma = s\lor t$.

```{.fitch seq="p -> (q \/ r), q -> s, r -> t |- p -> (s \/ t)"}
p -> (q \/ r)
q -> s
r -> t
---
|> p
|  q \/ r             ; ->E, 1, 4
||> q
||  s                 ; ->E, 2, 6
||  s \/ t            ; vI, 7
||> r
||  t                 ; ->E, 3, 9
||  s \/ t            ; vI, 10
|  s \/ t             ; vE, 5, 6-8, 9-11
p -> (s \/ t)         ; ->I, 4-12
```

#### (g) $(t\to(r\lor p))\to((\neg r\lor k)\land\neg k) \vdash \neg r$

Conclusão é negação: supor $r$, chegar a $\mathbf{F}$. Para usar a
premissa (estratégia 6) é preciso o seu antecedente $t\to(r\lor p)$: é
uma implicação, obtém-se supondo $t$ e tirando $r\lor p$ de $r$ (que está
disponível). Daí sai $(\neg r\lor k)\land\neg k$; o $\lor$E sobre
$\neg r\lor k$ dá $\mathbf{F}$ nos dois casos.

```{.fitch seq="(t -> (r \/ p)) -> ((~r \/ k) /\ ~k) |- ~r"}
(t -> (r \/ p)) -> ((~r \/ k) /\ ~k)
---
|> r
||> t
||  r \/ p            ; vI, 2
|  t -> (r \/ p)      ; ->I, 3-4
|  (~r \/ k) /\ ~k    ; ->E, 1, 5
|  ~r \/ k            ; &E, 6
|  ~k                 ; &E, 6
||> ~r
||  F                 ; FI, 2, 9
||> k
||  F                 ; FI, 11, 8
|  F                  ; vE, 7, 9-10, 11-12
~r                    ; ~I, 2-13
```

Repara na linha 4: $r\lor p$ sai de $r$ (linha 2), que está acessível
porque a sub-dedução 2--13 ainda está aberta. A hipótese $t$ nem chega a
ser usada, o que é permitido.

### S9 --- Raciocínio "estudar ou chumbar" (slide 9)

$r$ = chumbas, $t$ = repetes, $e$ = estudas.

#### Resposta: $r\to t,\ \neg e\to r,\ \neg t \vdash e\lor r\lor(e\land r)$

A conclusão é uma disjunção (lida como $(e\lor r)\lor(e\land r)$): basta
deduzir $e$ e aplicar $\lor$I duas vezes. Para ter $e$, por contradição:
supor $\neg e$; dá $r$, que dá $t$, contra $\neg t$.

```{.fitch seq="r -> t, ~e -> r, ~t |- e \/ r \/ (e /\ r)"}
r -> t
~e -> r
~t
---
|> ~e
|  r                  ; ->E, 2, 4
|  t                  ; ->E, 1, 5
|  F                  ; FI, 6, 3
~~e                   ; ~I, 4-7
e                     ; ~E, 8
e \/ r                ; vI, 9
(e \/ r) \/ (e /\ r)  ; vI, 10
```

## Aulas 5--6 --- Dedução natural: deduções sem premissas

### 2.6 --- Deduções sem premissas

#### (b) $\vdash (\delta\to\psi)\to((\neg\delta\to\neg\phi)\to(\phi\to\psi))$

Três implicações encaixadas: supor $\delta\to\psi$, depois
$\neg\delta\to\neg\phi$, depois $\phi$, e chegar a $\psi$. Para ter $\psi$
precisa-se de $\delta$ (primeira hipótese); $\delta$ obtém-se por
contradição, porque $\neg\delta$ daria $\neg\phi$, contra $\phi$.

```{.fitch seq="|- (delta -> psi) -> ((~delta -> ~phi) -> (phi -> psi))"}
|> delta -> psi
||> ~delta -> ~phi
|||> phi
||||> ~delta
||||  ~phi                ; ->E, 2, 4
||||  F                   ; FI, 3, 5
|||  ~~delta              ; ~I, 4-6
|||  delta                ; ~E, 7
|||  psi                  ; ->E, 1, 8
||  phi -> psi            ; ->I, 3-9
|  (~delta -> ~phi) -> (phi -> psi)              ; ->I, 2-10
(delta -> psi) -> ((~delta -> ~phi) -> (phi -> psi))   ; ->I, 1-11
```

#### (d) $\vdash \delta\to(\neg\phi\to\neg(\delta\to\phi))$

Supor $\delta$, supor $\neg\phi$, e deduzir a negação
$\neg(\delta\to\phi)$: supor $\delta\to\phi$ e chegar a $\mathbf{F}$ (dá
$\phi$, contra $\neg\phi$).

```{.fitch seq="|- delta -> (~phi -> ~(delta -> phi))"}
|> delta
||> ~phi
|||> delta -> phi
|||  phi                  ; ->E, 3, 1
|||  F                    ; FI, 4, 2
||  ~(delta -> phi)       ; ~I, 3-5
|  ~phi -> ~(delta -> phi)          ; ->I, 2-6
delta -> (~phi -> ~(delta -> phi))  ; ->I, 1-7
```

#### (e) $\vdash ((\phi\to\delta)\land(\delta\to\phi))\to((\phi\lor\delta)\to(\phi\land\delta))$

Supor a conjunção e separá-la; supor $\phi\lor\delta$ e fazer $\lor$E
com $\gamma=\phi\land\delta$. Em cada caso a implicação certa dá o
lado que falta.

```{.fitch seq="|- ((phi -> delta) /\ (delta -> phi)) -> ((phi \/ delta) -> (phi /\ delta))"}
|> (phi -> delta) /\ (delta -> phi)
|  phi -> delta           ; &E, 1
|  delta -> phi           ; &E, 1
||> phi \/ delta
|||> phi
|||  delta                ; ->E, 2, 5
|||  phi /\ delta         ; &I, 5, 6
|||> delta
|||  phi                  ; ->E, 3, 8
|||  phi /\ delta         ; &I, 9, 8
||  phi /\ delta          ; vE, 4, 5-7, 8-10
|  (phi \/ delta) -> (phi /\ delta)       ; ->I, 4-11
((phi -> delta) /\ (delta -> phi)) -> ((phi \/ delta) -> (phi /\ delta))   ; ->I, 1-12
```

### 2.8 --- Mais deduções

#### (a) $\delta\to(\phi\to\psi),\ \neg\psi,\ \delta \vdash \neg\phi$

```{.fitch seq="delta -> (phi -> psi), ~psi, delta |- ~phi"}
delta -> (phi -> psi)
~psi
delta
---
phi -> psi            ; ->E, 1, 3
|> phi
|  psi                ; ->E, 4, 5
|  F                  ; FI, 6, 2
~phi                  ; ~I, 5-7
```

Primeiro tira-se $\phi\to\psi$ (linha 4). Depois a conclusão é negação:
supor $\phi$, dá $\psi$, contra $\neg\psi$. (É o MT, feito à mão.)

#### (c) $\vdash (\delta\to(\phi\to\psi))\to(\phi\to(\delta\to\psi))$

Troca da ordem das hipóteses: supor as três ($\delta\to(\phi\to\psi)$,
$\phi$, $\delta$) e aplicar $\to$E duas vezes.

```{.fitch seq="|- (delta -> (phi -> psi)) -> (phi -> (delta -> psi))"}
|> delta -> (phi -> psi)
||> phi
|||> delta
|||  phi -> psi           ; ->E, 1, 3
|||  psi                  ; ->E, 4, 2
||  delta -> psi          ; ->I, 3-5
|  phi -> (delta -> psi)  ; ->I, 2-6
(delta -> (phi -> psi)) -> (phi -> (delta -> psi))   ; ->I, 1-7
```

#### (e) $\vdash ((\phi\to\delta)\to\delta)\to((\delta\to\phi)\to\phi)$

Supor $(\phi\to\delta)\to\delta$ e $\delta\to\phi$; falta $\phi$, que é
uma letra: por contradição, supor $\neg\phi$. Com $\neg\phi$ consegue-se
$\phi\to\delta$ (supor $\phi$: contradiz $\neg\phi$, e de $\mathbf{F}$
tira-se $\delta$). Então a primeira hipótese dá $\delta$, a segunda dá
$\phi$, contra $\neg\phi$.

```{.fitch seq="|- ((phi -> delta) -> delta) -> ((delta -> phi) -> phi)"}
|> (phi -> delta) -> delta
||> delta -> phi
|||> ~phi
||||> phi
||||  F                   ; FI, 4, 3
||||  delta               ; FE, 5
|||  phi -> delta         ; ->I, 4-6
|||  delta                ; ->E, 7, 1
|||  phi                  ; ->E, 2, 8
|||  F                    ; FI, 9, 3
||  ~~phi                 ; ~I, 3-10
||  phi                   ; ~E, 11
|  (delta -> phi) -> phi  ; ->I, 2-12
((phi -> delta) -> delta) -> ((delta -> phi) -> phi)   ; ->I, 1-13
```

#### (g) $\delta,\ \neg\phi \vdash \neg(\delta\to\phi)$

```{.fitch seq="delta, ~phi |- ~(delta -> phi)"}
delta
~phi
---
|> delta -> phi
|  phi                ; ->E, 3, 1
|  F                  ; FI, 4, 2
~(delta -> phi)       ; ~I, 3-5
```

### 2.9 --- Deduções válidas ou não (implicação)

#### (e) $\vdash (\neg\delta\to\delta)\to\delta$

**Válida.** Supor $\neg\delta\to\delta$; falta $\delta$, por contradição:
$\neg\delta$ dá $\delta$ pela hipótese, contradição.

```{.fitch seq="|- (~delta -> delta) -> delta"}
|> ~delta -> delta
||> ~delta
||  delta             ; ->E, 1, 2
||  F                 ; FI, 3, 2
|  ~~delta            ; ~I, 2-4
|  delta              ; ~E, 5
(~delta -> delta) -> delta   ; ->I, 1-6
```

#### (f) $\neg\delta\to\neg\psi \vdash \neg\psi\to\neg\delta$

**Não é válida.** Contraexemplo: $\delta = p$, $\psi = q$, com $v(p)=V$,
$v(q)=F$.

- $\models_v \neg p\to\neg q$ sse $\not\models_v \neg p$ ou
  $\models_v \neg q$. Como $v(p)=V$, $\models_v p$, logo
  $\not\models_v \neg p$. Portanto $\models_v \neg p\to\neg q$.
- $\not\models_v \neg q\to\neg p$ sse $\models_v \neg q$ e
  $\not\models_v \neg p$. Como $v(q)=F$, $\models_v \neg q$; e
  $\not\models_v \neg p$ (acima). Portanto
  $\not\models_v \neg q\to\neg p$.

Logo $\neg p\to\neg q \not\models \neg q\to\neg p$ e, pela integridade de
DN, $\neg p\to\neg q \nvdash \neg q\to\neg p$. (A premissa equivale a
$q\to p$ e a conclusão a $p\to q$: é a **recíproca**, não a contraposição.)

## Aulas 5--6 --- Regras derivadas, raciocínios e equivalências

### 2.1 --- Forma lógica de argumentos

#### (a) Hugo resolve os exercícios → viaja para os Açores; vai viajar; logo resolveu

$h$ = "o Hugo resolve corretamente os exercícios", $a$ = "o Hugo viaja
para os Açores". Forma: $h\to a,\ a$ logo $h$.

**Não é válido** (é a falácia da *afirmação do consequente*).
Contraexemplo $v(h)=F$, $v(a)=V$:

- $\models_v h\to a$ sse $\not\models_v h$ ou $\models_v a$: verdade
  (as duas, até).
- $\models_v a$, porque $v(a)=V$.
- $\not\models_v h$, porque $v(h)=F$.

Logo $\{h\to a,\ a\} \not\models h$ (e, pela integridade,
$h\to a,\ a \nvdash h$).

#### (b) Cinema → não resolvo; não resolvo → chumbo; logo cinema → chumbo

$c$ = "vou ao cinema", $e$ = "resolvo os exercícios", $f$ = "chumbo a
matemática". Forma: $c\to\neg e,\ \neg e\to f$ logo $c\to f$.

**Válido**: é o *silogismo hipotético* (transitividade da implicação).

```{.fitch seq="c -> ~e, ~e -> f |- c -> f"}
c -> ~e
~e -> f
---
|> c
|  ~e                 ; ->E, 1, 3
|  f                  ; ->E, 2, 4
c -> f                ; ->I, 3-5
```

### 2.2 --- Completar argumentos

$m$ = "a matemática é difícil", $s$ = "o Pai Natal existe".

#### (a) Se a matemática é difícil, o Pai Natal existe. O Pai Natal não existe. Logo...

**"...a matemática não é difícil"** ($\neg m$), por *modus tollens*:

```{.fitch seq="m -> s, ~s |- ~m"}
m -> s
~s
---
|> m
|  s                  ; ->E, 1, 3
|  F                  ; FI, 4, 2
~m                    ; ~I, 3-5
```

#### (b) Se a matemática é difícil, o Pai Natal existe. A matemática é difícil. Logo...

**"...o Pai Natal existe"** ($s$), por *modus ponens*:

```{.fitch seq="m -> s, m |- s"}
m -> s
m
---
s                     ; ->E, 1, 2
```

### 2.3 --- Tautologias e argumentos

#### Resposta

Em cada argumento, chama-se $p$, $q$, $r$ às frases na ordem em que
aparecem no padrão da tautologia; o argumento "premissas logo
conclusão" corresponde à tautologia "premissas $\to$ conclusão".

| Argumento | Formalização | Tautologia |
|:-:|:--------------------------------------|:-:|
| (a) | $p$ = inscrito em LC, $q$ = em AED: $p$ logo $p\lor q$ | (3) |
| (b) | $p$ = programa em Java, $q$ = em C: $q\land p$ logo $p$ (é (2) com os lados trocados) | (2) |
| (c) | $p$ = trabalho em C, $q$ = em Java, $r$ = frequência: $(p\lor q)\to r,\ p$ logo $r$ | (6) |
| (d) | $p$ = a Maria foi à aula: $p\lor\neg p$ | (1) |
| (e) | $p$ = chove, $q$ = vou ao cinema: $p\to q$ logo $\neg q\to\neg p$ | (4) |
| (f) | $p$ = neva, $q$ = fico em casa: $p\to q,\ \neg p\to q$ logo $q$ | (5) |

### 2.7 --- Prova de "choveu"

#### Resposta

$c$ = "chove", $n$ = "há nevoeiro", $v$ = "a regata realiza-se",
$d$ = "a demonstração de salvamento realiza-se", $t$ = "o troféu é
entregue". Hipóteses:

- "Se não chove ou não há nevoeiro, a regata e a demonstração
  realizam-se": $(\neg c\lor\neg n)\to(v\land d)$
- "Se a regata se realiza, o troféu é entregue": $v\to t$
- "O troféu não foi entregue": $\neg t$

Conclusão $c$. É uma letra: por contradição, supor $\neg c$; dá
$\neg c\lor\neg n$, logo $v\land d$, logo $v$, logo $t$, contra $\neg t$.

```{.fitch seq="(~c \/ ~n) -> (v /\ d), v -> t, ~t |- c"}
(~c \/ ~n) -> (v /\ d)
v -> t
~t
---
|> ~c
|  ~c \/ ~n           ; vI, 4
|  v /\ d             ; ->E, 1, 5
|  v                  ; &E, 6
|  t                  ; ->E, 2, 7
|  F                  ; FI, 8, 3
~~c                   ; ~I, 4-9
c                     ; ~E, 10
```

### 2.11 --- Equivalência dedutiva (implicação e disjunção)

#### (g) $(\phi\lor\psi)\to\delta \dashv\vdash (\phi\to\delta)\land(\psi\to\delta)$

**($\vdash$)** A conclusão é uma conjunção: deduzir cada lado e $\land$I.
Cada lado é uma implicação: supor $\phi$ (ou $\psi$), fazer $\phi\lor\psi$
com $\lor$I e usar a premissa.

```{.fitch seq="(phi \/ psi) -> delta |- (phi -> delta) /\ (psi -> delta)"}
(phi \/ psi) -> delta
---
|> phi
|  phi \/ psi         ; vI, 2
|  delta              ; ->E, 1, 3
phi -> delta          ; ->I, 2-4
|> psi
|  phi \/ psi         ; vI, 6
|  delta              ; ->E, 1, 7
psi -> delta          ; ->I, 6-8
(phi -> delta) /\ (psi -> delta)   ; &I, 5, 9
```

**($\dashv$)** A conclusão é uma implicação: supor $\phi\lor\psi$ e chegar
a $\delta$ por casos, usando a implicação certa em cada caso.

```{.fitch seq="(phi -> delta) /\ (psi -> delta) |- (phi \/ psi) -> delta"}
(phi -> delta) /\ (psi -> delta)
---
phi -> delta          ; &E, 1
psi -> delta          ; &E, 1
|> phi \/ psi
||> phi
||  delta             ; ->E, 2, 5
||> psi
||  delta             ; ->E, 3, 7
|  delta              ; vE, 4, 5-6, 7-8
(phi \/ psi) -> delta ; ->I, 4-9
```

### A7.9 --- De Morgan deduzido (Aula 7, slide 9)

#### (b) $\neg(\phi\land\psi) \vdash \neg\phi\lor\neg\psi$

Conclusão disjunção: por contradição, supor $\neg(\neg\phi\lor\neg\psi)$.
Para contradizer a premissa $\neg(\phi\land\psi)$ é preciso
$\phi\land\psi$, isto é, $\phi$ e $\psi$. Cada um obtém-se por
contradição: supor $\neg\phi$ dá $\neg\phi\lor\neg\psi$ por $\lor$I,
contra a hipótese da linha 2 (o mesmo para $\neg\psi$).

```{.fitch seq="~(phi /\ psi) |- ~phi \/ ~psi"}
~(phi /\ psi)
---
|> ~(~phi \/ ~psi)
||> ~phi
||  ~phi \/ ~psi     ; vI, 3
||  F                ; FI, 4, 2
|  ~~phi             ; ~I, 3-5
|  phi               ; ~E, 6
||> ~psi
||  ~phi \/ ~psi     ; vI, 8
||  F                ; FI, 9, 2
|  ~~psi             ; ~I, 8-10
|  psi               ; ~E, 11
|  phi /\ psi        ; &I, 7, 12
|  F                 ; FI, 13, 1
~~(~phi \/ ~psi)     ; ~I, 2-14
~phi \/ ~psi         ; ~E, 15
```

## Aulas 5--6 --- Propriedades de $\vdash$

### 2.10 --- Verdadeiro ou falso

#### (e) Se $\delta_1,\delta_2 \vdash \phi\to\psi$ e $\delta_1 \vdash \phi$, então $\delta_1,\delta_2 \vdash \psi$

**Verdadeiro.** Sejam $D_1$ uma dedução de $\phi\to\psi$ a partir de
$\delta_1,\delta_2$ e $D_2$ uma dedução de $\phi$ a partir de $\delta_1$.
Constrói-se uma dedução de $\psi$ a partir de $\delta_1,\delta_2$:

1. premissas $\delta_1$, $\delta_2$;
2. as linhas de $D_1$ (sem repetir as premissas), com os números das
   justificações ajustados; a última é $\phi\to\psi$, na barra principal;
3. as linhas de $D_2$ (sem repetir a premissa $\delta_1$, que já é a
   linha 1), com os números ajustados; a última é $\phi$, na barra
   principal. Os passos de $D_2$ continuam válidos: só usam $\delta_1$ e
   linhas de $D_2$, e a premissa $\delta_2$ a mais não muda nada;
4. $\psi$ por $\to$E, citando as últimas linhas de 2 e 3 (ambas na barra
   principal, logo acessíveis).

Logo $\delta_1,\delta_2 \vdash \psi$. $\blacksquare$

#### (f) Se $\delta_1,\delta_2 \vdash \phi\to\psi$ e $\delta_1 \vdash \phi$, então $\delta_1 \vdash \psi$

**Falso.** Contraexemplo: $\delta_1 = p$, $\delta_2 = p\to q$, $\phi = p$,
$\psi = q$.

- $\delta_1,\delta_2 \vdash \phi\to\psi$, isto é, $p,\ p\to q \vdash p\to q$:

```{.fitch seq="p, p -> q |- p -> q"}
p
p -> q
---
p -> q                ; R, 2
```

- $\delta_1 \vdash \phi$, isto é, $p \vdash p$:

```{.fitch seq="p |- p"}
p
---
p                     ; R, 1
```

- Mas $\delta_1 \nvdash \psi$, isto é, $p \nvdash q$: com $v(p)=V$,
  $v(q)=F$ tem-se $\models_v p$ e $\not\models_v q$, logo
  $p \not\models q$; pela integridade de DN, $p \nvdash q$. $\blacksquare$

(A diferença para a (e): a dedução de $\phi\to\psi$ pode precisar de
$\delta_2$, e na (f) $\delta_2$ deixou de estar disponível.)

#### (g) Se $\delta_1 \vdash \phi\to\psi$ e $\delta_2 \vdash \phi$, então $\delta_1,\delta_2 \vdash \psi$

**Verdadeiro.** Igual à (e): premissas $\delta_1$, $\delta_2$; depois as
linhas da dedução de $\phi\to\psi$ (que só usa $\delta_1$); depois as
linhas da dedução de $\phi$ (que só usa $\delta_2$), com os números
ajustados; por fim $\psi$ por $\to$E. Cada passo copiado continua
justificado, porque as premissas a mais não são usadas e não fecham
nenhuma sub-dedução. Logo $\delta_1,\delta_2 \vdash \psi$. $\blacksquare$

### 2.15 --- Se para todo o $\delta$, $\Sigma\vdash\delta$ ou $\Gamma\vdash\delta$

#### (a) Um dos conjuntos $\Sigma$ ou $\Gamma$ não é satisfazível

Toma-se $\delta = \mathbf{F}$. Por hipótese, $\Sigma \vdash \mathbf{F}$ ou
$\Gamma \vdash \mathbf{F}$.

**Caso $\Sigma \vdash \mathbf{F}$.** Pela integridade de DN,
$\Sigma \models \mathbf{F}$: toda a valoração $v$ com $\models_v \Sigma$
tem $\models_v \mathbf{F}$. Mas $\not\models_v \mathbf{F}$ para toda a
$v$. Logo não existe $v$ com $\models_v \Sigma$: $\Sigma$ não é
satisfazível.

**Caso $\Gamma \vdash \mathbf{F}$.** Pelo mesmo argumento, $\Gamma$ não é
satisfazível.

Em ambos os casos, um dos conjuntos não é satisfazível. $\blacksquare$

#### (b) $\Sigma\cup\Gamma$ não é satisfazível

Por absurdo: suponha-se que existe $v$ com $\models_v \Sigma\cup\Gamma$,
isto é, $\models_v \gamma$ para todo o $\gamma\in\Sigma\cup\Gamma$. Como
$\Sigma \subseteq \Sigma\cup\Gamma$, $\models_v \Sigma$, e $\Sigma$ é
satisfazível; da mesma forma $\Gamma$ é satisfazível. Isto contradiz (a).
Logo $\Sigma\cup\Gamma$ não é satisfazível. $\blacksquare$

## Aula 8 --- Axiomas de $\mathcal{H}$ em DN

### A7.9 --- Axiomas de $\mathcal{H}$ são teoremas de DN (Aula 7, slide 9)

#### (c) $\vdash \phi\to(\psi\to\phi)$

Duas implicações encaixadas: supor $\phi$, depois $\psi$, e repetir
$\phi$ (acessível, da sub-dedução exterior) com R.

```{.fitch seq="|- phi -> (psi -> phi)"}
|> phi
||> psi
||  phi              ; R, 1
|  psi -> phi        ; ->I, 2-3
phi -> (psi -> phi)  ; ->I, 1-4
```

#### (e) $\vdash (\neg\psi\to\neg\phi)\to((\neg\psi\to\phi)\to\psi)$

Supor os dois antecedentes (linhas 1 e 2). Falta $\psi$, uma letra: por
contradição, supor $\neg\psi$; as duas hipóteses dão então $\phi$ e
$\neg\phi$, logo $\mathbf{F}$.

```{.fitch seq="|- (~psi -> ~phi) -> ((~psi -> phi) -> psi)"}
|> ~psi -> ~phi
||> ~psi -> phi
|||> ~psi
|||  phi             ; ->E, 2, 3
|||  ~phi            ; ->E, 1, 3
|||  F               ; FI, 4, 5
||  ~~psi            ; ~I, 3-6
||  psi              ; ~E, 7
|  (~psi -> phi) -> psi  ; ->I, 2-8
(~psi -> ~phi) -> ((~psi -> phi) -> psi)  ; ->I, 1-9
```

## Aula 8 --- Tableaux

### 2.17 --- Deduções por tableau

Em cada alínea a raiz é $\neg\phi$; os números entre $[\,]$ dizem o nó
expandido e $\times\,(i,k)$ fecha o ramo com $\psi$ no nó $i$ e $\neg\psi$
no $k$ (ou vice-versa).

#### (b) $((p\to q)\land(q\to r))\to(p\to r)$

A raiz é $\alpha$ ($\neg(\cdot\to\cdot)$): nós 2 e 3. O nó 3,
$\neg(p\to r)$, é $\alpha$: $p$, $\neg r$. O nó 2 é $\alpha$: as duas
implicações. Só restam $\beta$: $p\to q$ abre $\neg p$ (fecha com $p$) e
$q$; aqui $q\to r$ abre $\neg q$ (fecha com $q$) e $r$ (fecha com
$\neg r$).

```{.tableau seq="((p -> q) /\\ (q -> r)) -> (p -> r)"}
~(((p -> q) /\ (q -> r)) -> (p -> r))
(p -> q) /\ (q -> r) ; 1
~(p -> r)            ; 1
p                    ; 3
~r                   ; 3
p -> q               ; 2
q -> r               ; 2
[
~p                   ; 6
x                    ; 4, 8
|
q                    ; 6
[
~q                   ; 7
x                    ; 10, 11
|
r                    ; 7
x                    ; 5, 13
]
]
```

Todos os ramos fecham: tableau fechado para $\{\neg\phi\}$, logo $\phi$ tem
dedução por tableau (é teorema). $\blacksquare$

#### (c) $(\neg p\to q)\to((p\to q)\to q)$

Duas $\alpha$ seguidas (nós 2--5) dão $\neg p\to q$, $p\to q$ e $\neg q$.
A $\beta$ do nó 2 abre $\neg\neg p$ e $q$ (fecha com $\neg q$); no ramo
esquerdo, $\neg\neg p$ dá $p$ e a $\beta$ do nó 4 abre $\neg p$ (fecha com
$p$) e $q$ (fecha com $\neg q$).

```{.tableau seq="(~p -> q) -> ((p -> q) -> q)"}
~((~p -> q) -> ((p -> q) -> q))
~p -> q              ; 1
~((p -> q) -> q)     ; 1
p -> q               ; 3
~q                   ; 3
[
~~p                  ; 2
p                    ; 6
[
~p                   ; 4
x                    ; 7, 8
|
q                    ; 4
x                    ; 5, 10
]
|
q                    ; 2
x                    ; 5, 12
]
```

Tableau fechado para $\{\neg\phi\}$: $\phi$ é teorema. $\blacksquare$

#### (d) $((p\to q)\to p)\to p$

A raiz dá $(p\to q)\to p$ e $\neg p$. A $\beta$ do nó 2 abre
$\neg(p\to q)$, uma $\alpha$ que dá $p$ (fecha com $\neg p$), e $p$ (fecha
logo com $\neg p$).

```{.tableau seq="((p -> q) -> p) -> p"}
~(((p -> q) -> p) -> p)
(p -> q) -> p        ; 1
~p                   ; 1
[
~(p -> q)            ; 2
p                    ; 4
~q                   ; 4
x                    ; 3, 5
|
p                    ; 2
x                    ; 3, 8
]
```

Tableau fechado para $\{\neg\phi\}$: $\phi$ é teorema. $\blacksquare$

## Aula 8 --- Resolução

### 2.18 --- Cláusulas e refutação

#### (a) Conjunto de cláusulas

Cada disjunção da FNC é uma cláusula (o conjunto dos seus literais):
$$\{\{p,\neg q,r\},\ \{\neg p\},\ \{p,q,r\},\ \{p,\neg r\}\}$$

#### (b) Dedução de $\mathbf{F}$ por resolução

Cláusulas 1--4 pela ordem de (a). A cláusula unitária $\{\neg p\}$ (2)
elimina $p$ das outras três; depois $q$ e $r$:

- 5: $\{\neg q,r\}$ de 1 e 2 (elimina $p$);
- 6: $\{q,r\}$ de 3 e 2 (elimina $p$);
- 7: $\{r\}$ de 5 e 6 (elimina $q$; $r\cup r = \{r\}$);
- 8: $\{\neg r\}$ de 4 e 2 (elimina $p$);
- 9: $\mathbf{F}$ de 7 e 8 (elimina $r$).

```{.resolucao}
{p, ~q, r}
{~p}
{p, q, r}
{p, ~r}
{~q, r}              ; 1, 2
{q, r}               ; 3, 2
{r}                  ; 5, 6
{~r}                 ; 4, 2
F                    ; 7, 8
```

Logo o conjunto (e a fórmula) é insatisfazível, pela integridade da
resolução. $\blacksquare$

### 2.19 --- Refutação

#### Resposta

Cláusulas 1 $\{\neg p,\neg q,r\}$, 2 $\{p,r\}$, 3 $\{q,r\}$, 4 $\{\neg r\}$.
A unitária $\{\neg r\}$ elimina $r$ das outras:

- 5: $\{\neg p,\neg q\}$ de 1 e 4;
- 6: $\{p\}$ de 2 e 4;
- 7: $\{q\}$ de 3 e 4;
- 8: $\{\neg q\}$ de 5 e 6 (elimina $p$);
- 9: $\mathbf{F}$ de 7 e 8 (elimina $q$).

```{.resolucao}
{~p, ~q, r}
{p, r}
{q, r}
{~r}
{~p, ~q}             ; 1, 4
{p}                  ; 2, 4
{q}                  ; 3, 4
{~q}                 ; 5, 6
F                    ; 7, 8
```

### 2.21 --- Tableau e resolução

#### (a) $(p\to q)\to((\neg p\to q)\to q)$

**Tableau.** As $\alpha$ dão $p\to q$, $\neg p\to q$ e $\neg q$. A $\beta$
do nó 2 abre $\neg p$ e $q$ (fecha com $\neg q$). Sob $\neg p$, a $\beta$
do nó 4 abre $\neg\neg p$, que fecha logo com $\neg p$ (são $\psi$ e
$\neg\psi$ com $\psi=\neg p$), e $q$ (fecha com $\neg q$).

```{.tableau seq="(p -> q) -> ((~p -> q) -> q)"}
~((p -> q) -> ((~p -> q) -> q))
p -> q               ; 1
~((~p -> q) -> q)    ; 1
~p -> q              ; 3
~q                   ; 3
[
~p                   ; 2
[
~~p                  ; 4
x                    ; 6, 7
|
q                    ; 4
x                    ; 5, 9
]
|
q                    ; 2
x                    ; 5, 11
]
```

**Resolução.** FNC de $\neg\phi$:
$$\begin{aligned}
\neg\phi &\Leftrightarrow (p\to q)\land\neg((\neg p\to q)\to q)
  && \neg(\phi'\to\psi')\Leftrightarrow\phi'\land\neg\psi'\\
&\Leftrightarrow (p\to q)\land(\neg p\to q)\land\neg q
  && \text{idem, associatividade}\\
&\Leftrightarrow (\neg p\lor q)\land(\neg\neg p\lor q)\land\neg q
  && \phi'\to\psi'\Leftrightarrow\neg\phi'\lor\psi'\\
&\Leftrightarrow (\neg p\lor q)\land(p\lor q)\land\neg q
  && \text{dupla negação}
\end{aligned}$$
Cláusulas 1 $\{\neg p,q\}$, 2 $\{p,q\}$, 3 $\{\neg q\}$. 4: $\{q\}$ de 1 e
2 (elimina $p$); 5: $\mathbf{F}$ de 4 e 3.

```{.resolucao de="(p -> q) -> ((~p -> q) -> q)"}
{~p, q}
{p, q}
{~q}
{q}                  ; 1, 2
F                    ; 4, 3
```

#### (b) $q\to(p\to(q\land p))$

**Tableau.** Duas $\alpha$ dão $q$, $p$ e $\neg(q\land p)$, uma $\beta$
que abre $\neg q$ (fecha com $q$) e $\neg p$ (fecha com $p$).

```{.tableau seq="q -> (p -> (q /\\ p))"}
~(q -> (p -> (q /\ p)))
q                    ; 1
~(p -> (q /\ p))     ; 1
p                    ; 3
~(q /\ p)            ; 3
[
~q                   ; 5
x                    ; 2, 6
|
~p                   ; 5
x                    ; 4, 8
]
```

**Resolução.** FNC de $\neg\phi$:
$$\begin{aligned}
\neg\phi &\Leftrightarrow q\land\neg(p\to(q\land p))
  && \neg(\phi'\to\psi')\Leftrightarrow\phi'\land\neg\psi'\\
&\Leftrightarrow q\land p\land\neg(q\land p)
  && \text{idem, associatividade}\\
&\Leftrightarrow q\land p\land(\neg q\lor\neg p)
  && \text{De Morgan}
\end{aligned}$$
Cláusulas 1 $\{q\}$, 2 $\{p\}$, 3 $\{\neg q,\neg p\}$. 4: $\{\neg p\}$ de 1
e 3 (elimina $q$); 5: $\mathbf{F}$ de 2 e 4.

```{.resolucao de="q -> (p -> (q /\\ p))"}
{q}
{p}
{~q, ~p}
{~p}                 ; 1, 3
F                    ; 2, 4
```

#### (c) $q\to(\neg p\to\neg(q\to p))$

**Tableau.** As $\alpha$ dão $q$, $\neg p$ e $\neg\neg(q\to p)$, que dá
$q\to p$. A $\beta$ abre $\neg q$ (fecha com $q$) e $p$ (fecha com
$\neg p$).

```{.tableau seq="q -> (~p -> ~(q -> p))"}
~(q -> (~p -> ~(q -> p)))
q                    ; 1
~(~p -> ~(q -> p))   ; 1
~p                   ; 3
~~(q -> p)           ; 3
q -> p               ; 5
[
~q                   ; 6
x                    ; 2, 7
|
p                    ; 6
x                    ; 4, 9
]
```

**Resolução.** FNC de $\neg\phi$:
$$\begin{aligned}
\neg\phi &\Leftrightarrow q\land\neg(\neg p\to\neg(q\to p))
  && \neg(\phi'\to\psi')\Leftrightarrow\phi'\land\neg\psi'\\
&\Leftrightarrow q\land\neg p\land\neg\neg(q\to p)
  && \text{idem, associatividade}\\
&\Leftrightarrow q\land\neg p\land(q\to p)
  && \text{dupla negação}\\
&\Leftrightarrow q\land\neg p\land(\neg q\lor p)
  && \phi'\to\psi'\Leftrightarrow\neg\phi'\lor\psi'
\end{aligned}$$
Cláusulas 1 $\{q\}$, 2 $\{\neg p\}$, 3 $\{\neg q,p\}$. 4: $\{p\}$ de 1 e 3
(elimina $q$); 5: $\mathbf{F}$ de 2 e 4.

```{.resolucao de="q -> (~p -> ~(q -> p))"}
{q}
{~p}
{~q, p}
{p}                  ; 1, 3
F                    ; 2, 4
```

## Aulas 9--10 --- Integridade

### A9.11 --- Não dedutibilidade (Aulas 9--10, slide 11)

#### Resposta

Seja $v(p)=V$, $v(q)=V$. De $\models_v p$ segue $\models_v q\to p$, logo
$\models_v \neg p\lor(q\to p)$. De $\models_v p$ segue $\not\models_v \neg p$,
logo $\not\models_v \neg p\land q$. Portanto
$\neg p\lor(q\to p) \not\models \neg p\land q$ e, pela integridade de DN,
$\neg p\lor(q\to p) \nvdash \neg p\land q$.

## Aulas 9--10 --- Completude

### A9.20 --- Os casos do Lema 1 (Aulas 9--10, slides 20--22)

#### (a) $\neg\phi_1\land\neg\phi_2 \vdash \phi_1\to\phi_2$

Supõe-se $\phi_1$; com $\neg\phi_1$ chega-se a $\mathbf{F}$ e daí a
qualquer fórmula.

```{.fitch seq="~phi1 /\ ~phi2 |- phi1 -> phi2"}
~phi1 /\ ~phi2
---
|> phi1
|  ~phi1             ; &E, 1
|  F                 ; FI, 2, 3
|  phi2              ; FE, 4
phi1 -> phi2         ; ->I, 2-5
```

#### (b) $\neg\phi_1\land\phi_2 \vdash \neg(\phi_1\land\phi_2)$

```{.fitch seq="~phi1 /\ phi2 |- ~(phi1 /\ phi2)"}
~phi1 /\ phi2
---
|> phi1 /\ phi2
|  phi1              ; &E, 2
|  ~phi1             ; &E, 1
|  F                 ; FI, 3, 4
~(phi1 /\ phi2)      ; ~I, 2-5
```

#### (c) $\neg\phi_1\land\neg\phi_2 \vdash \neg(\phi_1\lor\phi_2)$

Supõe-se a disjunção e cada caso do $\lor$E dá $\mathbf{F}$.

```{.fitch seq="~phi1 /\ ~phi2 |- ~(phi1 \/ phi2)"}
~phi1 /\ ~phi2
---
|> phi1 \/ phi2
||> phi1
||  ~phi1            ; &E, 1
||  F                ; FI, 3, 4
||> phi2
||  ~phi2            ; &E, 1
||  F                ; FI, 6, 7
|  F                 ; vE, 2, 3-5, 6-8
~(phi1 \/ phi2)      ; ~I, 2-9
```

#### (d) $\neg\phi_1\land\phi_2 \vdash \phi_1\lor\phi_2$

```{.fitch seq="~phi1 /\ phi2 |- phi1 \/ phi2"}
~phi1 /\ phi2
---
phi2                 ; &E, 1
phi1 \/ phi2         ; vI, 2
```
