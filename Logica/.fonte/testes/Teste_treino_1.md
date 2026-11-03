---
title: "Lógica Computacional --- Teste de treino 1"
subtitle: "Mesma estrutura do teste 1124 (2024). Duração: 2 h. Responde numa folha à parte."
---

**6 perguntas, 20 valores.** As resoluções estão em `Teste_treino_1_resolucao.pdf`:
só as abras depois de acabares.

## 1. (4 valores) Para cada alínea, indica a resposta correta.

**(a)** A fórmula $(p \land \neg q) \to (q \lor \neg p)$ é:

- A. uma tautologia
- B. uma contradição
- C. satisfazível, mas não tautologia

**(b)** Qual das seguintes é **falsa**?

- A. $\phi \to \psi,\ \neg\psi \lor \theta,\ \phi \models \theta$
- B. $\models (\phi \land \neg\phi) \to \psi$
- C. $\phi \lor \psi,\ \phi \to \theta \models \theta$

**(c)** Em Subterrânea não há maneira de saber se é dia ou noite; só os
habitantes o sentem. Há dois tipos de habitantes: os **cavaleiros do dia**,
que dizem a verdade de dia e mentem de noite, e os **cavaleiros da noite**,
que dizem a verdade de noite e mentem de dia. Um visitante encontra um
habitante, que diz: *"Agora é de noite e eu sou um cavaleiro do dia."* Se
isto chegou ao visitante para saber o tipo do habitante e se é dia ou
noite, qual é a solução?

- A. É um cavaleiro da noite e é de dia.
- B. É um cavaleiro do dia e é de noite.
- C. É um cavaleiro da noite e é de noite.

**(d)** Se $\Sigma \vdash \phi$ e $\Gamma \vdash \neg\psi$, qual das
seguintes **não** é necessariamente verdadeira?

- A. $\Sigma \cup \Gamma \vdash \psi \to \phi$
- B. $\Sigma \cup \Gamma \vdash \phi \land \neg\psi$
- C. $\Sigma \cup \Gamma \vdash \phi \to \psi$

## 2. (3 valores) Completa as deduções: as fórmulas em falta e as regras de cada passo.

**Esquerda** (falta a premissa, duas fórmulas e duas regras):

```{.fitch .nocheck}
\underline{\hspace{3.5cm}}
---
|> ~theta
||> \underline{\hspace{2cm}}
||  phi \/ psi        ; vI, 3
||  theta             ; ->E, 1, 4
||  F
|  \underline{\hspace{2cm}}          ; ~I, 3-6
~theta -> ~phi
```

**Direita** (faltam todas as regras):

```{.fitch .nocheck}
~(phi \/ psi)
---
|> phi
|  phi \/ psi
|  F
~phi
|> psi
|  phi \/ psi
|  F
~psi
~phi /\ ~psi
```

## 3. (3 valores) Para cada alínea, indica só a resposta.

**(a)** Para $v(p)=V$, $v(q)=F$ e $v(r)=V$, determina
$v\big((p \lor q) \to (r \land \neg p)\big)$.

**(b)** A partir da tabela de verdade, constrói uma fórmula em **forma
normal disjuntiva**.

| $p$ | $q$ | $\gamma$ |
|:-:|:-:|:-:|
| V | V | F |
| V | F | V |
| F | V | V |
| F | F | F |

**(c)** Determina a forma normal negativa de
$\neg\big((p \to \neg q) \lor (r \land \neg p)\big)$.

**(d)** Determina todas as cláusulas **novas** que se obtêm por **um só
passo** de resolução a partir de $\{\{p, q\}, \{\neg p, r\}, \{\neg q, \neg r\}\}$.

**(e)** Pelas regras de expansão do tableau, quais são os componentes da
fórmula $(\neg p \to q) \to \neg(r \lor p)$?

**(f)** Encontra uma valoração tal que
$\{p \to (q \lor r),\ \neg q\} \nmodels r \to p$.

## 4. (3 valores) Com o algoritmo de Davis-Putnam (DLL), verifica se o conjunto de cláusulas é satisfazível:

$$\{p \lor q \lor \neg r,\ \neg p \lor q,\ \neg q \lor r,\ \neg p \lor \neg r,\ p \lor r,\ \neg q \lor \neg r \lor s\}$$

## 5. (4 valores) Considera a fórmula $\phi = (p \to (q \to r)) \to ((p \land q) \to r)$.

**a)** Dá uma dedução de $\phi$ em dedução natural, na notação de Fitch,
com todos os passos anotados.

**b)** Dá uma dedução de $\phi$ por tableau.

## 6. (3 valores) Em dedução natural, na notação de Fitch, com todos os passos anotados, mostra:

$$(\phi \to \gamma) \lor (\neg\psi \to \neg\phi),\ \ \gamma \to \neg\delta \ \vdash\ \phi \to (\neg\delta \lor \psi)$$

Se usares regras derivadas, escreve também as provas delas.

# Parte extra (matéria que também pode sair)

Não faz parte dos 20 valores: são os temas que o teste de 2024 não trouxe,
mas que foram dados e podem aparecer.

## E1. Forma normal conjuntiva

**(a)** A partir da tabela de verdade, constrói uma fórmula em **forma
normal conjuntiva**.

| $p$ | $q$ | $r$ | $\gamma$ |
|:-:|:-:|:-:|:-:|
| V | V | V | V |
| V | V | F | F |
| V | F | V | V |
| V | F | F | V |
| F | V | V | F |
| F | V | F | V |
| F | F | V | V |
| F | F | F | V |

**(b)** Usando as leis de equivalência (indica uma por passo), determina
uma FNC de $(p \to q) \to (r \land \neg p)$.

## E2. Dedução por resolução completa

Encontra uma dedução por resolução de
$$\big((p \lor q) \land (p \to r) \land (q \to r)\big) \to r$$

## E3. Algoritmo de Horn

Aplica o algoritmo de satisfazibilidade para fórmulas de Horn a
$$(\neg p \lor \neg q \lor r) \land p \land (\neg p \lor q) \land (\neg r \lor s) \land (\neg s \lor \neg q)$$

## E4. Tableau aberto

Usa um tableau para decidir se $(p \to q) \to (q \to p)$ é tautologia. Se
não for, dá uma valoração que a torne falsa.

## E5. Conectivos completos

Mostra que $\{\neg, \to\}$ é um conjunto completo de conectivos.

## E6. Verdadeiro ou falso? Justifica.

**(a)** Se $\Sigma \cup \{\neg\phi\} \vdash \mathbf{F}$, então $\Sigma \vdash \phi$.

**(b)** Se $\Sigma \vdash \phi$ e $\Gamma \vdash \phi$, então $\Sigma \cap \Gamma \vdash \phi$.

**(c)** O conjunto $\{p \to q,\ q \to r,\ p,\ \neg r\}$ é consistente.
