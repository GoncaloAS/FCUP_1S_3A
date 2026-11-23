#!/usr/bin/env python3
"""
Banco de perguntas de Redes, 2.º teste (redes2.html): Capítulo 3 (Transporte) e Capítulo 4 até à
fragmentação IP (inclusive). Gera assets/js/data/questions-redes2/*.js.

Mesmo formato do perguntas.py (1.º teste): Q(id, enunciado, certa, [3 erradas], porquê_certa,
[porquê de cada errada], secção, calc=[linhas], lembrar="frase"). A posição da certa é sorteada e
equilibrada; a certa não pode ser a opção mais comprida em mais de 30% das perguntas (verificado);
sem "todas/nenhuma das anteriores". As de desenvolvimento (resposta aberta) usam a resolução do
SOLUCOES_Redes.md, a mesma do site.

Corre sozinho no fim do perguntas.py (e por isso no fechar.sh). Uso: python3 tools/redes-guide/perguntas2.py
"""
import json, random, re, shutil, subprocess
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "assets" / "js" / "data" / "questions-redes2"
GUIA = "guia_redes_teste1.html"   # o guia tem a matéria toda (gerado do resumo cumulativo)
html = (ROOT / GUIA).read_text()
TITULO = {i: re.sub(r"<[^>]+>", "", t).strip() for i, t in re.findall(r'<h[1-3] id="([^"]+)"[^>]*>(.*?)</h[1-3]>', html, re.S)}

S = {
 "mux": "serviços-e-multiplexagem", "udp": "udp-e-o-checksum", "rdt": "princípios-da-transferência-fiável",
 "sw": "stop-and-wait-e-a-sua-utilização", "gbnsr": "pipelining-go-back-n-e-selective-repeat",
 "tcpseg": "tcp-segmento-números-de-sequência-e-timeout", "rtt": "estimar-o-rtt-e-escolher-o-timeout",
 "tcprel": "tcp-transferência-fiável-e-retransmissão-rápida", "fluxo": "tcp-controlo-de-fluxo-e-gestão-de-conexões",
 "cong": "princípios-do-controlo-de-congestionamento", "reno": "controlo-de-congestionamento-no-tcp",
 "rede": "reenvio-encaminhamento-e-modelos-de-serviço", "cv": "circuitos-virtuais-e-datagramas",
 "router": "por-dentro-de-um-router", "ip": "ip-formato-do-datagrama-e-fragmentação",
}
for k, v in S.items():
    assert v in TITULO, f"secção {k} ({v}) não existe no guia"

L = "ABCD"

def Q(qid, text, right, wrongs, why_right, why_wrongs, sec, calc=None, lembrar=None, original=None):
    assert len(wrongs) == 3 and len(why_wrongs) == 3, qid
    for o in [right] + wrongs:
        assert not re.search(r"(todas|nenhuma) das anteriores", o, re.I), qid
    return dict(id=qid, text=text, right=right, wrongs=wrongs, wr=why_right, ww=why_wrongs,
                sec=S[sec], calc=calc or [], lembrar=lembrar, original=original)

def montar(q, pos, topic):
    opts = q["wrongs"][:]; whys = q["ww"][:]
    opts.insert(pos, q["right"]); whys.insert(pos, q["wr"])
    calc = "".join(f"<div>{c}</div>" for c in q["calc"])
    ok = (f'<div class="sol-ok"><b>({L[pos]}) Certa.</b> {whys[pos]}'
          + (f'<div class="sol-calc">{calc}</div>' if calc else "")
          + (f'<div class="sol-orig">No enunciado original é a alínea ({q["original"]}).</div>' if q["original"] else "")
          + "</div>")
    no = "".join(f"<li><b>({L[i]}) Errada.</b> {whys[i]}</li>" for i in range(4) if i != pos)
    exp = f'<div class="sol-title">Correção</div>{ok}<ul class="sol-no">{no}</ul>'
    nota = (f"<b>Para lembrar:</b> {q['lembrar']}<br>" if q["lembrar"] else "") + (
        f'Se a correção não chegou, lê a teoria: <a class="teoria" href="{GUIA}#{q["sec"]}" target="_blank">'
        f'📖 {TITULO[q["sec"]]}</a>')
    return [topic, q["id"], q["text"], opts, pos, exp, nota]

TOPICOS = []
def topic(slug, var, name, qs): TOPICOS.append((slug, var, name, qs))
def chk(a, b): assert abs(a - b) <= 1e-6 * max(1, abs(b)), (a, b)

# ── contas verificadas ──
def cksum(words):
    t = 0
    for w in words:
        t += int(w, 2); t = (t & 0xFFFF) + (t >> 16)
    return format(t, "016b"), format(~t & 0xFFFF, "016b")
s_, c_ = cksum(["1110011001100110", "1101010101010101"]); assert (s_, c_) == ("1011101110111100", "0100010001000011")
s2, c2 = cksum(["1000000000000001", "1000000000000011"]); assert (s2, c2) == ("0000000000000101", "1111111111111010")
chk((8000 / 1e9) / (0.030 + 8000 / 1e9), 0.000266596)                       # slides
chk((12000 / 1e7) / (0.040 + 12000 / 1e7), 0.0291262)                       # F6.1
chk((0.06 + 1e-5) / 1e-5, 6001)                                             # T: 1 Gbps, 1250 B, RTT 60 ms
chk(0.75 * (8 / 3) ** 0.5, 1.224744871)

# ═════════════════════════ Transporte, multiplexagem e UDP ═════════════════════════
topic("transporte-udp", "Q_R2_UDP", "Transporte e UDP", [
 Q("TU1", "Que entidades da rede correm o protocolo de transporte (TCP ou UDP)?",
   "só os terminais (os routers ficam pela camada de rede)",
   ["os terminais e todos os routers do caminho, salto a salto", "só os routers de fronteira entre ISPs", "só o terminal emissor; o receptor usa apenas o IP"],
   "O transporte é comunicação lógica entre <b>processos</b>, por isso só existe nas pontas. Os routers vão até à camada de rede: leem o cabeçalho IP para reenviar e nunca olham para portas nem números de sequência.",
   ["Salto a salto, nos routers, corre a camada de <b>rede</b> (IP). O transporte é extremo a extremo.",
    "Os routers de fronteira também são routers: não abrem o segmento de transporte.",
    "O receptor precisa do transporte para desmultiplexar para a socket certa (e, no TCP, para confirmar e reordenar)."],
   "mux", lembrar="transporte = processo a processo, só nos terminais."),
 Q("TU2", "Um servidor UDP com <code>new DatagramSocket(6428)</code> recebe datagramas de <code>A:9157</code> e de <code>B:5775</code>, ambos para a porta 6428. Quantas sockets os recebem?",
   "uma só: a do par (servidor, 6428)",
   ["duas, uma por cliente, porque as portas de origem diferem", "duas, porque os IPs de origem são diferentes", "nenhuma: o UDP exige uma socket por cliente criada antes"],
   "No UDP a socket é identificada pelo par <b>(IP destino, porta destino)</b>. Os dois datagramas vão para <code>servidor:6428</code>, logo para a mesma socket; o servidor distingue-os pelo endereço de origem que o <code>receive</code> devolve (é o \"endereço para a resposta\").",
   ["É o comportamento do TCP (tuplo de 4). No UDP a porta de origem não escolhe a socket.",
    "O IP de origem também não conta no UDP; só conta no TCP.",
    "O UDP não tem conexões: uma única socket recebe de qualquer cliente."],
   "mux", lembrar="UDP: (IP dest., porta dest.). TCP: os 4."),
 Q("TU3", "Num servidor web, chegam segmentos TCP de <code>A:9157→C:80</code>, <code>B:9157→C:80</code> e <code>B:5775→C:80</code>, todos de conexões abertas. Quantas sockets de conexão os recebem?",
   "três, porque cada tuplo de 4 é diferente",
   ["uma, porque a porta de destino é sempre a 80", "duas, porque só há dois IPs de origem", "duas, porque só há duas portas de origem"],
   "No TCP cada conexão tem a sua socket, identificada por <b>(IP orig., porta orig., IP dest., porta dest.)</b>. (A,9157), (B,9157) e (B,5775) são três pontas diferentes, logo três sockets, todas na porta 80 do servidor.",
   ["A porta 80 é comum a todas; é precisamente por isso que o TCP precisa dos outros três valores.",
    "B tem duas conexões (portas 9157 e 5775): o IP sozinho não chega.",
    "A e B usam ambos a 9157, mas têm IPs diferentes: são conexões diferentes."],
   "mux", lembrar="basta um dos quatro valores diferente para ser outra socket."),
 Q("TU4", "Porque é que o DNS e as aplicações multimédia usam UDP em vez de TCP?",
   "sem handshake nem estado, cabeçalho pequeno, ritmo livre",
   ["o UDP garante entrega por ordem, mais rápida do que a do TCP", "o UDP tem controlo de congestionamento mais justo do que o TCP", "o UDP reserva largura de banda na rede para cada fluxo"],
   "As vantagens do UDP nos slides: <b>sem conexão</b> (não perde um RTT a abrir), <b>sem estado</b>, <b>cabeçalho de 8 bytes</b>, e <b>sem controlo de congestionamento</b> (a multimédia mantém o débito, tolerando perdas).",
   ["O UDP não garante nada sobre a ordem: os segmentos podem chegar desordenados.",
    "O UDP não tem controlo de congestionamento nenhum (e por isso nem é justo).",
    "Nenhum protocolo de transporte da Internet reserva recursos: o IP é melhor esforço."],
   "udp", lembrar="UDP = mux + checksum, e mais nada."),
 Q("TU5", "O campo <b>comprimento</b> do cabeçalho UDP indica…",
   "segmento inteiro (cabeçalho + dados), em bytes",
   ["o tamanho só dos dados da aplicação, em bytes", "o número de segmentos em que a mensagem foi dividida", "o tamanho do datagrama IP que transporta o segmento"],
   "O cabeçalho UDP tem 4 campos de 16 bits: portas de origem e destino, <b>comprimento</b> e checksum. O comprimento conta o <b>segmento inteiro</b> em bytes, incluindo os 8 do cabeçalho (na F6.5 vale 16: 8 + 8 de dados).",
   ["Inclui também o cabeçalho de 8 bytes.",
    "O UDP não divide mensagens: cada mensagem vai num datagrama.",
    "O comprimento do datagrama IP está no cabeçalho IP (comprimento total), não no UDP."],
   "udp", lembrar="comprimento UDP = 8 + dados."),
 Q("TU6", "Soma (Internet checksum) de <code>1110011001100110</code> e <code>1101010101010101</code>. Qual é o checksum?",
   "<code>0100010001000011</code>", ["<code>1011101110111100</code>", "<code>0100010001000100</code>", "<code>1011101110111011</code>"],
   "Soma: dá 17 bits, <code>1 1011101110111011</code>. O 1 da esquerda volta a somar-se à direita (<i>wraparound</i>): <code>1011101110111100</code>. O checksum é o <b>complemento para 1</b>: troca cada bit, <code>0100010001000011</code>.",
   ["Esta é a <b>soma</b> (já com o wraparound), não o checksum: falta o complemento.",
    "É o complemento da soma sem o wraparound, mais 1: mistura dois erros (o transporte tem de voltar a entrar antes de complementar).",
    "É a soma sem o wraparound (deitou-se fora o bit 17)."],
   "udp", calc=["1110011001100110 + 1101010101010101 = 1 1011101110111011",
                "wraparound: 1011101110111011 + 1 = 1011101110111100",
                "checksum = NOT soma = 0100010001000011"], lembrar="soma, wraparound, depois inverte."),
 Q("TU7", "O receptor soma todas as palavras de 16 bits do segmento UDP, incluindo o checksum, e obtém <code>1111111111111110</code>. O que conclui?",
   "detetou um erro, porque a soma devia dar tudo uns",
   ["não há erros, porque só um bit difere de 1", "não há erros: a soma esperada é tudo zeros", "houve um erro e o próprio checksum diz qual foi o bit trocado"],
   "Se nada mudou, soma + checksum = soma + NOT(soma) = <code>1111111111111111</code>. Qualquer 0 indica que algo mudou: <b>erro detetado</b> e o segmento é descartado (o UDP não corrige).",
   ["Um só bit diferente já é um erro detetado.",
    "Com o checksum incluído, a soma correta é tudo <b>uns</b> (tudo zeros é o \"sem checksum\" do UDP).",
    "O Internet checksum só deteta; não diz que bit mudou nem corrige."],
   "udp", lembrar="receptor: tudo uns = ok; algum 0 = erro."),
 Q("TU8", "Que alteração a um segmento o Internet checksum <b>não</b> deteta?",
   "um 0→1 e um 1→0 na mesma coluna de duas palavras",
   ["um único bit trocado em qualquer posição do segmento", "um bit trocado no próprio campo do checksum", "três bits trocados de 0 para 1 em palavras diferentes"],
   "Uma palavra ganha 2<sup>k</sup> e a outra perde 2<sup>k</sup>: a soma fica igual e o receptor obtém tudo uns. É a resposta da F6.5d. Trocar duas palavras de ordem também passa (a soma é comutativa).",
   ["Um só bit trocado muda sempre a soma: é sempre detetado.",
    "O checksum também entra na soma do receptor: trocar um bit dele muda o resultado.",
    "Três subidas não se anulam: a soma aumenta e há um 0 no resultado."],
   "udp", lembrar="erros que se anulam na soma passam."),
 Q("TU9", "No UDP, o checksum é calculado sobre…",
   "segmento UDP inteiro + pseudo-cabeçalho (IPs, protocolo, comprimento)",
   ["só o cabeçalho UDP de 8 bytes, sem os dados", "só os dados da aplicação, para não repetir o cabeçalho IP", "o datagrama IP inteiro, recalculado em cada router porque o TTL muda a cada salto"],
   "Nota dos slides: cobre o segmento completo (cabeçalho + dados) e ainda um <b>pseudo-cabeçalho</b> com os IPs de origem e destino, o campo protocolo do IP e o comprimento UDP. Assim deteta também um segmento entregue à máquina errada.",
   ["Os dados também entram: o objetivo é detetar erros no segmento todo.",
    "O cabeçalho UDP também entra (e uma parte do IP, via pseudo-cabeçalho).",
    "Quem é recalculado em cada router é o checksum do <b>cabeçalho IP</b> (o TTL muda). O UDP só se verifica no destino."],
   "udp", lembrar="checksum UDP = segmento + pseudo-cabeçalho."),
])

