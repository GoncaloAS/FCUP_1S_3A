---
title: "Lógica Computacional --- Teste de treino 1: resolução"
subtitle: "Cada alínea: a resposta, como se chega lá e o que escrever no teste."
---

## 1. Escolha múltipla

### (a) $(p \land \neg q) \to (q \lor \neg p)$ --- **C** (satisfazível, mas não tautologia)

**Como pensar.** Uma implicação só é falsa com **V → F**. Procura-se esse caso:

- antecedente $p \land \neg q$ V obriga a $p = V$ e $q = F$;
- aí o consequente é $q \lor \neg p = F \lor F = F$, logo a fórmula é **F**.

Há uma valoração que a torna falsa (não é tautologia) e qualquer valoração
com $p = F$ torna o antecedente F e a fórmula V (não é contradição).

**Justificação.** Com $v(p)=V$, $v(q)=F$: $\models_v p\land\neg q$ e
$\nmodels_v q\lor\neg p$, logo $\nmodels_v$ da fórmula. Com $v'(p)=F$:
$\nmodels_{v'} p\land\neg q$, logo $\models_{v'}$ da fórmula.

### (b) A falsa é a **C**

**A. $\phi \to \psi,\ \neg\psi \lor \theta,\ \phi \models \theta$ --- verdadeira.**
Seja $v$ com as três premissas V. De $\models_v \phi$ e $\models_v \phi\to\psi$
tem-se $\models_v \psi$, logo $\nmodels_v \neg\psi$. Como
$\models_v \neg\psi\lor\theta$ e o lado esquerdo é F, $\models_v \theta$.
*Em português:* $\phi$ dá $\psi$; "não $\psi$ ou $\theta$" com $\psi$
verdadeiro só deixa $\theta$.

**B. $\models (\phi\land\neg\phi)\to\psi$ --- verdadeira.** Para qualquer $v$,
$\nmodels_v \phi\land\neg\phi$ (era preciso $\phi$ V e F ao mesmo tempo); uma
implicação com antecedente F é V. Logo é tautologia.

**C. $\phi\lor\psi,\ \phi\to\theta \models \theta$ --- falsa.** O
$\phi\to\theta$ só ajuda no caso $\phi$; no caso $\psi$ nada obriga $\theta$.
**Contraexemplo:** $\phi = p$, $\psi = q$, $\theta = r$ e $v(p)=F$,
$v(q)=V$, $v(r)=F$. Então $\models_v p\lor q$ (por $q$), $\models_v p\to r$
(antecedente F), mas $\nmodels_v r$.

### (c) **A** --- cavaleiro da noite, e é de dia

**Como pensar.** Há quatro combinações. Um habitante diz a verdade quando é
(do dia **e** é dia) ou (da noite **e** é noite). A frase é
$S$ = "é de noite **e** sou do dia". Testa-se cada caso: quem diz a verdade
tem de ter $S$ verdadeira; quem mente tem de ter $S$ falsa.

| tipo | hora | diz a verdade? | $S$ = noite ∧ do dia | coerente? |
|---|---|---|---|---|
| do dia | dia | sim | F (não é noite) | $\times$ (diria a verdade com $S$ falsa) |
| do dia | noite | não | V | $\times$ (mentiria com $S$ verdadeira) |
| da noite | dia | não | F | $\checkmark$ |
| da noite | noite | sim | F (não é do dia) | $\times$ |

Só sobra **cavaleiro da noite, de dia** (a opção A), e como é a única, o
visitante fica a saber as duas coisas.

### (d) **C** --- $\Sigma \cup \Gamma \vdash \phi \to \psi$ não é necessariamente verdadeira

Junta-se tudo: de $\Sigma\cup\Gamma$ deduz-se $\phi$ e $\neg\psi$ (mais
premissas nunca tiram conclusões).

- **A** é verdadeira: abre-se a hipótese $\psi$, repete-se $\phi$ (R) e
  fecha-se com →I: $\psi\to\phi$.
