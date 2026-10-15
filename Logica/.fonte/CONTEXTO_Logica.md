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
resposta certa, com nota.
