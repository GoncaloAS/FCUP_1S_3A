# Ficha de Exercícios nº 8

*Última alteração: segunda-feira, 14 de setembro de 2026 às 17:42*

1. **De janelas e perdas:**  Considere a descrição macroscópica do funcionamento do TCP Reno na fase de *congestion avoidance* , em que o tamanho da janela em MSSs varia entre *W* /2 e *W* , altura em que a perda de um pacote faz a janela reduzir-se novamente a metade. 
      1. Mostre que, para tamanhos relativamente grandes da janela máxima, *W* , a taxa de perdas é aproximadamente igual a 8/(3·*W* ^2^).
      2. Usando o resultado anterior, mostre que se a taxa de perdas numa conexão TCP for *L* , o seu débito (em Bytes por segundo) será aproximadamente 1.22·*MSS* /(*RTT* ·√*L* ).
2. **Circuitos virtuais vs. datagramas:**  Considere as arquitecturas de rede baseadas na comutação de circuitos virtuais e de datagramas. 
      1. Indique vantagens e inconvenientes de cada uma delas.
      2. Qual considera mais adequada para usar numa rede em que as ligações podem falhar com alguma frequência?
      3. Se projectasse uma rede para o transporte de fluxos multimédia que necessitassem de garantias (débito mínimo, atraso máximo), qual delas usaria?
      4. Explique para que serve o encaixe de prefixo mais longo (*longest prefix matching* ), justificando a sua utilização ou não em cada um destes tipos de arquitectura.
      5. Numa rede com comutação de circuitos virtuais podem ocorrer perdas, mas não reordenamento de pacotes. Justifique este facto.
3. **Quem parte e reparte...**  Um datagrama IP com o comprimento total de 1500 bytes chega a um *router*  onde a interface para o próximo salto tem uma unidade máxima de transferência (MTU) de 600 bytes. 
      1. Assumindo que o datagrama não tem opções no cabeçalho IP, explique como vai ser feita a fragmentação do datagrama, indicando o conteúdo dos campos relevantes do cabeçalho IP para cada um dos fragmentos.
      2. Calcule, em *bytes*  e em percentagem, o *overhead*  dos cabeçalhos IP (assumindo que não são usadas opções) com e sem fragmentação.
      3. Se a aplicação usar TCP (também sem opções), recalcule os *overheads*  tendo em conta também os cabeçalhos de transporte.
      4. Em que nó da rede vai ocorrer a remontagem dos fragmentos? Dê duas razões para ser nesse nó.
      5. Em geral, a fragmentação de pacotes é incompatível com o uso de NAT com tradução de portas. Explique porquê e diga que medidas podem tomar-se para os compatibilizar.
4. **É por aqui!**  A tabela de encaminhamento de um *router*  Linux (obtida com o comando `netstat -nr`) é a seguinte: 
   ```
   Destination    Gateway       Genmask          Flags   Metric  Ref    Use  Iface
   192.168.5.20   192.168.10.7  255.255.255.255  UGH     1       0      180  eth1
   192.168.1.0    192.168.10.5  255.255.255.128  UG      1       0      243  eth1
   192.168.10.0   0.0.0.0       255.255.255.0    U       0       0    63311  eth1
   192.168.0.0    192.168.10.7  255.255.254.0    UG      1       0     2132  eth1
   192.168.18.0   0.0.0.0       255.255.254.0    U       0       0   753430  eth0
   192.168.64.0   192.168.10.5  255.255.192.0    UG      1       0    47543  eth1
   10.0.0.0       0.0.0.0       255.0.0.0        U       0       0     3123  ppp0
   127.0.0.0      0.0.0.0       255.0.0.0        U       0       0      564  lo
   0.0.0.0        192.168.10.20 0.0.0.0          UG      1       0   183436  eth1
   ```
    
      1. Porque razão a máscara de rede tem esta designação? Para que serve ela e como se usa?
      2. Indique em notação CIDR (a.b.c.d/n) as redes às quais o *router*  está directamente ligado.
      3. Qual é o próximo salto para os pacotes com cada um dos seguintes endereços de destino: 194.117.24.32, 10.0.3.5, 192.168.72.4 e 192.168.1.214 ?
      4. Como se designa a última entrada nesta tabela de encaminhamento (0.0.0.0 com máscara 0.0.0.0)? Para que serve esta entrada?
      5. Como se designa e para que serve a rede 127.0.0.0/8?
5. **Modelos de serviço e QoS:**  O modelo de serviço utilizado na Internet é o de melhor esforço (*best effort* ). 
      1. Caracterize este modelo de serviço.
      2. Considere as diversas componentes do atraso de um pacote. Quais delas podem ser controladas (sem alterar o *hardware* )?
      3. Indique quais seriam as vantagens e inconvenientes de efectuar reserva de recursos para cada fluxo na rede.
