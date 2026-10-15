# Trabalho Prático — Alquerque

<!-- Fonte: https://www.dcc.fc.up.pt/~zp/SeWenta/TW-26-27/ → Práticas → Trabalho
     (regras/, entrega1/, envio, faq, grupos, apresenta) + Geral → Avaliação.
     Lido a 8 out 2026. Este ano o jogo é o Alquerque; o Tâb era o de 2025/26. -->

```{=latex}
\newcommand{\alq}[1]{\begin{tikzpicture}[scale=0.5,baseline=(current bounding box.center)]
  \foreach \i in {0,...,4}{\draw[gray!60] (0,\i)--(4,\i); \draw[gray!60] (\i,0)--(\i,4);}
  \draw[gray!60] (0,0)--(4,4) (0,4)--(4,0) (0,2)--(2,4)--(4,2)--(2,0)--cycle;
  #1\end{tikzpicture}}
\newcommand{\pB}[2]{\fill[blue!65!black] ({#2},{4-#1}) circle (0.3);}
\newcommand{\pR}[2]{\fill[red!75!black] ({#2},{4-#1}) circle (0.3);}
\newcommand{\pS}[2]{\draw[orange,line width=1.4pt] ({#2},{4-#1}) circle (0.36);}
\newcommand{\pA}[4]{\draw[->,>=stealth,orange!90!black,line width=1pt,shorten >=5pt,shorten <=5pt] ({#2},{4-#1})--({#4},{4-#3});}
\newcommand{\coords}{\foreach \i in {0,...,4}{\node[font=\tiny,gray] at (-0.75,{4-\i}) {\i}; \node[font=\tiny,gray] at (\i,4.75) {\i};}}
```

## Em 30 segundos

- **O quê:** uma versão web do jogo de tabuleiro **Alquerque**, feita à mão
  (HTML + CSS + JavaScript, **sem frameworks**), em grupos de até 3.
- **Duas entregas** (o site fala em três "fases"; a 2ª e a 3ª são entregues
  juntas):

| Entrega | O que se faz | Prazo | Vale |
|---|---|---|--:|
| **1ª** | Cliente: página única, jogo **contra o computador** (IA) | **sex 30 out 2026** (tolerância seg 2 nov, 10:00) | 3 val. |
| **2ª** (fases 2+3) | Jogo entre 2 pessoas via servidor + **servidor próprio em Node.js** | **sex 11 dez 2026** (tolerância seg 14 dez, 10:00) | 5 val. |

- **Frequência:** precisas de pelo menos 1 entrega com ≥ 25% da cotação.
- Depois de cada entrega há uma **apresentação/discussão** (ver §5).
- **Agora** só interessa a 1ª entrega: o enunciado da 2ª ainda **não foi
  publicado** para o Alquerque (ver §4).

## 1. Regras do Alquerque

*(Há variantes do jogo — no trabalho contam só estas.)*

### Tabuleiro, peças e posição inicial

- Grelha de **5 × 5 = 25 posições** (as interseções das linhas). Os
  caminhos válidos são as linhas horizontais, verticais e **diagonais**
  desenhadas.
- Nem todas as posições têm diagonais: só as posições com
  `linha % 2 == coluna % 2` (os cantos, o centro, ...). Nas outras só se
  anda na horizontal e na vertical.
- Cada jogador tem **12 peças** da sua cor (ex.: azul e vermelho). As duas
  filas do seu lado são suas; na fila do meio fica com as **2 posições à
  sua direita**; o **centro começa vazio** (é a única posição vazia).

Convenção usada neste documento (é a mesma do código do site,
`Position(row, column)`): linha 0 em cima, coluna 0 à esquerda; as **azuis**
começam em baixo e avançam **para cima**, as **vermelhas** o contrário.