# ═════════════════════════ Transferência fiável (rdt) e stop-and-wait ═════════════════════════
topic("rdt", "Q_R2_RDT", "Transferência fiável (rdt)", [
 Q("RD1", "Que problema do canal leva o rdt2.1 a acrescentar <b>números de sequência</b> ao rdt2.0?",
   "ACK/NAK corrompido: a retransmissão pode criar um duplicado",
   ["a perda de pacotes de dados, que exige um temporizador no emissor", "a troca de bits nos dados, que exige um checksum no receptor", "a chegada de pacotes fora de ordem num canal com vários caminhos"],
   "No rdt2.0, se o ACK/NAK vier estragado, o emissor não sabe o que aconteceu. Retransmite por segurança, mas isso pode criar um <b>duplicado</b>. O número de sequência (0/1) permite ao receptor descartá-lo.",
   ["As perdas são o problema do rdt3.0, que junta o temporizador.",
    "Os bits trocados nos dados já eram tratados no rdt2.0 (checksum + ACK/NAK).",
    "O canal do rdt nunca reordena: os números servem para duplicados, não para reordenar."],
   "rdt", lembrar="2.0 checksum+ACK/NAK; 2.1 nº seq.; 2.2 sem NAK; 3.0 timer."),
 Q("RD2", "No rdt2.2 deixa de haver NAK. Como é que o receptor avisa que um pacote chegou corrompido?",
   "repete o ACK do último pacote bom (ACK duplicado = NAK)",
   ["não avisa: o emissor espera um timeout e retransmite", "envia um ACK com o checksum do pacote corrompido", "envia o pacote corrompido de volta para o emissor comparar"],
   "Em vez de NAK, o receptor envia ACK com o número do <b>último pacote bom</b>. Para o emissor, um ACK duplicado (do pacote anterior) significa \"o atual não chegou bem\": retransmite. Mesma informação, menos tipos de mensagem.",
   ["Isso é o rdt3.0, que só retransmite por timeout. O rdt2.2 ainda não tem temporizador.",
    "O ACK leva o <b>número de sequência</b> do pacote confirmado, não um checksum do pacote estragado.",
    "Não há eco de pacotes: só ACKs com número."],
   "rdt", lembrar="ACK duplicado = NAK."),
 Q("RD3", "No rdt3.0 há um <b>timeout prematuro</b> (o ACK só se atrasou). O que garante que nada corre mal?",
   "os números de sequência (duplicados reconhecidos)",
   ["o checksum, que deteta o pacote retransmitido como corrompido", "o receptor, que deteta o atraso e pede ao emissor para esperar", "o emissor, que só retransmite se receber um NAK"],
   "A retransmissão é um <b>duplicado</b>: o receptor reconhece-o pelo número, descarta-o e volta a enviar o ACK. Quando o 2.º ACK repetido chega, o emissor já espera o número seguinte e ignora-o. Sem números nos ACKs, esse ACK atrasado confirmaria o pacote errado (F6.1a).",
   ["O pacote retransmitido não vem corrompido: é igual ao original, o checksum dá certo.",
    "O receptor não sabe nada sobre os temporizadores do emissor: não pode \"pedir para esperar\".",
    "O rdt3.0 não usa NAK e retransmite por timeout, não por NAK."],
   "rdt", lembrar="timeout prematuro → duplicados, resolvidos pelos números."),
 Q("RD4", "No rdt3.0, o que faz o emissor quando recebe um ACK <b>corrompido</b>?",
   "ignora-o e espera pelo timeout para retransmitir",
   ["retransmite logo o pacote, como se fosse um NAK", "pára o temporizador e avança para o pacote seguinte", "envia um pedido ao receptor para repetir o ACK"],
   "Nota dos slides: no rdt3.0 o emissor <b>só retransmite em caso de timeout</b>. Um ACK corrompido ou com o número errado é ignorado; os erros são tratados como perdas.",
   ["Retransmitir logo era o comportamento do rdt2.x; no 3.0 a única causa de retransmissão é o timeout.",
    "Avançar com um ACK que não se consegue ler podia perder o pacote atual.",
    "Não existe mensagem de \"repete o ACK\" no protocolo."],
   "rdt", lembrar="rdt3.0: só o timeout faz retransmitir."),
 Q("RD5", "Ligação de 1 Gbps, propagação de 15 ms (só ida), pacotes de 8000 bits, stop-and-wait. Qual é a utilização do emissor?",
   "≈ 0,00027 (0,027%)", ["≈ 0,00053 (0,053%)", "≈ 0,027 (2,7%)", "≈ 0,5 (50%)"],
   "U = (L/R)/(RTT + L/R). L/R = 8000/10<sup>9</sup> = 8 µs; RTT = 2 × 15 = 30 ms. U = 0,008/30,008 ≈ 0,00027. A ligação de 1 Gbps só dá ~267 kbit/s.",
   ["Usou só a propagação de ida (15 ms) em vez do RTT: o ACK também tem de voltar.",
    "Erro de 100× nas unidades (ms vs. µs).",
    "50% seria se o RTT fosse igual a L/R; aqui o RTT é ~3750 vezes maior."],
   "sw", calc=["L/R = 8000 / 10⁹ = 8×10⁻⁶ s = 0,008 ms", "RTT = 2 × 15 = 30 ms", "U = 0,008 / 30,008 ≈ 0,00027"],
   lembrar="U = (L/R) / (RTT + L/R)."),
 Q("RD6", "Rede de 10 Mbps, propagação de 20 ms, pacotes de 1500 bytes. Quantos pacotes têm de estar em trânsito para a transmissão ser contínua?",
   "35", ["34", "17", "3"],
   "Contínuo quando N·L/R ≥ RTT + L/R. L/R = 12 000/10<sup>7</sup> = 1,2 ms; RTT = 40 ms. N ≥ 41,2/1,2 = 34,3, e como N é inteiro, <b>35</b>.",
   ["34 × 1,2 = 40,8 ms &lt; 41,2 ms: ainda há um intervalo parado. Arredonda-se para cima.",
    "Usou só a propagação de ida (20 ms): 21,2/1,2 ≈ 17,7.",
    "3 é o exemplo dos slides (\"a utilização triplicou\"), não o resultado desta conta."],
   "sw", calc=["L/R = 1500×8 / 10⁷ = 1,2 ms; RTT = 40 ms", "N ≥ (40 + 1,2) / 1,2 = 34,3 → 35"],
   lembrar="N ≥ (RTT + L/R)/(L/R), arredondado para cima."),
 Q("RD7", "Com pipelining de N pacotes por RTT (sem perdas e N·L/R &lt; RTT + L/R), a utilização é…",
   "N vezes a do stop-and-wait: N·(L/R)/(RTT + L/R)",
   ["igual à do stop-and-wait, porque o RTT não muda", "N² vezes a do stop-and-wait, pela janela dos dois lados", "sempre 1, com qualquer N maior que 1"],
   "Em cada ciclo de RTT + L/R transmitem-se N pacotes em vez de 1: o tempo ocupado multiplica por N (\"a utilização triplicou\" com 3). O limite é U = 1.",
   ["O RTT não muda, mas passa a ser aproveitado com mais pacotes.",
    "Não há fator ao quadrado: são N pacotes por ciclo.",
    "Só chega a 1 se N·L/R ≥ RTT + L/R."],
   "sw", lembrar="U × N, até 1."),
 Q("RD8", "A principal limitação do stop-and-wait é…",
   "poder limitar severamente a taxa de transmissão",
   ["não detetar a perda das confirmações enviadas pelo receptor", "retransmitir todos os pacotes da janela num timeout", "não garantir que os pacotes são entregues por ordem"],
   "Pergunta de exame antigo. Com um pacote por RTT, num caminho longo e rápido a ligação fica quase sempre parada (U ≈ 0,00027 no exemplo dos slides).",
   ["Deteta-as: sem ACK, o temporizador expira e retransmite.",
    "Isso é o Go-Back-N; o stop-and-wait só tem um pacote em trânsito.",
    "Com um pacote de cada vez, a ordem é sempre garantida."],
   "sw", lembrar="stop-and-wait: correto, mas lento."),
])

# ═════════════════════════ Go-Back-N e Selective Repeat ═════════════════════════
topic("gbn-sr", "Q_R2_GBNSR", "Go-Back-N e Selective Repeat", [
 Q("GS1", "Go-Back-N com janela 4: envia 0, 1, 2, 3 e perde-se o 2. O que faz o receptor quando recebe o 3?",
   "descarta-o e repete o ACK1",
   ["guarda-o em buffer e envia ACK3", "guarda-o em buffer e envia ACK1", "descarta-o e envia um NAK2 a pedir o pacote em falta"],
   "O receptor GBN não tem buffer: só guarda o <code>expectedseqnum</code>. Um pacote fora de ordem é <b>ignorado</b> e reenvia-se o ACK do maior número recebido em ordem (ACK1, duplicado).",
   ["Guardar e confirmar individualmente é o Selective Repeat.",
    "O GBN não guarda nada fora de ordem; o ACK1 está certo, mas o pacote é descartado.",
    "Não há NAKs no GBN: só ACKs cumulativos."],
   "gbnsr", lembrar="GBN: receptor sem buffer, ACK cumulativo."),
 Q("GS2", "No mesmo cenário (janela 4, perde-se o 2, e entretanto já foram enviados o 4 e o 5), o que é retransmitido no timeout do Go-Back-N?",
   "os pacotes 2, 3, 4 e 5", ["só o 2 (o que se perdeu)", "os pacotes 2 e 3", "os pacotes 0 a 5"],
   "O GBN tem um temporizador, do pacote mais antigo por confirmar (o 2). No timeout reenvia esse e <b>todos os enviados depois</b>: 2, 3, 4 e 5. É a demonstração dos slides; o 3, 4 e 5 chegaram bem mas tinham sido descartados.",
   ["Retransmitir só o perdido é o Selective Repeat.",
    "O 4 e o 5 também foram descartados pelo receptor (fora de ordem), por isso também têm de voltar.",
    "O 0 e o 1 já estão confirmados (ACK1)."],
   "gbnsr", lembrar="GBN: timeout → o que falhou e tudo o que veio depois."),
 Q("GS3", "Selective Repeat com janela 4: envia 0 a 3, perde-se o 2, e chegam ACK0, ACK1 e ACK3. Qual é a base da janela do emissor?",
   "2 (o 3 fica marcado, mas a base não passa o 2)",
   ["4, porque o ACK3 confirma cumulativamente tudo até ao 3", "3, porque foi o último confirmado", "0, porque o SR só avança quando chegam todos"],
   "No SR os ACKs são <b>individuais</b>. ACK0 e ACK1 avançam a base para 2; o ACK3 marca o 3 como confirmado, mas a base fica no 2 (o mais antigo por confirmar).",
   ["ACK cumulativo (\"tudo até 3\") é GBN/TCP, não SR.",
    "A base é o primeiro <b>não</b> confirmado, não o último confirmado.",
    "A janela avança a cada ACK que confirme a base (aqui, com ACK0 e ACK1)."],
   "gbnsr", lembrar="SR: base = mais antigo por confirmar."),
 Q("GS4", "No Selective Repeat, o receptor recebe um pacote com número <b>já entregue</b> (dentro de [rcvbase−N, rcvbase−1]). O que faz?",
   "reenvia o ACK desse pacote, sem o entregar",
   ["ignora-o, porque já foi entregue à aplicação", "entrega-o outra vez à aplicação e envia o ACK", "guarda-o em buffer à espera da janela seguinte"],
   "Se o ACK se perdeu, o emissor continua a retransmitir esse pacote; sem novo ACK, a janela do emissor nunca avança. Por isso o receptor <b>re-confirma</b> sem entregar (é o instante 7 da F6.2b).",
   ["Ignorar sem ACK pode bloquear o emissor para sempre.",
    "Entregar outra vez seria um duplicado na aplicação.",
    "É um pacote antigo, não da janela seguinte."],
   "gbnsr", lembrar="SR: pacote antigo → só re-ACK."),
 Q("GS5", "Com números de sequência de <b>3 bits</b>, qual é a janela máxima no Selective Repeat?",
   "4", ["7", "8", "3"],
   "No SR a gama tem de ter pelo menos o dobro da janela: 2N ≤ 2<sup>k</sup>, ou seja, N ≤ 2<sup>k−1</sup> = 2<sup>2</sup> = <b>4</b>.",
   ["7 = 2<sup>3</sup> − 1 é o limite do <b>Go-Back-N</b>.",
    "8 é a gama inteira: com janela 8, um pacote retransmitido confundia-se com um novo.",
    "3 funciona, mas não é o máximo."],
   "gbnsr", calc=["k = 3 → 2³ = 8 números", "SR: 2N ≤ 8 → N ≤ 4"], lembrar="SR N ≤ 2^(k−1); GBN N ≤ 2^k − 1."),
 Q("GS6", "Porque é que o Selective Repeat precisa de uma gama de números de pelo menos o dobro da janela?",
   "as janelas do emissor e do receptor podem estar desfasadas mas contíguas",
   ["porque cada pacote usa dois números, um para os dados e outro para o ACK", "porque o receptor precisa de guardar duas cópias de cada pacote", "porque os ACKs se perdem em média metade das vezes"],
   "Se o receptor já avançou (confirmou uma janela inteira) e os ACKs se perderam, o emissor ainda retransmite a janela antiga. As duas janelas ocupam 2N números seguidos; se a gama for menor, um pacote velho é aceite como novo (o dilema 0123 com janela 3).",
   ["Os ACKs usam o mesmo número que o pacote que confirmam.",
    "O receptor guarda uma cópia de cada pacote fora de ordem, não duas.",
    "A regra não tem nada de probabilístico: tem de funcionar no pior caso."],
   "gbnsr", lembrar="pior caso: duas janelas contíguas = 2N números."),
 Q("GS7", "Fibra de 5000 km a 2 Gbps (v = 2×10<sup>8</sup> m/s), blocos de 1000 B, SR. Quantos blocos tem de ter a janela para fluxo contínuo?",
   "12 501", ["6251", "12 500", "25 002"],
   "d<sub>prop</sub> = 5×10<sup>6</sup>/2×10<sup>8</sup> = 25 ms, RTT = 50 ms; L/R = 8000/2×10<sup>9</sup> = 4 µs. N ≥ (RTT + L/R)/(L/R) = 50,004/0,004 = <b>12 501</b> (F6.4a).",
   ["Usou só a propagação de ida (25 ms).",
    "Esqueceu o L/R do próprio pacote no numerador (o ACK só sai depois do último bit chegar).",
    "25 002 é a gama de números de sequência que o SR precisa (2N), não a janela."],
   "gbnsr", calc=["RTT = 2 × 25 ms = 50 ms; L/R = 4 µs", "N = (50 + 0,004) / 0,004 = 12 501"], lembrar="janela = (RTT + L/R)/(L/R)."),
 Q("GS8", "Quantos temporizadores usa o emissor Go-Back-N?",
   "um, o do pacote mais antigo por confirmar", ["um por cada pacote enviado e não confirmado", "nenhum, porque usa ACKs duplicados para detetar perdas", "dois, um para os dados e outro para os ACKs"],
   "O GBN tem um só temporizador, que se reinicia a cada ACK que faz avançar a janela e se pára quando não há nada pendente (<code>base == nextseqnum</code>).",
   ["Um temporizador por pacote é o Selective Repeat.",
    "O GBN dos slides deteta perdas por timeout; os ACKs duplicados só entram com a retransmissão rápida do TCP.",
    "Os ACKs não têm temporizador próprio."],
   "gbnsr", lembrar="GBN: 1 timer. SR: 1 por pacote."),
 Q("GS9", "Qual é a vantagem do Go-Back-N face ao Selective Repeat?",
   "o receptor não precisa de buffer, só do número esperado",
   ["retransmite menos pacotes quando há perdas, porque só repete os que faltam", "precisa de uma gama de números de sequência maior", "confirma cada pacote individualmente"],
   "Os slides: o SR consome mais recursos no receptor (buffer) e tem um emissor mais complexo (um temporizador por pacote). O GBN troca isso por mais retransmissões.",
   ["É o contrário: o GBN retransmite a janela toda.",
    "O GBN aceita <b>mais</b> pacotes com os mesmos bits (2<sup>k</sup>−1 contra 2<sup>k−1</sup>); e isso não seria uma vantagem.",
    "Confirmação individual é do SR; o GBN usa ACKs cumulativos."],
   "gbnsr", lembrar="GBN: simples mas desperdiça; SR: eficiente mas complexo."),
])

