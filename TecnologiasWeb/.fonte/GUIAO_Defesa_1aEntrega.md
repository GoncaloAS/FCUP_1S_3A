---
title: "Alquerque — Defesa da 1.ª entrega"
subtitle: "Como funciona o site todo, o que o professor vai testar e as perguntas que pode fazer"
---

<!-- Fonte: código do repositório github.com/hugobolotoreis-wq/Tec-web
     (commit 297b5be), lido e validado no W3C a 3 nov 2026. Substitui o
     guião da apresentação: afinal não há apresentação, o professor testa
     o jogo à nossa frente e faz perguntas. -->

## Como usar este documento

- **Parte 1 — O esquema do site:** como o site funciona de ponta a ponta,
  em 4 diagramas. Quem perceber esta parte consegue responder a quase
  tudo por palavras suas.
- **Parte 2 — O professor a testar:** o que ele vai provavelmente
  experimentar, o que acontece e porquê, e as limitações que convém
  dizer antes de ele as encontrar.
- **Parte 3 — Perguntas e respostas:** por tema. Cada resposta tem a
  **frase para dizer** e, quando ajuda, **onde está no código**.
  A §3.0 é um mini-dicionário para quem não programa para a web.

Regra de ouro: **o professor pode perguntar a qualquer um de nós**. Não é
preciso saber o código de cor; é preciso saber **explicar o que faz** e
**em que ficheiro está** (no VS Code, `Cmd+Shift+F` e o nome da função).

# Parte 1 — O esquema do site

## 1.1 O site num relance

É uma **página única** (`index.html`) sem bibliotecas: HTML para a
estrutura, CSS para o aspeto, JavaScript para o comportamento. O JS está
dividido em três camadas: os **dados e as regras** não sabem nada do
ecrã; o **jogo** decide o que acontece; o **ecrã** só desenha o que o
jogo diz.

![](figuras/trab_arquitetura.pdf){width=88%}

| Ficheiro | Responsabilidade |
|---|---|
| `constantes.js` | Números fixos: tamanho 5, cores, tempos, medidas em píxeis, direções |
| `pecas.js` | Classes `Position` (linha, coluna, diagonais, andar) e `Piece` (cor); funções `corAdversaria`, `sentidoFrente`, `ultimaFila` |
| `tabuleiro.js` | Classe `Board`: a matriz 5 × 5 e **todas as regras** (movimentos, capturas, gerar jogadas, copiar) |
| `jogo.js` | Classe `Game`: de quem é a vez, os modos, os cliques, o sopro, o empate, o fim |
| `ia.js` | As três estratégias do computador |
| `interface.js` | Desenhar linhas e peças, destaques, animar, mensagens |
| `classificacoes.js` | Guardar e mostrar resultados (localStorage) |
| `identificacao.js` | Entrar, registar, sair |
| `comandos.js` | Liga os botões às funções e arranca tudo |

## 1.2 O que acontece quando a página abre

1. O navegador lê o HTML de cima para baixo e carrega os 5 CSS do
   `<head>` (`<link rel="stylesheet">`).
2. Desenha as áreas. Os painéis de **Instruções** e **Classificações** e
   o formulário de **Registar** já estão no HTML, mas com a classe
   `escondido` (`display: none`).
3. No fim do `<body>` carrega os 9 scripts **por ordem**: primeiro o que
   é usado (constantes, classes), por último quem usa.
4. O último, `comandos.js`, faz três coisas:
   `let nomeJogador = "Anónimo"`, `const jogo = new Game()` (cria o
   tabuleiro na posição inicial, modo `fimDeJogo`) e `prepararPagina()`.
5. `prepararPagina()` põe um `addEventListener("click", ...)` em cada
   botão, desenha as 16 casas das linhas (`desenharLinhas`, uma só vez)
   e as 25 posições (`desenharTabuleiro`).
6. A partir daqui **nada corre sozinho**: tudo começa num clique.

## 1.3 Uma vez de jogo, do princípio ao fim

![](figuras/trab_vez.pdf){width=72%}

A ideia central: **no início de cada vez, o jogo calcula a lista de todas
as jogadas válidas** (`gerarJogadas`). Com essa lista:

- o **humano** só consegue fazer jogadas que lá estão (é assim que se
  validam os cliques) e os destaques mostram-nas;
- o **computador** escolhe uma delas com a IA.

Por isso as regras estão **num só sítio** (`tabuleiro.js`) e valem para
os dois jogadores.

## 1.4 Os modos (o que um clique faz depende do modo)

![](figuras/trab_modos.pdf){width=80%}

`jogo.modo` guarda o modo e `cliqueCasa(linha, coluna)` faz um `switch`
sobre ele. Durante uma animação (`aAnimar = true`) os cliques são
ignorados.

## 1.5 Um clique, passo a passo

Exemplo: és tu a jogar, já tens uma peça selecionada e clicas num destino
amarelo.

1. O círculo clicado tem um *listener* criado em `criarPosicao(l, c)`,
   que chama `jogo.cliqueCasa(l, c)`.
2. Modo `pecaSelecionada` → `cliquePecaSelecionada(pos)`.
3. `procurarJogada(selecionada, pos)` procura na lista de jogadas válidas
   uma com essa origem e esse primeiro destino. Se não há →
   "Jogada inválida." (a caixa de mensagens pulsa).
4. Se há: `animarEDepois` → `animarPeca` muda o `left`/`top` do círculo e
   o CSS (`transition: left 0.3s, top 0.3s`) fá-lo deslizar.
