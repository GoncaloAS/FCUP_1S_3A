---
title: "Lógica Computacional --- Treino de deduções (tipo pergunta 6)"
subtitle: "Os outros padrões que podem sair, além de uma disjunção nas premissas."
---

Em dedução natural, na notação de Fitch, com todos os passos anotados.
**Sem regras derivadas** (se usares alguma, prova-a à parte, como pede o
teste). A resolução está em `Treino_deducoes_resolucao.pdf`.

Antes de cada uma, responde às quatro perguntas: *a conclusão é → ou ¬?
há um ∨ nas premissas? há um ∧? o objetivo aparece nas linhas que tenho?*

**D1.** $\neg(\phi \land \psi) \vdash \neg\phi \lor \neg\psi$

**D2.** $(\phi \land \psi) \to \theta,\ \neg\theta,\ \phi \vdash \neg\psi$

**D3.** $\neg\phi \to \psi,\ \psi \to \theta,\ \neg\theta \vdash \phi$

**D4.** $\phi \lor \psi,\ \neg\phi \vdash \psi$

**D5.** $\neg(\phi \to \psi) \vdash \phi \land \neg\psi$

**D6.** $\phi \to (\psi \land \theta) \vdash (\phi \to \psi) \land (\phi \to \theta)$

**D7.** $(\phi \lor \psi) \to \theta \ \dashv\vdash\ (\phi \to \theta) \land (\psi \to \theta)$
(as duas direções)

**D8.** $\phi \to \psi,\ \neg\phi \to \theta \vdash \psi \lor \theta$

**R.** Prova as regras derivadas mais usadas:
(a) MT: $\phi \to \psi,\ \neg\psi \vdash \neg\phi$;
(b) ¬¬I: $\phi \vdash \neg\neg\phi$.
