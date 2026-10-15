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
