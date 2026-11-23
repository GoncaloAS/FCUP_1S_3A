---
title: "Redes de Comunicação --- guia do 2.º teste"
date: "25/11/2026, 16:30, FC2 009"
---

# Tema 0 --- Começa aqui

**O que sai:** a camada de transporte e a camada de rede até à fragmentação IP.
O endereçamento IP (sub-redes, máscaras, DHCP, NAT) **não** sai.

**Como estudar:** lê um tema. Faz esse tema no quiz. Passa ao seguinte.
A ordem dos temas é a mesma no guia e no quiz.

## As palavras deste guia

Cada palavra tem um só sentido.

| palavra | sentido |
|:--------|:-------------------------------------------|
| **emissor** | a máquina que envia os dados |
| **receptor** | a máquina que recebe os dados |
| **terminal** | uma máquina na ponta da rede (o teu PC, um servidor) |
| ***router*** | uma máquina no meio da rede, que reenvia os dados |
| **segmento** | o pacote da camada de transporte (TCP ou UDP) |
| **datagrama** | o pacote da camada de rede (IP); leva um segmento lá dentro |
| **pacote** | o nome geral, nos protocolos de estudo (rdt, GBN, SR) |
| **ACK** | a mensagem do receptor que diz "recebi" |
| ***timeout*** | o tempo de espera acabou e o ACK não chegou |
| **RTT** | o tempo de ida e volta: do envio do pacote até chegar o ACK |
| ***buffer*** | a memória onde os dados esperam |
| **janela** | a quantidade de dados que podem estar enviados e sem ACK |
| **MSS** | o máximo de dados da aplicação num segmento |
| **MTU** | o maior datagrama que uma ligação aceita |

## As três contas que tens de saber fazer

| conta | fórmula | tema |
|:----------|:------------------------------|:-----:|
| utilização | $U = N\cdot(L/R)\,/\,(RTT + L/R)$ | 2 |
| *timeout* | $E + 4D$ | 4 |
| fragmentação | dados por fragmento = MTU $-$ 20, para baixo até um múltiplo de 8 | 8 |

Tens também de saber ler o **gráfico da janela** do TCP (tema 6).
Treina as contas com potências de 10. O 1.º teste foi sem calculadora.

# Tema 1 --- Transporte e UDP

## Para que serve o transporte

A camada de rede leva dados de **máquina a máquina**.
A camada de transporte leva dados de **processo a processo**.

- O transporte corre **só nos terminais**.
- Os *routers* não leem o cabeçalho de transporte.
- O emissor parte a mensagem em segmentos. O receptor junta os segmentos.
- O transporte **segmenta** a mensagem. A camada de rede **fragmenta** o datagrama. São coisas diferentes.

| | TCP | UDP |
|:--------|:----------------|:----------------|
| entrega tudo? | sim | pode perder dados |
| entrega por ordem? | sim | pode trocar a ordem |
| abre conexão? | sim | não |
| controlo de fluxo | sim | não |
| controlo de congestionamento | sim | não |
| cabeçalho | 20 bytes | 8 bytes |
| garante atraso máximo? | não | não |
| garante débito mínimo? | não | não |

## Que *socket* recebe o segmento?

Uma *socket* é a porta de entrada de um processo.

- **Multiplexagem:** o emissor junta os dados de várias *sockets* e põe as portas no cabeçalho.
- **Desmultiplexagem:** o receptor lê o cabeçalho e entrega à *socket* certa.

::: {.definicao title="--- A regra"}
- **UDP usa 2 valores:** IP de destino e porta de destino.
- **TCP usa 4 valores:** IP de origem, porta de origem, IP de destino, porta de destino.
:::

::: {.exemplo title="--- Contar sockets"}
Chegam ao servidor C dois segmentos UDP e três segmentos TCP.

- UDP: `A:9157 → C:6428` e `B:5775 → C:6428`. O destino é igual. **Uma** *socket*.
- TCP: `A:9157 → C:80`, `B:9157 → C:80`, `B:5775 → C:80`. Os 4 valores nunca são
  todos iguais. **Três** *sockets*.

A resposta troca as portas. A resposta UDP para A sai da porta 6428 e vai para a 9157.
:::

## UDP

O UDP faz só duas coisas: multiplexagem e deteção de erros.

**Porque se usa:** não espera pela abertura de uma conexão. Não guarda estado.
O cabeçalho é pequeno. A aplicação envia à velocidade que quer.

**Quem o usa:** DNS, SNMP, áudio e vídeo em direto, *multicast*.

**Cabeçalho (4 campos de 16 bits):** porta de origem, porta de destino,
comprimento, *checksum*. O comprimento conta o segmento **inteiro**, com o cabeçalho.

::: {.definicao title="--- Receita: checksum"}
1. Parte o segmento em palavras de 16 bits. Põe o campo *checksum* a zeros.
2. Soma as palavras em binário.
3. A soma passou dos 16 bits? Tira o 1 da esquerda e soma-o à direita.
4. Troca os bits: 0 passa a 1 e 1 passa a 0. Este é o *checksum*.
5. O receptor soma tudo, **com** o *checksum*. Só uns: não detetou erro. Algum 0: há erro.
:::

::: {.exemplo title="--- Checksum de duas palavras"}
```
   1110011001100110
 + 1101010101010101
 = 1 1011101110111011    17 bits: o 1 da esquerda sai
 +                  1    e volta a entrar à direita
 = 1011101110111100      soma
   0100010001000011      checksum (bits trocados)
```
:::

- O *checksum* só **deteta** erros. Não corrige e não recupera. O receptor deita fora o segmento com erro.
- Deteta **sempre** um erro de um só bit.
- **Não** deteta erros que se anulam. Exemplo: na mesma coluna, um bit passa de 0 a 1 e outro passa de 1 a 0.
- **Não** deteta duas palavras que trocaram de lugar.
- O *checksum* cobre o segmento e um **pseudo-cabeçalho** (os dois IPs, o protocolo e o comprimento).
- No UDP o *checksum* é opcional. Só zeros quer dizer "sem *checksum*". Se a conta der só zeros, envia-se só uns.

