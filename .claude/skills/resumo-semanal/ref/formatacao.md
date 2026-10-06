# Formatação: caixas, bugs do pandoc, paginação, tabelas, figuras

Ler quando se escreve uma caixa/tabela/figura de um tipo novo, ou quando o
build dá AVISO ou o PDF sai estranho.

## Caixas (filtro `_shared/template/div-envs.lua`)

```
::: definicao            ::: exemplo            ::: pratica
...                      ...                    ...
:::                      :::                    :::

::: {.definicao title="--- Autómato finito"}
...
:::
```

- Estilo v2 (disciplinas em `ESTILO_V2` no `build.sh`, `preamble-v2.tex`):
  só estas três caixas. Uma `atencao`/`exame` faz a compilação falhar de
  propósito. As disciplinas fora da lista usam o `preamble.tex` antigo.
- Para converter uma disciplina ao v2: tirar as caixas `atencao`/`exame`
  (fundir no texto com † ou cortar), acrescentá-la à linha `ESTILO_V2=`
  (acrescentar ao que lá está e confirmar com `grep`, porque outra sessão
  pode ter mexido nessa linha) e rever o PDF todo.
- Disciplinas sem aulas numeradas usam `# Tema N --- Título`. Um PDF com
  duas aulas dá `# Aulas N--M`.
- `::: center` à volta de uma imagem centra-a dentro de uma caixa.

## Bugs silenciosos do pandoc (o build não dá erro)

- `title=" --- X"`: um espaço logo a seguir às aspas parte a caixa toda
  (saem `:::` literais). Escreve sempre `title="--- X"`.
- Nada de `% # & _ $` em `title=` (vai tal e qual para LaTeX). O `%`
  comenta o resto da linha e dá um erro numa caixa *seguinte*. O `\%`
  também não serve.
- `(a)`, `(d)`, `(1)`, `(2)` no início de uma linha viram uma lista
  renumerada. Escreve `**(a)**`, `**(d)**`.
- Um parágrafo (ex.: `**Evitar:**`) seguido de uma lista `-` **sem linha em
  branco** funde-se num parágrafo. Deixa sempre uma linha em branco.
- Imagens: sem `implicit_figures` (o float não cabe numa caixa). Escreve
  `![](figuras/x.pdf){width=50%}` e, se precisares de legenda, escreve-a em
  itálico na linha a seguir.
- Unicode em blocos de código (`∧ ∈ ⊆ →`): o v2 usa a Menlo, que tem estes
  caracteres. No estilo antigo (IPM), saem em branco: usa ASCII (`e`,
  `em`, `->`). Os glifos `♀ ↗` não existem na Charter: escreve-os por
  extenso. `✓` em texto escreve-se `$\checkmark$`.
- Lógica: `\not\models` usa o `\nmodels` (⊭) definido no `preamble-v2.tex`.
- Heredocs com `$` (`$R`, `$57`): usa sempre `<<'EOF'`.

## Paginação (não texto a meio)

- As caixas não partem entre páginas. Cada caixa tem de caber numa página:
  um exemplo longo divide-se em duas caixas `exemplo` seguidas.
- Cada `# Aula` começa numa página nova.
- O filtro põe `\Needspace` antes de tabelas (≤40 linhas), de blocos de
  código (≤20 linhas) e de títulos `##`/`###` (título + frase + caixa).
  Código mais longo divide-se em blocos de até ~20 linhas, em fronteiras
  naturais.
- Um rótulo ou parágrafo que fica sozinho no fundo da página leva antes
  ```` ```{=latex} ```` com `\Needspace*{N\baselineskip}` (N = linhas, ou
  linhas de código + 3).
- Código inline comprido numa frase justificada estica a linha: reescreve a
  frase para o código não cair a meio da linha.
- Para encontrar títulos órfãos: `pdftotext -f p -l p` e compara as
  últimas linhas com os `##` do `.md`.

## Tabelas (`auto-align.lua`)

- Uma coluna com valores curtos (V/F, números) fica centrada sozinha. Uma
  tabela só com valores curtos fica com a largura natural.
- Quando a tabela mistura colunas curtas e uma coluna longa, indica as
  larguras pelo número de traços (`|:-:|:----|:----------------|`).
- Uma conta comprida numa célula sai da tabela: explica-a numa frase antes
  e deixa só o resultado na tabela. Células com fórmulas longas ficam
  melhor numa lista.

## Figuras (graphviz em `<Disciplina>/figuras/`, nomes descritivos)

- `dot -Tpdf x.dot -o figuras/x.pdf`. Usa `rankdir=LR` para autómatos e
  figuras altas e estreitas (redesenha-as na horizontal, com rótulos curtos).
- Árvores compactas: `ranksep=0.22; nodesep=0.35; margin=0`, letra 13,
  `arrowsize=0.6`, à escala natural (~85%) e centradas.
- Figuras altas dentro de caixas limitam-se por altura (`{height=10cm}`),
  não por largura.
- Curvas reais (Bézier): `neato -n2` com os pontos de controlo verdadeiros.
- Uma figura ilegível à escala da página troca-se por uma tabela ou lista,
  se o texto já disser o mesmo.
- Figuras originais dos slides: `pdfimages -f N -l N -png`. Composições:
  `pdftoppm -r 200` + `sips -c H W --cropOffset Y X` (não há PIL).
- Para gráficos com matplotlib: instala-o com pip só quando for preciso.
