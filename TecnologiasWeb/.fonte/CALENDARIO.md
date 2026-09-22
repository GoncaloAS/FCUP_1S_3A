# Tecnologias Web — Calendário 2026/27

<!-- Fonte: iframe Google Sheets embutido em geral/calendario.mdown, lido
     visualmente (a folha em si não é extraível por scraping de texto) -->

O calendário publicado no site é uma folha de cálculo incorporada (não dá
para copiar o texto diretamente) — abri-a no browser e transcrevi a tabela
abaixo. Cobre desde 14 de setembro até 14 de dezembro de 2026 (não há, por
agora, datas publicadas para além disso — nomeadamente não há período de
exames visível nesta folha).

**As aulas teóricas são sempre à segunda e quinta-feira, 16:00–17:00.** Estás
na **turma PL2** (quinta-feira, 14:00–16:00, docente Jaime Vale) — as datas
abaixo já estão ajustadas à tua turma.

## Onde estamos agora (atualizado a 22 de setembro de 2026)

Já demos as **Aulas 1 a 3** (Introdução, Web, HTML — segunda 14, quinta 17
e segunda 21 de setembro). A **Aula 4** é já esta quinta-feira, 24 de
setembro (início de CSS). A **Folha 1** (ver mapeamento abaixo) já devia
estar disponível para fazeres desde a Aula 3.

## Datas mais importantes (entregas e testes) — para a tua turma PL2

| O quê | Prazo / data | Valor |
|---|---|---|
| **1ª Entrega** (trabalho — jogo, versão só-cliente) | até **sexta-feira, 30 de outubro de 2026**; tolerância até **segunda, 2 de novembro às 10:00** *(prazo de submissão é igual para todas as turmas — não depende do teu dia de prática)* | 3 valores |
| **1º Teste** | **quinta-feira, 5 de novembro de 2026, 14:00–16:00** — na tua aula prática (PL2), em computador | 4 valores |
| **2ª Entrega(s)** (trabalho — protocolo cliente/servidor + servidor Node.js) | até **sexta-feira, 11 de dezembro de 2026**; tolerância até **segunda, 14 de dezembro às 10:00** | 5 valores |
| **2º Teste** | **provavelmente segunda-feira, 14 de dezembro de 2026** — no site aparece marcado com "‼", símbolo cuja legenda ("num único momento, para todas as turmas") está desativada (comentada) na página fonte. Se for mesmo "um único momento para todas as turmas", aplica-se a ti mesmo sendo PL2 (não é à quinta); mas como a nota está desativada, **confirma esta data com o docente antes de a dares como certa** | 8 valores |

**Regra geral de prazos** (nota de rodapé do calendário): entrega até à
sexta-feira da semana anterior à indicada, com tolerância até segunda-feira
seguinte às 10:00. É isso que já apliquei nas datas acima.

## Calendário completo, aula a aula

| Data | Dia | Aula nº | Rubrica | Tópico | Prática (Folha) | Avaliação |
|---|---|---|---|---|---|---|
| 14 set | Seg | 1 | Introdução | Apresentação | | |
| 17 set | Qui | 2 | Introdução | Web | | |
| 21 set | Seg | 3 | Cliente | HTML | Folha 1 | |
| 24 set | Qui | 4 | Cliente | CSS | Folha 2 | |
| 28 set | Seg | 5 | Cliente | CSS | Folha 2 | |
| 1 out | Qui | 6 | Cliente | (CSS, continuação) | | |
| 5 out | Seg | — | *Feriado* | | | |
| 8 out | Qui | 7 | Cliente | CSS | | |
| 12 out | Seg | 8 | Cliente | JS | | |
| 15 out | Qui | 9 | Cliente | JS | | |
| 19 out | Seg | 10 | Cliente | JS | | |
| 22 out | Qui | 11 | Cliente | JS | | |
| 26 out | Seg | 12 | Comunicação | HTTP | | |
| 29 out | Qui | — | *Formação em Competências Transversais* | | | |
| 2 nov | Seg | 13 | Comunicação | HTTP | | 1ª Entrega (prazo, todas as turmas) |
| **5 nov** | **Qui** | 14 | Comunicação | HTTP | | **1º Teste ‡ (PL2)** |
| 9 nov | Seg | 15 | Comunicação | AJAX | Folha 3 | |
| 12 nov | Qui | 16 | Comunicação | AJAX | Folha 3 | |
| 16 nov | Seg | 17 | Comunicação | AJAX | | |
| 19 nov | Qui | 18 | Servidor | Node | | |
| 23 nov | Seg | 19 | Servidor | Node | | |
| 26 nov | Qui | 20 | Servidor | Node | | |
| 30 nov | Seg | 21 | Comunicação | CGI | | |
| 3 dez | Qui | 22 | Comunicação | APIs | | |
| 7 dez | Seg | 23 | Comunicação | APIs | | |
| 10 dez | Qui | — | | | | |
| **14 dez** | **Seg** | — | | | | **2º Teste ‼ / 2ª Entregas** |