- **B** é verdadeira: $\land$I com $\phi$ e $\neg\psi$.
- **C** pode falhar. **Contraexemplo:** $\Sigma=\{p\}$, $\phi=p$,
  $\Gamma=\{\neg q\}$, $\psi=q$. Então $\Sigma\cup\Gamma=\{p,\neg q\}$; com
  $v(p)=V$, $v(q)=F$ as premissas são V e $p\to q$ é F, logo
  $\{p,\neg q\}\nmodels p\to q$ e, pela integridade, $\{p,\neg q\}\nvdash p\to q$.

*Em português:* tens $\phi$ verdadeiro e $\psi$ falso, por isso
"se $\phi$ então $\psi$" é exatamente V → F.

## 2. Completar deduções

### Esquerda

```{.fitch seq="(phi \/ psi) -> theta |- ~theta -> ~phi"}
(phi \/ psi) -> theta
---
|> ~theta
||> phi
||  phi \/ psi        ; vI, 3
||  theta             ; ->E, 1, 4
||  F                 ; FI, 5, 2
|  ~phi               ; ~I, 3-6
~theta -> ~phi        ; ->I, 2-7
```

**Como descobrir cada buraco (de trás para a frente):**

1. **Linha 8** é $\neg\theta\to\neg\phi$ fora das caixas: fecha a caixa que
   começa no 2 ($\neg\theta$) e acaba no 7, logo é **→I, 2--7** e a linha 7
   tem de ser $\neg\phi$.
2. **Linha 7** $= \neg\phi$ vem de **¬I, 3--6**: "imaginei a linha 3 e deu
   F", logo a **linha 3 é $\phi$**.
3. **Linha 6** é F: há $\theta$ (5) e $\neg\theta$ (2), logo **FI, 5, 2**.
4. **Linha 1**: a linha 5 diz **→E, 1, 4**, ou seja, $\theta$ sai da
   linha 1 com a linha 4 ($\phi\lor\psi$). O →E tira o lado direito de
   uma implicação quando se tem o lado esquerdo, por isso a linha 1 é
   (linha 4) → (linha 5), isto é, **$(\phi\lor\psi)\to\theta$**. A seta
   vai do que já tens ($\phi\lor\psi$) para o que ganhas ($\theta$).

### Direita (é a lei de De Morgan $\neg(\phi\lor\psi)\vdash\neg\phi\land\neg\psi$)

```{.fitch seq="~(phi \/ psi) |- ~phi /\ ~psi"}
~(phi \/ psi)
---
|> phi
|  phi \/ psi        ; vI, 2
|  F                 ; FI, 3, 1
~phi                 ; ~I, 2-4
|> psi
|  phi \/ psi        ; vI, 6
|  F                 ; FI, 7, 1
~psi                 ; ~I, 6-8
~phi /\ ~psi         ; &I, 5, 9
```

**Como reconhecer as regras pela forma das linhas:**

- linha que começa uma caixa → **hipótese** (não leva regra);
- de $\phi$ para $\phi\lor\psi$ → **∨I**;
- F logo a seguir a uma fórmula que é a negação de outra (aqui
  $\phi\lor\psi$ e a premissa $\neg(\phi\lor\psi)$) → **FI**;
- negação da hipótese, um nível à esquerda, depois de uma caixa que acaba
  em F → **¬I** com o intervalo da caixa;
- juntar duas linhas com ∧ → **∧I**, pela ordem: $\neg\phi$ (5) à esquerda,
  $\neg\psi$ (9) à direita.

## 3. Respostas curtas

### (a) $v\big((p \lor q) \to (r \land \neg p)\big) = F$

$p\lor q = V\lor F = V$; $\neg p = F$; $r\land\neg p = V\land F = F$;
$V \to F = F$.

### (b) FND: $(p \land \neg q) \lor (\neg p \land q)$

**FND** = disjunção (∨ fora) de conjunções (∧ dentro), **uma por cada linha
em que γ é V**, com as letras **iguais** à linha (V → $p$, F → $\neg p$):

- linha 2 ($p=V$, $q=F$) dá $p\land\neg q$;
- linha 3 ($p=F$, $q=V$) dá $\neg p\land q$.

Confirmação: na linha 2, $p\land\neg q = V$ $\checkmark$; na linha 1 ($p=q=V$) ambas
dão F $\checkmark$.