# ═════════════════════════ TCP: sequência, ACKs, RTT, retransmissão ═════════════════════════
topic("tcp-seq-rtt", "Q_R2_TCPSEQ", "TCP: sequência, ACK e timeout", [
 Q("TS1", "A envia três segmentos de 500, 300 e 200 bytes, o primeiro com sequência 1000. Que números de sequência têm?",
   "1000, 1500 e 1800", ["1000, 1001 e 1002", "1000, 1500 e 2000", "1500, 1800 e 2000"],
   "O número de sequência é o do <b>primeiro byte</b> do segmento: 1000; 1000 + 500 = 1500; 1500 + 300 = 1800.",
   ["O TCP conta bytes, não segmentos.",
    "2000 é onde começaria um 4.º segmento (1800 + 200).",
    "Esses são os ACKs que o receptor envia (próximo byte esperado)."],
   "tcpseg", lembrar="seq = 1.º byte; soma-se o tamanho dos dados."),
 Q("TS2", "No mesmo cenário (1000/500 B, 1500/300 B, 1800/200 B), perde-se o segmento 1500 e os outros chegam. Que ACKs envia o receptor?",
   "1500 e 1500 (duplicado)", ["1500 e depois 2000 (cumulativo)", "1500 e depois 1800 (o seguinte)", "1000 e depois 1800 (os recebidos)"],
   "O 1000 chega: ACK 1500 (próximo byte esperado). O 1800 chega <b>fora de ordem</b>: o receptor continua a esperar o 1500 e envia já um ACK <b>duplicado</b> de 1500 (slide da geração de ACKs).",
   ["O ACK 2000 só sai quando o buraco 1500–1799 for tapado.",
    "O ACK é cumulativo: não pode confirmar 1800 sem ter os bytes 1500–1799.",
    "O ACK diz o próximo byte esperado, não o número do segmento recebido."],
   "tcprel", lembrar="buraco → ACK duplicado do início do buraco."),
 Q("TS3", "Um receptor TCP recebe um segmento em ordem, e todos os anteriores já estão confirmados. O que faz (RFC 1122/2581)?",
   "adia o ACK até 500 ms à espera do próximo (delayed ACK)",
   ["envia logo um ACK cumulativo desse segmento", "envia logo um ACK duplicado do segmento anterior", "não envia ACK enquanto a janela do receptor não ficar cheia"],
   "<b>Delayed ACK</b>: se chegar outro segmento em ordem, um só ACK cumulativo confirma os dois; se não chegar em 500 ms, confirma este.",
   ["O ACK imediato é para o caso em que já há um segmento anterior por confirmar.",
    "ACK duplicado é para segmentos fora de ordem.",
    "O receptor nunca adia o ACK até a janela encher: isso bloqueava o emissor."],
   "tcprel", lembrar="em ordem e nada pendente → espera até 500 ms."),
 Q("TS4", "Quando é que um emissor TCP faz <b>retransmissão rápida</b>?",
   "ao receber 3 ACKs duplicados para o mesmo número",
   ["ao receber o primeiro ACK duplicado", "quando o temporizador chega a metade do valor do timeout", "quando a janela do receptor anunciada é zero"],
   "Três ACKs duplicados indicam que o segmento seguinte se perdeu mas os de trás chegaram. O emissor retransmite-o logo, sem esperar pelo timeout (que é longo).",
   ["Um só duplicado pode vir só de reordenação; o TCP espera por 3.",
    "Não há retransmissão a meio do timeout.",
    "A janela zero é controlo de fluxo: o emissor pára, não retransmite."],
   "tcprel", lembrar="3 ACKs dup. → reenvia sem esperar."),
 Q("TS5", "EstimatedRTT = 100 ms, DevRTT = 8 ms, chega SampleRTT = 140 ms (α = 1/8, β = 1/4; DevRTT com o EstimatedRTT antigo). Qual é o novo TimeoutInterval?",
   "169 ms", ["164 ms", "137 ms", "132 ms"],
   "DevRTT = ¾·8 + ¼·|140 − 100| = 6 + 10 = 16. EstimatedRTT = ⅞·100 + ⅛·140 = 105. Timeout = 105 + 4·16 = <b>169 ms</b>.",
   ["É o que dá calculando o DevRTT com o EstimatedRTT <b>novo</b> (|140 − 105| = 35 → DevRTT 14,75). O enunciado manda usar o antigo.",
    "Usou o DevRTT antigo (8) sem o atualizar: 105 + 32.",
    "Usou o EstimatedRTT novo e um DevRTT de 6,75 (esqueceu o fator ¼ na soma)."],
   "rtt", calc=["DevRTT = 0,75×8 + 0,25×40 = 16", "EstimatedRTT = 0,875×100 + 0,125×140 = 105", "Timeout = 105 + 4×16 = 169 ms"],
   lembrar="timeout = E + 4D; D com o E antigo."),
 Q("TS6", "Porque é que o TCP <b>não</b> usa como SampleRTT os ACKs de segmentos retransmitidos?",
   "não se sabe a que transmissão corresponde o ACK",
   ["porque esses ACKs chegam sempre corrompidos", "porque a retransmissão só acontece quando o RTT é zero", "porque o receptor não envia ACK de segmentos retransmitidos"],
   "Se medir desde a 1.ª transmissão e o ACK for da retransmissão, sobrestima; se medir desde a retransmissão e o ACK for da 1.ª, subestima. Por isso essas amostras são ignoradas (F7.3e).",
   ["Não há nenhuma razão para virem corrompidos.",
    "Não faz sentido: retransmite-se por timeout ou 3 ACKs dup., não por RTT zero.",
    "O receptor confirma normalmente; o problema está na interpretação no emissor."],
   "rtt", lembrar="ACK de retransmissão → amostra ignorada."),
 Q("TS7", "O RTT de uma conexão aumenta de repente e há timeouts sucessivos. O que faz o TCP ao temporizador?",
   "duplica o valor do temporizador em cada timeout",
   ["reduz o temporizador para metade, para reagir mais depressa", "mantém o valor da fórmula, porque a média se ajusta sozinha", "fecha a conexão ao fim de três timeouts seguidos"],
   "<b>Backoff exponencial</b>: em cada timeout, o temporizador duplica. Se usasse o valor antigo, todos os segmentos dariam timeout, seriam retransmitidos e, como as amostras de retransmitidos são ignoradas, a estimativa nunca mais se atualizava (F7.3f).",
   ["Reduzir faria ainda mais timeouts prematuros.",
    "A média não se ajusta: as amostras de segmentos retransmitidos são ignoradas.",
    "Os slides não falam de fechar a conexão; a reação é o backoff."],
   "rtt", lembrar="timeout → temporizador × 2."),
 Q("TS8", "No EWMA com α = 0,1, quanto pesa a amostra mais recente no novo EstimatedRTT?",
   "10%", ["90%", "1%", "50%"],
   "EstimatedRTT = (1 − α)·EstimatedRTT + α·SampleRTT: a amostra nova pesa α = 0,1. A anterior pesa 0,1 × 0,9 = 9%, a seguinte 8,1%, e assim por diante (decaimento exponencial).",
   ["90% é o peso de todo o histórico (1 − α).",
    "1% seria α²; não aparece na fórmula.",
    "50% seria α = 0,5."],
   "rtt", lembrar="peso da amostra i: α(1−α)^(i−1)."),
 Q("TS9", "O que indica o campo <b>janela do receptor</b> no cabeçalho TCP?",
   "quantos bytes o receptor ainda pode aceitar no seu buffer",
   ["quantos segmentos o emissor pode ter por confirmar na rede", "o número de sequência do próximo byte a enviar", "o número máximo de bytes de dados num segmento (MSS)"],
   "É o espaço livre no buffer de receção (RcvWindow), anunciado em cada segmento: é o controlo de fluxo.",
   ["O TCP conta bytes, não segmentos, e este campo vem do receptor.",
    "Isso é o campo número de sequência.",
    "O MSS negoceia-se nas opções, não neste campo."],
   "tcpseg", lembrar="campo janela = RcvWindow (bytes)."),
])

# ═════════════════════════ TCP: controlo de fluxo e conexões ═════════════════════════
topic("tcp-fluxo-conexoes", "Q_R2_FLUXO", "TCP: fluxo e conexões", [
 Q("FC1", "RcvBuffer = 4000 B; o receptor recebeu até ao byte 2999 e a aplicação leu até ao 999. Que RcvWindow anuncia?",
   "2000 bytes", ["1000 bytes", "3000 bytes", "4000 bytes"],
   "RcvWindow = RcvBuffer − (LastByteRcvd − LastByteRead) = 4000 − (2999 − 999) = 4000 − 2000 = <b>2000</b>.",
   ["Subtraiu os bytes recebidos (3000) sem descontar os já lidos.",
    "3000 são os bytes recebidos, não o espaço livre.",
    "Só seria 4000 se a aplicação tivesse lido tudo."],
   "fluxo", calc=["RcvWindow = 4000 − (2999 − 999) = 2000"], lembrar="espaço livre = buffer − (recebido − lido)."),
 Q("FC2", "O receptor anuncia RcvWindow = 0. O que faz o emissor TCP?",
   "pára, mas vai enviando segmentos de 1 byte",
   ["fecha a conexão com FIN", "retransmite o último segmento até a janela reabrir", "continua a enviar ao mesmo ritmo, porque o receptor descarta o excesso"],
   "Se parasse totalmente, nunca recebia um ACK com a janela atualizada. Os segmentos de 1 byte geram ACKs que trazem a RcvWindow nova.",
   ["A janela zero é temporária (a aplicação ainda vai ler); não é razão para fechar.",
    "Não há nada a retransmitir: o segmento chegou; o que falta é espaço no buffer.",
    "O controlo de fluxo existe precisamente para não extravasar o buffer."],
   "fluxo", lembrar="janela 0 → sondas de 1 byte."),
 Q("FC3", "Qual destas frases distingue bem o controlo de fluxo do controlo de congestionamento?",
   "fluxo: protege o receptor, comandado por ele; congestionamento: protege a rede, inferido pelo emissor",
   ["o de fluxo protege a rede e é o emissor que o comanda; o de congestionamento protege o receptor e é a rede que o comanda", "o de fluxo existe no UDP e no TCP; o de congestionamento só existe no TCP e é os routers que o comandam", "o de fluxo usa a janela de congestionamento; o de congestionamento usa a janela anunciada pelo receptor no cabeçalho"],
   "Fluxo: RcvWindow anunciada pelo <b>receptor</b>. Congestionamento: CongWin calculada pelo <b>emissor</b> a partir de perdas (3 ACKs dup. ou timeout). Ambas limitam a janela (F7.1).",
   ["Está trocado.",
    "O UDP não tem nenhum dos dois, e no TCP os routers não dão feedback.",
    "Está trocado: o fluxo usa a RcvWindow e o congestionamento a CongWin."],
   "fluxo", lembrar="fluxo = receptor; congestionamento = rede."),
 Q("FC4", "No three-way handshake, o cliente envia SYN com seq = x e o servidor responde SYN+ACK com seq = y. O que leva o 3.º segmento?",
   "ACK = y + 1, e já pode levar dados", ["ACK = x + 1, sem dados", "SYN com seq = x + 1", "ACK = y, e só depois o cliente envia os dados"],
   "O cliente confirma o número inicial do servidor: ACK = y + 1 (o SYN conta como um byte). Este segmento <b>já pode transportar dados</b> (slides).",
   ["x + 1 é o ACK que o servidor envia no 2.º segmento.",
    "O SYN só vai no 1.º e no 2.º segmento.",
    "O ACK é o próximo byte esperado (y + 1), e não é preciso esperar."],
   "fluxo", lembrar="SYN(x) → SYN+ACK(y, x+1) → ACK(y+1)."),
 Q("FC5", "Para que serve o three-way handshake?",
   "fixar os números de sequência iniciais e reservar buffers",
   ["medir o RTT inicial da conexão", "garantir um débito mínimo para toda a conexão", "escolher o caminho que os segmentos vão seguir"],
   "Abrir a conexão inicializa as variáveis do TCP: <b>números de sequência</b> (cada lado escolhe o seu e tem de saber que o outro o recebeu) e <b>buffers</b>/RcvWindow. Pergunta de exame antigo.",
   ["O RTT estima-se com amostras ao longo da conexão.",
    "O TCP não garante débito.",
    "O caminho é decidido pela camada de rede, salto a salto; o TCP não o escolhe."],
   "fluxo", lembrar="handshake = nºs de sequência iniciais + buffers."),
 Q("FC6", "No fecho de uma conexão TCP, quem fecha primeiro fica no estado <b>TIME_WAIT</b>. Porquê?",
   "para reenviar o último ACK se o FIN do outro lado se repetir",
   ["para esperar que o outro lado acabe de enviar os dados que faltam", "para dar tempo ao outro lado de abrir uma conexão nova", "para medir o RTT final e guardá-lo para a próxima conexão"],
   "Depois de responder ACK ao FIN do outro lado, espera 2 tempos de vida de um segmento. Se esse ACK se perder, o outro lado repete o FIN, e quem está em TIME_WAIT ainda responde (fiabilidade do FIN).",
   ["Esperar pelos dados do outro lado acontece em FIN_WAIT_2, antes do FIN dele.",
    "Não tem nada a ver com conexões novas.",
    "O TCP não guarda o RTT entre conexões."],
   "fluxo", lembrar="TIME_WAIT = garantir o último ACK."),
 Q("FC7", "Quantos segmentos se trocam, no caso normal, para fechar uma conexão TCP?",
   "quatro: FIN e ACK em cada sentido", ["três, como no handshake de abertura", "dois: FIN de um lado e ACK do outro", "um FIN de cada lado, sem ACKs"],
   "A conexão é full duplex: cada sentido fecha em separado. O cliente envia FIN, o servidor ACK; quando a aplicação do servidor fecha, FIN, e o cliente ACK (F7.2b).",
   ["Abrir são três; fechar normalmente são quatro (o ACK e o FIN do servidor podem ir juntos, mas não é o caso típico dos slides).",
    "Isso só fecha um sentido.",
    "O FIN tem de ser confirmado, senão não é fiável."],
   "fluxo", lembrar="fechar = FIN/ACK + FIN/ACK."),
])