## Que ficheiro é cada "Folha"

O calendário só diz "Folha 1/2/3" — não diz a que pasta isso corresponde
em `conteudo_site/praticas/folhas/`. Mapeamento (confirmado a partir do
conteúdo de cada pasta):

| Folha (calendário) | Pasta | Conteúdo |
|---|---|---|
| **Folha 1** | `folhas/homepage/` | Criar uma página HTML, publicá-la no servidor, validá-la no W3C. |
| **Folha 2** | `folhas/styling/` | Formatar caraterísticas gráficas e posicionar elementos com CSS. |
| **Folha 3** | `folhas/mashup/` | Combinar serviços web existentes (*mashup*) — usa AJAX. |

**Legenda dos símbolos** (das notas de rodapé do calendário):
- **†** — entrega até à sexta-feira da semana anterior, tolerância até segunda-feira às 10:00.
- **‡** — na aula prática, em computador.
- **‼** — nota comentada/desativada na página fonte (dizia "num único momento, para todas as turmas"); mantenho o símbolo mas não confio 100% no significado até confirmares com o docente ou veres o site atualizado.

## Sumários detalhados, aula a aula

Isto vem de uma segunda folha de cálculo do site (`geral/sumarios.mdown`,
"Sumários previstos") — descreve com mais detalhe o que cada aula cobre,
para além do tópico resumido da tabela acima.

**Aula 1** (14 set): Apresentação da unidade curricular e do seu funcionamento: objectivos, programa, conteúdos, bibliografia, aulas previstas, método de avaliação e cálculo da classificação final.

**Aula 2** (17 set): Da World Wide Web à web. O modelo cliente-servidor. Navegadores e clientes web. As tecnologias web. Introdução ao HTML. Morfologia dos constituintes de um documento HTML.

**Aula 3** (21 set): Elementos estruturais do HTML. Formatação em linha e em bloco. Exemplos de elementos HTML de ambos os géneros. Tipo de documento HTML e validação de documentos.

**Aula 4** (24 set): Formulários e diferentes tipos de componentes de interação (widgets). Tabelas e a sua estruturação em linhas e células. Intervalos de células. Tabelas versus posicionamento. Outros elementos estruturais de tabelas. Introdução às Cascading Style Sheets.

**Aula 5** (28 set): Morfologia das regras CSS e políticas de aplicação dessas regras para resolver potenciais ambiguidades. Associação de CSS ao HTML. Folhas de estilos partilhadas, regras embebidas e estilos inseridos. Utilização de classes e identificadores como seletores. Contentores HTML para formatação em CSS.

**Aula 6** (1 out): Características gerais das propriedades do CSS. Propriedades CSS para controlar o retângulo onde é renderizado cada elemento (caixa).

**Aula 7** (8 out): Propriedades CSS para formatação de: cores, texto, e tipos de letra. Posicionamento de elementos usando CSS.

**Aula 8** (12 out): Padrões de seletores em CSS. Exemplos de utilização de CSS na formatação e posicionamento: caixa de diálogo e calculadora. Introdução ao JavaScript. Três exemplos de programas elementares em JavaScript.

**Aula 9** (15 out): Sintaxe básica do JavaScript — tipos, expressões, funções, declaração e âmbito de variáveis, elevação de variáveis, funções anónimas. Notação de objetos. Estruturas de dados. Criação de objetos a partir de classes. Propriedades, índices de objetos e equivalência entre ambos. Iteração sobre campos de objetos.

**Aula 10** (19 out): Programação orientada a objetos em JS, possibilidades e limitações. Métodos e campos, construtores, protótipos, herança. Notificação usando métodos (*callbacks*). Reflexão do documento como estruturas de objetos: widgets de formulários, objetos para reflexão de propriedades CSS. Reflexão da estrutura do documento usando o Document Object Model (DOM).