### (c) FNN: $p \land q \land (\neg r \lor p)$

Empurram-se os ¬ para dentro, de fora para dentro:

$$
\begin{aligned}
&\neg\big((p \to \neg q) \lor (r \land \neg p)\big)\\
\Leftrightarrow\ & \neg(p \to \neg q) \land \neg(r \land \neg p) && \text{(De Morgan)}\\
\Leftrightarrow\ & (p \land \neg\neg q) \land (\neg r \lor \neg\neg p) && (\neg(A\to B)\Leftrightarrow A\land\neg B\text{; De Morgan})\\
\Leftrightarrow\ & p \land q \land (\neg r \lor p) && \text{(dupla negação, 2 vezes)}
\end{aligned}
$$

Os ¬ só ficam colados a letras: está em FNN.

### (d) $\{q, r\}$, $\{p, \neg r\}$ e $\{\neg p, \neg q\}$

Numeram-se $1=\{p,q\}$, $2=\{\neg p,r\}$, $3=\{\neg q,\neg r\}$ e testam-se
os três pares, procurando uma letra com sinais opostos:

| par | elimina | resolvente |
|---|---|---|
| 1 e 2 | $p$ | $\{q, r\}$ |
| 1 e 3 | $q$ | $\{p, \neg r\}$ |
| 2 e 3 | $r$ | $\{\neg p, \neg q\}$ |

Nenhuma já existia, logo as três são novas. (Cada par tinha só uma letra
oposta; se tivesse duas, davam duas resolventes, uma por letra, e nunca F.)

### (e) É uma fórmula **β** (disjuntiva), com componentes $\neg(\neg p \to q)$ e $\neg(r \lor p)$

A seta principal é a do meio, **sem ¬ à frente**: $A \to B$ é β e divide em
$\neg A \mid B$, com $A = \neg p\to q$ e $B = \neg(r\lor p)$. Atenção: o
$\neg A$ é **$\neg(\neg p\to q)$** (nega-se o antecedente inteiro) e o
$B$ fica tal e qual.

### (f) $v(p)=F$, $v(q)=F$, $v(r)=V$

Começa-se pela conclusão a **F**: $r\to p$ é F só com $r=V$, $p=F$. A
premissa $\neg q$ obriga $q=F$. Verifica-se a outra premissa:
$p\to(q\lor r)$ com $p=F$ é V. Premissas V, conclusão F $\checkmark$.

## 4. Davis-Putnam (DLL)

Seja
$S = \{p \lor q \lor \neg r,\ \neg p \lor q,\ \neg q \lor r,\ \neg p \lor \neg r,\ p \lor r,\ \neg q \lor \neg r \lor s\}$.

**Lembrete.** Propagar um literal $l$: saem as cláusulas que têm $l$ (já
são V); nas que têm o contrário de $l$, tira-se esse literal (é F e não
ajuda). Cláusula vazia (F) = escolha falhada; conjunto vazio = satisfazível.

Não há cláusulas unitárias, por isso escolhe-se um literal: $p$, e chama-se
DLL$(S\cup\{p\})$.

**Ramo $p$.** Propagando $p$: saem $p\lor q\lor\neg r$ e $p\lor r$;
$\neg p\lor q$ fica $q$; $\neg p\lor\neg r$ fica $\neg r$:
$$S_1 = \{q,\ \neg q \lor r,\ \neg r,\ \neg q \lor \neg r \lor s\}$$
Propagando $q$ (unitária): $\neg q\lor r$ fica $r$; $\neg q\lor\neg r\lor s$
fica $\neg r\lor s$:
$$S_2 = \{r,\ \neg r,\ \neg r \lor s\}$$
Propagando $r$: $\neg r$ perde o único literal e fica **vazia**, obtém-se
$\{\mathbf{F}, s\}$, que contém F. **Falhou.**

