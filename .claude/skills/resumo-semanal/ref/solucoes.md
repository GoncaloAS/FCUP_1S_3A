# Soluções (`.fonte/SOLUCOES_<Disciplina>.md` → `SOLUCOES.html`)

Ler quando se escrevem soluções novas.

- **Site único**: `SOLUCOES.html` na raiz, com um separador por disciplina.
  Gera-o o `build_solucoes.py` a partir de todos os `*/.fonte/SOLUCOES_*.md`
  (também corre no fim do `build.sh`). Não cries HTML por disciplina nem
  escrevas soluções diretamente em HTML.
- Convenção:
  ```
  ---
  title: "<Disciplina> --- Soluções dos exercícios \"Pratica agora\""
  subtitle: "<enunciado de origem>. Tenta primeiro sozinho; abre uma alínea só depois de a teres feito."
  ---
  ## Aula N --- tópico               (uma ## por caixa pratica, pela mesma ordem)
  ### 1.2 --- título do exercício    (o número dá o id: Logica-1.2-a)
  dados comuns, visíveis
  #### (a) enunciado da alínea       (fechada; a solução vem a seguir)
  ```
  - Um exercício sem alíneas leva um único `#### Resposta`.
  - **Uma `##` por caixa `pratica`, pela mesma ordem.** O rodapé de cada
    caixa liga a cada alínea da k-ésima `##`.
- **Cada item de cada caixa tem solução**, com a mesma numeração, escrita
  na mesma passagem que a caixa. Para verificar, corre
  `_shared/template/contexto.sh <D> --sol`.
- O método e o formato (prova formal com a notação da disciplina) vêm da
  skill `resolver-exercicio`.
- As soluções são totalmente explícitas e **verificadas antes de as
  escrever**: contas em Python, equivalências por força bruta, código
  compilado e corrido contra os testes do lab.
- Lógica (Fitch):
  - escreve-se em blocos ```` ```{.fitch} ```` (`|` por nível, `|>` abre
    hipótese, `---` fecha premissas, `; &E, 2` é a justificação);
  - corre `python3 _shared/tools/fitch_check.py` sobre o RESUMO e as
    SOLUCOES antes de compilar. Nenhuma dedução pode falhar;
  - `.nocheck` só para deduções erradas de propósito.
- Exercícios abertos (IPM, desenho) levam uma **resposta-modelo**, dita
  como tal.
- Entregáveis avaliados do grupo (personas, missões): as regras de IA da
  disciplina proíbem gerá-los, por isso a solução é uma grelha de
  verificação mais um contraexemplo.
- Quando a prática traz soluções oficiais, compara-as com as nossas e
  assinala as diferenças sem apagar nenhuma das duas.
- Quando a ficha traz um exercício igual a um que inventámos, o oficial
  substitui o inventado. Do inventado ficam só as perguntas que a ficha
  não faz, renumeradas.
- Figuras das soluções: SVG (`dot -Tsvg`) em `figuras/sol_*.svg`, embutido
  no site (que funciona offline, com MathML).
