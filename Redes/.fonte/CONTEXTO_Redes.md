# CONTEXTO_Redes (convenções e factos; não gera PDF)

**Exercícios.** Fichas numeradas `F2.x`, `F3.x`, `F4.x` (Ficha N, Ex. x); da
Ficha 1 como `Ex. N`; alíneas `**(a)**` no início da linha (um `**(i)**` a
meio da linha é um subcaso, não uma alínea). Exemplo-modelo:
`SOLUCOES_Redes.md`, `### F2.2` (l. ~8). A Ficha 1 tem soluções oficiais
(`Praticas/Semana_1/solucoes_ficha_1.pdf`): compara e assinala as diferenças
sem apagar nenhuma.

**Comandos reais.** Exercícios "corre este comando" (`dig`, `telnet`, `ping`,
`traceroute`, `nc`): corre-os e mostra a saída real, com a data. Nunca ações
com efeitos pelo Gonçalo (no SMTP, só `EHLO`/`QUIT`).

**Capturas `.cap`.** Nome `Teoricas/Aula_NN_captura_<proto>.cap`; lê-se com
`tcpdump -nn -A -r` (não há Wireshark); os números dos pacotes tiram-se com
`tcpdump -# -nn -r` **sem filtro** (com filtro, a numeração não bate com a do
Wireshark).

**Soluções oficiais e testes.** As fichas 2 e 3 têm respostas oficiais
(`Praticas/Semana_2/respostas.pdf`, `Semana_3/respostas-2.pdf`): curtas, só
fórmula e resultado. Os testes modelo ficam em `Testes/Teste_Modelo_N.pdf`
(+ `_resolucao.pdf`, digitalizado: ver como imagem) e os exercícios são
`MN.x`: os da Parte II na caixa do tópico, a escolha múltipla numa caixa no
fim. 1.º teste: 75 min, sem calculadora (contas em potências de 10).

**Fichas do Moodle → PDF.** As fichas são páginas do Moodle, não PDFs: a skill
`moodle-refresh` passa-as a `Praticas/Semana_N/ficha_N_<tema>.pdf` (soluções:
`solucoes_ficha_N.pdf`), com a fonte em `.fonte/moodle/`. As fichas 5 e 6 e o
trabalho foram feitos à mão antes da skill (`.fonte/moodle/gerar.py` + `conteudo.py`).
O trabalho prático está em `Trabalho/` (enunciado, guia passo a passo, esqueletos).

**2.º teste (25/11/2026, 16:30, FC2 009).** Matéria: Camada de Transporte
(Cap. 3, `Aula_04`) e Camada de Rede até à fragmentação IP inclusive
(Cap. 4, `Aula_05`, slides 1--36). O endereçamento IPv4 (slide 38 em
diante: sub-redes, máscaras, DHCP, NAT, ICMP, IPv6), a Ficha 8 Ex. 3e e 4
e a Ficha 9 são do 3.º teste. Não há teste modelo do 2.º teste.

**Convenções dos Cap. 3--4.** Exercícios inventados `C3.x`/`C4.x`;
escolha múltipla de exames antigos `EA.x` (fonte: `~/Desktop/universidade 2/3ºano/Redes de Comunicação/Testes e Exames/.../RC - múltiplas.pdf`,
sem respostas oficiais). RTT/timeout: o DevRTT usa o EstimatedRTT
**antigo** e a 1.ª amostra também entra; é a única leitura que dá os
84,9 ms oficiais da F7.3d. Reno: a ronda em que o *slow start* chega ao
limiar ainda conta como SS (solução oficial da F7.4a). Figuras dos Cap.
3--4: `figuras/src/transporte.py` (matplotlib, `uv run -q --with
matplotlib==3.9.2 python -I figuras/src/transporte.py` a partir de
`Redes/`) e `figuras/router.dot`.

**Material antigo útil** (não copiado para o repo): `~/Desktop/universidade 2/3ºano/Redes de Comunicação/`
tem fichas antigas com soluções (HTML) e resumos de anos anteriores
(`Aulas Teóricas/Resumos/`); `~/Desktop/LCC-MIERSI/.../Redes de Comunicacao/Aulas Teóricas/Livros/`
tem o livro adotado (Kurose & Ross, 6.ª ed., PDF).
