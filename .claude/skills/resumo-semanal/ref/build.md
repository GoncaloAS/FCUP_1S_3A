# Build: erros, avisos e diagnóstico

Ler só quando o `build.sh` falha ou dá AVISO.

- Erros do tectonic:
  - floats dentro de caixas: o `-f markdown-implicit_figures` já está no
    `build.sh`, não o tires;
  - não acrescentes ao preâmbulo pacotes que o pandoc já carrega
    (babel, fontenc);
  - a 1.ª compilação na máquina vai buscar pacotes e demora.
- AVISOs do build (todos bloqueantes):
  - **caixa maior que uma página**: o fim sai cortado. Divide a caixa ou
    reduz a figura (por altura);
  - **sem glifo**: o carácter sai em branco (ver `formatacao.md`);
  - **linha fora da margem**: parte o código/`texttt`;
  - **markdown por converter**: `:::` ou `{.x` ou `title=` no texto do PDF.
    É uma caixa partida (ver os bugs do pandoc em `formatacao.md`). Também
    apanha "texto: - item - item": uma lista colada ao parágrafo, sem
    linha em branco;
  - **contagem de caixas `pratica` ≠ `##` das soluções**: o `div-envs.lua`
    emparelha a k-ésima caixa com a k-ésima `##`. Corre
    `contexto.sh <D> --sol` e parte ou junta as `##`.
- Espaçamentos estranhos: `KEEP_TMP=1 bash _shared/template/build.sh X`
  guarda o `.tex`. Compila-o comentando uma linha do preâmbulo de cada vez
  e mede pela página onde acaba o índice. Causas já vistas: `tocloft` (usa
  o `titletoc`) e títulos do índice com estrutura diferente da das aulas.
- Índice com mais de uma página: junta a disciplina a `INDICE_2COL` no
  `build.sh`.
- Captura do `SOLUCOES.html` (só quando muda o template do site):
  ```
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new \
    --window-size=1000,3000 --virtual-time-budget=3000 --screenshot=<png> "file://<html>"
  ```
  - Para ver uma alínea aberta, faz uma cópia com ` open` num só
    `<details>`. Sem `#id` no URL (a captura sai em branco).
  - Para ver uma secção do fundo da página, corta o HTML: o `<head>` mais o
    bloco a partir do `<h2>` dessa secção.
  - Para testar comportamento: injeta um `<script>` que escreve num `<pre>`
    e lê-o com `--dump-dom`.
  - Apaga as cópias no fim.