::: {.exemplo title="--- Datagrama UDP de 16 bytes: portas e checksum (F6.5)"}
```
w1 01001010 01101010   w2 11011011 00101000
w3 00000000 00010000   w4 00000000 00000000
w5 10100010 10101010   w6 10000001 11110101
w7 11010001 11101000   w8 10001010 10110111
```
1. $w_1$ = porta de origem = 19050. $w_2$ = porta de destino = 56104.
2. $w_3$ = comprimento = 16 bytes (8 de cabeçalho + 8 de dados). $w_4$ = *checksum*, ainda a zeros.
3. Soma uma palavra de cada vez:

```
w1        0100101001101010
+ w2    1 0010010110010010   -> +1 ->  0010010110010011
+ w3                                   0010010110100011
+ w4      (zeros, não muda)            0010010110100011
+ w5                                   1100100001001101
+ w6    1 0100101001000010   -> +1 ->  0100101001000011
+ w7    1 0001110000101011   -> +1 ->  0001110000101100
+ w8                                   1010011011100011   soma
                                       0101100100011100   checksum
```
4. Verifica: soma + *checksum* = `1111111111111111`.
5. **Erro que não deteta:** o último bit de $w_5$ passa de 0 a 1 e o último bit de $w_8$ passa de 1 a 0. A soma fica igual.
:::

# Tema 2 --- Transferência fiável e *stop-and-wait*

**O problema:** o canal troca bits e perde pacotes.

**O objetivo:** entregar todos os dados, sem erros e por ordem.

O **rdt** é um protocolo de estudo. Cada versão resolve um problema novo.

| versão | problema do canal | o que o protocolo acrescenta |
|:---:|:-------------|:--------------------------------|
| 1.0 | nenhum | nada |
| 2.0 | troca bits nos dados | *checksum*; ACK ("recebi bem"); NAK ("recebi mal"); o emissor repete quando recebe NAK |
| 2.1 | troca bits nos ACK e NAK | número de sequência 0 ou 1: o receptor reconhece repetidos e deita-os fora |
| 2.2 | o mesmo | tira o NAK: o receptor repete o ACK do último pacote bom |
| 3.0 | também perde pacotes | temporizador: sem ACK a tempo, o emissor repete |

**Porque é que chega 1 bit de número?** O emissor só tem um pacote em viagem.
O receptor só precisa de distinguir "pacote novo" de "repetido".

**Se o rdt2.0 recebe um ACK ou NAK estragado?** O emissor não sabe o que aconteceu. Repete o pacote. O pacote pode ser um repetido. O número resolve isto.

**Porque é que o ACK tem número?** Um ACK pode chegar atrasado.
Sem número, o emissor pensa que esse ACK confirma o pacote seguinte.

::: {.exemplo title="--- ACKs sem número: o que corre mal (F6.1)"}
1. O emissor envia P1. O ACK de P1 atrasa-se.
2. Há *timeout*. O emissor repete P1.
3. Chega o primeiro ACK. O emissor envia P2.
4. P2 perde-se. Chega o segundo ACK, que é da repetição de P1.
5. O emissor pensa que o ACK é de P2 e avança. **P2 perdeu-se e ninguém sabe.**

Com número, o ACK diz "P1". O emissor espera o ACK de P2 e ignora este.
:::

**Porque é preciso o temporizador?** Se o pacote se perde, o receptor não responde.
Sem temporizador, os dois lados esperam para sempre.

No rdt3.0 o emissor **só** repete por *timeout*. Ele ignora os ACKs com erros e os ACKs com o número errado.

## Os quatro casos do rdt3.0

| caso | o que acontece |
|:--------|:------------------------------------------|
| sem perdas | pacote 0, ACK 0, pacote 1, ACK 1 |
| perde-se o pacote | há *timeout*; o emissor repete o pacote |
| perde-se o ACK | há *timeout*; o emissor repete; o receptor deita fora o repetido e **envia outra vez o ACK** |
| o ACK atrasa-se | há *timeout* cedo demais; o emissor repete; o segundo ACK chega e o emissor ignora-o |

## Que mecanismo resolve que problema?

| problema | mecanismo |
|:-------------|:-------------------|
| bits trocados | *checksum* |
| saber se chegou | ACK |
| pacote perdido | temporizador e repetição |
| pacote repetido ou fora de ordem | número de sequência |
| emissor parado muito tempo | *pipelining* (não dá fiabilidade; dá velocidade) |

## *Stop-and-wait* e a utilização

***Stop-and-wait*:** o emissor envia um pacote, para, e espera pelo ACK.
É correto, mas é lento quando o RTT é grande.

A **utilização** $U$ é a parte do tempo em que o emissor está a transmitir.

::: {.definicao title="--- Receita: utilização"}
1. Passa o tamanho $L$ para **bits** (bytes vezes 8).
2. Tempo de transmissão $= L/R$, com $R$ em bits por segundo.
3. RTT $= 2\,\times$ atraso de propagação. Propagação = distância / velocidade.
4. Um pacote de cada vez: $U = (L/R)\,/\,(RTT + L/R)$.
5. $N$ pacotes de cada vez: $U = N\cdot(L/R)\,/\,(RTT + L/R)$, no máximo 1.
6. Débito $= U\cdot R$.
7. Para o emissor nunca parar: $N \ge (RTT + L/R)\,/\,(L/R)$. Arredonda para cima.
:::

![](figuras/stop_wait_pipelining.pdf){width=68%}

::: {.exemplo title="--- 1 Gbps, propagação 15 ms, pacotes de 8000 bits"}
1. $L/R = 8000/10^9 = 8\ \mu$s $= 0{,}008$ ms.
2. $RTT = 2\times15 = 30$ ms.
3. $U = 0{,}008/30{,}008 \approx 0{,}00027$, ou seja, 0,027 %.
4. Débito $= 0{,}00027\times10^9 \approx 270$ kbps. A ligação dá 1 Gbps.
5. Para nunca parar: $N \ge 30{,}008/0{,}008 = 3751$ pacotes.
:::