# ═════════════════════════ Congestionamento e TCP Reno ═════════════════════════
topic("congestionamento", "Q_R2_CONG", "Congestionamento e TCP Reno", [
 Q("CG1", "TCP Reno com CongWin = 42 MSS em congestion avoidance deteta uma perda por <b>triplo ACK duplicado</b>. Quais ficam a ser o limiar e a janela?",
   "limiar 21 e janela 21", ["limiar 21 e janela 1", "limiar 42 e janela 21", "limiar 21 e janela 24"],
   "Triplo ACK dup. no Reno: limiar = CongWin/2 = 21 e <b>CongWin = limiar = 21</b>, continuando em congestion avoidance (recuperação rápida).",
   ["Janela a 1 é a reação a um <b>timeout</b>.",
    "O limiar passa a metade, não fica no valor antigo.",
    "24 é a janela 3 RTT depois (21, 22, 23, 24 contando a ronda da perda como 0), não logo a seguir."],
   "reno", lembrar="3 ACKs dup.: tudo a metade."),
 Q("CG2", "Mesmo cenário (42 MSS, triplo ACK duplicado, sem mais perdas). Como no exame antigo, 3 RTT depois…",
   "a janela é 23 MSS e o limiar 21 MSS", ["a janela e o limiar são ambos 23 MSS", "a janela é 4 MSS e o limiar 21 MSS", "a janela é 24 MSS e o limiar 24 MSS"],
   "Depois da perda: 21 (1.º RTT), 22, 23. Como na F7.4: perda no fim da ronda 16 com 42, ronda 17 = 21, 18 = 22, 19 = 23. O limiar só muda com outra perda: fica 21.",
   ["O limiar não acompanha a janela em CA.",
    "4 seria slow start depois de um timeout (1, 2, 4).",
    "O limiar não muda sem nova perda."],
   "reno", calc=["perda: limiar = 42/2 = 21, CongWin = 21", "+1 por RTT: 21 → 22 → 23"], lembrar="CA: +1 por RTT; limiar fixo até nova perda."),
 Q("CG3", "TCP Reno com CongWin = 26 MSS tem um <b>timeout</b>. O que acontece?",
   "limiar = 13 e CongWin = 1, em slow start", ["limiar = 13 e CongWin = 13, em congestion avoidance", "limiar = 26 e CongWin = 1, de volta ao slow start", "limiar = 1 e CongWin = 1, de volta ao slow start"],
   "Timeout = congestionamento severo (não chega nada): limiar = CongWin/2 = 13, CongWin = <b>1 MSS</b>, slow start. É a ronda 22 da F7.4.",
   ["Cortar só a metade é o triplo ACK duplicado.",
    "O limiar passa sempre a metade da janela antes da perda.",
    "O limiar não vai a 1; isso só acontece à janela."],
   "reno", lembrar="timeout: limiar = W/2, janela = 1."),
 Q("CG4", "Limiar inicial de 32 MSS, sem perdas, a começar em 1 MSS. Em que ronda é transmitido o <b>70.º</b> segmento?",
   "7.ª", ["6.ª", "8.ª", "70.ª"],
   "Janelas: 1, 2, 4, 8, 16, 32 (slow start até ao limiar), 33, … Acumulado: 1, 3, 7, 15, 31, <b>63</b> (ronda 6), 96 (ronda 7). Os segmentos 64 a 96 vão na 7.ª ronda (F7.4h).",
   ["Até à ronda 6 só se enviaram 63.",
    "Na ronda 7 o acumulado já chega a 96 ≥ 70.",
    "Confundiu segmento com ronda: em cada ronda vai uma janela inteira."],
   "reno", calc=["acumulado: 1, 3, 7, 15, 31, 63, 96", "63 &lt; 70 ≤ 96 → ronda 7"], lembrar="soma as janelas até chegar ao segmento."),
 Q("CG5", "No gráfico da janela de um TCP Reno, a janela cai de 42 para 21. Isso indica…",
   "uma perda detetada por triplo ACK duplicado", ["uma perda detetada por timeout", "que o receptor anunciou metade do espaço livre", "a passagem normal de slow start para congestion avoidance"],
   "Cair para <b>metade</b> é a recuperação rápida do Reno (3 ACKs dup.). Cair para 1 seria timeout (F7.4c/d).",
   ["O timeout leva a janela a 1 MSS.",
    "O gráfico é a CongWin, que não depende da RcvWindow.",
    "Essa passagem muda o ritmo de crescimento (exponencial → linear), não faz a janela cair."],
   "reno", lembrar="metade = 3 ACKs dup.; 1 = timeout."),
 Q("CG6", "Em slow start, quanto aumenta CongWin por cada ACK de dados novos?",
   "1 MSS, o que duplica a janela a cada RTT", ["MSS·MSS/CongWin, o que dá +1 MSS por RTT", "1 byte, o que dá crescimento lento", "o dobro da janela atual"],
   "Com n segmentos na janela chegam n ACKs; cada um soma 1 MSS: +n MSS por RTT, ou seja, a janela <b>duplica</b> (F7.5a). Exponencial, apesar do nome.",
   ["Esse é o incremento do congestion avoidance (F7.5b).",
    "O \"slow\" é por começar em 1 MSS; o crescimento é exponencial.",
    "Duplicar por ACK seria muito mais do que exponencial por RTT."],
   "reno", lembrar="SS: +MSS por ACK; CA: +MSS²/CongWin por ACK."),
 Q("CG7", "Segundo a análise dos slides, qual é o débito médio de uma conexão TCP com janela de pico W (ignorando o slow start)?",
   "0,75·W/RTT", ["W/RTT", "0,5·W/RTT", "W/(2·RTT) + MSS"],
   "A janela sobe linearmente de W/2 a W e volta a cair: a média de uma reta entre 0,5W e W é <b>0,75W</b>, por RTT.",
   ["W/RTT é o débito no pico, só no instante antes da perda.",
    "0,5W/RTT é o débito logo a seguir à perda.",
    "Não há termo MSS na média."],
   "reno", lembrar="média entre W/2 e W = 3W/4."),
 Q("CG8", "Com a fórmula débito ≈ 1,22·MSS/(RTT·√L), o que acontece ao débito se a taxa de perdas L for 4 vezes maior?",
   "cai para metade", ["cai para um quarto", "cai para 1/16", "não muda, porque a janela compensa"],
   "O débito é proporcional a 1/√L: √4 = 2, por isso cai para <b>metade</b>.",
   ["Seria assim se fosse proporcional a 1/L.",
    "Seria assim com 1/L².",
    "A janela não compensa: é a própria taxa de perdas que limita a janela média."],
   "reno", calc=["débito ∝ 1/√L → 1/√4 = 1/2"], lembrar="débito ∝ 1/√L."),
 Q("CG9", "Ligação de capacidade R já com 9 conexões TCP. Uma aplicação abre mais 10. Que fração da capacidade fica com essa aplicação (equidade ideal por conexão)?",
   "cerca de R/2", ["R/10", "R/19", "R/9"],
   "Cada conexão tem R/K, com K = 9 + 10 = 19. A aplicação tem 10 delas: 10R/19 ≈ <b>R/2</b>. É por isso que conexões paralelas \"fogem\" à equidade.",
   ["R/10 é o que teria se abrisse só 1 conexão (9 + 1 = 10).",
    "R/19 é a fatia de uma conexão, não das 10.",
    "R/9 é o que cada uma das 9 tinha antes."],
   "reno", calc=["K = 9 + 10 = 19 conexões", "aplicação: 10 × R/19 ≈ 0,53 R"], lembrar="equidade é por conexão, não por aplicação."),
 Q("CG10", "Porque é que o AIMD tende a repartir a capacidade de forma equitativa entre duas conexões?",
   "crescem igual, mas a redução a metade tira mais a quem tem mais",
   ["porque os routers dividem a capacidade a meias entre as conexões", "porque a conexão com mais débito tem mais perdas por timeout", "porque o slow start iguala as duas janelas no início"],
   "No gráfico débito 1 × débito 2, o crescimento aditivo é uma reta de declive 1 (não muda a diferença) e o decréscimo multiplicativo reduz proporcionalmente (encolhe a diferença). Os ciclos convergem para a diagonal.",
   ["Os routers não dão feedback nenhum ao TCP (só descartam quando a fila enche).",
    "As duas veem as mesmas perdas na ligação de estrangulamento; o mecanismo é a redução proporcional.",
    "O slow start só acontece no início e depois de timeouts; não explica a convergência."],
   "reno", lembrar="aditivo mantém a diferença; multiplicativo encolhe-a."),
 Q("CG11", "No cenário 3 de congestionamento (vários emissores, caminhos com vários saltos), porque é que o débito útil pode tender para 0?",
   "o que se perde no fim desperdiça a capacidade gasta a montante",
   ["porque a fila infinita faz o atraso tender para infinito", "porque as retransmissões passam a ter prioridade sobre os dados novos", "porque os routers deixam de reenviar pacotes quando estão cheios"],
   "Com carga alta, os pacotes que vêm de longe perdem-se nos últimos saltos: as ligações anteriores trabalharam para nada. O trabalho útil cai a pique: <b>colapso</b> da rede.",
   ["Atraso infinito com fila infinita é o cenário 1, e aí o débito chega a R/2.",
    "Não há prioridades no IP: a fila é FIFO.",
    "Os routers descartam o que não cabe e continuam a reenviar o resto."],
   "cong", lembrar="perda a jusante = capacidade a montante desperdiçada."),
 Q("CG12", "Como é que o emissor TCP sabe que há congestionamento?",
   "infere-o pelas perdas (timeout ou 3 ACKs duplicados)",
   ["os routers enviam-lhe uma mensagem a pedir para abrandar", "o receptor reduz a janela anunciada no cabeçalho", "mede a ocupação das filas dos routers com o traceroute"],
   "Os slides: <b>sem feedback específico dos routers</b>. O núcleo fica simples e a complexidade vai para os terminais, que inferem o congestionamento pelas perdas e atrasos.",
   ["Os routers da Internet não dão este feedback ao TCP (nos slides).",
    "A RcvWindow é o controlo de fluxo: reflete o buffer do receptor, não a rede.",
    "O TCP não usa traceroute."],
   "reno", lembrar="TCP infere: perda = congestionamento."),
])

# ═════════════════════════ Camada de rede: CVs, datagramas, router ═════════════════════════
topic("rede-cv-router", "Q_R2_REDE", "Rede: CVs, datagramas e router", [
 Q("RC1", "Qual é a diferença entre <b>encaminhamento</b> e <b>reenvio</b>?",
   "encaminhamento escolhe a rota e preenche a tabela; reenvio passa o pacote da entrada à saída",
   ["reenvio escolhe a rota e preenche a tabela; encaminhamento passa o pacote da entrada à saída", "encaminhamento é feito nos terminais e reenvio nos routers do núcleo", "encaminhamento é para datagramas e reenvio é só para circuitos virtuais"],
   "Analogia dos slides: encaminhamento = planear a viagem (algoritmos, tabela); reenvio = mudar do metro para o autocarro numa estação (consultar a tabela, mandar o pacote para a interface certa).",
   ["Está trocado.",
    "As duas funções existem nos routers.",
    "As duas existem nos dois tipos de rede."],
   "rede", lembrar="routing = planear; forwarding = mudar de linha."),
 Q("RC2", "Numa rede de circuitos virtuais, cada pacote leva…",
   "um nº de CV, que pode mudar em cada ligação",
   ["o endereço de destino, usado em cada router", "um identificador de CV igual em todo o caminho", "o caminho completo até ao destino, escrito pelo emissor"],
   "Os pacotes levam o <b>número de CV</b> e não o endereço de destino. Esse número é <b>por ligação</b>: em cada router a tabela dá a interface de saída e o número novo (ex.: entra pela 1 com 12, sai pela 3 com 22).",
   ["O reenvio pelo endereço de destino é das redes de datagramas.",
    "Um número global obrigaria a combinar números livres na rede toda; por isso é por ligação.",
    "O caminho fica guardado nas tabelas dos routers, não no pacote."],
   "cv", lembrar="CV: nº por ligação, troca em cada salto."),
 Q("RC3", "Numa rede de circuitos virtuais é impossível haver…",
   "reordenamento", ["perdas de pacotes", "erros de bit", "congestionamento"],
   "Todos os pacotes do CV seguem o <b>mesmo caminho</b>, fixado no estabelecimento, e as filas são FIFO: nenhum ultrapassa outro (F8.2e).",
   ["Podem perder-se pacotes (buffers cheios).",
    "Pode haver erros de bit na transmissão.",
    "Pode haver congestionamento; a reserva de recursos ajuda, mas não o torna impossível."],
   "cv", lembrar="mesmo caminho = mesma ordem."),
 Q("RC4", "Numa rede de circuitos virtuais…",
   "os routers guardam estado sobre cada fluxo",
   ["o reenvio é feito pelo endereço IP de destino", "pacotes do mesmo fluxo podem seguir caminhos distintos", "os pacotes podem ser entregues fora de ordem"],
   "Cada router tem uma entrada por CV que o atravessa (interface/número à entrada e à saída). É o principal custo: estado que cresce com O(n²) no número de terminais.",
   ["O reenvio é pelo número de CV.",
    "Isso é das redes de datagramas.",
    "Com caminho fixo, a ordem mantém-se."],
   "cv", lembrar="CV = estado por conexão nos routers."),
 Q("RC5", "Tabela: <code>11001000 00010111 00010</code> → 0; <code>11001000 00010111 00011000</code> → 1; <code>11001000 00010111 00011</code> → 2; senão → 3. Para onde vai <code>11001000 00010111 00011000 10101010</code>?",
   "interface 1", ["interface 2", "interface 0", "interface 3"],
   "O 3.º byte é <code>00011000</code>: encaixa no prefixo da 1 (24 bits) <b>e</b> no da 2 (<code>00011</code>, 21 bits). O <b>prefixo mais longo</b> ganha: interface 1.",
   ["Também encaixa, mas é o prefixo mais curto.",
    "<code>00011…</code> não começa por <code>00010</code>.",
    "Só se usa a \"senão\" quando nenhum prefixo encaixa."],
   "cv", lembrar="vários encaixes → o mais longo."),
 Q("RC6", "Mesma tabela. Para onde vai <code>11001000 00010110 00011000 00000000</code>?",
   "interface 3", ["interface 1", "interface 2", "interface 0"],
   "O <b>2.º byte</b> é <code>00010110</code>, e todos os prefixos têm <code>00010111</code>: não encaixa em nenhum. Vai para a entrada \"senão\".",
   ["O 3.º byte parece o da 1, mas o 2.º já não bate.",
    "Idem: o prefixo falha no 2.º byte.",
    "Idem."],
   "cv", lembrar="compara bit a bit desde o início, não só o fim."),
 Q("RC7", "Porque é que a Internet usa datagramas e o ATM usa circuitos virtuais?",
   "a Internet liga computadores que se adaptam; o ATM vem da rede telefónica",
   ["a Internet precisa de garantias de atraso estritas para a voz e o ATM não precisa", "o ATM foi feito para computadores e a Internet para telefones", "os datagramas reservam recursos e os circuitos virtuais não"],
   "Internet: serviço elástico, terminais \"inteligentes\", núcleo simples e complexidade nas pontas, muitos tipos de ligação. ATM: conversação humana (requisitos temporais estritos), terminais \"estúpidos\", complexidade no núcleo.",
   ["É o contrário.",
    "Está trocado.",
    "Quem pode reservar recursos são os CVs."],
   "cv", lembrar="Internet: pontas inteligentes; ATM: núcleo inteligente."),
 Q("RC8", "Que componente do atraso de um pacote pode ser controlada sem mudar o hardware?",
   "o atraso em fila de espera, reduzindo o congestionamento",
   ["o atraso de propagação, escolhendo caminhos com mais capacidade", "o atraso de transmissão, enviando os pacotes mais depressa", "o atraso de processamento, simplificando o cabeçalho IP"],
   "Transmissão (L/R), propagação (d/v) e processamento dependem do hardware e da física. Só a <b>fila</b> depende da carga (F8.5b).",
   ["A propagação depende da distância e do meio, não da capacidade.",
    "Enviar mais depressa exige uma ligação mais rápida.",
    "O processamento depende do router, não do formato."],
   "rede", lembrar="só a fila se controla."),
 Q("RC9", "Num router, o que é o <b>bloqueio Head-of-Line</b>?",
   "o 1.º pacote de uma fila de entrada, bloqueado, atrasa os de trás",
   ["a fila de saída cheia faz o router descartar o pacote mais antigo", "o processador de encaminhamento bloqueia o reenvio enquanto atualiza a tabela", "um pacote grande na matriz impede todas as entradas de transmitir"],
   "Acontece nas filas de <b>entrada</b>, quando a matriz é mais lenta do que as entradas juntas. Mesmo que a saída do 2.º pacote esteja livre, ele espera atrás do 1.º.",
   ["Isso é perda por extravasamento na saída.",
    "Os slides não descrevem isso; o reenvio usa uma cópia da tabela em cada entrada.",
    "O HOL é numa fila de entrada, não em toda a matriz."],
   "router", lembrar="HOL = filas de entrada."),
 Q("RC10", "Porque é que a comutação através de memória (1.ª geração de routers) é limitada?",
   "cada datagrama atravessa 2 vezes o barramento do sistema",
   ["porque só pode haver uma interface de entrada", "porque obriga a fragmentar todos os datagramas em células", "porque a tabela de encaminhamento não cabe em memória"],
   "O pacote é copiado da entrada para a memória e depois para a saída, sob controlo da CPU: <b>2 travessias</b> do barramento por datagrama.",
   ["Pode haver várias entradas; o problema é a passagem pela memória.",
    "As células de tamanho fixo são do desenho avançado das redes de interligação.",
    "A limitação é de velocidade, não de espaço."],
   "router", lembrar="memória: 2× o barramento."),
 Q("RC11", "Pela regra do RFC 3439, que buffer deve ter uma ligação de 10 Gbps com RTT típico de 250 ms?",
   "2,5 Gbit", ["40 Gbit", "25 Mbit", "250 Mbit"],
   "Buffer = RTT × C = 0,25 s × 10<sup>10</sup> bit/s = 2,5×10<sup>9</sup> bit = <b>2,5 Gbit</b>. Os estudos mais recentes sugerem dividir por √N (N fluxos) ou ainda menos (bufferbloat).",
   ["Dividiu em vez de multiplicar (10/0,25).",
    "Erro de 100× nas unidades.",
    "Erro de 10×: 0,25 × 10 = 2,5 e não 0,25."],
   "router", calc=["0,25 s × 10¹⁰ bit/s = 2,5 × 10⁹ bit"], lembrar="buffer = RTT × C (ou /√N)."),
])

