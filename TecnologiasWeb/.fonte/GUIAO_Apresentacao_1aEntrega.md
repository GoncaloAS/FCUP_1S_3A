---
title: "Alquerque — Apresentação da 1.ª entrega"
subtitle: "Guião (Gonçalo, Matilde, Hugo) e perguntas e respostas"
---

<!-- Fonte: código do repositório github.com/hugobolotoreis-wq/Tec-web
     (commit 297b5be), lido a 3 nov 2026. Os slides estão em
     Trabalho/Apresentacao_1aEntrega.pptx. -->

## Como usar este documento

- **Parte 1 — Guião:** quem diz o quê, slide a slide, e a demonstração
  passo a passo (cerca de 10 minutos).
- **Parte 2 — Perguntas e respostas:** o que o professor pode perguntar.
  Cada resposta tem primeiro a **frase para dizer** e depois, quando
  é preciso, **onde está no código** para mostrar no ecrã.
- **Antes da Parte 2** há um mini-dicionário (§2.0) com as palavras de
  programação web que aparecem nas respostas. Quem nunca programou para
  a web deve lê-lo primeiro: são 5 minutos e o resto passa a fazer sentido.

Regra de ouro na discussão: **o professor pode perguntar a qualquer um de
nós**. Não é preciso saber escrever o código de cor; é preciso saber
**explicar por palavras o que ele faz** e **em que ficheiro está**.

# Parte 1 — Guião da apresentação

Duração prevista: **8 a 10 minutos** + perguntas. São 8 slides.
Antes de começar: o `index.html` já aberto no navegador (separador ao
lado dos slides), as classificações com alguns jogos lá (fazer 2 ou 3
jogos antes), e o VS Code aberto na pasta do trabalho, para mostrar
código se ele pedir.

| Slide | Tema | Quem | Tempo |
|---|---|---|--:|
| 1 | Título | Matilde | 0:20 |
| 2 | O jogo em 30 segundos | Matilde | 1:00 |
| 3 | A página: as áreas | Matilde | 1:00 |
| 4 | Como o código está organizado | Gonçalo | 1:30 |
| 5 | Como o jogador humano joga (modos) | Gonçalo | 1:30 |
| 6 | A inteligência artificial | Hugo | 1:00 |
| 7 | Demonstração | Hugo (Gonçalo ajuda) | 3:00 |
| 8 | Resumo e 2.ª entrega | Hugo | 0:30 |

## Slide 1 — Título (Matilde)

> "Bom dia, professor. Somos o Gonçalo, a Matilde e o Hugo, e vamos
> apresentar a nossa 1.ª entrega: o Alquerque, jogado no navegador
> contra o computador. Fizemos tudo em HTML, CSS e JavaScript, sem
> nenhuma biblioteca nem *framework*."

## Slide 2 — O jogo em 30 segundos (Matilde)

> "O Alquerque joga-se num tabuleiro de 5 por 5 posições, que são os
> cruzamentos das linhas. Cada jogador tem 12 peças e só o centro começa
> vazio. Nós jogamos com as azuis, em baixo, e o computador com as
> vermelhas.
>
> As peças andam uma casa pelas linhas, para a frente ou para o lado,
> nunca para trás. Só há diagonais em metade das posições. Para capturar
> salta-se por cima de uma peça do adversário, e pode-se continuar a
> saltar com a mesma peça — é a captura múltipla.
>
> Capturar é obrigatório, mas quem não captura é castigado: o adversário
> pode **soprar** essa peça, ou seja, tirá-la do tabuleiro. Perde quem
> fica sem jogadas."

## Slide 3 — A página: as áreas (Matilde)

> "A página é uma aplicação de página única: tudo está no `index.html`.
> À esquerda temos a identificação, onde se entra ou se cria conta, a
> configuração, onde se escolhe quem começa e o nível do computador, e os
> comandos. À direita estão as mensagens e o tabuleiro. As instruções e as
> classificações são painéis que aparecem por cima da página quando se
> carrega no botão.
>
> Nesta entrega o login ainda não verifica nada, porque não há servidor,
> e a opção 'outro jogador' está desativada: fica para a 2.ª entrega. O
> HTML e todos os CSS passam no validador do W3C sem erros."

## Slide 4 — Como o código está organizado (Gonçalo)