**Aula 11** (22 out): Programação por eventos em JavaScript. Diferentes formas de registo de eventos: atributos HTML, propriedades e funções para maior controlo. Fases de propagação de eventos. Classes de objetos que corporizam eventos. Tipos de eventos JavaScript: rato, teclado e widgets. Exemplos de interfaces com utilizador ilustrando criação de classes de interação, geração de componentes usando DOM e processamento de eventos com métodos.

**Aula 12** (26 out): Apresentação do protocolo HTTP: agentes, características, versões, estrutura das mensagens, pedidos e respostas. Examinar o HTTP usando o navegador, o serviço `telnet` e o comando `curl`. Caracterização dos recursos no HTTP: URLs, tipos de media e codificações de dados. Métodos dos pedidos HTTP e sua caracterização.

**Aula 13** (2 nov): Métodos seguros, idempotentes e cacháveis do HTTP. Códigos de estado das linhas de resposta. Cabeçalhos das mensagens HTTP: identificação, metadados, redireção e estado.

**Aula 14** (5 nov): Cabeçalhos HTTP: cache de pedidos, partilha de recursos (CORS) e autenticação. Protocolo HTTP seguro: transmissão em canal seguro, certificados digitais.

**Aula 15** (9 nov): Atualização de formatação em HTML usando âncoras e formulários. Comunicação de dados usando HTTP. Serialização de dados: necessidade, exemplos de formatos, o formato JSON, conversão de/para JSON em JavaScript. Pedidos de dados usando `XMLHttpRequest`: pedidos síncronos, construtor, métodos `open()` e `send()`, receção de dados.

**Aula 16** (12 nov): Problemas do processamento síncrono. Pedidos assíncronos usando `XMLHttpRequest`: envio de dados, cabeçalhos, CORS em XHR. Fluxo de execução síncrono e assíncrono: retornar dados, encadear pedidos.

**Aula 17** (16 nov): Envio de dados em tempo real do servidor para o cliente: alternativas pré-HTML5, Server-Sent Events. Comunicação em tempo real com WebSockets. Comparação entre SSE e WebSockets. Exemplos: contador multi-utilizador e jogo do galo. API WebStorage (persistência local).

**Aula 18** (19 nov): Introdução ao Node.js. Servidor básico: importação de módulo, função de serviço, escuta. Lançamento a partir da linha de comando. Módulos em Node.js: mecanismo de inclusão, variáveis globais, padrões de importação (variáveis, funções, construtores).

**Aula 19** (23 nov): Módulos internos do Node. Processamento de pedidos HTTP e análise de URLs. A interface `stream` na leitura de pedidos. Módulo `fs` (sistema de ficheiros), síncrono e assíncrono.

**Aula 20** (26 nov): Exemplos de servidores com Node.js: servidor de páginas estáticas, contador multi-utilizador com difusão via SSE, servidor do jogo do galo com WebSockets.

**Aula 21** (30 nov — a folha de cálculo original tem esta linha marcada "30 Dezembro", o que não bate certo com a sequência das aulas anteriores/seguintes; corrigi para 30 de novembro, mas **confirma com o docente se tiveres dúvida**): Protocolos de comunicação servidor-aplicações: CGI, FastCGI e SimpleCGI. Modelo de execução CGI: variáveis de ambiente, processamento de entrada/saída standard.

**Aula 22** (3 dez): Introdução à API `canvas`: elemento, contexto gráfico, propriedades e primitivas. Conceitos básicos: coordenadas, dimensões, rectângulos, cores. Texto em `canvas`. Linhas poligonais: caminhos, traçado e preenchimento. Propriedades das linhas: largura, antisserrilhamento, uniões, tracejados.

**Aula 23** (7 dez): Linhas curvas: arcos, curvas quadráticas e de Bézier. Animações com temporização e `frames`. Embeber `canvas` na formatação (CSS, eventos). Transformações: translações, rotações, homotetias, composição, matrizes. Guardar/recuperar o estado do contexto gráfico. Exemplos: relógio e catavento.

## O que NÃO está neste calendário

Esta folha só vai até 14 de dezembro de 2026. Não há (ainda) informação
sobre:
- Período de exames / época normal ou de recurso;
- Datas exatas de apresentação dos trabalhos (ver `TRABALHO_Tab.md`, secção
  "Apresentação" — usam um calendário partilhado à parte, à medida da
  disponibilidade de cada grupo, **na semana seguinte** ao prazo de cada entrega).

Assim que estas informações forem publicadas no site, diz-me para eu voltar
a consultar e atualizar este ficheiro.
