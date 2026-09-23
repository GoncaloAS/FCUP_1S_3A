---
title: "Redes de Comunicação --- Soluções dos exercícios \"Pratica agora\""
subtitle: "Praticas/Semana_1/exercicios_redes.pdf. Tenta primeiro sozinho; abre uma alínea só depois de a teres feito. Convenções: 1 MB = 10⁶ bytes, 1 Mbps = 10⁶ bit/s, 1 byte = 8 bits."
---

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