> "Separámos os **dados** do **desenho**. O tabuleiro é uma matriz de 5
> por 5 dentro da classe `Board`; cada casa tem uma peça ou está vazia.
> Usámos classes, como o enunciado valoriza: `Position` para uma posição,
> `Piece` para uma peça, `Board` para o tabuleiro e as regras, e `Game`
> para o andamento do jogo.
>
> O tabuleiro que se vê é gerado por JavaScript através da DOM: as
> linhas são 16 quadrados desenhados com CSS, e as 25 posições são
> círculos criados com `createElement`. Sempre que os dados mudam,
> voltamos a desenhar as peças a partir da matriz.
>
> O coração do trabalho é a função `gerarJogadas`: dá todas as jogadas
> válidas de um jogador, incluindo as capturas múltiplas. A mesma função
> serve para validar os cliques do humano, para a IA escolher e para
> saber quando o jogo acaba."

## Slide 5 — Como o jogador humano joga (Gonçalo)

> "O mesmo clique faz coisas diferentes conforme o momento, por isso o
> jogo guarda um **modo**. Em 'espera de jogada', clicar numa peça nossa
> seleciona-a e clicar numa vermelha com contorno tracejado sopra-a. Em
> 'peça selecionada', clicar num destino amarelo faz a jogada. Se for uma
> captura e der para continuar, passamos a 'captura múltipla' e
> continuamos a clicar nos destinos; clicar na própria peça termina a
> jogada. Durante a vez do computador e no fim do jogo os cliques são
> ignorados.
>
> O jogador sabe sempre o que pode fazer: as peças com jogadas têm
> contorno branco, as que podem capturar brilham a amarelo, o cursor muda
> para a mãozinha e há sempre uma mensagem no topo."

## Slide 6 — A inteligência artificial (Hugo)

> "O computador tem três níveis. No **fácil** escolhe uma jogada ao calhas
> e nunca sopra. No **médio**, em cada jogada tira à sorte: metade das
> vezes joga ao calhas e metade das vezes joga a que captura mais peças;
> e sopra metade das vezes. No **difícil** joga sempre a que captura
> mais e, entre as que empatam, escolhe a que deixa o jogador com menos
> capturas na jogada seguinte; e sopra sempre que pode.
>
> O computador também propõe empate quando há 20 jogadas seguidas sem
> capturas, e só aceita o nosso empate nessa situação."

## Slide 7 — Demonstração (Hugo joga, Gonçalo comenta se for preciso)

Fazer por esta ordem; dizer em voz alta o que se está a fazer.

1. **Identificação:** no separador *Registar*, criar o utilizador `hugo`
   (senha qualquer, duas vezes igual). Aparece "Olá, hugo!".
   *"O login ainda não verifica nada; só guarda o nome para as
   classificações."*
2. **Instruções:** abrir e fechar o painel. *"É um painel por cima da
   página."*
3. **Configuração:** quem joga primeiro = Eu; nível = **Difícil**
   (assim, se não capturarmos, ele sopra sempre e dá para mostrar o
   sopro). Carregar em **Iniciar jogo**.
4. **Jogada simples:** clicar numa peça com contorno branco → fica com
   contorno amarelo e os destinos ficam amarelo-claro → clicar num destino.
   *"A peça desliza e a vez passa para o computador."*
5. **Vez do computador:** mostrar o indicador vermelho "a pensar". As
   jogadas dele são feitas passo a passo, com pausa, para se ver.
6. **Captura:** quando uma peça azul brilhar a amarelo, capturar com ela.
   Se der captura múltipla, continuar a clicar nos destinos.
   *"As peças capturadas ficam cinzentas até ao fim da jogada."*
7. **Sopro** (se aparecer a ocasião): ter uma peça a brilhar e jogar
   outra → o computador sopra-a. *"Não capturámos, por isso ele soprou-nos
   a peça."* Se for ao contrário (uma vermelha com contorno tracejado),
   clicar nela para a soprar.
8. **Propor empate:** carregar → *"O computador recusou"* (ainda não há
   20 jogadas sem capturas).
9. **Desistir:** carregar → mensagem "Desististe, perdeste."
10. **Classificações:** abrir → aparece a linha do `hugo` no nível
    Difícil com 1 derrota. *"Fica guardado no navegador, com o
    localStorage."*

Se algo correr mal na demo: não entrar em pânico, carregar em *Iniciar
jogo* outra vez e continuar.