**Ramo $\neg p$.** Volta-se ao último ponto de escolha e chama-se
DLL$(S\cup\{\neg p\})$. Propagando $\neg p$: saem $\neg p\lor q$ e
$\neg p\lor\neg r$; $p\lor q\lor\neg r$ fica $q\lor\neg r$; $p\lor r$ fica $r$:
$$S_3 = \{q \lor \neg r,\ \neg q \lor r,\ r,\ \neg q \lor \neg r \lor s\}$$
Propagando $r$: saem $\neg q\lor r$ e $r$; $q\lor\neg r$ fica $q$;
$\neg q\lor\neg r\lor s$ fica $\neg q\lor s$:
$$S_4 = \{q,\ \neg q \lor s\}$$
Propagando $q$: $S_5 = \{s\}$. Propagando $s$: $\{\ \}$, o **conjunto
vazio**.

**Conclusão:** o conjunto é **satisfazível**, para $v(p)=F$, $v(r)=V$,
$v(q)=V$, $v(s)=V$.

*Verificação:* $p\lor q\lor\neg r$ (q $\checkmark$), $\neg p\lor q$ $\checkmark$, $\neg q\lor r$
(r $\checkmark$), $\neg p\lor\neg r$ ($\neg p$ $\checkmark$), $p\lor r$ (r $\checkmark$),
$\neg q\lor\neg r\lor s$ (s $\checkmark$).

Nota: no ramo $p$, o $q$ e o $r$ foram **propagados** (estavam sozinhos), não
escolhidos, por isso não há ramo "$\neg q$" a testar. Só o $p$ foi escolha.

## 5. A mesma fórmula por dedução natural e por tableau

### a) Dedução natural

**Como começar.** Sem premissas, o início sai da conclusão. A seta
principal é a do meio: $A \to B$ com $A = p\to(q\to r)$, por isso
**imagina-se $A$**. O $B = (p\land q)\to r$ é outra implicação: **imagina-se
$p\land q$** e o objetivo passa a ser **$r$**.

**O meio.** $r$ aparece em $q\to r$, que sai de $p\to(q\to r)$ com $p$; o
$p$ e o $q$ saem de $p\land q$ por ∧E.

```{.fitch seq="|- (p -> (q -> r)) -> ((p /\ q) -> r)"}
|> p -> (q -> r)
||> p /\ q
||  p                 ; &E, 2
||  q                 ; &E, 2
||  q -> r            ; ->E, 1, 3
||  r                 ; ->E, 5, 4
|  (p /\ q) -> r      ; ->I, 2-6
(p -> (q -> r)) -> ((p /\ q) -> r)   ; ->I, 1-7
```

### b) Tableau

**Receita.** Raiz $\neg\phi$; primeiro as α (não dividem) e os ¬¬, as β no
fim; fecha-se um ramo com uma fórmula e a sua negação no caminho até à raiz.

- Nó 1 é $\neg(A\to B)$: **α**, dá $A$ (nó 2) e $\neg B$ (nó 3).
- Nó 3 é $\neg((p\land q)\to r)$: **α**, dá $p\land q$ (4) e $\neg r$ (5).
- Nó 4 é $p\land q$: **α**, dá $p$ (6) e $q$ (7).
- Só sobra o nó 2, $p\to(q\to r)$: **β**, divide em $\neg p$ | $q\to r$.
  - $\neg p$ fecha com $p$ (6).
  - $q\to r$ é outra **β**: $\neg q$ fecha com $q$ (7); $r$ fecha com $\neg r$ (5).

```{.tableau seq="(p -> (q -> r)) -> ((p /\\ q) -> r)"}
~((p -> (q -> r)) -> ((p /\ q) -> r))
p -> (q -> r)        ; 1
~((p /\ q) -> r)     ; 1
p /\ q               ; 3
~r                   ; 3
p                    ; 4
q                    ; 4
[
~p                   ; 2
x                    ; 6, 8
|
q -> r               ; 2
[
~q                   ; 10
x                    ; 7, 11
|
r                    ; 10
x                    ; 5, 13
]
]
```

Todos os ramos fechados: tableau fechado para $\{\neg\phi\}$, logo $\phi$ é
teorema.

## 6. Dedução com uma disjunção nas premissas

$$(\phi \to \gamma) \lor (\neg\psi \to \neg\phi),\ \ \gamma \to \neg\delta \ \vdash\ \phi \to (\neg\delta \lor \psi)$$

