---
title: "Lógica Computacional --- Folha de revisão"
author: "Gonçalo Sousa"
date: "Aulas 1--8. As receitas do resumo, sem exemplos: para rever antes do exame."
---

## Sintaxe e semântica

**Parêntesis**: $\neg$ > $\land$ > $\lor$ > $\to$; $\land$, $\lor$ à
esquerda; $\to$ à direita ($p\to q\to r = p\to(q\to r)$). Raiz da árvore =
conectivo de **menor** prioridade fora de parêntesis. Subfórmulas = nós da
árvore (repetidas contam uma vez).

| | $\models_v$ | $\not\models_v$ |
|:------|:----------------------|:----------------------|
| $\neg\phi$ | $\not\models_v \phi$ | $\models_v \phi$ |
| $\phi\land\psi$ | $\models_v \phi$ **e** $\models_v \psi$ | $\not\models_v \phi$ **ou** $\not\models_v \psi$ |
| $\phi\lor\psi$ | $\models_v \phi$ **ou** $\models_v \psi$ | $\not\models_v \phi$ **e** $\not\models_v \psi$ |
| $\phi\to\psi$ | $\not\models_v \phi$ **ou** $\models_v \psi$ | $\models_v \phi$ **e** $\not\models_v \psi$ |

**Satisfazível**: alguma $v$ dá $V$. **Tautologia** ($\models\phi$): todas.
**Contradição**: nenhuma. $\Gamma\models\phi$: toda a $v$ que satisfaz
$\Gamma$ satisfaz $\phi$. $\phi\Leftrightarrow\psi$: $\phi\models\psi$ e
$\psi\models\phi$.

## Equivalências

Comutatividade, associatividade, idempotência; De Morgan
$\neg(\phi\land\psi)\Leftrightarrow\neg\phi\lor\neg\psi$,
$\neg(\phi\lor\psi)\Leftrightarrow\neg\phi\land\neg\psi$; distributividade
$(\phi\land\psi)\lor\theta\Leftrightarrow(\phi\lor\theta)\land(\psi\lor\theta)$,
$(\phi\lor\psi)\land\theta\Leftrightarrow(\phi\land\theta)\lor(\psi\land\theta)$;
$\neg\neg\phi\Leftrightarrow\phi$; $\phi\to\psi\Leftrightarrow\neg\phi\lor\psi$.
**Extra**: $\phi\lor\neg\phi\Leftrightarrow V$, $\phi\land\neg\phi\Leftrightarrow F$;
$\phi\lor F\Leftrightarrow\phi$, $\phi\land V\Leftrightarrow\phi$;
$\phi\lor V\Leftrightarrow V$, $\phi\land F\Leftrightarrow F$;
absorção $\phi\lor(\phi\land\psi)\Leftrightarrow\phi$,
$\phi\land(\phi\lor\psi)\Leftrightarrow\phi$.

**Classificar por equivalências** (1.9): eliminar $\to$, empurrar $\neg$,
simplificar. $V$ → tautologia; $F$ → contradição; outra coisa →
satisfazível, com uma $v$ verdadeira e uma falsa **confirmadas na
original**. Uma lei por passo, com o nome.

**$\to$ e $\land$**: $(p\to q)\land(p\to r)\Leftrightarrow p\to(q\land r)$;
$(p\lor q)\to r\Leftrightarrow(p\to r)\land(q\to r)$; mas
$(p\to r)\land(q\to r)\not\Leftrightarrow(p\land q)\to r$.

## Provar com a definição (formato de exame)

- **$\Gamma\models\phi$**: "Seja $v$ tal que $\models_v\Gamma$." Abrir cada
  fórmula pelo conectivo principal; num **ou**, um caso de cada vez. Fecho:
  "como $v$ é arbitrária, $\Gamma\models\phi$." $\blacksquare$
- **Por absurdo** (bom com $\to$): supor $\not\models_v\phi$, abrir com a
  coluna $\not\models_v$, chegar a $\models_v\theta$ e $\not\models_v\theta$.
- **Falso**: uma $v$ concreta, verificada regra a regra
  ($\models_v\gamma$ para cada $\gamma\in\Gamma$, $\not\models_v\phi$).
- **Monotonicidade**: $\Gamma\models\theta$ e $\Gamma\subseteq\Sigma$ ⇒
  $\Sigma\models\theta$. Tirar premissas pode estragar.