::: {.exemplo title="--- 10 Mbps, propagação 20 ms, pacotes de 1500 bytes (F6.1)"}
1. $L = 1500\times8 = 12\,000$ bits. $L/R = 12\,000/10^7 = 1{,}2$ ms.
2. $RTT = 40$ ms.
3. $U = 1{,}2/41{,}2 \approx 0{,}029$, ou seja, 2,9 %. O protocolo não é adequado.
4. Para nunca parar: $N \ge 41{,}2/1{,}2 = 34{,}3$. Arredonda para cima: **35 pacotes**.
:::

# Tema 3 --- Go-Back-N e Selective Repeat

## *Pipelining*: GBN e SR

***Pipelining*:** o emissor envia vários pacotes antes de receber o primeiro ACK.
Serve para **melhorar o débito**. A utilização fica $N$ vezes maior, até 1.
Precisa de mais números de sequência e de *buffers*.

| | **Go-Back-N (GBN)** | **Selective Repeat (SR)** |
|:---------|:--------------------|:--------------------|
| ACK | **cumulativo**: ACK 5 confirma tudo até 5 | **individual**: ACK 5 confirma só o 5 |
| chega um pacote fora de ordem | deita fora; repete o último ACK bom | guarda no *buffer* e envia o ACK dele |
| temporizadores | um, do pacote mais antigo sem ACK | um por pacote |
| no *timeout* | repete esse pacote **e todos os seguintes** | repete **só** esse pacote |
| janela com $k$ bits | $N \le 2^k - 1$ | $N \le 2^{k-1}$ |
| receptor | simples | mais complexo |

![](figuras/gbn_sr.pdf){width=100%}

*Janela 4. Perde-se o pacote 2. O GBN repete 2, 3, 4 e 5. O SR repete só o 2.*

**Temporizador do GBN.** Um ACK que faz andar a janela reinicia-o. Se não há pacotes sem ACK, o temporizador para.

**Vantagem do GBN:** o receptor não precisa de *buffer*. Só guarda o número que espera.

**Como a janela anda.** No GBN, ACK($n$) põe o início da janela em $n+1$.
No SR, a janela só anda quando chega o ACK do pacote **mais antigo**.

**SR: chega um pacote que o receptor já entregou.** O receptor envia o ACK outra vez.
O primeiro ACK pode ter-se perdido. Sem este ACK, a janela do emissor não anda.

::: {.exemplo title="--- Porque o SR precisa de 2N números"}
Números 0 a 3 e janela 3. O emissor envia 0, 1, 2. O receptor recebe os três e passa a esperar 3, 0, 1.

- **Caso A:** os ACKs chegam. O emissor envia 3 e um 0 **novo**. O receptor aceita o 0. Está certo.
- **Caso B:** os ACKs perdem-se. O emissor repete o 0 **antigo**. O receptor aceita o 0 como novo. **Está errado.**

O receptor vê o mesmo nos dois casos. Com $2N$ números, as duas janelas nunca partilham um número.
:::

::: {.exemplo title="--- Janela e bits: 5000 km, 2 Gbps, blocos de 1000 bytes, SR (F6.4)"}
1. $L/R = 8000/(2\times10^9) = 4\ \mu$s.
2. Propagação $= 5\times10^6/(2\times10^8) = 25$ ms. $RTT = 50$ ms $= 50\,000\ \mu$s.
3. $N \ge (50\,000 + 4)/4 = 12\,501$ blocos.
4. O SR precisa de $2N = 25\,002$ números. $2^{14} = 16\,384$ não chega. $2^{15} = 32\,768$ chega: **15 bits**.

**Faz sentido uma janela maior?** Sem perdas, não: o emissor já nunca para. Com perdas, sim: recuperar demora pelo menos mais um RTT, e a janela maior deixa enviar blocos novos durante esse tempo.
:::

::: {.exemplo title="--- SR instante a instante: janela 3, timeout 3; perdem-se B(3) e A(2) (F6.2)"}
Em cada instante o emissor envia uma mensagem. A mensagem chega no instante seguinte e o receptor responde logo. O ACK chega 2 instantes depois do envio. Sem ACK, o emissor repete 3 instantes depois.

| t | emissor | receptor |
|:-:|:--------------------|:--------------------|
| 1 | envia B(0) | |
| 2 | envia B(1) | recebe B(0); envia A(0); janela [1,3] |
| 3 | recebe A(0); janela [1,3]; envia B(2) | recebe B(1); envia A(1); janela [2,4] |
| 4 | recebe A(1); janela [2,4]; envia B(3), **perdido** | recebe B(2); envia A(2), **perdido**; janela [3,5] |
| 5 | envia B(4) | |
| 6 | *timeout* de B(2): repete B(2) | recebe B(4), fora de ordem: guarda; envia A(4) |
| 7 | recebe A(4); *timeout* de B(3): repete B(3) | recebe B(2), já entregue: envia A(2) outra vez |
| 8 | recebe A(2); janela [3,5] | recebe B(3); entrega 3 e 4; envia A(3) |
| 9 | recebe A(3); acabou | |

B(4) não é repetido. A(4) chega no instante 7 e o *timeout* dele era no 8.
:::

# Tema 4 --- TCP: números, ACKs e timeout

## O que é o TCP

- **Ponto a ponto:** um emissor e um receptor.
- ***Full duplex*:** os dados vão nos dois sentidos, na mesma conexão.
- **Sequência de bytes:** o TCP não marca onde acaba cada mensagem.
- **Com conexão:** os dois lados preparam-se antes dos dados.
- **MSS:** máximo de **dados da aplicação** num segmento. Com MSS 1460, o segmento tem 1480 bytes e o datagrama 1500.

**Cabeçalho (20 bytes):** portas, número de sequência, número de ACK, tamanho do
cabeçalho, *flags*, janela do receptor, *checksum*, apontador urgente.

**_Flags_:** SYN abre. FIN fecha. RST reinicia. ACK diz que o campo de ACK é válido.
PSH entrega já à aplicação. URG marca dados urgentes.

