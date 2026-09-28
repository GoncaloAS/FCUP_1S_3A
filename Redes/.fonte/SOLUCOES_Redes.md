---
title: "Redes de Comunicação --- Soluções dos exercícios \"Pratica agora\""
subtitle: "Ficha 1 (Praticas/Semana_1/exercicios_redes.pdf), Ficha 2 (Praticas/Semana_2/ficha_2.pdf, exercícios F2.x) e exercícios inventados para o Capítulo 2 (C2.x). Tenta primeiro sozinho; abre uma alínea só depois de a teres feito. Convenções: 1 MB = 10⁶ bytes, 1 Mbps = 10⁶ bit/s, 1 byte = 8 bits."
---

## Comutação de pacotes --- multiplexagem estatística

### F2.2 --- Multiplexagem estatística (Ficha 2)

Ligação de 1 Mbps; cada utilizador transmite a 100 kbps durante 10% do
tempo. Com 35 utilizadores, $X$ = número dos que transmitem ao mesmo
tempo segue $X \sim \text{Bin}(35;\ 0{,}1)$.

#### (c) Probabilidade de exatamente $k$ a transmitir; valor para $k = 3$

Cada utilizador transmite com probabilidade $p = 0{,}1$, independentemente
dos outros:
$$P(X = k) = \binom{35}{k}\, 0{,}1^{k}\, 0{,}9^{35-k}$$

- $\binom{35}{k}$: de quantas maneiras se escolhem **quais** $k$ dos 35
  estão a transmitir;
- $0{,}1^k$: esses $k$ estão todos a transmitir;
- $0{,}9^{35-k}$: os outros $35-k$ estão todos calados.

Para $k = 3$:

- $\binom{35}{3} = \dfrac{35 \times 34 \times 33}{3 \times 2 \times 1} = 6545$;
- $0{,}1^3 = 0{,}001$;
- $0{,}9^{32} \approx 0{,}03434$.

$$P(X = 3) = 6545 \times 0{,}001 \times 0{,}03434 \approx \mathbf{0{,}225}$$

(É o valor mais provável: em média estão $35 \times 0{,}1 = 3{,}5$ a
transmitir.)

#### (d) $P(X \geq 11)$ com `BINOM.DIST()`

"11 ou mais" é o complementar de "10 ou menos", e o `BINOM.DIST` com o
último argumento `VERDADEIRO` dá a probabilidade acumulada, $P(X \leq k)$:

$$P(X \geq 11) = 1 - P(X \leq 10) = 1 - \texttt{BINOM.DIST(10; 35; 0,1; VERDADEIRO)}$$

$$= 1 - 0{,}999576 \approx \mathbf{0{,}000424}$$

É o 0,0004 da nota do resumo (valor confirmado em Python com
`scipy.stats.binom`). Na versão portuguesa do Excel a função pode
aparecer como `DISTR.BINOM`. O erro a evitar é calcular
`1 - BINOM.DIST(11; ...)`, que dá $P(X \geq 12)$.

## Núcleo da rede --- hierarquia de ISPs

### Ex. 1 --- Encaminhamento em redes muito grandes

#### Resposta

**Não.** O posto dos Aliados não conhece a rota até à Downing Street.
Conhece só o **próximo passo** na hierarquia: "cartas para o Reino Unido
vão para o centro de triagem internacional". Lá conhecem o país seguinte,
e em Londres conhecem a rua.

**Técnica: endereçamento e encaminhamento hierárquicos.** O endereço tem
níveis (país → cidade → rua, ou na Internet prefixo de rede → sub-rede →
máquina). Cada nó guarda uma entrada por **prefixo** e não uma por
destino:

- para destinos "dentro" do seu nível conhece a rota em detalhe;
- para tudo o resto tem uma entrada agregada, ou uma rota por omissão
  "manda para cima".

É o que a Internet faz com a hierarquia de ISPs: um ISP de acesso não
conhece todas as redes do mundo, entrega ao ISP regional/tier-1 acima.

**Custo:**

1. **Rotas que não são as mais curtas.** O tráfego sobe e desce na
   hierarquia mesmo quando havia um atalho direto. Duas redes vizinhas de
   ISPs diferentes podem comunicar através de um ponto de troca longe
   das duas.
2. **Os endereços têm de respeitar a topologia.** Uma máquina que muda de
   sítio tem de mudar de endereço, tal como uma morada muda quando se
   muda de casa.
3. Mais processamento em cada nó, que tem de procurar o **prefixo mais
   longo** que coincide com o destino em vez de consultar uma tabela
   direta.

O ganho é que as tabelas ficam **pequenas** e as alterações locais não se
propagam à rede inteira. Sem isto a Internet não escalava.

## Atrasos --- as quatro fontes de atraso

### Ex. 6 --- Experiências com atrasos (demonstração interativa)

A comparação decisiva é entre
$d_{trans} = L/R$ (tempo a pôr o pacote na linha) e
$d_{prop} = d/v$ (tempo que um bit demora a atravessar a ligação).

#### (a) O emissor acaba de transmitir **antes** de o primeiro bit chegar

É preciso $d_{trans} < d_{prop}$: pacote pequeno, ligação rápida e longa.
Por exemplo, com $v = 2\times10^8$ m/s:

- $L = 100$ bytes $= 800$ bits, $R = 10$ Mbps, então
  $d_{trans} = 800 / 10^7 = 80\ \mu s$
- comprimento $1000$ km, então
  $d_{prop} = 10^6 / (2\times10^8) = 5$ ms

Com $80\ \mu s < 5$ ms, o pacote inteiro já está "dentro do cabo" muito
antes de o primeiro bit chegar ao recetor.

#### (b) O primeiro bit chega **antes** de o emissor acabar de transmitir

É preciso $d_{trans} > d_{prop}$: pacote grande, ligação lenta e curta.

- $L = 1$ KB $= 8000$ bits, $R = 1$ Mbps, então
  $d_{trans} = 8000/10^6 = 8$ ms
- comprimento $10$ km, então $d_{prop} = 10^4/(2\times10^8) = 50\ \mu s$

Com $50\ \mu s < 8$ ms, os primeiros bits chegam ao recetor enquanto o
emissor ainda está a transmitir o resto.

(Se a demonstração só deixar escolher outros valores, qualquer combinação
com a desigualdade certa serve.)

### Ex. 7 --- O repórter "de compreensão lenta"

#### Resposta

Não é lentidão de raciocínio: é **atraso de propagação**. As ligações de
reportagem de longe usam muitas vezes **satélites geoestacionários**, a
cerca de **36 000 km** de altitude.