5. Passados 300 ms (`setTimeout`), a matriz é atualizada: movimento →
   `moverPeca`; captura → `saltar` (a peça saltada fica
   `capturada = true`, cinzenta).
6. Se ainda há saltos → modo `capturaMultipla`; senão → `terminarJogada`
   → vez do computador.
7. `desenharTabuleiro()` apaga e recria os 25 círculos a partir da
   matriz: **o ecrã é sempre uma cópia da matriz**.

## 1.6 Onde fica guardado o quê

| Informação | Onde | Dura até |
|---|---|---|
| Estado do jogo (tabuleiro, vez, modo) | objeto `jogo` (classe `Game`), em memória | recarregar a página |
| Nome de quem fez login | variável global `nomeJogador` (`comandos.js`) | recarregar a página ou Sair |
| Senha | **em lado nenhum**: é lida, verificada (não vazia, igual à confirmação) e o campo é limpo | — |
| Classificações | `localStorage`, chave `alquerqueClassificacoes`, em JSON | apagar os dados do navegador |
| Configuração (nível, quem começa) | lida dos `<select>` ao clicar em Iniciar | — |

Não usamos cookies, `sessionStorage` nem servidor nesta entrega.

## 1.7 Como o HTML, o CSS e o JS conversam

- **JS → HTML:** encontra elementos por `id` (`getElementById`), cria-os
  (`createElement`, `appendChild`), muda texto (`textContent`).
- **JS → CSS:** quase sempre **pondo e tirando classes**
  (`classList.add/remove`): `escondido`, `azul`, `selecionada`,
  `destaque`... O aspeto de cada classe está no CSS. A exceção é a
  posição das peças: o JS escreve `style.left`/`style.top`, porque
  depende de contas.
- **HTML → JS:** os eventos (`click`) chamam as funções do JS.

\newpage

# Parte 2 — O professor a testar o jogo

## 2.1 Antes de ele chegar

- `index.html` aberto no navegador, com 2 ou 3 jogos já feitos (para as
  Classificações não estarem vazias).
- VS Code aberto na pasta do trabalho (`Cmd+Shift+F` para procurar).
- Dois separadores com os validadores já corridos e verdes (§3.2):
  `validator.w3.org/nu` com o `index.html` e
  `jigsaw.w3.org/css-validator` com os CSS.
- Combinar quem responde a quê (sugestão: regras e IA — Hugo; código e
  estrutura — Gonçalo; HTML/CSS e áreas — Matilde), mas **todos** leem a
  Parte 1.

## 2.2 O que ele vai provavelmente experimentar

| Ele faz | O que acontece | Porquê / onde |
|---|---|---|
| Clica numa casa antes de iniciar | Nada | modo `fimDeJogo`: `cliqueCasa` ignora |
| Iniciar com "Eu" primeiro | "É a tua vez." e as tuas peças com jogadas ficam com contorno branco | `iniciar` → `iniciarVez` → `marcarDestaques` |
| Iniciar com "Computador" primeiro | Espera 1,1 s e o computador joga | `iniciarVezComputador` + `setTimeout(ESPERA)` |
| Clica numa peça que não se pode mexer | "Jogada inválida: essa peça não tem jogadas." | `cliqueEsperaJogada` |
| Clica numa casa vazia ou peça vermelha | "Jogada inválida." (a não ser que seja soprável) | idem |
| Tenta andar para trás | Não aparece destino amarelo; clicar lá dá "Jogada inválida." | `movimentosSimples` salta a direção contrária a `sentidoFrente` |
| Tenta andar na diagonal numa casa sem diagonal | Idem | `temDiagonais()`: só onde `linha % 2 === coluna % 2` |
| Põe uma peça na última fila e tenta subir/diagonal | Só aparecem destinos horizontais | `ultimaFila` em `movimentosSimples` |
| Captura | A peça desliza por cima, a saltada fica cinzenta e sai no fim da jogada | `saltar`, `terminarJogada` |
| Captura e ainda dá para saltar | "Tens de continuar a capturar com esta peça." e novos destinos | modo `capturaMultipla` |
| Na captura múltipla clica na própria peça | Para a captura; a peça fica soprável para o computador | `cliqueCapturaMultipla` + `calcularSopraveis` |
| Podia capturar e faz um movimento simples | Aviso ao selecionar; no médio (50 %) e difícil (sempre) o computador sopra-lhe uma peça | `selecionarPeca`, `computadorSopra` |
| O computador não captura quando podia | A peça vermelha aparece com contorno tracejado; ao clicar nela é soprada e depois joga-se | `soprar` |
| Clica durante a vez do computador ou a meio de uma animação | Nada | modo `vezComputador` / `aAnimar` |
| Propor empate logo no início | "O computador recusou o empate." | só aceita com ≥ 20 jogadas seguidas sem capturas |
| Propor empate a meio de uma captura múltipla | "Só podes propor empate no início da tua vez." | `proporEmpate` |
| Desistir | "Desististe, perdeste." e conta uma derrota | `desistir` |
| Desistir sem jogo | "Não há nenhum jogo a decorrer." | idem |
| Instruções / Classificações | Painel por cima com o resto da página escurecido; Fechar esconde-o | `abrirPainel`/`fecharPainel`, `.painel` |
| Entrar com campos vazios | "Preenche o utilizador e a senha." | `entrar` |
| Registar com senhas diferentes | "As senhas não são iguais." | `registar` |
| Faz login, ganha um jogo, abre Classificações | Aparece uma linha com o nome e o nível | `registarResultado`, `preencherClassificacoes` |
| Recarrega a página (F5) | O jogo e o login perdem-se; as classificações ficam | §1.6 |
| Inspecionar → Application → Local Storage | Vê a chave `alquerqueClassificacoes` com o JSON | `classificacoes.js` |
| Abre a consola (F12) | Não deve haver erros (confirmar antes de ele chegar) | — |

