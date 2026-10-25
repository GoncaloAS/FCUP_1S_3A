import os
R = "/Users/goncalosousa/Universidade_Primeiro_3_Ano/Redes/"
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fig") + "/"
ALT = "Última alteração: segunda-feira, 14 de setembro de 2026 às 17:40"


def src(p):
    return open(p, encoding="utf-8").read()


# ---------------------------------------------------------------- Ficha 5
f5_var = lambda lang, ex, extra_e, nota: [
    ("h2", f"Versão em {lang}:"),
    ("n", "1.", f"**É só conversa...** O objectivo deste exercício é construir um servidor muito simples de *chat*, "
                f"partindo dum [exemplo de servidor *multiplex* básico](https://moodle2627.up.pt/pluginfile.php/134448/mod_page/content/18/{ex}) "
                f"(`{ex}`, no anexo e nesta pasta), que aceita conexões de clientes e copia o que deles recebe para o *standard output*."),
    ("a", "a)", "Faça *download* do exemplo fornecido, " + ("compile-o e corra-o" if lang == "Java" else "e corra-o") +
                ", passando-lhe como argumento a porta em que o servidor deve correr. Teste-o usando dois telnets para essa porta."),
    ("a", "b)", "Estude o código fornecido de modo a compreender o seu funcionamento†."),
    ("a", "c)", "Altere o código fornecido de modo a que sempre que uma mensagem é recebida numa *socket* ela seja ecoada "
                "para a mesma *socket* em vez de ser impressa para o `stdout`."),
    ("a", "d)", "Altere o programa da alínea anterior de modo a que, em vez de ecoar a mensagem apenas para a mesma *socket*, "
                "a difunda para todos os clientes activos (*sockets* de conexão)."),
    ("a", "e)", "Altere o programa da alínea anterior de modo a difundir, juntamente com a mensagem, o pseudónimo (*nickname*) "
                "de quem a enviou. Por uma questão de simplicidade, assuma que o pseudónimo é a primeira linha que o cliente "
                "envia (não precisa de autenticação nem de verificar se esse pseudónimo já está a ser usado)." + extra_e),
    ("p", nota),
]
F5 = [
    ("p", "Esta ficha de exercícios tem duas variantes. A primeira, em Java, destina-se à maior parte dos estudantes, "
          "incluindo todos os estudantes de cursos do DCC. A segunda, em Python, destina-se a estudantes de cursos de "
          "outros departamentos que nunca tenham programado em Java."),
] + f5_var("Java", "Server.java",
           " Sugestão: use o [método `attach` da `SelectionKey`](https://docs.oracle.com/javase/7/docs/api/java/nio/channels/SelectionKey.html) "
           "para associar o pseudónimo ao `SocketChannel` a que a `SelectionKey` está associada.",
           "† Para compreender melhor a utilidade dos diferentes objectos e métodos utilizados, pode começar por ler "
           "[este tutorial sobre Java NIO](http://tutorials.jenkov.com/java-nio/index.html), particularmente as seguintes partes: "
           "Introduction, Overview, Channel, Buffer, Selector (este é o mais importante), SocketChannel e ServerSocketChannel.") \
  + f5_var("Python", "Server.py", "",
           "† Pode começar por ler este [Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html) para Python.") \
  + [("sp", 8), ("h2", "Anexo — Server.java (exemplo fornecido)"), ("code", src(R + "Praticas/Semana_5/Server.java")),
     ("h2", "Anexo — Server.py (exemplo fornecido)"), ("code", src(R + "Praticas/Semana_5/Server.py"))]

