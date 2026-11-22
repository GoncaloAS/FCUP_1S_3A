# Soluções da Ficha de Exercícios nº 7

*Última alteração: segunda-feira, 14 de setembro de 2026 às 17:42*

```
1. Controlo de fluxo: pretende evitar que o emissor envie mais rápido do que o receptor consegue processar. A entidade activa é o receptor, que anuncia ao emissor a Receiver Window (espaço livre em buffer).
   Controlo de congestionamento: pretende evitar que o emissor envie mais rápido do que a rede consegue transportar até ao receptor. A entidade activa é o emissor, que infere congestionamento a partir de eventos indicadores de perda (3dupAck ou timeout) e reage a ele diminuindo a Congestion Window.
   Tanto a Receiver Window como a Congestion Window são limites superiores à janela de pipelining do TCP.
```

 

```
2.a. SYN, SYN+ACK e ACK (consultar slides das aulas teóricas e livro)
```

 

```
2.b. FIN e ACK + FIN e ACK (consultar slides das aulas teóricas e livro)
```

 

```
3.a. 
```

 

```

```

 

```
3.b. Aproximadamente 
```

 

```
3.c. Por causa do expoente i-1: cada amostra perde exponencialmente peso à medida que novas amostras vão chegando.
```

 

```
3.d. 84.9 ms
```

 

```
3.e. Quando é recebido um Ack para um segmento retransmitido, não se sabe se corresponde à primeira transmissão ou à retransmissão, pelo que não é claro qual o valor de RTT que representa.  Por este motivo, Acks para segmentos retransmitidos não são usados como amostras do RTT.
```

 

```
3.f. Por cada timeout, o TCP duplica o valor do temporizador, de modo a evitar que ocorra timeout para todos os segmentos e, por serem retransmitidos, a estimativa do RTT deixe de ser actualizada.
```

 

```
4.a. [1,6] e [23,26]
```

 

```
4.b. [7,22]
```

 

```
4.c. 3dupAck porque a janela é reduzida a metade.
```

 

```
4.d. Timeout porque a janela é reduzida a 1MSS.
```

 

```
4.e. 32 MSS
```

 

```
4.f. 21 MSS
```

 

```
4.g. 13 MSS
```

 

```
4.h. 7ª ronda
```

 

```
4.i. 4 MSS (ambos)
```

 

```
5.a. MSS
```

 

```
5.b. MSS/n  onde n=CongWin/MSS
```

 

```
6. Ver e.g. https://en.wikipedia.org/wiki/TCP_congestion_control
```

 

```
 
```