- A pergunta do pivô **sobe e desce**: cerca de $2 \times 36\,000$ km
  $= 72\,000$ km. À velocidade da luz,
  $d_{prop} \approx 7{,}2\times10^7 / 3\times10^8 = 0{,}24$ s.
- A resposta do repórter faz o mesmo caminho de volta, mais $0{,}24$ s.

Entre o pivô acabar a pergunta e ouvir o início da resposta passa **cerca
de meio segundo**, mesmo que o repórter responda instantaneamente.
Juntam-se ainda os atrasos de processamento e codificação do vídeo nos
equipamentos de emissão. É por isso que se vê a pausa. Das quatro
componentes do atraso, é a de **propagação** que domina aqui. A de
transmissão é desprezável, porque o débito é alto.

## Atrasos --- vários pacotes e ligações em série

### Ex. 3 --- O vídeo da Alice, em pedaços

$L = 700$ MB $= 5{,}6 \times 10^9$ bits; 2 routers, portanto **3
ligações**, todas a $R = 100$ Mbps. Ignoram-se propagação,
processamento e filas, porque o enunciado não os dá.

#### (a) Ficheiro inteiro, *store-and-forward*

Cada nó tem de receber o ficheiro todo antes de o reenviar. O tempo de
transmissão numa ligação é
$$d_{trans} = \frac{L}{R} = \frac{5{,}6\times10^9}{10^8} = 56\text{ s}$$

Há três ligações em série e cada uma só começa quando a anterior acaba:
$$3 \times 56 = \mathbf{168\text{ s}}$$

#### (b) Em pedaços de 1000 bytes

- Número de pedaços: $N = 700\times10^6 / 1000 = 700\,000$.
- Transmissão de um pedaço: $8000 / 10^8 = 80\ \mu s$.

Com pedaços as ligações trabalham **em paralelo** (*pipelining*). Enquanto
o router 1 envia o pedaço 1, a Alice já envia o pedaço 2. O último pedaço
sai da Alice ao fim de $N$ transmissões e ainda tem de atravessar as
outras 2 ligações:
$$T = (N + 3 - 1)\times 80\ \mu s = 700\,002 \times 80\ \mu s \approx \mathbf{56{,}0002\text{ s}}$$

**Poupança:** $168 - 56{,}0002 \approx \mathbf{112\text{ s}}$ (fica cerca
de 3 vezes mais rápido).

Intuição: com pedaços pequenos o tempo total é praticamente o de
**uma** ligação ($L/R$). As outras duas só somam o tempo de um pedaço
cada.

#### (c) Com um "envelope" de 20 bytes por pedaço

**Sem pedaços (a):** só há um envelope, e o bloco fica com
$5{,}6\times10^9 + 160$ bits:
$$3 \times \frac{5{,}6\times10^9 + 160}{10^8} \approx \mathbf{168{,}000005\text{ s}}$$
Na prática não muda nada.

**Com pedaços (b):** cada pedaço passa a ter $1020$ bytes $= 8160$ bits,
e demora $81{,}6\ \mu s$ a transmitir:
$$T = 700\,002 \times 81{,}6\ \mu s \approx \mathbf{57{,}12\text{ s}}$$

**Poupança:** $168 - 57{,}12 \approx \mathbf{110{,}9\text{ s}}$.

**Comparação com as soluções oficiais** (`solucoes_ficha_1.pdf`): a
resposta oficial da 3(c) é "aprox. 1,12 s". É o **tempo a mais** que os
envelopes custam face à alínea (b): $57{,}12 - 56{,}00 = 1{,}12$ s. É o
mesmo resultado visto de outra forma.

Os envelopes custam cerca de 2% a mais ($20/1000$), mas o *pipelining*
continua a compensar de longe. Se os pedaços fossem **muito** pequenos
(por exemplo, 20 bytes de dados para 20 de envelope), o custo dos
cabeçalhos passava a dominar. Há um tamanho de pedaço ótimo.

### Ex. 4 --- *Store and forward* LAN + WAN

$L = 1250$ bytes $= 10\,000$ bits; $v = 2\times10^8$ m/s.
LAN: 4 km, 10 Mb/s. WAN: 80 km, 1 Gb/s. T1 → LAN → R → WAN → T2.

#### (a) Atrasos de transmissão e de propagação

| | $d_{trans} = L/R$ | $d_{prop} = d/v$ |
|:--|:--|:--|
| LAN | $10^4 / 10^7 = \mathbf{1\text{ ms}}$ | $4000 / (2\times10^8) = \mathbf{20\ \mu s}$ |
| WAN | $10^4 / 10^9 = \mathbf{10\ \mu s}$ | $80\,000 / (2\times10^8) = \mathbf{400\ \mu s}$ |

#### (b) Um pacote de T1 a T2

O router tem de receber o pacote todo antes de o reenviar, por isso
somam-se as quatro parcelas:
$$1\text{ ms} + 20\ \mu s + 10\ \mu s + 400\ \mu s = \mathbf{1{,}43\text{ ms}}$$

#### (c) Dez pacotes de T1 a T2

A **LAN é o gargalo**: 1 ms por pacote contra 10 µs na WAN.

Diagrama temporal (instantes em µs, quando cada pacote **acaba** de
chegar):

| pacote | sai de T1 | chega a R | sai de R | chega a T2 |
|:-:|:-:|:-:|:-:|:-:|
| 1 | 1000 | 1020 | 1030 | 1430 |
| 2 | 2000 | 2020 | 2030 | 2430 |
| ... | ... | ... | ... | ... |
| 10 | 10 000 | 10 020 | 10 030 | **10 430** |

O router despacha cada pacote em 10 µs, muito antes de chegar o seguinte
(1 ms depois). **Não há fila em R.** O último pacote só sai de T1 aos
$10 \times 1$ ms, e depois precisa das mesmas 430 µs do pacote 1:
$$10 \times 1\text{ ms} + 20 + 10 + 400\ \mu s = \mathbf{10{,}43\text{ ms}}$$

#### (d) Repetir com LAN = 1 Gb/s e WAN = 10 Mb/s

Agora $d_{trans}$ na LAN é **10 µs** e na WAN é **1 ms**. As propagações
não mudam: 20 µs e 400 µs.

- **1 pacote:** $10 + 20 + 1000 + 400\ \mu s = 1{,}43$ ms (igual).
- **10 pacotes:** os pacotes chegam a R de 10 em 10 µs (o primeiro aos
  30 µs), mas a WAN só consegue despachar um por milissegundo. **Forma-se
  fila em R.**

