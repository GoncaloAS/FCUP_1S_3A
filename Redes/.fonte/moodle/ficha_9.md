# Ficha de Exercícios nº 9

*Última alteração: segunda-feira, 14 de setembro de 2026 às 17:43*

1. **Especial, especialíssimo:**  Quando um terminal se liga pela primeira vez a uma rede e pretende obter um endereço através do protocolo DHCP, ele envia uma mensagem *DHCP Discover*  dentro dum datagrama IP com endereço de origem 0.0.0.0 e endereço de destino 255.255.255.255. O que significam estes endereços e por que razão são usados nesta mensagem DHCP?
2. **Endereçamento IP e sub-redes:**  Uma rede das tradicionais classes A, B ou C pode ser subdividida em sub-redes classless. 
      1. Uma empresa tem 4 departamentos, cada um com a sua rede, que quer interligar e ligar à Internet. O departamento A tem 10 máquinas, o B tem 19, o C tem 71 e o D tem 37. Supondo que a empresa dispõe da rede classe C 193.136.37.0/24 para dividir pelas várias sub-redes, atribua os endereços e máscaras a essas sub-redes.
      2. O que significa um comprimento de prefixo de 32 bits (/32) associado a uma entrada na tabela de encaminhamento?
      3. Qual é o número mínimo de bits que deve estar reservado para a parte de *host*  numa sub-rede de acesso múltiplo? Porquê?
3. **NATuralmente...**  Suponha que um computador duma rede doméstica por trás dum *router*  NAT envia um pacote com um pedido HTTP a um servidor *web*  na Internet. Esse pacote foi capturado na rede doméstica (antes de atravessar o NAT) e na Internet (depois de atravessar o NAT). O conteúdo dos cabeçalhos IP e TCP do pacote foi analisado nos dois casos, e continha (entre outras) as informações descritas na seguinte tabela: 
   |  | Cabeçalho IP | Cabeçalho TCP |
   | Src IP | Dst IP | Src port | Dst port |
   | Na rede doméstica | 192.168.1.23 | 193.136.39.12 | 33516 | 80 |
   | Na Internet | 89.155.236.7 | 193.136.39.12 | 62318 | 80 |
    
      1. Com base na informação da tabela diga se é possível saber cada um dos seguintes endereços IP e, em caso afirmativo, qual é: 
               - Computador na rede doméstica
               - Interface interna do *router*  NAT
               - Interface externa do *router*  NAT
               - Servidor *web*  na Internet
      2. Se fosse capturado na Internet um pacote da resposta a esse pedido, que endereços e portas de origem e destino teria? E se esse pacote de resposta fosse capturado já na rede doméstica?
      3. Se quisesse pôr a correr no computador de casa um servidor *web* , que configurações teria que fazer no *router*  NAT?
      4. Que limitações teria essa solução quando comparada com um servidor *web*  normal na Internet? Como poderia mitigá-las?
      5. Seria possível ter um segundo computador na rede doméstica com outro servidor *web*  também visível na Internet? Com que limitações?
4. **Ao fundo do túnel...**  Quando se usam túneis para transportar pacotes IPv6 através de zonas da rede que apenas suportam IPv4, diz-se que o IPv6 lida com o IPv4 como se este fosse um protocolo de ligação de dados. Concorda com esta afirmação? Porquê?
5. **To NAT or not to NAT:**  O NAT com tradução de portas usa-se muito em redes caseiras, mas menos em redes empresariais pelo facto de que complica a instalação de servidores. 
      1. Explique por que razão é fácil ter clientes por trás dum *router*  NAT mas é mais complicado ter servidores.
      2. As aplicações *peer-to-peer*  também têm mais dificuldade em funcionar por trás de NAT. Explique porquê e aponte soluções possíveis para mitigar essa dificuldade.
6. **Eu quero uma rede só para mim!**  Se tem em casa uma rede ligada à Internet através de um pequeno *router* , é provável que os endereços atribuídos aos terminais pelo servidor DHCP integrado no *router*  pertençam à rede 192.168.1.0/24. Isto acontece porque esta rede pertence a um dos blocos de endereços privados. 
      1. O que são e para que servem estes blocos de endereços IP privados?
      2. Descubra todos os blocos reservados para redes privadas no IPv4.
      3. Explique como podem ligar-se redes com endereços privados à Internet, permitindo a comunicação com o exterior.
      4. O que significa o sufixo /24?