# ═════════════════════════ IP e fragmentação ═════════════════════════
topic("ip-fragmentacao", "Q_R2_IP", "IP e fragmentação", [
 Q("IF1", "Datagrama de 4000 bytes (cabeçalho de 20) numa ligação com MTU de 1500. Que <i>offsets</i> têm os fragmentos?",
   "0, 185 e 370", ["0, 1480 e 2960", "0, 1500 e 3000", "0, 187 e 375"],
   "Dados por fragmento: 1500 − 20 = 1480. O <i>offset</i> conta em unidades de <b>8 bytes</b>: 0, 1480/8 = 185, 2960/8 = 370.",
   ["São os offsets em bytes; o campo conta em blocos de 8.",
    "Usou o comprimento total (1500) em vez dos dados (1480), e em bytes.",
    "Dividiu 1500 por 8 (187,5) em vez de 1480."],
   "ip", calc=["dados = 4000 − 20 = 3980 = 1480 + 1480 + 1020", "offsets: 0, 1480/8 = 185, 2960/8 = 370"], lembrar="offset = bytes de dados antes / 8."),
 Q("IF2", "No mesmo exemplo (4000 B, MTU 1500), qual é o campo <i>length</i> do último fragmento?",
   "1040", ["1020", "1500", "1060"],
   "Dados: 3980 − 1480 − 1480 = 1020; o fragmento leva o seu próprio cabeçalho de 20: <b>1040</b>.",
   ["1020 são só os dados; o <i>length</i> é o comprimento total.",
    "1500 é o length dos fragmentos cheios; o último leva só o resto dos dados.",
    "Somou dois cabeçalhos ao último."],
   "ip", calc=["3980 − 2 × 1480 = 1020 de dados", "length = 1020 + 20 = 1040"], lembrar="length = dados + 20."),
 Q("IF3", "Datagrama de 1500 B com MTU de 600. Quantos bytes de dados leva cada fragmento (menos o último)?",
   "576", ["580", "600", "584"],
   "MTU − 20 = 580, mas os dados de todos menos o último têm de ser <b>múltiplos de 8</b> (o offset conta em 8 bytes): 576 = 8 × 72. Fica 576 + 576 + 328 (F8.3a).",
   ["580 não é múltiplo de 8.",
    "Esqueceu o cabeçalho de 20 do fragmento.",
    "584 é múltiplo de 8, mas 584 + 20 = 604 &gt; 600."],
   "ip", calc=["600 − 20 = 580 → múltiplo de 8 abaixo: 576"], lembrar="(MTU − 20) arredondado para baixo a múltiplo de 8."),
 Q("IF4", "Que valores têm as <i>flags</i> MF dos fragmentos de um datagrama original com MF = 0, partido em 3?",
   "1, 1 e 0", ["0, 0 e 1", "1, 1 e 1", "0, 0 e 0"],
   "MF (<i>more fragments</i>) = 1 em todos menos no <b>último</b>, que herda o MF do original (0).",
   ["Está ao contrário.",
    "O último tem de dizer \"não há mais\".",
    "Com MF = 0 em todos, o destino achava que o 1.º fragmento era o datagrama inteiro."],
   "ip", lembrar="MF = 1 exceto no último."),
 Q("IF5", "Um fragmento com offset 370 e 1020 bytes de dados (MF = 0) atravessa uma ligação com MTU 620. Que <i>offset</i> tem o 2.º sub-fragmento?",
   "445", ["75", "370", "600"],
   "Dados por sub-fragmento: 620 − 20 = 600 (múltiplo de 8). O 1.º leva 600 a partir do offset 370; o 2.º começa 600/8 = 75 blocos depois: 370 + 75 = <b>445</b>. Os offsets contam sempre desde o início do <b>original</b>.",
   ["75 seria o offset se o fragmento fosse um datagrama novo; soma-se ao offset dele.",
    "É o offset do 1.º sub-fragmento.",
    "600 são bytes, não unidades de 8, e falta somar o 370."],
   "ip", calc=["620 − 20 = 600 = 8 × 75", "1.º: offset 370; 2.º: 370 + 75 = 445"], lembrar="fragmentar um fragmento: soma o offset dele."),
 Q("IF6", "Onde são remontados os fragmentos de um datagrama IP?",
   "só no destino",
   ["no primeiro router depois da ligação com MTU pequena", "em cada router, para reenviar o datagrama inteiro", "no router de fronteira da rede de destino"],
   "Os fragmentos podem seguir caminhos diferentes; só o destino os vê todos. E assim não se sobrecarregam os routers (F8.3d).",
   ["Esse router pode nem ver todos os fragmentos.",
    "Remontar em cada router gastava memória e tempo, e a ligação seguinte podia voltar a obrigar a fragmentar.",
    "Também pode não ver todos os fragmentos."],
   "ip", lembrar="remontagem só no destino."),
 Q("IF7", "Para que serve o campo <b>identification</b> do cabeçalho IP?",
   "juntar os fragmentos do mesmo datagrama original",
   ["para o receptor detetar datagramas duplicados e pedir retransmissão", "para escolher o processo de transporte que recebe os dados", "para os routers ordenarem os datagramas de um mesmo fluxo"],
   "Todos os fragmentos do mesmo datagrama levam o mesmo ID (com os mesmos IPs e protocolo). Pergunta de exame antigo.",
   ["O IP não pede retransmissões; isso é do transporte.",
    "Isso é o campo protocolo (e, no transporte, as portas).",
    "Os routers não ordenam nada: o IP é melhor esforço."],
   "ip", lembrar="ID = cola dos fragmentos."),
 Q("IF8", "Um datagrama IP com TCP e sem opções, com 1460 bytes de dados da aplicação. Qual é o overhead de cabeçalhos sem fragmentação?",
   "40 bytes (20 do TCP + 20 do IP)", ["20 bytes, só o IP", "28 bytes (20 do IP + 8 do TCP)", "60 bytes (20 do IP + 40 do TCP)"],
   "Slide do formato IP: com TCP são 20 + 20 = <b>40 bytes</b> por segmento, mais o overhead da aplicação. 40/1460 ≈ 2,7%.",
   ["Esqueceu o cabeçalho TCP.",
    "8 bytes é o cabeçalho UDP.",
    "O TCP sem opções tem 20, não 40."],
   "ip", lembrar="TCP/IP = 40 B de cabeçalhos."),
 Q("IF9", "Para que serve o campo <b>TTL</b> do cabeçalho IP?",
   "limitar o nº de saltos (cada router decrementa-o)",
   ["indica quanto tempo o destino guarda os fragmentos à espera dos outros", "indica o RTT estimado da conexão, para o TCP usar no timeout", "indica a prioridade do datagrama nas filas dos routers"],
   "<i>Time to live</i> = número máximo de saltos restantes, decrementado em cada router; evita que um datagrama ande em ciclo para sempre. Por mudar em cada salto, o checksum do cabeçalho é recalculado em cada router.",
   ["Isso é um temporizador interno do destino, não o TTL.",
    "O IP não sabe nada do RTT do TCP.",
    "A prioridade seria o tipo de serviço; as filas dos slides são FIFO."],
   "ip", lembrar="TTL = saltos restantes."),
])

# ═════════════════════════ Exames antigos (texto adaptado; ordem sorteada) ═════════════════════════
topic("exames-antigos", "Q_R2_EXAMES", "Exames antigos", [
 Q("EA1", "Para garantir um serviço de transporte fiável é necessário…",
   "identificar cada segmento", ["corrigir os erros de transmissão", "enviar segmentos do tipo NAK", "fazer cópias de certos segmentos"],
   "Sem números de sequência não se distinguem duplicados de pacotes novos (rdt2.1 em diante). Os erros recuperam-se por retransmissão.",
   ["Não se corrigem: deteta-se e retransmite-se.",
    "O rdt2.2 e o TCP passam sem NAK.",
    "Não há cópias preventivas."],
   "rdt", lembrar="fiabilidade = checksum + nº seq. + ACK + timer."),
 Q("EA2", "A técnica de fragmentação é usada…",
   "na camada de rede", ["na camada de transporte", "na camada de aplicação", "na camada de ligação de dados"],
   "O IP fragmenta quando o datagrama é maior do que a MTU da ligação seguinte. O transporte <b>segmenta</b>.",
   ["O transporte segmenta as mensagens; fragmentar é do IP.",
    "A aplicação não fragmenta.",
    "A MTU é da ligação, mas quem parte o datagrama é o IP."],
   "ip", lembrar="segmentar (transporte) ≠ fragmentar (rede)."),
 Q("EA3", "O TCP oferece um serviço…",
   "fiável e com controlo de fluxo", ["fiável e com largura de banda garantida", "sem conexão e com deteção de erros", "orientado a conexão e com correção de erros"],
   "Fiável, ordenado, com controlo de fluxo e de congestionamento, orientado a conexões. Não garante débito nem atraso.",
   ["Nenhum transporte da Internet garante largura de banda.",
    "Sem conexão é o UDP.",
    "Deteta erros (checksum) e retransmite; não os corrige."],
   "tcpseg", lembrar="TCP não garante débito nem atraso."),
 Q("EA4", "O uso de pipelining no protocolo de transporte visa…",
   "melhorar o débito efetivo", ["recuperar da perda de pacotes", "recuperar de erros de bit", "evitar sobrecarregar o receptor"],
   "Vários pacotes em trânsito em vez de um por RTT: a utilização multiplica.",
   ["Isso faz-se com temporizadores e retransmissões, com ou sem pipelining.",
    "Isso faz-se com checksum e retransmissão.",
    "Isso é o controlo de fluxo; o pipelining até aumenta o risco."],
   "sw", lembrar="pipelining = débito."),
 Q("EA5", "Pode implementar-se transporte fiável sobre uma rede como a Internet sem usar…",
   "pipelining", ["temporizadores", "confirmações", "retransmissões"],
   "O rdt3.0 é fiável e é stop-and-wait. As outras três são indispensáveis com perdas.",
   ["Sem temporizador, uma perda bloqueava tudo.",
    "Sem ACKs, o emissor não sabe o que chegou.",
    "Sem retransmissões, nada perdido se recupera."],
   "rdt", lembrar="pipelining é desempenho, não fiabilidade."),
 Q("EA6", "No contexto da equidade, uma aplicação TCP pode ser prejudicada por…",
   "outra que abra várias conexões TCP em paralelo",
   ["outra aplicação TCP que use o mesmo MSS", "outra aplicação TCP com o mesmo RTT", "outra aplicação TCP que também use controlo de fluxo no receptor"],
   "A equidade é por conexão: quem abre mais conexões leva mais fatias (os browsers e os download accelerators fazem-no). O UDP, sem controlo de congestionamento, também prejudica.",
   ["Com o mesmo MSS e RTT, o AIMD reparte igual.",
    "RTTs iguais é o caso ideal de equidade.",
    "O controlo de fluxo é com o receptor; não tira capacidade aos outros."],
   "reno", lembrar="conexões paralelas e UDP fogem à equidade."),
 Q("EA7", "A dado momento um emissor TCP reduziu o débito para 1 MSS por RTT. Porque detetou…",
   "uma perda por timeout", ["uma perda por triplo ACK duplicado", "um erro de checksum", "um segmento fora de ordem"],
   "Só o timeout põe CongWin a 1 MSS.",
   ["Triplo ACK dup. reduz só a metade.",
    "Um checksum errado descarta o segmento; quem reage é o timeout ou os ACKs dup.",
    "Fora de ordem gera um ACK duplicado, não uma redução."],
   "reno", lembrar="1 MSS ⇔ timeout."),
 Q("EA8", "Num protocolo de transporte fiável, os temporizadores são necessários para…",
   "recuperar de perdas de pacotes", ["detetar duplicados", "garantir a entrega ordenada", "detetar erros de bit"],
   "Uma perda não gera nenhum evento no emissor: o timeout cria-o (rdt3.0).",
   ["Os duplicados detetam-se com números de sequência.",
    "A ordem garante-se com números de sequência (e buffer).",
    "Os erros de bit detetam-se com o checksum."],
   "rdt", lembrar="timer ⇔ perdas."),
 Q("EA9", "Quando um segmento TCP chega a um terminal, a socket que o recebe é escolhida com base…",
   "nos IPs e portas de origem e de destino", ["no IP e na porta de destino", "na porta de destino", "no IP de destino"],
   "Cada conexão é uma socket identificada pelo tuplo de 4.",
   ["É a regra do UDP.",
    "Todas as conexões de um servidor web têm a porta 80.",
    "O IP sozinho só identifica a máquina."],
   "mux", lembrar="TCP: 4 valores."),
 Q("EA10", "O Go-Back-N e o Selective Repeat têm como objetivo…",
   "melhorar o débito efetivo", ["garantir a entrega ordenada", "recuperar de erros de bit", "adaptar a taxa à capacidade da rede"],
   "São as versões com pipelining da transferência fiável. A ordem e a recuperação de erros já existiam no stop-and-wait.",
   ["O stop-and-wait também garante a ordem.",
    "Isso é o checksum + retransmissão.",
    "Isso é o controlo de congestionamento."],
   "gbnsr", lembrar="GBN/SR = fiável + pipelining."),
 Q("EA11", "No slow start do TCP, o crescimento da janela de congestionamento é…",
   "exponencial", ["linear", "constante", "logarítmico"],
   "Duplica a cada RTT (+1 MSS por ACK). Linear é o congestion avoidance.",
   ["Linear é depois do limiar.",
    "A janela cresce a cada ACK.",
    "Não há nenhuma fase logarítmica no TCP."],
   "reno", lembrar="SS = exponencial; CA = linear."),
 Q("EA12", "A adaptação da taxa de transmissão à capacidade disponível na rede designa-se…",
   "controlo de congestionamento", ["controlo de fluxo", "controlo de acesso ao meio", "controlo de erros"],
   "A <b>rede</b> é o critério. O controlo de fluxo adapta ao receptor.",
   ["O fluxo protege o buffer do receptor.",
    "O acesso ao meio é da camada de ligação.",
    "O controlo de erros trata bits trocados e perdas."],
   "cong", lembrar="rede → congestionamento."),
])

