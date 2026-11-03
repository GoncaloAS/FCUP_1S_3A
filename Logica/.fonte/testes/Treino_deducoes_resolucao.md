---
title: "Lógica Computacional --- Treino de deduções: resolução"
subtitle: "Para cada uma: o padrão, o plano e a dedução verificada."
---

## Tabela de decisão

| o que vês | o que fazes |
|---|---|
| conclusão $A \to B$ | hipótese $A$, chegar a $B$, →I |
| conclusão $\neg A$ | hipótese $A$, chegar a F, ¬I |
| conclusão $A \land B$ | provar $A$ e $B$ à parte, ∧I |
| conclusão $A \lor B$ e um dos lados sai direto | provar esse lado, ∨I |
| conclusão $A \lor B$ e nenhum sai direto | **absurdo**: hipótese $\neg(A\lor B)$, chegar a F, ¬I, ¬E |
| conclusão positiva $A$ sem caminho direto | **absurdo**: hipótese $\neg A$, chegar a F, ¬I, ¬E |
| premissa $A \lor B$ | ∨E: uma caixa por caso, as duas no mesmo objetivo |
| premissa $A \land B$ | ∧E logo no início |
| premissa $A \to B$ | arranjar $A$ e fazer →E |
| premissa $\neg A$ | só serve para FI: arranjar $A$ |
| num caso, o objetivo não aparece em lado nenhum | chegar a F e usar **FE** |

## D1. $\neg(\phi \land \psi) \vdash \neg\phi \lor \neg\psi$ --- conclusão ∨ por absurdo

**Plano.** Nem $\neg\phi$ nem $\neg\psi$ saem sozinhos da premissa, por isso
não dá para usar ∨I diretamente: **absurdo**. Imagina-se
$\neg(\neg\phi\lor\neg\psi)$ e procura-se F. A premissa é uma negação, só
serve para FI, por isso o objetivo passa a ser **$\phi\land\psi$**. Para ter
$\phi$: outra vez por absurdo (imagina $\neg\phi$, dá $\neg\phi\lor\neg\psi$,
choca com a linha 2). O mesmo para $\psi$.

```{.fitch seq="~(phi /\ psi) |- ~phi \/ ~psi"}
~(phi /\ psi)
---
|> ~(~phi \/ ~psi)
||> ~phi
||  ~phi \/ ~psi        ; vI, 3
||  F                   ; FI, 4, 2
|  ~~phi                ; ~I, 3-5
|  phi                  ; ~E, 6
||> ~psi
||  ~phi \/ ~psi        ; vI, 8
||  F                   ; FI, 9, 2
|  ~~psi                ; ~I, 8-10
|  psi                  ; ~E, 11
|  phi /\ psi           ; &I, 7, 12
|  F                    ; FI, 13, 1
~~(~phi \/ ~psi)        ; ~I, 2-14
~phi \/ ~psi            ; ~E, 15
```

**O que reparar:** é a dedução mais comprida deste tipo (De Morgan "difícil").
A hipótese $\neg(\neg\phi\lor\neg\psi)$ é usada **duas vezes** para FI.

## D2. $(\phi \land \psi) \to \theta,\ \neg\theta,\ \phi \vdash \neg\psi$ --- conclusão ¬

**Plano.** Conclusão $\neg\psi$: imagina $\psi$ e procura F. Com $\phi$ e
$\psi$ faz-se $\phi\land\psi$, a premissa 1 dá $\theta$, que choca com
$\neg\theta$.

```{.fitch seq="(phi /\ psi) -> theta, ~theta, phi |- ~psi"}
(phi /\ psi) -> theta
~theta
phi
---
|> psi
|  phi /\ psi           ; &I, 3, 4
|  theta                ; ->E, 1, 5
|  F                    ; FI, 6, 2
~psi                    ; ~I, 4-7
```

## D3. $\neg\phi \to \psi,\ \psi \to \theta,\ \neg\theta \vdash \phi$ --- conclusão positiva por absurdo

**Plano.** $\phi$ não aparece sozinho em lado nenhum (só $\neg\phi$, na
premissa 1). Quando só tens o contrário do que queres: **imagina o
contrário**, $\neg\phi$, e chega a F. Aí a cadeia é direta:
$\neg\phi \Rightarrow \psi \Rightarrow \theta$, que choca com $\neg\theta$.