## Números de sequência e ACKs

::: {.definicao title="--- As duas regras"}
- **Número de sequência** = número do **primeiro byte** do segmento.
- **ACK** = número do **próximo byte** que o receptor espera. É cumulativo.

Soma **bytes**. Não somes 1 por segmento.
:::

::: {.exemplo title="--- Três segmentos: 500, 300 e 200 bytes, a partir do byte 1000"}
1. Números de sequência: 1000, 1500, 1800.
2. Sem perdas, os ACKs são 1500, 1800, 2000.
3. O segmento 1500 perde-se. O segmento 1000 gera ACK 1500. O segmento 1800 gera outra vez ACK 1500 (**duplicado**).
4. O segmento 1500 chega depois. O receptor já tem tudo. Envia ACK 2000.
:::

::: {.exemplo title="--- Continuação: A envia mais três segmentos de 100 bytes"}
O segmento 1500 perdeu-se. Todos os outros chegam.

1. Os segmentos novos têm os números 2000, 2100 e 2200.
2. O segmento 1800 já gerou o primeiro ACK 1500 duplicado. Cada segmento novo gera outro.
3. O segmento 2100 gera o **terceiro** duplicado. A repete o 1500 quando recebe esse ACK.
4. O 1500 chega. O receptor tem tudo até ao byte 2299. Envia **ACK 2300**.
:::

## Quando é que o emissor repete?

O TCP tem **um só temporizador**: o do segmento mais antigo sem ACK. Repete em dois casos.

1. ***Timeout*.** Repete só o segmento mais antigo sem ACK.
2. **3 ACKs duplicados** (4 ACKs iguais). Repete logo, sem esperar. Chama-se **retransmissão rápida**.

```{=latex}
\Needspace*{9\baselineskip}
```

| situação | o que acontece |
|:-----------|:--------------------------------------------|
| o ACK perde-se | há *timeout*; o emissor repete; o receptor envia o ACK outra vez |
| o *timeout* é cedo demais | o emissor repete o mais antigo; o receptor responde com o ACK de tudo o que já tem |
| perde-se o ACK 100, mas chega o ACK 120 | o ACK 120 confirma tudo; o emissor não repete nada |

| o que o receptor recebe | o que o receptor faz |
|:--------------------|:--------------------------|
| segmento por ordem, sem ACKs em atraso | espera até 500 ms pelo seguinte (*delayed ACK*) |
| segmento por ordem, com um ACK em atraso | envia **já** um ACK que confirma os dois |
| segmento fora de ordem | envia **já** um ACK duplicado |
| segmento que tapa o início do buraco | envia **já** o ACK |

## Calcular o *timeout*

O *timeout* tem de ser maior do que o RTT. O RTT muda, por isso o TCP faz uma estimativa.

- **Curto demais:** repete sem necessidade.
- **Longo demais:** demora a reagir a uma perda.

::: {.definicao title="--- Receita: timeout"}
$S$ = RTT medido. $E$ = RTT estimado. $D$ = desvio. Faz por **esta ordem**:
$$D = (1-\beta)\,D + \beta\,|S - E| \qquad\text{(com o $E$ antigo)}$$
$$E = (1-\alpha)\,E + \alpha\,S$$
$$\textit{timeout} = E + 4D$$
Valores típicos: $\alpha = 0{,}125$ e $\beta = 0{,}25$. Usa os valores do enunciado.
:::

::: {.exemplo title="--- Exame 2025/26: E = 20, D = 5, S = 10 (ms), alfa = 0,1 e beta = 0,2"}
1. $D = 0{,}8\times5 + 0{,}2\times|10-20| = 4 + 2 = 6$ ms.
2. $E = 0{,}9\times20 + 0{,}1\times10 = 18 + 1 = 19$ ms.
3. *timeout* $= 19 + 4\times6 = 43$ ms.
:::

- **Não** se mede o RTT de um segmento repetido. Não se sabe a que envio pertence o ACK.
- **Há um *timeout*:** o TCP **duplica** o valor do temporizador. Assim, um RTT que subiu de repente não causa *timeouts* sem fim.
- O peso de cada amostra, com $\alpha = 0{,}1$: a mais recente 10 %, a anterior 9 %, a seguinte 8,1 %.
- Chama-se média **exponencial** porque o peso de uma amostra é multiplicado por $(1-\alpha)$ sempre que chega outra.

::: {.exemplo title="--- Escrever E em função das amostras (F7.3)"}
$S(1)$ é a amostra mais recente. O primeiro $E$ é a amostra mais antiga. Com 4 amostras:
$$E = \alpha S(1) + \alpha(1-\alpha) S(2) + \alpha(1-\alpha)^2 S(3) + (1-\alpha)^3 S(4)$$
Com $\alpha = 0{,}1$: $E = 0{,}1\,S(1) + 0{,}09\,S(2) + 0{,}081\,S(3) + 0{,}729\,S(4)$. Com $n$ amostras:
$$E \approx \alpha\sum_{i=1}^{n}(1-\alpha)^{i-1}\,S(i)$$
:::

::: {.exemplo title="--- Tabela de oito amostras, com alfa = 0,1 e beta = 0,2 (F7.3)"}
Começa com $E = 54$ (a 1.ª amostra) e $D = 27$ (metade). A 1.ª amostra também entra na tabela.

| $S$ | $\lvert S-E\rvert$ | $D$ novo | $E$ novo | *timeout* |
|--:|--:|--:|--:|--:|
| 54 | 0 | 21,6 | 54 | 140,4 |
| 63 | 9 | 19,08 | 54,9 | 131,22 |
| 55 | 0,1 | 15,284 | 54,91 | 116,05 |
| 57 | 2,09 | 12,645 | 55,119 | 105,70 |
| 68 | 12,881 | 12,692 | 56,407 | 107,18 |
| 56 | 0,407 | 10,235 | 56,366 | 97,31 |
| 55 | 1,366 | 8,462 | 56,230 | 90,08 |
| 58 | 1,770 | 7,123 | 56,407 | **84,90** |