## Slide 8 — Resumo e 2.ª entrega (Hugo)

> "Resumindo: o jogo completo contra o computador, com todas as regras,
> incluindo capturas múltiplas e o sopro, três níveis de IA e todas as
> áreas pedidas. Na 2.ª entrega vamos ligar o jogo ao servidor para
> jogar contra outra pessoa, com login a sério, e fazer o nosso servidor
> em Node.js. Estamos à disposição para perguntas."

# Parte 2 — Perguntas e respostas

## 2.0 Mini-dicionário (ler primeiro)

| Palavra | O que é, em linguagem simples |
|---|---|
| **HTML** | A estrutura da página: que caixas, botões e textos existem. É o `index.html`. |
| **CSS** | O aspeto: cores, tamanhos, posições, animações. São os ficheiros da pasta `css/`. |
| **JavaScript (JS)** | O comportamento: o que acontece quando se clica. São os ficheiros da pasta `js/`. |
| **Elemento** | Uma "caixa" da página, por exemplo `<div>`, `<button>`, `<p>`. |
| **id** | Nome único de um elemento (`id="tabuleiro"`). O JS encontra-o com `document.getElementById("tabuleiro")`. |
| **classe CSS** | Uma etiqueta que se põe num elemento (`class="posicao azul"`) para lhe dar um estilo. Um elemento pode ter várias. |
| **classList** | A forma de o JS pôr e tirar classes CSS: `elem.classList.add("azul")`, `.remove(...)`. É assim que mudamos o aspeto das peças. |
| **DOM** | A "árvore" de todos os elementos da página, que o JS pode ler e alterar. "Gerar pela DOM" = o JS cria os elementos em vez de estarem escritos no HTML. |
| **createElement / appendChild** | Criar um elemento novo (`document.createElement("div")`) e metê-lo dentro de outro (`pai.appendChild(filho)`). |
| **Evento / addEventListener** | "Quando acontecer X, corre esta função." Ex.: `botao.addEventListener("click", iniciarJogo)`. |
| **Função** | Um bloco de código com nome, que se chama quando é preciso. |
| **Classe (JS)** | Um "molde" para criar objetos com dados e funções próprias (`Board`, `Game`...). As funções de uma classe chamam-se **métodos**. |
| **Objeto / `this`** | Um objeto criado a partir de uma classe; dentro dos métodos, `this` é o próprio objeto. |
| **Matriz** | Uma tabela de linhas e colunas. O tabuleiro é uma matriz 5 × 5: `casas[linha][coluna]`. |
| **`null`** | "Não há nada." Uma casa vazia tem `null`. |
| **Lista (array)** | Uma sequência de valores: `[a, b, c]`. `push` acrescenta ao fim, `pop` tira do fim. |
| **setTimeout** | "Corre esta função daqui a N milissegundos." Usamos para as pausas do computador e para esperar pela animação. |
| **transition (CSS)** | Quando uma propriedade muda (por ex. a posição), o navegador faz a mudança aos poucos em vez de saltar. É o que faz a peça deslizar. |
| **@keyframes / animation** | Uma animação definida em CSS por etapas (0%, 40%, 100%). Usamos na caixa das mensagens. |
| **position: absolute** | Pôr um elemento num ponto exato (x, y) dentro da caixa-mãe, com `left` e `top`. |
| **localStorage** | Uma pequena memória do navegador que não se apaga ao fechar a página. Guarda texto. |
| **JSON** | Uma forma de escrever objetos como texto, para os guardar no localStorage. |
| **Recursão** | Uma função que se chama a si própria. Usamos para encontrar as capturas múltiplas. |
| **SPA** | *Single-page application*: tudo numa só página HTML; o JS mostra e esconde partes. |

## 2.1 Estrutura geral

**P: Como está organizado o projeto?**
Um `index.html`, 5 ficheiros CSS (um por área: geral, identificação,
mensagens, tabuleiro, classificações) e 9 ficheiros JS, cada um com uma
responsabilidade:

| Ficheiro | O que tem |
|---|---|
| `constantes.js` | Números fixos: tamanho 5, cores, tempos, medidas em píxeis, direções |
| `pecas.js` | Classes `Position` e `Piece` e funções pequenas (cor adversária, sentido da frente) |
| `tabuleiro.js` | Classe `Board`: a matriz e as **regras** (movimentos, capturas, gerar jogadas) |
| `jogo.js` | Classe `Game`: o andamento (de quem é a vez, os modos, cliques, sopro, empate, fim) |
| `ia.js` | As três estratégias do computador |
| `interface.js` | Desenhar o tabuleiro, animar e mostrar mensagens |
| `identificacao.js` | Entrar, registar, sair |
| `classificacoes.js` | Guardar e mostrar resultados (localStorage) |
| `comandos.js` | Liga os botões às funções e arranca tudo |

**P: É uma aplicação de página única? Como mudam as "páginas"?**
Sim: só há o `index.html`. Os painéis de instruções e classificações já
estão no HTML mas escondidos com a classe `escondido` (que no CSS é
`display: none`). Abrir = tirar a classe; fechar = pô-la outra vez
(`abrirPainel` e `fecharPainel` em `comandos.js`). O mesmo para os
formulários de entrar/registar.

**P: Usaram alguma biblioteca ou framework?**
Não. É tudo JavaScript, HTML e CSS "puros", como o enunciado pede.

**P: Porque é que os `<script>` estão no fim do `<body>`?**
Para que, quando o JS corre, os elementos da página já existam. Se o
script corresse antes, o `getElementById` não encontrava os botões.

**P: A ordem dos scripts importa?**
Sim. Primeiro as constantes, depois as classes (`Position`, `Board`,
`Game`), e por último o `comandos.js`, que cria o jogo
(`const jogo = new Game()`) e chama `prepararPagina()`. Uma classe tem de
estar definida antes de se usar.

**P: O HTML e o CSS passam no validador?**
Sim, testámos: o HTML no validador do W3C e os 5 ficheiros CSS no
validador de CSS, sem erros.

**P: Porque é que os botões têm `type="button"`?**
Por omissão um botão dentro de um formulário "submete" e recarrega a
página. Com `type="button"` é só um botão que corre o nosso JS.

## 2.2 Os dados: como representam o tabuleiro

**P: Como guardam o estado do tabuleiro?**
Na classe `Board` há `this.casas`, uma matriz 5 × 5. Cada casa é `null`
(vazia) ou um objeto `Piece` com a cor (`"azul"` ou `"vermelha"`). Tudo o
resto — desenhar, validar cliques, a IA — trabalha sobre esta matriz.

**P: Como fazem a posição inicial?**
`posicaoInicial()` percorre as 25 casas: as linhas 0 e 1 são vermelhas,
as 3 e 4 azuis, e na linha do meio as colunas 0–1 são vermelhas, as 3–4
azuis e a coluna 2 (o centro) fica vazia.

**P: Como sabem se uma posição tem diagonais?**
Uma posição tem diagonais quando `linha % 2 === coluna % 2`, ou seja,
linha e coluna são ambas pares ou ambas ímpares (os cantos, o centro...).
É o método `temDiagonais()` da classe `Position`. Daí, `direcoes()`
devolve as 8 direções ou só as 4 retas.

**P: O que é uma "direção"?**
Um par `[variação da linha, variação da coluna]`. Por exemplo `[-1, 0]`
é "para cima", `[1, 1]` é "diagonal para baixo e para a direita". O
método `andar(direcao, passos)` dá a posição a 1 ou 2 casas nessa
direção.

**P: Porque usaram classes?**
O enunciado valoriza a orientação a objetos e assim cada coisa fica com
os seus dados e as suas funções juntos: a `Position` sabe se está dentro
do tabuleiro e para onde pode andar, o `Board` sabe as regras, o `Game`
sabe de quem é a vez. Na 2.ª entrega os dados do `Board` são os que vão
ser trocados com o servidor.

## 2.3 Gerar o tabuleiro no ecrã (desenho e CSS)

**P: Como geram o tabuleiro?**
Em duas camadas, dentro da `div` `#tabuleiro` (400 × 400 px, verde):

1. **As linhas** (`desenharLinhas`, em `interface.js`): uma vez, no
   início, o JS cria **16 quadrados** (4 × 4), cada um com uma borda de
   3 px. As bordas dos quadrados formam as linhas horizontais e
   verticais. A diagonal de cada quadrado é desenhada com um
   `linear-gradient` que é transparente em todo o lado menos numa faixa
   fina no meio. Conforme o canto do quadrado tem diagonais ou não, a
   diagonal "desce" ou "sobe" (classes `diagDesce` e `diagSobe`). É isto
   que dá o padrão em losango.
