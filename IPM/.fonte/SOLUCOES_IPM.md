---
title: "IPM --- Soluções dos exercícios \"Pratica agora\""
subtitle: "Exercícios de desenho não têm uma resposta única: isto é uma resposta-modelo para comparares com a tua, não um gabarito. Tenta primeiro sozinho."
---

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