## 2.3 Limitações conhecidas — dizer com calma se ele as encontrar

Não são erros: são escolhas desta entrega. Dizer o porquê e o que se
faria.

| Limitação | O que dizer |
|---|---|
| O login aceita qualquer nome e senha, e "Entrar" funciona sem ter registado antes | O enunciado diz que na 1.ª entrega não se autentica; a área existe e valida os campos. A verificação vem com o servidor (`register` na 2.ª entrega). |
| Ao recarregar, o login perde-se | O nome está numa variável em memória. Para sobreviver ao F5 bastava `sessionStorage.setItem("nome", nome)` e lê-lo ao abrir. |
| Duas pessoas com o mesmo nome partilham a linha nas classificações | Não há contas; a chave é o nome. Com o servidor a chave é o utilizador autenticado. |
| A tabela não está ordenada | Mostra os resultados pela ordem em que os jogadores apareceram. Para ordenar: pôr as linhas num array e `sort` por vitórias. |
| `Enter` nos campos do login não entra | Os campos não estão dentro de um `<form>` e os botões são `type="button"`. Com `<form>` + `submit` e `preventDefault()` o Enter funcionava. |
| Iniciar um jogo novo a meio não conta derrota | Só contam vitórias, derrotas por fim de jogo, desistências e empates aceites. |
| Não se adapta a ecrãs pequenos | Larguras fixas (tabuleiro 400 px, coluna 250 px) e sem *media queries*; pensado para computador. |
| O tabuleiro não se joga com o teclado | As posições são `div` com clique; para teclado seriam `button` ou `tabindex`. |

\newpage

# Parte 3 — Perguntas e respostas

## 3.0 Mini-dicionário (ler primeiro)

| Palavra | O que é, em linguagem simples |
|---|---|
| **HTML** | A estrutura da página: que caixas, botões e textos existem. É o `index.html`. |
| **CSS** | O aspeto: cores, tamanhos, posições, animações. Pasta `css/`. |
| **JavaScript (JS)** | O comportamento: o que acontece quando se clica. Pasta `js/`. |
| **Elemento** | Uma "caixa" da página, por exemplo `<div>`, `<button>`, `<p>`. |
| **id** | Nome único de um elemento (`id="tabuleiro"`); o JS encontra-o com `getElementById`. |
| **classe CSS** | Etiqueta num elemento (`class="posicao azul"`) que lhe dá um estilo. Pode ter várias. |
| **classList** | Como o JS põe e tira classes: `elem.classList.add("azul")`, `.remove(...)`. |
| **DOM** | A árvore de todos os elementos da página, que o JS pode ler e alterar. |
| **createElement / appendChild** | Criar um elemento novo e metê-lo dentro de outro. |
| **Evento / addEventListener** | "Quando acontecer X, corre esta função." |
| **Classe (JS) / método** | Um molde para criar objetos com dados e funções (`Board`, `Game`); as funções da classe são métodos. |
| **`this`** | Dentro de um método, o próprio objeto. |
| **Matriz** | Tabela de linhas e colunas: `casas[linha][coluna]`. |
| **`null`** | "Não há nada": casa vazia. |
| **Array** | Lista: `push` acrescenta ao fim, `pop` tira do fim. |
| **setTimeout** | "Corre esta função daqui a N ms", sem bloquear a página. |
| **transition** | O navegador muda uma propriedade aos poucos em vez de saltar. |
| **@keyframes / animation** | Animação CSS por etapas (0%, 40%, 100%). |
| **position: absolute** | Pôr um elemento num ponto (x, y) dentro do pai que tem `position: relative`. |
| **localStorage** | Memória do navegador que não se apaga ao fechar. Só guarda texto. |
| **JSON** | Forma de escrever objetos como texto, para os guardar. |
| **Recursão** | Uma função que se chama a si própria. |
| **SPA** | *Single-page application*: tudo numa só página; o JS mostra e esconde partes. |

## 3.1 Estrutura geral

**P: Como está organizado o projeto?**
Um `index.html`, 5 CSS (um por área) e 9 JS, cada um com uma
responsabilidade (tabela em §1.1). Os dados e as regras estão separados
do desenho.

**P: É uma aplicação de página única? Como mudam as "páginas"?**
Sim. Os painéis e os formulários já estão no HTML com a classe
`escondido` (`display: none`). Abrir = tirar a classe; fechar = pô-la
(`abrirPainel`/`fecharPainel` em `comandos.js`, `mostrarSeparador` no
login).

**P: Usaram alguma biblioteca ou framework?**
Não. HTML, CSS e JavaScript puros.

**P: Porque é que os `<script>` estão no fim do `<body>`?**
Para que, quando o JS corre, os elementos já existam; senão o
`getElementById` devolvia `null`. (Alternativa: `<script defer>` no
`<head>`.)

**P: A ordem dos scripts importa?**
Sim. Os scripts partilham o mesmo espaço global e uma classe tem de estar
definida antes de se usar: primeiro constantes e classes, por último o
`comandos.js`, que faz `new Game()` e `prepararPagina()`.