- **Cavaleiros/vilões**: por casos, em frases ("A não pode ser vilão e
  dizer isto, logo..."); cada caso impossível = cavaleiro a mentir ou
  vilão a dizer a verdade ($a\leftrightarrow S$).
- **Com $v$ dada**: de baixo para cima ("de $v(p)=V$ segue $\models_v p$,
  logo $\models_v p\lor q$..."). **Com tabela** (se não for proibida):
  "nas linhas em que as premissas são V, a conclusão também é".
- **Regra redundante** sse é consequência semântica das outras.

**Conjuntos completos**: $\{\land,\lor,\neg\}$ (indução em $n$, ou FND).
$\{\neg,\to\}$: $\phi\land\psi\Leftrightarrow\neg(\phi\to\neg\psi)$,
$\phi\lor\psi\Leftrightarrow\neg\phi\to\psi$. $\{\neg,\lor\}$:
$\phi\land\psi\Leftrightarrow\neg(\neg\phi\lor\neg\psi)$. NAND:
$\neg p=p\bar\land p$, $p\land q=(p\bar\land q)\bar\land(p\bar\land q)$,
$p\lor q=(p\bar\land p)\bar\land(q\bar\land q)$.

## Formas normais

| | FND ("ou" de "e"s) | FNC ("e" de "ou"s) |
|:-------|:-------------------------|:-------------------------|
| Da tabela | uma conjunção por linha **V**: var. a $V$ positiva, a $F$ negada | uma cláusula por linha **F**: var. a $V$ negada, a $F$ positiva |
| Da fórmula | eliminar $\to$/$\leftrightarrow$, FNN, distribuir $\land$ sobre $\lor$ | eliminar $\to$/$\leftrightarrow$, FNN, distribuir $\lor$ sobre $\land$ |
| Decide fácil | **satisfazível** sse **alguma** conjunção não tem $p,\neg p$ | **tautologia** sse **todas** as cláusulas têm $p,\neg p$ |

**FNN**: $\neg$ só em variáveis (De Morgan + dupla negação). Poucos $V$ na
tabela → FND curta; poucos $F$ → FNC curta. Apagar conjunções com par
($\phi\lor F$) e cláusulas com par ($\phi\land V$).

**Horn**: FNC com **no máximo um positivo** por cláusula
($\neg p_1\lor\dots\lor\neg p_n\lor p$ = regra, sem positivo = restrição
$\to F$, $p$ = facto). **Algoritmo**: factos a $V$; se todos os negativos
de uma cláusula estão a $F$, o positivo fica $V$; repetir. Uma cláusula
$F$ → insatisfazível; senão o resto a $F$ e é satisfazível. Sem
retrocesso, polinomial.

## SAT: cláusulas e DLL

Cláusula = conjunto de literais; FNC = conjunto de cláusulas. **Cláusula
vazia** = $F$ (insatisfazível). **Conjunto vazio** = $V$ (satisfazível).
Cláusula com $p,\neg p$ sai. $\tilde p=\neg p$, $\widetilde{\neg p}=p$.

**Propagação unitária** de $l$: saem as cláusulas com $l$; tira-se
$\tilde l$ das outras. **DLL(S)**: propagar; vazio → satisfazível; tem $F$
→ insatisfazível; escolher $l$ e tentar $S\cup\{l\}$, se falhar
$S\cup\{\tilde l\}$. Escrever: "sem unitárias; escolhe-se $p$,
DLL$(S\cup\{p\})$; a propagação de $p$ dá $S_1=\{\dots\}$".
Insatisfazível só se os dois ramos falham. Valoração
= literais supostos + propagados do ramo bom. Escolha: o mais frequente;
o produto de ocorrências de $l$ e $\tilde l$ máximo; o mais frequente nas
cláusulas mais curtas.

## Dedução natural (Fitch)

| Regra | De | Conclui | Cita |
|:-----|:------------------|:-----------|:-----------|
| $\land$I | $\phi$, $\psi$ | $\phi\land\psi$ | 2 linhas |
| $\land$E | $\phi\land\psi$ | $\phi$ (ou $\psi$) | 1 linha |
| $\lor$I | $\phi$ | $\phi\lor\psi$ (ou $\psi\lor\phi$) | 1 linha |
| $\lor$E | $\phi\lor\psi$; $[\phi]\dots\gamma$; $[\psi]\dots\gamma$ | $\gamma$ | linha, $i$--$j$, $k$--$l$ |
| $\to$E | $\phi$, $\phi\to\psi$ | $\psi$ | 2 linhas |
| $\to$I | $[\phi]\dots\psi$ | $\phi\to\psi$ | $i$--$j$ |
| $\neg$I | $[\phi]\dots\mathbf{F}$ | $\neg\phi$ | $i$--$j$ |
| $\neg$E | $\neg\neg\phi$ | $\phi$ | 1 linha |
| $\mathbf{F}$I | $\phi$, $\neg\phi$ | $\mathbf{F}$ | 2 linhas |
| $\mathbf{F}$E | $\mathbf{F}$ | qualquer $\phi$ | 1 linha |
| R | $\phi$ acessível | $\phi$ | 1 linha |

**Alcance**: o que está dentro de uma sub-dedução fechada **não se usa**
cá fora; o de fora usa-se lá dentro.

**Estratégias**: conclusão $\psi\to\theta$ → supor $\psi$, $\to$I.
Conclusão $\neg\psi$ → supor $\psi$, chegar a $\mathbf{F}$, $\neg$I. Letra
ou disjunção → supor $\neg\phi$, $\mathbf{F}$, $\neg$I ($\neg\neg\phi$),
$\neg$E. Premissa $\phi\lor\psi$ → $\lor$E. Tens $\neg\phi$ → procura
$\phi$ para $\mathbf{F}$I. Tens $\phi\to\theta$ → procura $\phi$ para
$\to$E. Caso impossível de um $\lor$E → $\mathbf{F}$ e $\mathbf{F}$E.
Nada de equivalências semânticas como passos.

**Derivadas** (provar à parte se usadas): MT ($\phi\to\psi$, $\neg\psi$ ⊢
$\neg\phi$: supor $\phi$, $\to$E, $\mathbf{F}$I, $\neg$I); $\neg\neg$I;
RA ($[\neg\phi]\dots\mathbf{F}$ ⊢ $\phi$); TE ($\vdash\phi\lor\neg\phi$:
supor $\neg(\phi\lor\neg\phi)$); contraposição.

**$\Gamma\nvdash\phi$**: contraexemplo $v$ com $\models_v\Gamma$ e
$\not\models_v\phi$, logo $\Gamma\not\models\phi$, logo (integridade)
$\Gamma\nvdash\phi$. **DN íntegra e completa**: $\Gamma\vdash\phi$ sse
$\Gamma\models\phi$. **Lema da dedução**: $\Sigma\cup\{\phi\}\vdash\psi$
sse $\Sigma\vdash\phi\to\psi$. **Integridade**: 1.º passo "mau" é
impossível, regra a regra. **Completude**: $\psi^v$ ($\psi$ ou
$\neg\psi$); Lema 1 $q_1^v,\dots,q_n^v\vdash\phi^v$ (indução); tautologia:
juntar os $2^n$ casos com TE + $\lor$E, uma variável de cada vez; com
premissas: Lema 4 ($\models\phi_1\to(\dots\to\psi)$) + lema da dedução.
**Decidível** ($\vdash$ = $\models$ = tabela finita); $\phi$ satisfazível
sse $\neg\phi$ não é tautologia. $\phi\dashv\vdash\psi$ = duas deduções.
**Falácias**: afirmar o consequente, negar o antecedente (contraexemplo
$v(\phi)=F$, $v(\psi)=V$).

## Hilbert, tableaux e resolução

**$\mathcal{H}$** ($\neg,\to$): A1 $\phi\to(\psi\to\phi)$; A2
$(\phi\to(\psi\to\theta))\to((\phi\to\psi)\to(\phi\to\theta))$; A3
$(\neg\psi\to\neg\phi)\to((\neg\psi\to\phi)\to\psi)$; só regra MP. Axiomas
= esquemas (dizer a substituição). Teorema da dedução;
$\vdash_{DN}$ = $\vdash_{\mathcal{H}}$, logo íntegro e completo.

**Tableau de $\phi$**: raiz $\neg\phi$. $\alpha$ ($\phi\land\psi$;
$\neg(\phi\lor\psi)$ → $\neg\phi,\neg\psi$; $\neg(\phi\to\psi)$ →
$\phi,\neg\psi$): dois nós seguidos. $\beta$ ($\phi\lor\psi$;
$\neg(\phi\land\psi)$ → $\neg\phi\mid\neg\psi$; $\phi\to\psi$ →
$\neg\phi\mid\psi$): ramifica, em todos os ramos abertos abaixo.
$\neg\neg\phi$ → $\phi$. Primeiro $\alpha$/$\neg\neg$, depois $\beta$.
Ramo fecha ($\times$) com $\psi$ e $\neg\psi$ (qualquer $\psi$). Todos
fechados → $\phi$ teorema. Ramo aberto esgotado → contraexemplo.

**Resolução de $\phi$**: FNC de $\neg\phi$ ($\neg(\phi\to\psi)\Leftrightarrow
\phi\land\neg\psi$, De Morgan, $\to$ em $\lor$, distributividade) →
cláusulas → resolver até $\mathbf{F}$: de $C\cup\{p\}$, $C'\cup\{\neg p\}$
sai $C\cup C'$. **Um par de cada vez** ($\{p,q\},\{\neg p,\neg q\}$ não
dão $\mathbf{F}$). Começar pelas unitárias. Numerar e citar "de $i$ e
$k$".