# ---------------------------------------------------------------- Ficha 6
F6 = [
    ("n", "1.", "**Stop-and-wait:** Com vista a garantir fiabilidade numa rede onde podem perder-se pacotes (mas não há erros "
                "de bit), o Fábio Fiável desenvolveu um protocolo simples do tipo stop-and-wait cuja máquina de estados do "
                "emissor se ilustra na figura 1."),
    ("img", FIG + "stop-and-wait.png", 11, "**Figura 1:** Máquina de estados do emissor"),
    ("a", "a)", "Explique ao Fábio por que razão tem que incluir números de sequência também nas confirmações."),
    ("a", "b)", "Será que este protocolo é adequado para usar numa rede a 10Mbps com um atraso de propagação de 20ms e "
                "tamanho máximo de pacote de 1500 bytes?"),
    ("n", "2.", "**Repetições selectivas manuais:** A figura 2 mostra um exemplo de troca de mensagens usando um protocolo do "
                "tipo selective repeat com uma janela de 4 blocos. Note que o tempo avança de cima para baixo, e que em cada "
                "instante só pode enviar-se ou receber-se uma mensagem. As mensagens demoram um tempo constante a ser "
                "transmitidas. São retransmitidas as mensagens para as quais não se recebe a confirmação em 3 unidades de "
                "tempo. Este protocolo permite recuperar de perdas de mensagens. No exemplo, perde-se a confirmação do bloco 1."),
    ("img", FIG + "manual-sack.png", 14, "**Figura 2:** Exemplo de repetições selectivas"),
    ("a", "a)", "Explique por que razão é necessário e suficiente para este protocolo ter uma gama de números de sequência de "
                "duas vezes o tamanho da janela."),
    ("a", "b)", "Numa outra conexão usando este protocolo é necessário transmitir 5 blocos (0 a 4) com uma janela de 3 blocos e "
                "um timeout também de 3 unidades de tempo. Faça um esquema semelhante ao da figura 2 para este cenário, "
                "assumindo que se perdem na rede o bloco 3 e a confirmação do bloco 2."),
    ("n", "3.", "**O transporte:** Tendo em conta o estudo que fez da camada de transporte,"),
    ("a", "a)", "Diga quais são as funções dessa camada. Destas funções, indique quais são comuns aos protocolos de transporte "
                "da pilha TCP/IP e quais existem apenas num deles."),
    ("a", "b)", "Para cada um dos protocolos da camada de transporte na pilha TCP/IP, diga que parâmetros são utilizados para "
                "seleccionar a socket à qual serão entregues os dados recebidos. Justifique a resposta com base nas "
                "características relevantes desses protocolos."),
    ("n", "4.", "**Size matters?** Considere um cabo de fibra óptica com 5000 km e 2 Gbps. Um protocolo do tipo selective repeat "
                "transmite blocos de 1000B."),
    ("a", "a)", "Quantos blocos é que a janela de transmissão precisa de ter para que haja um fluxo contínuo de dados? "
                "(A velocidade da luz na fibra é de aproximadamente 2x10^8^m/s)"),
    ("a", "b)", "Faria sentido aumentar a janela de transmissão para além desse valor? Porquê?"),
    ("n", "5.", "**Checksums:** O Cláudio foi contratado por uma empresa de datagramas para ler cabeçalhos UDP. O datagrama "
                "numero 1857000 tem o seguinte aspecto:"),
    ("code", "01001010 01101010 11011011 00101000\n00000000 00010000 00000000 00000000\n"
             "10100010 10101010 10000001 11110101\n11010001 11101000 10001010 10110111"),
    ("a", "a)", "Quais são as portas de origem e de destino? Qual é o tamanho do datagrama? (em decimal)"),
    ("a", "b)", "Calcule o checksum e adicione-o ao datagrama. Faça a verificação para se certificar de que está correcto."),
    ("a", "c)", "Introduza erros no datagrama resultante e faça nova verificação para ver se são detectados."),
    ("a", "d)", "Descubra um padrão de erros cuja introdução o checksum não permita detectar. Escreva o datagrama defeituoso e "
                "a respectiva verificação."),
]

# ---------------------------------------------------------------- Enunciado do trabalho
QUADRO = [
    ["Estado actual", "Evento", "Acção", "Próximo estado", "Notas"],
    ["init", "`/nick nome` && !disponível(`nome`)", "`ERROR`", "init", ""],
    ["init", "`/nick nome` && disponível(`nome`)", "`OK`", "outside", "`nome` fica indisponível para outros utilizadores"],
    ["outside", "`/join sala`", "`OK` para o utilizador; `JOINED nome` para os outros utilizadores na sala", "inside",
     "entrou na sala `sala`; começa a receber mensagens dessa sala"],
    ["outside", "`/nick nome` && !disponível(`nome`)", "`ERROR`", "outside", "mantém o nome antigo"],
    ["outside", "`/nick nome` && disponível(`nome`)", "`OK`", "outside", ""],
    ["inside", "mensagem", "`MESSAGE nome mensagem` para todos os utilizadores na sala", "inside",
     "necessário escape de / inicial, i.e., / passa a //, // passa a ///, etc."],
    ["inside", "`/nick nome` && !disponível(`nome`)", "`ERROR`", "inside", "mantém o nome antigo"],
    ["inside", "`/nick nome` && disponível(`nome`)", "`OK` para o utilizador; `NEWNICK nome_antigo nome` para os outros utilizadores na sala",
     "inside", ""],
    ["inside", "`/join sala`", "`OK` para o utilizador; `LEFT nome` para os outros utilizadores na sala antiga; "
     "`JOINED nome` para os outros utilizadores na sala nova", "inside",
     "entrou na sala `sala`; começa a receber mensagens dessa sala; deixa de receber mensagens da sala antiga"],
    ["inside", "`/leave`", "`OK` para o utilizador; `LEFT nome` para os outros utilizadores na sala", "outside",
     "deixa de receber mensagens"],
    ["inside", "`/bye`", "`BYE` para o utilizador; `LEFT nome` para os outros utilizadores na sala", "—",
     "servidor fecha a conexão ao cliente"],
    ["inside", "utilizador fechou a conexão", "`LEFT nome` para os outros utilizadores na sala", "—",
     "servidor fecha a conexão ao cliente"],
    ["qualquer excepto inside", "`/bye`", "`BYE` para o utilizador", "—", "servidor fecha a conexão ao cliente"],
    ["qualquer excepto inside", "utilizador fechou a conexão", "—", "—", "servidor fecha a conexão ao cliente"],
    ["qualquer excepto inside", "mensagem", "`ERROR`", "mantém o estado", ""],
    ["qualquer", "comando não suportado nesse estado", "`ERROR`", "mantém o estado", ""],
]
QW = [2.0, 3.6, 5.0, 1.9, 4.5]