**P: Porque é que os botões têm `type="button"`?**
Um botão dentro de um formulário, por omissão, submete-o e recarrega a
página. Com `type="button"` só corre o nosso JS.

## 3.2 Validação (HTML, CSS, formulário e jogadas)

"Validar" pode querer dizer quatro coisas; ter as quatro na cabeça.

**P: Como validaram o HTML e o CSS?**
Com os validadores oficiais do W3C, como o enunciado exige:

- **HTML:** *Nu HTML Checker*, `validator.w3.org/nu` → "File upload" do
  `index.html` → "Check". Resultado: **0 erros e 0 avisos**.
- **CSS:** *CSS Validation Service*, `jigsaw.w3.org/css-validator` →
  "By file upload", um ficheiro de cada vez (perfil CSS3). Resultado: os
  **5 ficheiros com 0 erros e 0 avisos**.

Voltámos a correr os dois a 3 nov 2026 sobre a versão entregue.

**P: Tiveram algum erro do validador pelo caminho? O que costuma dar
erro?**
*(Dizer a verdade sobre o que aconteceu.)* Erros típicos: `<label for>`
a apontar para um `id` que não existe, `id` repetidos, elementos fechados
fora de ordem, faltar o `lang` ou o `charset`, propriedades CSS
inventadas ou com prefixos (`-webkit-...`). Por isso cada `label` tem o
`for` igual ao `id` do campo e não usamos prefixos.

**P: Que propriedades CSS "arriscadas" usam e passam?**
`linear-gradient` com `calc()` (as diagonais), `radial-gradient` (peças
3D), `box-shadow`, `transition`, `@keyframes`, `transform: scale`. Tudo
CSS3 padrão: o validador aceita.

**P: Como validam o formulário de login?**
No JS, ao clicar: `trim()` ao nome; se o nome ou a senha estão vazios →
"Preenche o utilizador e a senha."; no registo, se a senha e a
confirmação são diferentes → "As senhas não são iguais." O aviso aparece
no `<p id="avisoIdentificacao">`. Não usámos `required` do HTML porque os
campos não estão num `<form>` e queríamos a mensagem na nossa área.

**P: Como validam as jogadas do humano?**
Não há regras repetidas: no início da vez, `gerarJogadas` calcula todas
as jogadas válidas. Um clique só é aceite se corresponder a uma delas
(`jogadasDaPeca`, `procurarJogada`); senão aparece "Jogada inválida". As
mesmas jogadas alimentam a IA, por isso o computador também nunca faz
jogadas ilegais.

## 3.3 Login e o que fica guardado

**P: Como guardam o login?**
Nesta entrega o login não autentica (o enunciado permite). Depois de
validar os campos, `iniciarSessao(nome)` guarda **só o nome** na variável
global `nomeJogador`, esconde o formulário (`#semSessao`), mostra
"Olá, nome!" e o botão Sair (`#comSessao`) e limpa os campos. Sem login o
nome é "Anónimo". Esse nome é a chave das classificações.

**P: E a senha?**
Não é guardada em lado nenhum: só se verifica que não está vazia (e no
registo que é igual à confirmação) e o campo é limpo. Guardar senhas no
navegador, em texto, seria inseguro; na 2.ª entrega é o servidor que as
verifica.

**P: Porque não guardar a senha no localStorage? Outros sites podem
lê-lo?**
Outros sites **não** podem: cada origem (protocolo + domínio + porta) tem
o seu localStorage (*same-origin policy*). Não se guarda lá a senha
porque: fica em texto simples no computador (vê-se em F12 → Application →
Local Storage); qualquer script que corra **na nossa página** a lê,
incluindo código injetado por XSS (as cookies podem ter `HttpOnly`, o
localStorage não tem proteção nenhuma); e não é precisa, porque quem a
verifica é o servidor. Atenção: localStorage **não** é onde ficam as
cookies; são coisas diferentes (tabela abaixo).

**P: Registar e Entrar fazem coisas diferentes?**
Visualmente sim (dois formulários; o de registo pede confirmação), mas os
dois acabam em `iniciarSessao`: não há lista de contas. Na 2.ª entrega o
"Registar/Entrar" passa a ser o pedido `register` ao servidor, que cria
a conta ou verifica a senha.

**P: O que faz o Sair?**
`sair()`: volta a pôr `nomeJogador = "Anónimo"`, esconde "Olá" e volta a
mostrar o formulário de Entrar.

**P: E se recarregar a página?**
O login e o jogo perdem-se (estão em memória); as classificações ficam
(estão no localStorage).

**P: Onde guardam as classificações e como?**
No `localStorage`, chave `alquerqueClassificacoes`. Como só guarda texto,
`JSON.stringify` para gravar e `JSON.parse` para ler. Formato:
`{ nome: { nivel: { vitorias, derrotas, empates } } }`.
`registarResultado` lê, cria o que falta a zeros, soma 1 e grava. Fica
mesmo fechando o navegador, mas só nesse navegador e nesse computador.

**P: Porquê localStorage e não sessionStorage ou cookies?**

| | Dura | Vai ao servidor? | Para quê |
|---|---|---|---|
| `localStorage` | até se apagar | não | classificações (queremos que fiquem) |
| `sessionStorage` | até fechar o separador | não | servia para o login sobreviver ao F5 |
| cookies | data de validade | sim, em cada pedido | sessões no servidor; não temos servidor |

