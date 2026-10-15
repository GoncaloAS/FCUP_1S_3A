---
title: "IPM --- Soluções dos exercícios \"Pratica agora\""
subtitle: "Exercícios de desenho não têm uma resposta única: isto é uma resposta-modelo para comparares com a tua, não um gabarito. Tenta primeiro sozinho."
---

## Aula 1 --- O projeto COL

### P.1 --- Perceber o enunciado do COL

Regras usadas (enunciado, secção 2): o operador move as comportas de
Touvedo **sozinho** desde que o **total largado pela barragem fique abaixo
de 300 m³/s**; **descargas acima de 300 m³/s**, **avisos à população** e
**fechos** precisam de autorização do coordenador, pedida e recebida na
interface.

#### (a) Touvedo larga 180 m³/s; o operador quer mais 100 m³/s. Pode sozinho?

Total depois da manobra: $180 + 100 = 280$ m³/s.

$280 < 300$, por isso **está dentro da autonomia do operador**: pode fazê-lo
sozinho. A manobra passa por **pedida → em curso → concluída**, sem passar
por "à espera de autorização".

Mesmo assim, é um comando que muda o estado do rio (regra 3 da sala): a
confirmação deve mostrar **o efeito** ("Touvedo passa de 180 para 280
m³/s"), e não um "tem a certeza?" genérico.

#### (b) Mesma situação, mas mais 150 m³/s. Por que estados passa a manobra?

Total depois da manobra: $180 + 150 = 330$ m³/s.

$330 > 300$, por isso **precisa de autorização do coordenador**. Pelo ciclo
de vida:

1. **pedida** --- o operador define a manobra (abrir a comporta para mais
   150 m³/s);
2. **à espera de autorização** --- a interface envia o pedido ao
   coordenador, e a comporta **ainda não se mexe**;
3. **autorizada** --- o coordenador aprova, na interface;
4. **em curso** --- o operador executa, e a comporta passa por "a abrir";
5. **concluída** --- a comporta fica "aberta a N metros" e o total chega a
   330 m³/s.

Se o coordenador recusar (ou o operador desistir), a manobra passa de "à
espera de autorização" para **cancelada** e o total fica nos 180 m³/s.

Repara que **o mesmo gesto** (abrir uma comporta) segue caminhos
diferentes consoante o número final. A interface tem de mostrar isso
**antes** de o operador confirmar ("isto ultrapassa 300 m³/s: vai pedir
autorização"), para não o surpreender.

#### (c) Tocar as sirenes a jusante de Touvedo. Pode sozinho?

**Não, na leitura mais segura: precisa de autorização.** As sirenes servem
para avisar as pessoas junto ao rio, por isso são um **aviso à
população**, e os avisos à população estão na lista do que precisa do
coordenador.

O enunciado não o diz com todas as letras: põe as sirenes na lista de
recursos, ao lado das SMS, e nunca diz "sirene = aviso". Por isso está na
lista de dúvidas a levar à aula. No relatório, se assumirem isto, **escrevam
a suposição** (o que conta é a decisão justificada).

Um aviso segue os seus próprios estados: **rascunho → pendente** (à espera
do coordenador) **→ emitido**.

#### (d) A comporta 2 de Touvedo está em modo manual local e é preciso fechá-la. O que faz a interface?

"Modo manual local" quer dizer que **alguém na barragem assumiu o controlo
no local** e o **controlo remoto deixou de estar disponível**. Portanto:

- a interface **não pode** mandar fechar a comporta, e não deve fingir que
  pode. O comando "fechar" fica **visível mas inativo** (não escondido:
  regra 2, não há menus escondidos), com a razão escrita ("controlo local
  na barragem");
- o estado "em modo manual local" tem de se distinguir **num relance** dos
  estados normais (regra 4: o operador cansado não pode confundir "não
  responde" com "está fechada");
- o que o operador **pode** fazer sozinho: **enviar uma equipa** de terreno
  (há 2 equipas das barragens) à barragem.

(Nota: a forma de falar com a pessoa que está no local não vem no
enunciado. Aqui a suposição é que o contacto se faz pela equipa enviada.)

#### (e) Volume útil de Touvedo a meio e entrada − saída = 250 m³/s. Quanto tempo até encher?

O volume útil total é 4,5 hm³ = 4 500 000 m³. A meio, falta encher metade:

$$\frac{4\,500\,000}{2} = 2\,250\,000 \text{ m}^3$$

A albufeira ganha 250 m³ por segundo (é o que entra a mais do que sai):

$$\frac{2\,250\,000 \text{ m}^3}{250 \text{ m}^3/\text{s}} = 9\,000 \text{ s}$$

$$9\,000 \text{ s} \div 60 = 150 \text{ min} = \mathbf{2 \text{ h } 30 \text{ min}}$$

A conta supõe que a diferença se mantém constante. Na realidade muda (a
chuva aumenta, o operador abre comportas), por isso o número tem de ser
**recalculado continuamente**. É exatamente o que o exemplo de "ouro" do
enunciado sugere mostrar: não só "está a 50 %", mas **"a este ritmo, enche
dentro de 2 h 30"**, que é o que o operador precisa para decidir.

## Aula 2 --- Personas

### P.2 --- Personas do COL

As personas são o item 2 do R1, ou seja, **trabalho avaliado do grupo**, e
as regras de IA da disciplina (Aula 1) proíbem que sejam geradas por IA.
Por isso a "solução" aqui é uma **grelha de verificação** para corrigires
as tuas. O exemplo da Mariana (cantina) no resumo serve de modelo de
formato.

#### Resposta

Passa cada uma das tuas três personas por estas perguntas.

**O que o enunciado exige:**

- São **três**, e **uma tem pouca experiência** (ex.: meses no posto e não
  anos). Esta é a que o *cognitive walkthrough* vai simular, porque a
  pergunta é "um **operador novo** saberia o que fazer?".
- Cada uma tem **nome**, **experiência** e **o que a põe em dificuldade**.

**As 10 regras (Aula 2):**

- **Regra 7:** as três são operadores, com o mesmo cargo. Se, ao tirares o
  nome e a idade, as três ficam iguais, **falhaste a regra 7**. Têm de
  diferir no **padrão de comportamento**: por exemplo, como reagem à
  incerteza, quanto confiam nos sensores, se preferem agir cedo ou esperar
  por mais dados, ou se hesitam em incomodar o coordenador de madrugada.
- **Regras 2, 5 e 10:** 3 ou 4 **objetivos** por persona, e objetivos, não
  tarefas. "Que a água não chegue ao Passeio sem a população ter sido
  avisada" é um objetivo. "Abrir a comporta 2" é uma tarefa.
- **Regra 4:** um ou dois detalhes pessoais concretos, e não uma biografia.
- **Regra 8:** não inventes uma quarta ou quinta "por via das dúvidas".

**A ficha do Módulo 03:**

- **Frustração:** deve ligar-se a um **desafio de interface** (item 1 do
  R1). Por exemplo, "perder um alerta no meio de muitos" liga-se a um
  problema de desenho; "o café da sala é mau" não liga a nada.
- **Contexto:** usa o que o enunciado dá: turno de 8 h, a regra "3 da
  manhã, seis horas dentro do turno", o coordenador fora da sala, 2
  monitores e a parede de ecrãs.

**Erros comuns:**

- três personas que são "o júnior, o médio e o sénior" sem mais nada;
- objetivos que são funcionalidades ("quer um mapa do rio");
- personas que não voltam a aparecer no resto do R1. Cada missão (item 3)
  deve dizer **de que persona** é.

## Aula 2 --- Esboçar

### P.4 --- Esboços antes da S3

As alíneas (a)--(c) são de compreensão e têm uma resposta certa. A (d) é
de desenho: a resposta é um **modelo** para comparares, não um gabarito.

#### (a) Ordem no contínuo esboço → protótipo, e comunicar ou verificar?

**Ordem (do esboço ao protótipo):** (2) → (4) → (1) → (3).

| Artefacto | Posição | Serve sobretudo para |
|:--------------------------|:----------------|:------------------------------|
| (2) Dez desenhos a lápis em 20 min | Esboço puro | **Comunicar**: explorar e discutir ideias em aberto |
| (4) *Storyboard* em *post-its* | Esboço | **Comunicar**: mostrar o fluxo de uma missão, cena a cena |
| (1) *Wireframe* Figma, sem cor | Meio do contínuo | **Verificar** (começa a ser): é sobre ele que se faz a avaliação heurística |
| (3) Protótipo Figma clicável | Protótipo | **Verificar**: testar com pessoas se a interface funciona |

**Porquê esta ordem:** a diferença que conta **sempre** é o **propósito**
(comunicar vs. verificar); a forma (lápis vs. computador) costuma
acompanhar, mas nem sempre. Os dois primeiros ainda fazem perguntas
("e se fosse assim?"), os dois últimos já dão respostas e são testados.

**Cuidado com a (4):** um *storyboard* é um esboço (cenas-chave, como banda
desenhada). Mas, se o usares no *cognitive walkthrough* para ver onde um
operador novo se engana, nesse momento estás a usá-lo para **verificar**.
É por isso que os slides dizem que é um contínuo e não duas caixas.

#### (b) Uma imagem gerada por IA na S3: atributos, risco e regra

**Atributos que falham** (compara com a tabela "esboço vs. maqueta gerada
por IA"):

- **Rápido, descartável, abundante:** é **uma** imagem, polida. Ninguém a
  trata como descartável e não há outras para comparar.
- **Vocabulário claro:** parece acabada, por isso diz "isto está
  decidido" quando a S3 é para ideias em aberto.
- **Resolução limitada** e **coerência com o estado:** cores, ícones e
  números exatos estão muito acima do estado do conceito, que na S3 ainda
  nem foi escolhido.
- **Sugere e explora, catalisador:** fecha a discussão em vez de a abrir.

**Risco para o grupo:** as pessoas **reagem às cores, não à ideia**; a
discussão fica presa a uma única resposta (falta o *getting the right
design*); e o colega **não consegue explicar cada decisão** que lá está,
porque não foi ele que as tomou. Isso é grave porque o exame também avalia
o trabalho do grupo.

**Regra quebrada:** imagens geradas por IA são **opcionais e só para
ilustrar um conceito que o grupo já escolheu, nunca como fonte de ideias**
(Módulo 04). Quebra também as regras da Aula 1: gerar esboços ou conceitos
de desenho com IA não é permitido, nem apresentar como evidência algo que
o grupo não criou.

**O que fazer:** deixar a imagem de lado e esboçar à mão **várias**
alternativas para o painel, como pede a S3.

#### (c) Artefacto e fidelidade em cada fase de avaliação do COL

| Fase do COL | Método | Artefacto | Fidelidade |
|:-------------------|:---------------------|:---------------------|:--------------|
| Fase 1, S6 (3 nov) | *Cognitive walkthrough* | Esboços | Baixa |
| Fase 2, S8 (17 nov) | Avaliação heurística | *Wireframes* no Figma | Média |
| Fase 3, S9 (24 nov) | Testes de usabilidade | Protótipo interativo | Média a alta |

**Onde se afasta da tabela dos slides:** a tabela "do desenho inicial ao
desenho final" põe a **avaliação heurística** sobre **protótipos de alta
fidelidade**. O COL fá-la sobre ***wireframes***, que são de média
fidelidade (posição e tamanho exatos, mas sem cor, sem acabamento e sem
comportamento). O resto coincide: *walkthrough* sobre esboços ou baixa
fidelidade, testes de usabilidade mais tarde, sobre algo que já se
comporta como o sistema. No projeto, **vale o enunciado**.

#### (d) Cinco formas diferentes de pôr o *reset* no relógio de ginásio

**Resposta-modelo** (as tuas podem ser outras; o que interessa é que os
mecanismos sejam diferentes):

1. **Botão próprio para o *reset***, com um ícone ↺ e ligeiramente
   recolhido, para não se carregar sem querer. Mecanismo: um botão físico
   dedicado.
2. **Etiquetas no ecrã por cima de cada botão** (*soft keys*), que mudam
   com o modo: no cronómetro parado, a etiqueta do botão de baixo diz
   "RESET". Mecanismo: o ecrã diz o que cada botão faz.
3. **Rodar a luneta para trás** até ao zero. Mecanismo: um controlo
   rotativo, em que a direção tem significado.
4. **Segurar START/STOP com o cronómetro parado**, com uma barra no ecrã a
   encher e o texto "segura para reset". Mecanismo: toque longo, **mas com
   retorno visível** (sem isso seria o erro do projetor Leitz).
5. ***Reset* automático**: ao iniciar uma corrida nova, o cronómetro
   anterior fica guardado num histórico e o novo começa em zero.
   Mecanismo: não há *reset*, o sistema decide.

**Verificação dos teus esboços:**

| Pergunta | Se a resposta for "não" |
|:-------------------------------|:-----------------------------------|
| Os cinco têm mecanismos diferentes? | Dois que só mudam o botão de sítio contam como um |
| Fizeste-os em cerca de 10 minutos? | Estás a desenhar demais: menos detalhe |
| O acabamento é igual ao da ideia (vago)? | Coerência com o estado: tira pormenores |
| Cada um tem uma anotação a explicar o que não se vê? | Acrescenta (ex.: "segurar 2 s") |
| Cada um resolve pelo menos uma das três falhas? | Diz qual: ver, lembrar ou verificar o estado |

## Aula 2 --- T4 (task flows)

### P.3 --- Missões do COL

Tal como as personas, as missões são trabalho avaliado do grupo (item 3 do
R1, feito na S4). A solução é uma grelha de verificação e um
**contraexemplo** comentado.

#### Resposta

**Contraexemplo (uma missão mal escrita):**

> Missão: usar o painel de comportas. 1. Clicar no separador "Touvedo".
> 2. Clicar em "Abrir comporta". 3. Clicar OK.

O que está mal:

1. **O objetivo está escrito com as palavras da interface** ("usar o
   painel"), e não com o objetivo do operador (ex.: "baixar o nível de
   Touvedo antes da preia-mar").
2. **Não tem situação de partida.** O enunciado exige-a em cada missão:
   caudais, estado dos equipamentos, hora, maré.
3. **Não diz o que o sistema mostra** em cada passo, só cliques.
4. **Não tem critério de sucesso** verificável.
5. **Pressupõe já uma interface** ("separador") e, pior, um separador
   esconde informação: viola a regra 2 da sala (não há menus escondidos).
   A missão deve poder ser seguida em **qualquer** alternativa de esboço,
   porque é com ela que outro grupo vai avaliar os teus esboços.
6. **Não diz quanto se abre.** Por isso não se sabe se passa os 300 m³/s
   (e se precisa de autorização).

**Grelha para verificar as tuas cinco:**

| Verificação | Como confirmar |
|:------------------------|:--------------------------------|
| Cobertura | Pelo menos 1 normal, 1 de cheia e 1 avaria no conjunto |
| Situação de partida | Números inventados mas **plausíveis** face aos valores reais (ex.: Lima em seca < 100 m³/s; nada acima da capacidade das comportas) |
| Objetivo | Nas palavras do operador e ligado a uma **persona** |
| Passos | Uma linha por passo: faz / o sistema mostra |
| Sucesso | Dito com os **estados obrigatórios** (ex.: "a manobra fica *concluída*", "o alerta fica *resolvido*") |
| Autorização | Pelo menos uma missão passa por "à espera de autorização" |
| Fim de turno | Pelo menos uma acaba ou passa por uma **passagem de turno** |
| Avaliável | Um colega de outro grupo consegue segui-la sem te perguntar nada |

## Aula 3 --- O método 10x10

### Cantina --- 10x10 aplicado ao projeto

Desafio: "a Mariana quer garantir o almoço sem perder tempo de estudo".

#### Passo 1 --- o desafio e as suposições

**Desafio de desenho:** como pode um estudante com pouco tempo entre aulas
**garantir** uma refeição que lhe sirva (a Mariana é vegetariana) **sem
perder tempo** em filas e **podendo mudar de plano** se a aula atrasar?

Está escrito com os objetivos da persona (Aula 2), e não com uma solução.
"Fazer uma app de reservas" já seria um conceito e fecharia logo o funil.

**Suposições** (para poder avançar, tal como no exemplo do "Connect!"):

- a cantina sabe de manhã o menu do dia e quantas doses tem de cada prato;
- a maioria dos estudantes tem telemóvel com dados, mas **não** se pode
  assumir que instalam mais uma app;
- o cartão de estudante tem NFC e já é usado para pagar;
- a cantina tem algum espaço à entrada (para um ecrã, cacifos, etc.);
- o funcionário da cantina (a 2.ª persona) não pode ter trabalho extra
  significativo por cada pedido.

#### Passo 2 --- 10 conceitos com mecanismos diferentes

Cada conceito responde ao desafio de uma maneira **diferente**. Entre
parêntesis está o que o distingue:

1. **App de reserva com hora marcada** (reserva antecipada, numa app
   própria): escolhe o prato e a hora de levantamento.
2. **Fila virtual num quiosque à entrada** (no local, no momento): tira
   senha e recebe uma notificação quando for a vez dela.
3. **Bot de mensagens** (conversa, num canal que ela já usa): "vegetariano
   às 12h45?" "Reservado. Código 482."
4. **Encostar o cartão de estudante** a um leitor à saída da sala
   (NFC, um gesto físico): encomenda o "prato habitual".
5. **Pedido recorrente / assinatura** (configurar uma vez só):
   "vegetariano, terças e quintas, 12h45". É automático e ela só cancela.
6. **Cacifos aquecidos com código** (levantamento sem contacto): a comida
   fica pronta num cacifo e ela abre-o com o código.
7. **Entrega no edifício do departamento** (a comida é que se desloca):
   um carrinho passa às 12h35 no átrio de Biologia.
8. **Painel público de doses em tempo real** (só informação, sem
   transação): ecrãs nos corredores e uma página web com "vegetariano:
   12 doses".
9. **Integração com o horário académico** (contexto automático): o
   sistema conhece o horário dela, propõe a hora e, se o professor fechar
   o sumário mais tarde, adia a reserva.
10. **Frigorífico "grab & go" com pagamento *self-service*** (elimina a
    reserva): pratos já embalados, ela tira um e paga com o cartão.

Repara que **nenhum** é "a app com outra cor". Os conceitos variam em
**canal** (app, mensagem, cartão, ecrã), **momento** (antes ou no local),
**quem se desloca** (ela ou a comida) e **tipo de ação** (reservar,
informar, eliminar a reserva).

#### Reduzir com uma grelha de avaliação (Aula 2, T3)

**Critérios**, tirados dos objetivos da Mariana, mais o custo para a
cantina:

- **c1** saber antes se há comida que lhe sirva
- **c2** não perder tempo (sem fila, 20 minutos no total)
- **c3** mudar de plano se a aula atrasar
- **c4** custo para a cantina (4 = barato)

A escala é **1--4** (número par, sem meio-termo). **Heurística de
agregação**, decidida antes de pontuar: somar, e há **veto** se c1 ou c2
tiverem 1, porque são os objetivos centrais da persona.

| Conceito | c1 | c2 | c3 | c4 | soma | decisão |
|:--|:-:|:-:|:-:|:-:|:-:|:--|
| 1 App de reserva | 4 | 4 | 3 | 2 | 13 | fica |
| 2 Fila virtual | 2 | 3 | 2 | 3 | 10 | --- |
| 3 Bot de mensagens | 4 | 4 | 3 | 3 | **14** | **fica** |
| 4 Cartão NFC | **1** | 3 | 1 | 2 | 7 | **veto** (não vê o menu) |
| 5 Pedido recorrente | 2 | 4 | 2 | 3 | 11 | --- |
| 6 Cacifos | 3 | 4 | 4 | 1 | 12 | fica |
| 7 Entrega no departamento | 3 | 4 | 2 | 1 | 10 | --- |
| 8 Painel de doses | 3 | 2 | 3 | 4 | 12 | fica |
| 9 Integração com horário | 3 | 4 | 4 | 2 | 13 | fica |
| 10 Grab & go | **1** | 4 | 4 | 3 | 12 | **veto** (não sabe antes) |

**Resultado:** sobrevivem **5 de 10** (3, 1, 9, 6, 8), no espírito dos "6 de 10" do
professor. O mais promissor é o **3 (bot)**: tem a melhor soma, e o
funcionário não precisa de um sistema novo.

Os outros **não se deitam fora**. O 9 (adiar quando a aula atrasa) e o 8
(mostrar as doses) são ótimos candidatos a **variações do 3** no passo 5.
Por exemplo, o bot avisa "só restam 3 doses" e pergunta "a aula atrasou?
adio para as 13h?".

Com um só avaliador (tu) isto é só um treino. O método pede **várias
grelhas**, de pessoas **diferentes**, de outros grupos.

#### Verificação --- o que torna cada par diferente?

Para cada par pergunta-se: "se eu descrever os dois numa frase, a frase
muda **o mecanismo**, ou só **a aparência**?"

- **4 vs. 10:** gesto de pedir (cartão) contra não haver pedido nenhum
  (tirar da prateleira). São mecanismos diferentes.
- **2 vs. 6:** os dois atuam no local, mas um organiza a **espera** e o
  outro **elimina** o contacto com o balcão. São diferentes.
- **5 vs. 9:** os dois são "automáticos", mas um repete uma regra fixa e o
  outro reage ao contexto (o horário real). São diferentes.
- **1 vs. 3: é o par mais próximo.** Os dois são "reserva antecipada
  remota" e só o **canal** muda: uma app nova contra um mensageiro que ela
  já usa. É defensável como diferente, porque a suposição "não instalam
  mais uma app" torna o canal decisivo. Mas um avaliador exigente podia
  contar os dois como um só.

  Nesse caso substituía-se um deles por uma ideia com outro mecanismo,
  por exemplo um **mercado de troca de reservas entre estudantes** ("já
  não vou, fica com a minha"). Isso resolve o c3 de outra forma.

Se dois conceitos só diferissem em "botão verde" contra "lista de
pratos", eram **um** conceito: isso é uma variação (passo 5), não um
conceito novo (passo 2).

## Aula 4 --- Como falham as interfaces

### P.5 --- Analisar interfaces que falham

Ferramentas a usar em todas as alíneas: a lista **informação /
apresentação / interação** e as **três falhas** (funções que não se veem,
códigos que não se lembram, estado que não se verifica). As propostas de
redesenho são **respostas-modelo**.

#### (a) Euro NCAP: piscas, limpa-vidros, buzina, quatro piscas e SOS num ecrã tátil

**Informação.** São funções de segurança, precisas **a qualquer momento e
sem aviso** (buzinar para evitar um choque, ligar os quatro piscas no fim
de uma fila, chamar o SOS). Por isso têm de estar **sempre** disponíveis,
como a velocidade no exemplo do slide, e não "quando o menu estiver
aberto".

**Apresentação.** Num ecrã tátil os comandos são desenhos num vidro liso,
muitas vezes dentro de menus ou de outro separador. O **estado** (o pisca
está ligado? o limpa-vidros está em "auto"?) também fica no ecrã, longe da
mão.

**Interação.** É aqui que falha mais. Um botão físico ou uma alavanca
**encontra-se pelo tato** a 120 km/h, sem tirar os olhos da estrada; um
ecrã tátil **não tem relevo nem retorno ao toque**, por isso obriga a
olhar para baixo para acertar no sítio, e com o carro a abanar é fácil
falhar.

**As três falhas:**

1. **Funções que não se veem:** se a função está num submenu, não está à
   vista quando é precisa.
2. **Códigos que não se lembram:** a sequência de toques (menu → separador
   → botão) é uma combinação que se tem de saber de cor, e muda de marca
   para marca (como as alavancas trocadas dos carros japoneses).
3. **Estado que não se verifica:** numa alavanca, a **posição** mostra o
   estado (alavanca para baixo = pisca para a esquerda); num ecrã, só se
   sabe olhando.

**O que correu mal, numa frase:** decidiu-se pelo lado da máquina (um
ecrã é mais barato e mais "limpo" do que dez botões) e não pelas
**limitações humanas** (lição 2): o condutor tem os mesmos olhos e a mesma
atenção ("lei de Darwin"), e tirar os olhos da estrada é exatamente o que
não pode fazer. E como **os erros custam mais**, um toque falhado já não é
um incómodo: é um acidente. Daí o Euro NCAP tirar pontos.

#### (b) O comando do projetor Leitz: diagnóstico e redesenho

**Diagnóstico com as três falhas:**

1. **Função que não se vê:** só há um botão, e nada nele mostra que
   recuar existe.
2. **Código que não se lembra:** "toque curto avança, toque longo recua" é
   uma regra arbitrária, que só está no manual. E não se sabe **quanto
   tempo** é "longo".
3. **Estado que não se verifica:** enquanto se carrega no botão, nada
   diz se aquilo já conta como toque longo. Só se descobre depois, quando
   o diapositivo muda para o lado errado. Quem segura um pouco demais
   recua sem querer e pensa que a culpa é sua (o mito do erro humano).

**Redesenho (resposta-modelo):** **dois botões**, um para cada direção.

- **Informação:** a única informação de que a pessoa precisa é "para que
  lado vou". Cada botão mostra isso com uma seta (◀ e ▶).
- **Apresentação:** o botão da direita é "avançar" e o da esquerda
  "recuar", porque os diapositivos se leem da esquerda para a direita. As
  setas e as formas são em **relevo** (por exemplo, o de avançar maior),
  porque o orador está numa sala escura e a olhar para o público, não para
  o comando.
- **Interação:** **um toque = uma ação**, sem depender do tempo. Erra-se
  menos, e quando se erra corrige-se com um toque no outro botão.

Resolve as três falhas: as duas funções **veem-se**, não há **código** para
lembrar, e o resultado de cada toque é imediato e previsível. (Um
interruptor basculante, que inclina para um lado ou para o outro, seria
uma variação da mesma ideia.)

#### (c) A porta com puxador e placa "PUSH"

**Porque precisa da placa:** a forma do puxador **diz "puxa"**. Uma pega
que se agarra com a mão fechada convida a puxar. A porta abre a empurrar,
por isso a forma e a ação estão em contradição, e a placa é um remendo
escrito por cima de um erro de desenho.

**De quem é a culpa (lição 1):** do **desenho**. A pessoa que puxa fez o
que a porta lhe mostrou. É o mesmo caso dos tratores: chamar-lhe "erro
humano" esconde que o desenho ignorou como as pessoas reagem (agarram e
puxam antes de lerem uma placa).

**Mudança que torna a placa desnecessária:** do lado em que se
**empurra**, tirar o puxador e pôr uma **placa lisa de metal** à altura da
mão: não se consegue agarrar uma superfície plana, por isso só dá para
empurrar. Deixar a pega só do lado em que se **puxa**. Alternativa: uma
porta de vaivém, que abre para os dois lados, e assim qualquer gesto
funciona.

(Nota adicional, do livro de Norman: a forma da pega é um **sinalizador**;
o redesenho consiste em pôr o sinalizador certo em cada lado da porta.)

## Aula 5 --- Modelos mentais

### P.6 --- Modelos mentais

Ferramentas: os **sete conceitos** (visibilidade, *affordance*,
mapeamento, restrições, transferência, associações culturais, *feedback*)
e as **seis características** dos modelos mentais (incompletos, instáveis,
pouco exatos, simplificados, supersticiosos, regras se-então). As
propostas de desenho são **respostas-modelo**.

#### (a) Termóstato, passadeira e portátil: característica e correção

| Situação | Característica | Porquê |
|:----------|:--------------|:----------------------------------|
| Termóstato a 30 °C | **Supersticioso** (e pouco exato) | Acredita-se num efeito ("aquece com mais força") que o mecanismo não tem: o termóstato é um interruptor. |
| Botão da passadeira | **Supersticioso** | Repete-se um ritual (três toques) que não muda nada, porque o ciclo é fixo ou o botão nem está ligado. |
| Reiniciar o portátil | **Simplificado** e **regra se-então** ("se está lento, então reinicio") | Um fenómeno complexo (memória cheia, processos presos) fica reduzido a uma regra. Como muitas vezes resulta, a regra fica reforçada e é aplicada onde não serve (o projetor). |

**Correções pela imagem do sistema:**

- **Termóstato:** falta **visibilidade do estado** e **feedback**. O
  mostrador deve dizer "a aquecer --- temperatura atual 17 °C, chega a
  21 °C em cerca de 40 min", e esse tempo **não muda** quando se pede
  30 °C. O utilizador vê que pedir mais não acelera nada, só muda o ponto
  em que para.
- **Passadeira:** falta **feedback**. Ao primeiro toque acende-se uma luz
  "pedido registado", que fica acesa até ao verde, e há uma contagem
  decrescente. Os toques seguintes não mudam nada visível, por isso a
  superstição perde a razão de ser. (Se o botão não está ligado, a
  imagem do sistema honesta é **não ter botão**: um botão que não faz nada
  é uma mentira.)

#### (b) A tesoura nas mãos de um canhoto

Resposta-modelo (o slide faz a pergunta mas não dá a resposta).

**O que continua certo:** a *affordance* (serve para cortar, pode magoar),
o mapeamento e as restrições dos buracos (buraco grande para os dedos,
pequeno para o polegar) funcionam em qualquer mão. Um canhoto **consegue**
pegar-lhe e abri-la e fechá-la.

**O que falha:** o modelo "de olhar" não mostra **qual lâmina fica por
cima**. Numa tesoura para destros, a lâmina de cima está do lado direito.
Na mão direita, o aperto natural (polegar a empurrar, dedos a puxar)
**encosta as lâminas** uma à outra e é isso que corta. Na mão esquerda, o
mesmo aperto **afasta-as**: o papel dobra-se entre as lâminas em vez de
ser cortado, e a lâmina de cima **tapa a linha** por onde se quer cortar.

**Porquê:** o modelo formado só de olhar é **incompleto**. A parte do
mecanismo que decide se corta bem (o lado das lâminas) não está na imagem
do sistema, e só se descobre ao "correr" o modelo, isto é, ao cortar.

#### (c) A comporta que leva três minutos

**O modelo que o operador constrói:** se o painel só mostra "120", o
operador conclui que **já está** a 120. Quando o nível a jusante não
responde, ou o caudal medido mostra 92, a explicação mais à mão é "o
comando não foi aceite" ou "a comporta encravou". O modelo é
**incompleto** (não inclui o tempo que a comporta leva a mexer-se) e
**pouco exato**. A regra se-então que daí sai, "se não mudou, carrego
outra vez", é a do segundo toque.

**O que evita o segundo comando:** o **feedback** e a **visibilidade do
estado**, com comando e estado em separado:

- feedback imediato (menos de 0,1 s) de que o pedido foi aceite;
- "pedido 120 --- atual 92 --- a abrir", com a barra a avançar e o tempo
  previsto até chegar;
- uma **restrição**: enquanto a manobra está "em curso", um novo comando
  sobre a mesma comporta mostra que **substitui** o anterior, em vez de
  se somar a ele em silêncio.

#### (d) O Wi-Fi: regras se-então e o que a aplicação deve mostrar

- **Modelo A:** "**se** o Wi-Fi está lento, **então** reinicio o
  *router* (porque se cansa), e fica rápido."
- **Modelo B:** "**se** o Wi-Fi está lento, **então** mudo de canal
  (porque os vizinhos estão no mesmo), e fica rápido."

**Para corrigir o modelo A**, a aplicação tem de tornar visível o que o
modelo B usa:

- o **canal** em uso e **quantas redes vizinhas** estão nesse canal, ou
  um nível de interferência;
- depois de um reinício, **se o canal mudou** (interpretação: muitos
  *routers* escolhem o canal ao arrancar, e isso explicaria porque é que
  reiniciar "às vezes resulta", pela razão errada);
- um botão "mudar para um canal livre", que dá ao utilizador a ação do
  modelo certo.

## Aula 5 --- As sete fases e os dois golfos

### P.7 --- As sete fases e os dois golfos

Ferramentas: as **sete fases**, os **dois golfos** e os **sete
conceitos**. As propostas de desenho são **respostas-modelo**.

#### (a) As sete fases para "abrir a descarga de fundo de Touvedo"

Dados usados: a descarga de fundo de Touvedo larga **50 m³/s** e tem os
estados **fechada, a abrir, aberta, avariada**; o operador abre-a sozinho;
a manobra passa por pedida → em curso → concluída. Supõe-se um total
atual de 200 m³/s, que passa para 250 (abaixo de 300).

| Fase | O que o operador faz | O que o painel tem de oferecer |
|:---------|:---------------------|:---------------------------------|
| 1 Objetivo | Largar mais 50 m³/s em Touvedo abrindo a descarga de fundo | O estado atual visível sem menus: descarga "fechada", total largado 200 m³/s |
| 2 Intenção | "Uso o comando da descarga de fundo de Touvedo" | **Visibilidade** e **mapeamento**: o comando está no painel de Touvedo, desenhado na base da barragem, separado das comportas e do grupo |
| 3 Sequência | Escolher Touvedo, escolher a descarga de fundo, "abrir", confirmar | Cada passo visível. **Restrições:** "abrir" fica desativado se o estado for "avariada", e a confirmação mostra o efeito: "total passa de 200 para 250 m³/s --- não precisa de autorização" |
| 4 Execução | Carregar em "abrir" e confirmar | **Affordance:** um botão que parece um botão, difícil de acionar por engano (regra 3 da sala) |
| 5 Perceção | O estado muda no ecrã | **Feedback** imediato: "a abrir" aparece em menos de 0,1 s |
| 6 Interpretação | "A válvula está a abrir, o caudal vai subir 50" | Comando e estado em separado: pedido "aberta", atual "a abrir", caudal da descarga de 0 a subir para 50 |
| 7 Avaliação | "Está aberta? O total chegou a 250? O rio a jusante responde?" | Estado "aberta", gráfico do total largado com a linha do alvo (250) e o nível a jusante; manobra "concluída" no registo |

#### (b) Execução ou avaliação?

| Caso | Golfo principal | O que o atravessa |
|:--------------|:-----------|:--------------------------------------|
| **(1)** Comando Leitz | **Execução** ("como recuo?"): a função não se vê e o toque longo é um código | Dois botões com setas (mapeamento e visibilidade): um para avançar, outro para recuar |
| **(2)** `*72` do telefone | **Avaliação** ("ficou reencaminhado?"): nenhum estado mostra o reencaminhamento | Uma luz ou um texto permanente "reencaminhado para 2345" (visibilidade do estado). (Lembrar o código é o golfo da execução.) |
| **(3)** "A guardar..." sem progresso | **Avaliação** ("está a andar ou parou?") | Barra de progresso ou tempo restante e, no fim, "guardado às 14:02" (feedback) |
| **(4)** Quatro bicos, quatro botões em linha | **Execução** ("qual é o botão deste bico?") | Mapeamento: botões dispostos no mesmo quadrado que os bicos, ou um pequeno desenho junto a cada botão |

#### (c) O frigorífico: o que mudar e como redesenhar

**O que mudar, com o modelo real.** O controlo A (FREEZER) dá o **frio
total**; o controlo B (FRESH FOOD) **divide** esse frio entre os dois
compartimentos.

- Só B, para mandar mais ar frio para o congelador: o congelador arrefece,
  mas o frigorífico, que estava bem, recebe menos frio e **aquece**.
- Só A, para mais frio total: o congelador arrefece, mas o frigorífico
  **também arrefece**, e fica frio demais.
- Por isso mudam-se **os dois**: B um pouco para o lado do congelador e A
  um pouco para cima, de forma que o frigorífico recebe mais ou menos o
  mesmo frio de antes e o extra vai para o congelador. Depois **espera-se
  24 horas** e corrige-se, porque não há outra forma de avaliar.

**Redesenho (resposta-modelo):**

- **Golfo da execução:** em vez de dois botões com o nome de
  compartimentos, o utilizador escolhe **a temperatura de cada
  compartimento em °C**, e um controlador calcula o compressor e a
  válvula. A alternativa mais barata é dar aos botões o nome do que fazem
  ("frio total" e "divisão congelador ↔ frigorífico"), para a imagem do
  sistema mostrar o mecanismo.
- **Golfo da avaliação:** um mostrador com a **temperatura atual de cada
  compartimento**, o alvo e uma seta de tendência ("a descer"), em vez de
  24 horas de espera às cegas.

#### (d) Porque o *walkthrough* avalia o primeiro uso, e um elemento para os dois dias

**Porque o primeiro uso:** na aprendizagem exploratória o utilizador não
tem expectativas fortes, por isso **cada uma das sete fases é consciente e
pode falhar**. As sete perguntas do *walkthrough* encontram exatamente
esses pontos. No uso repetido as fases encolhem em ciclos rápidos e os
problemas aparecem como tempo perdido e pequenos erros, que se medem em
testes de usabilidade (Módulo 11).

**Um elemento para os dois dias (resposta-modelo):** o **estado de cada
troço do rio na parede**, sempre no mesmo sítio, com cor **e** palavra
(normal, vigilância, alerta amarelo, laranja, vermelho, emergência).

- **Terça-feira normal:** tudo "normal", nada se mexe nem pisca; lê-se
  num relance, com carga atencional baixa.
- **Primeira noite de cheia:** o mesmo troço muda de cor, mostra a
  tendência do nível e a próxima ação. O operador encontra-o **onde
  sempre o viu** (transferência do uso diário), por isso não precisa de
  procurar nada no momento em que as sete fases voltam todas.

## Aula 5 --- Processamento de informação e carga

### P.8 --- Processamento de informação e carga

#### (a) Carga cognitiva ou atencional?

| Tarefa | Carga | Porquê |
|:----------------|:-----------|:-----------------------------------|
| **(1)** Vigiar a parede 8 h sem incidentes | **Atencional** | Não há nada para decidir; o custo é manter a atenção e reparar a tempo. |
| **(2)** Decidir quanto largar em Touvedo | **Cognitiva** | Juntar dois troços, prever o efeito da descarga, decidir. |
| **(3)** Encontrar um alarme novo entre indicadores a piscar | **Atencional** | O custo é reparar no que é novo entre várias coisas que competem pela atenção. |
| **(4)** Ler 30 valores e escolher o troço mais crítico | **Cognitiva** | Comparar valores e decidir. (Há atenção também, mas o custo principal é comparar.) |

#### (b) As seis etapas para "ver um alarme novo e reconhecê-lo"

| Etapa | O que acontece |
|:-------------|:------------------------------------------------|
| Entrada | Luz e cor do alarme num dos 12 ecrãs da parede (e um som, se houver) |
| Codificação | Juntar a cor, o ícone e o texto num só significado: "alarme novo no troço X" |
| Comparação mental | Procurar na memória o que significa: que nível é? já vi este alarme hoje? |
| Seleção da resposta | Decidir que o vai reconhecer (e depois tratar) |
| Execução da resposta | Levar o rato ou a mão ao comando "reconhecer" no ecrã privado |
| Saída | O clique ou a tecla |

**Estrangulamento mais provável às 3 da manhã:** a **entrada e a
codificação**, ou seja, reparar no alarme. Com cansaço e seis horas de
turno, a atenção está baixa, e um alarme novo perde-se se houver outras
coisas a mexer ou a piscar na parede.

**Decisão de desenho que o alivia (resposta-modelo):** só os alarmes
**novos** se mexem ou piscam (os reconhecidos ficam parados), o vermelho
fica reservado para o perigo, há um som curto para cada alarme novo, e o
texto diz o troço e o nível por extenso, para a comparação mental não
depender de decorar códigos. Na execução, um atalho de uma tecla para
"reconhecer o alarme mais recente".

## Aula 5 --- Cognição fora da cabeça

### P.9 --- Cognição fora da cabeça

#### (a) Propagação de uma descarga de 280 para 420 m³/s

A regra do enunciado: descargas acima de 300 m³/s precisam do coordenador,
e a autorização é **pedida e recebida na interface**. A manobra passa por
pedida → à espera de autorização → autorizada → em curso → concluída.

| Passo | O que acontece | Meio |
|:-:|:--------------------------------------------|:------------------|
| 1 | O operador decide que Touvedo tem de largar 420 m³/s | mental |
| 2 | O operador cria a manobra; a confirmação mostra "280 → 420 m³/s, precisa de autorização"; estado "à espera de autorização" | físico (teclado/rato) e visual |
| 3 | O coordenador, fora da sala, recebe o pedido na interface e lê o efeito | visual e mental |
| 4 | O coordenador autoriza; estado "autorizada" | físico |
| 5 | O operador vê a autorização e executa; estado "em curso" | visual, mental e físico |
| 6 | O sistema move as comportas; o ecrã mostra "pedido 420, atual 350", até "concluída" | visual |
| 7 | A manobra fica no registo e na passagem de turno | escrito |

**Onde fica guardada a ordem:** no **registo da manobra na interface**
(o que se pediu, quem autorizou, quando, e o estado atual) e na
**passagem de turno**. Não fica só na cabeça do operador nem numa chamada
telefónica. É a interface que garante que o operador do turno seguinte
sabe a mesma coisa.

#### (b) 234 × 456 em papel e a numeração romana

**Em papel**, uma parcela por algarismo de 456:

$$234 \times 6 = 1404, \qquad 234 \times 50 = 11\,700, \qquad 234 \times 400 = 93\,600$$

$$1404 + 11\,700 + 93\,600 = 106\,704$$

**Porque é que CCXXXIV × CDLVI é muito mais difícil:** o papel e a
**notação posicional** fazem parte da conta. Cada algarismo vale pela
**posição** (unidades, dezenas, centenas), por isso a multiplicação parte-se
em produtos de um algarismo (tabuada) e em somas alinhadas por colunas, e
as parcelas ficam escritas em vez de ficarem na memória. A numeração romana
não tem posições nem zero: CCXXXIV é uma soma de símbolos
(C + C + X + X + X + IV). Não há um algoritmo "algarismo a algarismo", e o
caminho prático é converter para decimal, que é uma tarefa nova.
**O problema é o mesmo; a representação muda a tarefa.**

#### (c) Parede ou ecrãs?

| Elemento | Onde | Porquê |
|:----------------|:--------------|:-------------------------------------|
| **(1)** Estado de alerta dos troços | **Parede** | É a situação partilhada: a sala toda tem de a perceber num relance (regra 4) |
| **(2)** Rascunho de um aviso público | **Ecrã privado** | É trabalho de um operador. Na parede podia ser lido como já emitido |
| **(3)** Manobra à espera de autorização | **Ecrã privado**, com um **indicador na parede** | Os detalhes são do operador que a pediu, mas a sala deve saber que há uma manobra pendente que vai mudar o rio |
| **(4)** Formulário para enviar uma equipa | **Ecrã privado** | Preencher é assunto de um operador. Quando a equipa fica "a caminho", o estado dela pode aparecer no mapa da parede |

## Aula 6 --- Fazer um walkthrough

### P.10 --- Fazer um walkthrough

#### (a) A máquina do Andante

Sequência correta: **1** escolher EN; **2** "Comprar um cartão novo" (o
visitante não tem cartão); **3** **Z2**† (Trindade e Campanhã estão na
mesma zona, e o título mínimo do Andante é o Z2); **4** "1"; **5** pagar e
retirar o cartão.

| Ecrã | Q1 | Q2 | Q3 | Q4 | Razão de cada "não" (e dos "sim" que contam) |
|:-:|:-:|:-:|:-:|:-:|:--------------------------------------------|
| 1 Idioma | sim | sim | sim | sim | O ecrã só pede isto; "EN" diz o que faz; o ecrã seguinte aparece em inglês |
| 2 O que quer? | sim | sim | **não** | sim | Ele quer **um bilhete**; as opções falam de **cartão**. Nada diz que, no Andante, o bilhete é um cartão. Acerta por eliminação ("carregar o meu cartão" não serve). **Sev. 2** |
| 3 Título | sim | sim | **não** | sim | "Título" e "Z2 ... Z8" são termos do tarifário. Nada liga "Trindade → Campanhã" a uma zona: não há mapa nem campo de destino. Pode escolher uma zona a mais (paga mais), a menos (viaja com um título inválido) ou desistir. **Sev. 4** |
| 4 Viagens | sim | sim | sim | sim | Quer uma viagem; o botão "1" diz isso; passa ao pagamento |
| 5 Pagar | sim | sim | sim | **não** | "Retire o seu cartão": é o bilhete ou o cartão do banco? Quem não ligou bilhete a cartão no ecrã 2 não sabe se acabou. **Sev. 2** |

**Que ecrã falha primeiro:** numa leitura estrita, o **ecrã 2, Q3**
(menor). A falha que importa é o **ecrã 3, Q3, severidade 4**: a zona é
um termo do mecanismo onde o visitante tem um termo da tarefa (o
destino), a mesma falha do "Setpoint (%)" do Tiago.

O Q4 do ecrã 3 também se pode marcar "não": a máquina avança, mas nada
confirma que Z2 serve para Campanhã. Avaliadores diferentes marcam coisas
diferentes no mesmo esboço; é por isso que a Fase 1 usa dois ou três.

#### (b) Que pergunta falha

| Caso | Falha | Porquê |
|:--|:-:|:----------------------------------------------|
| **(1)** Micro-ondas mudo | **Q4** | A ação foi feita e nada mostra progresso: a pessoa carrega outra vez ou abre a porta (o botão do elevador) |
| **(2)** Lugar escolhido depois de pagar | **Q1** | O utilizador não sabe que esse passo existe, por isso nunca o tenta (o START que precisa do travão) |
| **(3)** Modo férias em "Definições → Avançadas" | **Q2** | A ação existe, mas não está à vista (o "Rejeitar tudo" escondido) |
| **(4)** Botão "DF+" | **Q3** | O botão vê-se, mas a etiqueta é uma abreviatura do mecanismo: um operador novo não a liga a "abrir a descarga de fundo". Corrige-se com "Abrir descarga de fundo" |

#### (c) Corrigir o esboço do Tiago

| Problema | Mudança no esboço | Passa a "sim" |
|:--------------|:------------------------------------|:-:|
| Passo 2: comando que parece mostrador | Os valores editáveis em **caixas com contorno e fundo branco** (setas ou lápis), com outro aspeto dos valores só de leitura | Q2 |
| Passo 3: % onde se espera m³/s | O campo passa a **"Caudal pedido (m³/s)"**; o sistema calcula a abertura e mostra-a ao lado, só de leitura | Q3 |
| Passo 4: regra só na cabeça | Ao escrever o caudal, o painel mostra **Ponte da Barca ao lado** (nível, caudal, previsão com o valor novo), e a confirmação repete-o | Q1 |
| Passo 5: valor mostrado como feito | **"Pedido 120 / atual 92 m³/s"**, estado "em curso", tempo previsto (~3 min); *Apply* desativado até concluir | Q4 |

## Aula 6 --- Preparar e conduzir a Fase 1

### P.11 --- Preparar e conduzir a Fase 1

#### (a) A descarga de 280 para 420 m³/s

Acima de 300 m³/s é preciso o coordenador, e a manobra passa por pedida →
à espera de autorização → autorizada → em curso → concluída. Sequência
correta:

1. Selecionar Touvedo no mapa.
2. Encontrar os comandos das comportas.
3. Escrever 420 m³/s no campo do caudal.
4. Verificar Ponte da Barca.
5. **Pedir a manobra ao coordenador** (estado "à espera de autorização").
6. **Ver a autorização chegar** (estado "autorizada").
7. **Executar** (estado "em curso").
8. Acompanhar até "concluída".

Os passos 1 a 4 têm os mesmos problemas da aula. Passos que o esboço não
cobre:

| Passo | Q1 | Q2 | Q3 | Q4 | Razão |
|:-:|:-:|:-:|:-:|:-:|:----------------------------------------|
| 5 Pedir | **não** | **não** | **não** | **não** | Nada diz que 420 precisa do coordenador; não há botão para pedir; o único botão, *Apply*, sugere executar já; nada mostra o estado do pedido. **Sev. 4** (bloqueia, ou executa sem autorização) |
| 6 Ver a autorização | sim | **não** | --- | **não** | Ele sabe que tem de esperar, mas não há sítio onde a autorização apareça. **Sev. 4** |
| 7 Executar | sim | **não** | **não** | **não** | Sem estado "autorizada", não há ação distinta de "executar"; *Apply* outra vez é ambíguo. **Sev. 3** |
| 8 Acompanhar | sim | sim | sim | **não** | O mesmo problema do passo 5 da aula: não há "pedido / atual". **Sev. 3** |

**O ecrã que falta:** o das **manobras**, com o pedido ao coordenador e
o estado de cada manobra (pedida, à espera de autorização, autorizada, em
curso, concluída, cancelada). Foi **escrever a sequência correta** que o
revelou, antes de qualquer pergunta.

#### (b) "Isso explica-se na formação"

Quebra a regra **2 (não se defende o desenho)** e tenta apagar uma falha
(regra **3**). O **facilitador** lembra a regra e volta a dizer só o que
está no esboço. O **registador** escreve a falha na mesma: passo 3, Q3,
severidade 4. A persona está na primeira semana. Se o passo precisa de
formação para se acertar, o esboço não o explica, e a resposta é "não".

#### (c) Quantos problemas encontram três avaliadores

Um avaliador **falha** um problema com probabilidade $1 - \tfrac13 =
\tfrac23$. Com independência, os três falham-no com probabilidade

$$\left(\tfrac23\right)^3 = \tfrac{8}{27} \approx 0{,}30,$$

por isso **pelo menos um encontra-o** com probabilidade
$1 - \tfrac{8}{27} = \tfrac{19}{27} \approx 70\,\%$. Com dois:
$1 - \left(\tfrac23\right)^2 = \tfrac59 \approx 56\,\%$. Passa-se de
cerca de 33 % para 56--70 %. Na prática fica abaixo disto, porque os
avaliadores tendem a encontrar os mesmos problemas fáceis (não são
independentes), e há falsos alarmes para filtrar.