Linha do 63: $D = 0{,}8\times21{,}6 + 0{,}2\times9 = 19{,}08$ e $E = 0{,}9\times54 + 0{,}1\times63 = 54{,}9$.
:::

# Tema 5 --- TCP: controlo de fluxo e conexões

## Controlo de fluxo

**Objetivo:** o emissor não pode encher o *buffer* do **receptor**.

O receptor escreve em cada segmento o espaço livre que tem:
$$\text{RcvWindow} = \text{RcvBuffer} - (\text{LastByteRcvd} - \text{LastByteRead})$$
O emissor cumpre: $\text{LastByteSent} - \text{LastByteAcked} \le \text{RcvWindow}$.

::: {.exemplo title="--- Buffer de 4000 bytes"}
O receptor recebeu os bytes 0 a 2999. A aplicação leu os bytes 0 a 999.

1. Ocupado: $2999 - 999 = 2000$ bytes. Livre: $4000 - 2000 = 2000$ bytes.
2. O último byte com ACK é o 2999. O emissor pode enviar até ao byte $2999 + 2000 = 4999$.
3. Chegam mais 2000 bytes e a aplicação não lê. A janela passa a **0**.
4. O emissor envia segmentos de **1 byte**. Cada ACK diz-lhe se já há espaço.
:::

| | controlo de fluxo | controlo de congestionamento |
|:--------|:-------------------|:-------------------|
| protege | o receptor | a rede |
| entra em ação quando | a aplicação lê devagar | há perdas (3 ACKs duplicados ou *timeout*) |
| quem dá o limite | o receptor (RcvWindow) | o emissor (CongWin), pelas perdas que vê |

## Abrir a conexão: 3 mensagens

1. Cliente → servidor: **SYN**, número $x$. Sem dados.
2. Servidor → cliente: **SYN + ACK**, número $y$, ACK $= x+1$.
3. Cliente → servidor: **ACK** $= y+1$. Já pode levar dados.

O SYN conta como 1 byte. Por isso o ACK é $x+1$ ou $y+1$.

**Para que serve:** cada lado diz o seu número inicial e sabe que o outro o recebeu. Os dois lados reservam os *buffers*.

**Porque são 3 e não 2?** Um SYN antigo pode chegar atrasado. Com 2 mensagens, o servidor abria uma conexão que o cliente não pediu.

## Fechar a conexão: 4 mensagens

1. Cliente: **FIN**.
2. Servidor: **ACK**. Ainda pode enviar dados.
3. Servidor: **FIN**, quando acabar.
4. Cliente: **ACK**. Fica em **TIME_WAIT** (2 vezes o tempo de vida de um segmento) e só depois fecha.

O servidor também pode fechar primeiro. Fica em TIME_WAIT quem fecha primeiro.

**Porque existe o TIME_WAIT?** O último ACK pode perder-se. O servidor repete o FIN e o cliente ainda lhe responde.

![](figuras/tcp_conexao.pdf){width=82%}

**Estados do cliente:** CLOSED, SYN_SENT, ESTABLISHED, FIN_WAIT_1, FIN_WAIT_2, TIME_WAIT, CLOSED.

**CLOSE_WAIT:** o servidor já respondeu ao FIN, mas a aplicação dele ainda não fechou.

**Estados do servidor:** CLOSED, LISTEN, SYN_RCVD, ESTABLISHED, CLOSE_WAIT, LAST_ACK, CLOSED.

# Tema 6 --- Controlo de congestionamento

## O problema

**Congestionamento:** os emissores enviam mais do que a rede aguenta.

**Sinais:** atrasos grandes (filas nos *routers*) e perdas (filas cheias).

| cenário | custo |
|:-----------------|:---------------------------------------|
| fila infinita | o débito chega a $R/2$ para cada um, mas o atraso cresce sem limite |
| fila finita, com repetições | o emissor gasta capacidade em repetições; algumas são desnecessárias |
| vários saltos | um pacote perdido desperdiça a capacidade dos saltos anteriores; o débito útil pode cair para 0 (**colapso**) |

## Como o TCP reage

Os *routers* não ajudam. O emissor vê as perdas e muda a **janela de congestionamento** (CongWin).
$$\text{LastByteSent} - \text{LastByteAcked} \le \min(\text{CongWin}, \text{RcvWindow}) \qquad \text{débito} \approx \frac{\text{CongWin}}{RTT}$$

Há duas fases. O **limiar** (*ssthresh*) separa-as.

| fase | quando | por cada ACK | por cada RTT |
|:------------|:-------------|:-------------|:-------------|
| *slow start* (SS) | abaixo do limiar | +1 MSS | a janela **duplica** |
| *congestion avoidance* (CA) | acima do limiar | +MSS·(MSS/CongWin) | a janela soma **1 MSS** |

::: {.definicao title="--- O que acontece numa perda (TCP Reno)"}
| perda | limiar novo | janela nova | fase seguinte |
|:-----------|:-----------|:-----------|:-----------|
| 3 ACKs duplicados | janela / 2 | igual ao limiar novo | CA |
| *timeout* | janela / 2 | 1 MSS | SS |
:::

- **3 ACKs duplicados:** outros segmentos ainda chegam. O problema é leve. Corta para metade.
- ***Timeout*:** não chega nada. O problema é grave. Volta a 1.
- **TCP Tahoe** (mais antigo): volta a 1 nos **dois** casos.
- Um ou dois ACKs duplicados não mudam a janela.
- **AIMD:** soma 1 por RTT sem perdas; divide por 2 numa perda. O gráfico parece dentes de serra.

## Ler o gráfico da janela

::: {.definicao title="--- Receita: ler o gráfico"}
1. A curva duplica: **SS**. A curva sobe em reta: **CA**.
2. Cai para metade: **3 ACKs duplicados**. Cai para 1: ***timeout***.
3. Muda de curva para reta **sem cair**: chegou ao **limiar**. Não é uma perda.
4. Limiar num instante = metade da janela na **última perda**. Não muda até à perda seguinte.
5. Em que ronda sai o segmento número $k$? Soma as janelas, ronda a ronda, até chegares a $k$.
6. Em SS, se o dobro passa o limiar, a janela fica **no limiar**. Essa ronda ainda é SS.
:::

