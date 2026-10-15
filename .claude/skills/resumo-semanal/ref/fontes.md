# Fontes fora do normal (ler só quando aparecem)

As regras de **uma só** disciplina (módulos de IPM, `.cap` de Redes,
ferramentas de Compiladores, Fitch e tableaux de Lógica, site de
TecnologiasWeb) estão no `.fonte/CONTEXTO_<D>.md` dela, que o `prep.sh`
mostra. Aqui ficam os casos genéricos.

- **Aula em `.pptx`**: fica como `Aula_NN.pptx`. O `extrair.sh` lê-a
  sozinho (texto, tabelas e **notas do orador**), com o venv
  `_shared/.venv`, criado na 1.ª vez com `python-pptx` (o pip do sistema
  recusa, PEP 668; não há LibreOffice, e não o instales sem perguntar).
  Imagens: `shape.image.blob` nesse venv; vê só as que importam.
- **PDF que não é uma aula numerada** (livro, apontamentos de outro
  docente):
  - dá-lhe um nome descritivo dentro de `Teoricas/` e diz ao Gonçalo que
    foi uma decisão tua;
  - usa-o para preencher lacunas dos slides (com †): procura no cache
    (`grep -n` em `.fonte/.cache/<nome>.txt`) e lê só esses troços. A
    estrutura e a terminologia continuam a ser as das aulas.
- **Enunciado de projeto ou ficha prática sem teórica nova**:
  - vai para `Praticas/Semana_N/`;
  - funde-se nas secções que já existem e não cria uma secção nova;
  - fica no `<!-- processado -->` se alterou o resumo;
  - se as datas do enunciado contradizem os slides, vale o enunciado.
- **Código dos slides**: corre-o sempre, porque já apanhou erros reais (as
  ferramentas de cada disciplina estão no `CONTEXTO_<D>`).
- **Exercícios "corre este comando"**: corre-os de verdade e mostra a saída
  real, com a data. Nunca faças ações com efeitos pelo Gonçalo.
- **Disciplina nova**: cria `.fonte/RESUMO_<D>.md` com o esqueleto abaixo,
  junta-a a `ESTILO_V2` no `build.sh` e escreve um `CONTEXTO_<D>.md`. Entra
  sozinha no site de soluções quando ganha o seu `SOLUCOES_*.md`.

  ```markdown
  ---
  title: "<Disciplina> (<código>) --- Resumo Teórico"
  author: "Gonçalo Sousa"
  date: "Atualizado: Semana N"
  ---

  <!-- processado: Teoricas/Aula_01.pdf -->

  # Aula 1 --- <título>
  ```
