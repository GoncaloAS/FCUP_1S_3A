# Soluções da Ficha de Exercícios nº 8

*Última alteração: segunda-feira, 14 de setembro de 2026 às 17:43*

1. [Resolução neste PDF](/pluginfile.php/134455/mod_page/content/19/F8ex1.pdf)

 

2.a) Desvantagens dos circuitos virtuais (vs datagramas): obrigam a armazenar informação de estado para cada fluxo de pacotes (entre pares de máquinas), crescendo com O(*n* ^2^) no número de terminais; dificultam recuperar da falha de um nó ou ligação; demora mais até se poder enviar o primeiro pacote. Vantagens dos circuitos virtuais (vs datagramas): garantem entrega ordenada de pacotes; facilitam integração com reserva de recursos para cada fluxo.

 

2.b) Datagramas

 

2.c) Circuitos virtuais

 

2.d) Serve para agrupar endereços de destino na tabela de encaminhamento, permitindo usar o caminho mais específico possível para cada pacote. É usada apenas em redes de datagramas (com circuitos virtuais é feito encaixe completo/exacto).

 

2.e) Como todos os pacotes seguem o mesmo caminho, a sua ordem não é alterada.

 

3.a) 1500 bytes no total => 1480 bytes de dados
1º fragmento (576 bytes de dados, sobram 904): len=596, id=X, df=0, mf=1, offset=0
2º fragmento (576 bytes de dados, sobram 328): len=596, id=X, df=0, mf=1, offset=72 (=576/8)
3º fragmento (328 bytes de dados, sobram 0): len=348, id=X, df=0, mf=0, offset=144 (=1152/8)

 

3.b) sem fragmentação: 20 bytes, 1.4% (em relação aos dados da aplicação) com fragmentação: 60 bytes, 4.1% (em relação aos dados da aplicação)

 

NOTA: Também é comum calcular o overhead em relação ao tamanho total. Nesse caso, os valores seriam, respectivamente, 1.3% (sem fragmentação) e 3.9% (com fragmentação).

 

3.c) sem fragmentação: 40 bytes, 2.7% (em relação aos dados da aplicação)
com fragmentação: 80 bytes, 5.4% (em relação aos dados da aplicação)

 

NOTA: Se fosse em relação ao tamanho total, os valores seriam, respectivamente, 2.7% (sem fragmentação) e 5.2% (com fragmentação).

 

3.d) Nó de destino, para evitar sobrecarregar routers e (sobretudo) porque é o único nó onde garantidamente todos os fragmentos convergem.

 

3.e) Porque a informação sobre as portas está no cabeçalho TCP, que está no início do campo de dados do datagrama IP e, portanto, apenas no primeiro fragmento. Para compatibilizar, a remontagem teria que ser feita no router NAT.

 

4.a) Porque ao fazer AND bit a bit dela com o endereço IP de destino, os bits a zero na máscara vão mascarar a parte de *host* do endereço IP, deixando apenas o prefixo.

 

4.b) 
192.168.10.0/24
192.168.18.0/23
10.0.0.0/8 (ppp)
127.0.0.0/8 (loopback)

 

4.c)
194.117.24.32 — 192.168.10.20 (default)
10.0.3.5 — 10.0.3.5 (directa)
192.168.72.4 — 192.168.10.5
192.168.1.214 — 192.168.10.7

 

Ver [esta tabela](/pluginfile.php/134455/mod_page/content/19/4c.png).

 

4.d) Rota default. Encaixa em todos os endereços IP, mas é a menos específica de todas (prefixo mais curto), pelo que só é usada se o endereço não encaixar em mais nenhuma.

 

4.e) Corresponde à interface de *loopback* , uma interface lógica que serve para permitir comunicação TCP/IP entre programas a correr na mesma máquina mesmo que esteja desligada da rede.

 

5.a) A rede tenta entregar os pacotes mas não dá quaisquer garantias (podem perder-se, ser entregues fora de ordem, não há limite de atraso ou *jitter* , não há garantia de débito mínimo).

 

5.b) Apenas o atraso na fila de espera (baixando o nível de congestionamento).

 

5.c) Vantagens: melhor qualidade de serviço, melhor experiência do utilizador. Desvantagens: obriga a manter informação de estado por fluxo, que potencialmente cresce com O(*n* ^2^) no número de terminais.