**Em português.** Suponha-se $\phi$. Ou "$\phi$ dá $\gamma$", e então
$\gamma$ dá $\neg\delta$; ou "$\neg\psi$ dá $\neg\phi$", e como temos $\phi$,
o $\psi$ não pode ser falso. Num caso temos $\neg\delta$, no outro $\psi$:
nos dois, $\neg\delta\lor\psi$.

**Plano (as 4 perguntas):**

1. *A conclusão é →?* Sim: hipótese **$\phi$**, objetivo **$\neg\delta\lor\psi$**, no fim →I.
2. *Há um ∨ nas premissas?* Sim, a 1: **∨E**, uma caixa por caso, as duas a
   acabar em $\neg\delta\lor\psi$.
3. *Caso $\phi\to\gamma$:* fala de $\gamma$, e a premissa 2 liga $\gamma$ a
   $\delta$, por isso o lado a provar é **$\neg\delta$** (direto: dois →E).
4. *Caso $\neg\psi\to\neg\phi$:* fala de $\psi$, por isso o lado a provar é
   **$\psi$**. Não há caminho direto, logo **por absurdo**: hipótese
   $\neg\psi$ (o contrário do que se quer), dá $\neg\phi$, que choca com
   $\phi$; ¬I dá $\neg\neg\psi$ e ¬E dá $\psi$.

```{.fitch seq="(phi -> gamma) \/ (~psi -> ~phi), gamma -> ~delta |- phi -> (~delta \/ psi)"}
(phi -> gamma) \/ (~psi -> ~phi)
gamma -> ~delta
---
|> phi
||> phi -> gamma
||  gamma                 ; ->E, 4, 3
||  ~delta                ; ->E, 2, 5
||  ~delta \/ psi         ; vI, 6
||> ~psi -> ~phi
|||> ~psi
|||  ~phi                 ; ->E, 8, 9
|||  F                    ; FI, 3, 10
||  ~~psi                 ; ~I, 9-11
||  psi                   ; ~E, 12
||  ~delta \/ psi         ; vI, 13
|  ~delta \/ psi          ; vE, 1, 4-7, 8-14
phi -> (~delta \/ psi)    ; ->I, 3-15
```

**O que reparar:**

- a hipótese $\phi$ (linha 3) é usada **dentro** das caixas dos dois casos
  (linhas 6 e 11): está numa caixa de fora ainda aberta, pode citar-se;
- as duas caixas do ∨E acabam **exatamente** na mesma fórmula
  ($\neg\delta\lor\psi$, linhas 7 e 14), por isso o ∨I no fim de cada uma;
- no caso 2, a hipótese aberta foi **$\neg\psi$**, o contrário do que se
  queria ($\psi$), porque só assim o ¬I devolve $\neg\neg\psi$.

**Com regras derivadas (opcional).** As linhas 9--13 trocam-se por três:
$\neg\neg\phi$ (¬¬I, 3), $\neg\neg\psi$ (MT com a linha 8 e a anterior) e
$\psi$ (¬E). Mas então o teste pede também as provas da MT e da ¬¬I, e
acabas a escrever mais. A versão sem regras derivadas é a mais segura.

# Parte extra

## E1. Forma normal conjuntiva

### (a) $(\neg p \lor \neg q \lor r) \land (p \lor \neg q \lor \neg r)$

**FNC** = conjunção (∧ fora) de disjunções (∨ dentro), **uma por cada linha
em que γ é F**, com as letras **trocadas** (V → $\neg p$, F → $p$). Cada
cláusula tem de dar F exatamente nessa linha, e um ∨ só é F com todos os
literais F.

- linha 2 ($p=V$, $q=V$, $r=F$) dá $\neg p\lor\neg q\lor r$;
- linha 5 ($p=F$, $q=V$, $r=V$) dá $p\lor\neg q\lor\neg r$.

Confirmação na linha 2: $\neg p\lor\neg q\lor r = F\lor F\lor F = F$
$\checkmark$. Num atalho de memória: **FND usa as linhas V e copia as letras;
FNC usa as linhas F e troca-as.**

### (b) $(p \lor r) \land (\neg q \lor r) \land (\neg p \lor \neg q)$