# ═════════════════════════ perguntas que completam a matéria (entram no plano abaixo) ═════════════════════════
topic("extra", "Q_R2_EXTRA", "extra", [
 Q("TU0", "Qual destes serviços o TCP dá e o UDP <b>não</b> dá?",
   "entrega fiável e por ordem, com controlo de fluxo e de congestionamento",
   ["garantia de um atraso máximo e de um débito mínimo para cada conexão", "deteção de erros nos segmentos recebidos através de um checksum", "entrega dos dados ao processo certo, através das portas"],
   "O TCP: fiável, ordenado, controlo de fluxo (não afogar o receptor), controlo de congestionamento (não afogar a rede), com conexão. O UDP é o <b>melhor esforço</b> do IP com portas e checksum. Termos que vais aprender a seguir.",
   ["Nenhum dos dois garante atraso nem débito: o IP por baixo não dá essas garantias.",
    "O checksum existe nos dois.",
    "A multiplexagem por portas existe nos dois."],
   "mux", lembrar="UDP = portas + checksum; TCP = isso + fiabilidade, fluxo, congestionamento, conexão."),
 Q("TU10", "No UDP, o checksum é opcional. Se o cálculo der <code>0000000000000000</code>, o que se envia no campo?",
   "<code>1111111111111111</code>", ["<code>0000000000000000</code>", "<code>0000000000000001</code>", "o datagrama é descartado e recalculado"],
   "\"Tudo zeros\" no campo quer dizer \"sem checksum\". Para não haver confusão, um checksum calculado como zeros envia-se como <b>tudo uns</b> (em complemento para 1, são o mesmo valor: +0 e −0).",
   ["Seria lido como \"este datagrama não tem checksum\".",
    "Mudaria o valor e daria erro na verificação.",
    "Não há nada a recalcular: o valor é válido, só muda a representação."],
   "udp", lembrar="checksum 0 → envia-se 1111…1."),
 Q("RD0", "No rdt, que versão junta um <b>temporizador</b>, e porquê?",
   "a rdt3.0, porque o canal passa a perder pacotes", ["a rdt2.0, porque o canal passa a trocar bits", "a rdt2.1, porque os ACKs podem vir corrompidos", "a rdt2.2, porque deixa de haver NAKs"],
   "Com perdas, nenhum evento chega ao emissor: sem um <b>timeout</b> ficava à espera para sempre. Por ordem: 1.0 canal perfeito; 2.0 checksum + ACK/NAK; 2.1 números de sequência; 2.2 sem NAK; 3.0 temporizador.",
   ["Bits trocados resolvem-se com checksum + ACK/NAK.",
    "ACKs corrompidos resolvem-se com números de sequência.",
    "Tirar o NAK só muda como se avisa o erro (ACK duplicado)."],
   "rdt", lembrar="cada versão resolve um defeito novo do canal."),
 Q("RD9", "No rdt2.1 bastam os números de sequência 0 e 1. Porquê?",
   "só há um pacote em trânsito de cada vez", ["os ACKs não precisam de número de sequência", "o canal nunca perde pacotes nesta versão", "o receptor guarda todos os pacotes num buffer"],
   "Com stop-and-wait o receptor só tem de distinguir \"o pacote novo\" de \"a repetição do anterior\": dois valores chegam.",
   ["No rdt2.2 os ACKs também levam número; e isso não explica o 1 bit.",
    "É verdade que não há perdas no 2.1, mas não é isso que limita os números a 2.",
    "Não há buffer: só um pacote de cada vez."],
   "rdt", lembrar="1 pacote em trânsito → 1 bit chega."),
 Q("TS0", "No TCP, o <b>MSS</b> (<i>maximum segment size</i>) é…",
   "o máximo de dados da aplicação num segmento", ["o tamanho máximo do segmento com o cabeçalho TCP", "o tamanho máximo do datagrama IP numa ligação", "o número máximo de segmentos por confirmar"],
   "MSS = tamanho máximo do campo de <b>dados</b> (sem cabeçalhos). Com 1460 B de dados, o segmento tem 1480 e o datagrama IP 1500.",
   ["O cabeçalho TCP não conta para o MSS.",
    "Isso é a MTU da ligação (vês na camada de rede).",
    "O TCP conta bytes; a quantidade em trânsito é a janela."],
   "tcpseg", lembrar="MSS = só dados."),
 Q("TS11", "A envia <code>Seq=92</code> (8 B) e <code>Seq=100</code> (20 B). O <code>ACK=100</code> perde-se, mas o <code>ACK=120</code> chega antes do timeout. O que retransmite A?",
   "nada", ["o segmento 92", "o segmento 100", "os segmentos 92 e 100"],
   "O ACK é <b>cumulativo</b>: <code>ACK=120</code> diz que B tem tudo até ao byte 119, ou seja, os dois segmentos. O temporizador é cancelado. É um dos três cenários dos slides.",
   ["O 92 está confirmado pelo ACK 120.",
    "O 100 é exatamente o que o ACK 120 confirma.",
    "Os dois estão confirmados."],
   "tcprel", lembrar="ACK cumulativo tapa ACKs perdidos."),
 Q("FC8", "O servidor recebe o FIN do cliente e responde ACK, mas a aplicação dele ainda não fechou. Em que estado fica?",
   "CLOSE_WAIT", ["TIME_WAIT", "FIN_WAIT_2", "LAST_ACK"],
   "Fecho passivo: ESTABLISHED → (recebe FIN, envia ACK) <b>CLOSE_WAIT</b> → (aplicação faz close, envia FIN) LAST_ACK → (recebe ACK) CLOSED.",
   ["TIME_WAIT é do lado que fecha primeiro, no fim.",
    "FIN_WAIT_2 é do cliente, à espera do FIN do servidor.",
    "LAST_ACK vem depois, quando o servidor envia o seu FIN."],
   "fluxo", lembrar="passivo: CLOSE_WAIT → LAST_ACK; ativo: FIN_WAIT_1/2 → TIME_WAIT."),
 Q("CG13", "Cenário 2 do congestionamento (fila finita, retransmissões). Porque é que, com <b>timeouts prematuros</b>, o débito útil já não chega a R/2?",
   "chegam cópias duplicadas, que gastam capacidade sem dados novos", ["a fila infinita faz o atraso crescer sem limite", "os routers descartam primeiro as retransmissões", "o receptor deixa de enviar ACKs quando a fila enche"],
   "Um timeout prematuro retransmite um pacote que não se perdeu: a ligação leva <b>duplicados</b>. Mais retransmissões para o mesmo goodput, e algumas desnecessárias.",
   ["Fila infinita é o cenário 1.",
    "As filas são FIFO: não distinguem retransmissões.",
    "O receptor confirma o que recebe; o problema é do lado do emissor."],
   "cong", lembrar="custos: retransmissões, duplicados, capacidade a montante desperdiçada."),
 Q("CG14", "Qual é a diferença entre o TCP <b>Tahoe</b> e o TCP <b>Reno</b>?",
   "o Tahoe volta a 1 MSS em qualquer perda", ["o Reno volta a 1 MSS em qualquer perda", "o Tahoe não tem fase de slow start", "o Reno não tem limiar de slow start"],
   "O Reno acrescentou a <b>recuperação rápida</b>: com 3 ACKs duplicados corta só a metade. No Tahoe, qualquer perda (timeout ou 3 ACKs dup.) leva a janela a 1 MSS e volta ao slow start.",
   ["É o contrário: o Reno distingue os dois tipos de perda.",
    "Os dois começam em slow start.",
    "Os dois usam o limiar (metade da janela na perda)."],
   "reno", lembrar="Reno = Tahoe + recuperação rápida."),
 Q("CG15", "Para 10 Gbps com RTT de 100 ms e segmentos de 1500 bytes, quantos segmentos têm de estar em trânsito?",
   "≈ 83 333", ["≈ 666 667", "≈ 8 333", "≈ 833 333"],
   "Débito = W·L/RTT, logo W = débito·RTT/L = 10<sup>10</sup> × 0,1 / (1500 × 8) = 10<sup>9</sup>/12 000 ≈ <b>83 333</b>. E pela fórmula 1,22·MSS/(RTT√L) seria precisa uma taxa de perdas de 2×10<sup>−10</sup>: por isso há outras variantes do TCP.",
   ["Esqueceu-se de passar bytes a bits (÷1500 em vez de ÷12 000).",
    "Erro de 10× no RTT (usou 10 ms).",
    "Erro de 10× no RTT (usou 1 s)."],
   "reno", calc=["W = 10¹⁰ × 0,1 / (1500 × 8) = 10⁹ / 12 000 ≈ 83 333"], lembrar="W = débito × RTT / tamanho do segmento."),
 Q("RC12", "Em que redes existe <b>estabelecimento de conexão</b> na camada de rede?",
   "ATM, frame relay e X.25", ["na Internet (IP)", "em todas as redes de datagramas", "só nas redes locais Ethernet"],
   "É a 3.ª função da camada de rede, só em algumas arquiteturas (com circuitos virtuais): os terminais <b>e os routers</b> estabelecem o circuito antes dos dados. No IP não existe.",
   ["O IP não tem conexões; a conexão do TCP é só entre os terminais.",
    "Redes de datagramas, por definição, não têm conexões.",
    "Os slides não falam de Ethernet aqui."],
   "rede", lembrar="CV ⇒ conexão na rede; IP ⇒ não."),
 Q("RC13", "Que garantias dá a camada de rede da Internet (modelo de serviço)?",
   "nenhuma: é melhor esforço", ["entrega garantida, mas sem limite de atraso", "entrega por ordem, mas sem débito mínimo", "atraso máximo, mas sem entrega garantida"],
   "Os slides: entrega garantida, atraso máximo, entrega ordenada, débito mínimo, limite ao jitter — \"na Internet não há nenhuma destas garantias\".",
   ["Os pacotes podem perder-se.",
    "Podem chegar fora de ordem.",
    "Não há limite de atraso."],
   "rede", lembrar="best effort = zero garantias."),
 Q("RC14", "Num router, o que faz o <b>plano de controlo</b> e o que faz o <b>plano de dados</b>?",
   "controlo: corre o encaminhamento; dados: reenvia os pacotes", ["controlo: reenvia os pacotes; dados: corre o encaminhamento", "controlo: verifica checksums; dados: guarda as filas de saída", "controlo: escalona as filas; dados: calcula a tabela"],
   "Plano de controlo = processador de encaminhamento (RIP, OSPF, BGP → tabela, gestão). Plano de dados = interfaces de entrada, matriz de comutação e saídas: o reenvio, à velocidade da linha (cada entrada tem uma cópia da tabela).",
   ["Está trocado.",
    "Não é esta a divisão dos slides.",
    "Está trocado e misturado."],
   "router", lembrar="controlo = routing; dados = forwarding."),
 Q("IF10", "Um datagrama com a <i>flag</i> <b>DF = 1</b> é maior do que a MTU da ligação seguinte. O que acontece?",
   "é descartado", ["é fragmentado na mesma", "é enviado assim mesmo", "é guardado até a MTU aumentar"],
   "DF = <i>don't fragment</i>: o router não o pode partir; como não cabe, é <b>descartado</b> (e o emissor recebe um aviso de erro, ICMP, que é matéria do 3.º teste).",
   ["DF proíbe exatamente isso.",
    "A ligação não transmite mais do que a MTU.",
    "Os routers não guardam datagramas à espera."],
   "ip", lembrar="DF = 1 e não cabe → descartado."),
])

REDES = ROOT.parent / "Redes"
SOL = (REDES / ".fonte" / "SOLUCOES_Redes.md").read_text()
FIG = ROOT / "assets" / "guia-redes"

def bloco_sol(num):
    m = re.search(rf"^### {re.escape(num)} ---.*?\n(.*?)(?=^### |^## |\Z)", SOL, re.S | re.M)
    assert m, f"{num} não está no SOLUCOES_Redes.md"
    return m.group(1)

def alinea_md(num, alinea):
    corpo = bloco_sol(num)
    partes = re.split(r"^#### ", corpo, flags=re.M)
    dados = partes[0].strip()
    for p in partes[1:]:
        titulo, _, texto = p.partition("\n")
        if alinea is None or titulo.startswith(alinea):
            curtos = dados and len(dados) < 3000 and "```" not in dados
            return ((dados + "\n\n") if curtos else "") + texto.strip()
    raise AssertionError(f"{num} {alinea}: alínea não encontrada")

def md_html(md):
    md = re.sub(r"\{width=\d+%\}", "", md)
    r = subprocess.run(["pandoc", "-f", "markdown-implicit_figures", "-t", "html5", "--mathml", "--wrap=none"],
                       input=md, capture_output=True, text=True, check=True)
    return r.stdout

# a figura do gráfico da F7.4 (enunciado)
shutil.copy(REDES / ".fonte" / "moodle" / "img" / "65437-tcpcc.png", FIG / "reno_f7.png")
# gráfico do exame 2025/26 (reconstruído em figuras/src/transporte.py)
subprocess.run(["pdftoppm", "-r", "130", "-png", "-singlefile", str(REDES / "figuras" / "reno_exame25.pdf"), str(FIG / "reno_exame25")], check=True)

F65 = ("<b>Ficha 6, Ex. 5 — Checksums.</b> Um datagrama UDP tem estes 16 bytes (linhas de 32 bits):<br>"
       "<code>01001010 01101010 11011011 00101000</code><br><code>00000000 00010000 00000000 00000000</code><br>"
       "<code>10100010 10101010 10000001 11110101</code><br><code>11010001 11101000 10001010 10110111</code><br><br>")
F61 = ("<b>Ficha 6, Ex. 1 — Stop-and-wait.</b> O Fábio fez um protocolo stop-and-wait para uma rede onde se perdem pacotes "
       "(sem erros de bit). O emissor: \"espera dados\" → envia e passa a \"espera confirmação\"; timeout → reenvia; "
       "confirmação → volta a \"espera dados\".<br><br>")
F62 = ("<b>Ficha 6, Ex. 2 — Repetições seletivas.</b> Selective Repeat em que, em cada instante, o emissor só pode enviar "
       "uma mensagem; uma mensagem chega no instante seguinte, o receptor responde logo, e retransmite-se ao fim de 3 "
       "instantes sem confirmação.<br><br>")
F73 = ("<b>Ficha 7, Ex. 3 — Timeout.</b> Estimação do RTT com α = 0,1 e β = 0,2. ")
F74 = ("<b>Ficha 7, Ex. 4 — Controlo de congestionamento.</b> A figura é a janela de um TCP Reno (MSS) por ronda (RTT).<br>"
       '<img src="assets/guia-redes/reno_f7.png" alt="janela do TCP Reno por ronda" style="max-width:100%"><br>')
C32 = ("<b>Treino — retransmissão rápida.</b> A envia a B segmentos de 500, 300 e 200 bytes a partir do byte 1000; o 1500 "
       "perde-se, o 1800 chega. A envia depois mais três segmentos de 100 bytes, que chegam todos. B guarda os segmentos "
       "fora de ordem e confirma cada um logo.<br><br>")
F83 = ("<b>Ficha 8, Ex. 3 — Quem parte e reparte.</b> Um datagrama IP com 1500 bytes de comprimento total chega a um router "
       "cuja interface para o próximo salto tem MTU de 600 bytes (sem opções).<br><br>")
C42 = ("<b>Treino — fragmentar um fragmento.</b> Um datagrama de 4000 bytes (ID 777) é fragmentado numa ligação com MTU 1500 "
       "(fragmentos de 1480, 1480 e 1020 bytes de dados, offsets 0, 185, 370). Mais à frente, os fragmentos 1 e 3 atravessam "
       "uma ligação com MTU 620.<br><br>")
F81 = ("<b>Ficha 8, Ex. 1 — De janelas e perdas.</b> TCP Reno em congestion avoidance: a janela (em MSS) varia entre W/2 e W, "
       "quando uma perda a reduz a metade.<br><br>")

EX12 = ("<b>Exame 2025/26, Ex. 12.</b> A figura é a evolução da janela de congestionamento de uma conexão TCP (gráfico "
        "reconstruído: o original não se vê na foto).<br>"
        '<img src="assets/guia-redes/reno_exame25.png" alt="janela de congestionamento por RTT" style="max-width:100%"><br>')