| pacote | chega a R | começa a sair de R | acaba de sair | chega a T2 |
|:-:|:-:|:-:|:-:|:-:|
| 1 | 30 | 30 | 1030 | 1430 |
| 2 | 40 | 1030 (esperou) | 2030 | 2430 |
| ... | ... | ... | ... | ... |
| 10 | 120 | 9030 | 10 030 | **10 430** |

$$30\ \mu s + 10 \times 1\text{ ms} + 400\ \mu s = \mathbf{10{,}43\text{ ms}}$$

O tempo total é **o mesmo** da (c). O que manda é a ligação mais lenta,
esteja à entrada ou à saída, e ela tem de transmitir os 10 pacotes. O que
muda é **onde** os pacotes esperam: na (c) esperam em T1, antes de
entrar na LAN; na (d) acumulam-se na **fila do router**. Se a fila de R
fosse pequena, na (d) podia haver **perdas**.

## Atrasos --- filas de espera, ping e traceroute, perdas

### F2.3 --- Espere, mas não desespere (Ficha 2)

A máquina demora 15 s por café.

#### (a) 10 pessoas chegam ao mesmo tempo: espera média, mínima e máxima

A 1.ª pessoa é servida logo; a 2.ª espera que a 1.ª acabe (15 s); a
3.ª espera 30 s; ...; a 10.ª espera $9 \times 15 = 135$ s. As esperas
são $0, 15, 30, \dots, 135$ s.

$$\text{média} = \frac{15 \times (0+1+\dots+9)}{10} = \frac{15 \times 45}{10} = \mathbf{67{,}5\text{ s}}$$

**Mínimo: 0 s** (a primeira). **Máximo: 135 s** (a última).

(Se se contar até ter o café na mão, soma-se 15 s a cada uma: média
82,5 s, mínimo 15 s, máximo 150 s.) É exatamente o atraso de fila de uma
rajada de pacotes que chega a uma ligação vazia: o $n$-ésimo espera
$(n-1)\,L/R$.

#### (b) Há algum tempo médio entre chegadas que garanta que ninguém espera?

**Não.** Se as chegadas são **independentes** (aleatórias), por maior que
seja o intervalo **médio** entre chegadas, há sempre uma probabilidade
maior que zero de duas pessoas chegarem com menos de 15 s de diferença, e
a segunda espera. Só com chegadas **determinísticas** (por exemplo,
exatamente uma pessoa a cada 20 s) se garante que ninguém espera. Com
intervalos médios grandes a espera torna-se **rara**, mas nunca
impossível.

#### (c) Com uma chegada a cada 15 s em média, porque é que a espera cresce sem limite?

Em média, a máquina tem exatamente o trabalho que consegue fazer
($La/R = 1$). Mas as chegadas são aleatórias:

- às vezes passa um bocado **sem ninguém**: a máquina fica parada, e esse
  tempo de serviço **perde-se para sempre** (não se pode "guardar" para
  depois);
- outras vezes chegam **várias pessoas seguidas**: forma-se fila.

Para desfazer uma fila, a máquina teria de servir **mais depressa** do que
as pessoas chegam durante algum tempo. Com $La/R = 1$ **não há folga
nenhuma** para isso: em média chega tanto quanto sai. A fila comporta-se
como um passeio aleatório sem tendência para voltar a zero, e as suas
oscilações vão ficando cada vez maiores com o tempo. Por isso o tempo de
espera médio cresce sem limite. É a "explosão do atraso" do resumo: o
problema não é a média, é a **variabilidade** com zero margem.

### F2.7 --- Ferramentas: ping e traceroute (Ficha 2)

#### (a) O `ping`: para que serve, como funciona, que informação dá

Serve para testar se uma máquina **está alcançável** e medir o **atraso
de ida e volta** até ela.

Como funciona (nota adicional: o ICMP só vem na camada de rede): envia
pacotes ICMP ***Echo Request*** ao destino; o destino responde a cada um
com um ***Echo Reply***. Para cada resposta, o `ping` mede o tempo entre
o envio e a chegada.

Informação que dá: se a máquina **responde**; o **RTT** de cada pacote e
o mínimo/médio/máximo (e a variação); a **percentagem de pacotes
perdidos**. Não diz **por onde** passam os pacotes nem **onde** está o
atraso.

#### (b) O `traceroute`: para que serve e como funciona

Serve para descobrir o **caminho** (a sequência de *routers*) até um
destino e o **atraso até cada salto** (é o que o resumo mostra no exemplo
DCC $\to$ CMU).

Como funciona (nota adicional: o mecanismo não vem nos slides). Cada
pacote IP tem um campo **TTL** (*time to live*); cada *router* tira-lhe 1,
e o *router* onde ele chega a 0 descarta o pacote e devolve à origem uma
mensagem ICMP ***Time Exceeded***, com o seu próprio endereço. O
`traceroute`:

1. envia pacotes (por omissão 3) com **TTL = 1**: o 1.º *router* responde.
   Mede-se o RTT até ele;
2. envia com **TTL = 2**: responde o 2.º *router*;
3. e assim por diante, até o **destino** responder. Com sondas UDP para
   uma porta onde não há ninguém, o destino responde com ICMP *Port
   Unreachable*, e é assim que o `traceroute` sabe que chegou.

É por isso que só o *router* número $i$ responde à sonda com TTL $= i$.

#### (c) `traceroute -U -n -N 1 www.cmu.edu` e a geografia dos saltos

Resposta-modelo: os valores dependem de onde e quando corres o comando.

**As opções** (versão Linux do `traceroute`): `-U` usa sondas UDP; `-n`
não traduz os IPs para nomes (mais rápido, e não confunde a
geolocalização); `-N 1` envia uma sonda de cada vez (em vez de várias em
paralelo). No macOS as opções são outras; `traceroute -n www.cmu.edu` dá
o mesmo tipo de resultado.

**Como relacionar distância e RTT.** O sinal anda a cerca de
$2\times10^8$ m/s na fibra, por isso **cada 1000 km de distância (em linha
reta) somam pelo menos 10 ms ao RTT** (ida e volta: 2000 km a
$2\times10^8$ m/s dão 10 ms). Do Porto a Pittsburgh (CMU) são cerca de
5800 km em linha reta, o que dá um RTT mínimo de cerca de **58 ms**. O
valor medido será maior (a fibra não vai em linha reta, e há filas e
processamento).

**O que deves ver:**

- saltos dentro de Portugal e da Europa com RTTs de poucos ms, que
  crescem devagar;
- um **salto grande** (várias dezenas de ms) num único salto: é a
  travessia do **Atlântico** (fibra submarina). Os dois *routers* estão em
  continentes diferentes;
- depois, saltos dentro dos EUA com RTTs perto do valor final;
- às vezes um salto tem RTT **maior** do que o seguinte: o *router* dá
  pouca prioridade a responder a sondas; não quer dizer que o caminho
  "ande para trás".