```{=latex}
\begin{center}
\alq{\coords
 \foreach \c in {0,...,4}{\pR{0}{\c}\pR{1}{\c}\pB{3}{\c}\pB{4}{\c}}
 \pR{2}{0}\pR{2}{1}\pB{2}{3}\pB{2}{4}}
\qquad
\begin{minipage}[c]{0.5\linewidth}\small
Posição inicial.\\[2pt]
As azuis ficam com as colunas 3–4 da fila do meio (à direita de quem
joga de baixo); as vermelhas, que veem o tabuleiro rodado, ficam com as
colunas 0–1, que também são a direita delas. O tabuleiro é simétrico.
\end{minipage}
\end{center}
```

### Movimento simples (sem captura)

- Os jogadores alternam; em cada vez fazem **um movimento ou uma captura**.
- Um movimento leva uma peça para uma posição **adjacente e vazia**, desde
  que haja uma linha a ligá-las e a peça **não recue** em direção à sua
  fila inicial (para o lado pode).
- Na **última fila** (a do adversário) a peça só se pode mover na
  **horizontal**.

```{=latex}
\begin{center}
\begin{tabular}{ccc}
\alq{\pB{4}{1}\pS{4}{0}\pS{4}{2}\pS{3}{1}} &
\alq{\pB{2}{2}\pS{2}{1}\pS{1}{1}\pS{1}{2}\pS{1}{3}\pS{2}{3}} &
\alq{\pB{0}{3}\pS{0}{2}\pS{0}{4}} \\[2pt]
\footnotesize sem diagonais: lado ou frente &
\footnotesize centro: 5 destinos (não recua) &
\footnotesize última fila: só horizontal
\end{tabular}
\end{center}
```

### Capturar

- Captura-se **saltando por cima** de uma peça adversária adjacente para a
  posição vazia logo a seguir, na mesma linha. A peça saltada sai do
  tabuleiro.
- Ao contrário do movimento, **a captura pode ser para trás** (e uma peça
  na última fila pode capturar para o lado ou para trás).
- **Se houver captura possível, é obrigatório capturar** — quem não
  capturar arrisca o *sopro* (abaixo).

```{=latex}
\begin{center}
\begin{tabular}{ccc}
\alq{\pB{4}{1}\pR{3}{1}\pS{2}{1}\pA{4}{1}{2}{1}} &
\alq{\pB{3}{1}\pR{2}{2}\pS{1}{3}\pA{3}{1}{1}{3}} &
\alq{\pB{0}{3}\pR{1}{3}\pS{2}{3}\pA{0}{3}{2}{3}} \\[2pt]
\footnotesize em frente & \footnotesize na diagonal & \footnotesize para trás
\end{tabular}
\end{center}
```

### Capturas múltiplas

- Depois de capturar, a mesma peça pode continuar a capturar **no mesmo
  turno**, mudando de direção em cada salto, mas **sem passar duas vezes
  pela mesma posição** nem saltar duas vezes a mesma peça.
- Se houver vários percursos, escolhe-se **qualquer um** (não tem de ser o
  que captura mais). Mas no percurso escolhido é obrigatório continuar a
  capturar enquanto der.

```{=latex}
\begin{center}
\begin{tabular}{ccc}
\alq{\pB{4}{1}\pR{3}{1}\pR{1}{1}\pR{4}{2}\pR{1}{3}\pR{3}{3}\pS{2}{1}\pS{0}{1}\pA{4}{1}{2}{1}\pA{2}{1}{0}{1}} &
\alq{\pB{2}{0}\pR{1}{0}\pR{1}{1}\pS{0}{0}\pS{2}{2}\pA{2}{0}{0}{0}\pA{0}{0}{2}{2}} &
\alq{\pB{2}{0}\pR{1}{1}\pR{1}{3}\pR{3}{1}\pR{3}{3}\pS{0}{2}\pS{2}{4}\pS{4}{2}\pA{2}{0}{0}{2}\pA{0}{2}{2}{4}\pA{2}{4}{4}{2}} \\[2pt]
\footnotesize 2 capturas & \footnotesize a 2.ª é para trás &
\footnotesize 3 capturas; a 4.ª voltaria a (2,0)
\end{tabular}
\end{center}
```