::: {.exemplo title="--- Limiar inicial 8; 3 ACKs duplicados na ronda 8; timeout na ronda 11"}
| ronda | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| janela | 1 | 2 | 4 | 8 | 9 | 10 | 11 | 12 | 6 | 7 | 8 | 1 | 2 | 4 | 5 | 6 |
| limiar | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 6 | 6 | 6 | 4 | 4 | 4 | 4 | 4 |
| fase | SS | SS | SS | SS | CA | CA | CA | CA | CA | CA | CA | SS | SS | SS | CA | CA |

1. Rondas 1 a 4: duplica até ao limiar 8.
2. Rondas 5 a 8: soma 1 por ronda, até 12.
3. Perda na ronda 8: limiar $= 12/2 = 6$. Janela $= 6$. Continua em CA.
4. *Timeout* na ronda 11: limiar $= 8/2 = 4$. Janela $= 1$. Volta a SS.
5. O 30.º segmento: rondas 1 a 5 dão $1+2+4+8+9 = 24$. Com a ronda 6 dá 34. Sai na **ronda 6**.
:::

![](figuras/reno_exemplo.pdf){width=66%}

::: {.exemplo title="--- Gráfico da Ficha 7 (F7.4)"}
![](figuras/reno_f7.pdf){width=58%}

| pergunta | resposta |
|:------------|:------------------------------|
| onde está em SS? | rondas 1 a 6 e 23 a 26 (duplica) |
| onde está em CA? | rondas 7 a 22 (soma 1) |
| perda na ronda 16 | 42 cai para 21: 3 ACKs duplicados |
| perda na ronda 22 | 26 cai para 1: *timeout* |
| limiar inicial | 32 (a curva passa a reta) |
| limiar na ronda 18 | $42/2 = 21$ |
| limiar na ronda 24 | $26/2 = 13$ |
| ronda do 70.º segmento | soma: 1, 3, 7, 15, 31, 63, **96**. Ronda 7 |
| 3 ACKs duplicados depois da ronda 26 | a janela era 8: limiar 4 e janela 4 |

**3 RTT depois da perda com 42:** 21, 22, **23**. O limiar fica em 21.
:::

::: {.exemplo title="--- Exame 2025/26: gráfico de 70 RTT (o enunciado dá o gráfico)"}
![](figuras/reno_exame25.pdf){width=62%}

| instante | o que se vê no gráfico | resposta |
|:---:|:----------------|:--------------------------|
| 8 | 128 cai para 64 | 3 ACKs duplicados; limiar 64 |
| 25 | 80 cai para 40 | 3 ACKs duplicados; limiar 40 |
| 46 | 60 cai para 1 | *timeout*; limiar 30 |
| 52 | curva passa a reta, sem cair | chegou ao limiar 30; não é perda |

- **Limiar:** em 20 é 64. Em 40 é 40. Em 50 e 60 é 30.
- **Fase:** em 5 é SS. Em 20 é CA. Em 50 é SS. Em 60 é CA.

*O gráfico foi refeito a partir do enunciado. A foto do exame não o mostra.*
:::

## Débito médio e perdas

A janela anda entre $W/2$ e $W$. A média é $0{,}75\,W$:
$$\text{débito médio} = \frac{0{,}75\,W\cdot\text{MSS}}{RTT} \qquad\qquad \text{débito} \approx \frac{1{,}22\cdot\text{MSS}}{RTT\sqrt{L}}$$

::: {.exemplo title="--- De onde vem o 1,22 (F8.1)"}
1. Num ciclo, a janela sobe de $W/2$ até $W$, 1 por RTT. São cerca de $W/2$ rondas.
2. Cada ronda envia, em média, $\frac34 W$ segmentos. Total: $\frac W2\cdot\frac34 W = \frac38 W^2$.
3. Perde-se 1 segmento por ciclo: $L \approx 1/(\frac38 W^2) = 8/(3W^2)$.
4. Logo $W = \sqrt{8/(3L)}$.
5. Débito $= \frac34\cdot\sqrt{8/(3L)}\cdot\text{MSS}/RTT \approx 1{,}22\cdot\text{MSS}/(RTT\sqrt L)$.
:::

**$L$ sobe 4 vezes:** o débito cai para metade, porque $\sqrt 4 = 2$.

**Ligações longas e rápidas:** 10 Gbps, RTT de 100 ms e segmentos de 1500 bytes pedem uma
janela de $10^{10}\times0{,}1/(1500\times8) \approx 83\,333$ segmentos. A taxa de perdas tem de ser $2\times10^{-10}$. O TCP normal não chega.

## Equidade

**Objetivo:** $K$ conexões numa ligação $R$ recebem $R/K$ cada uma.

**Porque o TCP é justo:** as duas conexões somam o mesmo. Na perda, a que tem mais perde mais. Os débitos ficam iguais.

**Duas falhas:**

- **UDP** não reduz o débito.
- **Várias conexões:** com 9 conexões na ligação, uma aplicação que abre 1 fica com $R/10$. Uma que abre 10 fica com $10/19$, cerca de $R/2$.

# Tema 7 --- Camada de rede e routers

## Duas funções

- **Encaminhamento** (*routing*): escolher o **caminho** da origem ao destino. Preenche a tabela.
- **Reenvio** (*forwarding*): dentro de um *router*, passar o pacote da **entrada** para a **saída** certa.

*Encaminhamento é planear a viagem. Reenvio é mudar de comboio numa estação.*

**Objetivo da camada de rede:** levar pacotes entre máquinas que podem não estar ligadas diretamente.

- **3.ª função, só em redes com CV** (ATM, *frame relay*, X.25): estabelecer a conexão. O IP não a tem.
- O **controlo de acesso ao meio** não é da camada de rede. É da camada de ligação.