Se um salto tem RTT **menor** do que o mínimo que a distância permite
(por exemplo, um IP que a geolocalização diz estar nos EUA com 5 ms a
partir do Porto), a **geolocalização está errada** (é comum: o IP está
registado na sede da empresa, não onde está o *router*).

### F2.4 --- Os dois generais (Ficha 2)

#### Resposta

O especialista está **certo**: não há nenhum protocolo que dê essa
garantia. Prova por contradição.

Queremos um protocolo em que, **no fim**, os dois generais atacam à mesma
hora **e cada um tem a certeza** de que o outro também ataca, mesmo que
qualquer mensageiro possa ser apanhado.

1. **Suponhamos que existe** um protocolo assim. Entre todos os que
   existem, escolhe-se um com o **menor número de mensagens**, $n$.
2. $n \geq 1$: sem nenhuma mensagem, o general que escolhe a hora não a
   consegue comunicar ao outro.
3. Olha-se para a **última** mensagem, a $n$-ésima. Quem a envia **não sabe
   se ela chegou** (para saber, precisava de outra mensagem de volta, que
   já não há). Por isso a sua decisão de atacar não pode depender de ela
   chegar: vai atacar quer chegue quer não.
4. O protocolo tem de funcionar **mesmo que a última mensagem se perca**
   (os mensageiros podem ser sempre apanhados). Então o recetor também tem
   de decidir atacar à mesma hora **sem** ela.
5. Logo, a última mensagem **não serve para nada**: tirando-a, os dois
   decidem exatamente o mesmo. Isso dá um protocolo correto com $n-1$
   mensagens, o que contradiz a escolha de $n$ como mínimo.

A contradição mostra que o protocolo não existe.

**Intuição:** o general A envia a hora; mas A só ataca se souber que B a
recebeu, por isso B tem de confirmar; mas B só ataca se souber que a
confirmação chegou, por isso A tem de confirmar a confirmação; e assim
por diante, sem fim.

**Ligação às redes:** num canal de **melhor esforço** nunca se tem a
certeza **absoluta** de um acordo. Os protocolos reais (como o
*handshake* do TCP) contentam-se com uma certeza **suficiente**: repetem
as mensagens perdidas (retransmissões com temporizadores) e aceitam um
risco muito pequeno.

### F2.6 --- Perdidos na fila (Ficha 2)

Resposta-modelo: o resultado exato depende da demonstração e de cada
execução.

#### (a) Com emissão máxima e transmissão mínima, quando é a primeira perda?

Com a taxa de emissão (chegadas, $\lambda$ pacotes/s) **maior** do que a
de transmissão ($\mu$ pacotes/s), a intensidade de tráfego é maior do que
1: a fila **cresce**, em média, $\lambda - \mu$ pacotes por segundo. A
primeira perda acontece quando a fila **enche**. Se a fila tiver
capacidade para $B$ pacotes, isso acontece, em média, ao fim de cerca de
$$t \approx \frac{B}{\lambda - \mu}$$
Por exemplo, com $\lambda = 1000$ pacotes/s, $\mu = 350$ pacotes/s e
espaço para $B = 10$ pacotes (valores ilustrativos): $10/650 \approx
15$ ms. Na demonstração, lê o tempo da primeira perda e compara com esta
estimativa (usando o tamanho da fila que ela mostra).

#### (b) Repetindo, o valor é o mesmo?

**Não.** As chegadas são aleatórias (exponenciais): em cada execução a
sequência de chegadas é diferente, umas vezes com mais rajadas no início,
outras com menos. A fila enche mais cedo ou mais tarde, e o tempo da
primeira perda **varia** à volta do valor médio de (a). A transmissão é
determinística; a variabilidade vem só das chegadas. É a mesma razão
pela qual, na F2.3, não se consegue garantir que ninguém espera.

## Atrasos --- débito e produto largura de banda-atraso

### Ex. 2 --- O camião com discos rígidos

#### (a) Capacidade do "canal" em bits/s

Dados transportados por viagem:
$$100\,000 \times 1\text{ TB} = 10^5 \times 8\times10^{12}\text{ bits} = 8\times10^{17}\text{ bits}$$

O camião só pode levar outra carga depois de voltar, por isso cada carga
"ocupa" o canal durante uma ida e volta, 4 dias:
$$4 \times 86\,400 = 345\,600\text{ s}$$

$$\text{débito} = \frac{8\times10^{17}}{345\,600} \approx \mathbf{2{,}3\times10^{12}\text{ bit/s} \approx 2{,}3\text{ Tbps}}$$

(Se se contar só a ida, 2 dias, dá cerca de 4,6 Tbps. A resposta
esperada costuma ser a da ida e volta, mas justifica a que escolheres.)

É **mais** do que uma boa fibra ótica.

#### (b) Inconvenientes face a uma fibra com a mesma capacidade

O problema é o **atraso**, não o débito:

- o **primeiro bit** só chega ao fim de cerca de **2 dias** (a viagem de
  ida). Numa fibra Porto--Amesterdão (cerca de 1500 km) chega em cerca de
  **7,5 ms**;
- os dados chegam **todos de uma vez**, em rajadas de 8×10¹⁷ bits de 4
  em 4 dias, e não como um fluxo contínuo;
- qualquer interação fica impossível: um pedido e a resposta levam dias.
  Serve para cópias de segurança em massa, não para uma chamada de vídeo;
- se um disco se estragar, a "retransmissão" leva mais 4 dias.

Débito alto não quer dizer atraso baixo: são duas métricas
independentes.

### Ex. 5 --- Atrasos & companhia

$d = 10\,000$ km $= 10^7$ m; $v = 2{,}5\times10^8$ m/s; $L = 400\,000$
bits.

#### (a) $d_{trans}$ com $R = 1$ Mbps

$$d_{trans} = \frac{L}{R} = \frac{4\times10^5}{10^6} = \mathbf{0{,}4\text{ s}}$$

#### (b) $d_{prop}$

$$d_{prop} = \frac{d}{v} = \frac{10^7}{2{,}5\times10^8} = \mathbf{0{,}04\text{ s} = 40\text{ ms}}$$

#### (c) Produto largura de banda--atraso $R \cdot d_{prop}$

$$R\cdot d_{prop} = 10^6 \times 0{,}04 = \mathbf{40\,000\text{ bits}}$$

#### (d) Número máximo de bits na ligação num dado instante

É o produto largura de banda--atraso, **40 000 bits**. Ao fim de 40 ms o
primeiro bit chega ao destino. Nesse instante já foram emitidos
$R \times 40\text{ ms} = 40\,000$ bits, e a partir daí sai um por uma
ponta e entra outro pela outra.