$$
\begin{aligned}
&(p \to q) \to (r \land \neg p)\\
\Leftrightarrow\ & \neg(\neg p \lor q) \lor (r \land \neg p) && \text{(implicação, 2 vezes)}\\
\Leftrightarrow\ & (\neg\neg p \land \neg q) \lor (r \land \neg p) && \text{(De Morgan)}\\
\Leftrightarrow\ & (p \land \neg q) \lor (r \land \neg p) && \text{(dupla negação; já é uma FND)}\\
\Leftrightarrow\ & (p \lor r) \land (p \lor \neg p) \land (\neg q \lor r) \land (\neg q \lor \neg p) && \text{(distributividade, 2 vezes)}\\
\Leftrightarrow\ & (p \lor r) \land (\neg q \lor r) \land (\neg p \lor \neg q) && (p\lor\neg p \Leftrightarrow \mathbf{V}\text{; } \mathbf{V}\land A \Leftrightarrow A\text{; comutatividade})
\end{aligned}
$$

**A passagem FND → FNC** é "multiplicar os parênteses": em
$(A \land B) \lor (C \land D)$ junta-se cada literal do primeiro com cada
literal do segundo, $(A\lor C)\land(A\lor D)\land(B\lor C)\land(B\lor D)$.
Aqui $A=p$, $B=\neg q$, $C=r$, $D=\neg p$. Uma cláusula com uma letra e a
sua negação ($p\lor\neg p$) é sempre V e pode tirar-se.

## E2. Dedução por resolução

**Três passos:** negar a fórmula, pô-la em FNC, refutar as cláusulas.

**1. FNC de $\neg\phi$:**

$$
\begin{aligned}
&\neg\Big(\big((p \lor q) \land (p \to r) \land (q \to r)\big) \to r\Big)\\
\Leftrightarrow\ & (p \lor q) \land (p \to r) \land (q \to r) \land \neg r && (\neg(A\to B)\Leftrightarrow A\land\neg B)\\
\Leftrightarrow\ & (p \lor q) \land (\neg p \lor r) \land (\neg q \lor r) \land \neg r && \text{(implicação, 2 vezes)}
\end{aligned}
$$

**2. Cláusulas:** $1=\{p,q\}$, $2=\{\neg p,r\}$, $3=\{\neg q,r\}$,
$4=\{\neg r\}$.

**3. Refutação**, começando pela unitária $\{\neg r\}$, que corta o $r$:

- 5: $\{\neg p\}$ de 2 e 4 (elimina $r$);
- 6: $\{\neg q\}$ de 3 e 4 (elimina $r$);
- 7: $\{q\}$ de 1 e 5 (elimina $p$);
- 8: $\mathbf{F}$ de 7 e 6 (elimina $q$).

```{.resolucao de="((p \\/ q) /\\ (p -> r) /\\ (q -> r)) -> r"}
{p, q}
{~p, r}
{~q, r}
{~r}
{~p}                 ; 2, 4
{~q}                 ; 3, 4
{q}                  ; 1, 5
F                    ; 7, 6
```

Chegou-se a F: $\neg\phi$ é insatisfazível e $\phi$ é teorema. *Em
português:* sem $r$, nem $p$ nem $q$ podem ser V (cada um daria $r$), mas
um deles tem de ser.

## E3. Algoritmo de Horn

Cada cláusula lida como implicação:

| cláusula | lê-se | tipo |
|---|---|---|
| $\neg p\lor\neg q\lor r$ | $(p\land q)\to r$ | regra |
| $p$ | $p$ tem de ser V | facto |
| $\neg p\lor q$ | $p\to q$ | regra |
| $\neg r\lor s$ | $r\to s$ | regra |
| $\neg s\lor\neg q$ | $(s\land q)\to\mathbf{F}$ | restrição |

**Propagação** (só se põe V quando é obrigatório):

| passo | $p$ | $q$ | $r$ | $s$ | porquê |
|:-:|:-:|:-:|:-:|:-:|---|
| 1 | V | | | | $p$ é facto |
| 2 | V | V | | | em $\neg p\lor q$ o $\neg p$ é F, logo $q$ tem de ser V |
| 3 | V | V | V | | em $\neg p\lor\neg q\lor r$ os dois negativos são F, logo $r$ |
| 4 | V | V | V | V | em $\neg r\lor s$ o $\neg r$ é F, logo $s$ |
| 5 | V | V | V | V | em $\neg s\lor\neg q$ os dois literais são F: a cláusula fica **F** |