DIALOGO = """(cliente estabelece conexão para o servidor)
C→S: /nick maria
S→C: ERROR
C→S: /nick miquinhas
S→C: OK
C→S: /join moda
S→C: OK
S→O: JOINED miquinhas
C→S: Olá a todos!
S→C: MESSAGE miquinhas Olá a todos!
S→O: MESSAGE miquinhas Olá a todos!
S→C: MESSAGE francisca Olá, miquinhas!
S→C: MESSAGE berto Olá, miquinhas!
C→S: /nick micas
S→C: OK
S→O: NEWNICK miquinhas micas
C→S: Tchau!
S→C: MESSAGE micas Tchau!
S→O: MESSAGE micas Tchau!
C→S: /join C++
S→C: OK
S→O: LEFT micas                      (na sala moda)
S→O: JOINED micas                    (na sala C++)
C→S: /// marca o início de um comentário em C++
     (note que o utilizador escreveu  // marca o início de um comentário em C++)
S→C: MESSAGE micas // marca o início de um comentário em C++
S→O: MESSAGE micas // marca o início de um comentário em C++
C→S: /bye
S→C: BYE                             (servidor fecha a conexão à micas)
S→O: LEFT micas"""

TP = [
    ("p", "**Datas (Moodle):** abre domingo, 1 de novembro de 2026, 00:00 · data limite quarta-feira, 9 de dezembro de 2026, "
          "23:59. Grupos de dois (escolha em «Grupos para o trabalho prático»; o teu é o **Grupo 15**)."),
    ("h2", "Introdução"),
    ("p", "O trabalho consiste no desenvolvimento em Java de um servidor de *chat* e de um cliente simples para comunicar com "
          "ele. O servidor deve basear-se no modelo *multiplex*, aconselhando-se usar como ponto de partida o programa "
          "desenvolvido na ficha de exercícios nº 5 das aulas práticas. Quanto ao cliente, deve partir deste esqueleto "
          "(`esqueletos/ChatClient.java`), que implementa uma interface gráfica simples, e completá-lo com a implementação do "
          "lado cliente do protocolo. O cliente deve usar duas *threads*, de modo a poder receber mensagens do servidor "
          "enquanto espera que o utilizador escreva a próxima mensagem ou comando (caso contrário bloquearia na leitura da "
          "*socket*, tornando a interface inoperacional)."),
    ("h2", "Linha de comando"),
    ("p", "O servidor deve estar implementado numa classe chamada `ChatServer` e aceitar como argumento da linha de comando o "
          "número da porta TCP na qual ficará à escuta, por exemplo:"),
    ("code", "java ChatServer 8000"),
    ("p", "O cliente deve estar implementado numa classe chamada `ChatClient` e aceitar como argumentos da linha de comando o "
          "nome DNS do servidor ao qual se quer conectar e o número da porta TCP em que o servidor está à escuta, por exemplo:"),
    ("code", "java ChatClient localhost 8000"),
    ("h2", "Protocolo"),
    ("p", "O protocolo de comunicação é orientado à linha de texto, i.e., cada mensagem enviada pelo cliente ao servidor ou "
          "pelo servidor ao cliente deve terminar com uma mudança de linha, e a mensagem propriamente dita não pode conter "
          "mudanças de linha. Note que o TCP não faz delineação de mensagens, pelo que é possível que uma operação de leitura "
          "da *socket* retorne apenas parte de uma mensagem ou várias mensagens (podendo a primeira e a última ser parciais). "
          "Cabe ao servidor fazer *buffering* por cliente de mensagens parcialmente recebidas^1^."),
    ("p", "As mensagens enviadas pelo cliente ao servidor podem ser comandos ou mensagens simples. Os comandos são do formato "
          "`/comando`, podendo levar argumentos separados por espaços. As mensagens simples apenas podem ser enviadas quando o "
          "utilizador está numa sala de *chat*; se começarem por um ou mais caracteres ‘/’ é necessário fazer o seu escape, "
          "incluindo um carácter ‘/’ adicional (o servidor deve interpretar este caso especial, enviando aos outros "
          "utilizadores da sala a mensagem sem esse carácter extra)^2^; ocorrências de ‘/’ que não sejam no início da linha "
          "não precisam de escape. Este mecanismo de escape garante que, caso surja uma nova versão do protocolo com um "
          "comando adicional e um cliente da nova versão envie esse comando a um servidor que só suporta a antiga, o servidor "
          "não confunde o novo comando com uma mensagem de texto começada por ‘/’."),
    ("p", "O servidor deve suportar os seguintes comandos:"),
    ("b", "`/nick nome` — Usado para escolher um nome ou para mudar de nome. O nome escolhido não pode estar já a ser usado por "
          "outro utilizador."),
    ("b", "`/join sala` — Usado para entrar numa sala de *chat* ou para mudar de sala. Se a sala ainda não existir, é criada."),
    ("b", "`/leave` — Usado para o utilizador sair da sala de *chat* em que se encontra."),
    ("b", "`/bye` — Usado para sair do *chat*."),
    ("p", "As mensagens enviadas pelo servidor ao cliente começam por uma palavra em maiúsculas, indicando o tipo de mensagem, "
          "podendo seguir-se um ou mais argumentos, separados por espaços. O servidor pode enviar as seguintes mensagens:"),
    ("b", "`OK` — Usado para indicar sucesso do comando enviado pelo cliente."),
    ("b", "`ERROR` — Usado para indicar insucesso do comando enviado pelo cliente."),
    ("b", "`MESSAGE nome mensagem` — Usado para difundir aos utilizadores numa sala a `mensagem` (simples) enviada pelo "
          "utilizador `nome`, também nessa sala."),
    ("b", "`NEWNICK nome_antigo nome_novo` — Usado para indicar a todos os utilizadores duma sala que o utilizador "
          "`nome_antigo`, que está nessa sala, mudou de nome para `nome_novo`."),
    ("b", "`JOINED nome` — Usado para indicar aos utilizadores numa sala que entrou um novo utilizador, com o nome `nome`, nessa sala."),
    ("b", "`LEFT nome` — Usado para indicar aos utilizadores numa sala que o utilizador com o nome `nome`, que também se "
          "encontrava nessa sala, saiu."),
    ("b", "`BYE` — Usado para confirmar a um utilizador que invocou o comando `/bye` a sua saída."),
    ("p", "O servidor mantém, associada a cada cliente, informação de estado, podendo cada cliente estar num dos seguintes estados:"),
    ("b", "`init` — Estado inicial de um utilizador que acabou de estabelecer a conexão ao servidor e, portanto, ainda não tem "
          "um nome associado."),
    ("b", "`outside` — O utilizador já tem um nome associado, mas não está em nenhuma sala de *chat*."),
    ("b", "`inside` — O utilizador está numa sala de *chat*, podendo enviar mensagens simples (para essa sala) e devendo receber "
          "todas as mensagens que os outros utilizadores nessa sala enviem."),
    ("p", "O seguinte quadro ilustra as transições de estado possíveis para um utilizador, identificando os eventos que as "
          "despoletam e as acções a elas associadas."),
    ("p", "**Quadro 1:** Estados e transições"),
    ("table", QUADRO, QW),
    ("p", "De seguida, ilustra-se um diálogo entre o cliente e o servidor, onde **C→S** indica uma mensagem enviada do cliente "
          "para o servidor, **S→C** indica uma mensagem enviada do servidor para o cliente e **S→O** indica uma mensagem "
          "enviada do servidor para os outros clientes que estão na mesma sala."),
    ("code", DIALOGO),
    ("p", "**IMPORTANTE:** Dado que serão feitos testes automáticos, é muito importante que o serviço implementado cumpra "
          "escrupulosamente a especificação. As mensagens deverão ter exactamente o formato indicado, e o servidor não deve "
          "enviar nada mais para além delas (nem sequer uma mensagem inicial de boas-vindas)."),
    ("h2", "Valorização"),
    ("b", "A implementação inteiramente correcta do servidor acima descrito será valorizada com 50% da cotação do trabalho."),
    ("b", "A implementação inteiramente correcta do cliente acima descrito será valorizada com 35% da cotação do trabalho."),
    ("b", "Se, adicionalmente, implementar no servidor o comando `/priv nome mensagem` (ver abaixo), obterá mais 10%."),
    ("b", "Se processar as mensagens recebidas pelo cliente de modo a que na área de *chat* não apareça directamente o que foi "
          "recebido do servidor, mas sim o seu conteúdo num formato mais amigável (ver exemplo abaixo), obterá mais 5%."),
    ("p", "O comando `/priv nome mensagem` serve para enviar ao utilizador `nome` (e apenas a ele) a `mensagem`. Se o utilizador "
          "`nome` não existir, o servidor deverá devolver `ERROR`, caso contrário deverá devolver `OK` e enviar ao utilizador "
          "`nome` a mensagem `PRIVATE emissor mensagem` (onde `emissor` é o nickname de quem enviou a mensagem). Note que "
          "podem estar em salas diferentes, ou mesmo em nenhuma."),
    ("p", "Por formato mais amigável entende-se, por exemplo, que quando é recebida do servidor a mensagem "
          "`MESSAGE nome mensagem` seja mostrado na área de chat `nome: mensagem`, que quando é recebida do servidor a "
          "mensagem `NEWNICK nome_antigo nome_novo` seja mostrado na área de chat `nome_antigo mudou de nome para nome_novo`, etc."),
    ("h2", "Notas"),
    ("n", "1.", "É particularmente importante o servidor lidar correctamente com a delineação das mensagens. Para testar este "
                "aspecto pode usar como cliente o `ncat` (ou `netcat`, ou `nc`)."),
    ("b", "Para testar o envio de uma única mensagem partida em vários pacotes faça `ncat localhost 8000` e escreva "
          "`/ni<CTRL-D>ck bom<CTRL-D>rapaz<ENTER>`. O servidor não deve interpretar o comando ao fazer `<CTRL-D>`, apenas "
          "*bufferizar* os pedaços da mensagem (“`/ni`”, “`ck bom`” e “`rapaz`”). O comando completo (“`/nick bomrapaz`”) só "
          "deve ser processado quando fizer `<ENTER>`."),
    ("b", "Para testar o envio de múltiplas mensagens num único pacote pode criar um ficheiro com as linhas abaixo e fazer "
          "`ncat localhost 8000 < ficheiro`. O servidor deve interpretar o que recebe como dois comandos e uma mensagem de texto."),
    ("code", "/nick bomrapaz\n/join sala\nBom dia!"),
    ("n", "2.", "Por exemplo, se o utilizador `joe` escrever `/notacommand`, que não é nenhum dos comandos do protocolo, o cliente "
                "deve enviar ao servidor a mensagem `//notacommand`. O servidor detecta o mecanismo de escape, remove a ‘/’ "
                "extra e envia aos clientes `MESSAGE joe /notacommand`. Se o utilizador escrever `//comment`, o cliente envia "
                "ao servidor `///comment` e o servidor envia aos clientes `MESSAGE joe //comment`."),
    ("h2", "Entrega"),
    ("p", "O trabalho será desenvolvido em grupos de dois elementos. Cada grupo deverá entregar um arquivo .zip contendo exactamente:"),
    ("b", "Um ficheiro `ChatServer.java` com o código-fonte do servidor."),
    ("b", "Um ficheiro `ChatClient.java` com o código-fonte do cliente."),
    ("b", "Um ficheiro `grupo.txt` com a identificação dos dois elementos do grupo no formato aqui exemplificado:"),
    ("code", "201012345 Ana Beatriz Carvalho Duarte\n201054321 Eduardo Fernando Gonçalves Henriques"),
    ("p", "Se o cliente e/ou o servidor estiverem organizados em diferentes classes, deverão incluir ficheiros .java com o "
          "respectivo código-fonte (contudo, as classes principais do servidor e do cliente deverão ser, respectivamente, "
          "`ChatServer` e `ChatClient`). A submissão deverá ser feita no Moodle por apenas um dos elementos do grupo. O "
          "incumprimento das regras de submissão será penalizado."),
    ("h2", "Código de honra"),
    ("p", "A submissão de um trabalho implica a garantia, sob compromisso de honra, de que o trabalho submetido resultou "
          "exclusivamente do esforço dos elementos do respectivo grupo, não tendo havido qualquer partilha de código com "
          "pessoas externas ao grupo. É expressamente proibido usar código de outros grupos, bem como fornecer código a outros grupos."),
    ("h2", "Realização do trabalho prático em Python"),
    ("p", "*(Página à parte no Moodle; última alteração: sexta-feira, 23 de outubro de 2026 às 16:49.)*"),
    ("p", "A linguagem de programação a utilizar na implementação do trabalho prático é o Java. Isto aplica-se a todos os "
          "estudantes da LCC e outros cursos do DCC. Contudo, aos alunos de licenciaturas que não sejam do DCC e que não tenham "
          "tido contacto prévio com o Java é dada a possibilidade de implementar o trabalho em Python."),
    ("p", "Os grupos que realizarem o trabalho em Python devem começar por ler com cuidado o "
          "[Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html), particularmente a parte respeitante a "
          "sockets não-bloqueantes. Quanto ao cliente, devem usar este esqueleto (`esqueletos/ChatClient.py`) para construir "
          "uma GUI simples e preencher com o código respeitante à comunicação e o respectivo protocolo."),
]