O ficheiro (400 000 bits) é maior do que isto, por isso a ligação chega a
estar "cheia". Em geral o máximo é $\min(L,\ R\cdot d_{prop})$.

#### (e) Comprimento de um bit na ligação

Um bit ocupa o tempo $1/R$, e nesse tempo o sinal anda $v/R$:
$$\frac{v}{R} = \frac{2{,}5\times10^8}{10^6} = \mathbf{250\text{ m}}$$

Confirmação: 40 000 bits em 10 000 km dão $10^7/4\times10^4 = 250$ m por
bit $\checkmark$.

#### (f) Repetir com $R = 1$ Gbps

| | 1 Mbps | **1 Gbps** |
|:--|:-:|:-:|
| $d_{trans} = L/R$ | 0,4 s | $4\times10^5/10^9 = $ **0,4 ms** |
| $d_{prop}$ | 40 ms | **40 ms** (não depende de $R$) |
| $R\cdot d_{prop}$ | 40 000 bits | $10^9\times0{,}04 = $ **4×10⁷ bits** |
| máx. bits na ligação | 40 000 | $\min(4\times10^5,\ 4\times10^7) = $ **400 000** |
| comprimento de um bit | 250 m | $2{,}5\times10^8/10^9 = $ **0,25 m** |

**Atenção à solução oficial** (`solucoes_ficha_1.pdf`): para a (f) dá
"$R \times d_{prop} = 4\times10^7$ b (igual ao nº de bits na ligação)",
ou seja, interpreta a (d) como a **capacidade do tubo** (quantos bits lá
cabem se o emissor estiver sempre a transmitir). Com **só este ficheiro**
de 400 000 bits nunca estão mais do que 400 000 na ligação. As duas
respostas medem coisas diferentes; num teste, diz qual estás a calcular.
Com 1 Mbps as duas interpretações dão o mesmo, 40 000 bits.

Com 1 Gbps o ficheiro inteiro cabe no "tubo". O emissor acaba de
transmitir (0,4 ms) muito antes de o primeiro bit chegar (40 ms). O
máximo na ligação passa a ser o próprio ficheiro, 400 000 bits, e não o
produto, que é 100 vezes maior.

#### (g) Interpretação física do produto largura de banda--atraso

É a **"capacidade do tubo"**: quantos bits cabem ao mesmo tempo dentro da
ligação, a caminho do destino. Também é quantos bits o emissor tem de pôr
na linha até o primeiro chegar ao outro lado.

Consequência prática, que vai reaparecer no TCP: para usar toda a
capacidade de uma ligação, o emissor tem de ter **pelo menos** esse
número de bits "em voo" sem esperar confirmação. Se enviar um pacote e
ficar à espera da resposta, a ligação fica quase toda vazia. Com 1 Gbps
e 10 000 km, o tubo leva 40 Mbit, cerca de 5 MB.

## Débito --- estimar a capacidade de uma ligação

### F2.5 --- Estimada capacidade: o par de pacotes (Ficha 2)

Dois pacotes do mesmo tamanho $L$, enviados um logo a seguir ao outro. O
caminho tem uma ligação mais lenta, de capacidade $C$ (o
estrangulamento).

#### (a) Diagrama temporal

![Par de pacotes: o espaçamento criado na ligação lenta mantém-se até ao recetor](figuras/sol_par_pacotes.svg){width=100%}

- O emissor transmite P1 e P2 seguidos, cada um em $L/R_1$ (ligação
  rápida).
- No *router*, a ligação de saída é a lenta: P1 demora $L/C$ a ser
  transmitido, e P2, que chegou entretanto, **espera na fila** que P1
  acabe. P2 só acaba de sair $L/C$ depois de P1.
- No recetor, os dois chegam separados por $\Delta = L/C$. A máquina de
  destino responde a cada um (respostas pequenas), e as respostas voltam
  ao emissor **com o mesmo espaçamento**.

#### (b) Fórmula da capacidade

Na ligação mais lenta, o fim de P2 sai exatamente $L/C$ depois do fim de
P1 (P2 esperou que P1 acabasse de ser transmitido). As ligações mais
rápidas a seguir não reduzem esse espaçamento: cada pacote atravessa-as
depressa e os dois continuam separados por $L/C$. Se as respostas forem
pequenas e voltarem sem mais atrasos, o tempo medido entre elas é
$\Delta = L/C$, logo

$$\boxed{C = \frac{L}{\Delta}}$$

Exemplo: $L = 1500$ bytes $= 12\,000$ bits e $\Delta = 1{,}2$ ms dão
$C = 12\,000 / 0{,}0012 = 10^7$ b/s $= 10$ Mbps.

Repara que a fórmula dá a capacidade da ligação **mais lenta** do
caminho (o estrangulamento), não a de uma ligação qualquer.

#### (c) O que pode estragar a estimativa, e como atenuar

**Fatores:**

- **Tráfego cruzado**: pacotes de outros fluxos que entram na fila
  **entre** P1 e P2 afastam-nos (Δ maior: **subestima** $C$); se P1
  esperar numa fila **depois** do estrangulamento e P2 o apanhar, ficam
  mais juntos (Δ menor: **sobrestima** $C$).
- **O caminho de volta**: se as respostas forem grandes ou apanharem uma
  ligação lenta ou filas na volta, o espaçamento muda.
- **Processamento no destino**: o tempo que a máquina demora a responder
  a cada pacote pode variar.
- **Resolução do relógio**: com ligações rápidas, $\Delta$ é muito
  pequeno (microssegundos) e o erro da medição pesa muito.
- Os pacotes podem não sair mesmo "colados" do emissor.

**Como atenuar:**

- **repetir muitas vezes** e usar o valor mais frequente (a **moda**) ou a
  mediana, não a média (os valores estragados pelo tráfego cruzado
  espalham-se para os dois lados);
- usar pacotes **grandes** ($\Delta$ maior, menos erro relativo do
  relógio) e **respostas pequenas**;
- medir em alturas de **pouco tráfego**;
- descartar medições claramente impossíveis.

## Camadas protocolares

### F2.1 --- Arquitetura em camadas: o Chico e a Teresa (Ficha 2)

#### Resposta

**Porque discorda a Teresa do método.** Um *router* é um dispositivo da
**camada de rede**: deve decidir só com o **cabeçalho de rede** (é o que o
resumo sublinha na secção de encapsulamento). Olhar para o **cabeçalho de
transporte** quebra a separação em camadas:

- o *router* passa a depender de detalhes de uma camada que não é a sua:
  que protocolo de transporte é, que portas usa cada aplicação. Se aparecer
  uma aplicação nova, ou o email passar a usar outra porta ou protocolo, é
  preciso mudar todos os *routers*;
- o cabeçalho de transporte pode **nem estar visível**: pode ir cifrado,
  ou num fragmento de um datagrama que não o contém;
- é trabalho extra em cada pacote, em todos os *routers*.

**Solução que agrada à Teresa.** A decisão sobre a prioridade é tomada
**na origem**, onde se sabe que o tráfego é email (a aplicação, ou o
sistema operativo por pedido dela), e é **marcada num campo do cabeçalho
de rede**. O *router* só lê esse campo, que é da sua camada. (Nota
adicional: o IP tem mesmo um campo para isto, o *Type of Service*, hoje
chamado DSCP.)

**Problemas desta solução:**

- **Confiança e abuso**: qualquer utilizador pode marcar **todos** os seus
  pacotes como prioritários. É preciso controlar quem pode marcar o quê
  (e, por exemplo, cobrar por isso).
- **Acordo entre redes**: a marcação só funciona se os ISPs pelo caminho
  a respeitarem; cada domínio pode ignorá-la ou reescrevê-la.
- **Não cria capacidade**: dar prioridade ao email só **passa as perdas**
  para as outras aplicações, que podem ficar sem serviço em
  congestionamentos longos.
- Os *routers* têm de implementar e configurar várias filas com
  prioridades.

## Aula 2 --- Web e HTTP

### C2.1 --- Tempo de resposta do HTTP (exercício inventado)

1 HTML + 5 objetos = **6 objetos**; RTT = 40 ms; $T = 10$ ms de
transmissão por objeto.

#### (a) HTTP não persistente, um objeto de cada vez

Cada objeto precisa da sua conexão TCP: 1 RTT para a conexão, 1 RTT para
o pedido e os primeiros bytes, e o tempo de transmissão:
$$2\,\text{RTT} + T = 2 \times 40 + 10 = 90\text{ ms por objeto}$$
São 6 objetos, um de cada vez:
$$6 \times 90 = \mathbf{540\text{ ms}}$$

#### (b) HTTP persistente sem *pipelining*

- 1 RTT para abrir a conexão (só uma vez): 40 ms.
- Cada um dos 6 objetos: pedido e resposta, 1 RTT + $T$ = 50 ms, um de
  cada vez (o próximo pedido só sai quando a resposta anterior chega).

$$40 + 6 \times 50 = 40 + 300 = \mathbf{340\text{ ms}}$$

#### (c) HTTP persistente com *pipelining*

- Conexão: 40 ms. HTML: 1 RTT + $T$ = 50 ms. Aos 90 ms o browser tem o
  HTML e conhece os 5 objetos.
- Envia **os 5 pedidos de uma vez**. A primeira resposta começa a chegar
  1 RTT depois, e as 5 respostas vêm seguidas, cada uma a demorar $T$:
  $40 + 5 \times 10 = 90$ ms.

$$90 + 90 = \mathbf{180\text{ ms}}$$

Resumo: 540 $\to$ 340 $\to$ 180 ms. Em RTTs: 12, 7 e 3 RTT, mais $6T$ =
60 ms de transmissão nos três casos (confirma: $12 \times 40 + 60 = 540$;
$7 \times 40 + 60 = 340$; $3 \times 40 + 60 = 180$).

### C2.2 --- Analisar uma sessão HTTP real (exercício inventado)

Captura `Teoricas/Aula_03_captura_http.cap`: browser 192.168.50.41,
servidor 10.0.0.251 (`www.dcc.fc.up.pt`), porta 80. Os valores abaixo
foram tirados da própria captura.

#### (a) Quantas conexões TCP, e quantas transportam pedidos?

**Três** conexões TCP, das portas **55956**, **55957** e **55958** do
cliente para a porta 80.

- **55956**: a principal, com **5 pedidos**: `/~rprior/` (o HTML),
  `rprior.css`, `img/portonight.jpg` e `/favicon.ico` (duas vezes).
- **55957**: **1 pedido**, `img/rprior.jpg`.
- **55958**: aberta (há o *handshake*), mas **nunca leva nenhum pedido**;
  é fechada ao fim de cerca de 1,9 s.

Só **duas** transportam pedidos. O browser abriu mais duas conexões **em
paralelo** quando encontrou as imagens (os slides dizem que os browsers
fazem isto), mas acabou por só precisar de uma delas.

#### (b) A conexão principal é persistente? Provas

**Sim.** Provas na captura:

- passam **5 pedidos** pela mesma conexão (55956): com HTTP não
  persistente seria uma conexão por objeto;
- o browser pede `Connection: keep-alive` e o servidor responde
  `Connection: Keep-Alive`;
- o cabeçalho `Keep-Alive` das respostas nessa conexão conta os pedidos
  que ainda aceita: `max=100`, `99`, `98`, `97`, `96`. Cada resposta
  gasta um. (Na conexão 55957 volta a `max=100`: é outra conexão.)

Repara também que cada pedido só sai **depois** de a resposta anterior
começar a chegar (o CSS é pedido aos 25,5 ms, depois de o HTML chegar aos
10,1 ms): é persistente **sem *pipelining***.

#### (c) Que códigos de estado aparecem?

- **200 OK**: para `/~rprior/`, `rprior.css`, `portonight.jpg` e
  `rprior.jpg`.
- **404 Not Found**: para `/favicon.ico` (as duas vezes). O browser pede
  sozinho o ícone do site, que não existe neste servidor.

Nota adicional: as respostas 200 dizem o tamanho com `Content-Length`
(por exemplo, 2144 bytes para o HTML e 86 267 para `portonight.jpg`). As
404 usam `Transfer-Encoding: chunked`: o corpo vai em pedaços, cada um
precedido do seu tamanho, e acaba num pedaço de tamanho 0. É outra forma
de o browser saber onde acaba a resposta sem saber o tamanho à partida.

#### (d) RTT a partir do *handshake* TCP

O cliente envia o primeiro pacote do *handshake* (SYN) no instante 0 e a
resposta do servidor (SYN-ACK) chega aos **0,24 ms**. O RTT é cerca de
**0,24 ms**.

Isso é muito pouco: à velocidade de $2\times10^8$ m/s, 0,24 ms de ida e
volta são no máximo 24 km de fibra para cada lado, e na prática menos
(há processamento). O cliente está na **mesma rede local** (ou muito
perto) do servidor. Os endereços confirmam: 192.168.x.x e 10.x.x.x são
endereços **privados**, de redes internas (aqui, dentro do DCC).

## Aula 2 --- FTP

