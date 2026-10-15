# CONTEXTO_Compiladores (convenções e factos; não gera PDF)

**Exercícios.** Como nas folhas de lab: `Ex. N` com alíneas `Ex. 1(b)` ou
`**(a)**`; exercícios inventados com letra (`Ex. D`); lab. de ASTs como
`ASTs N`. Exemplo-modelo: `SOLUCOES_Compiladores.md`, `### Ex. 2` (l. ~8)
para papel e lápis, `### ASTs 2` (l. ~1072) para código.

**Soluções de labs de código:** só o código que cada alínea acrescenta ou muda
e **uma** saída real por alínea; o código corre-se sempre (já apanhou erros
reais nos slides).

**Ferramentas** (todas instaladas):
- C: `gcc`; Java: `javac`;
- Flex + Bison: usar o Bison do brew (`/opt/homebrew/opt/bison/bin`; o do
  macOS é o 2.3);
- Haskell: Alex/Happy instalados com `cabal install` (em `~/.cabal/bin`);
  `happy -i` gera o `.info` com os conflitos reais.

**Labs.** Semana_1 scanner-c (folha 2), Semana_2 gramática (folha 3),
Semana_3 Parsing LR (folha 4), Semana_4 Abstract_Syntax_Trees.
