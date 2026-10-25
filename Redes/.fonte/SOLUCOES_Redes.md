---
title: "Redes de Comunicação --- Soluções dos exercícios \"Pratica agora\""
subtitle: "Ficha 1 (Praticas/Semana_1/exercicios_redes.pdf), Ficha 2 (Praticas/Semana_2/ficha_2.pdf, exercícios F2.x), Ficha 3 (Praticas/Semana_3/ficha_3_protocolos_aplicacionais.pdf, exercícios F3.x), Ficha 4 (Praticas/Semana_4/ficha_4_sockets_smtp.pdf, exercícios F4.x) o Teste modelo 1 (Testes/Teste_Modelo_1.pdf, M1.x) e exercícios inventados para o Capítulo 2 (C2.x). As fichas 1 a 3 e o teste modelo têm soluções oficiais; as diferenças estão assinaladas. Tenta primeiro sozinho; abre uma alínea só depois de a teres feito. Convenções: 1 MB = 10⁶ bytes, 1 Mbps = 10⁶ bit/s, 1 byte = 8 bits."
---

## Comutação de pacotes --- multiplexagem estatística

### F2.2 --- Multiplexagem estatística (Ficha 2)

**Significado de todas as variáveis e conceitos:**
* **$R$ (capacidade total / largura de banda da ligação)**: $1\text{ Mbps} = 1000\text{ kbps} = 10^6\text{ bit/s}$.
* **$r$ (taxa de transmissão de cada utilizador quando ativo)**: $100\text{ kbps} = 10^5\text{ bit/s}$.
* **$p$ (probabilidade de um utilizador estar ativo a transmitir)**: $10\% = 0{,}1$.
* **$1 - p$ (probabilidade de um utilizador estar inativo / silencioso)**: $90\% = 0{,}9$.
* **$N$ (número total de utilizadores a partilhar a ligação)**: $35$ utilizadores.
* **$X$ (variável aleatória)**: número de utilizadores a transmitir em simultâneo num dado instante. Como os utilizadores agem de forma independente, $X$ segue uma distribuição binomial: $X \sim \text{Bin}(N = 35;\ p = 0{,}1)$.
* **Comutação de Circuitos vs Comutação de Pacotes com Multiplexagem Estatística:**
  * Na comutação de circuitos (TDM/FDM com reserva estrita de largura de banda), a ligação só suportaria $R / r = 1000\text{ kbps} / 100\text{ kbps} = 10$ utilizadores garantidos em simultâneo.
  * Na comutação de pacotes com **multiplexagem estatística**, podemos aceitar 35 utilizadores porque os utilizadores não transmitem em contínuo e raramente estão mais de 10 ativos ao mesmo tempo.

#### (c) Probabilidade de exatamente $k$ a transmitir; valor para $k = 3$

**Fórmula da Distribuição Binomial:**
$$P(X = k) = \binom{N}{k}\, p^k\, (1-p)^{N-k} = \binom{35}{k}\, 0{,}1^k\, 0{,}9^{35-k}$$

**O que significa cada termo da fórmula:**
1. **$\binom{35}{k} = \frac{35!}{k!(35-k)!}$ (combinações de 35 a $k$)**: é o número de maneiras distintas de escolher **quais** $k$ utilizadores (de entre os 35 utilizadores possíveis) estão ativos a transmitir em simultâneo.
2. **$0{,}1^k$**: probabilidade de esses $k$ utilizadores específicos estarem **todos ativos** ao mesmo tempo ($0{,}1$ multiplicado $k$ vezes).
3. **$0{,}9^{35-k}$**: probabilidade dos restantes $(35 - k)$ utilizadores estarem **todos inativos/silenciosos** ($0{,}9$ multiplicado $35-k$ vezes).

**Cálculo passo a passo para $k = 3$ utilizadores:**

1. **Número de combinações:**
$$\binom{35}{3} = \frac{35 \times 34 \times 33}{3 \times 2 \times 1} = \frac{39\,270}{6} = 6545$$

2. **Probabilidade dos 3 estarem ativos:**
$$0{,}1^3 = 0{,}1 \times 0{,}1 \times 0{,}1 = 0{,}001$$

3. **Probabilidade dos restantes 32 estarem inativos:**
$$0{,}9^{35 - 3} = 0{,}9^{32} \approx 0{,}0343368$$

4. **Multiplicação das três parcelas:**
$$P(X = 3) = 6545 \times 0{,}001 \times 0{,}0343368 \approx \mathbf{0{,}2247} \approx \mathbf{22{,}5\%}$$

**Interpretação:**
Existe cerca de $22{,}5\%$ de probabilidade de exatamente 3 utilizadores estarem a transmitir em simultâneo. Este é o valor mais provável de todos, porque o número médio esperado de utilizadores ativos é $E[X] = N \times p = 35 \times 0{,}1 = 3{,}5$ utilizadores.

#### (d) $P(X \geq 11)$ com `BINOM.DIST()`

"11 ou mais" é o complementar de "10 ou menos", e o `BINOM.DIST` com o
último argumento `VERDADEIRO` dá a probabilidade acumulada, $P(X \leq k)$:

$$P(X \geq 11) = 1 - P(X \leq 10) = 1 - \texttt{BINOM.DIST(10; 35; 0,1; VERDADEIRO)}$$

$$= 1 - 0{,}999576 \approx \mathbf{0{,}000424}$$