TR, RD = "Parte II · Transporte", "Parte II · Rede"
ABERTAS = [  # (tópico, id, número no SOLUCOES, alínea, enunciado, secção, para lembrar)
 (TR, "D-F65b", "F6.5", "(b)", F65 + "(a) Quais são as portas e o tamanho do datagrama? (b) Calcula o checksum, põe-no no datagrama e verifica-o.", "udp",
  "soma com wraparound, depois complemento para 1; o receptor tem de obter tudo uns."),
 (TR, "D-F65d", "F6.5", "(d)", F65 + "(d) Encontra um padrão de erros que o checksum não deteta, e mostra a verificação.", "udp",
  "um 0→1 e um 1→0 na mesma coluna."),
 (TR, "D-F61a", "F6.1", "(a)", F61 + "(a) Explica porque é que as confirmações também precisam de número de sequência (desenha o cenário).", "rdt",
  "timeout prematuro: o ACK atrasado confirma o pacote errado."),
 (TR, "D-F61b", "F6.1", "(b)", F61 + "(b) O protocolo é adequado para 10 Mbps, propagação de 20 ms e pacotes de 1500 bytes? Calcula a utilização.", "sw",
  "U = (L/R)/(RTT + L/R)."),
 (TR, "D-F62b", "F6.2", "(b)", F62 + "(b) Faz o esquema (instante a instante) para 5 blocos (0 a 4), janela 3 e timeout 3, perdendo-se o bloco 3 e a confirmação do bloco 2. Faz no papel e compara.", "gbnsr",
  "SR: buffer fora de ordem, re-ACK de pacotes antigos, só se reenvia o que expira."),
 (TR, "D-F64a", "F6.4", "(a)", "<b>Ficha 6, Ex. 4 — Size matters?</b> Fibra de 5000 km a 2 Gbps (v ≈ 2×10<sup>8</sup> m/s), Selective Repeat com blocos de 1000 B. (a) Quantos blocos tem de ter a janela para fluxo contínuo? Quantos bits de número de sequência?", "gbnsr",
  "janela = (RTT + L/R)/(L/R); SR precisa de gama ≥ 2N."),
 (TR, "D-F73d", "F7.3", "(d)", F73 + "Os RTT medidos foram 54, 63, 55, 57, 68, 56, 55 e 58 ms. O EstimatedRTT inicial é o 1.º RTT e o DevRTT inicial metade dele. Que timeout se usa para o pacote seguinte? Faz a tabela.", "rtt",
  "D com o E antigo; a 1.ª amostra também entra; timeout = E + 4D."),
 (TR, "D-F73a", "F7.3", "(a)", F73 + "SampleRTT(1) é a mais recente. (a) Com 4 amostras, SampleRTT(4) a SampleRTT(1), escreve o EstimatedRTT em função delas.", "rtt",
  "aplica a fórmula 3 vezes a partir de S(4)."),
 (TR, "D-F74", "F7.4", "(h)", F74 + "(h) Em que ronda é transmitido o 70.º segmento? (Confirma também: limiar inicial, tipo de perda nas rondas 16 e 22, e limiar nas rondas 18 e 24.)", "reno",
  "soma as janelas ronda a ronda; metade = 3 ACKs dup., 1 = timeout."),
 (TR, "D-F74i", "F7.4", "(i)", F74 + "(i) Se depois da ronda 26 houver uma perda por triplo ACK duplicado, quais ficam a ser a janela e o limiar?", "reno",
  "Reno, 3 ACKs dup.: limiar = janela = W/2."),
 (TR, "D-C32b", "C3.2", "(b)", C32 + "(a) Que números de sequência e que ACKs têm os três segmentos novos? (b) Quando é que A retransmite o 1500? (c) Que ACK envia B quando o 1500 chega?", "tcprel",
  "conta os ACKs duplicados: o 3.º duplicado dispara a retransmissão."),
 (TR, "D-F81a", "F8.1", "(a)", F81 + "(a) Mostra que a taxa de perdas é ≈ 8/(3W²). (b) Deduz que o débito é ≈ 1,22·MSS/(RTT·√L).", "reno",
  "segmentos num ciclo = Σ(W/2 + n), n = 0..W/2; 1 perda por ciclo."),
 (TR, "D-F72a", "F7.2", "(a)", "<b>Ficha 7, Ex. 2 — Hello Goodbye.</b> (a) Explica o three-way handshake: para que serve e como se processa. (b) Como se terminam as conexões TCP?", "fluxo",
  "SYN(x) → SYN+ACK(y, x+1) → ACK(y+1); fecho FIN/ACK em cada sentido."),
 (TR, "D-F71", "F7.1", None, "<b>Ficha 7, Ex. 1 — Controla o quê?</b> Explica as diferenças entre o controlo de fluxo e o controlo de congestionamento: objetivos e entidade ativa de cada um.", "fluxo",
  "fluxo = receptor (RcvWindow); congestionamento = emissor (CongWin)."),
 (RD, "D-F83a", "F8.3", "(a)", F83 + "(a) Explica como é feita a fragmentação, com os campos relevantes do cabeçalho de cada fragmento.", "ip",
  "(MTU − 20) ↓ múltiplo de 8; offset em unidades de 8."),
 (RD, "D-F83c", "F8.3", "(c)", F83 + "(b) Calcula o overhead dos cabeçalhos IP com e sem fragmentação. (c) Recalcula com o TCP (sem opções).", "ip",
  "o cabeçalho TCP só vai no 1.º fragmento."),
 (RD, "D-C42a", "C4.2", "(a)", C42 + "(a) Em que sub-fragmentos se parte o fragmento 1? Dá length, MF e offset.", "ip",
  "offsets somam-se ao do fragmento; o MF do último é o do pai."),
 (RD, "D-C42b", "C4.2", "(b)", C42 + "(b) E o fragmento 3?", "ip",
  "confirma: offset × 8 + dados do último = dados do original."),
 (RD, "D-F82a", "F8.2", "(a)", "<b>Ficha 8, Ex. 2 — Circuitos virtuais vs. datagramas.</b> (a) Indica vantagens e inconvenientes de cada arquitetura.", "cv",
  "CV: ordem e reserva, mas estado por fluxo; datagramas: simples e robustos, sem garantias."),
 (TR, "D-EX12", "EX25.12", None, EX12 + "(a) Nos instantes 8, 25, 46 e 52 ocorreram eventos que causaram a alteração da evolução da janela. Para cada um desses instantes, identifique detalhadamente o evento ocorrido, justificando devidamente. (b) Diga, justificando, qual é o valor do limiar (ssThresh) nos instantes 20, 40, 50 e 60. (c) Para cada um dos instantes 5, 20, 50 e 60, diga se o TCP está em modo slow start ou congestion avoidance, justificando.", "reno",
  "metade = 3 ACKs dup.; 1 = timeout; chegar ao limiar não é perda."),
 (TR, "D-EX13", "EX25.13", None, "<b>Exame 2025/26, Ex. 13 (2,5 valores).</b> Numa conexão TCP, em determinado instante, os valores estimados do RTT e do seu desvio eram de 20 ms e 5 ms, respectivamente. De seguida, foi recebida uma confirmação de entrega de um segmento, 10 ms depois de esse segmento ter sido enviado. Os parâmetros α (para o RTT) e β (para o desvio) são, respectivamente, α = 0,1 e β = 0,2. (a) Calcule o valor estimado do RTT e do seu desvio no instante imediatamente a seguir à recepção dessa confirmação. (b) Calcule o valor de <i>timeout</i> usado para um segmento enviado logo após a recepção dessa confirmação.", "rtt",
  "D com o E antigo; timeout = E + 4D."),
 (RD, "D-F82d", "F8.2", "(d)", "<b>Ficha 8, Ex. 2 — Circuitos virtuais vs. datagramas.</b> (d) Para que serve o encaixe do prefixo mais longo? Usa-se nas duas arquiteturas?", "cv",
  "agrupar destinos e escolher o mais específico; só em datagramas."),
]

# ═════════════════════════ alíneas das fichas 6–8 que faltavam (auditoria ficha a ficha) ═════════════════════════
topic("extra2", "Q_R2_EXTRA2", "extra2", [
 Q("FX1", "Ficha 6, Ex. 3a. Das funções da camada de transporte, quais tem o <b>UDP</b>?",
   "multiplexagem e deteção de erros", ["multiplexagem, deteção de erros e controlo de fluxo", "deteção de erros e entrega fiável", "multiplexagem e controlo de congestionamento"],
   "Funções do transporte: multiplexagem/desmultiplexagem, deteção de erros (checksum), fiabilidade, controlo de fluxo e controlo de congestionamento. O UDP só tem as <b>duas primeiras</b>; o TCP tem todas (solução oficial da F6.3a).",
   ["O UDP não tem controlo de fluxo: o receptor pode ser afogado.",
    "O UDP não é fiável: perdas e desordem passam.",
    "O UDP não tem controlo de congestionamento."],
   "udp", lembrar="UDP = mux + checksum."),
 Q("FX2", "Ficha 6, Ex. 4b. A janela de 12 501 blocos já dá fluxo contínuo. Faz sentido usar uma janela ainda maior?",
   "sim, se houver perdas: recuperar uma perda demora pelo menos mais um RTT",
   ["não, nunca: depois do fluxo contínuo os blocos a mais ficam à espera", "sim, sempre: uma janela maior aumenta o débito mesmo sem perdas", "não, porque o Selective Repeat proíbe janelas maiores do que a gama"],
   "Sem perdas, não ganha nada (já transmite sem parar). Com perdas, enquanto se espera pelo timeout/retransmissão de um bloco, a janela maior deixa continuar a enviar blocos novos em vez de parar (solução oficial).",
   ["Com perdas, os blocos a mais preenchem o tempo de recuperação.",
    "Sem perdas, a ligação já está ocupada a 100%: não há mais débito para ganhar.",
    "A regra é gama ≥ 2N; com bits suficientes, uma janela maior é possível."],
   "gbnsr", lembrar="janela extra só serve para tapar o tempo de recuperar perdas."),
 Q("FX3", "Ficha 7, Ex. 3b. Com <i>n</i> amostras, sendo S(1) a mais recente, o EstimatedRTT é aproximadamente…",
   "α·Σ (1−α)<sup>i−1</sup>·S(i)", ["α·Σ α<sup>i−1</sup>·S(i)", "(1−α)·Σ α<sup>i−1</sup>·S(i)", "(1/n)·Σ S(i)"],
   "Cada vez que se aplica E ← (1−α)E + αS, as amostras antigas são multiplicadas por (1−α). A amostra i (contando da mais recente) foi multiplicada i−1 vezes: peso α(1−α)<sup>i−1</sup>. Para n grande, o termo do valor inicial desaparece.",
   ["Com α = 0,1, α<sup>i−1</sup> faria as amostras antigas desaparecer quase logo; o fator que se repete é (1−α).",
    "Troca os papéis: a amostra nova pesa α, não 1−α.",
    "Média simples: todas pesariam o mesmo, e o EWMA dá mais peso às recentes."],
   "rtt", lembrar="peso da amostra i: α(1−α)^(i−1)."),
 Q("FX4", "Ficha 7, Ex. 4a. Neste gráfico de um TCP Reno, em que rondas está em <b>slow start</b>?<br>"
   '<img src="assets/guia-redes/reno_f7.png" alt="janela do TCP Reno por ronda" style="max-width:100%">',
   "[1, 6] e [23, 26]", ["[1, 5] e [23, 26]", "[1, 6] e [17, 22]", "só [1, 6]"],
   "A janela <b>duplica</b> por ronda: 1→2→4→8→16→32 (rondas 1–6) e, depois do timeout, 1→2→4→8 (23–26). Nas rondas 7–22 sobe 1 por ronda: congestion avoidance (F7.4b). A ronda 6, em que chega ao limiar 32, ainda conta como slow start (solução oficial).",
   ["A ronda 6 (16→32) ainda é duplicação.",
    "Em 17–22 a janela sobe de 1 em 1 (21→26): é congestion avoidance, porque a perda da ronda 16 foi por 3 ACKs dup.",
    "Depois do timeout da ronda 22 volta ao slow start."],
   "reno", lembrar="duplica = SS; +1 = CA."),
 Q("FX5", "Ficha 7, Ex. 5b. Quanto deve o TCP somar à CongWin por cada ACK para a janela crescer <b>1 MSS por RTT</b>?",
   "MSS·MSS/CongWin", ["MSS", "MSS/2", "CongWin/MSS"],
   "Há n = CongWin/MSS ACKs por RTT. Para somar 1 MSS no total, cada um soma MSS/n = MSS·MSS/CongWin (é a linha do congestion avoidance na tabela do Reno).",
   ["+MSS por ACK duplica a janela por RTT (slow start, F7.5a).",
    "Daria +n/2 MSS por RTT, não +1.",
    "Nem é um número de bytes: CongWin/MSS é o número de segmentos na janela."],
   "reno", calc=["n = CongWin / MSS ACKs por RTT", "por ACK: MSS / n = MSS × MSS / CongWin"], lembrar="CA: +MSS²/CongWin por ACK."),
 Q("FX6", "Ficha 8, Ex. 2b–c. Uma rede A tem ligações que falham com frequência; uma rede B transporta multimédia com débito mínimo e atraso máximo garantidos. Que arquitetura para cada?",
   "A: datagramas; B: circuitos virtuais", ["A: circuitos virtuais; B: datagramas", "circuitos virtuais nas duas", "datagramas nas duas"],
   "Datagramas não têm circuito que caia: os pacotes seguintes seguem outro caminho. Circuitos virtuais permitem <b>reservar recursos</b> por fluxo ao longo do caminho, que é o que dá garantias.",
   ["Está trocado: um CV que perde uma ligação tem de ser restabelecido.",
    "Na rede A, cada falha obrigava a refazer os CVs.",
    "Na rede B, os datagramas (melhor esforço) não dão garantias."],
   "cv", lembrar="falhas → datagramas; garantias → CVs."),
 Q("FX7", "Ficha 8, Ex. 5c. Qual é o principal inconveniente de <b>reservar recursos para cada fluxo</b> na rede?",
   "estado por fluxo nos routers, que cresce com O(n²)", ["deixa de haver entrega ordenada dos pacotes", "aumenta o atraso de propagação dos pacotes", "impede o uso de TCP por cima da rede"],
   "Cada router tem de guardar informação de cada fluxo que o atravessa (entre pares de terminais: O(n²)). A vantagem é a qualidade de serviço garantida (solução oficial).",
   ["Pelo contrário: com reserva (CVs) a ordem até fica garantida.",
    "A propagação depende só da distância e do meio.",
    "O transporte funciona igual por cima."],
   "cv", lembrar="QoS por fluxo custa estado por fluxo."),
])