### Regra do sopro (penalização)

- Se o adversário **podia ter capturado e não o fez** — moveu essa ou
  outra peça, ou fez só uma captura simples quando podia fazer uma
  múltipla — tu **podes** "soprar" (retirar definitivamente) **uma** peça
  dele: a que devia ter capturado.
- O sopro é opcional e faz-se **no início da tua jogada**, antes de mover
  ou capturar. Mesmo que várias peças pudessem ter capturado, só se sopra
  **uma**.

### Fim do jogo

- **Perde** quem, na sua vez, **não tem peças** ou **não tem nenhuma
  jogada válida** (nem movimento nem captura).
- **Empate** por **acordo mútuo**, por exemplo quando já não pode haver
  capturas (as peças já se cruzaram e não podem recuar) ou quando já não há
  capturas há muitas jogadas. Daí o comando "propor/aceitar empate".

## 2. 1ª entrega — o cliente (só contra o computador)

### Requisitos técnicos

- **Aplicação de página única** (*single-page application*): tudo numa só
  página `index.html`, sem carregar outras páginas HTML.
- CSS em **um ou mais ficheiros `.css`** próprios; JavaScript num ficheiro
  `.js` próprio.
- HTML e CSS **têm de passar no validador** do W3C; erros de CSS são
  penalizados. Se o validador rejeitar uma *feature* de CSS, não a uses.
- **Sem frameworks** de JS nem de CSS.

### As áreas da página

Não têm de estar todas visíveis ao mesmo tempo; algumas podem ser painéis
que se sobrepõem temporariamente aos outros.

| Área | O que tem de fazer |
|---|---|
| **Logotipo** | Nome do jogo em destaque ("Alquerque" ou um nome vosso), em texto formatado ou imagem. |
| **Configuração** | Escolher: contra o computador ou contra outro jogador (na 1ª entrega **só se implementa contra o computador**); quem joga primeiro; nível da IA. |
| **Comandos** | Ver instruções; iniciar jogo com a configuração atual; **propor/aceitar empate**; **desistir** (vitória para o adversário); ver classificações. |
| **Identificação** | Login (identificador + senha) e, depois de autenticado, mostrar o nome e permitir sair. Na 1ª entrega **não autentica nada**, mas a área tem de existir e estar formatada. |
| **Tabuleiro** | A área principal (ver abaixo). |
| **Instruções** | As regras do jogo (§1) e como jogar nesta aplicação. Pode ser um painel sobreposto, com um comando para abrir e outro para fechar. |
| **Classificações** | Tabela com os melhores resultados; na 1ª entrega, só dos jogos contra a IA. O conteúdo é livre desde que faça sentido (ex.: vitórias e derrotas por nível). Também pode ser um painel sobreposto. |
| **Mensagens** | É a tua vez; jogada inválida; fim do jogo e quem ganhou; o adversário propôs empate; desististe e perdeste. |

### Tabuleiro

1. **Fase 1:** escrever o tabuleiro à mão em HTML (contentores para as
   linhas e as peças), com o posicionamento e o aspeto em CSS.
2. **Fase 2:** gerar o tabuleiro **a partir de JavaScript**, através da DOM e
   da sintaxe JS do CSS (`elem.style...`, `classList`).
3. Começa pela **estrutura de dados** que representa o tabuleiro (ex.: uma
   matriz 5 × 5 com `'Blue'`, `'Red'` ou `null`, como no código do site). Os
   métodos que desenham o tabuleiro e tratam os cliques trabalham sobre
   esses dados; na 2ª entrega serão estes os dados trocados com o servidor.