2. **As peças** (`desenharTabuleiro`): o JS apaga todos os círculos e
   cria **25** de novo, um por posição, com `createElement("div")`, a
   partir da matriz. Cada círculo recebe classes: `vazia`, `azul` ou
   `vermelha`, e os destaques (`temJogada`, `podeCapturar`, `destino`...).

**P: Como sabem onde pôr cada peça no ecrã?**
Com `position: absolute` e a função `centro(i) = 40 + i × 80`: a primeira
linha está a 40 px da borda e as posições estão a 80 px umas das outras.
O círculo tem raio 25, por isso `left = centro(coluna) − 25` e
`top = centro(linha) − 25`. Mudar `elem.style.left` e `elem.style.top` é
usar o CSS a partir do JS, como o enunciado pede.

**P: Porque é que os quadrados têm 83 px e não 80?**
Porque a borda tem 3 px: 80 + 3. Os quadrados vizinhos sobrepõem a
borda uns dos outros, por isso a linha não fica a dobrar. Também os
recuamos 1,5 px para a linha ficar centrada no ponto certo.

**P: Porque é que redesenham as 25 peças sempre em vez de mexer só nas
que mudaram?**
É mais simples e não há erros de "ecrã diferente dos dados": o ecrã é
sempre uma cópia fiel da matriz. Com 25 elementos é instantâneo.

**P: Como fazem as peças parecerem 3D?**
Com `radial-gradient` no CSS: um ponto mais claro em cima à esquerda e
mais escuro na borda, mais uma `box-shadow` por baixo.

**P: Porque não usaram canvas ou SVG?**
Nesta fase o enunciado pede o tabuleiro feito com elementos HTML, a DOM
e o CSS. O canvas aparece como melhoria na 2.ª entrega.

**P: Como é que o clique sabe em que casa foi?**
Ao criar cada círculo, `criarPosicao(linha, coluna)` põe-lhe um
`addEventListener("click", ...)` que chama `jogo.cliqueCasa(linha,
coluna)` com aqueles valores. Cada círculo "lembra-se" da sua linha e
coluna.

**P: E os destaques (contorno branco, brilho amarelo...)?**
`marcarDestaques` decide, conforme o modo, que classes pôr:

| Classe | Aspeto | Quando |
|---|---|---|
| `temJogada` | contorno branco | peça tua que se pode mexer |
| `podeCapturar` | brilho amarelo | peça tua que pode capturar |
| `selecionada` | contorno amarelo grosso | a peça que escolheste |
| `destino` | amarelo-claro tracejado | para onde podes ir |
| `sopravel` | contorno amarelo tracejado | peça vermelha que podes soprar |
| `capturada` | cinzenta, transparente | já saltada, sai no fim da jogada |
| `clicavel` | cursor de mãozinha + cresce ao passar o rato | tudo o que se pode clicar |

## 2.4 As animações

**P: Como fizeram a peça deslizar?**
No CSS, `.posicao` tem `transition: left 0.3s, top 0.3s`. Quando uma peça
se mexe, `animarPeca` muda o `left` e o `top` do círculo para o destino
e o navegador faz o movimento aos poucos durante 0,3 s. Também lhe põe a
classe `aMover` (`z-index: 10`) para passar **por cima** das outras.
O JS espera esses 300 ms com `setTimeout` (`animarEDepois` em `jogo.js`)
e só então atualiza a matriz e redesenha.

**P: E se o utilizador clicar durante a animação?**
Enquanto anima, `this.aAnimar` está a `true` e `cliqueCasa` ignora os
cliques. Assim não se pode fazer duas jogadas ao mesmo tempo.

**P: Como fizeram a caixa das mensagens "pulsar"?**
Em `mensagens.css` há uma animação `@keyframes pulsar` (cresce 3% e
faz uma onda laranja à volta). Está ligada à classe `destaque`.
`mostrarMensagem` tira a classe, faz `void caixa.offsetWidth` e volta a
pô-la.

**P: Para que serve esse `void caixa.offsetWidth`?**
Se tirarmos e pusermos a classe logo a seguir, o navegador não nota a
diferença e a animação não recomeça. Ler o `offsetWidth` obriga o
navegador a recalcular a página entre as duas coisas, por isso a
animação volta a correr do início sempre que há uma mensagem nova.