**Não é satisfazível.** Todos os V foram obrigatórios, por isso nenhuma
valoração escapa à cláusula $\neg s\lor\neg q$.

## E4. Tableau aberto

```{.tableau .aberto}
~((p -> q) -> (q -> p))
p -> q               ; 1
~(q -> p)            ; 1
q                    ; 3
~p                   ; 3
[
~p                   ; 2
|
q                    ; 2
]
```

- Nó 1, $\neg(A\to B)$: **α**, dá $p\to q$ (2) e $\neg(q\to p)$ (3).
- Nó 3, outra **α**: dá $q$ (4) e $\neg p$ (5).
- Nó 2, $p\to q$: **β**, divide em $\neg p$ | $q$. Nenhum dos ramos tem uma
  fórmula e a sua negação: ficam os dois **abertos**.

**Não é tautologia.** Um ramo aberto com tudo expandido dá a valoração:
$v(p)=F$, $v(q)=V$. Verificação: $p\to q = V$, $q\to p = V\to F = F$, logo
$(p\to q)\to(q\to p) = V\to F = F$ $\checkmark$.

## E5. $\{\neg, \to\}$ é completo

**Ideia:** $\{\neg,\land,\lor\}$ é completo (toda a função de verdade tem uma
FND). Basta escrever $\land$ e $\lor$ só com $\neg$ e $\to$:

- $p \lor q \Leftrightarrow \neg p \to q$, porque
  $\neg p\to q \Leftrightarrow \neg\neg p\lor q \Leftrightarrow p\lor q$
  (implicação; dupla negação);
- $p \land q \Leftrightarrow \neg(p \to \neg q)$, porque
  $\neg(p\to\neg q) \Leftrightarrow p\land\neg\neg q \Leftrightarrow p\land q$
  ($\neg(A\to B)\Leftrightarrow A\land\neg B$; dupla negação).

Substituindo numa FND cada $\land$ e $\lor$ por estas fórmulas, obtém-se uma
fórmula equivalente só com $\neg$ e $\to$. Logo $\{\neg,\to\}$ é completo.

## E6. Verdadeiro ou falso

### (a) Verdadeiro

**Ideia:** é a prova por absurdo. Se juntar $\neg\phi$ a $\Sigma$ dá F,
então dentro de uma dedução a partir de $\Sigma$ abre-se a hipótese
$\neg\phi$, repete-se essa dedução até F, e fecha-se:

```{.fitch .nocheck}
\Sigma
---
|> ~phi
|  ...
|  F                 ; dedução de $\Sigma\cup\{\neg\phi\}\vdash\mathbf{F}$
~~phi                ; ~I
phi                  ; ~E
```

As fórmulas de $\Sigma$ podem citar-se dentro da caixa (estão fora e
abertas), e o $\neg\phi$ é a hipótese. Logo $\Sigma\vdash\phi$.

### (b) Falso

É a 1.16 (c) com $\vdash$. **Contraexemplo:** $\Sigma=\{p,\ p\to q\}$,
$\Gamma=\{q\}$, $\phi=q$. Tem-se $\Sigma\vdash q$ (→E) e $\Gamma\vdash q$
(é premissa), mas $\Sigma\cap\Gamma=\emptyset$ e $\nvdash q$: pela
integridade, se $\vdash q$ então $\models q$, e $q$ não é tautologia
($v(q)=F$).

### (c) Falso: o conjunto é inconsistente

Deduz-se F a partir dele:

```{.fitch seq="p -> q, q -> r, p, ~r |- F"}
p -> q
q -> r
p
~r
---
q                    ; ->E, 1, 3
r                    ; ->E, 2, 5
F                    ; FI, 6, 4
```

*Em português:* $p$ dá $q$, $q$ dá $r$, mas temos $\neg r$. (Também se vê
semanticamente: nenhuma valoração satisfaz o conjunto, e consistente =
satisfazível, pela integridade e completude.)
