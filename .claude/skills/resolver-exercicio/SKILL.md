---
name: resolver-exercicio
description: Resolve exercícios das práticas (ex. "faz o 1.13 d) de lógica") no estilo que é aceite em exame — prova matemática formal com a notação da disciplina, não explicação por palavras. Usar sempre que o Gonçalo pede para resolver/explicar um exercício no chat, e também ao escrever exemplos resolvidos no resumo ou soluções no SOLUCOES_<Disciplina>.md (a skill resumo-semanal remete para aqui).
---

# Resolver exercícios no estilo de exame

O Gonçalo quer as resoluções **como a professora as faz e como são aceites
em exame**: prova matemática, com a notação das teóricas, cada passo
justificado por uma definição ou lei. Uma explicação "por palavras" ("como
C é inocente, A não pode ser culpado...") **não é válida em exame** e só
serve de complemento.

Regra geral: **escolhe sempre a forma matemática**. Só se resolve por
palavras quando o exercício é demasiado simples para isso fazer sentido
(ex. traduzir uma fórmula para português, avaliar uma fórmula numa
valoração dada com 2 contas). Mesmo aí, usa a notação certa no resultado.

## Antes de resolver

1. **Lê o enunciado original** (`<Disciplina>/Praticas/Semana_N/*.pdf`, com
   `pdftotext -layout`). Não confies na memória nem no resumo para o texto.
2. **Vê o método pedido** ("using the definitions", "without truth table",
   "using semantic equivalences"). Se o enunciado não diz, usa o método da
   aula a que o exercício pertence.
3. **Usa a notação dos slides da disciplina** (`Teoricas/Aula_NN.pdf`). Para
   Lógica, ver a secção abaixo.
4. **Verifica a resposta antes de a escrever** (Python, força bruta das
   valorações). Uma prova bonita com a conclusão errada é o pior resultado.

## Onde se escreve

- **No chat (terminal):** o terminal não mostra LaTeX. Usa Unicode:
  `⊨ ⊭ ⊨ᵥ ⊭ᵥ ¬ ∧ ∨ → ↔ ⇔ ⇒ ∅ ∈ ⊆ ∪ ∎` e escreve "sse" por extenso. Nunca
  `$\models$`.
- **No resumo / soluções (`.md` compilado com pandoc):** LaTeX normal
  (`\models_v`, `\not\models_v`, `\Leftrightarrow`). Cadeias longas em
  `aligned`, com a justificação de cada passo à direita (`&& \text{(...)}`).

## Lógica Computacional — o estilo da professora

Notação (slides da Aula 1–2):

- `⊨ᵥ φ`: a valoração v satisfaz φ. `⊭ᵥ φ`: não satisfaz.
- `⊨ φ`: φ é tautologia. `Γ ⊨ φ`: toda a v que satisfaz Γ satisfaz φ.
- `φ ⇔ ψ`: equivalência semântica.

Definição de `⊨ᵥ` (é **isto** que justifica cada passo da prova):

1. `⊨ᵥ p` sse `v(p) = V`
2. `⊨ᵥ ¬φ` sse `⊭ᵥ φ`
3. `⊨ᵥ φ ∧ ψ` sse `⊨ᵥ φ` e `⊨ᵥ ψ`
4. `⊨ᵥ φ ∨ ψ` sse `⊨ᵥ φ` ou `⊨ᵥ ψ`
5. `⊨ᵥ φ → ψ` sse `⊭ᵥ φ` ou `⊨ᵥ ψ`

E as negações que saem delas (usar sempre que se supõe algo falso):

- `⊭ᵥ φ ∧ ψ` sse `⊭ᵥ φ` ou `⊭ᵥ ψ`
- `⊭ᵥ φ ∨ ψ` sse `⊭ᵥ φ` e `⊭ᵥ ψ`
- `⊭ᵥ φ → ψ` sse `⊨ᵥ φ` e `⊭ᵥ ψ`

### Tipos de exercício e o esqueleto de cada um

**`Γ ⊨ φ` verdadeiro (prova direta).**

```
Seja v uma valoração tal que ⊨ᵥ Γ, isto é, ⊨ᵥ γ₁, …, ⊨ᵥ γₙ.
Queremos mostrar que ⊨ᵥ φ.
  ⊨ᵥ γ₁  sse  …                     (definição de ⊨ᵥ para o conectivo principal)
  …
Caso 1: …  Então … logo ⊨ᵥ φ.
Caso 2: …  Então … logo ⊨ᵥ φ.
Como v era arbitrária, Γ ⊨ φ.  ∎
```

- Abre a premissa pelo **conectivo principal**, com a regra 1–5. Quando dá
  um "ou", **separa em casos** e fecha cada caso.
- "ou" na definição ⇒ casos alternativos. Nunca os juntar com "e" (erro
  que o Gonçalo já fez: "se ⊨ᵥ r então v(r)=V e v(p)=F e v(q)=F").
- *Modus ponens* pode ser citado: de `⊨ᵥ φ` e `⊨ᵥ φ → ψ` vem `⊨ᵥ ψ`
  (pela regra 5, `⊭ᵥ φ` é impossível).

**`⊨ φ` (tautologia) verdadeiro**: é o caso `Γ = ∅`, pelo que a prova é
igual, com "seja v uma valoração qualquer". Uma alternativa é a **prova por
absurdo**: supõe `⊭ᵥ φ` para algum v, abre com as regras de `⊭ᵥ` e chega a
`⊨ᵥ ψ` e `⊭ᵥ ψ` ao mesmo tempo (contradição). Esta costuma ser a mais curta
para implicações (força antecedente ⊨ᵥ e consequente ⊭ᵥ).

**Falso (`Γ ⊭ φ` ou `⊭ φ`)**: dá um **contraexemplo explícito**, uma
valoração concreta `v(p)=…, v(q)=…`, e **verifica-o com as regras**:
`⊨ᵥ γ₁`, …, `⊨ᵥ γₙ` e `⊭ᵥ φ`, cada um com a regra que o justifica. Para
encontrá-lo, supõe `⊭ᵥ φ` e vê o que isso força.

**Afirmações com fórmulas genéricas (φ, ψ, Γ, Σ)**, por exemplo
"se Γ ⊨ θ e Γ ⊆ Σ então Σ ⊨ θ":
- Verdadeira: prova com as definições (seja v tal que ⊨ᵥ Σ; como
  Γ ⊆ Σ, ⊨ᵥ Γ; por hipótese, ⊨ᵥ θ).
- Falsa: **instancia** com fórmulas concretas (φ = p, ψ = q, …), mostra
  que as hipóteses valem e a conclusão não, com valoração explícita.

**Equivalências / classificar fórmulas**: cadeia de `⇔`, **uma lei por
passo**, com o nome da lei e os papéis (φ, ψ, θ) quando não é óbvio. Usa as
leis da tabela dos slides/enunciado. As leis extra (complementaridade,
absorção…) só como atalho assinalado. A conclusão diz a classificação com
a notação: `⊨ φ`, contradição, ou satisfazível com `⊨ᵥ φ` e `⊭ᵥ' φ` para
duas valorações dadas.

**Modelação (cavaleiros/vilões, suspeitos, regras)**: (1) define as
variáveis; (2) traduz cada frase para uma fórmula; (3) escreve **a
condição** como fórmula (cavaleiro: `a ↔ S_A`; "inocente diz a verdade":
`S_A ↔ ¬g_a`; "todos dizem a verdade": `{S_A, S_B, S_C}`); (4) resolve
essa condição com a notação: "é satisfazível?" = existe v com ⊨ᵥ Γ;
"é consequência?" = prova de `Γ ⊨ φ` como acima ou contraexemplo. A tabela
de verdade é aceitável quando tem ≤ 8 linhas e o enunciado não a proíbe,
mas a conclusão escreve-se sempre com ⊨/⊭.

### Exemplo de referência (aprovado pelo Gonçalo, 2026-10-01)

1.13 (d): `{ (p ∨ q) → r } ⊨ (p → r) ∨ (q → r)`

```
Seja v uma valoração tal que ⊨ᵥ (p ∨ q) → r. Queremos ⊨ᵥ (p → r) ∨ (q → r).
  ⊨ᵥ (p ∨ q) → r  sse  ⊭ᵥ p ∨ q  ou  ⊨ᵥ r
Caso 1: ⊨ᵥ r. Como ⊨ᵥ p → r sse ⊭ᵥ p ou ⊨ᵥ r, temos ⊨ᵥ p → r.
        Logo ⊨ᵥ (p → r) ∨ (q → r).
Caso 2: ⊭ᵥ p ∨ q  sse  ⊭ᵥ p e ⊭ᵥ q. Como ⊭ᵥ p, ⊨ᵥ p → r.
        Logo ⊨ᵥ (p → r) ∨ (q → r).
Em ambos os casos ⊨ᵥ (p → r) ∨ (q → r); como v é arbitrária,
{ (p ∨ q) → r } ⊨ (p → r) ∨ (q → r).  ∎
```

## Outras disciplinas

O princípio é o mesmo: **a forma que o professor usa nas teóricas e que é
aceite em exame**. Por exemplo, em Compiladores, as derivações e a
construção de autómatos seguem passo a passo o algoritmo dos slides, com a
notação dos slides, e não uma descrição em prosa. Quando não sabes qual é
essa forma, abre os slides e copia o formato dos exemplos resolvidos pelo
professor. Se o Gonçalo mostrar como o professor resolveu, isso passa a ser
a referência: grava-o aqui, numa secção da disciplina.

## Depois de resolver

- Se o Gonçalo disser que não percebeu, **não troques a prova por
  palavras**. Mantém a prova e acrescenta uma explicação ao lado, ou parte
  o passo que falhou em passos mais pequenos.
- Feedback novo sobre o estilo das resoluções vai para a secção abaixo
  **e** para as "Aprendizagens" da skill `resumo-semanal`.

### Aprendizagens

- 2026-10-01: Criada a partir do feedback do Gonçalo sobre a 1.11 e a
  1.13 de Lógica: as resoluções "por palavras" não são válidas em exame. A
  professora prova com `⊨ᵥ`, abre cada fórmula pelas regras da definição e
  separa em casos quando aparece um "ou". O exemplo da 1.13 (d) acima foi
  aprovado como referência.