# ═════════════════════════ Exame 2025/26 (recurso, parte do 2.º teste; texto oficial, versão B) ═════════════════════════
topic("exame25", "Q_R2_EX25", "exame25", [
 Q("XA1", "<b>Exame 2025/26, 1.</b> Por si só, o <i>internet checksum</i> permite",
   "apenas detectar erros.", ["garantir fiabilidade.", "detectar e corrigir erros.", "apenas corrigir erros."],
   "O receptor só fica a saber que algo não bate certo. Não sabe <b>que</b> bit mudou (não corrige) e, sem ACKs e retransmissões, não recupera.",
   ["A fiabilidade precisa também de números de sequência, ACKs, temporizadores e retransmissões. O UDP tem checksum e não é fiável.",
    "Não indica que bit mudou, por isso não há como corrigir.",
    "Sem detetar não se corrige, e o checksum não corrige nada."],
   "udp", lembrar="checksum = só deteção.", original="c"),
 Q("XA2", "<b>Exame 2025/26, 2.</b> No TCP, o fecho de uma conexão",
   "inicia-se com o envio de um segmento com a <i>flag</i> FIN activa.",
   ["é sempre iniciado pelo servidor.", "é sempre iniciado pelo cliente.", "inicia-se com o envio de um segmento com a <i>flag</i> SYN activa."],
   "Quem quer fechar envia FIN, o outro responde ACK, e depois faz o mesmo no seu sentido.",
   ["Qualquer dos lados pode fechar primeiro.",
    "Qualquer dos lados pode fechar primeiro (no HTTP/1.0 é o servidor).",
    "O SYN é do estabelecimento (three-way handshake)."],
   "fluxo", lembrar="SYN abre, FIN fecha; qualquer lado pode começar.", original="d"),
 Q("XA3", "<b>Exame 2025/26, 3.</b> Numa rede baseada em circuitos virtuais, o encaminhamento dos pacotes de dados é feito com base",
   "em identificadores de circuito virtual.",
   ["no nome das máquinas de origem e destino.", "nos endereços das máquinas de origem e destino.", "no endereço da máquina de destino."],
   "Cada pacote leva o número de CV; o router procura (interface de entrada, CV) na tabela e troca-o pelo número de saída.",
   ["Os nomes são da camada de aplicação (DNS).",
    "Os endereços completos só são precisos para estabelecer o circuito.",
    "É a regra das redes de <b>datagramas</b> (Internet)."],
   "cv", lembrar="CV → número de CV; datagramas → endereço de destino.", original="d"),
 Q("XA4", "<b>Exame 2025/26, 4.</b> Se uma aplicação demorar muito a ler e processar os dados recebidos numa <i>socket</i> TCP, isso faz entrar em acção o mecanismo",
   "de controlo de fluxo.", ["AIMD (<i>additive increase, multiplicative decrease</i>).", "de controlo de congestionamento.", "recuperação rápida (<i>fast recovery</i>)."],
   "O buffer do receptor enche, a RcvWindow anunciada desce e o emissor abranda. É proteção do <b>receptor</b>.",
   ["O AIMD é a regra da janela de congestionamento: reage a perdas na rede.",
    "Esse protege a <b>rede</b>; aqui quem está lento é o receptor.",
    "A recuperação rápida segue-se a um triplo ACK duplicado."],
   "fluxo", lembrar="receptor lento → controlo de fluxo.", original="c"),
 Q("XA5", "<b>Exame 2025/26, 5.</b> O objectivo da <i>camada de rede</i> na pilha protocolar TCP/IP é",
   "transferir pacotes entre máquinas que podem não estar directamente ligadas.",
   ["definir mensagens trocadas e procedimentos usados por programas distribuídos.",
    "transferir pacotes apenas entre máquinas adjacentes (i.e., com uma ligação directa entre si).",
    "estabelecer um canal lógico de comunicação entre processos a correr em máquinas distintas."],
   "Da máquina de origem à de destino, passando por routers: é comunicação máquina a máquina.",
   ["É a camada de aplicação.",
    "É a camada de ligação de dados.",
    "Entre <b>processos</b> é a camada de transporte."],
   "rede", lembrar="ligação: vizinhos; rede: máquinas; transporte: processos.", original="b"),
 Q("XA6", "<b>Exame 2025/26, 6.</b> No <i>go-back-n</i>, quando dispara o temporizador",
   "são retransmitidos todos os segmentos ainda não confirmados.",
   ["é retransmitido apenas o último segmento transmitido.", "é retransmitido apenas o primeiro segmento da janela.", "é retransmitido o segmento que tem um número de sequência específico."],
   "Há um só temporizador (o do mais antigo não confirmado); ao expirar, o emissor volta atrás e reenvia toda a janela enviada e não confirmada.",
   ["O receptor GBN descartou também tudo o que veio depois da perda; só o último não chega.",
    "É o que faz o TCP. No GBN reenviam-se todos.",
    "Um temporizador por segmento, e só esse reenviado, é o Selective Repeat."],
   "gbnsr", lembrar="GBN reenvia tudo o que falta confirmar; SR só o que expirou.", original="b"),
 Q("XA7", "<b>Exame 2025/26, 7.</b> Pode implementar-se transporte fiável sobre uma rede como a Internet sem usar",
   "<i>pipelining</i>.", ["temporizadores.", "confirmações.", "retransmissões."],
   "O rdt3.0 é fiável e é stop-and-wait. As outras três são indispensáveis com perdas.",
   ["Sem temporizador, uma perda bloqueava tudo.",
    "Sem ACKs, o emissor não sabe o que chegou.",
    "Sem retransmissões, nada perdido se recupera."],
   "rdt", lembrar="pipelining é desempenho, não fiabilidade.", original="c"),
 Q("XA8", "<b>Exame 2025/26, 8.</b> Num segmento TCP com dados, o número de sequência indica",
   "o número do primeiro byte de dados nesse segmento.",
   ["o número desse segmento.", "o número do último byte de dados nesse segmento.", "o número de segmentos que tinham sido enviados nessa conexão."],
   "O TCP numera <b>bytes</b>: o segmento leva o número do seu 1.º byte no fluxo. O ACK leva o do próximo byte esperado.",
   ["O TCP não numera segmentos (o rdt/GBN/SR é que sim).",
    "É o primeiro. Último byte = seq + comprimento − 1.",
    "Não conta segmentos."],
   "tcpseg", lembrar="seq = 1.º byte; ACK = próximo byte esperado.", original="d"),
 Q("XA9", "<b>Exame 2025/26, 9.</b> A fragmentação IP é necessária para",
   "poder transmitir numa ligação datagramas maiores do que a sua MTU (<i>Maximum Transmission Unit</i>).",
   ["diminuir o atraso de processamento de datagramas grandes.",
    "enviar esses fragmentos por caminhos diferentes, aumentando assim o débito entre o emissor e o receptor.",
    "partir mensagens demasiado grandes para caberem num segmento TCP."],
   "Cada ligação tem a sua MTU; se o datagrama não cabe, o router parte-o, e o destino remonta.",
   ["Pelo contrário: fragmentar e remontar dá mais trabalho.",
    "Os fragmentos até podem seguir caminhos diferentes, mas não é esse o objetivo.",
    "Isso é a segmentação do TCP (transporte), pelo MSS."],
   "ip", lembrar="fragmentação ⇔ datagrama &gt; MTU.", original="a"),
 Q("XA10", "<b>Exame 2025/26, 10.</b> A principal limitação do <i>Stop-and-Wait</i> é",
   "poder limitar severamente a taxa de transmissão.",
   ["retransmitir todos os segmentos na janela em caso de <i>timeout</i>, mesmo que apenas um se tenha perdido.",
    "não garantir a entrega ordenada dos segmentos.",
    "não ser capaz de detectar perdas de confirmações."],
   "Um pacote por RTT: U = (L/R)/(RTT + L/R), muito baixa quando o RTT é grande face a L/R.",
   ["É a limitação do Go-Back-N; no stop-and-wait só há um segmento em trânsito.",
    "Garante: só envia o seguinte depois de confirmado o anterior.",
    "Um ACK perdido provoca timeout e retransmissão (rdt3.0)."],
   "sw", lembrar="stop-and-wait: correto mas lento.", original="d"),
 Q("XB9", "<b>3.º teste de 2025/26, 9 (a única que também é matéria deste teste).</b> Na seguinte lista de funções há apenas uma que nunca existe na camada de rede. Identifique-a.",
   "Controlo de acesso ao meio", ["Encaminhamento", "Reenvio (<i>forwarding</i>) de pacotes", "Estabelecimento de circuitos virtuais"],
   "Decidir quem transmite num meio partilhado é da camada de <b>ligação de dados</b>. As outras três são as funções da camada de rede (a terceira só em redes de circuitos virtuais).",
   ["Escolher os caminhos é função da camada de rede.",
    "Passar o pacote da interface de entrada para a de saída é função da camada de rede.",
    "Existe em redes como o ATM; a Internet é que não a tem."],
   "rede", lembrar="rede = encaminhar + reenviar (+ estabelecer CVs).", original="a"),
 # recurso de fevereiro de 2026: só se conhece o assunto das perguntas (as opções são nossas)
 Q("XC1", "<b>Saiu em 2025/26 (reconstruída; opções nossas).</b> As duas principais funções da camada de rede são",
   "reenvio e encaminhamento", ["controlo de fluxo e de congestionamento", "multiplexagem e deteção de erros", "acesso ao meio e encaminhamento"],
   "Reenvio (local, dentro de um router) e encaminhamento (global, calcular os caminhos).",
   ["São do transporte (TCP).", "São as funções do UDP, na camada de transporte.", "O acesso ao meio é da camada de ligação."],
   "rede", lembrar="forwarding + routing."),
 Q("XC2", "<b>Saiu em 2025/26 (reconstruída; opções nossas).</b> Que função existe tanto no TCP como no UDP?",
   "deteção de erros", ["controlo de fluxo", "controlo de congestionamento", "estabelecimento de conexão"],
   "Ambos têm checksum (e multiplexagem por portas). O UDP descarta o que vem errado; o TCP retransmite.",
   ["Só o TCP (RcvWindow).", "Só o TCP (CongWin).", "Só o TCP (three-way handshake)."],
   "udp", lembrar="em comum: mux + checksum."),
 Q("XC3", "<b>Saiu em 2025/26 (reconstruída; opções nossas).</b> No Selective Repeat com números de sequência de 4 bits, o tamanho máximo da janela é",
   "8", ["4", "15", "16"],
   "4 bits dão 16 números; a janela pode ter no máximo metade.",
   ["4 é o número de bits, não a janela.", "15 = 2<sup>4</sup> − 1 é o máximo do <b>Go-Back-N</b>.", "16 é a gama toda: o receptor confundia pacotes novos com repetidos."],
   "gbnsr", calc=["gama = 2⁴ = 16", "N ≤ 16 / 2 = 8"], lembrar="SR: 2^(k−1); GBN: 2^k − 1."),
])

# ═════════════════════════ plano de estudo: ordem da matéria, sem dependências para a frente ═════════════════════════
# Cada tópico: as de escolha múltipla pela ordem em que a matéria se aprende (conceito → regra → conta) e, logo a
# seguir, as de desenvolvimento (Parte II) que usam essa matéria. Nenhuma pergunta precisa de um tópico posterior.
PLANO = [
 ("01-transporte-udp", "1 · Transporte, portas e UDP",
  "TU0 TU1 TU2 TU3 TU4 FX1 TU5 TU9 TU6 TU7 TU8 TU10", "D-F65b D-F65d"),
 ("02-rdt", "2 · Transferência fiável e stop-and-wait",
  "RD0 RD1 RD9 RD2 RD3 RD4 RD8 RD5 RD6 RD7", "D-F61a D-F61b"),
 ("03-gbn-sr", "3 · Go-Back-N e Selective Repeat",
  "GS8 GS1 GS2 GS9 GS3 GS4 GS6 GS5 GS7 FX2", "D-F64a D-F62b"),
 ("04-tcp-seq-timeout", "4 · TCP: sequência, ACKs e timeout",
  "TS0 TS1 TS8 FX3 TS5 TS6 TS7 TS3 TS2 TS11 TS4", "D-F73a D-F73d D-C32b"),
 ("05-tcp-fluxo-conexoes", "5 · TCP: fluxo e conexões",
  "TS9 FC1 FC2 FC4 FC5 FC7 FC8 FC6", "D-F72a"),
 ("06-congestionamento", "6 · Congestionamento e TCP Reno",
  "CG11 CG13 CG12 CG6 FX5 CG1 CG3 CG5 CG14 FX4 CG2 CG4 FC3 CG7 CG8 CG15 CG10 CG9", "D-F71 D-F74 D-F74i D-F81a"),
 ("07-rede-routers", "7 · Rede: CVs, datagramas e routers",
  "RC1 RC12 RC13 RC2 RC4 RC3 RC5 RC6 RC7 FX6 RC14 RC10 RC9 RC11 RC8 FX7", "D-F82a D-F82d"),
 ("08-ip-fragmentacao", "8 · IP e fragmentação",
  "IF9 IF8 IF7 IF3 IF1 IF2 IF4 IF10 IF5 IF6", "D-F83a D-F83c D-C42a D-C42b"),
 ("09-revisao-exames", "9 · Revisão final: exames antigos",
  "EA1 EA2 EA3 EA4 EA5 EA6 EA7 EA8 EA9 EA10 EA11 EA12", ""),
]
# Perguntas do exame de 2025/26: entram no plano a seguir à pergunta indicada. Ficam à parte do PLANO para a posição
# da certa nas outras não mudar (o progresso guardado refere-se a ela).
EXAME = {"FX1": "XC2", "TU9": "XA1", "RD8": "XA10", "RD7": "XA7", "GS4": "XA6", "GS5": "XC3", "TS1": "XA8", "FC7": "XA2",
         "FC3": "XA4", "RC1": "XA5 XC1", "RC12": "XB9", "RC2": "XA3", "IF9": "XA9",
         "D-F73d": "D-EX13", "D-F74i": "D-EX12"}
def com_exame(ids): return [x for i in ids.split() for x in [i] + EXAME.get(i, "").split()]
POOL = {q["id"]: q for _, _, _, qs in TOPICOS for q in qs}
ABERTA = {a[1]: a for a in ABERTAS}
usadas = [i for _, _, mc, ab in PLANO for i in com_exame(mc + " " + ab)]
assert len(usadas) == len(set(usadas)), "pergunta repetida no plano"
assert set(usadas) == set(POOL) | set(ABERTA), f"fora do plano: {(set(POOL) | set(ABERTA)) ^ set(usadas)}"

def aberta(qid, topico):
    _, _, num, alinea, texto, sec, lembrar = ABERTA[qid]
    if qid == "D-F74":   # a (h) e as leituras do gráfico (c)-(g) vêm juntas
        md = "\n\n".join(f"**{a}** " + alinea_md(num, a) for a in ["(c)", "(d)", "(e)", "(f)", "(g)", "(h)"])
    elif qid in ("D-F65b", "D-C32b", "D-F81a", "D-F72a", "D-F83c", "D-EX12", "D-EX13"):   # várias alíneas no mesmo enunciado
        al = {"D-F65b": ["(a)", "(b)"], "D-C32b": ["(a)", "(b)", "(c)"], "D-F81a": ["(a)", "(b)"],
              "D-F72a": ["(a)", "(b)"], "D-F83c": ["(b)", "(c)"], "D-EX12": ["(a)", "(b)", "(c)"], "D-EX13": ["(a)", "(b)"]}[qid]
        md = "\n\n".join(f"**{a}** " + alinea_md(num, a) for a in al)
    else:
        md = alinea_md(num, alinea)
    exp = f'<div class="sol-title">Resolução</div><div class="sol-aberta">{md_html(md)}</div>'
    nota = (f"<b>Para lembrar:</b> {lembrar}<br>"
            f'Se a resolução não chegou, lê a teoria: <a class="teoria" href="{GUIA}#{S[sec]}" target="_blank">'
            f'📖 {TITULO[S[sec]]}</a>')
    return [topico, qid, "<b>Desenvolvimento (Parte II).</b> " + texto, None, -1, exp, nota]

rng = random.Random(20261122)
ex_mc = [i for v in EXAME.values() for i in v.split() if i in POOL]
ex_pos = [(i + 2) % 4 for i in range(len(ex_mc))]
random.Random(2526).shuffle(ex_pos)
EX_POS = dict(zip(ex_mc, ex_pos))
glob = [0] * 4
OUT.mkdir(parents=True, exist_ok=True)
for f in OUT.glob("*.js"): f.unlink()
txt = lambda s: re.sub(r"<[^>]+>", "", s)
total = mais_comprida = n_abertas = 0
variaveis, ficheiros = [], []
for n_t, (slug, nome, mc, ab) in enumerate(PLANO, 1):
    qs = [POOL[i] for i in mc.split()]
    n = len(qs)
    pos = [i % 4 for i in range(n - n % 4)]
    resto = sorted(range(4), key=lambda l: (glob[l] + pos.count(l), rng.random()))[: n % 4]
    pos += resto
    rng.shuffle(pos)
    for p in pos: glob[p] += 1   # só as do PLANO
    onde = dict(zip(mc.split(), pos)) | EX_POS
    qs = [POOL[i] for i in com_exame(mc)]
    n = len(qs); pos = [onde[q["id"]] for q in qs]
    ab = " ".join(com_exame(ab))
    entries = [montar(q, p, nome) for q, p in zip(qs, pos)]
    mais_comprida += sum(len(txt(q["right"])) > max(len(txt(w)) for w in q["wrongs"]) for q in qs)
    entries += [aberta(i, nome) for i in ab.split()]
    var = f"Q_R2_T{n_t}"
    body = ",\n".join("  " + json.dumps(e, ensure_ascii=False) for e in entries)
    (OUT / f"{slug}.js").write_text(
        f"/**\n * Banco de perguntas — {nome} (Redes de Comunicação, Teste 2). {n} de escolha múltipla"
        f" + {len(ab.split())} de desenvolvimento.\n * GERADO por tools/redes-guide/perguntas2.py — edita lá, não aqui.\n"
        f" * Esquema: [topic, id, questionHtml, [4 options] | null, correctIdx | -1, explanationHtml, hintHtml]\n */\n"
        f"/* eslint-disable */\nconst {var} = [\n{body},\n];\n")
    variaveis.append(var); ficheiros.append(slug)
    total += n; n_abertas += len(ab.split())
    print(f"{nome:42s} {n:3d} + {len(ab.split())} abertas  A-D: {[pos.count(i) for i in range(4)]}")
print(f"total {total} + {n_abertas} abertas; certa A-D: {[a + ex_pos.count(i) for i, a in enumerate(glob)]}; certa é a mais comprida em {mais_comprida} ({100*mais_comprida/total:.0f}%)")
assert mais_comprida <= 0.30 * total, "a certa é a opção mais comprida demasiadas vezes"

# junta o banco (pela ordem do plano) e liga os ficheiros no redes2.html
(ROOT / "output-redes2.js").write_text(
    "/* GERADO por tools/redes-guide/perguntas2.py: o banco do 2.º teste, pela ordem do plano de estudo. */\n"
    f"const ALL = [{', '.join('...' + v for v in variaveis)}];\n")
pagina = ROOT / "redes2.html"
h = pagina.read_text()
tags = "\n".join(f'<script src="assets/js/data/questions-redes2/{f}.js"></script>' for f in ficheiros)
h = re.sub(r'(?:<script src="assets/js/data/questions-redes2/[^"]+"></script>\n)+', tags + "\n", h)
pagina.write_text(h)