A camada de rede corre nos terminais **e em todos os *routers***.

A Internet dá **melhor esforço** (*best effort*). Não garante entrega, ordem, atraso, débito nem limite ao *jitter* (a variação do espaço entre pacotes).

## Circuitos virtuais e datagramas

| | circuitos virtuais (CV) | datagramas (Internet) |
|:---------|:-------------------|:-------------------|
| antes dos dados | abre um circuito | nada |
| o pacote leva | o número de CV | o endereço de destino |
| estado no *router* | por conexão: cresce com $O(n^2)$ | não guarda por fluxo |
| primeiro pacote | demora mais (abre o circuito) | sai logo |
| caminho | fixo | pode mudar de pacote para pacote |
| ordem | mantém-se | pode trocar |
| perdas | pode haver | pode haver |
| reservar recursos | é fácil | é difícil |
| falha de uma ligação | o circuito cai | os pacotes seguem por outro caminho |
| melhor para | garantias (vídeo, voz) | redes que falham |
| exemplo | ATM, *frame relay*, X.25 | IP |

**O número de CV muda em cada ligação.** O *router* lê o número à entrada e escreve outro à saída.
Assim, cada ligação escolhe os seus números sem falar com o resto da rede.

**Exemplo:** na tabela está "entrada 1, CV 12 → saída 3, CV 22". O pacote entra pela 1 com o 12 e sai pela 3 com o 22.

**CV e conexão TCP não são o mesmo.** No CV, os *routers* guardam estado. No TCP, só os dois terminais sabem da conexão.

**Porque o ATM usa CV:** vem da rede telefónica. A voz precisa de tempo e entrega garantidos. Os telefones são simples, por isso a complexidade está **na rede**.

**Porque a Internet usa datagramas:** liga computadores, que se adaptam e recuperam erros. A complexidade está **nos terminais**. Há muitos tipos de ligação e um serviço igual para todos é difícil.

**Reservar recursos por fluxo:** dá débito e atraso garantidos. Custa estado por fluxo nos *routers* ($O(n^2)$), e o que se reserva e não se usa é desperdício.

**Que atraso se controla sem mudar o *hardware*?** Só o atraso na **fila de espera**, com menos congestionamento.

## Prefixo mais longo

Há mais de 4 mil milhões de endereços. A tabela guarda **prefixos**.
Se vários prefixos encaixam, **ganha o mais longo**. Só existe nos datagramas.

::: {.exemplo title="--- Escolher a interface"}
| prefixo | interface |
|:--|:--:|
| `11001000 00010111 00010` | 0 |
| `11001000 00010111 00011000` | 1 |
| `11001000 00010111 00011` | 2 |
| outro | 3 |

Os dois primeiros bytes são `11001000 00010111`. Olha para o terceiro byte.

- `00010110`: encaixa só no 0. **Interface 0.**
- `00011000`: encaixa no 1 (24 bits) e no 2 (21 bits). O 1 é mais longo. **Interface 1.**
- `00011111`: encaixa só no 2. **Interface 2.**

Se o segundo byte for `00010110`, não encaixa em nenhum. **Interface 3.**
:::

## Dentro de um *router*

![](figuras/router.pdf){width=62%}

- **Plano de controlo:** o processador corre o encaminhamento (RIP, OSPF, BGP).
- **Plano de dados:** as interfaces e a matriz fazem o reenvio.

**Três partes do plano de dados:**

1. **Entrada:** recebe os bits. Procura a saída na sua **cópia da tabela**.
2. **Matriz:** leva o pacote da entrada à saída.
3. **Saída:** guarda o pacote na fila e transmite-o. Um algoritmo escolhe o próximo (normalmente FIFO).

| tipo de matriz | limite |
|:-------------|:-----------------------------------|
| memória | cada pacote passa **2 vezes** no barramento |
| barramento | um só barramento, partilhado por todos |
| rede de interligação | passa vários pacotes ao mesmo tempo; pode partir o pacote em células iguais |

**Fila na entrada:** a matriz é mais lenta do que as entradas juntas.
**Bloqueio HOL:** o primeiro da fila espera por uma saída ocupada. Os de trás também esperam, mesmo com a saída deles livre.

**Fila na saída:** chegam pacotes mais depressa do que a ligação os transmite. É aqui a maior parte do atraso e das perdas.

**Tamanho do *buffer*:** RTT × C. Exemplo: $0{,}25\text{ s}\times10\text{ Gbps} = 2{,}5$ Gbit.
Com $N$ fluxos: $RTT\cdot C/\sqrt N$. Um *buffer* grande demais só cria atraso (*bufferbloat*).

# Tema 8 --- IP e fragmentação

## O cabeçalho IP (20 bytes)

| campo | para que serve |
|:-----------|:-----------------------------------------|
| versão | 4 |
| tamanho do cabeçalho | diz onde começam os dados (20 bytes sem opções) |
| tipo de serviço | o tipo de tratamento do datagrama |
| comprimento total | cabeçalho e dados, em bytes |
| identificador (ID) | junta os fragmentos do mesmo datagrama |
| *flags* DF e MF | DF: não fragmentar. MF: há mais fragmentos |
| *offset* | a posição dos dados, em unidades de **8 bytes** |
| TTL | saltos que faltam; desce 1 em cada *router*; em 0 deita-se fora; evita que o datagrama ande em círculos |
| protocolo | a quem entregar: 6 = TCP, 17 = UDP |
| *checksum* | **só do cabeçalho**; cada *router* calcula-o outra vez, porque o TTL muda |
| IP de origem e de destino | 32 bits cada |

Um segmento TCP num datagrama IP gasta $20 + 20 = 40$ bytes de cabeçalhos. Com 1460 bytes de dados: $40/1460 \approx 2{,}7\,\%$.

## Fragmentar

Uma ligação aceita no máximo a sua **MTU**. O *router* parte um datagrama maior em fragmentos.

**Quem junta os fragmentos? Só o destino.** Há duas razões:

- Os fragmentos podem seguir caminhos diferentes. Só o destino os vê todos.
- Os *routers* não gastam tempo nem memória com isso.