**P: E as outras animações?**
Ao passar o rato por cima de algo clicável a peça cresce 12%
(`transform: scale(1.12)` com transição de 0,15 s), e os botões mudam de
cor suavemente (`transition: background-color 0.2s`).

**P: Porque é que o computador joga devagar?**
Entre cada passo do computador há uma pausa de 1,1 s (`ESPERA`), feita
com `setTimeout`. Sem isso, as jogadas dele (sobretudo as capturas
múltiplas) apareciam todas de uma vez e não se percebia o que tinha
acontecido.

## 2.5 Os modos e o jogo

**P: Que modos tem o jogo e o que faz cada um?**
O `Game` tem `this.modo`, e `cliqueCasa` faz um `switch` sobre ele:

| Modo | Quando | O que faz um clique |
|---|---|---|
| `esperaJogada` | início da tua vez | peça tua com jogadas → seleciona; vermelha soprável → sopra; outra coisa → "Jogada inválida" |
| `pecaSelecionada` | escolheste uma peça | destino válido → joga; a mesma peça → cancela; outra peça tua → troca a seleção |
| `capturaMultipla` | capturaste e ainda dá para saltar | destino de captura → salta outra vez; a tua peça → para (arriscas o sopro) |
| `vezComputador` | o computador está a jogar | nada |
| `fimDeJogo` | antes de começar ou no fim | nada |

**P: Como sabe o jogador em que modo está?**
Pelos destaques das peças, pelo cursor (mãozinha só no que é clicável),
pela etiqueta "Vez: tu (azuis)" / "Vez: computador" por cima do
tabuleiro, e pela mensagem no topo, que muda em cada modo.

**P: Como corre uma vez de jogo, do princípio ao fim?**
1. `iniciarVez()` calcula todas as jogadas do jogador (`gerarJogadas`) e
   que peças podiam capturar (`pecasQuePodemCapturar`).
2. Se for o humano e não tiver jogadas (nem nada para soprar), perde.
3. O humano clica; o computador escolhe com a IA.
4. `terminarJogada()` vê o que fica soprável para o adversário, tira as
   peças capturadas, conta jogadas sem capturas, passa a vez e volta ao
   passo 1.

**P: O que é o `self = this` que aparece várias vezes?**
Dentro de uma `function` passada ao `setTimeout`, o `this` deixa de ser
o jogo. Guardamos o jogo numa variável `self` antes, para o usar lá
dentro. (Uma *arrow function* `() => {}` também resolvia.)

## 2.6 As regras: movimentos, capturas e sopro

**P: Como geram todas as jogadas válidas?**
`gerarJogadas(cor)` em `tabuleiro.js`: para cada peça dessa cor junta os
movimentos simples (`movimentosSimples`) e as capturas
(`procurarCapturas`). Cada jogada é um objeto com a `origem`, o
`caminho` (lista de posições por onde passa), as peças `capturadas` e o
`tipo` ("movimento" ou "captura").

**P: Como garantem que a peça não recua e que na última fila só anda na
horizontal?**
Em `movimentosSimples`: cada cor tem um "sentido da frente"
(`sentidoFrente`: −1 para as azuis, que sobem; +1 para as vermelhas).
Uma direção com a variação de linha contrária é saltada. Se a peça
estiver na última fila (`ultimaFila`), salta-se qualquer direção que não
seja horizontal. O destino tem ainda de estar dentro do tabuleiro e vazio.

**P: Como verificam uma captura?**
`saltosPossiveis`: em cada direção olha para a casa do meio (a 1 passo) e
a de destino (a 2 passos). Há salto se o destino está dentro e vazio, o
meio tem uma peça **do adversário**, essa peça ainda não foi saltada e o
destino ainda não está no caminho. As capturas não têm a restrição de
não recuar.

**P: Como encontram as capturas múltiplas?**
Com **recursão** (`procurarCapturas`): a partir da posição atual,
experimenta cada salto possível, acrescenta-o ao caminho, e chama-se a si
própria a partir do novo sítio. Quando já não há saltos, guarda a
sequência como uma jogada. Depois desfaz o último salto (`pop`) e
experimenta o seguinte. Assim encontra todos os caminhos, sem passar duas
vezes pela mesma posição nem saltar duas vezes a mesma peça.