**P: Como é feita a tabela das classificações?**
`preencherClassificacoes` apaga as linhas antigas, lê o JSON e, com
`for...in` sobre os nomes e um ciclo sobre os 3 níveis, cria um `<tr>`
por jogador e nível (`criarLinha`, com `createElement("td")` e
`textContent`). Sem dados: "Ainda não há resultados". Riscas alternadas
com `tr:nth-child(even)` no CSS.

**P: Porque `textContent` e não `innerHTML`?**
Com `textContent` o nome é sempre texto. Se alguém se registasse com
`<img src=x onerror=...>` como nome, com `innerHTML` isso corria
(*XSS*); com `textContent` aparece escrito.

## 3.4 Os dados: como representam o tabuleiro

**P: Como guardam o estado do tabuleiro?**
`Board.casas`, matriz 5 × 5. Cada casa é `null` (vazia) ou um `Piece`
com a `cor` (`"azul"`/`"vermelha"`) e `capturada`. Desenhar, validar
cliques e a IA trabalham todos sobre esta matriz.

**P: Como fazem a posição inicial?**
`posicaoInicial()`: linhas 0–1 vermelhas, 3–4 azuis; na linha do meio
colunas 0–1 vermelhas, 3–4 azuis e o centro vazio. 12 de cada.

**P: Como sabem se uma posição tem diagonais?**
`temDiagonais()`: `linha % 2 === coluna % 2` (ambas pares ou ambas
ímpares). `direcoes()` devolve então as 8 direções, senão só as 4 retas.

**P: O que é uma "direção"?**
Um par `[Δlinha, Δcoluna]`: `[-1, 0]` é para cima, `[1, 1]` é diagonal
para baixo-direita. `andar(direcao, passos)` dá a posição a 1 ou 2 casas.

**P: Porque usaram classes?**
O enunciado valoriza a orientação a objetos: cada coisa fica com os seus
dados e funções. `Position` sabe se está dentro e para onde pode andar,
`Board` sabe as regras, `Game` sabe de quem é a vez. O `Board` são os
dados que na 2.ª entrega se trocam com o servidor.

## 3.5 Gerar o tabuleiro no ecrã

**P: Como geram o tabuleiro?**
Duas camadas dentro de `#tabuleiro` (400 × 400 px, `position: relative`):

1. **Linhas** (`desenharLinhas`, uma vez): 16 quadrados (4 × 4) com borda
   de 3 px; as bordas fazem as linhas retas. A diagonal de cada quadrado
   é um `linear-gradient` transparente exceto numa faixa de 3 px no meio;
   `diagDesce` ou `diagSobe` conforme o canto tem diagonais, o que dá o
   padrão em losango.
2. **Peças** (`desenharTabuleiro`): apaga e cria 25 círculos (`div`) a
   partir da matriz, com as classes `vazia`/`azul`/`vermelha` e os
   destaques.

**P: Como sabem onde pôr cada peça?**
`position: absolute` e `centro(i) = 40 + i × 80` (`MARGEM`, `ESPACO`). O
raio é 25, logo `left = centro(coluna) − 25`, `top = centro(linha) − 25`.

**P: Porque é que os quadrados têm 83 px e não 80?**
Borda de 3 px: os vizinhos sobrepõem a borda, a linha não fica a dobrar.
Recuam 1,5 px para a linha ficar centrada.

**P: Porque redesenham as 25 peças sempre?**
É mais simples e o ecrã nunca fica diferente dos dados. Com 25
elementos é instantâneo.

**P: Como é que o clique sabe em que casa foi?**
Em `criarPosicao(linha, coluna)` cada círculo recebe
`addEventListener("click", function () { jogo.cliqueCasa(linha, coluna); })`.
A função "lembra-se" da `linha` e `coluna` com que foi criada (uma
*closure*).

**P: Como fazem as peças parecerem 3D?**
`radial-gradient` com um ponto claro em cima à esquerda e `box-shadow`.

**P: Porque não canvas ou SVG?**
Nesta fase pede-se o tabuleiro com elementos HTML e CSS manipulados pela
DOM. O canvas é melhoria da 2.ª entrega.

**P: E os destaques?**
`marcarDestaques` decide, conforme o modo:

| Classe | Aspeto | Quando |
|---|---|---|
| `temJogada` | contorno branco | peça tua que se pode mexer |
| `podeCapturar` | brilho amarelo | peça tua que pode capturar |
| `selecionada` | contorno amarelo grosso | a peça escolhida |
| `destino` | amarelo claro tracejado | para onde podes ir |
| `sopravel` | contorno amarelo tracejado | vermelha que podes soprar |
| `capturada` | cinzenta, transparente | saltada, sai no fim da jogada |
| `clicavel` | mãozinha + cresce 12 % | tudo o que se pode clicar |

## 3.6 Layout e CSS da página

**P: Como fizeram as duas colunas?**
`#principal` tem `display: flex`; a coluna esquerda tem 250 px fixos e a
do jogo `flex: 1` (ocupa o resto). `max-width: 1000px` + `margin: 0 auto`
centra tudo. Os separadores Entrar/Registar também são flex, com
`flex: 1` cada (metade-metade).

**P: Porque é que os painéis aparecem por cima, com o fundo escuro?**
`.painel` tem `position: fixed` (fica no mesmo sítio mesmo com scroll),
`left: 0; right: 0; width: 600px; margin: 0 auto` para centrar e uma
`box-shadow` de 2000 px semitransparente que escurece o resto da página.
`max-height: 80%` + `overflow-y: auto` dá scroll se o texto for grande.

**P: Como é que o botão Iniciar fica amarelo se todos os botões são
verdes?**
Especificidade: `button` (só elemento) < `#comandos button` (1 id) <
`#comandos #botaoIniciar` (2 ids). Ganha a regra mais específica.

