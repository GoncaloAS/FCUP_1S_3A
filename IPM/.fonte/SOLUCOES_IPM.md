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