É o 0,0004 do exemplo do resumo (valor confirmado em Python com
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

**Significado de todas as variáveis e conceitos:**
* **$L$ (tamanho do vídeo)**: $700\text{ MB} = 700 \times 10^6\text{ Bytes}$. Em bits: $700 \times 10^6 \times 8 = 5{,}6 \times 10^9\text{ bits}$ *(1 Byte = 8 bits)*.
* **$R$ (capacidade / taxa de transmissão de cada ligação)**: $100\text{ Mbps} = 100 \times 10^6\text{ bit/s} = 10^8\text{ bit/s}$.
* **Topologia**: Alice $\to$ Router 1 $\to$ Router 2 $\to$ Bob (2 routers intermédios $\implies$ **3 ligações físicas em série**, $h = 3$ saltos).
* **$d_{trans}$ (atraso de transmissão)**: tempo que um transmissor demora a injetar todos os bits de um bloco/pacote no cabo: $d_{trans} = \text{bits} / R$.
* **Princípio de *Store-and-Forward* (armazenar e reenviar)**: cada router tem de receber o bloco/pacote por completo antes de poder começar a retransmiti-lo para a ligação seguinte.
* **Princípio de *Pipelining* (segmentação)**: ao dividir o ficheiro em milhares de pacotes pequenos, as 3 ligações trabalham em paralelo, reduzindo drasticamente o tempo total.

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

**1. Sem divisão em pedaços (ficheiro inteiro com 1 envelope de 20 Bytes):**
* O ficheiro fica com $5{,}6 \times 10^9\text{ bits} + (20 \times 8\text{ bits}) = 5{,}6 \times 10^9 + 160\text{ bits}$.
* Tempo de transmissão numa ligação de 100 Mbps:
$$d_{trans} = \frac{5{,}6 \times 10^9 + 160}{10^8} \approx 56\text{ s}$$
* Com 3 ligações em série sem *pipelining* (cada nó recebe tudo antes de reenviar):
$$T_{total,inteiro} = 3 \times 56\text{ s} \approx \mathbf{168\text{ s}}$$
*(O envelope único de 20 Bytes é completamente desprezável face aos 700 MB).*

**2. Com divisão em pedaços de 1000 Bytes de dados + 20 Bytes de envelope:**
* **Número de pedaços ($N$)**:
$$N = \frac{700 \times 10^6\text{ Bytes}}{1000\text{ Bytes/pedaço}} = 700\,000\text{ pedaços}$$
* **Tamanho total de cada pedaço com envelope ($L_{pacote}$)**:
$$L_{pacote} = 1000 + 20 = 1020\text{ Bytes} = 1020 \times 8 = 8160\text{ bits}$$
* **Atraso de transmissão de 1 pedaço ($d_{trans,pacote}$)**:
$$d_{trans,pacote} = \frac{8160\text{ bits}}{10^8\text{ bit/s}} = 8{,}16 \times 10^{-5}\text{ s} = 81{,}6\ \mu\text{s}$$
* **Tempo total com *pipelining* ao longo de 3 ligações ($T_{total,pedaços}$)**:
  * A Alice injeta os $N = 700\,000$ pedaços na 1.ª ligação consecutivamente: o último pedaço acaba de sair da Alice no instante $N \times d_{trans,pacote}$.
  * Esse último pedaço ainda tem de ser retransmitido pelo Router 1 (2.ª ligação) e pelo Router 2 (3.ª ligação), demorando mais 2 transmissões ($2 \times d_{trans,pacote}$).
  * Fórmula de *pipelining*:
$$T = (N + 3 - 1) \times d_{trans,pacote} = 700\,002 \times 81{,}6\ \mu\text{s} = 700\,002 \times 81{,}6 \times 10^{-6}\text{ s} \approx \mathbf{57{,}12\text{ s}}$$

**Comparação e Poupança:**
* **Poupança brutal com segmentação**: $168\text{ s} - 57{,}12\text{ s} \approx \mathbf{110{,}9\text{ s}}$ (a transferência fica quase 3 vezes mais rápida graças ao trabalho em paralelo das ligações!).
* **Custo do cabeçalho / envelope (soluções oficiais `solucoes_ficha_1.pdf`)**:
  * Sem envelope (alínea b), demorava $56{,}00\text{ s}$.
  * Com o envelope de 20 Bytes por pacote (alínea c), demora $57{,}12\text{ s}$.
  * O acréscimo de tempo devido aos envelopes é de $57{,}12 - 56{,}00 = \mathbf{1{,}12\text{ s}}$ (exatamente a resposta do gabarito oficial).
  * Conclusão: o overhead do cabeçalho custa apenas cerca de 2% ($20 / 1000$), compensando largamente o ganho do *pipelining*.

### Ex. 4 --- *Store and forward* LAN + WAN

**Significado de todas as variáveis e conceitos:**
* **$L$ (tamanho do pacote)**: $1250\text{ Bytes} = 1250 \times 8\text{ bits} = 10\,000\text{ bits} = 10^4\text{ bits}$.
* **$v$ (velocidade de propagação da luz na fibra)**: $2 \times 10^8\text{ m/s}$.
* **Topologia**: T1 $\to$ LAN (comprimento $d_{LAN}$, débito $R_{LAN}$) $\to$ Router R $\to$ WAN (comprimento $d_{WAN}$, débito $R_{WAN}$) $\to$ T2.
* **$d_{trans} = L / R$ (atraso de transmissão)**: tempo gasto pela placa de rede a injetar todos os bits do pacote no cabo.
* **$d_{prop} = d / v$ (atraso de propagação)**: tempo gasto pelo sinal de luz a viajar fisicamente pela fibra da origem ao destino.
* **Princípio de *Store-and-Forward***: o router R tem de receber o pacote por completo antes de começar a transmiti-lo para a WAN.

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

Invertendo as taxas de transmissão, a LAN passa a ser ultra-rápida e a WAN lenta:
* **LAN ($R_{LAN} = 1\text{ Gbps} = 10^9\text{ b/s}$, $d_{LAN} = 4\text{ km} = 4000\text{ m}$)**:
  * $d_{trans,LAN} = \frac{10^4\text{ bits}}{10^9\text{ b/s}} = 10^{-5}\text{ s} = \mathbf{10\ \mu\text{s}}$
  * $d_{prop,LAN} = \frac{4000\text{ m}}{2\times 10^8\text{ m/s}} = 2 \times 10^{-5}\text{ s} = \mathbf{20\ \mu\text{s}}$
* **WAN ($R_{WAN} = 10\text{ Mbps} = 10^7\text{ b/s}$, $d_{WAN} = 80\text{ km} = 80\,000\text{ m}$)**:
  * $d_{trans,WAN} = \frac{10^4\text{ bits}}{10^7\text{ b/s}} = 10^{-3}\text{ s} = \mathbf{1\text{ ms}} = 1000\ \mu\text{s}$
  * $d_{prop,WAN} = \frac{80\,000\text{ m}}{2\times 10^8\text{ m/s}} = 4 \times 10^{-4}\text{ s} = \mathbf{400\ \mu\text{s}} = 0{,}4\text{ ms}$

**Cálculo para 1 pacote de T1 a T2:**
Soma-se a transmissão e propagação nas duas ligações:
$$T_1 = d_{trans,LAN} + d_{prop,LAN} + d_{trans,WAN} + d_{prop,WAN}$$
$$= 10\ \mu\text{s} + 20\ \mu\text{s} + 1000\ \mu\text{s} + 400\ \mu\text{s} = 1430\ \mu\text{s} = \mathbf{1{,}43\text{ ms}}$$

**Cálculo para 10 pacotes de T1 a T2 (Atenção à Fila no Router!):**
* **Porque se forma fila no router R?**
  * A LAN despacha pacotes para R a cada $10\ \mu\text{s}$ (o 1.º chega aos $30\ \mu\text{s}$, o 2.º aos $40\ \mu\text{s}$, ..., o 10.º aos $120\ \mu\text{s}$).
  * Contudo, a WAN (o **gargalo**) demora $1000\ \mu\text{s}$ ($1\text{ ms}$) a transmitir cada pacote!
  * Quando os pacotes 2 a 10 chegam ao router, a WAN ainda está ocupadíssima com o pacote 1. Por isso, os pacotes **acumulam-se obrigatoriamente na fila de espera (*buffer*) do router**!
* **Cronologia dos 10 pacotes (em microssegundos $\mu\text{s}$):**

| Pacote | Chega a R | Começa a sair de R para a WAN | Acaba de sair de R | Acaba de chegar a T2 |
|:---:|:---:|:---:|:---:|:---:|
| 1 | $10 + 20 = 30$ | 30 (WAN livre) | $30 + 1000 = 1030$ | $1030 + 400 = 1430$ |
| 2 | $20 + 20 = 40$ | 1030 (esperou na fila!) | $1030 + 1000 = 2030$ | $2030 + 400 = 2430$ |
| 3 | $30 + 20 = 50$ | 2030 (esperou na fila!) | $2030 + 1000 = 3030$ | $3030 + 400 = 3430$ |
| ... | ... | ... | ... | ... |
| 10 | $100 + 20 = 120$ | 9030 (esperou na fila!) | $9030 + 1000 = \mathbf{10\,030}$ | $10\,030 + 400 = \mathbf{10\,430}$ |

* **Fórmula direta do tempo total:**
  * O tempo total é determinado pela ligação mais lenta (a WAN), que transmite os 10 pacotes consecutivamente ($10 \times d_{trans,WAN}$), somado ao tempo que o 1.º pacote demorou a chegar a R e à propagação final até T2:
  $$T_{total} = (d_{trans,LAN} + d_{prop,LAN}) + 10 \times d_{trans,WAN} + d_{prop,WAN}$$
  $$= (10\ \mu\text{s} + 20\ \mu\text{s}) + (10 \times 1000\ \mu\text{s}) + 400\ \mu\text{s} = 30 + 10\,000 + 400 = \mathbf{10\,430\ \mu\text{s}} = \mathbf{10{,}43\text{ ms}}$$

**Conclusão física essencial:**
O tempo total ($10{,}43\text{ ms}$) é igual ao da alínea (c), porque a ligação mais lenta (10 Mbps) tem sempre de transmitir os 10 pacotes. A diferença vital é **onde os pacotes esperam**:
* Na alínea (c), esperam em T1 antes de entrar na rede.
* Na alínea (d), entram depressa na rede e acumulam-se no **buffer do router**. Se a fila for pequena, pode ocorrer **perda de pacotes** por descarte!

### M1.11 --- *Store-and-forward* LAN + WAN (Teste modelo 1, P. 11)

**Significado de todas as variáveis e abreviações do problema:**
* **$L$ (*Length* = tamanho do pacote)**: $1000\text{ Bytes} = 1000 \times 8\text{ bits} = 8000\text{ bits} = 8\times 10^3\text{ b}$. *(Atenção: 1 Byte tem 8 bits; as contas de transmissão usam sempre bits, nunca Bytes!).*
* **$R_{LAN}$ (*Rate* = taxa de transmissão / capacidade da ligação LAN)**: $10\text{ Mbit/s} = 10 \times 10^6\text{ bit/s} = 10^7\text{ b/s}$.
* **$l_{LAN}$ (*length* = comprimento físico do cabo da LAN)**: $20\text{ metros}$.
* **$v$ (*velocity* = velocidade de propagação da luz no meio físico)**: $2\times 10^8\text{ m/s}$ *(valor típico da velocidade da luz dentro do núcleo de fibra ótica)*.
* **$d_{trans}$ (*transmission delay* = atraso de transmissão)**: tempo que a placa de rede demora a "injetar" (empurrar) todos os bits do pacote para o cabo. Fórmula: $d_{trans} = L / R$. *(Depende do tamanho do pacote $L$ e da taxa $R$; não depende da distância!).*
* **$d_{prop}$ (*propagation delay* = atraso de propagação)**: tempo que o sinal eletromagnético demora a percorrer fisicamente o cabo da origem ao destino à velocidade da luz. Fórmula: $d_{prop} = \text{distância} / v$. *(Depende da distância e do meio; não depende do tamanho do pacote!).*
* **Dados da ligação WAN (já calculados e fornecidos no enunciado):**
  * $d_{trans,WAN} = 0{,}6\text{ ms} = 6\times 10^{-4}\text{ s}$ *(atraso de transmissão na WAN)*.
  * $d_{prop,WAN} = 15\text{ ms} = 1{,}5\times 10^{-2}\text{ s}$ *(atraso de propagação na WAN)*.

#### (a) Atrasos de transmissão e de propagação na LAN

1. **Atraso de transmissão na LAN ($d_{trans,LAN}$)** — tempo para injetar os 8000 bits no cabo da LAN a 10 Mbps:
$$d_{trans,LAN} = \frac{L\text{ (tamanho do pacote em bits)}}{R_{LAN}\text{ (capacidade em bit/s)}} = \frac{8\times10^3\text{ b}}{10^7\text{ b/s}} = \mathbf{8\times10^{-4}\text{ s}} = \mathbf{0{,}8\text{ ms}}$$

2. **Atraso de propagação na LAN ($d_{prop,LAN}$)** — tempo para a luz percorrer os 20 metros de cabo:
$$d_{prop,LAN} = \frac{l_{LAN}\text{ (distância em metros)}}{v\text{ (velocidade da luz em m/s)}} = \frac{20\text{ m}}{2\times10^8\text{ m/s}} = \mathbf{10^{-7}\text{ s}} = \mathbf{0{,}1\ \mu s}\text{ (microssegundos)}$$

#### (b) Um pacote de T1 a T2

**Princípio de *Store-and-forward* (armazenar e reenviar):** o router R1 só começa a transmitir o pacote para a WAN **depois de o ter recebido por completo** da LAN (o último bit do pacote tem de estar guardado na memória do router).

Como não há filas de espera nem atrasos de processamento nodais, o percurso de um único pacote soma as 4 parcelas cronológicas:
1. $d_{trans,LAN}$: T1 injeta todos os bits na LAN ($0{,}8\text{ ms}$).
2. $d_{prop,LAN}$: os bits viajam fisicamente pela fibra da LAN até chegarem a R1 ($0{,}0001\text{ ms}$).
3. $d_{trans,WAN}$: R1 injeta todos os bits na WAN ($0{,}6\text{ ms}$).
4. $d_{prop,WAN}$: os bits viajam fisicamente pela fibra da WAN até chegarem a T2 ($15\text{ ms}$).

$$d_{total,1} = d_{trans,LAN} + d_{prop,LAN} + d_{trans,WAN} + d_{prop,WAN}$$
$$= 0{,}8\text{ ms} + 0{,}0001\text{ ms} + 0{,}6\text{ ms} + 15\text{ ms} = \mathbf{16{,}4001\text{ ms}} \approx 16{,}4\text{ ms}$$

#### (c) Diagrama temporal de 4 pacotes

![4 pacotes de T1 a T2: a LAN (0,8 ms por pacote) é a ligação mais lenta, por isso nunca há fila em R1](figuras/sol_m1_store_forward.svg){width=100%}

**Como ler e construir o diagrama temporal:**
* O eixo vertical representa o **tempo a avançar para baixo**.
* A largura de cada faixa representa o atraso de transmissão $d_{trans}$ (tempo gasto a emitir o pacote).
* A inclinação de cada faixa representa o atraso de propagação $d_{prop}$ (tempo de viagem no cabo).
  * Na LAN, a propagação é minúscula ($0{,}1\ \mu\text{s} = 0{,}0001\text{ ms}$), pelo que as faixas parecem quase horizontais.
  * Na WAN, a propagação é grande ($15\text{ ms}$), pelo que as faixas descem bastante.
* **Porque não há fila no router R1?** A LAN despacha 1 pacote a cada $0{,}8\text{ ms}$, mas a WAN despacha cada pacote em apenas $0{,}6\text{ ms}$. Quando o pacote seguinte chega da LAN ao router, a WAN já acabou de enviar o anterior há $0{,}2\text{ ms}$ e está livre à espera!

Instantes em milissegundos (ms) em que cada pacote acaba de ser processado em cada ponto:

| pacote | acaba de sair de T1 | acaba de chegar a R1 | acaba de sair de R1 | acaba de chegar a T2 |
|:-:|:-:|:-:|:-:|:-:|
| 1 | 0,8 | 0,8001 | 0,8001 + 0,6 = 1,4001 | 1,4001 + 15 = 16,4001 |
| 2 | 1,6 | 1,6001 | 1,6001 + 0,6 = 2,2001 | 2,2001 + 15 = 17,2001 |
| 3 | 2,4 | 2,4001 | 2,4001 + 0,6 = 3,0001 | 3,0001 + 15 = 18,0001 |
| 4 | 3,2 | 3,2001 | 3,2001 + 0,6 = 3,8001 | 3,8001 + 15 = **18,8001** |

#### (d) Tempo dos 4 pacotes

**Conceito de *Pipelining* (cadeia de transmissão):**
Não precisamos de calcular tudo do zero para cada pacote. O ritmo de toda a rede é ditado pela **ligação mais lenta (gargalo = LAN)**.
* A LAN transmite os 4 pacotes colados, um a seguir ao outro, demorando $4 \times d_{trans,LAN} = 4 \times 0{,}8\text{ ms} = 3{,}2\text{ ms}$.
* O 4.º pacote (o último) sai de T1 ao instante $3{,}2\text{ ms}$. A partir daí, basta cronometrar o resto do percurso deste último pacote até chegar ao destino T2 (exatamente como se estivesse sozinho):
  * Propagação na LAN: $d_{prop,LAN} = 0{,}0001\text{ ms}$.
  * Transmissão na WAN: $d_{trans,WAN} = 0{,}6\text{ ms}$.
  * Propagação na WAN: $d_{prop,WAN} = 15\text{ ms}$.

$$d_{total,4} = 4 \times d_{trans,LAN} + d_{prop,LAN} + d_{trans,WAN} + d_{prop,WAN}$$
$$= 3{,}2\text{ ms} + 0{,}0001\text{ ms} + 0{,}6\text{ ms} + 15\text{ ms} = \mathbf{18{,}8001\text{ ms}} \approx 18{,}8\text{ ms}$$

É a resolução oficial (`Testes/Teste_Modelo_1_resolucao.pdf`), com os
mesmos valores. O oficial desenha o diagrama à mão e não faz a tabela: no
teste basta o desenho, com os quatro atrasos assinalados.

## Atrasos --- filas de espera

### F2.3 --- Espere, mas não desespere (Ficha 2)

**Analogia de Redes e Significado das Variáveis:**
* **Máquina de café $\iff$ Interface de rede / Router**: representa o transmissor que processa e transmite os dados com taxa de transmissão $R$.
* **Tirar um café $\iff$ Atraso de transmissão ($d_{trans}$)**: tempo que a ligação demora a injetar um pacote no cabo, $d_{trans} = L / R = 15\text{ s}$ ($L$ = tamanho do pacote em bits, $R$ = capacidade em bit/s).
* **Fila de pessoas $\iff$ Fila de espera de pacotes (*Queueing Delay* $d_{fila}$)**: tempo que um pacote aguarda na memória (*buffer*) do router até chegar a sua vez de ser transmitido.
* **Chegada simultânea de 10 pessoas $\iff$ Rajada de pacotes (*Burst Arrival*)**: $N = 10$ pacotes que chegam no mesmo instante a um buffer inicialmente vazio.

#### (a) 10 pessoas chegam ao mesmo tempo: espera média, mínima e máxima

**1. Tempos de espera em fila individuais:**
Como o buffer obedece a uma política FIFO (*First-In, First-Out* / primeiro a chegar, primeiro a ser servido):
* O 1.º pacote encontra a linha desocupada e é servido imediatamente: espera $d_{fila}(1) = \mathbf{0\text{ s}}$.
* O 2.º pacote espera que o 1.º termine: espera $d_{fila}(2) = 15\text{ s}$.
* O 3.º pacote espera que os 2 anteriores terminem: espera $d_{fila}(3) = 2 \times 15 = 30\text{ s}$.
* Genericamente, o $n$-ésimo pacote (onde $n \in \{1, 2, \dots, N\}$) aguarda por $(n - 1)$ transmissões anteriores:
$$d_{fila}(n) = (n - 1) \times d_{trans} = (n - 1) \times \frac{L}{R} = (n - 1) \times 15\text{ s}$$

Para o 10.º pacote ($n = 10$):
$$d_{fila}(10) = (10 - 1) \times 15 = 9 \times 15 = \mathbf{135\text{ s}}$$

* **Tempo de espera mínimo em fila:** $\mathbf{0\text{ s}}$ (a 1.ª pessoa/pacote).
* **Tempo de espera máximo em fila:** $\mathbf{135\text{ s}}$ (a 10.ª pessoa/pacote).

**2. Tempo médio de espera em fila ($\bar{d}_{fila}$):**
Fórmula analítica da média para uma rajada de $N$ pacotes:
$$\bar{d}_{fila} = \frac{1}{N} \sum_{n=1}^{N} d_{fila}(n) = \frac{1}{N} \sum_{n=1}^{N} (n - 1) \times d_{trans} = \frac{d_{trans}}{N} \times [0 + 1 + 2 + \dots + (N - 1)]$$

Usando a soma da progressão aritmética $\sum_{i=0}^{N-1} i = \frac{(N-1)N}{2}$:
$$\bar{d}_{fila} = \frac{d_{trans}}{N} \times \frac{(N-1)N}{2} = \frac{N - 1}{2} \times d_{trans} = \frac{N - 1}{2} \times \frac{L}{R}$$

Substituindo $N = 10$ e $d_{trans} = 15\text{ s}$:
$$\bar{d}_{fila} = \frac{10 - 1}{2} \times 15\text{ s} = \frac{9}{2} \times 15 = 4{,}5 \times 15 = \mathbf{67{,}5\text{ s}}$$

*(Nota: se a pergunta se referir ao tempo total no sistema até ter o café pronto na mão, soma-se o tempo de transmissão de si próprio, $15\text{ s}$: tempo total mínimo = $15\text{ s}$, máximo = $150\text{ s}$, e média = $67{,}5 + 15 = 82{,}5\text{ s}$. Contudo, o atraso estrito de fila é $0$, $135$ e $67{,}5\text{ s}$).*

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

## Atrasos --- ping e traceroute

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

## Atrasos --- perdas e melhor esforço

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

**Comparação com as respostas oficiais** (`Semana_2/respostas.pdf`): o
oficial faz a mesma prova pelo outro lado. Se um protocolo funciona com
$N$ mensagens, como cada uma se pode perder, também funciona com $N-1$;
aplicando isto repetidamente, funcionaria com 0 mensagens, o que é
impossível. Escolher o $n$ mínimo, como acima, é a forma rigorosa desse
"repetidamente".

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

**Técnica do Par de Pacotes (*Packet-Pair Dispersion*) e Significado das Variáveis:**
* **Conceito**: Técnica usada para medir a capacidade da ligação mais estreita (o **gargalo / *bottleneck***) de um caminho na rede sem precisar de privilégios de administração nos routers intermédios.
* **$L$ (tamanho de cada pacote em bits)**: enviam-se dois pacotes idênticos (P1 e P2), de tamanho $L$ bits, colados um ao outro (*back-to-back*).
* **$R_{emissor}$ (taxa de envio do emissor)**: ligação de envio rápida ($R_{emissor} > C$).
* **$C$ (capacidade da ligação mais lenta / estrangulamento)**: largura de banda da ligação mais lenta do percurso em bit/s.
* **$\Delta t$ (dispersão temporal / desfasamento)**: intervalo de tempo entre o instante em que o 1.º pacote acaba de chegar e o instante em que o 2.º pacote acaba de chegar ao destino.

#### (a) Diagrama temporal

![Par de pacotes: o espaçamento criado na ligação lenta mantém-se até ao recetor](figuras/sol_par_pacotes.svg){width=100%}

**Como o diagrama funciona e explicação passo a passo:**
1. **No Emissor (ligação rápida $R_1$):**
   * O emissor transmite o pacote 1 (P1) e o pacote 2 (P2) colados um ao outro.
   * O tempo de transmissão de cada um é curto: $d_{trans,1} = L / R_1$.
2. **No Router de entrada da ligação de estrangulamento ($C$):**
   * O router recebe P1 e começa imediatamente a transmiti-lo na ligação lenta de capacidade $C$. A transmissão de P1 demora $L / C$ segundos.
   * Como a ligação $R_1$ era muito mais rápida do que $C$, o pacote P2 chega ao router logo a seguir, enquanto o router ainda está a transmitir P1.
   * Por isso, **P2 é forçado a esperar na fila do router** até P1 acabar de ser transmitido por completo.
   * Assim que P1 acaba de sair, o router começa imediatamente a transmitir P2. Portanto, o fim de P2 sai do router exatamente $L / C$ segundos depois do fim de P1.
3. **Nas ligações seguintes e no Recetor:**
   * Mesmo que as ligações seguintes até ao destino sejam ultra-rápidas, elas não conseguem aproximar os pacotes: cada pacote viaja à mesma velocidade e sofre as mesmas propagações.
   * Logo, os dois pacotes chegam ao recetor com a **mesma separação temporal**: $\Delta t = \frac{L}{C}$.
4. **Estimativa da capacidade da ligação ($C$):**
   * Conhecendo o tamanho dos pacotes enviados ($L$ bits) e medindo no recetor (ou nos ACKs de volta) a diferença de tempo $\Delta t$ entre o fim do 1.º e o fim do 2.º pacote, deduz-se imediatamente a capacidade da ligação mais lenta:
$$\Delta t = \frac{L}{C} \iff \mathbf{C = \frac{L}{\Delta t}}$$

*Exemplo prático:* se enviarmos pacotes de $L = 1500\text{ Bytes} = 12\,000\text{ bits}$ e o espaçamento medido à chegada for $\Delta t = 1{,}2\text{ ms} = 1{,}2 \times 10^{-3}\text{ s}$, a capacidade estimada do gargalo é:
$$C = \frac{12\,000\text{ bits}}{1{,}2 \times 10^{-3}\text{ s}} = 10^7\text{ bit/s} = \mathbf{10\text{ Mbit/s}}$$

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

## Aula 2 --- Tempo de resposta do HTTP

### C2.1 --- Tempo de resposta do HTTP (exercício inventado)

**Significado de todas as variáveis e conceitos:**
* **$RTT$ (*Round Trip Time* = Tempo de Ida e Volta)**: $40\text{ ms}$. É o tempo que um pequeno pacote de controlo demora a viajar do cliente até ao servidor e o pacote de resposta/confirmação a regressar ao cliente ($RTT \approx 2 \times d_{prop}$).
* **$T$ (atraso de transmissão de cada objeto)**: $10\text{ ms}$. Tempo gasto pelo servidor a injetar todos os bits de um ficheiro/imagem na ligação ($T = L / R$).
* **Ficheiros a descarregar**: 1 ficheiro base de texto HTML + 5 objetos embutidos (imagens/gráficos) = **6 objetos no total**.
* **Estabelecimento de conexão TCP (*3-Way Handshake*)**: antes de enviar qualquer pedido HTTP, o cliente tem de abrir uma ligação de transporte TCP (SYN $\to$ SYN-ACK $\to$ ACK), o que consome exatamente **$1\text{ RTT}$**.

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

**Como funciona o HTTP Persistente com *Pipelining*:**
Com uma única conexão TCP aberta, o browser descarrega primeiro o HTML. Assim que o processa e identifica todos os 5 objetos referenciados, **envia os 5 pedidos HTTP GET de uma assentada (em rajada / *pipeline*)**, sem esperar pela resposta de nenhum! O servidor processa-os e envia as 5 respostas consecutivamente, uma a seguir à outra.

**Cronologia detalhada:**
1. **Abertura da conexão TCP:**
   * O cliente envia o segmento TCP SYN e recebe TCP SYN-ACK: demora **$1\text{ RTT} = 40\text{ ms}$**.
2. **Obtenção do ficheiro base HTML:**
   * O cliente envia o pedido `GET index.html` (que segue acoplado ao ACK final do handshake TCP) e o servidor devolve o ficheiro HTML: demora **$1\text{ RTT} + T_{HTML} = 40\text{ ms} + 10\text{ ms} = 50\text{ ms}$**.
   * Ao instante $t = 40 + 50 = 90\text{ ms}$, o browser tem o ficheiro HTML completo. O analisador (*parser*) lê o HTML e descobre a referência para as 5 imagens.
3. **Obtenção dos 5 objetos com *pipelining*:**
   * O browser envia imediatamente os 5 pedidos `GET` seguidos no mesmo instante ($t = 90\text{ ms}$).
   * O primeiro bit da primeira resposta chega após **$1\text{ RTT} = 40\text{ ms}$** de propagação de ida e volta.
   * O servidor transmite as 5 respostas de seguida sem pausas: $5 \times T = 5 \times 10\text{ ms} = 50\text{ ms}$.
   * Tempo gasto nesta fase: $1\text{ RTT} + 5 \times T = 40\text{ ms} + 50\text{ ms} = 90\text{ ms}$.

**Tempo Total:**
$$T_{total,pipelining} = 90\text{ ms (TCP + HTML)} + 90\text{ ms (5 objetos)} = \mathbf{180\text{ ms}}$$

**Comparação exaustiva dos 3 modos HTTP:**

| Modo HTTP | Conexões TCP | RTTs gastos | Transmissão ($6 \times T$) | Tempo Total |
|:---|:---:|:---:|:---:|:---:|
| **Não persistente** (1 conexão por objeto) | 6 conexões | $6 \times (1\text{ TCP} + 1\text{ GET}) = 12\text{ RTT} = 480\text{ ms}$ | $60\text{ ms}$ | **540 ms** |
| **Persistente sem *pipelining*** | 1 conexão | $1\text{ TCP} + 6\text{ GETs individuais} = 7\text{ RTT} = 280\text{ ms}$ | $60\text{ ms}$ | **340 ms** *(ou 290 ms se fossem 4 objetos)* |
| **Persistente com *pipelining*** | 1 conexão | $1\text{ TCP} + 1\text{ HTML} + 1\text{ rajada} = 3\text{ RTT} = 120\text{ ms}$ | $60\text{ ms}$ | **180 ms** |

*Verificação algébrica:*
* Não persistente: $12 \times 40\text{ ms} + 6 \times 10\text{ ms} = 480 + 60 = 540\text{ ms}$.
* Sem pipelining: $7 \times 40\text{ ms} + 6 \times 10\text{ ms} = 280 + 60 = 340\text{ ms}$.
* Com pipelining: $3 \times 40\text{ ms} + 6 \times 10\text{ ms} = 120 + 60 = 180\text{ ms}$.
O pipelining é 3 vezes mais rápido que o não persistente e quase 2 vezes mais rápido que o persistente sem pipelining!

### C2.7 --- MSC de HTTP não persistente (exercício inventado)

$d_{prop} = 20$ ms, logo $\text{RTT} = 2\,d_{prop} = 40$ ms;
$R = 10$ Mb/s $= 10^7$ b/s.

- $L_{HTML} = 25$ kB $= 2\times10^5$ b, logo $d_{trans,HTML} = \dfrac{2\times10^5}{10^7} = 20$ ms.
- $L_{img} = 50$ kB $= 4\times10^5$ b, logo $d_{trans,img} = \dfrac{4\times10^5}{10^7} = 40$ ms.

#### (a) MSC

![HTTP não persistente: cada objeto abre a sua conexão TCP (SYN, SYN-ACK) e o pedido vai com o último ACK](figuras/sol_c27_http_msc.svg){width=70%}

Para **cada** objeto, um a seguir ao outro:

1. SYN e SYN-ACK: 1 RTT para abrir a conexão;
2. o GET vai com o último ACK do *handshake*; o primeiro bit da
   resposta chega ao cliente 1 RTT depois de o GET sair;
3. a resposta demora $d_{trans}$ a passar toda (a faixa larga);
4. o servidor fecha a conexão e o browser abre outra para o objeto
   seguinte. As imagens só se pedem depois de o HTML chegar (é ao lê-lo
   que o browser as descobre).

#### (b) Tempo até ter tudo

Cada objeto custa $2\,\text{RTT} + d_{trans}$:

- HTML: $2 \times 40 + 20 = 100$ ms;
- cada imagem: $2 \times 40 + 40 = 120$ ms.

$$d_{total} = 100 + 120 + 120 = \mathbf{340\text{ ms}} = 6\,\text{RTT} + 100\text{ ms}$$

#### (c) Ganho com persistente sem *pipelining*

Abre-se a conexão **uma só vez** (1 RTT) e cada objeto custa
$\text{RTT} + d_{trans}$:
$$d_{pers} = \text{RTT} + 3\,\text{RTT} + (20 + 40 + 40) = 160 + 100 = 260\text{ ms}$$
Ganho: $340 - 260 = \mathbf{80\text{ ms}} = 2\,\text{RTT}$, as duas
conexões que deixam de se abrir (uma por imagem). É o MSC da P. 12 do
teste modelo.

### M1.12 --- A página com duas imagens (Teste modelo 1, P. 12)

**Significado de todas as variáveis e abreviações:**
* **$d_{prop}$ (*propagation delay* = atraso de propagação só de ida)**: $30\text{ ms} = 3\times 10^{-2}\text{ s}$ *(tempo que um sinal elétrico/luz demora a ir do cliente ao servidor)*.
* **$\text{RTT}$ (*Round-Trip Time* = tempo de ida e volta)**: tempo que um pacote pequeno demora a ir até ao servidor e a confirmação a voltar. Como a ida demora $d_{prop}$ e a volta demora $d_{prop}$, temos:
  $$\text{RTT} = 2 \times d_{prop} = 2 \times 30\text{ ms} = 60\text{ ms} = 6\times 10^{-2}\text{ s}$$
* **$R$ (*Rate* = taxa de transmissão / capacidade da ligação do utilizador)**: $80\text{ Mbit/s} = 80 \times 10^6\text{ bit/s} = 8\times 10^7\text{ b/s}$.
* **$L_{HTML}$ (*Length* = tamanho do ficheiro HTML base)**: $10\text{ kByte} = 10 \times 8 \times 10^3\text{ bits} = 8\times 10^4\text{ bits}$ *(1 Byte = 8 bits)*.
* **$d_{trans,HTML}$ (*atraso de transmissão do HTML*)**: tempo que a ligação demora a escoar os bits do HTML:
  $$d_{trans,HTML} = \frac{L_{HTML}}{R} = \frac{8\times 10^4\text{ b}}{8\times 10^7\text{ b/s}} = 10^{-3}\text{ s} = \mathbf{1\text{ ms}}$$
* **$L_{img}$ (*Length* = tamanho de cada uma das 2 imagens)**: $200\text{ kByte} = 200 \times 8 \times 10^3\text{ bits} = 1{,}6\times 10^6\text{ bits}$.
* **$d_{trans,img}$ (*atraso de transmissão de cada imagem*)**:
  $$d_{trans,img} = \frac{L_{img}}{R} = \frac{1{,}6\times 10^6\text{ b}}{8\times 10^7\text{ b/s}} = 2\times 10^{-2}\text{ s} = \mathbf{20\text{ ms}}$$
* **HTTP/1.1 persistente sem *pipelining***:
  * *Persistente*: abre a conexão TCP apenas **uma vez** para todos os objetos (não precisa de abrir e fechar novas conexões para cada imagem).
  * *Sem pipelining*: o browser só envia o pedido do objeto seguinte **depois de ter recebido completamente** a resposta do objeto anterior (nunca há dois pedidos em voo ao mesmo tempo).

#### (a) MSC com HTTP/1.1 persistente sem *pipelining*

![Uma conexão TCP para tudo; cada pedido só sai quando a resposta anterior acabou de chegar](figuras/sol_m1_http_msc.svg){width=70%}

**Construção passo a passo do MSC (Message Sequence Chart):**
1. **Abertura da conexão TCP (Handshake):**
   * O cliente envia `SYN` para o servidor (demora $\frac{1}{2}\text{ RTT} = d_{prop}$).
   * O servidor responde com `SYN-ACK` (demora $\frac{1}{2}\text{ RTT} = d_{prop}$).
   * Total do handshake: **1 RTT**.
2. **Pedido e resposta do HTML:**
   * O cliente envia o `ACK` final do handshake juntamente com o pedido `GET /index.html`.
   * O servidor recebe o pedido e devolve a resposta com o ficheiro HTML (demora 1 RTT de ida e volta, mais o tempo de transmissão física do ficheiro: $d_{trans,HTML} = 1\text{ ms}$).
3. **Descoberta das imagens:**
   * O browser lê o ficheiro HTML que acabou de chegar e descobre que a página referencia duas imagens (`img1.jpg` e `img2.jpg`).
4. **Obtenção da Imagem 1:**
   * Envia `GET /img1.jpg`. A resposta chega 1 RTT depois e demora $d_{trans,img} = 20\text{ ms}$ a passar pelo cabo.
5. **Obtenção da Imagem 2 (sem pipelining):**
   * Só quando a Imagem 1 acabou de ser recebida na totalidade é que o browser envia `GET /img2.jpg`. Demora outro 1 RTT de ida e volta mais $d_{trans,img} = 20\text{ ms}$ de transmissão.

#### (b) Tempo até ter a página e as imagens

Pelo diagrama temporal, o tempo total é a soma de todos os RTTs gastos e das transmissões dos ficheiros:
* **1 RTT** para abrir a conexão TCP;
* **1 RTT** para pedir e receber o início do HTML;
* **1 RTT** para pedir e receber a Imagem 1;
* **1 RTT** para pedir e receber a Imagem 2;
* Mais os tempos de transmissão dos dados úteis ($d_{trans,HTML}$ e $2 \times d_{trans,img}$).

$$d_{total} = 4\,\text{RTT} + d_{trans,HTML} + 2\,d_{trans,img}$$
$$d_{total} = 4 \times (60\text{ ms}) + 1\text{ ms} + 2 \times (20\text{ ms}) = 240\text{ ms} + 1\text{ ms} + 40\text{ ms} = \mathbf{281\text{ ms}}$$

*(Em notação científica das potências de 10: $24\times 10^{-2}\text{ s} + 10^{-3}\text{ s} + 4\times 10^{-2}\text{ s} = 2{,}81\times 10^{-1}\text{ s} = 281\text{ ms}$).*

Fórmula geral da folha de revisão com $n=2$ imagens em HTTP persistente sem pipelining:
$$d_{total} = 2\,\text{RTT}\text{ (conexão + HTML)} + n\,\text{RTT}\text{ (uma por cada imagem)} + \sum d_{trans}$$

## Aula 2 --- HTTP à mão

### F3.1 --- HTTP à mão: persistente, hã? (Ficha 3, Ex. 1)

Testado em 2026-10-06 com o `nc` (o `telnet` do macOS não vem instalado;
o comportamento é o mesmo). Os números (tamanhos, cabeçalhos) são os do
`neverssl.com` nesse dia.

#### (a) Para que serve o telnet e o que tem o utilizador de fazer?

O `telnet` é o cliente do protocolo TELNET (RFC 854, porta 23): serve
para abrir uma **sessão de terminal numa máquina remota** e lá correr
comandos, como se estivéssemos sentados nela.

Para o usar basta escrever `telnet <máquina> [porta]`, por exemplo
`telnet neverssl.com 80`. Sem porta, liga à 23 (servidor TELNET). Depois
escreve-se o que se quer enviar e lê-se o que o servidor responde. Para
sair: `Ctrl+]` e depois `quit`.

Está praticamente obsoleto como terminal remoto porque **não cifra
nada**, *passwords* incluídas: quem capturar os pacotes lê tudo (como
lemos a *password* na captura FTP). Usa-se o **SSH**. Mas continua útil
como **cliente TCP genérico** para falar à mão com protocolos de texto
(HTTP, SMTP, POP3).

#### (b) Como funciona internamente?

1. Resolve o nome da máquina para um IP (DNS) e abre uma **conexão TCP**
   para esse IP e porta (é um cliente de *sockets*, como o `TCPClient`).
2. Entra num ciclo: o que o utilizador escreve no teclado é **enviado
   pela socket** (no fim de cada linha envia CR LF); o que chega da
   socket é **escrito no ecrã**.
3. Na porta 23 também negoceia opções do terminal (eco, tamanho da
   janela) com comandos especiais começados pelo byte 255 (`IAC`).
   Noutras portas é só um "tubo" de bytes de texto.
4. Quando o servidor fecha a conexão, o `telnet` mostra
   `Connection closed by foreign host.` e termina.

#### (c) Os pedidos ao neverssl.com: o que acontece

**Sessão 1** (`telnet neverssl.com 80`), pedido HTTP/1.0 sem `Host:`:

```
GET / HTTP/1.0
User-Agent: Mozilla/5.0
                                 <- linha vazia: fim do pedido
HTTP/1.1 200 OK
Server: Apache/2.4.68 ()
Upgrade: h2,h2c
Connection: Upgrade, close
Content-Length: 3961
Content-Type: text/html; charset=UTF-8

<!DOCTYPE html> ... (3961 bytes de HTML)
Connection closed by foreign host.
```

O servidor responde **e fecha logo a conexão** (`Connection: close`).
Para o pedido seguinte é preciso um `telnet` novo. (A resposta diz
`HTTP/1.1` porque o servidor indica a versão mais alta que fala, mas
trata o pedido com as regras do 1.0. O `Upgrade: h2,h2c` é o servidor a
oferecer HTTP/2.)

**Sessão 2** (outro `telnet neverssl.com 80`), os 4 pedidos HTTP/1.1,
um a seguir ao outro:

| Pedido | Resposta | O que acontece à conexão |
|:--|:--|:----------|
| `GET /` | `200 OK`, 3961 bytes | **fica aberta** |
| `GET /` | `200 OK`, 3961 bytes | fica aberta (mesma conexão) |
| `GET /favicon.ico` | `200 OK`, 124 bytes, `image/vnd.microsoft.icon` | fica aberta |
| `GET /` + `Connection: close` | `200 OK`, 3961 bytes, `Connection: close` | o servidor **fecha** |

Os três primeiros pedidos HTTP/1.1 passam **pela mesma conexão TCP**: o
servidor responde e fica à espera. O `telnet` não sabe onde acaba cada
resposta, mas o browser saberia pelo `Content-Length`. Só o último, com
`Connection: close`, leva o servidor a fechar.

Dois cuidados práticos:

- Se demorares muito a escrever o pedido seguinte, o servidor fecha a
  conexão por *timeout* (o Apache usa 5 s por omissão). Escreve os
  pedidos num editor e **cola-os**.
- Sem a linha `Host:` num pedido HTTP/1.1, a resposta é
  `400 Bad Request` (o `Host:` é obrigatório no 1.1).

#### (d) Persistência e *pipelining*, e o que se viu

- **Conexão persistente**: a conexão TCP **fica aberta** depois de uma
  resposta e serve para os pedidos seguintes. Poupa-se 1 RTT (o
  estabelecimento da conexão) por objeto e o *overhead* de abrir e
  fechar conexões. No HTTP/1.1 é o comportamento por omissão; para
  fechar, envia-se `Connection: close`.
- ***Pipelining***: numa conexão persistente, o cliente envia **vários
  pedidos seguidos, sem esperar pelas respostas**. As respostas vêm
  **pela mesma ordem** dos pedidos. Em vez de 1 RTT por objeto, gasta-se
  ~1 RTT para todos.

**Comentário dos resultados:**

- HTTP/1.0: **não persistente**, uma conexão por objeto: o servidor
  fechou depois da primeira resposta.
- HTTP/1.1: **persistente**: três respostas na mesma conexão, que só
  fechou com o `Connection: close`.
- Nesta experiência **não houve *pipelining***, porque cada pedido só foi
  escrito depois de ver a resposta anterior (é persistente **sem**
  *pipelining*: 1 RTT por pedido).
- Para ver o *pipelining*: colar três pedidos de uma vez (`GET /`,
  `GET /favicon.ico`, `GET /` com `Connection: close`). No teste, as
  **três respostas chegaram seguidas, pela ordem dos pedidos**, cerca de
  0,27 s depois do envio, o tempo de **um** pedido e não de três. Depois
  da terceira, o servidor fechou.

## Aula 2 --- Capturas HTTP

### F3.7a --- Captura HTTP (Ficha 3, Ex. 7a)

Captura `Teoricas/Aula_03_captura_http.cap` (a `Cap2-http.cap` do
Moodle): browser 192.168.50.41, servidor 10.0.0.251 (`www.dcc.fc.up.pt`),
porta 80. Os números de pacote são os do Wireshark (contados a partir de
1), tirados da própria captura.

#### (i) Método e URL de todos os pedidos

Todos usam o método **GET** (o browser só vai buscar objetos; não envia
formulários):

| Pacote | Conexão (porta do cliente) | Pedido | Resposta |
|:-:|:-:|:---------------------|:--|
| 4 | 55956 | `GET /~rprior/` | 200 OK (o HTML) |
| 8 | 55956 | `GET /~rprior/homepage/rprior.css` | 200 OK |
| 13 | 55956 | `GET /~rprior/homepage/img/portonight.jpg` | 200 OK |
| 19 | 55957 | `GET /~rprior/homepage/img/rprior.jpg` | 200 OK |
| 96 | 55956 | `GET /favicon.ico` | 404 Not Found |
| 99 | 55956 | `GET /favicon.ico` | 404 Not Found |

Os URLs completos são `http://www.dcc.fc.up.pt` + o caminho (o nome vem
do cabeçalho `Host:`). O HTML é o primeiro; os outros são objetos que ele
referencia (o CSS e as duas imagens), mais o ícone que o browser pede
sempre sozinho.

#### (ii) Conexões simultâneas e persistência

Pacotes **SYN** (aberturas): 1 (porta 55956), 14 (55957) e 15 (55958),
os dois últimos aos 28 ms, quando o browser já tinha o HTML e viu que
precisava das imagens. Pacotes **FIN** (fechos): 102, 103 e 104, os três
do **browser**, aos 1,94 s.

Logo, durante quase toda a sessão estiveram abertas **3 conexões
simultâneas**. Só duas levaram pedidos: a 55956 (5 pedidos) e a 55957
(1); a 55958 abriu e fechou vazia.

**São persistentes**:

- a 55956 transporta **5 pedidos** antes do FIN; com HTTP não
  persistente seria uma conexão por objeto;
- nenhuma conexão fecha depois de uma resposta: fecham todas **juntas**,
  quase 2 s depois do último pedido, quando o browser as liberta;
- os cabeçalhos confirmam: o browser envia `Connection: keep-alive` e o
  servidor responde `Connection: Keep-Alive` com
  `Keep-Alive: timeout=5, max=100`, e o `max` desce de resposta em
  resposta na 55956 (100, 99, 98, 97, 96).

Não há *pipelining*: na 55956 cada pedido só sai depois de a resposta
anterior começar a chegar (o CSS no pacote 8, depois do HTML no 6). Para
ter paralelismo, o browser abriu **conexões paralelas** em vez disso.

### F3.7d --- A tua captura de neverssl.com (Ficha 3, Ex. 7d)

Resposta-modelo: o resultado exato depende do browser e da hora. Isto é
o que se espera, verificado com pedidos feitos à mão ao `neverssl.com`.

#### (i) O que observas?

1. Um **pedido DNS** não aparece (o filtro é `port 80`, e o DNS usa a
   porta 53). Aparece logo o **SYN** do browser para a porta 80 de
   `neverssl.com`.
2. `GET /` com `Host: neverssl.com` $\to$ `200 OK` com uma página HTML de
   ~4 KB. A página tem um *script* que inventa um subdomínio aleatório
   (ex.: `coolcalmzen.neverssl.com`) e manda o browser para
   `http://<aleatório>.neverssl.com/online`.
3. Nova conexão TCP (é outro nome, e o browser não reaproveita conexões
   entre nomes diferentes) e `GET /online` $\to$ **`301 Moved
   Permanently`** com `Location: .../online/` (falta a barra final).
4. `GET /online/` $\to$ `200 OK`, a página final.
5. Pedidos de `/favicon.ico`.

O subdomínio aleatório serve para **fugir às *caches***: como o nome é
sempre novo, nenhuma *cache* (do browser, de um *proxy*) tem a página, e
o pedido chega mesmo ao servidor. Também se vê que, como o site é HTTP
(sem TLS), tudo vai **em texto claro**: o Wireshark mostra os pedidos e o
HTML inteiro.

#### (ii) Foram usadas conexões persistentes?

**Sim** (com um browser atual). Provas a procurar na captura:

- o browser envia `Connection: keep-alive` e a conexão **não fecha**
  depois da resposta (não há FIN logo a seguir);
- na conexão para o subdomínio, o pedido a seguir ao `301` (`GET
  /online/`) e o do `favicon.ico` vão **na mesma conexão** (mesma porta do
  cliente);
- os FIN só aparecem segundos depois, quando o browser ou o servidor
  fecham a conexão parada.

Pode haver mais do que uma conexão para o mesmo nome (os browsers abrem
conexões paralelas), e a primeira, para `neverssl.com`, fica parada
depois de o *script* mudar de página.

### C2.2 --- Captura HTTP: códigos e RTT (exercício inventado)

Mesma captura do F3.7a.

#### (a) Que códigos de estado aparecem?

- **200 OK**: para `/~rprior/`, `rprior.css`, `portonight.jpg` e
  `rprior.jpg`.
- **404 Not Found**: para `/favicon.ico` (as duas vezes). O browser pede
  sozinho o ícone do site, que não existe neste servidor.

Nota adicional: as respostas 200 dizem o tamanho com `Content-Length`
(por exemplo, 2144 bytes para o HTML e 86 267 para `portonight.jpg`). As
404 usam `Transfer-Encoding: chunked`: o corpo vai em pedaços, cada um
precedido do seu tamanho, e acaba num pedaço de tamanho 0. É outra forma
de o browser saber onde acaba a resposta sem saber o tamanho à partida.

#### (b) RTT a partir do *handshake* TCP

O cliente envia o primeiro pacote do *handshake* (SYN) no instante 0 e a
resposta do servidor (SYN-ACK) chega aos **0,24 ms**. O RTT é cerca de
**0,24 ms**.

Isso é muito pouco: à velocidade de $2\times10^8$ m/s, 0,24 ms de ida e
volta são no máximo 24 km de fibra para cada lado, e na prática menos
(há processamento). O cliente está na **mesma rede local** (ou muito
perto) do servidor. Os endereços confirmam: 192.168.x.x e 10.x.x.x são
endereços **privados**, de redes internas (aqui, dentro do DCC).

## Aula 2 --- Web caches: o proxy do Paulo

### F3.2 --- À volta do HTTP: o proxy do Paulo (Ficha 3, Ex. 2)

Notação: $n$ objetos de tamanho $m$; $R = 10$ Mbps; $T = m/R$ o tempo
de transmissão de um objeto; $\text{RTT}$ o tempo de ida e volta entre
o computador do Paulo e o servidor. Como no resumo: um objeto em HTTP
não persistente custa $2\,\text{RTT} + T$; numa conexão persistente já
aberta, sem *pipelining*, custa $\text{RTT} + T$.

#### (a) Ganho com o proxy HTTP/1.1 no próprio computador

**Antes (browser HTTP/1.0 direto ao servidor).** Não persistente, um
objeto de cada vez:
$$t_{\text{antes}} = n\,(2\,\text{RTT} + T)$$

**Depois (browser $\to$ proxy local $\to$ servidor).** O caminho
parte-se em dois troços:

- **browser $\leftrightarrow$ *proxy***: continua HTTP/1.0 (uma conexão
  por objeto), mas é dentro da mesma máquina: RTT $\approx 0$ e cópia
  instantânea. Custa $\approx 0$.
- ***proxy* $\leftrightarrow$ servidor**: HTTP/1.1 com **uma conexão
  persistente**, aberta uma só vez. Mas **sem *pipelining***: o browser
  só pede o objeto $k+1$ depois de receber o $k$, por isso o *proxy* só
  conhece um pedido de cada vez e não tem nada para "adiantar".

Tempo no troço *proxy*--servidor:

- 1.º objeto: 1 RTT (conexão) + 1 RTT (pedido) + $T$ $= 2\,\text{RTT} + T$;
- cada um dos outros $n-1$: 1 RTT (pedido) + $T$.

$$t_{\text{depois}} = (2\,\text{RTT} + T) + (n-1)(\text{RTT} + T) = (n+1)\,\text{RTT} + nT$$

**Ganho:**
$$t_{\text{antes}} - t_{\text{depois}} = 2n\,\text{RTT} + nT - (n+1)\,\text{RTT} - nT = \mathbf{(n-1)\,RTT}$$

Poupa-se o estabelecimento da conexão TCP em todos os objetos menos o
primeiro. O tempo de transmissão $nT$ fica igual (os bits têm de passar
na mesma), por isso o ganho **relativo** é grande para muitos objetos
pequenos (RTT domina) e pequeno para poucos objetos grandes ($T$
domina).

Exemplo numérico: $n = 10$, $m = 100$ kB, RTT = 100 ms.
$T = 800\,000 / 10^7 = 0{,}08$ s.
Antes: $10 \times (0{,}2 + 0{,}08) = 2{,}8$ s. Depois:
$11 \times 0{,}1 + 10 \times 0{,}08 = 1{,}1 + 0{,}8 = 1{,}9$ s. Ganho
$0{,}9$ s $= 9 \times 0{,}1$ s (32%).

#### (b) E com o proxy noutro computador (RTT browser--proxy grande)?

**Faz diferença, e pode deixar de compensar.** Seja $\text{RTT}_p$ o RTT
browser--*proxy* (e suponha-se que o *proxy*--servidor continua a ter
RTT $\approx$ RTT). O troço browser--*proxy* continua HTTP/1.0 **não
persistente**, e agora custa a sério, em **cada** objeto:

- $2\,\text{RTT}_p$ (conexão + pedido/resposta até ao *proxy*);
- e, se o *proxy* só reencaminha o objeto depois de o ter todo
  (*store-and-forward*), mais um $T$ para o enviar ao browser.

$$t_{\text{depois}} = n\,(2\,\text{RTT}_p + T) + (n+1)\,\text{RTT} + nT$$
$$\text{ganho} = (n-1)\,\text{RTT} - 2n\,\text{RTT}_p - nT$$

(Se o *proxy* for reencaminhando os bytes à medida que chegam, o termo
$-nT$ desaparece: ganho $= (n-1)\,\text{RTT} - 2n\,\text{RTT}_p$.)

O *proxy* só ganha alguma coisa se $2n\,\text{RTT}_p < (n-1)\,\text{RTT}$,
isto é, $\text{RTT}_p$ menor do que cerca de **metade do RTT** até ao
servidor. Com o *proxy* longe, cada objeto paga dois RTT até ele, o que
come (ou ultrapassa) o RTT poupado no outro troço: o ganho fica
**negativo**.

**Comparação com as respostas oficiais** (`Semana_3/respostas-2.pdf`): o
oficial dá $2n\,\text{RTT}_{BP} + (n+1)\,\text{RTT}_{PS} + nT$, que é a
nossa variante em que o *proxy* reencaminha à medida que recebe ($T$
contado uma vez só). Assume que a ligação browser--*proxy* não é mais
lenta do que a *proxy*--servidor. Conclusão igual: com o *proxy* na rede
local ($\text{RTT}_{BP} \ll \text{RTT}_{PS}$) poupa-se quase tanto como
na (a); com $\text{RTT}_{BP}$ parecido com $\text{RTT}_{PS}$ demora mais
do que sem *proxy*. As alíneas (a) e (c) dão o mesmo que o oficial:
$(n-1)\,\text{RTT}$ e $(2n-2)\,\text{RTT}$.

#### (c) Ganho se o browser suportasse HTTP/1.1 (proxy local)

Com HTTP/1.1 o browser usa uma conexão **persistente com *pipelining***:
envia os $n$ pedidos seguidos ao *proxy* (custo $\approx 0$, é local), e
o *proxy* também os envia seguidos ao servidor. Supondo que o browser já
conhece os $n$ objetos:

- 1 RTT para abrir a conexão *proxy*--servidor;
- 1 RTT até a primeira resposta começar a chegar (os $n$ pedidos seguem
  juntos);
- as $n$ respostas chegam umas atrás das outras: $nT$.

$$t = 2\,\text{RTT} + nT$$
$$\text{ganho} = n\,(2\,\text{RTT} + T) - (2\,\text{RTT} + nT) = \mathbf{2\,(n-1)\,RTT}$$

O dobro do ganho da alínea (a). No exemplo numérico: $0{,}2 + 0{,}8 =
1{,}0$ s, contra 2,8 s (ganho 1,8 s).

Duas observações:

- Aqui o *proxy* **já não serve para nada**: sem *cache* nem
  compressão, o browser HTTP/1.1 ligado diretamente ao servidor teria o
  mesmo $2\,\text{RTT} + nT$. O *proxy* só ajudava porque "traduzia"
  HTTP/1.0 em conexões persistentes.
- Se os $n$ objetos forem uma página (1 HTML + $n-1$ objetos
  referenciados), o browser só conhece os outros depois de ter o HTML:
  $t = 2\,\text{RTT} + T + \text{RTT} + (n-1)T = 3\,\text{RTT} + nT$, e o
  ganho é $(2n-3)\,\text{RTT}$ (como no exemplo dos 3 RTT do resumo).

## Aula 2 --- FTP

### F3.7b --- Captura FTP (Ficha 3, Ex. 7b)

Captura `Teoricas/Aula_03_captura_ftp.cap` (a `Cap2-ftp.cap` do
Moodle): cliente 192.168.1.110, servidor 193.137.24.17 (vsFTPd). Os
números de pacote são os do Wireshark, tirados da captura.

#### (i) Todos os comandos enviados ao servidor, e para que serve cada um

Todos vão na conexão de **controlo** (porta 21), em texto:

| Pacote | Comando | Para que serve | Resposta |
|:-:|:----------|:--------------------|:----------|
| 6 | `USER anonymous` | indica o utilizador | `331 Please specify the password.` |
| 10 | `PASS someone@the.inter.net` | indica a *password* | `230 Login successful.` |
| 12 | `SYST` | pergunta o tipo de sistema do servidor | `215 UNIX Type: L8` |
| 15 | `CWD /pub/Linux` | muda o diretório corrente | `250 Directory successfully changed.` |
| 18 | `TYPE I` | modo binário (byte a byte) | `200 Switching to Binary mode.` |
| 20 | `PORT 192,168,1,110,196,43` | diz ao servidor o IP e a porta do cliente para a conexão de dados | `200 PORT command successful. Consider using PASV.` |
| 22 | `RETR iperf-1.7.0-source.tar.gz` | pede o ficheiro | `150 Opening BINARY mode data connection ... (182773 bytes).` e, no fim, `226 File send OK.` |
| 255 | `QUIT` | termina a sessão | `221 Goodbye.` |

Antes do `USER`, o servidor apresentou-se com `220 (vsFTPd 2.0.5)`
(pacote 4, logo depois do *handshake* TCP). `CWD` e `TYPE` mostram o
**estado** que o servidor FTP guarda (diretório corrente, modo), ao
contrário do HTTP.

#### (ii) Em que pacote é pedido o estabelecimento da conexão de dados?

No **pacote 20**, o comando **`PORT 192,168,1,110,196,43`**. É aí que o
cliente diz onde está à espera da conexão de dados:

- IP: os 4 primeiros números, **192.168.1.110** (o próprio cliente);
- porta: $196 \times 256 + 43 = 50176 + 43 = \mathbf{50219}$.

O `RETR` (pacote 22) é o que faz o servidor **abrir** de facto essa
conexão: o SYN do servidor, da porta 20 para a 50219, é o **pacote 23**.

Um pormenor: esse primeiro SYN (aos 43,0 s) **não teve resposta**; o
servidor repetiu-o 3 s depois (pacote 25), e só então o cliente
respondeu (SYN-ACK, pacote 26). O cliente tem um endereço privado, atrás
de um *router* com NAT, e no modo ativo é o **servidor** que tem de
chegar ao cliente, o que é frágil. Por isso o servidor sugere
"Consider using PASV" (no modo passivo é o cliente que abre a conexão de
dados).

#### (iii) Portas do servidor: controlo e dados

- **Controlo: porta 21** do servidor (da porta 50212 do cliente). Aberta
  pelo **cliente** (SYN no pacote 1), dura a sessão toda.
- **Dados: porta 20** do servidor (para a porta 50219 do cliente).
  Aberta pelo **servidor** (SYN no pacote 23, repetido no 25), só para
  este ficheiro; fecha no fim da transferência (FIN do servidor, que vai
  junto com o último bloco de dados).

É o FTP **ativo** dos slides: controlo *out of band*, numa conexão
separada dos dados.

### C2.3 --- Captura FTP: segurança e débito (exercício inventado)

Mesma captura do F3.7b.

#### (a) Utilizador e *password*; o que mostra sobre a segurança

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

#### (b) Tamanho do ficheiro e débito médio

- **Tamanho: 182 773 bytes** (diz o `150`, e é também a soma dos dados
  que passam na conexão de dados).
- Primeiro pacote com dados: aos **46,0736 s**; último: aos **46,2901 s**.
  Duração: $46{,}2901 - 46{,}0736 = 0{,}2165$ s.

$$\text{débito} = \frac{182\,773 \times 8\text{ bits}}{0{,}2165\text{ s}} = \frac{1\,462\,184}{0{,}2165} \approx \mathbf{6{,}75\text{ Mbit/s}}$$

## Aula 2 --- Correio eletrónico

### F3.3 --- Correio direto (Ficha 3, Ex. 3)

#### Resposta

Resposta-modelo. As linhas `C:` são o que escreves; as `S:` são o que o
servidor responde. O início (até ao `EHLO`) foi testado em 2026-10-06;
as respostas a partir do `MAIL FROM` são as típicas do servidor (Postfix
com códigos estendidos, como `2.1.0`). Troca `upXXXXXXXXX` pelo teu
endereço.

```
$ gnutls-cli smtp.fc.up.pt -p 25 --starttls-proto=smtp --crlf
  (... certificado e handshake TLS: o gnutls-cli já fez EHLO + STARTTLS)
C: EHLO portatil
S: 250-smtp.fc.up.pt
S: 250-PIPELINING
S: 250-SIZE 35840000
S: 250-AUTH LOGIN PLAIN
S: 250-ENHANCEDSTATUSCODES
S: 250-8BITMIME
S: 250 DSN
C: MAIL FROM:<bugsbunny@warnerbros.com>
S: 250 2.1.0 Ok
C: RCPT TO:<upXXXXXXXXX@fc.up.pt>
S: 250 2.1.5 Ok
C: DATA
S: 354 End data with <CR><LF>.<CR><LF>
C: From: Bugs Bunny <bugsbunny@warnerbros.com>
C: To: upXXXXXXXXX@fc.up.pt
C: Subject: Eh... What's up, doc?
C:
C: Did you know email is insecure?
C: .
S: 250 2.0.0 Ok: queued as ...
C: QUIT
S: 221 2.0.0 Bye
```

**Porque é assim:**

- **`EHLO` outra vez**: o `gnutls-cli` fez o `EHLO` e o `STARTTLS` em
  claro; depois do TLS o diálogo recomeça. Vê-se na lista: já não aparece
  `STARTTLS` (já estamos em TLS) e aparece `AUTH` (o servidor só deixa
  autenticar dentro do TLS).
- **Envelope vs. cabeçalhos**: o remetente aparece **duas vezes**. O
  `MAIL FROM` é o **envelope** (para onde voltam os erros de entrega); o
  `From:` vai **dentro** do `DATA` e é o que o leitor de email mostra.
  O destinatário igual: `RCPT TO` (envelope, é o que decide a entrega,
  um por destinatário) e `To:` (só para mostrar).
- O **assunto** é um cabeçalho (`Subject:`), não um comando SMTP.
- A **linha vazia** separa os cabeçalhos do corpo; a linha **só com
  `.`** acaba a mensagem.
- `--crlf`: o SMTP exige CR LF no fim de cada linha.

**Verificar que funcionou:** a mensagem aparece na caixa de correio da
FCUP (muitas vezes no **spam**), "enviada" por Bugs Bunny. Abre o
código-fonte da mensagem: os cabeçalhos `Received:` mostram por onde ela
passou, **incluindo o teu IP**: o remetente é falso, mas o envio não é
anónimo. É provável aparecer também um resultado de **SPF** a falhar
(`warnerbros.com` não autoriza o servidor da FCUP a enviar por ele).

**Possíveis problemas:**

- `554 Relay access denied` no `RCPT TO`: o servidor só entrega sem
  autenticação a endereços **dos domínios dele**. Usa o endereço da
  FCUP que te foi atribuído.
- Se o servidor fechar a conexão a meio, foi *timeout*: escreve as
  linhas num editor e cola-as.

**A lição** (o corpo da mensagem): o SMTP **não verifica o remetente**.
Qualquer pessoa escreve o `MAIL FROM` e o `From:` que quiser. O TLS só
cifra a conversa; não prova quem envia.

### F3.7c --- Captura SMTP (Ficha 3, Ex. 7c)

#### Resposta

Captura `Teoricas/Aula_03_captura_smtp.cap` (a `Cap2-smtp.cap`):
cliente Thunderbird 10.0.0.92 (porta 3152), servidor
`smtp.dcc.fc.up.pt` 10.0.0.10 (porta 25). Pacotes 1--3: *handshake*
TCP. Depois:

| Pacote | Sentido | Comando / resposta | Significado |
|:-:|:-:|:--------------|:--------------------|
| 4 | S$\to$C | `220 smtp.dcc.fc.up.pt ESMTP Postfix` | o servidor apresenta-se |
| 5 | C$\to$S | `EHLO [10.0.0.92]` | o cliente apresenta-se (SMTP estendido) |
| 7 | S$\to$C | `250-smtp.dcc.fc.up.pt`, `250-PIPELINING`, ..., `250 8BITMIME` | aceita e lista as extensões |
| 8 | C$\to$S | `MAIL FROM:<rprior@dcc.fc.up.pt> SIZE=639` | remetente (e tamanho) |
| 9 | S$\to$C | `250 Ok` | remetente aceite |
| 10 | C$\to$S | `RCPT TO:<rcprior@fc.up.pt>` | destinatário |
| 11 | S$\to$C | `250 Ok` | destinatário aceite |
| 12 | C$\to$S | `DATA` | "a seguir vai a mensagem" |
| 13 | S$\to$C | `354 End data with <CR><LF>.<CR><LF>` | pode enviar |
| 14 | C$\to$S | a mensagem: cabeçalhos, linha vazia, corpo | (639 bytes) |
| 16 | C$\to$S | `.` | fim da mensagem |
| 18 | S$\to$C | `250 Ok: queued as 588D7E837A` | aceite, na fila de entrega |
| 19 | C$\to$S | `QUIT` | terminar |
| 20 | S$\to$C | `221 Bye` | o servidor fecha (FIN no pacote 21) |

Os pacotes que faltam (6, 15, 17, 22--24) são só confirmações (ACK) e o
fecho do TCP, sem dados SMTP. Repara que as respostas seguem a regra
"código + descrição", e que o `250-` com hífen quer dizer "há mais
linhas" (o último é `250 ` com espaço).

### C2.4 --- POP3 com dois aparelhos (exercício inventado)

#### Resposta

**1. O que acontece com o POP3 no modo "transfere e apaga" (*download-and-delete*):**
* Quando o utilizador abre o correio no **portátil**, o cliente POP3 transfere todas as mensagens novas para o disco local do portátil e envia o comando `DELE` ao servidor para **apagar essas mensagens da caixa de correio central**.
* Quando o utilizador liga o **telemóvel** mais tarde, a caixa de correio no servidor já está vazia: o telemóvel **não vê nenhuma dessas mensagens**, vendo apenas os emails que tenham chegado entretanto.
* O correio fica irremediavelmente fragmentado: mensagens descarregadas no portátil ficam presas no portátil; mensagens descarregadas no telemóvel ficam presas no telemóvel.
* *Nota adicional sobre o modo alternativo do POP3:* Mesmo configurando o POP3 em modo "transfere e mantém" (*download-and-keep*), o POP3 é um protocolo **sem estado (*stateless*) entre sessões**. Isto significa que:
  * Não sincroniza pastas remotas (não cria pastas "Trabalho", "Pessoal" no servidor).
  * Não sincroniza o estado das mensagens (se leres ou arquivares um email no portátil, ele continua a aparecer como novo/não lido no telemóvel).

**2. Qual o protocolo que resolve o problema, e porquê?**
* O protocolo que resolve este problema é o **IMAP (*Internet Message Access Protocol*)**.
* **Porquê o IMAP?**
  1. **Armazenamento centralizado no servidor:** todas as mensagens residem permanentemente no servidor de correio. Os dispositivos (portátil, telemóvel, tablet, Webmail) atuam apenas como interfaces de visualização remota em tempo real. Ambos os aparelhos veem exatamente a mesma caixa de correio completa.
  2. **Protocolo com estado (*stateful*):** o IMAP sincroniza o estado de cada mensagem entre múltiplos dispositivos:
     * Sinalizadores de mensagens (*flags* de *lida/não lida*, *respondida*, *com estrela/sinalizada*) são mantidos no servidor e refletem-se instantaneamente em todos os aparelhos.
     * Gestão de pastas remotas: criar, renomear ou mover emails entre pastas (ex.: Caixa de Entrada $\to$ Arquivo) mantém a mesma organização exata em todos os aparelhos.

## Aula 2 --- DNS: resolução e registos

### C2.5 --- DNS (exercício inventado)

**Conceitos e Funcionamento da Hierarquia DNS:**
* **Consulta Recursiva**: o cliente (`khedo`) passa todo o trabalho de resolução para o Servidor DNS Local e aguarda que este lhe devolva a resposta final (o endereço IP).
* **Consulta Iterativa**: o Servidor DNS Local pergunta a cada nível da hierarquia por sua conta. Se o servidor contactado não souber a resposta final, devolve uma referência apontando para o servidor do nível seguinte.
* **Os 4 níveis em jogo**: Cliente $\leftrightarrow$ Servidor DNS Local $\leftrightarrow$ Servidor Raiz (Root) $\leftrightarrow$ Servidor de Topo (TLD `.edu`) $\leftrightarrow$ Servidor com Autoridade (`mit.edu`).

#### (a) Quantas mensagens DNS em cada caso?

**Detalhamento de todas as 8 mensagens no caso normal (caches vazias):**
1. `khedo` $\to$ Servidor DNS Local: pedido recursivo ("Qual o IP de `www.mit.edu`?")
2. Servidor DNS Local $\to$ Servidor Raiz: pedido iterativo ("Qual o IP de `www.mit.edu`?")
3. Servidor Raiz $\to$ Servidor DNS Local: resposta de referência com os registos NS do TLD `edu` (e os seus respetivos IPs)
4. Servidor DNS Local $\to$ Servidor TLD `edu`: pedido iterativo ("Qual o IP de `www.mit.edu`?")
5. Servidor TLD `edu` $\to$ Servidor DNS Local: resposta de referência com os registos NS do servidor com autoridade de `mit.edu`
6. Servidor DNS Local $\to$ Servidor com Autoridade de `mit.edu`: pedido iterativo ("Qual o IP de `www.mit.edu`?")
7. Servidor com Autoridade de `mit.edu` $\to$ Servidor DNS Local: resposta final contendo o registo A com o endereço IP de `www.mit.edu`
8. Servidor DNS Local $\to$ `khedo`: resposta final entregando o IP ao cliente

**Contagem de mensagens para cada uma das 3 situações do enunciado:**
* **(i) Caches vazias:**
  Ocorrem todas as mensagens numeradas de 1 a 8:
  $$4\text{ pares de (pedido + resposta)} = \mathbf{8\text{ mensagens}}$$
* **(ii) O servidor local já conhece em cache o servidor TLD `edu`:**
  O servidor local não precisa de contactar a Raiz (poupam-se as mensagens 2 e 3). São trocadas as mensagens 1, 4, 5, 6, 7 e 8:
  $$8 - 2 = \mathbf{6\text{ mensagens}}$$
  *(Este é o caso mais frequente na navegação do dia a dia, pois os servidores TLD ficam em cache durante dias, aliviando quase todo o tráfego nos servidores de raiz).*
* **(iii) O servidor local já tem o IP de `www.mit.edu` em cache:**
  O servidor local responde imediatamente da sua memória cache sem enviar nenhuma mensagem para a Internet. Trocam-se apenas as mensagens 1 e 8:
  $$1\text{ par (pedido local + resposta)} = \mathbf{2\text{ mensagens}}$$

#### (b) Registos de `ferramentas.pt`

**Significado dos 4 tipos principais de Registos de Recurso (RR):**
O formato padrão de um RR é `(Nome, Valor, Tipo)`:
* **Tipo A (*Address*)**: mapeia um nome canónico de máquina para o seu endereço IPv4.
* **Tipo NS (*Name Server*)**: especifica o nome do servidor de nomes responsável/com autoridade por um domínio.
* **Tipo CNAME (*Canonical Name*)**: cria um pseudónimo (*alias*) que aponta para o nome canónico verdadeiro da máquina.
* **Tipo MX (*Mail Exchange*)**: especifica o servidor de correio eletrónico que recebe os emails enviados para o domínio.

**1. Registos configurados no Servidor TLD `pt`:**
*(Inseridos pela entidade gestora do `.pt` no ato do registo, para que a hierarquia mundial saiba a quem encaminhar perguntas sobre o domínio `ferramentas.pt`):*
* `(ferramentas.pt, dns1.ferramentas.pt, NS)`: indica qual é o servidor de nomes com autoridade para `ferramentas.pt`.
* `(dns1.ferramentas.pt, 192.0.2.53, A)`: registo de "cola" (*glue record*) fornecendo o IP do próprio servidor de nomes. *(Sem este registo A, quem recebesse o registo NS não saberia a que IP enviar as perguntas para contactar o `dns1`!).*

**2. Registos configurados no Servidor com Autoridade `dns1.ferramentas.pt`:**
*(A base de dados oficial mantida pelo administrador da Ferramentas Lda):*
* `(servidor1.ferramentas.pt, 192.0.2.10, A)`: endereço IP da máquina física onde reside o site web.
* `(www.ferramentas.pt, servidor1.ferramentas.pt, CNAME)`: cria o pseudónimo `www.ferramentas.pt` apontando para o nome canónico `servidor1.ferramentas.pt`.
* `(ferramentas.pt, mail.ferramentas.pt, MX)`: define que o correio para `@ferramentas.pt` deve ser entregue a `mail.ferramentas.pt`.
* `(mail.ferramentas.pt, 192.0.2.25, A)`: endereço IP do servidor de correio.
* *(Normalmente também inclui os registos NS e A do próprio servidor `dns1`, para consistência interna).*

*Como funciona a resolução prática:* Quando um browser pede o IP de `www.ferramentas.pt`, o servidor com autoridade consulta o registo CNAME, descobre que o nome canónico é `servidor1.ferramentas.pt`, consulta o registo A de `servidor1` e devolve o IP final `192.0.2.10`.

### C2.8 --- Setas DNS de www.publico.pt (exercício inventado)

#### (a) Caso habitual

![(a) o local é recursivo para o cliente e iterativo para fora; (b) se tudo fosse recursivo, cada servidor perguntava ao seguinte](figuras/sol_c28_dns.svg){width=100%}

São **8 mensagens**:

1. cliente → local: "A de `www.publico.pt`?" (pedido **recursivo**: quer
   a resposta final);
2. local → raiz: a mesma pergunta (**iterativo**);
3. raiz → local: não sabe, mas manda os **NS do TLD `pt`** (com os IPs);
4. local → TLD `pt`: a mesma pergunta;
5. TLD → local: os **NS de `publico.pt`**;
6. local → servidor com autoridade de `publico.pt`: a mesma pergunta;
7. autoridade → local: o **registo A** de `www.publico.pt`;
8. local → cliente: o registo A (e o local guarda tudo em *cache*).

#### (b) Tudo recursivo

Também **8 mensagens**, mas em cadeia: cada servidor pergunta ao
seguinte e espera pela resposta, e as respostas voltam pelo mesmo
caminho:

cliente → local (1), local → raiz (2), raiz → TLD `pt` (3), TLD →
autoridade (4); depois o registo A volta: autoridade → TLD (5), TLD →
raiz (6), raiz → local (7), local → cliente (8).

#### (c) Porque é que (b) não se usa

Em (b), a **raiz** e os **TLD** teriam de fazer o trabalho todo de cada
pergunta do mundo: guardar o estado de cada pedido pendente até a
resposta voltar. Recebem um volume enorme de pedidos, por isso só
respondem com **referências** (iterativo), que é rápido e não guarda
estado. Quem faz o trabalho é o servidor local, que serve poucos
clientes e aproveita a *cache*.

### M1.13 --- Resolução iterativa de www.jn.pt (Teste modelo 1, P. 13)

**Conceitos e termos de DNS que precisas de saber para este exercício:**
* **Resolução Iterativa**: o cliente pergunta a um nível da hierarquia; o servidor contactado responde *"eu não sei o IP final, mas contacta este outro servidor mais abaixo"* (devolve uma referência / delegação). O cliente é quem faz as perguntas todas, uma a uma. **Nenhuma seta liga dois servidores entre si.**
* **Hierarquia dos servidores contactados:**
  1. **Servidor de Raiz (*Root*)**: conhece os servidores dos TLDs (`.pt`, `.com`).
  2. **Servidor TLD (*Top-Level Domain*, `.pt`)**: conhece os servidores autoritários de cada domínio em Portugal (`jn.pt`, `up.pt`).
  3. **Servidor com Autoridade (*Authoritative Server*, `jn.pt`)**: guarda a base de dados oficial com os IPs do Jornal de Notícias.
* **Tipos de registos referidos:**
  * **Registo NS (*Name Server*)**: indica o nome do servidor de nomes com autoridade para um domínio.
  * **Registo A (*Address*)**: indica o endereço IPv4 definitivo da máquina pedida.
  * **Flag `aa` (*Authoritative Answer*)**: indica que a resposta vem do servidor oficial dono do domínio e não de uma cópia em cache.

#### Resposta

![Resolução iterativa: o cliente pergunta a cada nível e cada um devolve só a referência para o seguinte](figuras/sol_m1_dns_iterativo.svg){width=100%}

São **6 mensagens** (3 pares de pedido/resposta), sempre entre o cliente (na prática, o servidor de nomes local) e um servidor de cada vez:

1. **Mensagem 1 (Cliente $\to$ Servidor de Raiz):** "Qual é o registo A (endereço IP) de `www.jn.pt`?"
2. **Mensagem 2 (Servidor de Raiz $\to$ Cliente):** Não tem o IP, mas devolve os **registos NS do TLD `pt`** (e os respetivos IPs na secção adicional, para o cliente saber como contactar o TLD).
3. **Mensagem 3 (Cliente $\to$ Servidor TLD `pt`):** "Qual é o registo A de `www.jn.pt`?"
4. **Mensagem 4 (Servidor TLD `pt` $\to$ Cliente):** Não tem o IP da máquina, mas devolve os **registos NS do domínio `jn.pt`** (o servidor com autoridade).
5. **Mensagem 5 (Cliente $\to$ Servidor com Autoridade de `jn.pt`):** "Qual é o registo A de `www.jn.pt`?"
6. **Mensagem 6 (Servidor com Autoridade $\to$ Cliente):** Resposta conclusiva: devolve o **registo A com o IP final** de `www.jn.pt` (com a flag `aa = 1`).

*(No teste: desenha as 6 setas tal como na figura e escreve junto de cada uma o que leva — por exemplo: "1: GET A www.jn.pt", "2: NS pt", "3: GET A www.jn.pt", "4: NS jn.pt", "5: GET A www.jn.pt", "6: A IP-final").*

### C2.9 --- Email para um subdomínio (exercício inventado)

#### (a) Primeiro registo

O registo **MX** de `dei.uc.pt`. O SMTP não entrega ao IP do domínio, mas
ao **servidor de email** do domínio, e é o MX que o diz: por exemplo
`(dei.uc.pt, mail.dei.uc.pt, MX)`, com uma preferência (menor primeiro).
Depois falta o **A** de `mail.dei.uc.pt`, para ter o IP a que se liga o
SMTP; normalmente já vem na secção *additional* da resposta ao MX.

#### (b) Servidores e mensagens

O servidor local pergunta **iterativamente** a quatro servidores, cada um
com uma referência para o seguinte:

1. **raiz** → NS do TLD `pt`;
2. **TLD `pt`** → NS de `uc.pt`;
3. **servidor com autoridade de `uc.pt`** → NS de `dei.uc.pt` (a
   delegação do subdomínio);
4. **servidor com autoridade de `dei.uc.pt`** → o **MX** (com `aa`).

São $4 \times 2 = 8$ mensagens iterativas, mais **2** entre o servidor de
correio e o servidor local (pedido recursivo e resposta): **10**. Se o A
de `mail.dei.uc.pt` não vier na secção *additional*, há mais 2 (o local
já tem o NS de `dei.uc.pt` em *cache* e pergunta-lhe diretamente), e mais
2 entre o servidor de correio e o local.

## Aula 2 --- DNS: host e dig

### F3.4 --- dig da name? (Ficha 3, Ex. 4)

Saídas reais de 2026-10-06 (cortadas). Os IPs e TTL que te aparecerem
podem ser outros: os registos mudam, e o teu servidor local também. O
servidor local usado aqui foi o 1.1.1.1 (Cloudflare); na FCUP será o da
universidade.

#### (a) Com o host, o IP de www.dcc.fc.up.pt

```
$ host www.dcc.fc.up.pt
www.dcc.fc.up.pt is an alias for echo.dcc.fc.up.pt.
echo.dcc.fc.up.pt has address 193.136.39.92
```

O IP é **193.136.39.92**. O `host` mostra também que `www.dcc.fc.up.pt`
é um **pseudónimo** (registo CNAME) do nome canónico `echo.dcc.fc.up.pt`.

#### (b) Com o dig, o IP de www.google.com: secções e tipos de registo

```
$ dig www.google.com
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 29188
;; flags: qr rd ra; QUERY: 1, ANSWER: 8, AUTHORITY: 0, ADDITIONAL: 1
;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;www.google.com.            IN   A
;; ANSWER SECTION:
www.google.com.     228     IN   A    142.251.152.119
www.google.com.     228     IN   A    142.251.157.119
   (... mais 6 registos A, 142.251.15x.119)
;; Query time: 11 msec
;; SERVER: 1.1.1.1#53(1.1.1.1)
```

**Secções:**

- **HEADER**: o cabeçalho da mensagem DNS. `id` (o *identification*),
  `status: NOERROR` (correu bem), as *flags* `qr` (é resposta), `rd`
  (pedimos recursão), `ra` (o servidor faz recursão), e os 4
  contadores.
- **OPT PSEUDOSECTION**: não é um registo verdadeiro; é a extensão EDNS,
  onde cada lado diz o tamanho máximo de mensagem UDP que aceita (nota
  adicional, não está nos slides).
- **QUESTION**: a pergunta: nome `www.google.com`, classe `IN`, tipo `A`.
- **ANSWER**: os registos que respondem: **8 registos A**, cada um com
  um IP. O 228 é o TTL (segundos que faltam na *cache*).
- **AUTHORITY** e **ADDITIONAL**: vazias aqui (contadores 0, fora o
  OPT). O servidor local respondeu da *cache* e não juntou os NS da
  Google. Noutros servidores (como no exemplo `mit.edu` do resumo)
  aparecem os **NS** com autoridade e, na adicional, os **A** desses
  servidores.

**Tipos de registo:**

- **A**: nome $\to$ endereço IPv4. Aqui há 8: a Google tem muitos
  servidores para o mesmo nome (distribuição de carga).
- Os que podem aparecer noutras respostas: **NS** (domínio $\to$ servidor
  com autoridade, na secção de autoridade), **CNAME** (pseudónimo $\to$
  nome canónico, como na alínea a), **AAAA** (nome $\to$ IPv6, nas
  adicionais), **MX** (domínio $\to$ servidor de email).

#### (d) A mesma resolução com +trace

```
$ dig +trace www.dcc.fc.up.pt
.        517052  IN  NS  a.root-servers.net.   (... até m.root-servers.net)
;; Received 525 bytes from 1.1.1.1#53(1.1.1.1) in 14 ms

pt.      172800  IN  NS  c.dns.pt.             (... os 9 NS de pt)
;; Received 943 bytes from 2001:dc3::35#53(m.root-servers.net) in 34 ms

up.pt.   7200    IN  NS  ns1.up.pt.            (... os 5 NS de up.pt)
;; Received 507 bytes from 2001:690:a80:4001::100#53(g.dns.pt) in 15 ms

www.dcc.fc.up.pt.  300  IN  CNAME  echo.dcc.fc.up.pt.
echo.dcc.fc.up.pt. 600  IN  A      193.136.39.92
;; Received 1583 bytes from 193.136.2.228#53(ns02.fccn.pt) in 19 ms
```

Bate certo com os passos da alínea (c), com mais um passo no início:

1. O `dig` pede ao **servidor local** a lista dos servidores de raiz
   (`. NS`), para saber por onde começar.
2. Pergunta a uma raiz (aqui `m.root-servers.net`) $\to$ referência para
   os NS de `pt`.
3. Pergunta a um servidor de `pt` (`g.dns.pt`) $\to$ referência para os
   NS de `up.pt`.
4. Pergunta a um servidor de `up.pt` (`ns02.fccn.pt`) $\to$ a resposta:
   CNAME + A, IP **193.136.39.92**.

Diferenças em relação à (c): o `+trace` **escolhe sozinho** um servidor
de cada nível (aqui `m`, `g.dns.pt`, `ns02.fccn.pt`, outros que não os
da (c), e às vezes por IPv6), e usa sempre pedidos **iterativos**. O
resultado é o mesmo.

#### (e) Lista de IPs de www.jn.pt

```
$ dig www.jn.pt +noall +answer
www.jn.pt.                    228  IN  CNAME  dq9uigovq8yc3.cloudfront.net.
dq9uigovq8yc3.cloudfront.net.  60  IN  A      3.160.132.5
dq9uigovq8yc3.cloudfront.net.  60  IN  A      3.160.132.106
dq9uigovq8yc3.cloudfront.net.  60  IN  A      3.160.132.90
dq9uigovq8yc3.cloudfront.net.  60  IN  A      3.160.132.117
```

`www.jn.pt` é um **CNAME** para um nome da **CloudFront** (a rede de
distribuição de conteúdos da Amazon), e esse nome tem **4 endereços**:
3.160.132.5, .106, .90 e .117. O TTL dos A é só 60 s: a CDN quer poder
mudar os endereços depressa.

#### (f) Repetir e comparar a ordem; para que serve a rotação?

Duas perguntas seguidas que caíram na mesma *cache* deram:

```
1.ª vez: 3.160.132.117  3.160.132.5    3.160.132.106  3.160.132.90
2.ª vez: 3.160.132.5    3.160.132.106  3.160.132.90   3.160.132.117
```

São os **mesmos 4 endereços, por outra ordem**: o primeiro passou para
o fim e os outros subiram uma posição (*round robin*). (Noutras perguntas,
vindas de outra *cache*, até apareceram outros 4 endereços, 52.222.132.x:
a CDN também escolhe réplicas conforme a localização e a hora.)

**Objetivo: distribuição de carga.** Cada endereço é uma réplica do
servidor. Os clientes usam normalmente o **primeiro** endereço da lista;
se a ordem roda de resposta para resposta, clientes diferentes recebem
primeiros diferentes e os pedidos repartem-se pelas réplicas. É o
serviço "distribuição de carga" do DNS dos slides. Se uma réplica
falhar, o cliente ainda tem as outras na lista.

#### (g) O servidor de email de fc.up.pt e o seu IP

O servidor de email de um domínio é o registo **MX**:

```
$ dig fc.up.pt MX +noall +answer
fc.up.pt.   3600  IN  MX  10 mx01.up.pt.
fc.up.pt.   3600  IN  MX  10 mx02.up.pt.
   (... até mx06.up.pt, todos com preferência 10)
$ dig mx01.up.pt +noall +answer
mx01.up.pt. 3600  IN  A   193.137.55.24
```

A FCUP tem **6 servidores de email**, `mx01.up.pt` a `mx06.up.pt` (são
da U.Porto, partilhados). O 10 é a **preferência**: como é igual em
todos, a carga reparte-se entre eles. O MX dá um **nome**, por isso é
preciso uma segunda pergunta (registo A) para o IP: `mx01.up.pt` tem o
**193.137.55.24** (os outros obtêm-se da mesma forma).

#### (h) +qr: o campo id. Para que serve, e porque é necessário no DNS?

```
$ dig +qr www.up.pt
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 51699     <- pedido
;; flags: rd ad; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1
...
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 51699     <- resposta
;; flags: qr rd ra ad; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 1
```

Noutra execução: `id: 45578` no pedido e na resposta. Em cada pergunta o
`id` é **diferente** (aleatório), mas o da **resposta é sempre igual ao
do pedido**. (O pedido não tem a *flag* `qr`; a resposta tem.)

**Para que serve:** é o *identification* do cabeçalho: permite ao
cliente **associar cada resposta à pergunta que lhe deu origem**.

**Porque é necessário no DNS:** o DNS usa **UDP**, que **não tem
conexões**. Um cliente (ou um servidor local, que faz muitas perguntas
ao mesmo tempo) pode ter várias perguntas pendentes, e as respostas
podem chegar por outra ordem ou perder-se. Sem uma conexão por pergunta
(como no TCP), é o `id` que diz "esta resposta é para aquela pergunta".
Nota adicional: ser **aleatório** também protege: um atacante que tente
enviar uma resposta falsa tem de adivinhar o `id` (e a porta), senão a
resposta é ignorada.

## Aula 2 --- DNS: TTL e servidores de raiz

### F3.5 --- Quanto tempo me resta? (Ficha 3, Ex. 5)

#### (a) O que observas? Porquê?

Com um servidor local "normal" (o da faculdade, o do *router* de casa):

```
dig www.google.com    ->  www.google.com.  228  IN  A  ...
(10 s depois)         ->  www.google.com.  218  IN  A  ...
```

(Valores ilustrativos do comportamento esperado; o que se viu no teste
está na nota abaixo.)

O **TTL desce** de uma pergunta para a outra, **tanto quanto o tempo
que passou** entre elas. Quando chega a 0, a pergunta seguinte volta a
mostrar o valor **cheio** (300) e depois recomeça a descer.

**Porquê:** o servidor local responde **da *cache*** e devolve o **tempo
que falta** para essa entrada expirar. Quando expira, apaga-a; a pergunta
seguinte vai outra vez aos servidores da Google, que dão o TTL original
(300 s), e o ciclo recomeça.

Nota (o que se viu no teste, com o servidor 1.1.1.1): os valores **não**
desceram de forma regular (198, depois 237, depois 299 em 14 s). O
1.1.1.1 não é uma máquina: são muitos servidores com o mesmo IP
(*anycast*), cada um com a **sua** *cache*, e cada pergunta pode cair num
diferente, com a entrada mais ou menos "velha". Num servidor local único
vê-se a descida certinha.

#### (b) Perguntando diretamente a um servidor da Google. A diferença?

Os servidores com autoridade de `google.com` obtêm-se com
`dig google.com NS` (`ns1.google.com` a `ns4.google.com`). Perguntando
a um deles:

```
$ dig @ns1.google.com www.google.com +norecurse +noall +answer
www.google.com.   300  IN  A  142.251.156.119
(7 s depois)
www.google.com.   300  IN  A  142.251.150.119
```

O TTL é **sempre 300**: **não desce**. (E a resposta traz a *flag* `aa`.)

**Diferença:** o `ns1.google.com` é o servidor **com autoridade**: não
responde de uma *cache*, tem o registo **original**, e devolve sempre o
TTL que o administrador definiu (300 s = 5 min). Só as *caches* contam o
tempo que falta. O IP também muda de resposta para resposta: a Google
escolhe que réplica indicar (distribuição de carga).

### F3.6 --- Descobrir as raízes (Ficha 3, Ex. 6)

#### (a) Como se pode obter a lista atual de servidores de raiz?

Há duas formas, que se usam juntas:

1. **O ficheiro *root hints*** (`named.root`), publicado pela
   IANA/InterNIC (`https://www.internic.net/domain/named.root`, ou por
   FTP em `FTP.INTERNIC.NET`). Tem os nomes e IPs (IPv4 e IPv6) dos 13
   servidores de raiz e vem instalado com o servidor de nomes. Pode
   estar desatualizado.
2. ***Priming***: ao arrancar, o servidor local usa um IP qualquer desse
   ficheiro e **pergunta a um servidor de raiz quais são os servidores
   da raiz**: registos **NS do nome `.`** (a raiz). A resposta vem do
   próprio servidor de raiz (com autoridade), logo é a lista **atual**.
   Basta que um dos IPs do ficheiro ainda funcione.

#### (b) Obtê-la com o dig

Pede-se os registos NS do nome `.`, de preferência **a um servidor de
raiz** (por exemplo o `a.root-servers.net`, 198.41.0.4, que vem no
enunciado):

```
$ dig @198.41.0.4 . NS +norecurse
;; flags: qr aa; QUERY: 1, ANSWER: 13, AUTHORITY: 0, ADDITIONAL: 27
;; ANSWER SECTION:
.     518400  IN  NS  a.root-servers.net.
.     518400  IN  NS  b.root-servers.net.
   (... até m.root-servers.net: 13 registos)
;; ADDITIONAL SECTION:
a.root-servers.net.  518400  IN  A     198.41.0.4
a.root-servers.net.  518400  IN  AAAA  2001:503:ba3e::2:30
   (... A e AAAA de todos)
```

- **13 servidores**, `a` a `m.root-servers.net` (na resposta vêm por uma
  ordem qualquer).
- A *flag* `aa`: a resposta tem **autoridade** (é a raiz a falar de si
  própria).
- Na secção adicional vêm os IPs: 13 IPv4 + 13 IPv6 = 26 registos, mais
  o OPT = os 27 do contador.
- TTL 518 400 s = 6 dias: a lista quase nunca muda.

`dig . NS` (sem `@`) também dá os 13 nomes, mas vem da *cache* do
servidor local (sem `aa`, TTL a descer).

## Aula 2 --- Aplicações P2P

### C2.6 --- Tempo de distribuição (exercício inventado)

**Significado de todas as variáveis e fórmulas:**
* **$F$ (tamanho do ficheiro a distribuir)**: $1\text{ Gbit} = 10^9\text{ bits}$.
* **$u_s$ (taxa de *upload* do servidor)**: $100\text{ Mbps} = 10^8\text{ bit/s} = 100 \times 10^6\text{ b/s}$.
* **$u$ (taxa de *upload* de cada par/cliente)**: $5\text{ Mbps} = 5 \times 10^6\text{ bit/s}$.
* **$d$ (taxa de *download* de cada par/cliente)**: $50\text{ Mbps} = 50 \times 10^6\text{ bit/s} = 5 \times 10^7\text{ bit/s} = d_{\min}$.
* **$N$**: número total de clientes / pares receptores.

**Fórmulas fundamentais:**
1. **Modelo Cliente-Servidor ($d_{CS}$)**:
$$d_{CS} = \max\left\{ \frac{N \times F}{u_s},\ \frac{F}{d_{\min}} \right\}$$
* O servidor tem de enviar sozinho $N$ cópias completas do ficheiro: demora $\frac{NF}{u_s}$.
* Nenhum cliente pode receber o ficheiro mais rápido do que a sua taxa de download: $\frac{F}{d_{\min}}$.

2. **Modelo Peer-to-Peer ($d_{P2P}$)**:
$$d_{P2P} = \max\left\{ \frac{F}{u_s},\ \frac{F}{d_{\min}},\ \frac{N \times F}{u_s + N \times u} \right\}$$
* O servidor só precisa de enviar para a rede pelo menos uma cópia de cada bloco do ficheiro: $\frac{F}{u_s}$.
* Nenhum cliente pode descarregar mais rápido do que o seu download: $\frac{F}{d_{\min}}$.
* O volume total de dados recebido por todos os clientes é $N \times F$. A taxa total combinada de upload da rede é o upload do servidor mais o upload de todos os $N$ pares ($u_s + N \times u$): demora $\frac{NF}{u_s + N u}$.

**Termos constantes (independentes de $N$):**
* $\frac{F}{u_s} = \frac{10^9\text{ b}}{10^8\text{ b/s}} = 10\text{ s}$
* $\frac{F}{d_{\min}} = \frac{10^9\text{ b}}{5 \times 10^7\text{ b/s}} = 20\text{ s}$

#### (a) $N = 10$

- $d_{CS} = \max\left\{ \frac{10 \times 10^9}{10^8},\ 20 \right\} = \max\{100,\ 20\} = \mathbf{100\text{ s}}$ *(manda o upload do servidor).*
- P2P: upload agregado $= 10^8 + 10 \times (5 \times 10^6) = 1{,}5 \times 10^8\text{ b/s}$.
  $\frac{10 \times 10^9}{1{,}5 \times 10^8} \approx 66{,}7\text{ s}$.
  $d_{P2P} = \max\{10,\ 20,\ 66{,}7\} = \mathbf{66{,}7\text{ s}}$ *(manda o upload agregado).*

#### (b) $N = 100$

**1. No modelo Cliente-Servidor ($d_{CS}$):**
* Termo do servidor:
$$\frac{N \times F}{u_s} = \frac{100 \times 10^9\text{ bits}}{10^8\text{ bit/s}} = \frac{10^{11}}{10^8} = 1000\text{ s}$$
* Termo do cliente:
$$\frac{F}{d_{\min}} = \frac{10^9\text{ bits}}{5 \times 10^7\text{ bit/s}} = 20\text{ s}$$
* Resultado final:
$$d_{CS} = \max(1000\text{ s},\ 20\text{ s}) = \mathbf{1000\text{ s}}\text{ (16 minutos e 40 segundos)}$$
*(O termo que manda é o **upload do servidor**, que fica sobrecarregado).*

**2. No modelo Peer-to-Peer ($d_{P2P}$):**
* Upload do servidor: $\frac{F}{u_s} = 10\text{ s}$.
* Download do cliente mais lento: $\frac{F}{d_{\min}} = 20\text{ s}$.
* Capacidade agregada de upload de toda a rede:
$$u_{total} = u_s + N \times u = 100\text{ Mbps} + 100 \times 5\text{ Mbps} = 100 + 500 = 600\text{ Mbps} = 6 \times 10^8\text{ bit/s}$$
* Tempo de escoamento agregado:
$$\frac{N \times F}{u_s + N \times u} = \frac{100 \times 10^9\text{ bits}}{6 \times 10^8\text{ bit/s}} = \frac{1000}{6} \approx \mathbf{166{,}7\text{ s}}$$
* Resultado final:
$$d_{P2P} = \max(10\text{ s},\ 20\text{ s},\ 166{,}7\text{ s}) = \mathbf{166{,}7\text{ s}}\text{ (2 minutos e 47 segundos)}$$
*(O termo que manda é o **upload agregado da rede**).*

**Por que razão o P2P é muito mais rápido e escalável à medida que $N$ cresce?**
* Para $N = 100$, o P2P é **6 vezes mais rápido** que o Cliente-Servidor (166,7 s vs 1000 s).
* No modelo Cliente-Servidor, cada novo cliente representa apenas mais um encargo para o servidor central: o tempo cresce **linearmente** em função de $N$ ($\frac{NF}{u_s}$).
* No modelo P2P, **cada novo cliente é também um distribuidor**: ao entrar na rede, cada par traz consigo a sua própria taxa de upload ($u = 5\text{ Mbps}$) e partilha os pedaços que já descarregou com os vizinhos!
* Quando $N$ é muito grande ($N \to \infty$), a capacidade agregada tende para o limite:
$$\lim_{N \to \infty} \frac{N \times F}{u_s + N \times u} = \frac{F}{u} = \frac{10^9\text{ bits}}{5 \times 10^6\text{ bit/s}} = \mathbf{200\text{ s}}$$
Isto significa que, mesmo com 100 000 utilizadores, o P2P nunca demorará mais de 200 segundos (~3,3 minutos), ao passo que o servidor clássico levaria semanas!

#### (c) $N = 1000$

- $d_{CS} = \max\{10\,000,\ 20\} = \mathbf{10\,000\text{ s}}$ (quase 3 horas; servidor).
- P2P: $\dfrac{10^{12}}{10^8 + 5\times10^9} = \dfrac{10^{12}}{5{,}1\times10^9} \approx 196{,}1$ s.
  $d_{P2P} = \mathbf{196{,}1\text{ s}}$ (*upload* agregado).

**Leitura:** de $N = 10$ para $N = 1000$ o cliente-servidor fica **100
vezes** mais lento; o P2P só **3 vezes**. Quando $N$ é muito grande, o
termo P2P aproxima-se de $F/u = 10^9 / (5\times10^6) = 200$ s: cada par
novo traz tanta capacidade quanta pede. Contas confirmadas em Python.

## Aula 2 --- Sockets TCP: servidor persistente e concorrente

### F4.1 --- Um servidor com letra grande (Ficha 4, Ex. 1)

O servidor é o persistente do exemplo (Ex. 1a), em `TCPServer.java`.

#### (b) Cliente com o servidor na linha de comando, até CTRL-D

Muda o `main` do `TCPClient` (o resto fica igual):

```java
        Socket clientSocket = new Socket(argv[0], 6789);   // servidor da linha de comando
        ...
        String sentence;
        // readLine() devolve null no fim da stream (CTRL-D)
        while ((sentence = inFromUser.readLine()) != null) {
            outToServer.writeBytes(sentence + '\n');
            System.out.println("FROM SERVER: " + inFromServer.readLine());
        }
        clientSocket.close();
```

- O `"hostname"` fixo passa a `argv[0]`: `java TCPClient localhost`.
- O pedido e a resposta ficam dentro de um ciclo, que acaba quando o
  `readLine()` do **teclado** devolve `null` (CTRL-D). Só então o cliente
  fecha a socket, e é isso que faz o `readLine()` do **servidor**
  devolver `null`.

Saída real (compilado e testado):

```
$ java TCPClient localhost
ola mundo
FROM SERVER: OLA MUNDO
segunda linha
FROM SERVER: SEGUNDA LINHA
^D
```

#### (c) Dois clientes com o servidor iterativo

**O que se vê:** o primeiro cliente (A) funciona normalmente. O segundo
(B) arranca sem erro, mas a primeira linha que escreve **fica sem
resposta**. Só quando o A faz CTRL-D é que o B recebe a resposta, e daí
em diante funciona. No teste, o A ligou-se e fechou 3 s depois; o B, que
enviou `sou o B` logo a seguir ao A, só recebeu `SOU O B` no instante em
que o A fechou.

**Porquê:**

1. O servidor é **iterativo**: faz `accept()` para o A e fica no ciclo
   `while (readLine() != null)` **até o A fechar**. Durante esse tempo
   não volta a chamar `accept()`.
2. A conexão do B **é estabelecida** na mesma: o sistema operativo faz o
   *handshake* TCP e põe a conexão numa **fila de conexões pendentes**
   da *welcome socket*. Por isso o `new Socket(...)` do B não dá erro.
3. A linha que o B envia chega e fica no *buffer* de receção dessa
   conexão, mas **ninguém a lê**. O B fica bloqueado no seu
   `inFromServer.readLine()`.
4. Quando o A fecha, o `readLine()` do servidor devolve `null`, o servidor
   fecha a socket do A e volta ao `accept()`, que devolve logo a conexão
   do B (já estava na fila). Lê a linha que lá estava e responde.

Com conexões persistentes isto agrava-se: o servidor iterativo atende
**um cliente de cada vez durante a sessão inteira dele**, não só durante
um pedido.

#### (d) Servidor concorrente com *threads*

Resposta-modelo, com a estrutura sugerida na ficha (compilado e
testado):

```java
import java.io.*;
import java.net.*;

class TCPServerThreads {
    public static void main(String argv[]) throws Exception {
        ServerSocket welcomeSocket = new ServerSocket(6789);
        while (true) {
            Socket connectionSocket = welcomeSocket.accept();
            Helper h = new Helper(connectionSocket);
            new Thread(h).start();      // atende este cliente noutra thread
        }                               // e volta logo ao accept()
    }
}

class Helper implements Runnable {
    private Socket connectionSocket;

    Helper(Socket s) { connectionSocket = s; }

    public void run() {
        try {
            BufferedReader inFromClient = new BufferedReader(
                new InputStreamReader(connectionSocket.getInputStream()));
            DataOutputStream outToClient =
                new DataOutputStream(connectionSocket.getOutputStream());
            String clientSentence;
            while ((clientSentence = inFromClient.readLine()) != null)
                outToClient.writeBytes(clientSentence.toUpperCase() + '\n');
            connectionSocket.close();
        } catch (IOException e) {
            System.err.println("Erro com um cliente: " + e.getMessage());
        }
    }
}
```

- A *thread* principal **só** faz `accept()`: entrega cada
  `connectionSocket` a um `Helper` numa *thread* nova e volta logo a
  esperar o próximo cliente.
- O `run()` faz o que o ciclo do servidor iterativo fazia para um
  cliente. O `try/catch` tem de ficar lá dentro, porque o `run()` não
  pode lançar `IOException`, e assim um erro com um cliente não deita
  abaixo o servidor.

**Repetindo a (c):** os dois clientes são atendidos ao mesmo tempo. No
teste, o B recebeu `SOU O B` no mesmo segundo em que a enviou, com o A
ainda ligado, e as respostas dos dois intercalaram-se.

## Aula 2 --- Um cliente SMTP com sockets

### F4.2 --- Message for you, sir (Ficha 4, Ex. 2)

#### (a) Cliente SMTP com HELO, MAIL FROM, RCPT TO, DATA e QUIT

Resposta-modelo: as funções `resposta()` e `comando()` do exemplo mais
o `main`.

```java
import java.io.*;
import java.net.*;

class SMTPClient {
    static BufferedReader inFromServer;
    static DataOutputStream outToServer;

    // resposta() e comando(): as do exemplo do resumo

    // uso: java SMTPClient servidor remetente destinatario < corpo.txt
    public static void main(String argv[]) throws Exception {
        Socket clientSocket = new Socket(argv[0], 25);
        inFromServer = new BufferedReader(
            new InputStreamReader(clientSocket.getInputStream()));
        outToServer = new DataOutputStream(clientSocket.getOutputStream());

        if (resposta() != 220) throw new IOException("servidor indisponivel");
        comando("HELO portatil", 250);
        comando("MAIL FROM:<" + argv[1] + ">", 250);
        comando("RCPT TO:<" + argv[2] + ">", 250);
        comando("DATA", 354);

        BufferedReader inFromUser =
            new BufferedReader(new InputStreamReader(System.in));
        String linha;
        while ((linha = inFromUser.readLine()) != null) {
            if (linha.startsWith(".")) linha = "." + linha;  // dot-stuffing
            outToServer.writeBytes(linha + "\r\n");
        }
        comando(".", 250);                             // fim da mensagem
        comando("QUIT", 221);
        clientSocket.close();
    }
}
```

**Os códigos esperados:** `220` ao ligar, `250` ao `HELO`, ao
`MAIL FROM`, ao `RCPT TO` e ao `.` final, `354` ao `DATA` e `221` ao
`QUIT`.

- O corpo **não** passa pelo `comando()`: entre o `354` e o `.` o servidor
  não responde a cada linha, só no fim.
- Se um código não for o esperado (ex.: `550` no `RCPT TO`), o
  `comando()` envia `QUIT` e lança uma exceção: não faz sentido mandar o
  `DATA` de uma mensagem que não tem destinatário.

**Testado** contra um servidor SMTP falso local, que regista os bytes
recebidos. Com o corpo `Ola!` / `.linha a comecar por ponto` / `Adeus`:

```
S: 220 fake ESMTP
C: HELO portatil
S: 250 fake
C: MAIL FROM:<eu@fc.up.pt>
S: 250 2.1.0 Ok
C: RCPT TO:<up123@fc.up.pt>
S: 250 2.1.5 Ok
C: DATA
S: 354 End data with <CR><LF>.<CR><LF>
C: .
S: 250 2.0.0 Ok: queued as 1234
C: QUIT
S: 221 2.0.0 Bye
```

O servidor recebeu `Ola!\r\n`, `..linha a comecar por ponto\r\n`
(o ponto extra do *dot-stuffing*), `Adeus\r\n` e `.\r\n`. Com um
servidor que recusa o destinatário:

```
C: RCPT TO:<naoexiste@fc.up.pt>
S: 550 5.1.1 <x>: Recipient address rejected: User unknown
Exception in thread "main" java.io.IOException: esperava 250 e veio 550
```

Contra o `smtp.fc.up.pt` foram testados só o `220`, o `EHLO` e o `QUIT`
(ver o exemplo do resumo). O envio real fica para ti: `java SMTPClient
smtp.fc.up.pt upXXXXXXXXX@fc.up.pt upXXXXXXXXX@fc.up.pt`. Se a porta 25
estiver bloqueada fora da rede da faculdade, a ligação dá *timeout*: usa
a VPN.

#### (b) Cabeçalhos From:, To: e Subject:

Os cabeçalhos fazem parte da **mensagem** (RFC 2822), não do diálogo
SMTP. Por isso vão **dentro do `DATA`**, antes do corpo, separados dele
por uma **linha vazia**. O assunto passa a ser o 4.º argumento:

```java
        comando("DATA", 354);
        // cabecalhos RFC 2822, uma linha vazia, e so depois o corpo
        outToServer.writeBytes("From: " + argv[1] + "\r\n");
        outToServer.writeBytes("To: " + argv[2] + "\r\n");
        outToServer.writeBytes("Subject: " + argv[3] + "\r\n");
        outToServer.writeBytes("\r\n");
        // ... o ciclo do corpo, como na (a)
```

Testado no servidor falso com `java SMTPClient localhost eu@fc.up.pt
up123@fc.up.pt "Teste da ficha 4"` e o corpo `Corpo`. Depois do `DATA`,
o servidor recebeu:

```
From: eu@fc.up.pt
To: up123@fc.up.pt
Subject: Teste da ficha 4

Corpo
.
```

- Sem a linha vazia, o servidor e o leitor de email tomariam a primeira
  linha do corpo por mais um cabeçalho.
- Sem estes cabeçalhos, a mensagem da (a) chega **sem assunto** e o
  leitor de email não tem `From:` nem `To:` para mostrar. O `From:` pode
  até ser diferente do `MAIL FROM`, como na F3.3.

## Teste modelo 1 --- escolha múltipla

### M1.1--10 --- Parte I (Teste modelo 1)

Grelha oficial: 1a, 2b, 3a, 4d, 5b, 6b, 7a, 8a, 9c, 10a.

#### (1) Característica do HTTP

**(a)**. O HTTP é pedido/resposta e as mensagens são texto ASCII
(linhas de pedido e cabeçalhos). (b) o HTTPS é que cifra; (c) é o FTP
(controlo *out-of-band*); (d) o HTTP corre sobre TCP (só o HTTP/3 vai
sobre QUIC/UDP).

#### (2) Servidor de *chat*

**(b) *multiplex***. Um só processo atende todas as *sockets* com
`select()` e tem logo acesso a todas, por isso reenvia uma mensagem de
uma conexão para as outras sem comunicar entre processos. Com processos
(a, d), cada conexão está num processo diferente e era preciso IPC; o
iterativo (c) atende um cliente de cada vez.

#### (3) Camada de rede

**(a)**. A rede leva datagramas de máquina a máquina **através de
*routers***, extremo-a-extremo. (b) é a camada de ligação (um salto);
(c) e (d) são o transporte (processos, identificados por portas).

#### (4) Servidor de nomes local

**(d)**. O terminal faz-lhe um pedido **recursivo** ("dá-me a resposta
final") e ele resolve com pedidos **iterativos** à raiz, ao TLD e ao
servidor com autoridade.

#### (5) Aplicação elástica

**(b)**. Elástica = usa o débito que houver (transferência de ficheiros,
email, web), ao contrário das multimédia, que precisam de um mínimo.

#### (6) `new Socket("api.example.com", 80)`

**(b) cliente TCP**. A classe `Socket` (sem `Server`) com um nome e uma
porta **liga-se** a um servidor: é o cliente. Um servidor TCP usaria
`ServerSocket(porta)`; UDP usaria `DatagramSocket`.

#### (7) Multiplexagem estatística

**(a)**. Não há reserva: um fluxo sozinho usa toda a capacidade da
ligação. (b) é FDM; (c) e (d) são comutação de circuitos (reserva, TDM
com padrão fixo).

#### (8) Cliente em UDP

**(a)**. Em UDP não há conexão, por isso (c) não se aplica; o cliente é
quem **toma a iniciativa**, enviando a primeira mensagem. (b) descreve o
servidor.

#### (9) Intensidade de tráfego

**(c)**. Mais tráfego só enche as filas. A propagação depende da
distância e do meio, e a transmissão de $L/R$; nenhuma muda com a carga.

#### (10) Fim de uma mensagem SMTP

**(a)**. Depois do `DATA`, a mensagem acaba numa linha só com `.`
(`CRLF.CRLF`). Não pode ser (c): a conexão é persistente e pode levar
mais mensagens.