**P: Para que serve o `box-sizing: border-box`?**
Os `input` têm `width: 100%` e padding; sem `border-box` o padding
somava-se à largura e passavam da caixa. Com ele a largura inclui padding
e borda. Usamos também nos quadrados e nos círculos.

**P: Usaram HTML semântico?**
Sim: `<header>` (logótipo), `<main>`, `<section>` para cada área com
`<h2>`, `<h1>` só um, `<table>` com `<thead>`/`<tbody>`/`<th>`, `<label
for>` em todos os campos, `type="password"`, `autocomplete`,
`lang="pt"` e `<meta charset="utf-8">`.

## 3.7 As animações

**P: Como fizeram a peça deslizar?**
`.posicao` tem `transition: left 0.3s, top 0.3s`. `animarPeca` muda o
`left`/`top` do círculo para o destino e o navegador anima; a classe
`aMover` (`z-index: 10`) põe-na por cima das outras. `animarEDepois`
espera 300 ms com `setTimeout` e só então atualiza a matriz e redesenha.

**P: E se clicar durante a animação?**
`aAnimar` está a `true` e `cliqueCasa` ignora o clique.

**P: Como fizeram a caixa das mensagens pulsar?**
`@keyframes pulsar` em `mensagens.css` (cresce 3 % com uma onda laranja),
ligado à classe `destaque`. `mostrarMensagem` tira a classe, faz
`void caixa.offsetWidth` e volta a pô-la.

**P: Para que serve o `void caixa.offsetWidth`?**
Tirar e pôr a classe seguidas não é notado e a animação não recomeça.
Ler `offsetWidth` obriga o navegador a recalcular o *layout* entre as
duas, por isso a animação corre de novo a cada mensagem.

**P: Outras animações?**
Hover nas peças clicáveis (`transform: scale(1.12)`, 0,15 s) e nos botões
(`transition: background-color 0.2s`).

**P: Porque é que o computador joga devagar?**
1,1 s (`ESPERA`) entre cada passo, com `setTimeout`, para se perceber o
que ele fez, sobretudo nas capturas múltiplas.

## 3.8 Os modos e o jogo

**P: Que modos há?** Ver o diagrama em §1.4.

| Modo | Um clique faz |
|---|---|
| `esperaJogada` | peça tua com jogadas → seleciona; vermelha soprável → sopra; resto → "Jogada inválida" |
| `pecaSelecionada` | destino válido → joga; a mesma peça → cancela; outra peça tua → troca |
| `capturaMultipla` | destino de captura → salta; a tua peça → para (fica soprável) |
| `vezComputador`, `fimDeJogo` | nada |

**P: Como sabe o jogador em que modo está?**
Pelos destaques, pelo cursor, pela etiqueta "Vez: tu (azuis)" / "Vez:
computador" e pela mensagem no topo.

**P: O que é o `self = this`?**
Dentro de uma `function` passada ao `setTimeout`, `this` deixa de ser o
jogo. Guardamos o jogo em `self` antes. (Uma *arrow function* `() => {}`
também resolvia, porque mantém o `this` de fora.)

**P: O `setTimeout` bloqueia a página?**
Não. O JS tem uma só *thread*: o `setTimeout` agenda a função e devolve
logo; a página continua a responder. Por isso é preciso o `aAnimar` e o
modo `vezComputador` para ignorar cliques. Ao desistir ou iniciar um jogo
novo fazemos `clearTimeout(this.temporizador)` para cancelar o que estava
agendado.

## 3.9 As regras: movimentos, capturas e sopro

**P: Como geram todas as jogadas válidas?**
`gerarJogadas(cor)`: para cada peça dessa cor junta `movimentosSimples` e
`procurarCapturas`. Cada jogada é `{ origem, caminho, capturadas, tipo }`.

**P: Como garantem que não recua e que na última fila só anda na
horizontal?**
`sentidoFrente`: −1 para as azuis (sobem), +1 para as vermelhas. Uma
direção com Δlinha contrária é saltada. Na `ultimaFila` só passam as
direções com Δlinha = 0. O destino tem de estar dentro e vazio.

**P: Como verificam uma captura?**
`saltosPossiveis`: em cada direção, casa do meio (1 passo) e destino (2
passos). Há salto se o destino está dentro e vazio, o meio tem uma peça
do adversário ainda não saltada e o destino ainda não está no caminho. As
capturas podem ser para trás. As direções são as da posição de partida
(`direcoes()`): só se salta na diagonal onde há linha diagonal.

Exemplo: azul em (2,2), que tem diagonais. Na direção "para cima"
`[-1, 0]`, o meio é (1,2) e o destino é (0,2). Se em (1,2) está uma
vermelha e (0,2) está vazia, há salto: `{ destino: (0,2), saltada: (1,2) }`.
Se o meio está vazio, tem uma azul ou o destino está fora ou ocupado,
essa direção não dá.

**P: Como sabem que peças podem capturar (as do brilho amarelo)?**
`pecasQuePodemCapturar(cor)` em `tabuleiro.js`: percorre as 25 casas e,
para cada peça dessa cor, chama `saltosPossiveis`; se houver pelo menos um
salto, a posição vai para a lista. É calculada no início de cada vez
(`iniciarVez` → `jogo.podiamCapturar`) e serve para três coisas:

1. **destaque:** `marcarPecaComJogada` põe a classe `podeCapturar`
   (brilho amarelo) em vez de `temJogada` (contorno branco);
