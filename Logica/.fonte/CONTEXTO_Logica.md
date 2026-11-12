# CONTEXTO_Logica (convenções e factos; não gera PDF)

**Nomes.** Um PDF com duas aulas dá `Aula_05-06.pdf` e `# Aulas N--M`.
`Teoricas/Apontamentos_Nelma_Moreira.pdf` (176 p.) é suplementar: não se
processa; procura-se no cache (`grep -n` em `.fonte/.cache/`) só para as
lacunas (†).

**Exercícios.** Numerados como nas fichas: `1.13`, `2.21` (proplogic.pdf =
cap. 1, proplogicproofs.pdf = cap. 2); alíneas `**(d)**`. O método é o que o
enunciado pede. Resoluções em estilo de exame: notação e definição de ⊨ᵥ na
skill `resolver-exercicio` (secção "Lógica Computacional"); resoluções "por
palavras" não valem. Exemplo-modelo: `SOLUCOES_Logica.md`, `### 1.6` (l. ~155).

**Blocos verificados automaticamente** (o `fechar.sh` corre os dois verificadores):
- dedução natural em ```` ```{.fitch} ```` (`|` por nível, `|>` abre
  hipótese, `---` fecha premissas, `; &E, 2`); `.nocheck` só para deduções
  erradas de propósito;
- tableaux e resolução em ```` ```{.tableau} ```` / ```` ```{.resolucao} ````
  (figuras geradas em `figuras/auto/` a cada build).

**LaTeX.** `\not\models` → usa `\nmodels` (⊭, definido no `preamble-v2.tex`).

**Soluções oficiais.** `Praticas/Semana_1/proplogic_resolv.pdf` (ficha 1)
é a referência de forma (resumida na `resolver-exercicio`). Na folha, a
1.13 (a)/(b) corresponde às alíneas (c)/(d) do enunciado; na 1.12 (b) ela
diz que R4 não é consequência das outras, mas é ({R2, R3} ⊨ R4): fica a
resposta certa, com nota. Resolução do teste 1124 (`Testes/Teste_1124_resolucao.pdf`): na 3(a)
diz F, mas o valor é V (s∨q = V; q ∧ (¬s∨p) = V); na 3(b) pede FND e dá a
FNC (s∨¬p)∧(¬s∨¬p) — a FND é (s∧¬p)∨(¬s∧¬p) ⇔ ¬p. Na 2 (direita), a linha 8
diz ¬I, 1–9, mas é ¬I, 1–7; na 2 (esquerda) põe a premissa ¬(φ∧γ) e FI, 1, 5,
o que contradiz o "θ →E, 1, 5" do enunciado: a premissa é (φ∧γ)→θ e a linha 7
é FI, 6, 2.

**Ficha 3** (`Praticas/Semana_8/folsem.pdf`, cap. 3, semântica de 1.ª
ordem) e a resolução oficial (`folsem_resolv.pdf`, só as alíneas ⇒; forma
na `resolver-exercicio`). Recomendados na semana 8: 3.4, 3.5, 3.7, 3.8,
3.9. Gralhas da 3.9: usa $R$ binário em (c), (e), (g), $h$ com 1 argumento
em (d) e um $T$ fora da linguagem; (f)--(h) juntam duas fórmulas. Na
resolução, a 3.11 (d) é a (f) do enunciado. Slide 19 da Aula 14: a linha 7
cita a 4, de dentro da caixa já fechada (a nossa versão tira $\psi$ antes).

**DN de 1.ª ordem no verificador**: `forall x`, `exists x`, `t != u`,
`phi[v/x]`, regras `AI AE EI EE =I =E`; `|> [v] ...` abre a caixa da
variável nova; `|> [u]` sozinho abre-a na linha seguinte; `naolivre="psi:x"`
no bloco.

**Suplementar.** `Teoricas/Extra_Notes_Propositional_FOL.pdf` (notas em inglês) também é suplementar, como os apontamentos. `Testes/Teste_1124.pdf` é um teste antigo do Moodle (bom para treinar o 1.º teste).
