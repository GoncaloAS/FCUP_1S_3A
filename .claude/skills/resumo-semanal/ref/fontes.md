# Fontes fora do normal (ler só quando aparecem)

- **Aula em `.pptx`**: não há LibreOffice, e não o instales sem perguntar.
  - Fica como `Aula_NN.pptx`.
  - Lê-a com `python-pptx` num venv no scratchpad:
    `python3 -m venv .../venv && .../venv/bin/pip install python-pptx pillow`.
    O pip do sistema recusa (PEP 668).
  - Lê o texto **e as notas do orador** de cada slide. Extrai as imagens com
    `shape.image.blob` e vê só as que importam.
- **Capturas `.cap`** (Redes):
  - nome `Teoricas/Aula_NN_captura_<proto>.cap`;
  - lê-se com `tcpdump -nn -A -r` (não há Wireshark);
  - os números dos pacotes tiram-se com `tcpdump -# -nn -r` **sem filtro**
    (com filtro, a numeração não bate com a do Wireshark).
- **PDF que não é uma aula numerada** (livro, apontamentos de outro
  docente):
  - dá-lhe um nome descritivo dentro de `Teoricas/` e diz ao Gonçalo que
    foi uma decisão tua;
  - usa-o para preencher lacunas dos slides (com †). A estrutura e a
    terminologia continuam a ser as das aulas.
- **Enunciado de projeto ou ficha prática sem teórica nova**:
  - vai para `Praticas/Semana_N/`;
  - funde-se nas secções que já existem e não cria uma secção nova;
  - fica no `<!-- processado -->` se alterou o resumo;
  - se as datas do enunciado contradizem os slides, vale o enunciado.
- **Calendário ou sumários numa Google Sheet embutida**: troca `pubhtml`
  por `pub?output=csv` no mesmo URL.
- **Código dos slides** (`javac`, `gcc`):
  - corre-o, porque já apanhou erros reais;
  - em labs de geradores, usa o Bison do `brew install bison`
    (`/opt/homebrew/opt/bison/bin`), porque o do macOS é o 2.3;
  - `happy`/`alex` instalam-se com `cabal install` (ficam em `~/.cabal/bin`);
  - `happy -i` gera relatórios `.info` com conflitos reais.
- **Exercícios "corre este comando"** (`dig`, `telnet`): corre-os de
  verdade e mostra a saída real, com a data. Nunca faças ações com efeitos
  pelo Gonçalo (no SMTP, só `EHLO`/`QUIT`).
- **Módulos em vez de aulas** (IPM): o nome segue o número do módulo
  (`Module 04 · Lecture 3` → `Aula_04.pdf`), para manter Aula N = Módulo N.
