# Soluções da Ficha de Exercícios nº 6

*Última alteração: segunda-feira, 14 de setembro de 2026 às 17:41*

```
1.a. Para evitar um problema como este:
```

 

```

```

 

```
1.b. U≈0.029 portanto não é adequado
```

 

```
2.a. No pior caso, a janela do emissor e a do receptor estão completamente desfasadas, mas são contíguas.  Se todos os segmentos nessas janelas tiverem números de sequência diferentes (i.e., o espaço de números de sequência for pelo menos o dobro do tamanho da janela), não é possível o emissor enviar um segmento e ele ser interpretado no receptor como outro mais à frente (com o mesmo número de sequência).
```

 

```
2.b. 
```

 

```

```

 

```
 
```

 

```
3.a. Funções: multiplexagem/desmultiplexagem, detecção de erros (checksum), fiabilidade, controlo de fluxo, controlo de congestionamento.  O UDP só tem as duas primeiras; o TCP tem todas.
```

 

```
3.b. No UDP, o endereço IP de destino e a porta de destino.  No TCP, os endereços IP de origem e destino e as portas de origem e destino (socket associada a conexão, que é identificada pelas duas "pontas").
```

 

```
4.a. 12501 blocos.
```

 

```
4.b. Se não houver perdas, não, porque já há transmissão contínua.  Se puderem ocorrer perdas, sim, porque recuperar de uma perda demora no mínimo um tempo igual ao RTT (e há que encher esse outro RTT com transmissões).
```

 

```
5.a. Olhando para o formato do cabeçalho UDP, as portas de origem e destino são campos de 16 bits logo no início do segmento.  Como os dados estão em Network Order (big endian), a porta de origem é 19050 e a de destino 56104.
```

 

```
5.b. Soma=1010011011100011 (com o campo checksum a zeros)
     Checksum=0101100100011100
```

 

```
5.c. (a soma calculada no receptor tem que ser diferente de tudo uns, indicando que é detectado um erro)
```

 

```
5.d. Na mesma coluna, numa linha substituir um 0 por um 1 e noutra linha substituir um 1 por um 0.
```

 

```
 
```