```{.fitch seq="~phi -> psi, psi -> theta, ~theta |- phi"}
~phi -> psi
psi -> theta
~theta
---
|> ~phi
|  psi                  ; ->E, 1, 4
|  theta                ; ->E, 2, 5
|  F                    ; FI, 6, 3
~~phi                   ; ~I, 4-7
phi                     ; ~E, 8
```

**O que reparar:** o fim é sempre o mesmo par, **¬I** (dá $\neg\neg\phi$) e
**¬E** (dá $\phi$).

## D4. $\phi \lor \psi,\ \neg\phi \vdash \psi$ --- FE num caso

**Plano.** Premissa com ∨: dois casos, os dois a acabar em $\psi$. No caso
$\psi$ já está (R). No caso $\phi$, o $\psi$ não aparece em lado nenhum,
mas $\phi$ choca com $\neg\phi$: F, e do absurdo tira-se $\psi$ (**FE**).

```{.fitch seq="phi \/ psi, ~phi |- psi"}
phi \/ psi
~phi
---
|> phi
|  F                    ; FI, 3, 2
|  psi                  ; FE, 4
|> psi
|  psi                  ; R, 6
psi                     ; vE, 1, 3-5, 6-7
```

**O que reparar:** é o "silogismo disjuntivo" ("ou A ou B; não A; logo B").
Aparece muitas vezes **dentro** de deduções maiores.

## D5. $\neg(\phi \to \psi) \vdash \phi \land \neg\psi$ --- premissa negada

**Plano.** A conclusão é ∧: provar $\phi$ e $\neg\psi$ à parte. A premissa
é uma negação, só serve para FI: em cada parte, o objetivo é construir
**$\phi\to\psi$** para chocar com ela.

- **$\phi$:** por absurdo, imagina $\neg\phi$. Para ter $\phi\to\psi$,
  imagina $\phi$: choca com $\neg\phi$, e por FE sai $\psi$.
- **$\neg\psi$:** imagina $\psi$. Para ter $\phi\to\psi$, imagina $\phi$ e
  repete $\psi$ (R).

```{.fitch seq="~(phi -> psi) |- phi /\ ~psi"}
~(phi -> psi)
---
|> ~phi
||> phi
||  F                   ; FI, 3, 2
||  psi                 ; FE, 4
|  phi -> psi           ; ->I, 3-5
|  F                    ; FI, 6, 1
~~phi                   ; ~I, 2-7
phi                     ; ~E, 8
|> psi
||> phi
||  psi                 ; R, 10
|  phi -> psi           ; ->I, 11-12
|  F                    ; FI, 13, 1
~psi                    ; ~I, 10-14
phi /\ ~psi             ; &I, 9, 15
```

**O que reparar:** dentro de uma caixa podes repetir (R) uma linha de uma
caixa de fora ainda aberta (linha 12 repete a 10).

## D6. $\phi \to (\psi \land \theta) \vdash (\phi \to \psi) \land (\phi \to \theta)$ --- conclusão ∧

**Plano.** Conclusão ∧: duas implicações à parte, cada uma com a sua caixa
(imagina $\phi$, →E, ∧E), e no fim ∧I.

```{.fitch seq="phi -> (psi /\ theta) |- (phi -> psi) /\ (phi -> theta)"}
phi -> (psi /\ theta)
---
|> phi
|  psi /\ theta         ; ->E, 1, 2
|  psi                  ; &E, 3
phi -> psi              ; ->I, 2-4
|> phi
|  psi /\ theta         ; ->E, 1, 6
|  theta                ; &E, 7
phi -> theta            ; ->I, 6-8
(phi -> psi) /\ (phi -> theta)   ; &I, 5, 9
```

**O que reparar:** o $\psi\land\theta$ da linha 3 **não** se pode usar na
segunda caixa (está numa caixa fechada): repete-se o →E na linha 7.

## D7. $(\phi \lor \psi) \to \theta \dashv\vdash (\phi \to \theta) \land (\psi \to \theta)$ --- equivalência

**$\dashv\vdash$ são duas deduções**, uma em cada sentido.

**Da esquerda para a direita.** Conclusão ∧ de duas implicações (como a
D6). Em cada uma: imagina o antecedente, faz ∨I para ter $\phi\lor\psi$, e
→E com a premissa.

