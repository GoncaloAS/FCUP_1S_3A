# Quizrama

Quizzes de estudo para testes da FCUP: **Sistemas de Operações** (`index.html`, `teste2.html`) e **Redes de Comunicação — 1.º teste** (`redes.html`).

## Redes de Comunicação (Teste 1)

- `redes.html` — 157 perguntas dos Capítulos 1–2 (matéria do 1.º teste), mais a escolha múltipla do teste modelo e treino da Parte II (cálculos e diagramas). Mostra a nota /20 com o desconto de 1/3 por errada.
- `guia_redes_teste1.html` — a matéria, gerada a partir do resumo de Redes; cada correção liga à secção certa.
- Para regenerar depois de o resumo mudar:

```bash
python3 tools/redes-guide/build.py      # guia + figuras + ids das secções
python3 tools/redes-guide/perguntas.py  # banco de perguntas (edita as perguntas aqui)
npm test
```

## Sistemas de Operações

Quiz interactivo para estudar **Sistemas de Operações** (FCUP 2025/2026), com ~540 perguntas de exames anteriores e treinos estilo exame, organizadas por tópico (C, processos, escalonamento, sincronização, deadlocks, IPC, etc.). Persistência local de progresso, modo retry, heatmap de respostas e atalhos de teclado.

Inclui um **gerador de guia de estudo** em formato `.docx` (Word), construído a partir de módulos JavaScript — útil para imprimir ou ler offline.

## Stack

- HTML5 + CSS3 + JavaScript ES2020 vanilla — **sem framework, sem bundler**.
- Node.js v20+ — apenas necessário para correr os smoke tests e o gerador de `.docx`.
- 1 dependência npm: `docx` (usada só pelo gerador de guia).

## Como correr localmente

A app é estática — basta servir os ficheiros. Qualquer servidor HTTP serve.

```bash
# Opção 1 — abrir directamente
open index.html         # macOS
xdg-open index.html     # Linux

# Opção 2 — servidor local (recomendado para evitar restrições de CORS)
python3 -m http.server 8000
# depois: http://localhost:8000/
```

## Como correr os smoke tests

```bash
npm test               # corre os 4 smoke tests
npm run validate       # smoke tests + node --check em todos os .js
```

Os tests usam só `assert` built-in do Node, sem framework adicional. Verificam:

- estrutura das 538 entradas em `output.js` (banco de perguntas);
- IDs DOM e funções globais referenciados pelo HTML existem nos módulos JS;
- todos os `<script src=…>` e `<link href=…>` apontam para ficheiros que existem;
- o gerador `tools/os-guide` carrega e monta um Document válido.

## Como gerar o guia de estudo `.docx`

```bash
npm run build:guide
# output: OS_Improved_Study_Guide.docx (na raiz)
```

## Estrutura do projecto

Ver [ARCHITECTURE.md](ARCHITECTURE.md) para detalhe.

```
.
├── index.html                  # entry-point da app web
├── output.js                   # banco de perguntas (define o global ALL)
├── sistemas_operacoes_estudo__2_.html  # guia de estudo (linkado pelas explicações)
├── assets/
│   ├── css/                    # tokens / layout / components
│   └── js/                     # data, core, ui, quiz, keyboard, boot
├── tools/os-guide/             # gerador de guia em .docx
│   ├── theme.js, primitives.js, tables.js, diagrams.js
│   └── content/chapter-NN-*.js
├── tests/smoke/                # smoke tests (Node puro)
├── docs/                       # material de estudo extra (.md)
├── ANALYSIS.md, ARCHITECTURE.md, REFACTOR_LOG.md, CONTRIBUTING.md
└── package.json, .gitignore
```

## Atalhos de teclado (na app)

- `1` `2` `3` `4` — selecciona opção A/B/C/D
- `←` `→` — pergunta anterior / seguinte
- `S` — skip (igual a `→`)
- `R` — refazer (apagar respostas dentro do filtro de tópico actual)