Com DF = 1, o *router* não fragmenta. Se o datagrama não cabe, deita-o fora.

::: {.definicao title="--- Receita: fragmentar"}
1. Dados = comprimento total $-$ 20.
2. Dados por fragmento = MTU $-$ 20, **para baixo** até um múltiplo de 8.
3. Divide. O último fragmento leva o resto.
4. Em cada fragmento:
    - comprimento = dados + 20;
    - ID igual em todos;
    - MF = 1, e 0 no último;
    - *offset* = bytes de dados **antes** deste, a dividir por 8.
5. Confirma: *offset* do último × 8 + dados do último = total de dados.
:::

::: {.exemplo title="--- 4000 bytes, MTU 1500"}
Dados: $4000 - 20 = 3980$. Por fragmento: $1500 - 20 = 1480 = 8\times185$.

| fragmento | dados | comprimento | MF | *offset* |
|:--:|--:|--:|:--:|--:|
| 1 | 1480 | 1500 | 1 | 0 |
| 2 | 1480 | 1500 | 1 | 185 |
| 3 | 1020 | 1040 | 0 | 370 |

Confirma: $370\times8 + 1020 = 2960 + 1020 = 3980$.
:::

::: {.exemplo title="--- 1500 bytes, MTU 600: aqui há arredondamento (F8.3)"}
Dados: $1480$. Por fragmento: $600 - 20 = 580$. Não é múltiplo de 8. Desce para $576 = 8\times72$.

| fragmento | dados | comprimento | MF | *offset* |
|:--:|--:|--:|:--:|--:|
| 1 | 576 | 596 | 1 | 0 |
| 2 | 576 | 596 | 1 | 72 |
| 3 | 328 | 348 | 0 | 144 |

Confirma: $144\times8 + 328 = 1152 + 328 = 1480$.
:::

::: {.exemplo title="--- Overhead no exemplo anterior (F8.3)"}
***Overhead*** = bytes de cabeçalho a dividir pelos bytes de dados.

| | sem fragmentar | com 3 fragmentos |
|:-----------|:-----------|:-----------|
| só IP (1480 de dados) | $20/1480 \approx 1{,}4\,\%$ | $60/1480 \approx 4{,}1\,\%$ |
| IP e TCP (1460 de dados) | $40/1460 \approx 2{,}7\,\%$ | $80/1460 \approx 5{,}5\,\%$ |

O cabeçalho TCP vai **só no 1.º fragmento**: $3\times20 + 20 = 80$ bytes. A solução oficial escreve 5,4 % na última conta, porque divide 80 por 1480.
:::

::: {.exemplo title="--- Partir um fragmento: MTU 620, no exemplo dos 4000 bytes"}
Por fragmento: $620 - 20 = 600 = 8\times75$. O *offset* conta **sempre** desde o datagrama original.

| parte-se | dados | comprimento | MF | *offset* |
|:--|--:|--:|:--:|--:|
| fragmento 1 | 600 | 620 | 1 | 0 |
| | 600 | 620 | 1 | 75 |
| | 280 | 300 | **1** | 150 |
| fragmento 3 | 600 | 620 | 1 | 370 |
| | 420 | 440 | 0 | 445 |

A última parte fica com o MF do fragmento que se partiu. O fragmento 1 tinha MF = 1.
:::

**Como sabe o destino que tem tudo?** Tem um fragmento com *offset* 0. Tem um com MF = 0. Não há buracos entre eles.

# Tema 9 --- Antes de entrar no teste

## Erros que custam pontos

| erro | certo |
|:----------------------|:----------------------------|
| somar 1 por segmento no TCP | soma os **bytes** |
| 3 ACKs iguais já dão retransmissão rápida | são 3 **duplicados**: 4 iguais |
| no *timeout*, o TCP repete tudo | repete **só** o mais antigo (o GBN é que repete tudo) |
| o ACK diz o último byte recebido | diz o **próximo** byte esperado |
| o ACK do GBN também é o próximo | no GBN, ACK($n$) confirma **até $n$** |
| *slow start* é lento | é **exponencial** |
| o limiar muda quando a janela lá chega | só muda numa **perda** |
| chegar ao limiar é uma perda | só muda de SS para CA |
| usar o $E$ novo no desvio | usa o $E$ **antigo** |
| MTU são só dados | a MTU **inclui** o cabeçalho IP |
| *offset* em bytes | em unidades de **8 bytes** |
| os *routers* juntam fragmentos | só o **destino** |
| controlo de fluxo protege a rede | protege o **receptor** |
| o *checksum* corrige erros | só **deteta** |
| só há TIME_WAIT no cliente | fica em TIME_WAIT **quem fecha primeiro** |
| num CV não há perdas | não há **trocas de ordem**; perdas pode haver |
| esquecer bytes → bits em $L/R$ | multiplica por 8 |

## Perguntas de escrever: a resposta curta

| pergunta | resposta |
|:----------------|:-------------------------------------------|
| Porque usar UDP? | Não espera pela conexão, não guarda estado, o cabeçalho é pequeno e o débito é livre. |
| Porque ter números nos ACKs? | Um ACK atrasado confirmava o pacote errado. |
| Porque são 3 mensagens a abrir? | Os dois lados confirmam os números iniciais e um SYN antigo não abre nada. |
| Porque existe o TIME_WAIT? | O último ACK pode perder-se e o FIN é repetido. |
| Porque não medir segmentos repetidos? | Não se sabe a que envio pertence o ACK. |
| Porque tratar as perdas de modo diferente? | Com 3 ACKs duplicados a rede ainda entrega; com *timeout* não. |
| Porque precisa o SR de $2N$ números? | O receptor não distingue um pacote novo de um repetido. |
| Porque remontar só no destino? | Só ele vê todos os fragmentos e os *routers* ficam livres. |
| Porque múltiplos de 8? | O *offset* tem 13 bits e conta de 8 em 8 bytes. |
| Porque recalcular o *checksum* IP? | O TTL muda em cada *router*. |