### C2.3 --- Analisar uma sessão FTP real (exercício inventado)

Captura `Teoricas/Aula_03_captura_ftp.cap`: cliente 192.168.1.110,
servidor 193.137.24.17 (vsFTPd). Valores tirados da captura.

#### (a) Quantas conexões TCP, entre que portas, e quem abre cada uma?

**Duas:**

- **controlo**: da porta 50212 do cliente para a **porta 21** do
  servidor. Abre-a o **cliente** (o primeiro SYN vem dele), logo no
  início;
- **dados**: da **porta 20** do servidor para a porta **50219** do
  cliente. Abre-a o **servidor** (o SYN vem da porta 20), depois do
  comando `RETR`.

É o FTP em **modo ativo**: o controlo é *out of band*, numa conexão
separada dos dados.

#### (b) Utilizador e *password*; o que mostra sobre a segurança

```
S: 220 (vsFTPd 2.0.5)
C: USER anonymous
S: 331 Please specify the password.
C: PASS someone@the.inter.net
S: 230 Login successful.
```

Utilizador **`anonymous`**, *password* **`someone@the.inter.net`**. É um
FTP **anónimo** (servidor público de ficheiros, onde por tradição se usa
um email como *password*). Mas a lição é geral: o FTP envia utilizador e
*password* **em texto claro**. Qualquer pessoa que capture os pacotes
(como nesta captura) lê a *password*. Com uma conta verdadeira seria
grave; é o problema de "TCP e UDP não cifram" da secção de segurança.

#### (c) Descodificar o `PORT`

```
C: PORT 192,168,1,110,196,43
S: 200 PORT command successful. Consider using PASV.
C: RETR iperf-1.7.0-source.tar.gz
S: 150 Opening BINARY mode data connection for iperf-1.7.0-source.tar.gz (182773 bytes).
S: 226 File send OK.
```

- IP: os 4 primeiros números, **192.168.1.110** (o cliente).
- Porta: $196 \times 256 + 43 = 50176 + 43 = \mathbf{50219}$.

Bate certo: a conexão de dados que aparece a seguir vai da porta 20 do
servidor para a porta **50219** do cliente.

Um pormenor da captura: o primeiro SYN do servidor para a porta 50219
(aos 43,0 s) **não teve resposta**; o servidor repetiu-o 3 s depois
(46,0 s), e aí a conexão abriu. Por isso o `150` só chega aos 46,06 s. O
cliente tem um endereço **privado** (192.168.x.x), atrás de um *router*
com NAT, e no modo ativo é o servidor que tem de conseguir chegar ao
cliente, o que é frágil. É por isso que o servidor sugere "Consider using
PASV" (modo passivo, em que é o cliente que abre a conexão de dados).

Antes do `PORT`, o cliente mandou `SYST` (tipo de sistema), `CWD
/pub/Linux` (muda de diretório) e `TYPE I` (modo binário): isto é o
**estado** que o servidor FTP guarda (diretório corrente, modo), ao
contrário do HTTP.

#### (d) Tamanho do ficheiro e débito médio

- **Tamanho: 182 773 bytes** (diz o `150`, e é também a soma dos dados
  que passam na conexão de dados).
- Primeiro pacote com dados: aos **46,0736 s**; último: aos **46,2901 s**.
  Duração: $46{,}2901 - 46{,}0736 = 0{,}2165$ s.

$$\text{débito} = \frac{182\,773 \times 8\text{ bits}}{0{,}2165\text{ s}} = \frac{1\,462\,184}{0{,}2165} \approx \mathbf{6{,}75\text{ Mbit/s}}$$

## Aula 2 --- Correio eletrónico

### C2.4 --- E-mail (exercício inventado)

#### (a) Sessão SMTP para dois destinatários

Resposta-modelo (só o lado do cliente; o servidor responderia `220`,
`250`, `354`, `250`, `221` como no exemplo dos slides):

```
HELO exemplo.pt
MAIL FROM: <ana@exemplo.pt>
RCPT TO: <rui@exemplo.pt>
RCPT TO: <eva@outro.pt>
DATA
From: ana@exemplo.pt
To: rui@exemplo.pt, eva@outro.pt
Subject: Reunião

Olá aos dois. A reunião é amanhã às 10h.
Ana
.
QUIT
```

- **Um `RCPT TO` por destinatário**: é o "envelope", o que o servidor usa
  para entregar. O **cabeçalho** `To:` é outra coisa (parte da mensagem,
  para o leitor ver); os dois costumam coincidir, mas não têm de.
- Os cabeçalhos (`From:`, `To:`, `Subject:`) vão **dentro** do `DATA`, e
  uma **linha vazia** separa-os do corpo.
- A mensagem acaba numa linha **só com `.`**.
- Pormenor: "Reunião" e "Olá" têm acentos. Com a regra dos 7 bits, eles
  teriam de ser codificados (no corpo, com MIME; no assunto, com uma
  codificação própria para cabeçalhos), a não ser que o servidor aceite
  8 bits (`8BITMIME`, como na captura do resumo).

#### (b) POP3 "transfere e apaga" com dois aparelhos

Quando o **portátil** vai buscar o correio, transfere as mensagens e
**apaga-as do servidor**. Quando o **telemóvel** se liga depois, **já não
estão lá**: vê só as mensagens que chegaram entretanto. O correio fica
"partido" entre os dois aparelhos.

Resolve-se com **IMAP**: as mensagens **ficam no servidor**, e todos os
aparelhos veem as mesmas. Além disso o IMAP **guarda estado entre
sessões** (pastas, que mensagem está em que pasta), por isso organizar
o correio num aparelho aparece igual no outro. (O POP3 no modo "transfere
e deixa ficar" evita perder as mensagens, mas não guarda estado entre
sessões: pastas e organização não passam de um aparelho para o outro.)

## Aula 2 --- DNS

### C2.5 --- DNS (exercício inventado)

#### (a) Quantas mensagens DNS em cada caso?

Numeração do caso normal: 1 e 8 entre `khedo` e o servidor local; 2--3
com a raiz; 4--5 com o TLD `edu`; 6--7 com `ns.mit.edu`.

- **(i) *Caches* vazias**: todas, **8 mensagens**.
- **(ii) O servidor local já conhece o TLD `edu`**: não precisa de
  perguntar à raiz (sem 2 e 3). Ficam 1, 4, 5, 6, 7, 8: **6 mensagens**.
  É o caso mais comum, porque os TLD estão quase sempre em *cache* (por
  isso a raiz raramente é contactada).
- **(iii) O servidor local já tem o IP de `www.mit.edu`**: responde logo
  da *cache*. Só 1 e 8: **2 mensagens**.