**P: Na captura múltipla do humano, as peças saltadas saem logo?**
Não: ficam marcadas com `capturada = true` (aparecem cinzentas) e só saem
em `terminarJogada`. Assim não se pode saltá-las outra vez, e o
tabuleiro continua coerente durante a sequência.

**P: Capturar é obrigatório. O vosso jogo obriga?**
Não obriga, de propósito: é a regra do sopro. Se o jogador podia capturar
e não o fez, o adversário pode soprar-lhe a peça. O jogo avisa ("Tens
capturas... se não capturares, podes ser soprado") mas deixa jogar.

**P: Como funciona o sopro no código?**
No fim de cada jogada, `calcularSopraveis()` vê o que o jogador fez mal:

- se capturou mas **parou a meio** (ainda havia saltos), a peça que parou
  fica soprável;
- se **não capturou** e havia peças que podiam, essas peças ficam
  sopráveis (se a peça que devia capturar se mexeu, conta a nova
  posição dela).

Na vez seguinte, o adversário pode soprar **uma**: o humano clica numa
vermelha com contorno tracejado (`soprar`); o computador decide em
`computadorSopra`, conforme o nível. Depois de soprar, a vez continua
normalmente.

**P: Quando acaba o jogo?**
- Perde quem, na sua vez, **não tem jogadas** (sem peças também conta,
  porque então não há jogadas). Verifica-se no início de cada vez.
- **Desistir:** quem desiste perde.
- **Empate:** só por acordo (ver §2.8).

**P: O que é a contagem por baixo do tabuleiro?**
`contarPecas` de cada cor, atualizada sempre que se redesenha.

## 2.7 A inteligência artificial

**P: Como funciona a IA?**
Primeiro gera **todas** as jogadas válidas do computador (a mesma
`gerarJogadas` que valida o humano) e depois escolhe uma, conforme o
nível (`escolherJogada` em `jogo.js`, estratégias em `ia.js`):

| Nível | Que jogada escolhe | Sopra? |
|---|---|---|
| Fácil | ao calhas (`jogadaAleatoria`) | nunca |
| Médio | 50 % ao calhas, 50 % gulosa | 50 % das vezes |
| Difícil | gulosa + olha uma jogada à frente | sempre que pode |

**P: O que é a jogada "gulosa"?**
A que captura **mais peças** agora. Se houver várias empatadas, escolhe
uma delas ao calhas (`jogadaGulosa`).

**P: E o difícil, o que faz a mais?**
Entre as jogadas que capturam o máximo, experimenta cada uma numa
**cópia** do tabuleiro (`copiar()` + `aplicarJogada`) e vê qual é a maior
captura que o humano poderia fazer a seguir (`maiorCaptura`). Escolhe a
que deixa o humano com menos. É uma versão simples de "pensar uma jogada
à frente".

**P: Porque é que fazem uma cópia do tabuleiro?**
Para experimentar jogadas sem estragar o tabuleiro verdadeiro.

**P: Usaram Minimax?**
Não, era opcional. O difícil já olha uma jogada do adversário à frente;
um Minimax a sério seria fazer isto com mais profundidade.

**P: O computador também pode parar a meio de uma captura múltipla?**
Não. As capturas que `gerarJogadas` devolve vão sempre até ao fim. Mas
no fácil (e às vezes no médio) pode escolher um movimento simples quando
podia capturar — e nesse caso o humano pode soprá-lo.

**P: As jogadas do computador são calculadas onde?**
No cliente, no navegador, como pede a 1.ª entrega.

## 2.8 Empate, desistir e mensagens

**P: Como funciona o empate?**
- **Proposto por nós:** o computador só aceita se já houve **20 jogadas
  seguidas sem capturas** (`computadorAceitaEmpate`). Contam as jogadas
  dos dois, ou seja, cerca de 10 de cada.
- **Proposto pelo computador:** quando chega às 20 jogadas sem capturas,
  propõe (uma só vez). Aparece a mensagem e o botão muda para "Aceitar
  empate". Se jogarmos em vez de aceitar, é uma recusa.
- Só se pode propor no início da nossa vez.

**P: O que acontece ao desistir?**
Para os temporizadores, o jogo passa a `fimDeJogo`, conta uma derrota nas
classificações e aparece "Desististe, perdeste."

**P: Que mensagens mostram?**
É a tua vez; vez do computador; jogada inválida (e porquê); tens de
continuar a capturar; o computador soprou-te; empate proposto, recusado
ou aceite; ganhaste / o computador ganhou; desististe. As mensagens de
aviso pulsam a laranja para dar nas vistas; as de "é a tua vez" não.

## 2.9 Identificação e classificações

**P: O login funciona?**
Nesta entrega não autentica, como o enunciado permite: verifica que os
campos estão preenchidos e, ao registar, que as duas senhas são iguais.
Depois esconde o formulário, mostra "Olá, nome!" e o botão Sair, e guarda
o nome para as classificações. A senha não é guardada em lado nenhum.
A autenticação a sério vem com o servidor, na 2.ª entrega.

**P: Como mudam entre "Entrar" e "Registar"?**
São dois formulários; `mostrarSeparador` mostra um e esconde o outro com
a classe `escondido`, e marca o separador ativo.

**P: Onde guardam as classificações?**
No **localStorage** do navegador, na chave `alquerqueClassificacoes`.
Como o localStorage só guarda texto, convertemos o objeto em JSON
(`JSON.stringify` para guardar, `JSON.parse` para ler). O formato é
`{ nome: { nivel: { vitorias, derrotas, empates } } }`. Ficam guardadas
mesmo fechando a página, mas só naquele navegador.

**P: Como é feita a tabela?**
`preencherClassificacoes` apaga as linhas antigas e cria uma linha
(`<tr>`) por jogador e nível, com `createElement` e `textContent`. Se não
houver resultados, mostra "Ainda não há resultados".

**P: Porque `textContent` e não `innerHTML`?**
Com `textContent` o nome do utilizador é sempre tratado como texto. Se
alguém se registar com um nome que tenha código HTML, não é executado.

**P: Quem não faz login aparece como?**
"Anónimo".

## 2.10 Perguntas difíceis ou "e se...?"

**P: E se quisessem um tabuleiro maior?**
O tamanho está numa constante (`TAMANHO = 5`) e as medidas em píxeis
também (`MARGEM`, `ESPACO`, `RAIO`), por isso a lógica já funciona com
outro tamanho. Teríamos de ajustar a posição inicial e o tamanho da
`div` do tabuleiro no CSS. No Alquerque o tabuleiro é sempre 5 × 5.

**P: Como vão ligar isto ao servidor na 2.ª entrega?**
A lógica e os dados estão separados do desenho: em vez de a jogada vir da
IA, virá do servidor; e o login passa a ser verificado pelo servidor.
O `Board` é o que se troca.

**P: Encontraram dificuldades?**
As capturas múltiplas (resolvidas com a recursão) e o sopro (perceber
exatamente que peça fica soprável quando se pára a meio). Também
acertar as linhas diagonais com CSS.

**P: Como dividiram o trabalho?**
*(Combinar antes a resposta entre os três e dizer a verdade.)*

**P: Mostra-me no código onde está X.**
Usar a tabela de ficheiros em §2.1. No VS Code, `Cmd+Shift+F` procura
em todos os ficheiros: escrever o nome da função (por exemplo
`procurarCapturas`, `animarPeca`, `calcularSopraveis`).

**Tabela rápida "onde está"**

| Coisa | Ficheiro → função |
|---|---|
| Posição inicial | `tabuleiro.js` → `posicaoInicial` |
| Diagonais | `pecas.js` → `temDiagonais` |
| Linhas do tabuleiro | `interface.js` → `desenharLinhas` + `tabuleiro.css` |
| Desenhar as peças | `interface.js` → `desenharTabuleiro`, `criarPosicao` |
| Destaques | `interface.js` → `marcarDestaques` |
| Animação da peça | `interface.js` → `animarPeca`; `jogo.js` → `animarEDepois` |
| Animação da mensagem | `interface.js` → `mostrarMensagem`; `mensagens.css` |
| Cliques e modos | `jogo.js` → `cliqueCasa` |
| Todas as jogadas | `tabuleiro.js` → `gerarJogadas` |
| Capturas múltiplas | `tabuleiro.js` → `procurarCapturas` |
| Sopro | `jogo.js` → `calcularSopraveis`, `soprar`, `computadorSopra` |
| IA | `ia.js`; `jogo.js` → `escolherJogada` |
| Empate | `jogo.js` → `proporEmpate`, `computadorAceitaEmpate` |
| Classificações | `classificacoes.js` |
| Login | `identificacao.js` |
| Botões | `comandos.js` → `prepararPagina` |