```{.fitch seq="(phi \/ psi) -> theta |- (phi -> theta) /\ (psi -> theta)"}
(phi \/ psi) -> theta
---
|> phi
|  phi \/ psi           ; vI, 2
|  theta                ; ->E, 1, 3
phi -> theta            ; ->I, 2-4
|> psi
|  phi \/ psi           ; vI, 6
|  theta                ; ->E, 1, 7
psi -> theta            ; ->I, 6-8
(phi -> theta) /\ (psi -> theta)   ; &I, 5, 9
```

**Da direita para a esquerda.** Premissa ∧: separa-se logo. Conclusão →:
imagina $\phi\lor\psi$; é um ∨, por isso dois casos, cada um com a sua
implicação.

```{.fitch seq="(phi -> theta) /\ (psi -> theta) |- (phi \/ psi) -> theta"}
(phi -> theta) /\ (psi -> theta)
---
phi -> theta            ; &E, 1
psi -> theta            ; &E, 1
|> phi \/ psi
||> phi
||  theta               ; ->E, 2, 5
||> psi
||  theta               ; ->E, 3, 7
|  theta                ; vE, 4, 5-6, 7-8
(phi \/ psi) -> theta   ; ->I, 4-9
```

## D8. $\phi \to \psi,\ \neg\phi \to \theta \vdash \psi \lor \theta$ --- ∨ sem ∨ nas premissas

**Plano.** Em português: ou $\phi$ é V (e dá $\psi$) ou é F (e dá $\theta$).
Esse "ou" não está nas premissas, por isso arranja-se **por absurdo**
(sem regras derivadas): imagina $\neg(\psi\lor\theta)$. Imaginando $\phi$
chega-se a $\psi\lor\theta$, que choca: logo $\neg\phi$, e então $\theta$,
que outra vez dá $\psi\lor\theta$ e choca.

```{.fitch seq="phi -> psi, ~phi -> theta |- psi \/ theta"}
phi -> psi
~phi -> theta
---
|> ~(psi \/ theta)
||> phi
||  psi                 ; ->E, 1, 4
||  psi \/ theta        ; vI, 5
||  F                   ; FI, 6, 3
|  ~phi                 ; ~I, 4-7
|  theta                ; ->E, 2, 8
|  psi \/ theta         ; vI, 9
|  F                    ; FI, 10, 3
~~(psi \/ theta)        ; ~I, 3-11
psi \/ theta            ; ~E, 12
```

**Com o terceiro excluído (TE, regra derivada).** Mais natural, mas no teste
obriga a escrever a prova do TE (é a dedução da direita da pergunta 2 do
teste de 2024, 9 linhas):

```{.fitch seq="phi -> psi, ~phi -> theta |- psi \/ theta"}
phi -> psi
~phi -> theta
---
phi \/ ~phi             ; TE
|> phi
|  psi                  ; ->E, 1, 4
|  psi \/ theta         ; vI, 5
|> ~phi
|  theta                ; ->E, 2, 7
|  psi \/ theta         ; vI, 8
psi \/ theta            ; vE, 3, 4-6, 7-9
```

**O que reparar:** sempre que a ideia é "por casos de $\phi$ ser V ou F" e
não há um ∨ para usar, as duas saídas são TE + ∨E ou absurdo com a negação
da conclusão. Sem regras derivadas, a do absurdo é mais curta no total.

## R. Provas das regras derivadas

Se usares uma regra derivada no teste, tens de a provar. As duas mais úteis:

**(a) MT** (modus tollens): de $\phi\to\psi$ e $\neg\psi$ tira-se $\neg\phi$.

```{.fitch seq="phi -> psi, ~psi |- ~phi"}
phi -> psi
~psi
---
|> phi
|  psi                  ; ->E, 1, 3
|  F                    ; FI, 4, 2
~phi                    ; ~I, 3-5
```

**(b) ¬¬I**: de $\phi$ tira-se $\neg\neg\phi$.

```{.fitch seq="phi |- ~~phi"}
phi
---
|> ~phi
|  F                    ; FI, 1, 2
~~phi                   ; ~I, 2-3
```

**TE** ($\vdash \phi\lor\neg\phi$) é a dedução da direita da pergunta 2 do
teste de 2024.