4. É **valorizada uma abordagem orientada a objetos** (ex.: classes
   `Board`, `Position`, `Game`).

**Modos de interação.** O mesmo clique faz coisas diferentes consoante o
momento, por isso é preciso guardar o estado da interação em variáveis:

| Clique | Significado |
|---|---|
| 1.º clique numa peça **do adversário** | essa peça é **soprada** (se o sopro for possível) |
| 1.º clique numa peça **tua** | escolhes a peça a jogar |
| clique seguinte numa posição **adjacente** válida | a peça move-se logo |
| clique seguinte numa posição com uma peça adversária **pelo meio** | é uma captura; como pode ser múltipla, continuas a clicar nos destinos e **voltas a clicar** para terminar a jogada |

O utilizador tem de saber sempre em que modo está, através do cursor e/ou
de mensagens.

### IA (obrigatória)

As jogadas do computador são calculadas **no cliente**. Podes usar uma
destas abordagens ou combiná-las:

- **aleatória:** gerar todas as jogadas válidas e escolher uma ao calhas;
- **gulosa:** preferir as jogadas que capturam;
- **níveis de dificuldade:** em cada jogada sortear qual das duas usar, com
  mais probabilidade de usar a gulosa nos níveis mais altos;
- **opcional:** [Minimax](https://pt.wikipedia.org/wiki/Minimax), com o
  nível a determinar a profundidade da procura.

Repara que, para qualquer uma delas, precisas de uma função que **gera
todas as jogadas válidas** de um jogador, incluindo as capturas múltiplas,
a obrigação de capturar e o sopro. Essa função é também a que valida as
jogadas do humano e deteta o fim do jogo, por isso é o núcleo do trabalho.

### Plano semanal sugerido pelo professor (folhas das práticas)

1. **Estrutura da interface:** ficheiros HTML + CSS + JS; definir em HTML e
   posicionar em CSS as áreas fixas (autenticação, jogo) e as temporárias
   (regras, pontuação); pôr conteúdo de exemplo (peças, tabela, texto das
   regras e os formulários de autenticação, configuração e comandos);
   formatar com CSS.
2. **Peças e tabuleiro:** primeiro em HTML e CSS estáticos, depois gerados
   pela DOM, e por fim a interação em JavaScript.
3. **Interação e jogo:** controlo do jogo, jogador humano, IA e níveis de
   dificuldade.

As aulas práticas **não chegam** para acabar cada folha, por isso é preciso
trabalhar também fora delas.

### O que no site ainda é do jogo do ano passado (ignorar)

O enunciado foi adaptado do Tâb e ficaram restos que não se aplicam ao
Alquerque:

- a página **"Dado de paus"** está listada nas áreas da 1ª entrega, mas o
  Alquerque **não tem dado**, por isso essa área não deve ser precisa;
- a página do Tabuleiro fala em "pilhas" e em "remover a peça e as que
  estão acima", o que também não é deste jogo;
- a FAQ diz que deve haver um **seletor de tamanhos de tabuleiro**, mas o
  tabuleiro do Alquerque é fixo em 5 × 5 (a opção de tamanho está
  comentada na página da Configuração).

Na dúvida, confirma no Slack ou com o professor. Se a área do dado for
mesmo pedida, isso é dito lá.

## 3. Como submeter

- Submete-se **online** um **ZIP**, por qualquer elemento do grupo. Podes
  submeter várias vezes e só conta a última.
- O ZIP tem `index.html` **na raiz** (sem pasta por cima) e um ou mais
  `.css` e `.js`:

```bash
cd $PASTA_TRABALHO
zip trabalho.zip index.html *.{css,js}
```

- Submete-se em <https://mooshak.dcc.fc.up.pt/~tw/cgi-bin/execute?login>,
  com as credenciais LDAP do LabCC. Se o ZIP estiver bem, aparece
  **Accepted**; se aparecer **Compile Time Error**, clica na mensagem para
  ver a causa.

## 4. 2ª entrega — o que já se sabe

O enunciado do Alquerque para esta entrega **ainda não está publicado**:
no site os itens "Segunda fase" e "Terceira fase" não têm link. As páginas
antigas ainda existem no servidor, mas descrevem o **protocolo do Tâb**
(com `roll`, `dice` e `pass`), por isso os pedidos concretos vão mudar. O
que é geral e deve manter-se:

**Fase 2 — jogo distribuído.** Dois jogadores em computadores diferentes
jogam através de um servidor de testes do professor
(`http://twserver.alunos.dcc.fc.up.pt:8008/`). Os pedidos são feitos com
`fetch` em **POST** com JSON; as atualizações do jogo chegam por
**Server-Sent Events** (`update`, em GET). Os pedidos do ano passado eram
`register`, `join`, `leave`, `notify`, `update` e `ranking` (mais `roll` e
`pass`, específicos do Tâb), com os argumentos `group` (n.º do grupo),
`nick`, `password` e `game` (o identificador devolvido pelo `join`).
Quando não há jogo à espera, o `join` deixa-te à espera de adversário; se
não jogares durante 2 minutos, perdes o jogo.

**Fase 3 — servidor próprio em Node.js** que substitui o do professor:

- ficheiro principal `index.js`, organizado em módulos, que implementa os
  mesmos pedidos e respostas e valida todos os argumentos;
- códigos HTTP: `200` OK, `400` pedido inválido, `401` nick/password
  errados, `404` pedido desconhecido;
- persistência em ficheiros JSON com o módulo `fs` (sem base de dados);
- identificador do jogo gerado com MD5, e passwords cifradas antes de as
  guardar, ambos com o módulo `crypto`:
  `crypto.createHash('md5').update(valor).digest('hex')`;
- **mínimo:** `register` e `ranking`. O resto (`join`, `leave`, `notify`,
  `update`) é valorização, e a integração com o cliente é particularmente
  valorizada;
- publicado em `twserver.alunos.dcc.fc.up.pt`, porta `81XX` (XX = n.º do
  grupo), com as credenciais LDAP do LabCC:

```bash
ssh -J up<nº>@ssh.alunos.dcc.fc.up.pt up<nº>@twserver-be
scp -J up<nº>@ssh.alunos.dcc.fc.up.pt * up<nº>@twserver-be:pasta
```

**Valorizações** (sem elas não se tem a nota máxima):

- **WebStorage** para guardar as classificações dos jogos contra o
  computador, que persistem mesmo depois de reiniciar o navegador;
- **Canvas** para melhorar a apresentação (por exemplo, animações).

**ZIP da 2ª entrega:** os módulos do servidor com `index.js` na raiz, mais
o `index.html`, CSS e JS do cliente, já configurados para falar com o
servidor Node **do vosso grupo**. A 1ª entrega não é reavaliada.

## 5. Grupos, apresentação e regras gerais

- **Grupos** de até 3 pessoas. A lista está numa
  [folha partilhada](https://docs.google.com/spreadsheets/d/e/2PACX-1vTAFI_23NJjf1DvKUvdRWoB5pFdS4cWraPHTIlMc4KYP1oPHG4-_ThGP5nvTTbhVAlSF4c1kDKJiRW9/pubhtml);
  para encontrar grupo usa o Slack. Em último caso podes fazer sozinho.
- **Apresentação:** na semana seguinte a cada prazo, inscreves o grupo no
  [calendário partilhado](https://docs.google.com/spreadsheets/d/1nKH8SYfdcDFVT8TcxIqOMSkpv6UCU_ZKaFPyRuM1x3c/edit#gid=0),
  num horário livre, escolhendo o modo (presencial ou remoto).
- **Plágio:** a prova é anulada e há processo disciplinar (regulamento da
  UP). Na avaliação distribuída não há melhoria nem recurso.