# ---------------------------------------------------------------- Guia passo a passo
G = [
    ("p", "Guia nosso (não é do professor) para fazer o trabalho do princípio ao fim. A especificação oficial é o "
          "`enunciado_trabalho_pratico.pdf`; em caso de dúvida, manda ele. Em Java (LCC/DCC). Prazo: **9 de dezembro, 23:59**; "
          "submissão a partir de 1 de novembro."),

    ("h2", "Passo 0 — Organizar"),
    ("a", "0.1", "Confirmar o grupo no Moodle («Grupos para o trabalho prático» — estás no Grupo 15) e escrever já o `grupo.txt`: "
                 "uma linha por elemento, `número nome completo`, exactamente como no exemplo do enunciado."),
    ("a", "0.2", "Criar uma pasta de trabalho com `ChatServer.java`, `ChatClient.java` (copiado de `esqueletos/`) e "
                 "`grupo.txt`. Dividir: um faz o servidor (vale 50% + 10% do `/priv`), o outro o cliente (35% + 5%). "
                 "O protocolo é o contrato entre os dois — ler juntos o Quadro 1 antes de começar."),
    ("a", "0.3", "Calendário sugerido: semana 1 — ficha 5 e esqueleto do servidor (passos 1–3); semana 2 — comandos e estados "
                 "(4–6); semana 3 — cliente (7–8); semana 4 — extras, testes e entrega (9–11), com folga antes de 9/12."),

    ("h2", "Passo 1 — Fazer primeiro a ficha 5"),
    ("p", "O servidor do trabalho é a ficha 5 levada até ao fim: `Server.java` (multiplex com `Selector`) → eco → difusão a "
          "todos → pseudónimo com `key.attach(...)`. Com a ficha 5 feita tens o esqueleto do `ChatServer`: um único "
          "thread, um `Selector`, `OP_ACCEPT` no `ServerSocketChannel` e `OP_READ` em cada `SocketChannel`. "
          "Renomeia a classe para `ChatServer` e mantém a porta em `args[0]`."),

    ("h2", "Passo 2 — Estado por cliente"),
    ("p", "Cria uma classe (p. ex. `Cliente`) e associa uma instância a cada `SelectionKey` no accept "
          "(`sc.register(selector, OP_READ, new Cliente())` ou `key.attach`). Campos:"),
    ("b", "`estado`: `INIT`, `OUTSIDE` ou `INSIDE` (um `enum`);"),
    ("b", "`nick` (null em `INIT`) e `sala` (null fora de sala);"),
    ("b", "um *buffer* de entrada só deste cliente (passo 3)."),
    ("p", "E duas estruturas globais: `Map<String, SelectionKey> nicks` (nome → cliente; serve para «disponível(nome)» e "
          "para o `/priv`) e `Map<String, Set<SelectionKey>> salas` (sala → membros; a sala cria-se no primeiro `/join`; "
          "podes apagá-la quando fica vazia)."),

    ("h2", "Passo 3 — Delineação das mensagens (o mais testado)"),
    ("p", "O TCP é um fluxo de bytes: um `read` pode trazer meia linha ou várias. Por isso:"),
    ("a", "3.1", "Em cada `read`, acrescenta os bytes lidos ao *buffer* do cliente (não ao `buffer` global partilhado)."),
    ("a", "3.2", "Enquanto o *buffer* tiver um `\\n`: tira a linha até ao `\\n`, remove um `\\r` final se existir (o telnet manda "
                 "`\\r\\n`, o ncat só `\\n`) e processa-a (passo 4). O que sobra fica à espera do próximo `read`."),
    ("a", "3.3", "Guarda bytes e só descodifica UTF-8 por linhas completas: um «ã» pode chegar partido entre dois `read`. "
                 "Partir no byte `\\n` é seguro em UTF-8."),
    ("a", "3.4", "`read` devolve `-1` → o cliente fechou: trata como «utilizador fechou a conexão» (passo 6)."),
    ("p", "Teste imediato: `ncat localhost 8000`, escrever `/ni`, CTRL-D, `ck bom`, CTRL-D, `rapaz`, ENTER → só aí "
          "deve aparecer `OK`. E `ncat localhost 8000 < ficheiro` com três linhas → três respostas."),

    ("h2", "Passo 4 — Interpretar cada linha"),
    ("b", "Começa por `//` → é mensagem simples com escape: tira **uma** `/` (`///x` → `//x`)."),
    ("b", "Começa por uma só `/` → é comando: separa por espaços. `/nick`, `/join` levam 1 argumento; `/leave`, `/bye` "
          "nenhum; `/priv` leva nome + resto da linha (`split(\" \", 3)`, a mensagem pode ter espaços). "
          "Comando desconhecido ou com argumentos a menos → `ERROR`."),
    ("b", "Caso contrário → mensagem simples."),

    ("h2", "Passo 5 — Implementar o Quadro 1, linha a linha"),
    ("p", "Um `switch` pelo comando e, dentro, pelo estado. Cada linha do Quadro 1 é um caso; quem recebe o quê:"),
    ("table", [
        ["Evento", "Ao próprio", "Aos outros da sala", "Efeito"],
        ["`/nick n` (n ocupado)", "`ERROR`", "—", "nada muda"],
        ["`/nick n` em init/outside", "`OK`", "—", "liberta o nome antigo, reserva `n`; init → outside"],
        ["`/nick n` em inside", "`OK`", "`NEWNICK antigo n`", "igual, fica inside"],
        ["`/join s` em outside", "`OK`", "`JOINED nome` (sala `s`)", "entra em `s`"],
        ["`/join s` em inside", "`OK`", "`LEFT nome` (antiga), `JOINED nome` (nova)", "muda de sala"],
        ["`/leave` em inside", "`OK`", "`LEFT nome`", "inside → outside"],
        ["mensagem em inside", "`MESSAGE nome msg`", "`MESSAGE nome msg`", "a própria pessoa também a recebe"],
        ["mensagem fora de sala", "`ERROR`", "—", ""],
        ["`/bye`", "`BYE`", "`LEFT nome` (se inside)", "fecha a conexão"],
        ["fecho da conexão", "—", "`LEFT nome` (se inside)", "fecha e limpa"],
        ["`/join`, `/leave` em init", "`ERROR`", "—", "comando não suportado nesse estado"],
        ["`/priv n m` (extra)", "`OK` / `ERROR` se `n` não existe", "só `n` recebe `PRIVATE emissor m`", "em init → `ERROR` (sem nome)"],
    ], [3.6, 3.4, 5.0, 5.0]),
    ("p", "Pormenores que os testes automáticos apanham:"),
    ("b", "a ordem do diálogo do enunciado: primeiro a resposta ao próprio (`OK`), depois as notificações aos outros;"),
    ("b", "`JOINED`, `LEFT` e `NEWNICK` vão só aos **outros**; `MESSAGE` vai a **todos** na sala, incluindo quem a enviou;"),
    ("b", "`/leave` em outside e `/join` em init dão `ERROR`; o enunciado não diz o que fazer em `/nick` para o próprio nome "
          "actual nem em `/join` para a sala onde já se está — escolham (o mais literal: o nome já está em uso → `ERROR`; "
          "`/join` segue o quadro) e sejam consistentes;"),
    ("b", "nada de mensagens de boas-vindas nem *prints* de *debug* para a *socket* (para o `stdout` do servidor não faz mal)."),

    ("h2", "Passo 6 — Enviar e fechar"),
    ("a", "6.1", "Função `enviar(key, texto)`: `ByteBuffer.wrap((texto + \"\\n\").getBytes(StandardCharsets.UTF_8))` e "
                 "`while (bb.hasRemaining()) sc.write(bb);` — em modo não-bloqueante o `write` pode escrever só parte."),
    ("a", "6.2", "Função `sair(key)` usada por `/bye` e pelo fecho da conexão: se inside, `LEFT nome` aos outros e tira-o da "
                 "sala; liberta o nick em `nicks`; `key.cancel()` e `sc.close()`. No `/bye` envia `BYE` antes de fechar."),
    ("a", "6.3", "Apanha `IOException` por cliente (um cliente que cai não pode deitar abaixo o servidor) e chama `sair`."),

    ("h2", "Passo 7 — Cliente: ligação e duas threads"),
    ("a", "7.1", "No construtor (na zona «adicionar código de inicialização»): `socket = new Socket(server, port)`, um "
                 "`BufferedReader` com `InputStreamReader(socket.getInputStream(), UTF_8)` e um `OutputStream` / `PrintWriter` "
                 "em UTF-8. Não mexer nas partes marcadas «NÃO MODIFICAR»."),
    ("a", "7.2", "`run()`: arranca uma thread que faz `while ((linha = in.readLine()) != null) printMessage(formatar(linha) + \"\\n\");`. "
                 "A thread principal do Swing fica livre para o utilizador escrever. Se `readLine` devolver `null` ou chegar "
                 "`BYE`, fecha a socket e termina (`frame.dispose()` / `System.exit(0)`)."),

    ("h2", "Passo 8 — Cliente: enviar com escape"),
    ("p", "Em `newMessage(message)`: se a mensagem começa por `/` e a primeira palavra **não** é um dos comandos "
          "(`/nick`, `/join`, `/leave`, `/bye`, `/priv`), acrescenta mais uma `/` à frente. Assim `/notacommand` → "
          "`//notacommand` e `//comment` → `///comment`, como na nota 2. Envia a linha com `\\n` no fim e faz *flush*."),

    ("h2", "Passo 9 — Extras (+15%)"),
    ("b", "**`/priv nome mensagem`** no servidor (+10%): procura `nome` em `nicks`; se não existe `ERROR`; senão `OK` ao emissor e "
          "`PRIVATE emissor mensagem` só ao destinatário, estejam em que sala estiverem (o emissor precisa de ter nome)."),
    ("b", "**Formato amigável** no cliente (+5%), em `formatar(linha)` (com `split(\" \", 3)`): `MESSAGE n m` → `n: m`; "
          "`NEWNICK a b` → `a mudou de nome para b`; `JOINED n` → `n entrou na sala`; `LEFT n` → `n saiu da sala`; "
          "`PRIVATE e m` → `(privado) e: m`; `OK`/`ERROR` → «Comando aceite» / «Erro»; `BYE` → «Saíste do chat»."),

    ("h2", "Passo 10 — Testar como o professor vai testar"),
    ("code", "javac ChatServer.java ChatClient.java\n"
             "java ChatServer 8000                    # terminal 1\n"
             "ncat localhost 8000                     # terminais 2, 3, 4 (ou nc)\n"
             "java ChatClient localhost 8000          # no fim, com a GUI"),
    ("b", "Reproduzir o diálogo do enunciado com três `ncat` (miquinhas, francisca, berto) e comparar carácter a carácter."),
    ("b", "Os dois testes da nota 1 (CTRL-D a meio da linha; ficheiro com várias linhas)."),
    ("b", "Cada linha do Quadro 1, incluindo os `ERROR` (mensagem em init, `/leave` em outside, nome repetido, comando inventado)."),
    ("b", "Fechar um `ncat` com CTRL-C dentro de uma sala → os outros recebem `LEFT`, e o nome volta a ficar livre."),
    ("b", "Acentos («Olá», «ação») partidos e inteiros; linhas compridas; dez clientes ao mesmo tempo."),

    ("h2", "Passo 11 — Entregar"),
    ("code", "zip grupoXX.zip ChatServer.java ChatClient.java grupo.txt   # + outros .java, se houver"),
    ("b", "Só esses ficheiros (sem `.class`, sem pastas, sem `package` no topo dos `.java`)."),
    ("b", "Classes principais exactamente `ChatServer` e `ChatClient`; compila com `javac *.java` numa pasta vazia."),
    ("b", "Submete só um dos dois, no Moodle («Enunciado do trabalho prático»), antes de 9/12 às 23:59."),
    ("b", "Código de honra: nada de código de outros grupos nem partilhado com eles."),
]

DOCS = [
    (R + "Praticas/Semana_5/ficha_5_servidor_chat.pdf", "Ficha de Exercícios nº 5 — Servidor de chat multiplex", ALT, F5),
    (R + "Praticas/Semana_6/ficha_6_camada_transporte.pdf", "Ficha de Exercícios nº 6 — Camada de transporte", ALT, F6),
    (R + "Trabalho/enunciado_trabalho_pratico.pdf", "Enunciado do trabalho prático — Servidor e cliente de chat",
     "Copiado do Moodle (Redes de Comunicação 2026/27) a 25 de outubro de 2026", TP),
    (R + "Trabalho/guia_passo_a_passo.pdf", "Trabalho prático — guia passo a passo",
     "Servidor e cliente de chat em Java · entrega até 9 de dezembro de 2026, 23:59", G),
]