2. **aviso:** selecionar outra peça mostra "Atenção: esta peça não
   captura…" e a mensagem da vez diz que tens capturas;
3. **sopro:** se no fim da jogada não capturaste, `calcularSopraveis` usa
   esta lista para saber que peças o adversário te pode soprar.

**P: Como encontram as capturas múltiplas?**
Recursão com *backtracking* (`procurarCapturas`): experimenta cada salto,
acrescenta-o ao caminho, chama-se a partir do novo sítio; quando não há
mais saltos guarda a sequência; depois desfaz (`pop`) e experimenta o
seguinte. Encontra todos os caminhos sem repetir posições nem peças.
Cada sequência encontrada é uma jogada
`{ origem, caminho: [partida, salto1, salto2…], capturadas: [peça1, peça2…], tipo: "captura" }`.

**P: Como é que uma peça é capturada, do clique até sair do tabuleiro?**
Humano (um salto de cada vez, porque ele escolhe o caminho):

1. Clica na sua peça → `selecionarPeca`; os destinos amarelos são os
   primeiros saltos das jogadas dessa peça (`destinosSelecionada`).
2. Clica num destino → `procurarJogada` confirma que é uma jogada
   válida; `animarEDepois` faz a peça deslizar 300 ms.
3. `saltar(destino, saltada)`: `moverPeca` leva a peça para o destino,
   a saltada fica `capturada = true` (cinzenta, ainda no tabuleiro) e o
   destino e a saltada entram em `caminho` e `capturadas`.
4. `continuarOuTerminar`: se `saltosPossiveis` ainda dá saltos a partir
   do novo sítio → modo `capturaMultipla` e repete do passo 2; senão (ou
   se clicar na própria peça para parar) → `terminarJogada`.
5. `terminarJogada` faz `removerPeca` a cada posição de `capturadas`: só
   aqui as peças saem, o contador de jogadas sem captura volta a 0 e a
   contagem por baixo do tabuleiro desce.

Computador: a IA escolhe já a sequência inteira (uma jogada de
`gerarJogadas`). `passoComputador` faz cada salto com animação e 1,1 s
entre saltos, chamando o mesmo `saltar`, e no fim o mesmo
`terminarJogada` remove as peças.