Em todos os casos, a pergunta de `khedo` é **recursiva** (quer a resposta
final) e as do servidor local são **iterativas**.

#### (b) Registos de `ferramentas.pt`

Formato (nome, valor, tipo); o ttl fica à escolha do administrador.

**No servidor TLD `pt`** (inseridos pelo agente de registo), para que a
hierarquia saiba a quem perguntar:

- `(ferramentas.pt, dns1.ferramentas.pt, NS)`: o servidor com autoridade
  do domínio;
- `(dns1.ferramentas.pt, 192.0.2.53, A)`: o IP desse servidor (sem ele,
  saber o nome do servidor não chegava para lá chegar).

**No servidor com autoridade `dns1.ferramentas.pt`:**

- `(servidor1.ferramentas.pt, 192.0.2.10, A)`: a máquina do site;
- `(www.ferramentas.pt, servidor1.ferramentas.pt, CNAME)`: `www` é um
  **pseudónimo**, e o nome canónico é `servidor1`;
- `(ferramentas.pt, mail.ferramentas.pt, MX)`: o servidor de email do
  **domínio** (é para aqui que vai o correio para `...@ferramentas.pt`);
- `(mail.ferramentas.pt, 192.0.2.25, A)`: o IP do servidor de email;
- normalmente também os registos NS e A do próprio `dns1`, como no TLD.

Resolver `www.ferramentas.pt` dá o CNAME `servidor1.ferramentas.pt`, e
depois o registo A dá 192.0.2.10.

## Aula 2 --- Aplicações P2P

### C2.6 --- Tempo de distribuição (exercício inventado)

$F = 1$ Gbit $= 10^9$ bits; $u_s = 100$ Mbps $= 10^8$ b/s; $u = 5$ Mbps
$= 5\times10^6$ b/s; $d = 50$ Mbps $= 5\times10^7$ b/s.

Termos que não dependem de $N$:

- $F/u_s = 10^9 / 10^8 = 10$ s;
- $F/d_{\min} = 10^9 / (5\times10^7) = 20$ s.

Termos que dependem de $N$:

- cliente-servidor: $NF/u_s = N \times 10$ s;
- P2P: $\dfrac{NF}{u_s + Nu} = \dfrac{N \times 10^9}{10^8 + N \times 5\times10^6}$.

#### (a) $N = 10$

- $d_{CS} = \max\{10 \times 10,\ 20\} = \max\{100,\ 20\} = \mathbf{100\text{ s}}$:
  manda o *upload* do servidor.
- P2P: $\dfrac{10 \times 10^9}{10^8 + 5\times10^7} = \dfrac{10^{10}}{1{,}5\times10^8} \approx 66{,}7$ s.
  $d_{P2P} = \max\{10,\ 20,\ 66{,}7\} = \mathbf{66{,}7\text{ s}}$: manda o
  *upload* agregado.

#### (b) $N = 100$

- $d_{CS} = \max\{1000,\ 20\} = \mathbf{1000\text{ s}}$ (servidor).
- P2P: $\dfrac{10^{11}}{10^8 + 5\times10^8} = \dfrac{10^{11}}{6\times10^8} \approx 166{,}7$ s.
  $d_{P2P} = \mathbf{166{,}7\text{ s}}$ (*upload* agregado).

#### (c) $N = 1000$

- $d_{CS} = \max\{10\,000,\ 20\} = \mathbf{10\,000\text{ s}}$ (quase 3 horas;
  servidor).
- P2P: $\dfrac{10^{12}}{10^8 + 5\times10^9} = \dfrac{10^{12}}{5{,}1\times10^9} \approx 196{,}1$ s.
  $d_{P2P} = \mathbf{196{,}1\text{ s}}$ (*upload* agregado).

**Leitura:** de $N = 10$ para $N = 1000$ o cliente-servidor fica **100
vezes** mais lento; o P2P só **3 vezes**. Quando $N$ é muito grande, o
termo P2P aproxima-se de $F/u = 10^9 / (5\times10^6) = 200$ s: cada par
novo traz tanta capacidade quanta pede. Contas confirmadas em Python.

## Aula 2 --- Programação com sockets

### C2.7 --- Sockets (exercício inventado)

#### (a) Servidor iterativo: quando é que o B recebe a resposta?

O B só recebe a resposta **depois de o A ser atendido**, cerca de **3 s**
depois (testado: o B recebeu a resposta ao fim de 3,01 s).

Porquê: o `TCPServer` faz `accept()` e fica a tratar do A. A linha
`inFromClient.readLine()` **bloqueia** à espera da linha do A, que só
chega 3 s depois. Durante esse tempo o servidor não volta ao `accept()`.
A conexão do B **é estabelecida** na mesma (o sistema operativo completa
o *handshake* TCP e põe-na numa fila de conexões pendentes), e a linha
que o B enviou fica no *buffer*. Mas ninguém a lê até o servidor acabar o
A, fechar essa socket e voltar ao início do ciclo.

É a limitação dos servidores **iterativos**: um cliente lento atrasa
todos os outros.

#### (b) Servidor concorrente com *threads*

Resposta-modelo (compilada e testada: com o A parado 3 s, o B recebeu a
resposta de imediato):

```java
import java.io.*;
import java.net.*;

class TCPServerThreads {
    public static void main(String argv[]) throws Exception {
        ServerSocket welcomeSocket = new ServerSocket(6789);
        while (true) {
            Socket connectionSocket = welcomeSocket.accept();   // espera um cliente
            new Thread(() -> atende(connectionSocket)).start(); // atende-o noutra thread
        }                                                       // e volta logo ao accept()
    }

    static void atende(Socket connectionSocket) {
        try {
            BufferedReader inFromClient = new BufferedReader(
                new InputStreamReader(connectionSocket.getInputStream()));
            DataOutputStream outToClient =
                new DataOutputStream(connectionSocket.getOutputStream());
            String clientSentence = inFromClient.readLine();
            outToClient.writeBytes(clientSentence.toUpperCase() + '\n');
            connectionSocket.close();
        } catch (IOException e) {
            System.err.println("Erro com um cliente: " + e.getMessage());
        }
    }
}
```

- A *thread* principal **só** faz `accept()`: assim que um cliente se
  liga, entrega a `connectionSocket` a uma *thread* nova e volta
  imediatamente a esperar pelo próximo.
- Cada *thread* faz o que o ciclo do servidor iterativo fazia para um
  cliente: ler a linha, responder, fechar.
- O `try/catch` fica dentro da *thread*: um erro com um cliente não deita
  abaixo o servidor (os métodos de uma *thread* não podem lançar
  `IOException` para fora).