**P: Podia capturar mais uma para trás e o jogo acabou a jogada. Porquê?**
A captura para trás é permitida e não há limite de capturas seguidas,
mas cada salto tem de cumprir as regras. O caso típico é o salto seguinte
**cair numa posição por onde a peça já passou**, muitas vezes a casa de
partida. O enunciado proíbe-o ("sem passar duas vezes pela mesma
posição"; a figura "a 4.ª voltaria a (2,0)" é este caso) e o código
verifica-o com `contemPosicao(caminho, destino)`. Outros motivos: o salto
seria na diagonal a partir de uma posição sem diagonais, o destino está
ocupado ou fora do tabuleiro. Quando não há mais saltos válidos, a
jogada acaba sozinha (`continuarOuTerminar`).
Uma peça já saltada (cinzenta) nunca bloqueia um destino: todos os
destinos de uma sequência estão a um número par de casas da partida e as
peças saltadas a um número ímpar (testado em 200 000 tabuleiros
aleatórios, 4 nov 2026: nenhum caso).

**P: As peças saltadas saem logo?**
Não: ficam `capturada = true` (cinzentas) e saem em `terminarJogada`,
para não serem saltadas outra vez durante a mesma sequência.

**P: Capturar é obrigatório. O jogo obriga?**
Não, de propósito: é a regra do sopro. O jogo avisa e deixa jogar.

**P: Como funciona o sopro?**
`calcularSopraveis()` no fim de cada jogada:

- capturou mas **parou a meio** → a peça que parou fica soprável;
- **não capturou** e havia peças que podiam → essas ficam sopráveis (se
  a que devia capturar se mexeu, conta a nova posição).

Na vez seguinte o adversário pode soprar **uma**: o humano clica na
vermelha tracejada (`soprar`); o computador decide em `computadorSopra`
conforme o nível. Depois a vez continua.

**P: Quando acaba o jogo?**
Perde quem, na sua vez, não tem jogadas (sem peças também). Desistir é
perder. Empate só por acordo.

## 3.10 A inteligência artificial

**P: Como funciona?**
Gera todas as jogadas válidas (a mesma `gerarJogadas`) e escolhe uma
(`escolherJogada` em `jogo.js`, estratégias em `ia.js`):

| Nível | Escolhe | Sopra? |
|---|---|---|
| Fácil | ao calhas (`jogadaAleatoria`) | nunca |
| Médio | 50 % ao calhas, 50 % gulosa | 50 % das vezes |
| Difícil | gulosa + olha a resposta do humano | sempre que pode |

**P: O que é a gulosa?**
A que captura mais peças agora; empates resolvidos ao calhas.

**P: E o difícil?**
Entre as que capturam o máximo, experimenta cada uma numa **cópia** do
tabuleiro (`copiar` + `aplicarJogada`) e mede a maior captura que o
humano faria a seguir (`maiorCaptura`). Escolhe a que deixa o humano com
menos.

**P: Porque uma cópia?**
Para experimentar sem estragar o tabuleiro verdadeiro.

**P: Usaram Minimax?**
Não, era opcional. O difícil olha uma jogada do adversário à frente; o
Minimax fazia isto com mais profundidade.

**P: O computador pode parar a meio de uma captura múltipla?**
Não: as capturas de `gerarJogadas` vão até ao fim. Mas no fácil (e às
vezes no médio) pode não capturar quando podia, e aí pode ser soprado.

## 3.11 Empate, desistir e mensagens

**P: Como funciona o empate?**
Tudo depende de um contador, `jogadasSemCaptura`, com o limite
`LIMITE_SEM_CAPTURAS = 20` (`constantes.js`). No fim de cada jogada
(`terminarJogada`), dos dois jogadores, volta a 0 se houve captura e soma
1 se não houve; 20 jogadas são cerca de 10 de cada um. Um sopro não é
captura: não põe o contador a zero.

**P: Quando é que o computador aceita?**
Quando carregamos em "Propor empate" (`proporEmpate`), só aceita se o
contador for **≥ 20** (`computadorAceitaEmpate`); senão: "O computador
recusou o empate. Continua a jogar." Só se pode propor no início da
nossa vez (com ou sem peça selecionada); na vez dele ou a meio de uma
captura múltipla: "Só podes propor empate no início da tua vez."

**P: Quando é que o computador propõe?**
No início da vez dele (`computadorJoga`), antes de jogar: se o contador
for **≥ 20** e ainda não propôs neste jogo (`computadorPropos`), marca
`empateProposto = true` e depois joga normalmente. Na nossa vez aparece
"O adversário propôs empate…" e o botão passa a **"Aceitar empate"**:
carregar aceita logo; jogar em vez de aceitar é recusar
(`empateProposto` volta a `false` no fim da nossa jogada). Só propõe
**uma vez por jogo**, mas continua a aceitar se formos nós a propor com
o contador ≥ 20. O empate aceite conta nas classificações.

**P: E se o computador propõe e, na mesma jogada, captura?**
O contador volta a 0, mas a proposta fica de pé e podemos aceitá-la.
Justificação: a proposta foi feita quando o jogo estava parado há 20
jogadas; a jogada dele vem a seguir.

**P: Em que jogada é que isso acontece, na prática?**
Testado com o código do jogo (2000 jogos por nível, 3 nov 2026): no
**Fácil** o computador propõe em cerca de 90 % dos jogos, por volta da
jogada 70–80 (a mais cedo foi a 22); no **Médio** só em 1–5 % e no
**Difícil** quase nunca, porque ele captura e sopra e o contador volta a
zero. Para mostrar a proposta ao professor: nível Fácil e evitar
capturar.

**P: Desistir?**
Para os temporizadores, `fimDeJogo`, conta uma derrota, "Desististe,
perdeste."

**P: Que mensagens há?**
Vez de cada um, jogada inválida (e porquê), continuar a capturar,
sopro, empate proposto/recusado/aceite, vitória/derrota, desistência. As
de aviso pulsam a laranja (`mostrarMensagem`); as de "é a tua vez" não
(`mostrarVez`).

## 3.12 Perguntas difíceis ou "e se...?"

**P: E um tabuleiro maior?**
O tamanho e as medidas estão em constantes (`TAMANHO`, `MARGEM`,
`ESPACO`, `RAIO`), por isso a lógica serve. Faltava a posição inicial e o
tamanho da `div` no CSS.

**P: Como ligam ao servidor na 2.ª entrega?**
Lógica e dados estão separados do desenho: a jogada do adversário passa
a vir do servidor em vez da IA, e o login passa a ser o pedido
`register`. O `Board` é o que se troca. Os pedidos serão assíncronos
(`fetch`), por isso a interface continua a responder.

**P: Testaram como?**
*(Dizer o que fizeram de facto.)* Por exemplo: a jogar os casos da
Parte 2 nos três níveis e com os dois a começar, com a consola aberta
para ver erros, e os validadores do W3C.

**P: Dificuldades?**
As capturas múltiplas (recursão), o sopro (que peça fica soprável quando
se para a meio) e acertar as diagonais em CSS.

**P: Como dividiram o trabalho?**
*(Combinar antes entre os três e dizer a verdade.)*

**P: Mostra-me no código onde está X.**

| Coisa | Ficheiro → função |
|---|---|
| Arranque | `comandos.js` → `prepararPagina` (fim do ficheiro) |
| Posição inicial | `tabuleiro.js` → `posicaoInicial` |
| Diagonais | `pecas.js` → `temDiagonais` |
| Linhas do tabuleiro | `interface.js` → `desenharLinhas`; `tabuleiro.css` |
| Desenhar peças | `interface.js` → `desenharTabuleiro`, `criarPosicao` |
| Destaques | `interface.js` → `marcarDestaques` |
| Animação da peça | `interface.js` → `animarPeca`; `jogo.js` → `animarEDepois` |
| Animação da mensagem | `interface.js` → `mostrarMensagem`; `mensagens.css` |
| Cliques e modos | `jogo.js` → `cliqueCasa` |
| Todas as jogadas | `tabuleiro.js` → `gerarJogadas` |
| Capturas múltiplas | `tabuleiro.js` → `procurarCapturas` |
| Sopro | `jogo.js` → `calcularSopraveis`, `soprar`, `computadorSopra` |
| IA | `ia.js`; `jogo.js` → `escolherJogada` |
| Empate | `jogo.js` → `proporEmpate`, `computadorAceitaEmpate` |
| Login | `identificacao.js` → `entrar`, `registar`, `iniciarSessao`, `sair` |
| Classificações | `classificacoes.js` → `registarResultado`, `preencherClassificacoes` |
| Layout | `geral.css` → `#principal`, `.area`, `.painel` |
