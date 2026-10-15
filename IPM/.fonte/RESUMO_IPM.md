---
title: "Interação Pessoa-Máquina (IPM) --- Resumo Teórico"
author: "Gonçalo Sousa"
date: "Atualizado: Semana 6 (Aulas 1--6, Módulos 01--06, enunciado do projeto COL)"
---

<!-- processado: Teoricas/Aula_01.pdf, Teoricas/Aula_02.pdf, Teoricas/Aula_03.pptx, Teoricas/Aula_04.pdf (tópico Esboçar fundido na Aula 2), Teoricas/Aula_05.pdf (três modelos fundidos na Aula 2, T3), Praticas/Semana_2/Enunciado_Projeto_COL.pdf (projeto, fundido na Aula 1), Praticas/Semana_4/IPM_2627_Handout_04.pdf (S4, tabela semanal da Aula 1), Teoricas/Aula_06.pdf -->

# Aula 1 --- Enquadramento da disciplina e do projeto

## O que é a IPM

**Interação Pessoa-Máquina** (IPM, em inglês *Human-Computer Interaction* —
HCI) estuda como as pessoas usam sistemas interativos e como esses sistemas
devem ser desenhados para que essa interação funcione bem. A disciplina
divide-se em dois grandes blocos:

- **Fundamentos de IPM** (teoria): o processo de desenhar interfaces,
  usabilidade.
- **Implementação de sistemas interativos** (prática): prototipagem,
  tecnologias interativas, aplicação e validação das metodologias
  aprendidas.

Os tópicos principais do semestre são: conceitos do processo de desenho,
modelo do processador humano (perceção, atenção, memória), prototipagem
(de baixa a alta fidelidade, ferramentas), engenharia da usabilidade
(definição do problema, ciclo de desenvolvimento, avaliação), a interação
como algo que gera sentimento (não é só eficiência mecânica) e uma breve
história da IPM.

## Frequência e regras de assiduidade

- **Aulas teóricas**: presenciais, sem controlo de assiduidade (a matéria
  é a base do exame).
- **Aulas práticas (lab)**: presenciais, trabalho em grupo.
  - Assiduidade mínima: **70%** das sessões de lab.
  - Máximo de **3 faltas**.
- **Todo o trabalho de grupo tem de ser completado**: dois relatórios de
  grupo, um protótipo, duas apresentações.

## Avaliação

::: {.definicao title="--- Componentes de avaliação"}
A nota final (FG, *Final Grade*) tem 20 valores, divididos em três
componentes:

| Componente | Nome | Pontos | Tipo |
|---|---|---|---|
| R1 | *First Report* | 4 | Trabalho de grupo |
| PR2 | *Prototype + Second Report* | 6 | Trabalho de grupo |
| FE | *Final Exam* | 10 | Individual (Moodle) |

$$FG = R1 + PR2 + FE$$

com a condição **FE $\geq$ 35%**: pelo menos 3,5 dos 10 valores *no próprio
exame*. É eliminatório por si só: mesmo com R1 e PR2 perfeitos, abaixo
disso não há aprovação.
:::

### R1 --- Primeiro relatório (4 pontos)

Trabalho de grupo baseado no **estudo e desenho** de um sistema capaz de
fazer interação pessoa-máquina. Envolve: investigação (*research*), análise
de requisitos, metodologia de implementação e resultados preliminares de
avaliação. Feito em **grupos de 4**. Não há nota mínima, mas é avaliado de
forma contínua ao longo do trabalho (não só no entregável final). Os
slides falam de uma apresentação intercalar do relatório (data a
confirmar); o calendário do enunciado não a menciona.

**O que o R1 cobre** (ver a sequência completa na Aula 3): da formação do
grupo até à **proposta de modelos conceptuais e decisões de desenho** ---
estudos exploratórios, stakeholders, recolha de dados, personas e estudo da
tecnologia, modelos conceptuais --- **e ainda a 1.ª avaliação** (o
*cognitive walkthrough* sobre os esboços), segundo o enunciado do projeto.

::: {.definicao title="--- R1: entrega e conteúdo obrigatório (enunciado do projeto COL)"}
**Entrega:** domingo **8 de novembro, 23:30**, em PDF, no máximo **30 MB**.
O R1 conta a história do grupo até à Fase 1: o que pensaram, o que
desenharam, como escolheram e o que a primeira avaliação mostrou. **Não é
um relatório de design bonito, é um relatório de decisões justificadas.**
Tem de ter, **por esta ordem**:

1. **O problema por palavras vossas** e os 3 ou 4 maiores desafios de
   interface que identificaram.
2. **Quem opera:** **três personas**, com nome, experiência e o que as põe
   em dificuldade. **Uma tem de ser um operador com pouca experiência.**
3. **As missões** escritas na S4 (**pelo menos cinco**), cada uma com
   objetivo, situação de partida e o que tem de estar feito no fim. Têm de
   cobrir situações **normais**, de **cheia** e **pelo menos uma avaria**
   de equipamento.
4. **A divisão da interface em painéis**, com a distribuição pelos **2
   monitores e pela parede de ecrãs** justificada.
5. **Os esboços:** todas as alternativas da S3 (fotografadas com bom
   contraste), os **critérios** usados para as comparar (ex.: quanto ajuda
   a cumprir as missões, quanto ruído acrescenta, quão nova é a
   abordagem), as **escalas**, os **votos de cada membro** e os
   resultados. As conclusões da votação escritas e as **iterações** feitas
   a partir delas.
6. **A lista de funcionalidades com prioridade (MoSCoW)** e os **dois
   *storyboards***.
7. **O *cognitive walkthrough* (Fase 1):** quem vos avaliou, a grelha
   preenchida, os problemas encontrados e o que decidiram mudar por causa
   deles.
8. **O "ouro" do grupo**, tal como está nesse momento (mesmo que ainda seja
   só uma ideia a começar).
:::

### PR2 --- Protótipo + Segundo relatório (6 pontos)

Trabalho baseado numa **implementação de protótipo**, associado ao trabalho
anterior (R1). Envolve: materiais e ferramentas de prototipagem rápida, uso
de software (**Figma**, usado a partir da S7), e detalhes de implementação
decididos caso a caso com o professor. É feito **pelo mesmo grupo** do R1.
Também sem nota mínima, mas avaliado continuamente. Há uma apresentação
final do protótipo desenvolvido + segundo relatório.

**O que o PR2 cobre**: do **protótipo** em diante --- protótipo, avaliação
de usabilidade e relatório final. O relatório final é uma "pasta enorme"
com **todo** o trabalho de cada etapa (esboços, diagramas e gráficos,
texto, cor). Regra desta disciplina: juntar a **evidência de cada fase** e,
para cada avaliação, o **antes/depois** do artefacto com a **razão da
mudança** (o que a avaliação mostrou e o que se alterou por causa disso).

::: {.definicao title="--- PR2: entrega e conteúdo obrigatório (enunciado do projeto COL)"}
**Entrega:** domingo **13 de dezembro, 23:30**: o relatório em PDF (no
máximo **50 MB**), o **link do protótipo Figma** (com permissão de
visualização para os docentes) e a **evidência das três fases** numa pasta
ou anexo. Continua a história do R1 e acaba na interface final. Tem de ter:

1. Um **resumo do R1 em meia página**, a destacar o que mudou entretanto.
2. Os ***wireframes*** e a passagem para o **protótipo Figma**, de
   fidelidade **média a alta**, que permita cumprir **todas as missões do
   grupo com cliques reais**.
3. A **avaliação heurística (Fase 2):** lista de problemas com
   severidade, quem os encontrou e o que mudaram por causa deles.
4. Os **testes de usabilidade (Fase 3):** o protocolo (o que pediram, a
   quem, como mediram), os resultados na aula e com as **5 pessoas de
   fora**, e o que mudaram por causa deles.
5. A **interface final:** descrição de cada painel, dos estados e de como
   o operador interage, com imagens legíveis.
6. O **"ouro" do grupo, defendido com os resultados das avaliações**.
7. **Balanço:** o que ficou por fazer e o que fariam de outra maneira.
:::

::: {.definicao title="--- Apresentação final e peso do projeto"}
**15 de dezembro**, na aula (P1 e P2 das 9:00 às 11:00; P3 das 11:00 às
13:00). Cada grupo mostra o protótipo a funcionar, a cumprir **pelo menos
três missões ao vivo**, e tem de mostrar **o caminho, não só o
resultado**: que alternativas criaram, como as avaliaram e como o
protótipo mudou por causa das avaliações. O tempo por grupo é anunciado na
S9.

A nota do projeto conta o R1, o PR2 com o protótipo, a **participação nas
três fases de avaliação** (provada pela evidência) e a apresentação final.
**Um grupo que falte a uma fase de avaliação sem justificação perde essa
componente.** Há ainda um relatório de estado de cada grupo, por email aos
docentes, a **4 de dezembro**.
:::

### Exame final (10 pontos)

- Feito no **Moodle**, individual.
- Perguntas de escolha múltipla, perguntas de associação, perguntas de
  arrastar e largar (*drag and drop*).
- Duração aproximada: 70 a 90 minutos.
- Mínimo: **35%** da nota do exame (ver caixa de exame acima).

## O projeto deste ano: Centro de Operações do Lima (COL)

Há **um projeto para toda a turma**: todos os grupos desenham a **mesma**
interface --- a interface gráfica da **sala de operações de um troço de rio
com duas barragens**. O que distingue os grupos é a **qualidade das
decisões**, a forma como as **justificam** e o **"ouro"** de cada grupo (o
seu diferencial, ver abaixo). O enunciado completo está em
`Praticas/Semana_2/Enunciado_Projeto_COL.pdf`; esta secção resume-o por
inteiro, para não teres de voltar a ele.

### O problema

O **rio Lima** nasce na Galiza e entra em Portugal em Ponte da Barca; daí
até ao mar, em Viana do Castelo, corre cerca de 60 km. Nesse troço há **duas
barragens**. A água retida atrás de cada barragem forma um lago artificial,
a **albufeira**; a barragem tem aberturas que se abrem e fecham, e a água só
passa quando alguém decide abrir as **comportas**.

- **Alto Lindoso** (a montante) é o maior produtor de eletricidade de
  origem hídrica do país. A água desce por dentro da montanha e faz girar as
  turbinas: a isto chama-se **turbinar**. Não turbina continuamente: produz
  quando a rede elétrica precisa (ex.: ao fim da tarde) e para quando não
  precisa. Resultado: o Lima recebe, uns quilómetros abaixo, **grandes
  golfadas de água durante algumas horas e quase nada no resto do dia**.
- **Touvedo**, 12 km abaixo, existe precisamente para resolver isso: é muito
  mais pequena, recebe as golfadas do Lindoso e devolve-as ao rio **de forma
  regular, sem picos**. Mas a albufeira de Touvedo é pequena: quando chove
  muito, os afluentes e a própria chuva enchem-na depressa, e Touvedo deixa
  de conseguir reter o que recebe. Tem então de **largar água**: abrir as
  comportas (grandes portas de aço no topo) e deixar passar para o rio
  parte do que chega.

O **caudal** (a quantidade de água que passa num ponto por unidade de tempo)
mede-se em **m³/s**. 1 m³ = 1000 litros: "Touvedo está a largar 500 m³/s"
são 500 000 litros por segundo, ou uma piscina olímpica a cada 5 segundos.
Com tempo seco, o Lima leva bem menos de 100 m³/s em Ponte de Lima.

Há ainda **dois fatores que ninguém controla**:

- **Os afluentes** (rios mais pequenos que desaguam no Lima): o **Vez**, o
  **Vade** e o **Estorãos**. Não têm barragens, por isso quando chove trazem
  água para o Lima e não há forma de a reter.
- **A maré.** Perto do mar, o nível do rio sobe e desce duas vezes por dia,
  e isso chega até Ponte de Lima. Na **preia-mar** (o ponto mais alto da
  maré) o rio escoa mais devagar e a água que vem de montante acumula-se.

![O troço do Lima que o COL controla (figura 1 do enunciado): duas barragens, três afluentes sem controlo, três localidades e a maré](figuras/col_rio_lima.png){width=100%}

::: {.exemplo title="--- O que aconteceu a 2 de fevereiro de 2026 (o caso que motiva o projeto)"}
Depois de vários dias de chuva forte, Touvedo largava cerca de **500 m³/s**
às 10h. O Vez e o Vade estavam cheios. A **preia-mar** em Ponte de Lima foi
às **15h**. O rio cobriu o **areal** de Ponte de Lima, chegou ao muro do
**Passeio 25 de Abril**, entrou no **Clube Náutico** e, em Ponte da Barca,
galgou as margens no **Choupal** (parque ribeirinho). Não houve vítimas,
mas houve muitos estragos.

Repara que o problema é a **soma** de três coisas, só uma delas
controlável: a descarga de Touvedo (controlável), os afluentes cheios (não
controláveis) e a maré alta (não controlável, mas **previsível** pela tabela
de marés). É isto que a interface tem de ajudar o operador a ver **em
conjunto**.
:::

Hoje estas funções estão **espalhadas**: as descargas são decididas pela
**EDP** (dona das barragens); avisar as pessoas é tarefa da **APA**
(agência pública que gere os rios) e da **Proteção Civil**; responder no
terreno é tarefa dos **bombeiros** dos dois municípios. Estão em sítios
diferentes e falam por telefone. **A vossa tarefa é desenhar a interface
gráfica de uma única sala de operações para este troço de rio, o Centro de
Operações do Lima (COL)**, que junta as três funções num só sítio:
**decidir o que as barragens fazem**, **avisar quem está em risco** e
**coordenar as equipas no terreno**. O COL é fictício e os dados são
inventados, mas as barragens, as localidades, os afluentes e a maré são
reais.

### Quem usa a interface: o operador (e o coordenador)

O COL tem **três operadores**, um por turno de **8 horas**, e um
**coordenador** que **não está na sala** mas pode ser contactado a qualquer
hora. De **outubro a abril** (época das chuvas) a sala funciona **24 horas
por dia**; fora disso, só de dia. **A interface é desenhada para o
operador**; o coordenador só aparece como **quem autoriza** certas
decisões.

::: {.definicao title="--- O que o operador pode fazer sozinho e o que precisa de autorização"}
**O operador decide sozinho:**

- **Reconhecer um alerta** (marcar que o viu e que passa a ser
  responsável por ele).
- **Alterar o caudal turbinado** (mais ou menos água pelas turbinas ---
  muda a eletricidade produzida **e** o caudal largado para o rio).
- **Abrir ou fechar a descarga de fundo** (conduta com válvula junto à base
  da barragem, que larga água sem passar pelas turbinas nem pelas
  comportas).
- **Mover as comportas de Touvedo**, desde que o total largado pela
  barragem fique **abaixo de 300 m³/s**.
- **Pedir análises de água** a uma estação e **enviar equipas** a um local.

**Precisa de autorização do coordenador** (pedida e recebida **na
interface**):

- **Descargas acima de 300 m³/s.**
- **Avisos à população.**
- **Fechar pontes, parques ou o Passeio 25 de Abril.**

**Cada turno acaba com uma passagem de turno registada**: um resumo, gravado
na interface, do que aconteceu no turno e do que ficou pendente, que o
operador seguinte lê antes de assumir a sala.
:::

### O sistema que existe no terreno

Tudo o que está nesta secção é **dado**: não se podem acrescentar nem
retirar barragens, sensores ou equipas. Os números das barragens são reais.

::: {.definicao title="--- As duas barragens"}
| | **Alto Lindoso** (1992) | **Touvedo** (1993) |
|:------------|:------------------|:------------------|
| Tipo | **Abóbada** (parede curva que se apoia na rocha dos dois lados do vale) | **Gravidade** (segura a água pelo próprio peso) |
| Altura | 110 m | 42,5 m |
| Albufeira | 379 hm³ (entra pela Galiza) | 15,5 hm³, dos quais **só 4,5 hm³ úteis** |
| Comportas de segmento | **6** (2760 m³/s com todas abertas) | **3** (3200 m³/s com todas abertas) |
| Descarga de fundo | 400 m³/s | 50 m³/s |
| Grupos geradores | **2** (Francis), 630 MW no total, em central subterrânea | **1** (Kaplan), 22 MW, em central ao lado da barragem |

**1 hm³** (hectómetro cúbico) = 1 milhão de m³ = mil milhões de litros.
**Volume útil** é a parte da albufeira que o operador pode armazenar ou
largar; o resto fica sempre abaixo das aberturas. As **comportas de
segmento** são portas de aço curvas no topo da barragem que rodam para
cima para deixar passar a água; o conjunto delas é o **descarregador de
cheias**. Um **grupo gerador** (o "grupo", na linguagem das barragens) é
uma turbina mais o gerador que ela faz girar. O tipo de turbina (Francis
para grandes quedas, Kaplan em Touvedo) **não importa para a interface**:
importa que cada grupo pode estar parado, a arrancar, a produzir N MW, a
parar, ou indisponível. **Touvedo recebe tudo o que o Lindoso turbina.**
:::

![Esboço 1 do enunciado: Alto Lindoso em corte (comportas, descarga de fundo, grupos)](figuras/col_barragem_lindoso.png){width=88%}

*Esboço 1 do enunciado: Alto Lindoso em corte --- 6 comportas no topo, descarga de fundo de 400 m³/s, 2 grupos numa central subterrânea.*

![Esboço 2 do enunciado: Touvedo em corte (a linha a ponteado marca o limite do volume útil)](figuras/col_barragem_touvedo.png){width=88%}

*Esboço 2 do enunciado: Touvedo em corte --- 3 comportas, descarga de fundo de 50 m³/s, 1 grupo; abaixo da linha a ponteado a água já não pode ser largada (é a fronteira do volume útil).*

::: {.definicao title="--- Rios, sensores, previsões e recursos"}
- **Afluentes sem controlo:** Vez (entra perto de Ponte da Barca, vem de
  Arcos de Valdevez), Vade (vem de Vila Verde) e Estorãos (entra pouco antes
  de Ponte de Lima). Cada um tem uma **estação hidrométrica**: um posto na
  margem que mede a **altura da água** (o **nível**, em metros) e, a partir
  dela, **estima o caudal** em m³/s.
- **No Lima:** **8 estações hidrométricas** (nível e caudal) e **6 estações
  de qualidade da água**, do Lindoso à foz. As de qualidade medem **pH**
  (ácida ou alcalina), **oxigénio dissolvido** (de que os peixes precisam),
  **condutividade** (sobe com sais ou poluição) e **turbidez** (quão turva
  está a água).
- **Maré e tempo:** um **marégrafo** em Viana do Castelo (mede a altura da
  maré a cada instante), a **tabela de marés** dos dias seguintes e a
  **previsão de chuva a 72 h** do IPMA.
- **8 câmaras de vídeo** em direto: nas duas barragens, no Choupal, no areal
  e no Passeio 25 de Abril, na ponte medieval de Ponte de Lima, na foz e
  numa estrada ribeirinha.
- **3 pontos de descarga de ETAR** (estação de tratamento de águas
  residuais), em Ponte da Barca, Ponte de Lima e Viana do Castelo. Importam
  porque, se o tratamento falhar, a qualidade da água **a jusante** (rio
  abaixo) piora.
- **Recursos:** **4 equipas de terreno** (2 das barragens, 2 da Proteção
  Civil), **2 viaturas**, **sirenes** a jusante das barragens, **SMS** às
  juntas de freguesia e à população, e **3 fechos possíveis**: (i) o
  Passeio 25 de Abril, (ii) os parques do Choupal e do Campo da Feira,
  (iii) as estradas municipais junto ao Estorãos.
- **Cotas de referência:** uma **cota** é a altura da água medida a partir
  de uma referência fixa. Para cada sítio sensível (**areal**, **Passeio 25
  de Abril**, **Choupal**) há a cota a partir da qual a água o começa a
  invadir; cada barragem tem a sua **cota de segurança** (o máximo que a
  albufeira pode atingir). Isto permite à interface mostrar, a cada
  momento, **a que distância a água está de cada limite**.
:::

### Os estados que a interface tem de mostrar e deixar mudar

Cada elemento do sistema está, a cada momento, num **estado**. A interface
tem de mostrar **sempre** o estado atual de cada elemento, de forma fácil
de perceber, e deixar mudá-lo quando isso é permitido. Estes estados são
**obrigatórios**; podem acrescentar-se outros, se justificados.

::: {.definicao title="--- Estados obrigatórios"}
| Elemento | Estados |
|:-----------|:-----------------------------------|
| Comporta de segmento | fechada, a abrir, aberta a N metros, a fechar, bloqueada, em manutenção, **em modo manual local** |
| Descarga de fundo | fechada, a abrir, aberta, avariada |
| Grupo gerador | parado, a arrancar, em carga (a produzir N MW), a parar, indisponível |
| Troço de rio | normal, vigilância, alerta amarelo, alerta laranja, alerta vermelho, emergência |
| Manobra (qualquer ação sobre comportas, descarga de fundo ou grupos) | pedida, à espera de autorização, autorizada, em curso, concluída, cancelada |
| Alerta | novo, reconhecido, atribuído, em tratamento, escalado, resolvido, falso positivo |
| Aviso público | rascunho, pendente, emitido, atualizado, cancelado |
| Equipa de terreno | disponível, atribuída, a caminho, no local, a regressar |
| Ponte, parque ou passeio | aberto, condicionado, fechado |
| Sensor | ok, suspeito, avariado, em calibração |

**Modo manual local** quer dizer que alguém na barragem assumiu o controlo
no local e o **controlo remoto deixa de estar disponível**.
:::

O enunciado dá só a lista de estados, não as transições. Como exemplo de
leitura, o ciclo de vida de uma **manobra** combina a lista de estados com
a tabela de autorizações acima:

![Ciclo de vida de uma manobra (interpretação: o enunciado dá os estados, não as setas)](figuras/col_estados_manobra.pdf){width=92%}

**As setas do diagrama† não estão escritas no enunciado**; esta é a
leitura mais natural. Uma manobra dentro da autonomia do operador salta "à
espera de autorização"; uma que exige o coordenador passa por lá. Desenhar
isto para **cada** elemento ajuda muito: cada seta é um botão ou evento que
a interface tem de ter, cada estado é algo que tem de ser **visível**, e
tudo é matéria-prima direta para as missões.

### O que **não** é pedido

- **Calcular a hidráulica real.** Não é preciso saber quanto sobe o rio se
  Touvedo largar mais 100 m³/s: basta que os números inventados sejam
  **plausíveis** face aos valores da secção anterior.
- **Desenhar a app do cidadão.** O COL avisa a população, mas a app que a
  população usaria é outro projeto.
- **Desenhar o SCADA** (o sistema industrial interno da EDP que manda
  comandos aos motores das comportas e lê os sensores), nem a rede
  elétrica. O COL fala com esse sistema, mas o que se desenha é **o que o
  operador vê e usa**.

### A sala, os ecrãs e as regras de um sistema crítico

O operador trabalha **sentado**, com **teclado e rato**. À frente tem **2
monitores de 27" UHD** e, mais longe, uma **parede de 12 ecrãs (4 × 3)**
para ser vista à distância. A interface tem de usar **os três espaços** e
dizer o que vai em cada um.

::: {.definicao title="--- As quatro regras da sala"}
1. **É um sistema crítico:** a informação de que o operador precisa para
   decidir tem de estar **sempre visível**, sem abrir menus e **sem fazer
   scroll**.
2. **Não há menus escondidos:** tudo o que se pode fazer está à vista ou
   **a um gesto de distância**.
3. **Um comando que muda o estado do rio** (largar água, emitir um aviso,
   fechar uma ponte) tem de ser **difícil de acionar por engano** e **fácil
   de confirmar**.
4. **O operador às 3 da manhã, seis horas dentro do turno, tem de perceber
   a situação num relance.**
:::

**Ligação com a teoria†:** a regra 4 é, na prática, uma **persona** (Aula
2): um operador cansado, de madrugada, com atenção reduzida. A regra 3 é o
compromisso clássico entre **evitar erros** e **não tornar a ação lenta**:
um "tem a certeza?" genérico, que o operador aprende a clicar sem ler,
**não** a cumpre. A confirmação tem de mostrar **o que vai acontecer**
(ex.: "Touvedo passa de 280 para 420 m³/s --- precisa de autorização").

### O "ouro" do grupo

Como todos os grupos trabalham no mesmo problema, cada grupo tem de ter
**algo que os outros não têm**: uma ideia, uma forma de mostrar ou de
interagir que resolva **bem** um ponto difícil. Não tem de ser grande; tem
de ser **vosso** e tem de ser **defendido com resultados das avaliações**.
Exemplo dado no enunciado, só para dar a ideia: **como mostrar, em tempo
real, quanto espaço ainda resta em Touvedo**.

### Três fases, três avaliações --- o calendário

O protótipo é avaliado **três vezes** ao longo do semestre, sempre na aula
e sempre por membros de **outros grupos**. As três fases **contam para a
nota**. O que se regista em cada fase chama-se **evidência** (grelhas
preenchidas, fotos dos esboços, notas dos avaliadores, resultados dos
testes) e é entregue com o PR2.

::: {.definicao title="--- As três fases do projeto"}
| Fase | Quando | Artefacto (fidelidade) | Avaliação |
|:-:|:-----|:-----------|:-----------|
| 1 | S6, semana de **3 nov** | Esboços (*sketches*), baixa | *Cognitive walkthrough* |
| 2 | S8, semana de **17 nov** | *Wireframes* no Figma, média | Avaliação heurística |
| 3 | S9, semana de **24 nov** | Protótipo interativo, média a alta | Testes de usabilidade (na aula + **5 pessoas de fora**, como TPC) |

Depois de cada fase: outros grupos avaliam o artefacto → escrevem
conclusões → o grupo melhora o artefacto com base nisso.
:::

As três fases são todas em **novembro** (3, 17 e 24; vale o enunciado,
que é mais recente do que os slides). Dezembro fica para acabar o
protótipo, o PR2 (13 dez) e a apresentação (15 dez).

::: {.definicao title="--- O trabalho semana a semana (aulas práticas)"}
| Semana | Sessão | O que se faz na aula | O que fica feito |
|:--|:-:|:--------------------|:------------|
| 22 set | S1 | Aquecimento: exercícios curtos sobre interfaces e sobre como observar quem as usa | Grupos formados |
| 29 set | S2 | Leitura guiada do enunciado; discussão do problema e de quem é o operador; perguntas | Todos percebem o problema e o sistema |
| 6 out | S3 | Cada membro escolhe **um assunto** do sistema e faz **esboços** de como o mostraria e controlaria num ecrã | Um painel por membro, em esboço; **muitas alternativas, nenhuma escolhida** |
| 13 out | S4 | (Handout 04) Três esboços novos por membro a partir das 3 ideias da S3; pontuá-los com as heurísticas do grupo (ninguém pontua os seus) e ficar com as 3 melhores; cada membro **refina** uma (etiquetas, unidades, valores de exemplo, estados de cada comando); post-its por elemento, agrupados por função, dão os **primeiros painéis** | Esboços refinados; painéis, cada um com **zona de informação** (o que se lê) e **zona de ação** (o que se opera) |
| 20 out | S5 | Consolidação: escolher, **com critérios escritos**, entre as alternativas de cada painel e ligar os painéis num todo; **storyboards** de duas missões | Conjunto coerente de esboços + 2 storyboards |
| 3 nov | S6 | **Fase 1:** cada grupo percorre uma missão, passo a passo, nos esboços de outro grupo e regista onde um operador novo se enganaria | Grelha do walkthrough (evidência); lista de correções |
| 10 nov | S7 | Básico de **Figma**; início dos **wireframes** (os esboços corrigidos passam a ecrãs desenhados com precisão, nos 2 monitores e na parede) | Primeiros wireframes no Figma |
| 17 nov | S8 | **Fase 2:** cada grupo examina os wireframes de outro contra uma lista de princípios e classifica a **severidade** de cada problema | Problemas com severidade (evidência); plano de correção |
| 24 nov | S9 | **Fase 3:** membros de outro grupo tentam cumprir missões no protótipo, **sem ajuda**, medindo tempo e erros; TPC: repetir com 5 pessoas de fora | Protocolo e resultados (evidência) |
| 15 dez | | Apresentações finais | |

As turmas de terça (P1, P2) e de sexta (P3) fazem o mesmo na mesma semana.
As sextas de **30 out, 4 dez e 11 dez** são sobretudo sessões de apoio.
**Não há aulas a 27 out, 1 dez e 8 dez.**
:::

::: {.definicao title="--- Vocabulário das fases (pela ordem em que aparece)"}
- **Esboço** (*sketch*): desenho rápido a lápis, sem preocupação de
  precisão, para explorar ideias.
- **Painel:** uma área do ecrã, ou um monitor inteiro, dedicada a um
  assunto.
- **Missão:** uma tarefa **completa, do início ao fim**, que o operador tem
  de conseguir cumprir. Cada grupo escreve as suas na S4; têm de cobrir
  situações **normais**, de **cheia** e **pelo menos uma avaria**. (É o
  *task flow* da Aula 2, T4.)
- **MoSCoW:** método para priorizar funcionalidades, dividindo-as em
  **M**ust (tem de existir), **S**hould (devia existir), **C**ould (pode
  existir) e **W**on't (fica de fora, por agora). (As letras "o" só estão
  lá para se ler como uma palavra.)
- ***Storyboard*:** sequência de quadros, como uma banda desenhada, a
  mostrar o operador a cumprir uma missão na interface.
- ***Cognitive walkthrough*:** avaliação em que se segue uma missão passo a
  passo, perguntando em cada passo se **um operador novo** saberia o que
  fazer.
- ***Wireframe*:** desenho **preciso** de um ecrã, com a posição e o tamanho
  de cada elemento, ainda **sem cores, sem acabamento gráfico e sem
  comportamento**.
- **Avaliação heurística:** exame de uma interface contra uma lista de
  princípios de boas interfaces (as **heurísticas**), com uma **severidade**
  para cada problema encontrado.
- **Teste de usabilidade:** observar pessoas reais a tentar cumprir missões
  no protótipo, **sem ajuda**, medindo tempo, erros e o que dizem.
:::

**Os três métodos de avaliação†** (só nomeados no Módulo 02, T4; são
explicados em detalhe mais tarde):

- **Cognitive walkthrough** (Fase 1): não precisa de utilizadores reais nem
  de protótipo funcional, só do esboço e do percurso mental do avaliador;
  nos slides da Aula 1 cada passo da missão é pontuado (0 / 1 / 2). A
  Aula 6 dá a grelha completa: sim/não a cada uma de quatro perguntas por
  passo e uma severidade de 0 a 4 por problema (interpretação: o 0/1/2 é
  um resumo do passo; para a Fase 1 vale a grelha da Aula 6).
- **Avaliação heurística** (Fase 2): normalmente as **heurísticas de
  Nielsen**, mais heurísticas próprias do grupo; para cada problema
  regista-se a **severidade** e a **extensão** (quantas partes do sistema
  afeta).
- **Testes de usabilidade** (Fase 3): regista-se sucesso/insucesso, tempo,
  erros e frases ditas (*quotes*) durante a tarefa.

Cada método precisa de um artefacto mais acabado do que o anterior (esboço
→ wireframe → protótipo interativo), o que explica a ordem das fases.

**Dúvidas que o enunciado não resolve† (levar à aula):**

1. A **descarga de fundo do Lindoso** larga até **400 m³/s**. O operador
   pode abri-la ou fechá-la sozinho, mas "descargas acima de 300 m³/s"
   precisam de autorização. Abri-la toda precisa? (Leitura mais segura:
   sim, porque o total passa os 300.)
2. O limite de 300 m³/s de Touvedo conta **tudo** o que a barragem larga
   (turbina + descarga de fundo + comportas) ou só as comportas? "O total
   largado pela barragem" aponta para tudo.
3. As **sirenes** contam como "aviso à população" (e precisam de
   autorização)? Estão na lista de recursos, ao lado das SMS.
4. Como aparece o coordenador quando **não responde** a um pedido de
   autorização urgente? O enunciado só diz que "pode ser contactado a
   qualquer hora".

::: {.pratica title="--- Perceber o enunciado do COL"}
**Exercício P.1** (inventado, a partir do enunciado). Para cada situação,
diz o que a interface deve deixar fazer e porquê.

**(a)** Touvedo está a largar 180 m³/s no total. O operador quer abrir uma
comporta para largar mais 100 m³/s. Pode fazê-lo sozinho?

**(b)** A mesma situação, mas agora quer largar mais 150 m³/s. Por que
estados passa a manobra? (Usa o diagrama do ciclo de vida.)

**(c)** Chove muito e o operador quer tocar as sirenes a jusante de
Touvedo. Pode fazê-lo sozinho? (Pista: vê as dúvidas acima.)

**(d)** A comporta 2 de Touvedo está "em modo manual local" e o operador
precisa de a fechar. O que deve a interface mostrar e deixar fazer?

**(e)** O volume útil de Touvedo está a meio e está a entrar mais água do
que a sair: a diferença é de 250 m³/s. Quanto tempo falta até o volume útil
encher? (É a conta por trás do exemplo de "ouro" do enunciado.)
:::

## Como os grupos funcionam

- **Grupos de 4**, mantidos durante todo o semestre (para R1 e PR2).
- **Liderança rotativa**: um líder de equipa diferente em cada sessão. No
  fim da sessão, o líder aponta o que o grupo devia mudar para trabalhar
  melhor (uma espécie de retrospetiva curta).
- **Um painel por membro**: cada elemento do grupo é dono de um painel (uma
  parte) do sistema, responde por ele e apresenta-o.
- **Escolher sozinho, depois discutir**: as escolhas individuais são feitas
  *antes* da discussão em grupo (por exemplo, que funcionalidades cada um
  esboça primeiro) — evita que a opinião mais forte do grupo domine logo de
  início.
- **Evidência em cada aula**: fotos dos esboços, votos, matrizes e decisões
  são guardados no fim de cada sessão (no Moodle).
- **Avaliação entre grupos**: usa missões (escritas como *task flows*, ver
  T4 na Aula 2), matrizes avaliador-por-objeto (grelhas de avaliação, ver
  T3 na Aula 2), pontuações independentes e conclusões escritas. Os
  avaliadores conhecem o domínio do problema (não são utilizadores
  totalmente ingénuos).

::: {.definicao title="--- Como criar a equipa (primeira etapa do procedimento)"}
- **Não perder tempo** --- formar o grupo cedo.
- **Acrescentar valor** à equipa com **pessoas diferentes** (perfis,
  competências e pontos de vista distintos, não quatro cópias da mesma
  pessoa).
- Garantir que **todos estão motivados**.
- Garantir **pelo menos dois canais de comunicação** entre todos: um
  **ponto-a-ponto** (falar com um colega) e um de **difusão** (*broadcast*,
  falar com o grupo inteiro).
- Criar formas **ágeis** de fazer reuniões de equipa úteis (curtas, com
  objetivo).
- **Distribuir tarefas de forma sistemática** (não "quem se oferecer").
- **Informar o grupo das descobertas individuais antes de cada marco**
  (*milestone*) --- ninguém chega a uma entrega sem os outros saberem o que
  encontrou.
:::

## Uso de Inteligência Artificial generativa na disciplina

::: {.definicao title="--- Regras sobre IA generativa"}
**Permitido** (como apoio instrumental):

- Reformular e rever os teus próprios textos.
- Explorar vocabulário e alternativas *depois* de teres a tua própria ideia.
- Pequenos trechos de código (*snippets*) e ajuda com as ferramentas de
  prototipagem.
- Resumir referências que já leste.

**Não permitido** (como substituto do teu próprio raciocínio):

- Gerar os esboços ou os conceitos de design.
- Usar imagens geradas por IA **como fonte de ideias**. (Módulo 04: são
  opcionais e só servem para **ilustrar um conceito que o grupo já
  escolheu**; o porquê está na Aula 2, "Um esboço vs. uma maqueta gerada
  por IA".)
- Tomar as decisões de design pelo grupo.
- Escrever as avaliações ou as conclusões.
- Produzir "evidência" que o grupo não criou de facto.

**O que conta** (só o que é teu):

- O que percebeste, o que consegues explicar.
- O que validaste com utilizadores ou avaliadores.
- Cada decisão tem de poder ser defendida pelo grupo, se pedido.
- **O exame também avalia sobre o trabalho de grupo** — ou seja, não basta
  ter um bom relatório; é preciso perceber o que lá está escrito.
:::

## Material a trazer para as aulas

Caderno de esboços (A5 ou A4), caneta ou lápis, borracha, papel para notas,
uma conta **Figma** (plano gratuito de educação — usada para *wireframes*
e o protótipo interativo), e acesso ao **Moodle** (onde se sobe a evidência
do grupo: fotos, matrizes, decisões).

## Prototipagem: um primeiro exemplo (máquina de café tipo Nespresso)

::: exemplo
O professor usa como primeiro exemplo de prototipagem/interface uma
máquina de venda automática de café "ao estilo Nespresso": por fora, o
utilizador só vê um ecrã tátil (ou botões) com fotos de bebidas e opções
de personalização — uma interface simples e amigável. Por dentro, a
máquina é um sistema complexo: garrafões de água, tubagens, sistema de
aquecimento, mecanismos de dispensa de cápsulas, etc.

A lição desta comparação é a que vai ser formalizada mais à frente (ver
"Desenho conceptual" na Aula 2, abaixo): o utilizador **nunca vê o
mecanismo real** da máquina — só vê a **imagem do sistema** (o ecrã, os
botões, os sons). O trabalho de quem desenha a interface é garantir que
essa imagem leva o utilizador a construir na cabeça um modelo mental
correto e simples ("carrego neste botão, sai um café"), **independentemente**
da complexidade real por trás.
:::

## TPC (trabalho de casa) da Aula 1

1. Tirar uma **fotografia** de algum sistema de IPM interessante (por bons
   ou maus motivos).
2. **Anotar a foto** com: o teu nome, a data, e uma descrição curta (o que
   é, porque é interessante).
3. **Submeter no Moodle**: formato JPG, menos de 1 MB, antes da próxima
   aula teórica.

Uma foto **sem** as anotações (nome, objeto, data) conta como mau exemplo,
mesmo que o objeto seja interessante: a anotação é parte obrigatória do
exercício.

# Aula 2 --- Como desenhar um sistema de IPM

## Antes de começar a planear

Antes de sequer começar a desenhar o sistema, o grupo tem de resolver três
coisas de organização:

1. **Escolher colegas e formar o grupo** --- são precisas 4 pessoas.
2. **Perceber o papel de cada um e o que se espera** --- os papéis rodam
   (líder de equipa muda a cada sessão, um painel por membro, ver Aula 1).
3. **Discutir a gestão do grupo** --- reuniões, marcos temporais
   (*milestones*), indicadores de progresso, onde se guarda a evidência.

## Visão geral: as quatro tarefas (T1 -- T4)

O processo de desenho de um sistema de IPM organiza-se em quatro tarefas,
sempre pela mesma ordem, com um ciclo de retorno no fim:

![As quatro tarefas do processo de desenho: identificar utilizadores/stakeholders, estudos iniciais, desenho conceptual, avaliação — e voltar ao desenho conceptual com o que a avaliação ensinou](figuras/ciclo_tarefas.pdf){width=95%}

*Quatro tarefas, por esta ordem, e depois de volta a T3 com o que T4
ensinou.*

::: {.definicao title="--- T1 a T4"}
- **T1**: identificar as personas e os stakeholders para o problema.
- **T2**: fazer estudos iniciais (investigação sobre o tema).
- **T3**: fazer o desenho conceptual.
- **T4**: avaliar o que foi feito --- e o resultado dessa avaliação
  realimenta T3, não recomeça o processo do zero em T1.
:::

## T1 --- Identificar utilizadores e stakeholders

::: {.definicao title="--- Stakeholder"}
Um **stakeholder** é qualquer pessoa (ou entidade) que **tem interesse** no
sistema, não só quem o vai usar diretamente.
:::

Ao identificar stakeholders, o grupo deve pensar em:

- Quem vai **usar** o sistema? (as *personas* --- ver secção própria abaixo)
- Quem vai **construir** o sistema?
- Quem vai **vender** o sistema?
- Mais alguém que possa ter interesse nisto (reguladores, vizinhos,
  manutenção, etc.)?

**Como fazer isto na prática**: fazer *brainstorming* dentro do grupo,
discutir com amigos e colegas, e escrever tudo numa lista. Exemplos de
categorias de stakeholder dados nos slides: utilizadores, construtores,
vendedores, responsáveis pela manutenção, reguladores, vizinhos.

**Para que servem os stakeholders.** Falar com eles permite:

1. perceber melhor o **contexto**;
2. perceber melhor os **problemas**;
3. estabelecer **prioridades** na resolução do problema.

Em cada uma destas três coisas há *feedback* a aproveitar. Por isso a
atitude pedida é **pró-ativa**: estudar o assunto, usar a Internet e
**perguntar às pessoas**, em vez de esperar que a informação chegue.

### Desenho centrado no utilizador (*User-Centred Design*)

Os utilizadores finais têm necessidades e expectativas — muitas vezes nem
sequer conscientes para eles próprios. A experiência que têm com o produto
é o que acaba por determinar o sucesso real do produto. Por isso, **o
utilizador tem de estar no centro do processo de desenho**: é isto que se
chama **User-Centred Design**. Uma ferramenta central para isto é criar
**personas** que descrevam, de forma objetiva, as possibilidades de
utilizador que existem (ver secção "Personas" abaixo).

### T1.1 --- Investigação sobre utilizadores (*user research*)

Ao investigar os utilizadores, o foco deve estar em cinco coisas:
utilizadores potenciais, as suas características, as tarefas que precisam
ou querem realizar, o contexto em que operam, e as suas expectativas.

De onde vêm as respostas a estas perguntas: **entrevistas e observação**
(secções seguintes), questionários curtos, dados já existentes, e os
próprios stakeholders já listados em T1.

**Escreve sempre as palavras exatas dos utilizadores.** Esse vocabulário
*é* o material com que se constrói o modelo conceptual (T3); não o
parafraseies logo para linguagem técnica.

### Como os utilizadores se definem e diferem entre si

Um utilizador caracteriza-se por três eixos:

::: {.definicao title="--- Três eixos de caracterização do utilizador"}
1. **O que sabem sobre as tarefas**: se a tarefa já era conhecida,
   recentemente introduzida, ou completamente nova para eles; como a
   compreenderam; o seu nível de perícia.
2. **O que sabem sobre as ferramentas**: o que usam atualmente, e como o
   usam.
3. **Que modelos mentais têm**: como interpretam o sistema internamente, e
   que vocabulário associam aos elementos e às tarefas — isto **é** o
   modelo conceptual do utilizador.
:::

Dentro da mesma população de utilizadores há sempre diferenças
individuais, que podem criar subgrupos:

- **Traços pessoais**: por exemplo, métodos de aprendizagem ou de trabalho
  diferentes.
- **Diferenças físicas**: acuidade visual, audição, incapacidades,
  características ligadas à idade.
- **Diferenças culturais**: línguas que se leem da esquerda para a direita
  vs. da direita para a esquerda, expressões, símbolos, diferenças
  relacionadas com a idade (ex: adolescente vs. adulto).
- **Motivação e atitude**: entusiasmo por coisas novas vs. resistência à
  mudança.

### Níveis de perícia do utilizador

::: {.definicao title="--- Os quatro níveis de perícia"}
- **Principiante** (*beginner*): não sabe inicialmente o que fazer, tem
  medo de falhar; pode tornar-se "principiante avançado" num período
  relativamente curto.
- **Principiante avançado** (*advanced beginner*): perde o medo, sabe o
  suficiente para executar as tarefas necessárias e foca-se nisso.
  **80% dos utilizadores não passam deste nível** — é o nível para o qual
  se deve otimizar o desenho da interface.
- **Competente**: exposição mais longa cria um modelo mental sólido;
  consegue prever e planear melhor como executar uma tarefa; consegue
  diagnosticar e resolver problemas; reconhece que quer aprender mais para
  fazer melhor.
- **Perito** (*expert*): altamente motivado, usa o produto como parte
  integral da sua atividade, cria os seus próprios processos e mantém-se a
  explorar o sistema. Tipicamente uma fração muito pequena da base de
  utilizadores.
:::

### Métodos para investigar utilizadores

Os métodos de investigação de utilizadores organizam-se tipicamente em
dois eixos: um eixo **qualitativo (direto)** vs. **quantitativo
(indireto)**, e um eixo **comportamental** (o que as pessoas fazem) vs.
**atitudinal** (o que as pessoas dizem).

Cada lado do eixo† responde a perguntas diferentes: o **qualitativo** a
"porquê" e "como resolver", o **quantitativo** a "quantos" e "quanto". É
isso que decide o método, consoante a pergunta de investigação.

Exemplos de métodos, agrupados pelo tipo de resposta que dão:

| Método | Tipo | O que mede |
|---|---|---|
| Entrevistas | Qualitativo, atitudinal | O que as pessoas dizem, em profundidade |
| Grupos de foco (*focus groups*) | Qualitativo, atitudinal | Opiniões partilhadas em grupo |
| Estudos de diário (*diary studies*) | Qualitativo, atitudinal | Comportamento ao longo do tempo, relatado pelo próprio |
| *Card sorting* / *tree testing* | Qualitativo/quantitativo, atitudinal | Como as pessoas organizam/categorizam informação |
| Testes de conceito | Qualitativo, atitudinal | Reação a uma ideia ainda não construída |
| Inquéritos (*surveys*) | Quantitativo, atitudinal | Opiniões, em escala |
| Inquérito contextual (*contextual inquiry*) | Qualitativo, comportamental | Comportamento real, no contexto real de uso |
| Estudos de campo (*field studies*) | Qualitativo, comportamental | Comportamento real, no ambiente natural |
| Testes de usabilidade | Qualitativo/quantitativo, comportamental | O que as pessoas conseguem (ou não) fazer com o produto |
| Testes A/B | Quantitativo, comportamental | Qual de duas versões tem melhor desempenho |
| *Eye tracking* | Quantitativo, comportamental | Para onde vai a atenção visual |
| Análise de *clickstream* | Quantitativo, comportamental | Padrões de uso reais, em escala |

### Perguntar aos utilizadores: perguntas boas e más

::: {.definicao title="--- Evitar vs. preferir"}
**Evitar:**

- Perguntas indutoras (*leading*): *"Não achas que o novo menu é mais
  fácil?"*
- Perguntas fechadas sim/não que fecham a conversa: *"Gostas disto?"*
- Perguntas de dois em um (*double-barreled*): *"Foi rápido e fácil de
  encontrar?"* (mistura duas perguntas numa só resposta)
- Hipotéticas: *"Usarias esta funcionalidade?"*
- Jargão próprio: *"O que achaste do fluxo de onboarding?"* (se o
  utilizador não usa essa palavra, ele não sabe do que falas)

**Preferir:**

- Perguntas abertas: *"Conta-me sobre a última vez que…"*
- Comportamento, não opinião: *"O que fizeste?"* em vez de *"O que
  farias?"*
- Uma coisa de cada vez: dividir a pergunta dupla, perguntar a primeira
  metade, depois a segunda.
- Episódios concretos e recentes: *"Explica-me passo a passo o que
  aconteceu."*
- As palavras do próprio utilizador: escrever o vocabulário dele — é o
  modelo conceptual dele.
:::

### Manter a conversa a fluir

Alguns estímulos conversacionais úteis durante uma entrevista: *"Conta-me
mais."*, *"Porquê?"* (e depois "porquê" outra vez), *"O que aconteceu a
seguir?"*, *"Podes mostrar-me?"*, *"O que esperavas que acontecesse?"*, e
até **silêncio** — contar até cinco antes de fazer a pergunta seguinte (dar
espaço para o entrevistado continuar sozinho).

::: {.definicao title="--- Protocolo mínimo de entrevista"}
- Um guião de **6 a 8 perguntas abertas**, cerca de **30 minutos**,
  semiestruturado: seguir o que a pessoa vai dizendo, não ler o guião à
  letra.
- **Dois entrevistadores**: um pergunta, o outro toma notas (citações,
  surpresas, vocabulário usado).
- Pedir permissão antes de gravar. Aquecer com perguntas de contexto.
- Terminar com: *"Há mais alguma coisa que eu devesse ter perguntado?"*
- Escrever o resumo logo a seguir à entrevista, enquanto está fresco na
  memória.
:::

::: exemplo
**Exemplo resolvido: guião de entrevista para um sistema de reservas da
cantina universitária.**

Suponhamos que o projeto do grupo é desenhar um sistema para gerir
reservas de refeições na cantina da faculdade. Um guião de 6 perguntas
abertas, seguindo as regras acima, podia ser:

1. "Conta-me como foi a última vez que foste almoçar à cantina, desde que
   saíste da aula até te sentares a comer." *(episódio concreto e
   recente, não "normalmente")*
2. "O que aconteceu quando chegaste e viste a fila?" *(comportamento, não
   opinião)*
3. "Já alguma vez tentaste saber antes o que ia haver para comer? Como o
   fizeste?" *(comportamento, aberta)*
4. "Podes mostrar-me, no teu telemóvel, o que costumas usar para ver o
   menu ou horários?" *("mostra-me", concreto)*
5. "O que esperavas que acontecesse quando [fizeste X, referido na
   resposta anterior]?" *(usa a resposta anterior, não hipotética)*
6. "Há mais alguma coisa sobre almoçar cá na faculdade que eu devesse ter
   perguntado?" *(fecho recomendado)*

Excerto ilustrativo de como a conversa podia fluir usando os estímulos
acima (E = entrevistador, U = utilizador):

> **E:** Conta-me como foi a última vez que foste almoçar à cantina.
> **U:** Fui às 12h30, estava uma fila enorme...
> **E:** Conta-me mais. *(estímulo "conta-me mais")*
> **U:** Pois, cheguei e vi a fila lá fora, quase desisti.
> **E:** Porquê? *(estímulo "porquê")*
> **U:** Porque já me tinha acontecido perder a aula a seguir por causa
> disto.
> **E:** *(silêncio de 5 segundos)*
> **U:** ...e às vezes nem sei se ainda há do prato que eu queria, quando
> lá chego.

Repara que a última frase do utilizador ("nem sei se ainda há do prato que
eu queria") só apareceu **depois do silêncio** — é exatamente o tipo de
informação espontânea que o protocolo tenta capturar, e que não teria
aparecido com uma pergunta fechada como "gostas da fila da cantina?".
:::

### Enviesamentos (*bias*) na investigação com utilizadores

Tanto o entrevistador como o entrevistado trazem enviesamentos para a
investigação. Para cada um, os slides dão um "antídoto" concreto:

::: {.definicao title="--- Enviesamentos e antídotos"}
- **Confirmação**: notas só o que confirma o que já acreditavas. *Antídoto:*
  escreve, antes da entrevista, o que provaria que estás errado.
- **Indução do entrevistador** (*leading*): a pergunta já contém a
  resposta. *Antídoto:* usa sempre o mesmo guião, com formulação neutra.
- **Desejabilidade social**: as pessoas dizem o que as faz parecer bem.
  *Antídoto:* pergunta sobre factos e comportamento recente, não sobre
  virtudes.
- **Aquiescência**: as pessoas tendem a concordar com o que propões.
  *Antídoto:* evita perguntas sim/não; oferece alternativas reais.
- **Enviesamento de memória** (*recall bias*): a memória é uma
  reconstrução, não uma reprodução exata. *Antídoto:* pergunta pela última
  vez concreta, nunca pelo que a pessoa faz "normalmente".
- **Enviesamento de amostragem**: os teus amigos e colegas de turma não são
  os teus utilizadores. *Antídoto:* procura as personas que definiste, não
  as pessoas que tens mais à mão.
:::

**Observar mais do que perguntar.** Ver alguém fazer a tarefa vale mais do
que perguntar como a faz: o relato passa pelo filtro da memória e dos
enviesamentos acima, a observação direta não.

### Personas

::: {.definicao title="--- Persona (definições dadas nos slides)"}
> "Uma Persona é um arquétipo de utilizador que se pode usar para ajudar a
> guiar decisões sobre funcionalidades do produto, navegação, interações,
> e mesmo o desenho visual." --- Kim Goodwin, *Perfecting Your Personas*

> "Personas dão-nos uma forma precisa de pensar e comunicar sobre como os
> utilizadores se comportam, como pensam, o que querem realizar, e
> porquê." --- Alan Cooper

> "Personas ajudam uma equipa a evitar desenhar para si própria." --- Alan
> Cooper
:::

**Uma persona não é:**

- baseada em dados demográficos ou segmentos de mercado;
- feita a partir de "sensações à barriga" (*gut feelings*) sobre o público;
- um perfil de utilizador genérico ou um estereótipo.

### Como criar as personas: segmentar e escolher uma pessoa-exemplo

O procedimento dado no Módulo 03 é: **segmentar o mercado** (os grupos de
utilizadores com necessidades diferentes) e depois **escolher uma
pessoa-exemplo, imaginária, para cada segmento**. Cada persona é descrita
por uma ficha curta com: nome e idade, um retrato breve com detalhes
pessoais, e quatro campos --- **objetivo**, **frustração**, **tecnologia**
que usa e **contexto** de uso.

::: {.exemplo title="--- As duas personas dos slides (produto de registo de hábitos/saúde)"}
| | **Susana, 42** | **Rogério, 37** |
|---|---|---|
| Retrato | Professora de Português e História numa escola em Gaia. Dois filhos. Gosta de ler sobre dietas e experimenta uma nova todos os janeiros. | Analista de mercado numa empresa de retalho no Porto. Vai ao ginásio antes do trabalho, três vezes por semana. |
| Objetivo | Registar o que come **sem introduzir dados** | Ver o seu progresso **num relance, sem parar** |
| Frustração | Apps que pedem cada ingrediente; texto pequeno | Relógios com quatro botões e menus escondidos |
| Tecnologia | Telemóvel Android e WhatsApp; raramente portátil | Smartwatch; dois monitores e folhas de cálculo o dia todo |
| Contexto | À noite, no sofá, depois de corrigir testes; 20 minutos | No ginásio às 7h30, mãos ocupadas, auriculares postos |

Repara como os **quatro campos** já dão decisões de desenho diretas: para a
Susana, entrada de dados mínima e letra grande num telemóvel; para o
Rogério, informação visível sem interação num ecrã de relógio.
:::

**Teste de cobertura:** *"Há alguém que fique de fora, entre estas duas?"*
Se sim, é preciso mais personas --- mas **no máximo 3 ou 4** (coerente com
a regra 8 abaixo). **Questionários e testes** aos utilizadores reais servem
para prever como vão comportar-se com o produto e que conhecimentos prévios
têm --- é isso que alimenta os campos da ficha, não a imaginação do grupo.

**Isto não contradiz** "uma persona não é baseada em segmentos de mercado"
nem a regra 9 abaixo† (interpretação para conciliar os dois módulos): a
segmentação só serve de **ponto de partida para garantir cobertura** (não
deixar nenhum tipo de utilizador de fora). A persona continua a ser
definida pelos **objetivos, frustrações e contexto**, não pelos dados
demográficos: as fichas da Susana e do Rogério têm idade e profissão, mas
o que as distingue e orienta o desenho são esses três campos.

### As 10 regras para criar personas

::: {.definicao title="--- 10 regras"}
1. Mantém-as simples e **memoráveis**.
2. Devem separar-se por **objetivos** (*goals*), não por comportamento.
3. Foca-te em satisfazer a audiência mais ampla, não a audiência de vendas.
4. Acrescenta algum detalhe pessoal.
5. Foca-te em 3 ou 4 objetivos por persona.
6. Cria as personas no contexto de um projeto específico.
7. As personas representam **padrões de comportamento**, não descrições de
   cargo ou função.
8. Mantém o conjunto de personas pequeno.
9. Não há correlação direta entre segmentos de mercado e personas.
10. **Foca-te em objetivos, não em tarefas.** Tarefas são coisas que
    fazemos para atingir objetivos.
:::

::: exemplo
**Exemplo resolvido: construir uma persona para o sistema da cantina,
aplicando as 10 regras uma a uma.**

Continuando o exemplo do sistema de reservas da cantina universitária:

- **Regra 1 (simples e memorável)**: chamamos-lhe "Mariana, a estudante
  entre aulas" — um nome e uma etiqueta curta, fácil de lembrar em
  discussão de grupo, em vez de "Utilizador tipo A".
- **Regra 2 (separar por objetivos, não comportamento)**: definimos a
  Mariana pelo que ela **quer alcançar** ("não perder tempo de estudo à
  espera numa fila"), não por "ela usa sempre o telemóvel" (isso é
  comportamento, não objetivo).
- **Regra 3 (audiência mais ampla, não a de vendas)**: a Mariana representa
  o estudante comum com 15 minutos entre aulas — não o "cliente ideal" que
  a cantina gostaria de atrair (ex: alguém que janta lá todos os dias), mas
  quem realmente vai usar o sistema todos os dias.
- **Regra 4 (detalhe pessoal)**: Mariana está no 2.º ano de Biologia, tem
  aula das 11h às 12h30 e outra às 14h — o detalhe (o curso, o horário)
  torna-a concreta em vez de abstrata.
- **Regra 5 (3-4 objetivos)**: os objetivos da Mariana ficam limitados a
  quatro: (1) saber antes de sair de casa se vai haver comida que lhe
  sirva (é vegetariana), (2) não perder tempo em fila, (3) não gastar mais
  do que 20 minutos no almoço, (4) conseguir mudar de plano se a aula
  atrasar.
- **Regra 6 (contexto de um projeto específico)**: esta persona só faz
  sentido *para este projeto* (sistema de reservas de cantina) — não é uma
  persona genérica de "estudante universitário" reutilizável noutro
  projeto.
- **Regra 7 (padrões de comportamento, não cargo)**: não a descrevemos como
  "estudante de Biologia" (isso é uma categoria/cargo); descrevemo-la pelo
  padrão "decide o que comer em função do tempo livre real que tem entre
  aulas", que é um padrão de comportamento que outras pessoas de cursos
  diferentes também partilham.
- **Regra 8 (conjunto pequeno)**: o grupo define só **duas** personas no
  total para este projeto (por exemplo, "Mariana" e um funcionário da
  cantina que gere o stock), não seis ou sete variantes.
- **Regra 9 (sem correlação direta com segmentos de mercado)**: não se cria
  uma persona por curso (Biologia, Direito, Engenharia...) só porque esses
  são segmentos que existem na faculdade — os objetivos da Mariana podem
  ser partilhados por alguém de qualquer curso.
- **Regra 10 (objetivos, não tarefas)**: a ficha final da persona lista
  "não perder tempo de estudo à espera" como objetivo — e só depois, à
  parte, é que aparecem as tarefas concretas que a ajudam a atingir isso
  (ex: "consultar o menu do dia antes de sair de casa"), para não
  confundir o objetivo com o caminho para lá chegar.

O resultado (uma ficha de persona típica) tem então: nome + etiqueta curta,
um retrato breve com 1-2 detalhes pessoais concretos, e uma lista de 3-4
objetivos. No formato de ficha do Módulo 03 (ver secção anterior),
acrescentam-se os outros três campos:

- **Frustração**: filas de que só se apercebe quando já lá está; não
  saber se ainda há o prato vegetariano.
- **Tecnologia**: telemóvel (usa sobretudo o Instagram e a app da
  universidade).
- **Contexto**: no intervalo entre aulas, a andar no corredor, com 5
  minutos para decidir.
:::

::: {.pratica title="--- Personas do COL (item 2 do R1)"}
**Exercício P.2** (projeto COL). Escreve as **três personas** de operador
que o R1 pede --- **uma com pouca experiência** --- aplicando as 10 regras
acima e a ficha do Módulo 03 (objetivos, frustração, tecnologia, contexto).

Pistas: o enunciado já te dá muito do **contexto** (turnos de 8 h, sala 24 h
de outubro a abril, o coordenador fora da sala, "às 3 da manhã, seis horas
dentro do turno"). Cuidado com a **regra 7**: "operador" é um **cargo**, e
as três personas têm o mesmo cargo. O que as distingue tem de ser o
**padrão de comportamento** e os **objetivos**, não o posto. E o enunciado
pede explicitamente "**o que as põe em dificuldade**".

Faz isto sozinho **antes** da discussão em grupo (regra "escolher sozinho,
depois discutir", Aula 1).
:::

## T2 --- Estudos iniciais

Depois de identificados os stakeholders e as personas (T1), a T2 aprofunda
a investigação em três frentes:

::: {.definicao title="--- As três frentes dos estudos iniciais"}
- **Utilizador**: o que sabe o utilizador final? O que quer? Do que é
  capaz? Que metáforas reconhece? Qual a sua literacia tecnológica?
- **Tecnologia**: que tecnologia pode ser usada? Que características tem?
  Que alternativas existem?
- **Objetivos**: o que deve o sistema fazer? O que é crítico? O que é
  opcional? Quais as prioridades entre os vários objetivos?
:::

Estas três frentes (Utilizador, Tecnologia, Objetivos) vão reaparecer como
os três vértices do "triângulo mágico" mais à frente nesta aula — não é
coincidência: são as mesmas três forças que atuam ao longo de todo o
processo de desenho, só que aqui aparecem como perguntas de investigação e
mais à frente como restrições a negociar.

### Perceber o problema

Antes de propor soluções, o grupo tem de **perceber o problema**:

- saber **o que deve fazer** --- e **o que não pode fazer**;
- usar **argumentos racionais** e **procurar evidência**;
- perceber **o que vale a pena** (o que tem valor para os stakeholders).

Na prática: **identificar os stakeholders**; **procurar mais informação em
várias fontes**; **discutir o problema com os outros membros do grupo**;
**discutir os prós e contras** --- incluindo aquilo que o grupo é e não é
capaz de fazer.

::: {.exemplo title="--- A história do lojista (contada pelo professor)"}
Um lojista queixava-se: *"Eu não chego... Não consigo... O negócio vai
arruinar-se porque não chego, sozinho não consigo... E depois é um problema
com as contas."* A solução adotada foi arranjar outra pessoa para fazer a
contabilidade. Mas o problema real era outro: o senhor **não chegava
fisicamente às prateleiras mais altas**, onde estavam guardados os registos
das encomendas.

**Lição:** as palavras do utilizador têm de ser levadas à letra e
investigadas ("não chego" era literal), e **observar** o contexto teria
revelado o problema verdadeiro --- é a regra "observar mais do que
perguntar" (T1) e "escrever as palavras exatas do utilizador". Resolver o
problema errado pode custar muito e não resolver nada.
:::

O slide do "Yoda" resume, com humor, como é a procura de informação nesta
fase: a informação está onde está (é preciso ir procurá-la); **não vais
saber à partida se é correta e precisa** (daí cruzar várias fontes); e
começa-se... pelo princípio.

### Racionalizar o processo: evidência

Todas as decisões têm de **fornecer evidência**. Por isso a evidência tem
de ser **recolhida e organizada**: obter dados de **quem sabe**
(stakeholders), recolher **muitos** dados (inquéritos/questionários),
**agregar** os resultados e **tirar conclusões**. Esta etapa ("recolher
dados, agregar, concluir") é uma das etapas do procedimento completo (Aula
3) e entra no R1.

## T3 --- Desenho conceptual

O desenho conceptual junta os **modelos mentais** identificados na
investigação de utilizadores com decisões de desenho concretas. Envolve
três construções distintas:

::: {.definicao title="--- Funcionalidade, modelo conceptual e imagem do sistema"}
1. **Desenhar a funcionalidade do sistema**: definir como o sistema
   *realmente* é, por dentro (a lógica/mecanismo real).
2. **Construir um modelo conceptual**: definir como *queres* que o
   utilizador veja o sistema (uma simplificação intencional, não o
   mecanismo real).
3. **Construir uma imagem do sistema**: definir a imagem (ecrãs, botões,
   textos, sons) que vai levar o utilizador a formar exatamente o modelo
   conceptual pretendido.
:::

![](figuras/modelo_conceptual_imagem_sistema.pdf){width=100%}

*Três modelos e um só canal (Módulo 05). O desenhador espera que o
utilizador construa o mesmo modelo que ele, mas a única mensagem que lhe
envia é o próprio produto. Esboços e protótipos são a forma mais barata de
testar se essa imagem produz o modelo certo.*

- **Modelo do desenhador:** como o desenhador pensa que o produto funciona
  e deve ser usado.
- **Imagem do sistema:** tudo o que o produto mostra: ecrãs, etiquetas,
  sons, comportamento, e o manual que ninguém lê.
- **Modelo do utilizador:** o que o utilizador conclui ao usá-lo, a partir
  da imagem do sistema e da experiência passada.

Quando a imagem do sistema esconde ou contradiz o mecanismo, o modelo do
utilizador sai errado, e o desenhador chama-lhe "erro do utilizador" (os
tratores da Aula 4). Por isso, **o desenho conceptual é o desenho da
imagem do sistema**: o objetivo é que o modelo do utilizador fique perto
o suficiente do real para **prever o que o sistema vai fazer**. No COL,
ninguém vai estar ao lado do operador às 3 da manhã numa noite de cheia:
só os dois ecrãs e a parede se vão poder explicar sozinhos. (O que
alimenta o modelo do utilizador e como ele falha: Aula 5.)

::: exemplo
**Ligação ao exemplo da máquina de café (Aula 1):** o **sistema real** da
máquina de café é o conjunto de tubagens, aquecedores e mecanismos de
dispensa. O **modelo conceptual** que o desenhador da interface *quer* que
o utilizador tenha é algo como "escolho uma bebida no ecrã, pago, e ela
sai" — uma simplificação total do mecanismo real, mas suficiente e correta
para o que o utilizador precisa de saber. A **imagem do sistema** é o ecrã
tátil com fotos das bebidas, o leitor de moedas/cartão visível, e o som de
confirmação ao escolher — tudo desenhado para que, ao olhar para a máquina,
o utilizador construa sozinho aquele modelo mental simples, sem nunca
precisar de saber que há um garrafão de água e um sistema de aquecimento
lá dentro.

Se a imagem do sistema estivesse mal desenhada (por exemplo, um botão sem
etiqueta, ou um ecrã que pede um código antes de mostrar as bebidas sem
explicar porquê), o utilizador construiria um modelo conceptual errado
(ex: "isto pede uma password, deve ser só para funcionários") — e o
protótipo/esboço é precisamente a ferramenta mais barata para detetar isto
**antes** de construir o sistema real.
:::

**Dica dada nos slides**: usar um protótipo rápido e simples para testar
isto, em vez de tentar acertar a imagem do sistema de forma puramente
teórica.

### Do problema aos modelos conceptuais: o *pipeline*

::: {.definicao title="--- Pipeline do modelo conceptual (6 passos)"}
1. **Perceber** o que tens de fazer.
2. **Criar** modelos para soluções (vários, não um).
3. **Esboçar** cada modelo --- depressa!
4. **Descrever** o modelo por texto.
5. **Avaliar** os modelos.
6. **Melhorar** o(s) mais promissor(es).

Os **quatro primeiros** produzem modelos candidatos; os **dois últimos**
selecionam e refinam. Depois volta-se a **Esboçar** (passo 3) com o modelo
melhorado --- é um ciclo, como o ciclo de desenho iterativo abaixo.
:::

A forma de gerar e reduzir os modelos é o **método 10x10** (Aula 3). O fim
deste processo é chegar ao "máximo" da melhor ideia, documentado com
**esboço + texto** --- e ter, no fim, **muita evidência** para mostrar
(esboços, grelhas, decisões).

### Avaliar os modelos conceptuais: grelhas de avaliação

::: {.definicao title="--- Grelhas de avaliação"}
- **Criar grelhas de avaliação**: **uma linha por modelo**, **uma coluna
  por critério**, **uma grelha por avaliador**.
- **Quantos mais avaliadores, melhor** --- e **quanto mais diferentes
  entre si, melhor**. Avaliadores de **outros grupos** conhecem o domínio:
  é isso que torna a crítica informada.
- **Criar escalas** para as avaliações e **evitar avaliações neutras**:
  usar um **número par de níveis** (ex.: 1--4, não 1--5).
- **Criar heurísticas de agregação** dos valores das grelhas: a regra que
  diz como as pontuações individuais se tornam a decisão do grupo.
:::

**Porquê um número par de níveis†:** numa escala 1--5, um avaliador
indeciso responde "3", que não diz para que lado tende. Numa escala 1--4
não há meio: tem de se inclinar para "mais bom" (3) ou "mais mau" (2), e a
grelha fica mais informativa.

::: {.exemplo title="--- Grelha de avaliação para o sistema da cantina (exemplo construído)"}
Três modelos conceptuais: **A** --- reserva na app com hora marcada;
**B** --- ecrã à entrada com fila virtual; **C** --- menu publicado nas
redes sociais com contador de doses. Critérios: **c1** rapidez para a
Mariana (a persona principal), **c2** custo técnico (4 = barato),
**c3** facilidade para o funcionário da cantina. Escala **1--4** (par). Dois
avaliadores de outros grupos, **uma grelha cada**:

| Avaliador 1 | c1 | c2 | c3 | soma |
|---|---|---|---|---|
| A | 4 | 2 | 3 | 4+2+3 = **9** |
| B | 3 | 3 | 2 | 3+3+2 = **8** |
| C | 2 | 4 | 4 | 2+4+4 = **10** |

| Avaliador 2 | c1 | c2 | c3 | soma |
|---|---|---|---|---|
| A | 4 | 2 | 4 | 4+2+4 = **10** |
| B | 2 | 3 | 2 | 2+3+2 = **7** |
| C | 1 | 4 | 3 | 1+4+3 = **8** |

**Heurística de agregação** (definida pelo grupo **antes** de ver os
resultados): (1) somar as pontuações de todos os avaliadores; (2) **veto**:
um modelo que tenha **1** no critério da persona principal (c1), em
qualquer grelha, fica eliminado.

- Passo (1): A = 9 + 10 = **19**; B = 8 + 7 = **15**; C = 10 + 8 = **18**.
- Passo (2): C tem c1 = 1 na grelha do Avaliador 2 → **eliminado**, apesar
  de ter a segunda maior soma.
- Decisão: **A** (19 > 15). B e C **não se deitam fora** --- podem dar
  ideias para as variações de A (passo 5 do 10x10, Aula 3).

Sem a regra de veto, a soma sozinha teria escondido que C falha no objetivo
principal da persona; é por isso que a heurística de agregação tem de ser
pensada e não só "somar tudo".
:::

### O desenho como um processo de negociação iterativa

Numa tarefa de desenho há sempre **objetivos em conflito**. Sobre os
stakeholders, há uma abordagem errada e uma correta:

- **Abordagem simples (incorreta):** considerar o utilizador como o
  único stakeholder.
- **Abordagem correta:** considerar **todos** os stakeholders (ver T1).

Ao desenhar/construir o sistema, há uma ordem de prioridade nas restrições:
os **objetivos funcionais têm de ser cumpridos** (isto é a linha de base,
não negociável), mas **as limitações do utilizador** e **as limitações da
tecnologia** também têm de ser tidas em conta.

### O triângulo mágico

![O triângulo mágico: Objetivos, Tecnologia e Utilizador — três forças que puxam em direções diferentes; o desenho é o compromisso negociado entre elas](figuras/triangulo_magico.pdf){width=60%}

*Três vértices que puxam em direções diferentes. Um desenho é o
compromisso que o grupo negoceia entre eles.*

**Dica prática para o trabalho de grupo**: cada um dos (três ou quatro)
elementos do grupo estuda um vértice do problema. Nas reuniões de grupo,
cada membro "defende" o seu vértice, e o grupo "negoceia" uma solução de
desenho. A negociação só para quando **todos** os participantes ficam
satisfeitos com o compromisso encontrado (não quando a maioria vence).

### O ciclo de desenho iterativo

![O ciclo iterativo: analisar, conceptualizar, prototipar, avaliar — e voltar a analisar com o que se aprendeu](figuras/ciclo_desenho_iterativo.pdf){width=80%}

::: {.definicao title="--- As quatro etapas do ciclo"}
**Analisar** (utilizadores, tarefas, contexto) → **Conceptualizar** (modelo
mental, imagem do sistema) → **Prototipar** → **Avaliar** → de volta a
Analisar, com o que se aprendeu na avaliação. Repete-se **até a evidência
dizer que o resultado já é suficientemente bom**.
:::

Nota como este ciclo (Analisar/Conceptualizar/Prototipar/Avaliar) é, na
prática, a mesma lógica de T1→T2→T3→T4→T3 vista no início da aula, só que
descrita ao nível do processo de desenho em si, e não ao nível das tarefas
do trabalho de grupo.

## Esboçar (*sketching*)

**Esboçar não é sobre desenhar bem** — é uma ferramenta para **exprimir**,
**desenvolver** e **comunicar** ideias de desenho. Faz parte do processo em
várias fases: geração de ideias, elaboração do desenho, escolhas de
desenho, e engenharia. (Esta secção junta o que os Módulos 02 e 04 dizem
sobre esboços: as razões, os atributos de um esboço, a diferença para um
protótipo e o caderno de esboços.)

### Porque esboçar?

::: {.definicao title="--- Três razões para esboçar"}
- **Criar**: ideação inicial; pensar abertamente sobre ideias; força a
  visualizar como as coisas se encaixam; *brainstorming* (gerar ideias em
  abundância sem te preocupares com a qualidade); inventar e explorar
  conceitos.
- **Registar**: ideias que desenvolves; ideias com que te deparas; arquivar
  ideias para reflexão posterior.
- **Refletir, partilhar, criticar, decidir**: comunicar ideias a outros;
  convidar respostas, críticas e alternativas; escolher as ideias que vale
  a pena perseguir.
:::

**Um esboço, uma ideia.** Misturar ideias diferentes no mesmo esboço
impede depois avaliá-las, compará-las ou escolher entre elas.

**"Queremos que falhes depressa"** (*"We want you to fail fast"*). O
Módulo 04 responde assim às perguntas "porquê desenhos maus? porquê
esboçar? porque não desenhos de qualidade?": **os esboços tornam o falhar
barato.** Uma ideia má descoberta num esboço de dois minutos custa dois
minutos; a mesma ideia descoberta num protótipo Figma acabado custa dias,
e descoberta no sistema já construído custa muito mais. Como quase todas as
primeiras ideias falham (é o que a Aula 4 mostra, em "Como falham as
interfaces"), o objetivo é falhar **cedo e muitas vezes**, enquanto é
barato.

### Os atributos de um esboço

Os atributos vêm do livro *Sketching User Experiences* (Bill Buxton), em
que o Módulo 04 se baseia. São o que distingue um esboço de qualquer outro
desenho: um desenho que não os tem não é um esboço, mesmo que seja feito a
lápis.

::: {.definicao title="--- Atributos de um esboço (1): o processo"}
- **Rápido** (*quick*) **de fazer.** Segundos ou minutos, não horas.
- **Oportuno** (*timely*): está disponível **quando é preciso**, no
  momento da discussão, e não dias depois.
- **Descartável** (*disposable*): o investimento está **no processo e no
  conceito, não na execução**. *"Se não te podes dar ao luxo de o deitar
  fora, não é um esboço."*
- **Abundante** (*plentiful*): os esboços fazem sentido **numa coleção ou
  série de ideias**. Um esboço sozinho diz pouco; o significado e a
  relevância vêm do contexto (por exemplo, os estudos de forma de um
  despertador digital no slide: dezenas de formas lado a lado, cada uma só
  interessa comparada com as outras).
:::

**"Descartável" não quer dizer "deita fora".** O slide acrescenta: *"(Obs:
in this course you shouldn't!)"*. Descartável é uma atitude: não te
prendas a um esboço só porque já o fizeste. Mas o esboço fica guardado,
porque é **evidência**: o R1 pede **todas as alternativas da S3
fotografadas** (Aula 1, R1), o passo 4 do 10x10 diz "não deites fora os
outros desenhos" (Aula 3) e a regra do caderno de esboços (abaixo) é "não
apagues ideias".

::: {.definicao title="--- Atributos de um esboço (2): a forma"}
- **Vocabulário claro** (*clear vocabulary*): o traço e o estilo mostram
  logo que é um esboço e **não uma implementação**. Quem o vê sabe que
  ainda pode mudar tudo.
- **Resolução limitada** (*constrained resolution*): o detalhe **não vai
  além do necessário** para captar o conceito.
- **Coerência com o estado** (*consistency with state*): o acabamento do
  desenho **acompanha o estado de desenvolvimento** do conceito. Uma ideia
  ainda vaga tem um desenho vago; uma ideia já decidida pode ter um desenho
  mais definido.
:::

![](figuras/esboco_tres_estados_dialogo.png){width=92%}

*O mesmo diálogo de alerta em três estados do conceito (slide 26): primeiro
um rabisco com "?" e "OK" (só se sabe que há uma pergunta e um botão);
depois um esboço mais limpo, com texto de enchimento (sabe-se a estrutura,
ainda não o texto); por fim, o diálogo real, com o texto definitivo. O
acabamento cresce com a ideia.*

O Módulo 04 desdobra estes três atributos em mais três ideias, mostradas
com exemplos do "ligar dois telemóveis" (o exemplo do 10x10, Aula 3):

::: {.definicao title="--- Detalhe mínimo, refinamento adequado, abertura"}
- **Detalhe mínimo** (*minimal detail*): incluir **só o que é preciso**
  para mostrar o propósito ou o conceito. No slide, dois ecrãs "Connected!
  with George / with Sally" com três botões (Photos, Contacts, ...) e uma
  frase escrita ao lado ("uma vez ligadas, as pessoas podem trocar várias
  coisas") chegam para explicar a ideia.
- **Grau de refinamento adequado** (*appropriate degree of refinement*): o
  esboço é **tão refinado como a ideia**. Ideia sólida, esboço mais
  definido; ideia genérica, esboço menos definido. O contraexemplo do slide
  é um telemóvel desenhado em perspetiva, sombreado, com etiquetas técnicas,
  para uma ideia que ainda era só "encostar os dois telemóveis": o desenho
  promete mais do que a ideia tem.
- **Abertura e liberdade vs. fechado e preciso** (*openness and freedom
  vs. tight and precise*): um bom esboço é **incompleto** e deixa espaço
  para criar ("3 toques simultâneos nos dois telemóveis", desenhado à mão
  com dois telemóveis e um dedo). Um desenho técnico de patente, com todas
  as peças numeradas, está **completo**: não deixa nada para fazer, por
  isso já não serve para explorar.
:::

::: {.definicao title="--- Atributos de um esboço (3): o efeito nas pessoas"}
- **Sugere e explora, em vez de confirmar** (*suggest and explore rather
  than confirm*): mostra e provoca **o que podia ser**, não o que já está
  decidido.
- **Catalisador** (*catalyst*): **provoca conversa e discussão**. Um
  esboço é bom quando as pessoas pegam nele, escrevem por cima e propõem
  outra coisa.
:::

![](figuras/esboco_catalisador.png){width=88%}

*O esboço como catalisador (slide 29): ao lado do diálogo "Alert" alguém
colou uma nota "'Alert' soa intimidante" e outra "e se, em vez de diálogos
modais, fosse uma notificação (toaster) que aparece uns segundos?", com
três variações dessa ideia à direita. O esboço não foi aprovado nem
reprovado: gerou ideias novas.*

**A lista completa** (*wrap-up* do Módulo 04, slide 29): rápido, oportuno,
descartável, abundante, vocabulário claro, resolução limitada, coerente
com o estado do desenho, sugere e explora, catalisador. Para cada um,
sabe dizer o que é numa frase e dar um exemplo do que o viola.

### Um esboço não é um protótipo

::: {.definicao title="--- Esboço vs. protótipo"}
A diferença entre os dois é:

- um **contraste de propósito** (**sempre**): o **esboço serve para
  comunicar** (explorar e discutir ideias); o **protótipo serve para
  verificar** (testar se o desenho funciona);
- um **contraste de forma** (**normalmente, mas nem sempre**): o esboço
  costuma ser a lápis e o protótipo no computador, mas pode haver um
  protótipo em papel, ou um esboço feito numa ferramenta digital.

Não há uma fronteira nítida: é um **contínuo** (*continuum*), do esboço
puro ao protótipo puro. *"Esboçar é sobre desenho da interface;
prototipar é sobre teste da interface."*
:::

![](figuras/esboco_prototipo_buxton.png){width=48%}

*Do esboço ao protótipo (Buxton, 2007). O eixo horizontal é o tempo e o
vertical o investimento. A mancha começa larga e cor de laranja (esboço,
"Design": muitas ideias em aberto) e estreita até ficar rosa (protótipo,
"Usability": poucas ideias, já a ser testadas). A seta vermelha mostra que
o investimento em cada artefacto cresce com o tempo; as setas curvas são as
iterações, que continuam em todas as fases.*

Os **esboços** servem a **ideação inicial**, nas fases iniciais do desenho
(e dentro de cada fase); os **protótipos** servem para **captar e detalhar o
desenho real**. As propriedades de cada um vêm aos pares, cada propriedade
do esboço com a sua oposta no protótipo:

| Esboço | Protótipo |
|-----------------------------------|-----------------------------------|
| evocativo (*evocative*) | didático (*didactic*) |
| sugere (*suggest*) | descreve (*describe*) |
| explora (*explore*) | refina (*refine*) |
| pergunta (*question*) | responde (*answer*) |
| propõe (*propose*) | testa (*test*) |
| provoca (*provoke*) | resolve (*resolve*) |
| tentativo (*tentative*) | específico (*specific*) |
| sem compromisso (*noncommittal*) | representação (*depiction*) |

**Em resumo** (*wrap-up*): o esboço é evocativo, sugere, explora,
pergunta, propõe, provoca; o protótipo é didático, descreve, refina,
responde, testa, resolve, é específico.

**Do desenho inicial ao desenho final.** À medida que o desenho avança, o
artefacto usado passa de muitos esboços a um sistema que funciona:

| Fase do desenho | Artefacto |
|------------------------------------------------|---------------------------|
| Gerar ideias e representações diferentes (*brainstorm*) | Muitos esboços |
| Escolher uma representação; definir o estilo da interface em traços gerais | Variações e detalhes em esboço |
| *Walkthrough* centrado nas tarefas e redesenho | Esboços ou protótipos de baixa fidelidade |
| Afinar a interface, desenho dos ecrãs | Protótipos de baixa a média fidelidade |
| Avaliação heurística e redesenho; testes de usabilidade e redesenho | Protótipos de alta fidelidade |
| Testes de campo limitados; testes *alpha*/*beta* | Sistemas a funcionar |

*Lê-se de cima (desenho inicial, early design) para baixo (desenho final,
late design).*

**No projeto COL†**, o calendário (Aula 1) segue esta tabela quase à
letra: S3/S5 = muitos esboços e variações; Fase 1 (S6) = *cognitive
walkthrough* sobre **esboços**; S7 = *wireframes*; Fase 3 (S9) = testes de
usabilidade sobre o **protótipo interativo**. A única diferença é a
**avaliação heurística** (Fase 2, S8): a tabela põe-na sobre protótipos de
alta fidelidade, o COL sobre ***wireframes*** (média fidelidade). No
projeto, vale o enunciado.

**Fidelidade†:** quão parecido o artefacto é com o sistema final, no
aspeto e no comportamento. Baixa: papel, sem cores, sem interação real.
Alta: parece e comporta-se quase como o produto.

### Um esboço vs. uma maqueta gerada por IA

O Módulo 04 compara o esboço com uma maqueta (*mockup*) gerada por IA,
usando os atributos acima. A maqueta gerada **falha precisamente nos
atributos** que tornam o esboço útil:

| O esboço | A maqueta gerada por IA |
|----------------------------------------|----------------------------------------|
| Rápido, descartável, abundante: dez numa hora, nenhum precioso | Parece acabada: o vocabulário errado para uma ideia em aberto |
| Resolução limitada: mostra a ideia, não os píxeis | Resolução muito acima do estado do conceito |
| Coerente com o estado do conceito | Uma única resposta polida, em vez de muitas diferentes |
| Sugere e provoca: as pessoas desenham por cima | Fecha a discussão: as pessoas reagem às cores, não à ideia |
| Feito por ti: consegues explicar cada traço | Não é teu: as decisões lá dentro não foram tomadas por ninguém |

**Regra da disciplina:** imagens geradas por IA são opcionais e só servem
para **ilustrar um conceito que o grupo já escolheu**, nunca como fonte de
ideias (completa as regras de IA da Aula 1). A tabela acima explica
porquê: além da questão ética, uma maqueta polida estraga a discussão que
o esboço devia provocar.

### O caderno de esboços (*sketchbook*)

::: {.definicao title="--- Para que serve o caderno de esboços"}
- Fazer *brainstorming* de **muitas ideias iniciais, boas e más**.
- Explorar e refinar ideias, **no geral e no pormenor**.
- Desenvolver **variações, alternativas e detalhes**.
- **Refletir** sobre como o raciocínio foi mudando ao longo do tempo.
- **Comunicar** ideias aos outros, mostrando-as.
- **Escolher** as que vale a pena desenvolver.
- **Registar** boas ideias que vês noutros sítios.
- Recortar imagens inspiradoras (de revistas, por exemplo).
- Fotografar, imprimir e colecionar fotografias inspiradoras.
:::

**Instrumentos.** O **lápis** (barato, flexível, fácil de levar, na
argola do caderno; leva sempre um contigo); a **borracha e o afia**
(práticos, mas opcionais); **fita-cola, tesoura e cola** para colar objetos
encontrados (não precisas de os levar sempre contigo; junta-lhes a
**câmara do telemóvel**); **outros materiais**, desde que não atrapalhem.

::: {.definicao title="--- Boas práticas do caderno de esboços"}
- **Leva-o e usa-o com regularidade**: esboça em qualquer sítio, a
  qualquer hora. Só funciona se o tiveres contigo.
- **Enche as páginas**: uma ideia bem composta, uma série de desenhos
  relacionados, coisas que vês e que te dão ideias.
- **Esboça alternativas** (*getting the right design*): aspetos diferentes
  da interface, representações diferentes, contextos de uso diferentes...
- **Esboça detalhes** (*getting the design right*): esboços detalhados que
  desenvolvem as nuances da interface.
- **Anota os desenhos**: o que não consegues desenhar, texto
  complementar, de onde veio a ideia, a data...
- **Não apagues ideias e não o uses para outras coisas**: é o registo de
  todas as ideias em desenvolvimento, boas e más. Só para desenho.
:::

As duas boas práticas "alternativas" e "detalhes" são os dois modos de
Buxton explicados logo a seguir, em "*Getting the Design Right* vs.
*Getting the Right Design*".

**Não precisas de ser artista.** *"Um desenho feio e tosco pode captar uma
ideia tão bem como um bonito."* O exemplo do slide é uma página do caderno
de Saul Greenberg: linhas tortas, pontos e setas, mas cheia de anotações
("o primeiro evento é mostrado repetido", "o detalhe do evento fica
visível", "como uma parede em perspetiva, mas nas duas dimensões"). Os
cadernos de artistas (estudos de figuras e de narizes, no slide 39) são
mostrados com um sinal de proibido: **não é isso que se pede**.

::: {.definicao title="--- O que se encontra num caderno de esboços (exemplos dos slides)"}
- **Ideias, variações e anotações**: formatos possíveis para um relógio
  computador (de um estudante de *design* industrial); quatro versões
  diferentes de uma ideia lado a lado (caderno de Nicolai Marquardt).
- **Variações de desenho**: quatro comandos com disposições diferentes dos
  mesmos botões (do livro *Paper Prototyping* de Carolyn Snyder).
- **Visões gerais** (*overviews*): vários ecrãs numa página, com **setas a
  mostrar as relações e o fluxo** entre eles.
- ***Storyboards***: as **cenas-chave**, como numa banda desenhada (em
  *post-its*, numerados).
- **Transições de *storyboard***: ecrãs numerados (1 a 7) com o que o
  utilizador faz para passar de um ao seguinte ("selecionar um indicador",
  "clicar"...).
- **Cenários** (*scenarios*): **histórias de usos imaginados**; no slide,
  cinco cenários de uma tecnologia em ação, cada um num balão, com setas
  verdes a mostrar o que passa de um objeto para outro.
:::

No COL usas três destes tipos já nas próximas semanas: **muitas
alternativas por painel** na S3, **visões gerais** a ligar os painéis e
**dois *storyboards*** de missões na S5 (Aula 1, calendário).

::: {.pratica title="--- Esboços antes da S3"}
**Exercício P.4** (inventado, a partir do Módulo 04 e do calendário do
COL).

**(a)** Põe estes artefactos por ordem no contínuo esboço → protótipo e diz,
para cada um, se serve sobretudo para **comunicar** ou para **verificar**:
(1) um *wireframe* Figma com a posição exata de cada elemento, sem cor;
(2) dez desenhos a lápis de um painel, feitos em 20 minutos; (3) o
protótipo Figma clicável que 5 pessoas de fora vão testar; (4) um
*storyboard* de uma missão em *post-its*.

**(b)** Na S3 um colega aparece com **uma** imagem gerada por IA do painel
dele, com cores, ícones e números. Que atributos de um esboço falham? Que
risco traz para a discussão do grupo? Que regra da disciplina quebra?

**(c)** Para cada fase de avaliação do COL (*walkthrough*, heurística,
testes), diz que artefacto se usa e que fidelidade tem. Onde é que o COL
se afasta da tabela "do desenho inicial ao desenho final"?

**(d)** Aquecimento (10 minutos, fora do COL): esboça **5 formas
diferentes** de pôr o "*reset* do cronómetro" no relógio de ginásio da
Aula 4. Cada esboço tem de ter **um mecanismo diferente**, não só os
botões noutro sítio. No fim, confirma os atributos: rápido? coerente com o
estado? anotado?
:::

## *Getting the Design Right* vs. *Getting the Right Design*

Bill Buxton cunhou esta distinção entre dois modos, complementares mas
diferentes, de avançar num processo de desenho:

::: {.definicao title="--- Getting the Design Right"}
Pega-se numa ideia e **itera-se e desenvolve-se essa mesma ideia**
repetidamente — como subir uma colina (uma "paisagem de qualidade" onde o
topo representa a melhor versão possível daquela ideia).

**Problema**: fixa-se na primeira ideia. É uma "subida de colina local"
(*local hill climbing*) — não há garantia de que se chegou ao topo mais
alto possível (**máximo global**) em vez de apenas ao topo da colina mais
próxima (**máximo local**).
:::

::: {.definicao title="--- Getting the Right Design"}
Em vez de aprofundar uma só ideia, **exploram-se várias ideias em
paralelo**, escolhendo depois as mais promissoras. Regra prática dada nos
slides: gerar cerca de **5 ideias distintas** já é considerado o mínimo
para uma primeira revisão formal. A forma concreta de fazer isto nesta
disciplina é o **método 10x10** (10 conceitos diferentes, depois 10
variações do mais promissor), explicado passo a passo na Aula 3.

> "Um *designer* que apresentasse três ideias provavelmente seria
> despedido. Diria que cinco é o ponto de entrada para uma primeira revisão
> formal (destiladas de uma centena)... se estiveres só a defender uma,
> vais ser apanhado, e despedido... isto é sobre abertura de espírito,
> humildade, descoberta e aprendizagem. Se não estiveres genuinamente
> dedicado a essa abordagem, estás só a fazer batota." --- Alistair
> Hamilton, VP Design, Symbol Technologies
:::

### Elaboração e redução

::: {.definicao title="--- Elaborar, reduzir, repetir"}
- **Elaborar**: gerar soluções — estas são as oportunidades.
- **Reduzir**: decidir quais valem a pena perseguir.
- **Repetir**: elaborar e reduzir de novo, sobre as soluções escolhidas.
:::

**Desenhar é escolher** (*"Design is choice"*). Há dois espaços distintos
onde há lugar para criatividade neste processo:

1. A criatividade de **enumerar opções significativamente distintas**
   entre as quais escolher.
2. A criatividade de **definir os critérios ou heurísticas** segundo os
   quais se fazem essas escolhas.

**Os dois modos não se excluem†:** usa-se **redução** (*Getting the Right
Design*, entre várias ideias) para escolher em que ideia vale a pena
investir, e depois **elabora-se em profundidade** (*Getting the Design
Right*, dentro dessa ideia). O funil abaixo mostra essa alternância.

### O funil de desenho

Ao longo de várias iterações, o processo alterna entre **geração** de
novos conceitos e **convergência** (redução), com a granularidade a
aumentar a cada iteração:

| Iteração | Granularidade | O que acontece |
|---|---|---|
| Geral | Geral, conceitos gerais | Geração inicial de conceitos, depois primeira redução |
| Iteração 1 | Grosseira, alternativas significativas | Adicionam-se novos conceitos, reduz-se de novo |
| Iteração 2 | Média, desenvolvimento intermédio | Mais adições e reduções, a convergir |
| Iteração 3 | Fina, refinamento detalhado | Última geração/redução → conceito selecionado |

Cada iteração passa por: convergência (redução dos conceitos da iteração
anterior) → geração (novos conceitos juntam-se aos que sobreviveram) →
nova redução, num movimento em "zig-zag" até sobrar um único conceito
selecionado no fim.

**A visão de produto** (Módulo 04, slide 24). O funil não acaba no
desenho: é a primeira parte da vida de um produto, que continua em
engenharia e vendas.

![](figuras/visao_produto_sequencial.png){width=47%} ![](figuras/visao_produto_integrada.png){width=50%}

*À esquerda, a visão sequencial: o desenho (vermelho) considera **muitos
desenhos em paralelo** e a redução filtra-os até convergirem; o semáforo
verde marca o momento em que um (ou mais) desenhos recebem luz verde para
passar à engenharia (verde) e, no navio, ao lançamento e às vendas. À
direita, a visão integrada: **não há barreiras** entre as fases; desenho,
engenharia, gestão e marketing, e vendas estão presentes ao mesmo tempo e
trocam informação ao longo de todo o processo.*

A lição do slide é a da direita: o desenho não "entrega" um resultado à
engenharia e desaparece; **deve haver interação entre muitos intervenientes
diferentes** (desenho, engenharia, gestão e marketing, vendas) desde o
início, o que liga à regra de considerar **todos** os stakeholders (T1).

::: exemplo
**Exemplo dado nos slides: evolução do design de telemóveis.**

Os slides mostram duas "linhas" de evolução paralelas: uma de telemóveis
com teclado físico (dos primeiros telemóveis simples até modelos como o
BlackBerry, com "mudanças incrementais" entre cada geração), e outra que
nasce de uma **"nova ideia"** — o ecrã tátil (do primeiro iPhone até
modelos posteriores, também evoluindo por mudanças incrementais dentro
dessa linha) — seguida de outra **"nova ideia"** mais recente, o ecrã
dobrável.

A lição do exemplo: dentro de cada linha, o que acontece é sobretudo
"Getting the Design Right" (afinar a mesma ideia geração após geração —
subir a mesma colina). Mas os saltos entre linhas ("nova ideia") só
aparecem quando alguém, em algum momento, voltou a explorar **muitas
alternativas** em vez de continuar só a refinar o teclado físico — ou seja,
fez "Getting the Right Design" outra vez, em vez de continuar a otimizar
localmente uma ideia que já tinha esgotado o seu potencial.
:::

## T4 --- Avaliação

Depois de desenhado e prototipado, é preciso responder a duas perguntas:
"como vou saber que o meu modelo conceptual é suficientemente bom?" e "como
vou saber que a imagem do sistema é boa?" A resposta é **avaliar**:
construir um protótipo, usar medidas e procedimentos de avaliação
adequados, medir, e avaliar (*assess*) os resultados.

No projeto, a sequência é **cognitive walkthrough → avaliação heurística →
testes de usabilidade**: as três fases do COL ("Três fases, três
avaliações", Aula 1). Como se conduz cada um fica para módulos
seguintes.

::: {.definicao title="--- O que se avalia (avaliação de usabilidade)"}
**Não se está a avaliar um protótipo --- está-se a avaliar um conceito.** O
protótipo é só o veículo. A avaliação tem de ser **objetiva** e
**mensurável**. Nesta disciplina: *cognitive walkthrough* sobre os
**esboços**, avaliação heurística sobre os **wireframes**, testes de
usabilidade sobre o **protótipo** --- e **cada um precisa de missões
escritas como *task flows***.
:::

### *Task flows*: como escrever as missões

::: {.definicao title="--- Task flow"}
Um ***task flow*** é **um objetivo** e a **sequência de passos** que um
utilizador segue para o atingir.

- **Uma linha por passo**: o que o utilizador faz, o que o sistema mostra.
- Escrito **a partir do objetivo do utilizador, não da interface**:
  "libertar a âncora 3", e não "clicar no botão da âncora".
- **Cada dono de painel** escreve os *flows* das funcionalidades
  complexas do **seu** painel.
- Os *flows* tornam-se as **missões** do *cognitive walkthrough* e dos
  testes de usabilidade: os avaliadores seguem-nos passo a passo e
  **pontuam cada passo**.
- Termina com um **critério de sucesso** verificável.
:::

::: {.exemplo title="--- Task flow dos slides (painel de monitorização da turbina eólica)"}
**Objetivo:** verificar porque é que a âncora 3 não está a segurar e
libertar o seu cabo.

1. Reparar no alerta do painel de estabilidade.
2. Abrir o detalhe da âncora 3.
3. Ler a tensão e a profundidade.
4. Escolher "libertar cabo".
5. Confirmar e ver a tensão baixar.

**Sucesso:** o alerta desaparece dentro da missão.
:::

::: {.exemplo title="--- O mesmo formato aplicado à cantina (exemplo construído)"}
**Objetivo (da Mariana):** garantir um prato vegetariano antes de sair da
aula das 12h30.

1. Abrir a app --- o sistema mostra o menu do dia com as doses restantes.
2. Tocar no prato vegetariano --- o sistema mostra as horas de levantamento
   livres.
3. Escolher 12h45 --- o sistema pede confirmação com o preço.
4. Confirmar --- o sistema mostra o código de levantamento.

**Sucesso:** a reserva aparece em "As minhas reservas" com a hora 12h45.

Repara: cada passo diz o que **ela faz** e o que o **sistema mostra**; o
objetivo está nas palavras dela ("garantir um prato vegetariano"), não nas
da interface ("usar o ecrã de reservas").
:::

::: {.pratica title="--- Missões do COL (item 3 do R1, S4)"}
**Exercício P.3** (projeto COL). Escreve **cinco missões** para o operador
do COL no formato *task flow* acima: objetivo (nas palavras do operador),
**situação de partida**, uma linha por passo (o que ele faz / o que o
sistema mostra) e **critério de sucesso** verificável. As cinco têm de
cobrir, no conjunto, uma situação **normal**, uma de **cheia** e **pelo
menos uma avaria** de equipamento (o enunciado exige as três).

Pistas: o dia 2 de fevereiro de 2026 (Aula 1, projeto COL) é uma cheia
pronta a usar. Para as avarias, a lista de estados obrigatórios está cheia
delas (comporta bloqueada ou em modo manual local, descarga de fundo
avariada, grupo indisponível, sensor suspeito). Pelo menos uma missão
deve atravessar a **autorização do coordenador** e outra deve terminar numa
**passagem de turno**.
:::

## TPC (trabalho de casa) da Aula 2

A pergunta colocada nos slides é: qual a diferença entre *getting the
design right* e *getting the right design*? A resposta está desenvolvida
na secção correspondente acima — em resumo: a primeira aprofunda **uma**
ideia até à exaustão (risco: ficar preso num máximo local); a segunda
explora **várias** ideias em paralelo antes de escolher uma para aprofundar
(o processo real de desenho intercala as duas, como mostra o funil de
desenho).

## Dicas finais do Módulo 02

- **Planear com antecedência.**
- **Usar sempre que possível metodologias sólidas e bem estudadas**:
  desenho conceptual, inquéritos contextuais, protótipos horizontais,
  entrevistas semiestruturadas, métodos de avaliação "*discount*"
  (avaliação heurística rápida e barata, sem grande aparato experimental).
- Prestar atenção nas aulas e usar os slides como referência.
- Usar as aulas de laboratório para discutir o projeto com o professor.

# Aula 3 --- O procedimento de IPM: do problema ao protótipo

## Criar uma IPM é um processo

Há um **problema** e é preciso encontrar uma **solução** --- mas não num
único salto: é uma **sequência de passos**, em que **cada passo produz
evidência para o seguinte**. O Módulo 03 percorre essa sequência completa
e mostra onde encaixa cada coisa já vista nas Aulas 1 e 2.

![A sequência final do procedimento: oito etapas, divididas entre as duas partes do trabalho (R1 e PR2)](figuras/procedimento_ipm.pdf){width=85%}

*As oito etapas por ordem. A faixa de cima é a matéria do R1; a de baixo, a
do PR2.*

| # | Etapa | Onde está explicada neste resumo |
|--|------------------------|------------------------------|
| 1 | Formação do grupo / equipa | Aula 1, "Como os grupos funcionam" (inclui "Como criar a equipa") |
| 2 | Estudos exploratórios + stakeholders + marcos | Aula 2, T1 (stakeholders) e T2 ("Perceber o problema") |
| 3 | Recolher dados + agregar + concluir | Aula 2, T2 ("Racionalizar o processo: evidência") e métodos de T1.1 |
| 4 | Estudar o utilizador + personas + tecnologia | Aula 2, T1.1, "Personas" e T2 |
| 5 | Modelos conceptuais de desenho + decisões | Aula 2, T3 (pipeline, grelhas) + **método 10x10** (abaixo) |
| 6 | Protótipo | Aula 2, "Um esboço não é um protótipo" (o que os distingue, fidelidade por fase); a construção no Figma fica para módulos seguintes |
| 7 | Avaliação de usabilidade | Aula 2, T4 (inclui *task flows*) |
| 8 | Relatório final | Aula 1, "PR2" |

**A fronteira R1/PR2:** o R1 vai até aos **modelos conceptuais e
decisões** (etapa 5); o PR2 começa no **protótipo** (etapa 6) e inclui a
avaliação de usabilidade e o relatório final.

No COL, o **R1 já inclui a 1.ª avaliação** (o *cognitive walkthrough*
sobre os esboços, item 7 do R1). Não contradiz a fronteira: o walkthrough
avalia os **esboços** (o conceito), não um protótipo; a heurística e os
testes, sobre wireframes e protótipo, continuam no PR2.

No "meio" deste processo (entre os modelos conceptuais e o protótipo) está
o passo em que se **criam muitas "soluções" diferentes**: é aí que entra o
método 10x10. Nesta fase é preciso **fazer suposições** (*assumptions*),
**fazer muitos esboços** (treinado no laboratório --- o professor usa
cartas de Pictionary para treinar esboços rápidos) e ser **rápido a
esboçar**.

## O método 10x10

::: {.definicao title="--- Método 10x10"}
**Gerar 10 conceitos de desenho diferentes; depois produzir 10 variações /
detalhes do conceito mais promissor.** É a concretização de *Getting the
Right Design* (explorar muitas ideias) seguida de *Getting the Design
Right* (aprofundar a escolhida) --- ver Aula 2. Tem **sete passos**, que
alternam **expandir** e **reduzir** (o funil de desenho da Aula 2).
:::

![Os sete passos do método 10x10: expandir (verde), reduzir (laranja), e voltar atrás, cada vez mais fundo no funil](figuras/metodo_10x10.pdf){width=62%}

::: {.definicao title="--- Os 7 passos (1--4)"}
1. **Enunciar o desafio de desenho.** Qual é o problema a resolver? Quais
   são as necessidades do cliente? (Ex.: "produzir um sistema novo que tire
   partido de uma tecnologia em particular".)
2. **Gerar $\geq$ 10 conceitos de desenho diferentes** que respondam ao
   desafio (**fase de expansão**): *brainstorming*; ser o mais criativo e
   diverso possível; **não julgar os desenhos no momento da criação**; os
   esboços devem captar a **essência** da ideia, não os detalhes.
3. **Reduzir o número de conceitos** (**fase de redução**): rever todos os
   desenhos; descartar os que não têm mérito; explicar os restantes a
   outras pessoas e pedir *feedback*; recolher as reações (incluindo as
   tuas). **OU**, com base na reflexão, **repetir o passo 2** (melhorar).
4. **Escolher o(s) conceito(s) mais promissor(es)** --- é o teu ponto de
   partida. **Não deites fora os outros desenhos!** (Nota do professor: dos
   10 iniciais podem ficar, por exemplo, 6.)
:::

::: {.definicao title="--- Os 7 passos (5--7)"}
5. **Produzir 10 detalhes / variações dos conceitos sobreviventes**:
   explorar o conceito; gerar formas diferentes de o concretizar; ir mais
   fundo numa direção particular (mostrar os detalhes). (Nota do professor:
   expande-se **o melhor** --- **ou** os 6 sobreviventes --- com 10
   hipóteses/variações **para cada um**.)
6. **Apresentar as ideias a um grupo**: pedir *feedback* (o que é positivo,
   o que se pode melhorar) e sugestões de redesenho. ("Café e donuts são
   bem-vindos.")
7. **À medida que as ideias mudam, esboçá-las**: ou seja, voltar ao passo
   1 (ou 4), mas **mais fundo no funil de desenho**.
:::

**Não confundir as duas "dezenas":** o primeiro 10 são **conceitos
diferentes** para o mesmo desafio (largura); o segundo 10 são
**variações** de um conceito já escolhido (profundidade). Dez variações da
mesma ideia no passo 2 **não** contam como dez conceitos: seria voltar ao
máximo local (Aula 2).

## Exemplo trabalhado do 10x10: ligar dois telemóveis

O exemplo dos slides é adaptado de *Sketching User Experiences: The
Workbook* (Greenberg et al.). Segue os passos um a um.

::: {.exemplo title="--- Passo 1: o desafio e as suposições"}
**Desafio:** como podem duas pessoas ligar os seus dispositivos móveis
para trocar informação (ex.: transferir fotografias) **sem recorrer a
caixas de diálogo** ou outros pedidos tediosos da interface?

**Suposições** (*assumptions*) feitas para poder avançar:

- o dispositivo deteta telemóveis próximos;
- inicialmente, os telemóveis conseguem comunicar de forma limitada;
- as duas pessoas podem fazer uma **ação que ambos os telemóveis
  reconhecem como um "aperto de mão"** (*handshake*), confirmando que
  querem uma ligação completa --- ou seja, explora-se uma **convenção
  social**: ambos concordam em fazer alguma coisa.
:::

**Passo 2 --- gerar 10 conceitos concorrentes.** Repara que cada esboço
capta só a **essência** (sem detalhes de ecrã) e que os 10 usam **sensores
diferentes** (teclado, acelerómetro, ecrã tátil, microfone, câmara, sensor
de luz) --- é isso que os torna realmente distintos:

![Os 10 conceitos do exemplo (esboços dos slides)](figuras/connect_10_conceitos.png){width=100%}

*i) ambos escrevem uma palavra combinada; ii) um roda o telemóvel num
padrão que o outro imita (acelerómetro); iii) traçar uma linha através dos
dois ecrãs lado a lado num só gesto; iv) dizer um comando captado pelos
dois microfones; v) padrão de flash LED captado pela câmara do outro;
vi) chocar os telemóveis ("bump" --- o acelerómetro dos dois deteta a mesma
vibração); vii) som musical tocado num e captado pelo outro; viii) encostar
os ecrãs num padrão, ambos detetam o mesmo padrão claro/escuro no sensor de
luz; ix) três toques simultâneos nos dois telemóveis; x) fotografar um
elemento identificador no telemóvel do outro.*

::: {.exemplo title="--- Passos 3 e 4: reduzir e escolher"}
**Tema comum** a todos os conceitos: as duas pessoas fazem uma ação que os
dois telemóveis reconhecem como "aperto de mão" --- a convenção social das
suposições.

**Repetir?** Antes de reduzir, pergunta-se se vale a pena criar outras
variações a partir desta noção, ou explorar **outros temas** (é o "OU
repetir o passo 2" do passo 3).

**Escolher (reduzir):** as **câmaras são o denominador comum mais baixo**
--- praticamente todos os telemóveis têm uma, ao contrário de sensores de
luz ou de acelerómetros fiáveis. Por isso escolhe-se o **conceito x**:
tirar uma fotografia de um elemento identificador no telemóvel da outra
pessoa. (O critério de escolha --- disponibilidade da tecnologia --- é um
exemplo de heurística para decidir; relembra "desenhar é escolher", Aula 2,
e o vértice **Tecnologia** do triângulo mágico.)
:::

**Passo 5 --- detalhar o conceito escolhido** (três esboços em sequência,
a mostrar a interação passo a passo):

![Detalhe do conceito x: sequência de interação](figuras/connect_detalhes.png){width=100%}

*1) a Sally e o Fred abrem ambos a app "Connect!", que mostra "um de vocês
tire uma fotografia ao ecrã do outro" e um código visual; 2) uma pessoa
fotografa o ecrã do outro; 3) já ligados ("Connected! with Sally"), podem
trocar fotografias, contactos, etc.*

**...e as variações** do mesmo conceito (ainda passo 5 --- formas
diferentes de concretizar "reconhecer o outro com a câmara"):

![Variações do conceito escolhido](figuras/connect_variacoes.png){width=100%}

*Padrões a piscar nos dois ecrãs, reconhecidos pelas duas câmaras (ou luz
estroboscópica); marcas fiduciárias (tipo código) na capa, fotografadas ---
para mais segurança, ambos os telemóveis teriam de o fazer; panorama
cooperativo (uma pessoa começa um panorama, a segunda continua, a terceira
completa); os dois fotografam a mesma coisa ao mesmo tempo.*

::: {.definicao title="--- Sinopse do exemplo: boas práticas de esboço"}
Criar **muitas ideias**; **esboçar muito**; usar **bom material**; fazer
**bom uso do espaço** (da folha); criar **legendas**; criar **sequências de
ações do utilizador** (como os três esboços do passo 5); usar **cor**; usar
**setas**; **avaliar e fazer evoluir** as ideias.
:::

::: {.pratica title="--- Aplicar o 10x10 ao projeto da cantina"}
Pega no desafio "a Mariana quer garantir o almoço sem perder tempo de
estudo" e faz **só os passos 1 e 2**: escreve o desafio e as tuas
suposições, e esboça 10 conceitos **com mecanismos diferentes** (não 10
versões da mesma app). Depois, aplica uma grelha de avaliação (Aula 2, T3)
para reduzir. Confirma no fim: consegues dizer, para cada par de conceitos,
**o que os torna diferentes**? Se dois só diferem na cor do botão, contam
como um.
:::

## Exemplo de projeto de anos anteriores: a turbina eólica offshore

Os slides mostram um projeto de um ano anterior: a interface de controlo de
uma **turbina eólica offshore flutuante** (plataforma no mar, presa ao fundo
por âncoras a cerca de 300 m de profundidade). Os esboços iniciais do quadro
mostram configurações de plataformas ("3 linhas de 3"), a turbina com os
cabos das âncoras, e a plataforma vista de cima e de lado. O componente
principal é a **nacelle** (a "cabeça" no topo da torre, com o gerador, a
caixa de velocidades e o controlador); as pás mudam de ângulo (*pitch*) e a
nacelle roda para o vento (*yaw*).

O ponto importante é a forma como o problema foi **decomposto**: do
sistema inteiro para **5 problemas** (um por painel/membro do grupo), e de
cada problema para **perguntas cada vez mais detalhadas**:

![Decomposição do problema da turbina: 5 problemas, e as perguntas concretas do problema 3](figuras/eolica_decomposicao.pdf){width=100%}

::: {.exemplo title="--- O que este exemplo ensina sobre o procedimento"}
- **Decompor em painéis** liga diretamente à regra "um painel por membro"
  (Aula 1): cada membro fica dono de um dos 5 problemas, e é ele que
  escreve os *task flows* das funcionalidades complexas desse painel
  (Aula 2, T4) --- o *task flow* da âncora 3 visto em T4 é precisamente do
  painel de estabilidade deste projeto.
- **Detalhar em perguntas** ("+ detalhe", "+++ detalhe") é a forma de
  **perceber o problema** antes de desenhar: para "estabilizar a plataforma
  com as âncoras" o grupo chegou a 9 perguntas concretas (como representar a
  estabilidade em 2D/em 2 eixos? a partir de que ponto há ameaça? como
  gerir a estabilidade com as âncoras? como
  monitorizar 6 ou 8 âncoras? como entra a profundidade? que ações ---
  libertar/recolher/soltar cabo? âncoras presas? automático vs. manual?).
  Cada pergunta é uma fonte natural de conceitos para o 10x10.
- Os esboços de quadro branco mostram o nível esperado numa sessão: rápido,
  com legendas e setas, uma ideia por esboço.
:::

## Pergunta final do módulo

*"Na próxima aula prática, o que vais fazer primeiro?"* --- A resposta
segue a sequência do procedimento: primeiro a **etapa 1** (garantir que o
grupo está formado e organizado: canais de comunicação, papéis, líder da
sessão) e logo a seguir a **etapa 2** (perceber o problema: stakeholders,
estudos exploratórios, marcos). (Nota adicional: é a interpretação
coerente com o procedimento; o slide só deixa a pergunta.)

# Aula 4 --- Introdução à IPM: porquê, como falham as interfaces, e porque se esboça

O Módulo 04 (25 set 2026) tem quatro tópicos: **porquê IPM**, **introdução
à IPM**, **como falham as interfaces** e **esboçar**. Os três primeiros
são matéria nova e estão nesta aula. O quarto aprofunda o que o Módulo 02
já dizia sobre esboços, por isso foi **fundido na secção "Esboçar" da Aula
2** (ver a tabela no fim desta aula).

## Porquê IPM?

### As máquinas melhoram exponencialmente; as pessoas não

::: {.definicao title="--- Lei de Moore vs. “lei de Darwin”"}
- **Lei de Moore:** a velocidade, o tamanho e o custo dos computadores
  melhoram **exponencialmente** (o número de transístores num chip duplica
  a intervalos regulares).
- **"Lei de Darwin"** (nome irónico do slide): os **sentidos, o cérebro e
  as mãos** das pessoas são **os mesmos do ano 0**. As capacidades humanas
  são uma linha horizontal.

**O fosso entre as duas curvas é onde vive o desenho de interação.** Cada
ano, a máquina consegue fazer e mostrar mais, mas a pessoa continua a ter
os mesmos dois olhos, a mesma memória curta e os mesmos dez dedos. Quem
desenha a interface é quem faz caber uma coisa na outra.
:::

Em 2026 o slide junta **mais uma curva**: interfaces **geradas por
máquinas**, mais depressa do que alguém as consegue avaliar.

Além do fosso, há **três razões** para a IPM ser cada vez mais importante:

1. **O estrangulamento mudou de sítio.** Computação é barata e abundante;
   a **atenção, o tempo e a compreensão humanas não são**. A interface
   define o teto do que toda essa computação vale para uma pessoa.
2. **Hoje toda a gente é utilizador.** Em 1965 havia uns milhares de
   computadores, com operadores treinados e manuais. Em 2026 são **mais de
   cinco mil milhões de pessoas, sem formação e sem manual**. O desenho tem
   de levar o conhecimento consigo.
3. **Os erros custam mais.** Ecrãs controlam carros, bombas de infusão,
   redes elétricas e **comportas de barragens**. Um número mal lido num
   ecrã já não é uma chamada para o apoio técnico: **é um incidente**.

### Onde o fosso aparece primeiro: os dados

Hoje são as máquinas que produzem a maior parte dos dados, e produzem-nos
**para outras máquinas** (no slide: uma t-shirt com sensores, sensores
ligados a um *tablet*). Ao mesmo tempo, surgiram **novas formas de
interagir**: toque (2007), voz (2011--2014), óculos de realidade
virtual/aumentada (2019, 2024), interfaces de conversa e agentes
(2022--2026). Estas mudaram **o como, não o quem**: do outro lado continua
uma pessoa.

Cada um dos "V" do *big data* é, na verdade, **uma pergunta de
interface**:

| V | A pergunta de interface |
|--------------------|------------------------------------------------------|
| Volume | Milhões de leituras. Quais são as poucas que a pessoa precisa de ver **agora**? |
| Velocidade (*velocity*) | Valores novos a cada segundo. Redesenhar o ecrã sempre, ou só alertar quando algo muda? |
| Variedade (*variety*) | Números, mapas, vídeo, alarmes. Como partilham um ecrã sem lutarem entre si? |
| Veracidade (*veracity*) | Um sensor pode avariar. Como mostra o ecrã **quanto se pode confiar** num valor? |
| Variabilidade (*variability*) | Um dia normal e um dia de cheia. O mesmo ecrã deve ter o mesmo aspeto nos dois? |

*"Seja o que for que as máquinas produzam, uma pessoa ainda tem de o ver,
perceber e agir. Esse é o trabalho."*

**Ligação ao COL†:** os cinco V são, quase palavra por palavra, perguntas
que o COL tem de responder. **Variabilidade**: situações **normais** e de
**cheia**. **Veracidade**: o estado **sensor suspeito**. **Velocidade**:
caudais e níveis mudam ao minuto. **Volume** e **variedade**: duas
barragens, comportas, grupos, níveis, previsões e câmaras em dois
monitores e uma parede.

### Investimento em IPM: de onde vem o próximo crescimento

O slide mostra duas curvas em **S** cruzadas: o **investimento atual** (a
GUI, interface gráfica) e o **crescimento futuro** (a próxima curva). Por
baixo, ecrãs cada vez maiores: 1", 4", 10"--20" (a GUI), 42"--61", 72"+.

::: {.definicao title="--- Como ler as curvas em S"}
Cada tecnologia é uma curva em S: no início rende pouco, depois rende
muito, e no fim **dá cada vez menos por cada euro a mais**. A curva
seguinte começa com **uma nova forma de mostrar e manipular informação**,
não com chips mais rápidos.

- **Investimento atual: a GUI.** Desde 1981: ecrãs maiores, mais píxeis,
  retornos cada vez menores. Um ecrã de 72" não duplica a tua
  produtividade (mas aumenta-a).
- **Crescimento futuro: a próxima curva.** Cada nova forma de mostrar e
  manipular informação abriu um mercado que chips mais rápidos não
  abriram:
  - **GUI e rato (1984--1995):** a computação chegou a todas as
    secretárias, não só aos especialistas;
  - **multitoque (2007):** em 2011 já se vendiam mais *smartphones* do que
    PCs;
  - **interfaces de conversa (2022):** 100 milhões de utilizadores em dois
    meses, **sem hardware novo**.

**A próxima curva começa na interface.** Isso faz da IPM uma **decisão de
investimento**, não um acabamento final.
:::

O investimento já lá está: **cerca de metade do código e do tempo de
desenvolvimento** de uma aplicação típica vai para a interface com o
utilizador (**Myers e Rosson, 1992**).

## Introdução à IPM

### O que é o desenho de interfaces

::: {.definicao title="--- Desenho de interfaces (user interface design)"}
**Métodos e teorias para, de forma iterativa, desenhar, implementar e
avaliar a interação humana com um computador.**

O desenho é o que fica no meio de um triângulo com **pessoas**
(*humans*), **tarefas** (*tasks*) e **tecnologia** (*technology*): são as
escolhas que fazem os três encaixar. E faz-se **iterativamente**.
:::

![](figuras/triangulo_hci.pdf){width=45%}

*O triângulo da IPM: o desenho só faz sentido em relação às pessoas que
vão usar o sistema, às tarefas que querem fazer e à tecnologia disponível.
(É parecido com o triângulo mágico da Aula 2, mas não é o mesmo: lá os
vértices são objetivos, tecnologia e utilizador.)*

::: {.exemplo title="--- O Multibanco visto pelo triângulo (exemplo dos slides)"}
- **Pessoas:** qualquer pessoa dos 15 aos 85 anos. Com pressa, na rua, ao
  sol ou de noite, com alguém à espera atrás.
- **Tarefas:** levantar dinheiro, pagar uma conta, ver o saldo. Raras,
  curtas, e um erro custa dinheiro a sério.
- **Tecnologia:** um ecrã pequeno, um teclado numérico, uma ranhura para o
  cartão, outra para as notas. Sem rato, sem teclado, sem apoio ao
  cliente.
- **Desenho:** as escolhas que fazem os três encaixar: as palavras no
  ecrã, a ordem dos passos, os bips. **Porque é que o cartão sai antes do
  dinheiro?** Porque as pessoas vão-se embora quando têm **aquilo que
  vieram buscar** (o dinheiro) e esquecem-se do resto. Se o dinheiro saísse
  primeiro, o cartão ficava na máquina.
- **Iterativamente:** nada disto era óbvio quando o primeiro Multibanco
  (ATM) abriu, em 1967. **Cada passo foi aprendido a ver pessoas a usá-lo
  e a falhar.**
:::

### Alguns marcos da história da IPM

| Ano | Inovação |
|-----------------|------------------------------------------------------|
| 1963 | Manipulação direta de objetos (Sutherland, *Sketchpad*) |
| 1965 | O rato (Engelbart) |
| 1979 | A folha de cálculo (*VisiCalc*, Bricklin e Frankston) |
| 1981 | A metáfora do ambiente de trabalho (*desktop*; Xerox Star) |
| 1991 | A Web e o navegador |
| 2007 | iPhone: o multitoque como forma principal de entrada |
| 2010 | iPad. Kinect: o corpo como comando |
| 2011--2014 | Assistentes de voz (Siri, Alexa) |
| 2019, 2024 | Óculos de realidade virtual e aumentada (Quest, Vision Pro) |
| 2022 | Interfaces de conversa com LLMs (ChatGPT) |
| 2025--2026 | Interfaces com agentes: **o sistema age, a pessoa supervisiona** |

### A IPM é interdisciplinar

A interface é o sítio onde **duas famílias de disciplinas** se encontram.
Um estudante de Informática vem da coluna da esquerda; cada decisão de
desenho no projeto vai buscar algo à da direita, quer se saiba quer não.

| Do lado da máquina | Do lado humano |
|----------------------------------------|----------------------------------------|
| Computação gráfica | Arte, *design* gráfico e tátil: estética (disposição, cor, escolha de ícones, sensação ao toque) |
| Sistemas operativos | Sociologia e antropologia: comportamento de grupo e cultural |
| Linguagens de programação | Psicologia e cinesiologia: comportamento **cognitivo, percetivo e motor** |
| Ambientes de desenvolvimento | **Capacidades humanas** para usar e aprender máquinas |
| Redes; engenharia de software | |
| ... e cada vez mais: *design* industrial e de produto, processamento de média digitais, robótica | |

**Nota do professor:** esta disciplina existe para cobrir a **coluna da
direita**; a da esquerda já está coberta pelo resto do curso.

### O que faz disto IPM?

O slide define a IPM por **quatro assuntos**, cada um com um exemplo e
**a forma como falha**:

::: {.definicao title="--- Os quatro assuntos da IPM (1--2)"}
**1. Desempenho conjunto de tarefas por pessoas e máquinas.**
*Exemplo:* o GPS do carro calcula o caminho; a pessoa conduz e avalia a
estrada. **Decidir quem faz o quê é o desenho.**
*Como falha:* quando a máquina fica com a parte fácil e deixa à pessoa a
difícil. Um assistente de condução que guia durante horas e espera que a
pessoa retome o controlo em dois segundos. **Vigiar uma máquina é o que as
pessoas fazem pior.**

**2. Comunicação: da máquina para a pessoa, e de pessoa para pessoa
através da máquina.**
*Exemplo:* "Error 0x80070057" vs. "O nome do ficheiro não pode conter /".
Os vistos azuis: a máquina diz a alguém que leste a mensagem.
*Como falha:* a máquina fala por códigos e bips. Os vistos azuis são **um
estado, não uma mensagem**, mas são lidos como mensagem: "visto às 14:02,
sem resposta". Um estado técnico torna-se uma afirmação social, e **ligada
por omissão**.
:::

::: {.definicao title="--- Os quatro assuntos da IPM (3--4)"}
**3. Métodos de desenho: especificar, desenhar, implementar e avaliar
interfaces.**
*Exemplo:* nesta disciplina, personas, esboços, protótipo Figma,
*cognitive walkthrough*, avaliação heurística, testes com utilizadores
reais.
*Como falha:* o passo que costuma ser saltado é a **avaliação**. "Funciona
para mim" não é um teste: **quem desenvolve não é o utilizador**.

**4. Compromissos (*trade-offs*) de desenho.**
*Exemplo:* simples vs. completo (um comando com 6 botões ou com 60). Seguro
vs. rápido ("Tem a certeza?" antes de cada apagar).
*Como falha:* quando "completo" ganha a "simples": o relógio de ginásio
(abaixo), oito funções em quatro botões, e ninguém encontra o *reset*.
Quando "seguro" ganha a "rápido": um aviso antes de cada apagar, e toda a
gente carrega em OK sem ler.
:::

*"Todas as linhas acabam numa falha."* É a ponte para o tópico seguinte:
como falham as interfaces, e como ver isso antes dos utilizadores.

## Como falham as interfaces

### *The Design of Everyday Things* (Don Norman)

O livro de referência deste tópico é ***The Design of Everyday Things***,
de **Don Norman** (leitura opcional). A capa tem um bule com o bico do
mesmo lado da asa: um objeto que não se consegue usar.

**A psicopatologia dos objetos do dia a dia** (título de um capítulo de
Norman) são as frustrações típicas com objetos comuns:

- um engenheiro não consegue perceber como aquecer duas chávenas de leite
  com café no micro-ondas da empresa;
- quantos conseguem programar, ou usar todas as funções, do comando da
  smart TV e da *box*, do ecrã tátil do carro, da placa de indução, da
  máquina de lavar e secar, da aparelhagem (de casa ou do carro), de uma
  folha de Excel...?

A foto do slide é uma **misturadora termostática** de duche: dois manípulos
cromados iguais, sem marcas visíveis. Qual regula a temperatura e qual o
caudal? Para que lado é mais quente? Só se descobre experimentando, debaixo
de água.

### Os primeiros tratores e o "erro do condutor"

![](figuras/tratores_erro_condutor.png){width=50%}

*Terreno típico: sem pavimento, irregular, inclinado. O desenho original
tinha o **centro de gravidade alto** e as **rodas pouco afastadas**
(distância entre eixos curta). Os tratores capotavam. Chamava-se a isso
"erro do condutor"... mas os acidentes tornaram-se raros quando o desenho
passou a ter **centro de gravidade baixo e rodas mais afastadas**.*

Se mudar **só o desenho** (e não os condutores) fez desaparecer os
acidentes, então o erro não era do condutor: era de um desenho que
**ignorou o terreno, o centro de gravidade e a distância entre eixos**.

::: {.definicao title="--- As duas lições da psicologia dos objetos do dia a dia"}
**Lição 1: o mito do erro humano.** A maior parte das falhas dos sistemas
pessoa-máquina deve-se a:

- **desenhos fracos**, que não reconhecem as **capacidades** das pessoas
  (o que elas fazem bem, $+$), e
- às **falibilidades** das pessoas (o que elas fazem mal, $-$), que o
  desenho também não teve em conta.

É isto que dá origem a aparente "**mau uso da máquina**" e "**erro
humano**".

**Lição 2: um bom desenho tem em conta as limitações humanas.** (Lembra a
lei de Moore vs. a "lei de Darwin": as pessoas não vão mudar; é o desenho
que tem de se adaptar.)
:::

### O comando do projetor de diapositivos Leitz

O comando tem **um único botão**. Pergunta do slide: como se avança? E
como se recua? A resposta está no **manual de instruções**: **toque curto
= diapositivo seguinte; toque longo = diapositivo anterior.**

O problema: as duas funções estão no mesmo botão e **só a duração do
toque** as distingue. Nada no comando mostra que recuar existe; ninguém
adivinha a regra sem ler o manual; não se sabe **quanto tempo** é "longo";
e quem quer avançar mas segura o botão um pouco demais **recua**, e
pensa que foi ele que se enganou (lição 1). (O redesenho fica para o
exercício P.5 abaixo.)

### Funções escondidas, ontem e hoje

::: {.exemplo title="--- O telefone de escritório (anos 90) e a alavanca do limpa-vidros (2026)"}
**O telefone de escritório:** um teclado numérico com `*` e `#`. Dezenas
de funções escondidas atrás de códigos: `*72` + número = reencaminhar
todas as chamadas.

- Consigo lembrar-me do código?
- Se o marcar, como sei que funcionou?
- Como me lembro de que deixei as chamadas reencaminhadas?

**A alavanca do limpa-vidros:** uma alavanca, **sete funções**: uma
passagem, intermitente, lento, rápido, lavar, limpa-vidros de trás,
"auto". (No desenho do slide: rodar o anel = intervalo; para cima = lento,
rápido; para baixo = uma passagem; puxar = lavar; empurrar = vidro de
trás; "auto" no anel.)

- Consigo lembrar-me de qual direção faz o quê? **Muda de marca para
  marca.** Num carro japonês as alavancas estão trocadas: queres fazer
  pisca e ligas o limpa-vidros.
- Deixei-o ligado? O "auto" fica ligado, e o limpa-vidros arranca sozinho
  na estação de lavagem.

*"OK, vou ler o manual. Página 212, 'Comando do limpa e lava-vidros'. Onde
está o manual?"*
:::

**Trinta anos de diferença, as mesmas três falhas** --- uma grelha para
analisar qualquer interface (o comando Leitz acima, o relógio de ginásio
abaixo):

1. **funções que não se veem** (estão lá, mas nada na interface as
   mostra);
2. **códigos que não se conseguem lembrar** (combinações arbitrárias que
   é preciso saber de cor);
3. **um estado que não se consegue verificar** (o sistema está num modo,
   reencaminhado ou em "auto", e nada o mostra).

### As três preocupações da IPM: informação, apresentação, interação

::: {.definicao title="--- A lista de verificação da IPM"}
1. **Informação:** *que* informação mostrar ao utilizador?
   No carro: velocidade e avisos, **sempre**; pressão dos pneus, **só
   quando interessa**.
2. **Apresentação** (*display*): *como* mostrar essa informação?
   Um ponteiro mostra uma variação **num relance**; um número **tem de ser
   lido**. Vermelho **só para perigo**.
3. **Interação:** *como* manipular e interagir com a informação?
   Um botão rotativo de volume encontra-se **pelo tato** a 120 km/h; um menu
   num ecrã tátil não.

O professor pede para usar esta lista **em cada painel do trabalho
prático**.
:::

**Pergunta para a turma (slide 19):** a partir de janeiro de 2026, o Euro
NCAP (o programa europeu que classifica a segurança dos carros) tira pontos
aos carros que põem os piscas, o limpa-vidros, a buzina, os quatro piscas
e a chamada SOS num ecrã tátil. O que correu mal, em termos de IPM? (É a
alínea (a) do exercício P.5, abaixo.)

::: {.exemplo title="--- O relógio de ginásio pela lista de verificação (slide 20)"}
O relógio do slide tem um ecrã LCD com três linhas e **quatro botões**
(na foto leem-se "LIGHT" e "SET" nos botões de um lado). Funções:

- hora (horas, minutos, segundos); data (ano, mês, dia, dia da semana);
- luz;
- cronómetro: iniciar, parar, *reset*;
- alarme: acertar a hora, ligar/desligar;
- Hora 1 e Hora 2 (dois fusos);
- acertar a data (A/M/D); acertar a hora (H:M).

**Contar as ações.** Ver hora, ver data, luz, iniciar, parar, *reset*,
acertar o alarme, ligar/desligar o alarme, trocar Hora 1/Hora 2, acertar
o ano, o mês, o dia, a hora e os minutos: são **14 ações** (sem contar
"subir" e "descer" um valor ao acertar). Com 4 botões, cada botão tem de
fazer, em média, $14/4 = 3{,}5$ coisas. Isto só se consegue com
**modos** (o mesmo botão faz coisas diferentes consoante o modo) e com
**toques longos ou combinações** de botões.

**Informação.** O ecrã mostra hora, data e dia da semana ao mesmo tempo
("9:42 41", "Yr 16", "FRI 02 1"), mais pequenos indicadores ("TIME",
"HRM"). O modo atual aparece em letras minúsculas num canto: é a
informação mais importante para saber o que cada botão faz, e é a menos
visível.

**Apresentação.** Algarismos de 7 segmentos, legíveis para a hora, mas as
abreviaturas ("Yr", "FRI") e os indicadores pequenos têm de ser **lidos**
com atenção, o que é difícil a meio de um treino.

**Interação.** É aqui que falha, e com as três falhas da secção anterior:

1. **funções que não se veem:** nada no relógio diz que o *reset* existe
   nem onde está (por isso "ninguém encontra o *reset*", slide 11);
2. **códigos que não se lembram:** os toques longos e as combinações de
   que falámos acima (do género "segurar SET uns segundos para acertar" ou
   "carregar em dois botões ao mesmo tempo"; o slide não diz quais são as
   deste relógio) são códigos tão arbitrários como o `*72` do telefone;
3. **estado que não se verifica:** em que modo estou? O alarme está
   ligado? A Hora 2 está ativa? Só um ícone minúsculo, ou nada.

**Conclusão:** é o compromisso "simples vs. completo" a correr mal (o
quarto assunto da IPM): o relógio ficou **completo** e perdeu o
**simples**, e o custo vai todo para a pessoa.
:::

### A psicologia dos objetos do dia a dia: conclusão

- Muitos dos chamados "erros humanos" e "mau uso da máquina" são, na
  verdade, **erros de desenho**.
- Quem desenha ajuda as coisas a funcionar dando-lhes um **bom modelo
  conceptual** (Aula 2, T3: funcionalidade, modelo conceptual e imagem do
  sistema).
- Quem desenha decide um conjunto de utilizadores como **público** do
  desenho: **as personas** (Aula 2).
- Mas **desenhar é difícil**, por muitas razões que vão além do desenho
  (custos, prazos, tecnologia, interesses dos stakeholders: o triângulo
  mágico da Aula 2).
- **É preciso experimentar e testar várias vezes!** (O ciclo de desenho
  iterativo, Aula 2.)

O slide ilustra com **portas com uma placa "PUSH"** (empurrar): uma tem um
puxador vertical, a outra uma pega. Uma pega convida a **puxar**; se a
porta abre a empurrar, a placa é um remendo para um erro de desenho. Pela
lição 1, quem puxa a porta não se enganou: foi a porta que lhe disse para
puxar.

**Portas de Norman†** (do livro de Norman, não está nos slides): Norman
chama **sinalizador** (*signifier*) a qualquer sinal que diz à pessoa que
ação é possível e onde; a forma da pega é um sinalizador (diz "puxa").
Quando a forma contradiz a ação real, nenhuma placa resolve bem o
problema, porque as pessoas reagem à forma antes de lerem a placa.

::: {.pratica title="--- Analisar interfaces que falham"}
**Exercício P.5** (perguntas dos slides do Módulo 04 e inventadas a partir
deles).

**(a)** A pergunta do slide 19: o Euro NCAP tira pontos, desde janeiro de
2026, aos carros que põem piscas, limpa-vidros, buzina, quatro piscas e
chamada SOS num ecrã tátil. O que correu mal em termos de IPM? Usa a lista
**informação / apresentação / interação** e as **três falhas** das
funções escondidas.

**(b)** O comando do projetor Leitz (um botão; toque curto avança, toque
longo recua). Diagnostica-o com as três falhas e propõe um redesenho que as
resolva, justificado pela lista de verificação.

**(c)** A porta com puxador e placa "PUSH". Porque precisa da placa? De
quem é a culpa quando alguém puxa (lição 1)? Que mudança de desenho torna
a placa desnecessária?
:::

## Esboçar: onde ficou o quarto tópico

O quarto tópico do Módulo 04 (*Sketching*, adaptado de *Sketching User
Experiences*) abre com *"We want you to fail fast"*: **os esboços tornam o
falhar barato**, que é exatamente o que este tópico pede depois de se ver
como as interfaces falham. Como aprofunda a secção "Esboçar" da Aula 2, o
conteúdo foi fundido lá:

| Conteúdo do Módulo 04 | Onde está neste resumo |
|------------------------------------|----------------------------------------|
| "Falhar depressa", porquê desenhos maus | Aula 2, "Esboçar", "Porque esboçar?" |
| A visão de produto (desenho, engenharia, vendas) | Aula 2, "O funil de desenho" |
| Atributos de um esboço (1), (2) e (3); detalhe mínimo, refinamento, abertura | Aula 2, "Os atributos de um esboço" |
| Esboço vs. protótipo; propriedades; do desenho inicial ao final | Aula 2, "Um esboço não é um protótipo" |
| Esboço vs. maqueta gerada por IA; regra da disciplina | Aula 2, "Um esboço vs. uma maqueta gerada por IA" (e Aula 1, regras de IA) |
| O caderno de esboços: para quê, instrumentos, boas práticas, exemplos | Aula 2, "O caderno de esboços" |

# Aula 5 --- Modelos mentais e cognição

O Módulo 05 (7 out 2026) explica **como as pessoas descobrem como as
coisas funcionam, e porque se enganam**. Tem quatro tópicos: porquê estudar
a cognição; modelos mentais; as sete fases de ação de Norman e os dois
golfos; e a cognição fora da cabeça.

## Porquê estudar a cognição

**Agimos sobre um modelo de como a coisa funciona, não sobre a coisa.** A
pergunta de abertura (está frio, pões o termóstato a 30 °C para aquecer
mais depressa; aquece?) e mais duas situações mostram-no:

| O que fazes | O que acreditas (o teu modelo) | O que acontece de facto |
|:---------------|:----------------------|:-----------------------------|
| Pões o termóstato a 30 °C | "Quanto mais alto, mais força faz a aquecer." | A maioria dos termóstatos é um interruptor: a caldeira trabalha no máximo até ao valor pedido e depois para. 30 °C só faz com que pare **mais tarde**. |
| Carregas três vezes no botão da passadeira | "Cada toque é um pedido; mais toques, verde mais cedo." | Ciclos fixos; muitos botões nem estão ligados (em 2004, cerca de 2500 dos 3250 de Nova Iorque não faziam nada). |
| Reinicias o portátil lento | "Reiniciar limpa o que quer que esteja mal." | Muitas vezes resulta, mas por outra razão. Os sucessos reforçam um modelo que também leva as pessoas a reiniciar o projetor. |

**Porquê um quadro teórico da cognição:** os modelos teóricos têm **poder
preditivo e explicativo** (dizem o que o utilizador vai tentar e porque
falhou), e podem-se **aproveitar teorias** da psicologia e da ergonomia em
vez de adivinhar. O módulo usa dois grupos de quadros:

- **Internos (dentro da cabeça):** os **modelos mentais** (a ideia que o
  utilizador tem de como a coisa funciona); os **golfos da execução e da
  avaliação** (Norman); o **processamento de informação** (o humano como
  um processador com etapas).
- **Externos (fora da cabeça):** a **cognição distribuída** (entre
  pessoas, artefactos e tempo); a **cognição externa** (usar o mundo para
  pensar: notas, mapas, post-its); a **interação incorporada** (o corpo e
  o contexto social dão significado).

No COL, o operador **já tem um modelo do rio**. Os painéis ou encaixam
nele ou têm de o corrigir de forma visível; ignorá-lo não é opção.

## Modelos mentais

::: {.definicao title="--- Modelo mental"}
*"Ao interagir com o ambiente, com os outros e com os artefactos da
tecnologia, as pessoas formam modelos mentais internos de si próprias e
das coisas com que interagem"* (Norman, 1983).

As pessoas usam o modelo mental para:

- **raciocinar** sobre um sistema: como funciona e como interagir com
  ele;
- **reagir** a uma situação: descobrir o que fazer quando algo corre mal.
:::

**O mesmo sintoma, dois modelos, duas ações.** O Wi-Fi está lento.
Modelo A: "o *router* cansa-se" → reinicia o *router*. Modelo B: "os
vizinhos estão no mesmo canal" → muda de canal. **O modelo nunca se vê; só
se veem as ações que ele produz.** A interface é o único sítio onde se pode
corrigir.

De onde vem o modelo do utilizador (o **modelo do desenhador**, a
**imagem do sistema** e o **modelo do utilizador**, ligados por um só
canal) está na Aula 2, T3. Aqui fica o que alimenta esse canal.

### Os sete conceitos que informam o modelo mental

::: {.definicao title="--- Sete conceitos de desenho"}
| Conceito | Pergunta que responde | Exemplo |
|:------------|:-----------------|:-------------------------------------|
| **Visibilidade** | Consigo ver o estado e os comandos? | O nível de combustível vê-se; a bateria de um rato sem fios não, até acabar. |
| **Affordance** | O que é que o objeto "oferece" para se fazer com ele? | Uma pega convida a puxar, uma placa lisa a empurrar (as portas de Norman, Aula 4). |
| **Mapeamento** (*mapping*) | Que relação há entre os comandos e os efeitos? | Quatro bicos num quadrado, quatro botões em linha: qual é qual? |
| **Restrições** (*constraints*) | O que é que **não** se pode fazer? | A USB-C entra dos dois lados; a USB-A precisava de três tentativas. Uma comporta não abre mais de 100 %. |
| **Efeitos de transferência** | O que traz o uso de objetos parecidos? | Todos os telemóveis põem o "voltar" no mesmo lado; muda-se e o utilizador desliza para o vazio. |
| **Associações culturais** | O que já significa isto nesta cultura? | Vermelho = parar ou perigo; nas bolsas chinesas, vermelho = o preço subiu. |
| **Feedback** | O que me diz o que acabou de acontecer? | O clique da tecla, o apito do multibanco, o ícone a rodar. Feedback atrasado = segundo toque. |
:::

Os sete informam o modelo mental, mas **nenhum é o mecanismo**: todos são
**imagem do sistema**. (O *sinalizador*† da Aula 4 é a parte visível de
uma *affordance*: diz onde e como agir.) A transferência pode ser
**positiva** (o que se sabe de objetos parecidos ajuda) ou **negativa**†
(atrapalha, como as alavancas trocadas dos carros japoneses).

::: {.exemplo title="--- Formar um modelo só de olhar: a tesoura"}
- **Affordance:** serve para cortar... e pode magoar, se não for usada
  com cuidado.
- **Mapeamento:** os buracos sugerem onde vão os dedos.
- **Restrições:** a forma dos buracos limita os dedos: o buraco grande é
  para vários dedos, o pequeno para o polegar.
- **Transferência positiva e idioma cultural:** usa-se desde a infância e
  o mecanismo nunca mudou.
- **Modelo mental:** o objeto físico mostra como funcionam as partes que
  se mexem.

O modelo não é perfeito: pode um canhoto usá-la? (É o exercício P.6(b).)
:::

**Objetos que mentem** (atividade, 2 min, com o *Catálogo de objetos
introuváveis* de Jacques Carelman, 1969): cada objeto promete alguma coisa;
diz o que promete e onde a promessa falha. É o mesmo exercício que a
tesoura, ao contrário: a imagem do sistema contradiz o mecanismo.

### Os modelos são executáveis e imperfeitos

**Desenhar uma bicicleta** (atividade): quatro voluntários (dois que não
andam de bicicleta há cinco anos, dois que andam muitas vezes) desenham de
memória, em três minutos, uma bicicleta que funcione (quadro, pedais,
corrente, rodas, direção), e a turma julga: andaria? viraria? Cerca de
**40 %** dos adultos faz um erro básico: a corrente na roda da frente
(então não podia virar) ou um tubo do quadro a unir as duas rodas. Quem
anda de bicicleta faz só um pouco melhor (Lawson, 2006). Antes de desenhar,
todos estavam confiantes: é a **ilusão de profundidade explicativa**
(Rozenblit e Keil, 2002). **Os modelos mentais são incompletos, e só o
descobrimos quando os pomos a correr.**

**"Quem vai ser derrubado?"** (atividade, 1 min): um desenho com cinco
bonecos (A a E) numa pista com uma bola, uma rampa, uma balança e um
gancho; vota-se quem cai. Ao responder, **correu-se um modelo de física
na cabeça e previu-se um resultado sem tocar em nada**. É o que os
utilizadores fazem com cada interface, antes de cada clique.

::: {.definicao title="--- Modelos executáveis e características dos modelos mentais"}
**Executável** (*runnable*): o utilizador mexe no sistema para perceber
como funciona e constrói uma noção de causalidade, "fazer isto dá aquilo".
Depois o modelo corre em dois sentidos:

- **Previsão:** o que acontece se eu fizer isto? Que ação escolho? (O lado
  da **intenção**, ou execução, das sete fases.)
- **Explicação:** porque é que o sistema respondeu assim? (O lado da
  **avaliação** das sete fases.)

Cada clique é **precedido de uma previsão** e **seguido de uma
explicação**.

**Características** (Norman, 1983). Os modelos mentais são:

1. **incompletos** (a corrente na roda da frente);
2. **instáveis** (esquecem-se detalhes; o modelo evolui com o uso);
3. **pouco exatos** (o frigorífico, abaixo);
4. **simplificados** (um fenómeno complexo reduzido ao que cabe numa
   cabeça);
5. **supersticiosos** (o termóstato a 30 °C, o botão da passadeira);
6. **expressáveis em regras se-então** ("se eu carregar aqui, então aquilo
   acende").
:::

::: {.pratica title="--- Modelos mentais"}
**Exercício P.6** (perguntas dos slides do Módulo 05 e inventadas a partir
deles). Técnica: os sete conceitos e as características dos modelos
mentais.

**(a)** Para o termóstato a 30 °C, o botão da passadeira e o portátil
reiniciado: que característica do modelo mental mostra cada um? Para o
termóstato e para a passadeira, que conceito de desenho, aplicado à imagem
do sistema, corrigia o modelo? (Pista: o que é que o utilizador não vê?)

**(b)** A pergunta do slide: um canhoto pode usar a tesoura? Diz que
partes do modelo "de olhar" continuam certas e qual falha, e porquê.

**(c)** No COL, uma comporta de Touvedo leva três minutos a chegar à
abertura pedida. Se o painel só mostrar o valor pedido, que modelo
constrói o operador e que característica dos modelos mentais aparece? Que
conceito de desenho evita um segundo comando?

**(d)** O Wi-Fi lento: escreve a regra se-então de cada modelo (A e B) e
diz o que a aplicação do *router* teria de mostrar para corrigir o
modelo A.
:::

## As sete fases de ação de Norman e os dois golfos

### As sete fases

As sete fases descrevem **uma ação humana orientada a um objetivo**
(Norman, *The Design of Everyday Things*, 1988 e 2013). Pelo lado
esquerdo **faz-se** (execução: a descer, fases 2--4, atravessa-se o golfo
da execução); pelo lado direito **verifica-se** (avaliação: a subir, fases
5--7, o golfo da avaliação).

::: center
![](figuras/sete_fases_norman.pdf){width=60%}
:::

::: {.definicao title="--- As sete fases e as perguntas do utilizador"}
| Fase | Lado | Pergunta que o utilizador faz |
|:-----------------------------|:----------|:--------------------------|
| 1 Objetivo (estabelecer o objetivo) | --- | O que quero fazer? |
| 2 Intenção de agir | execução | Acho que se pode fazer. Como? |
| 3 Sequência de ações | execução | Para isso, faço isto, depois isto... |
| 4 Execução da sequência | execução | (a mão mexe-se) |
| 5 Perceção do estado do mundo | avaliação | O que estou a ver agora? |
| 6 Interpretação da perceção | avaliação | O que é que o sistema acabou de fazer? |
| 7 Avaliação da interpretação | avaliação | Era isto que eu queria? (verifico o modelo mental) |

O ***cognitive walkthrough*** (Aula 6) agrupa estas fases em quatro
perguntas, feitas no papel aos esboços de outro grupo (Fase 1).
:::

::: {.exemplo title="--- As sete fases no COL: uma missão (slide 19)"}
Missão: **subir a descarga de Touvedo de 80 para 120 m³/s** (o total fica
abaixo de 300 m³/s, por isso o operador decide sozinho).

| Fase | O que o operador faz | O que o painel tem de oferecer |
|:---------|:--------------------|:----------------------------------|
| 1 Objetivo | Subir Touvedo de 80 para 120 m³/s | A missão visível na parede, com o valor atual ao lado |
| 2 Intenção | "Uso os comandos das comportas de Touvedo" | **Visibilidade:** os comandos existem e vê-se onde estão |
| 3 Sequência | Escolher Touvedo, escolher a comporta, pôr 120, confirmar | Cada passo visível. **Restrições:** não há maneira de escrever 1200 |
| 4 Execução | Arrastar o cursor, ou escrever, ou rodar um botão | **Affordance:** o comando parece o que faz |
| 5 Perceção | Algo muda no ecrã | **Feedback** em menos de uma décima de segundo (Módulo 09), mesmo que a comporta leve minutos |
| 6 Interpretação | "A comporta está a abrir, o caudal vai subir" | Mostrar **comando e estado em separado**: pedido 120, atual 92 |
| 7 Avaliação | "Cheguei a 120? O nível a jusante está a subir como esperado?" | O gráfico, com a linha do alvo, e o tempo previsto até lá chegar |

A terceira coluna é a **primeira lista de verificação** dos painéis. É
também assim que o *walkthrough* da Fase 1 vai ler os esboços.
:::

### Os dois golfos

::: {.definicao title="--- Golfo da execução e golfo da avaliação"}
- **Golfo da execução** ("como é que o faço?"): a distância entre o que
  quero e as ações que o sistema oferece. Ex.: o comando do projetor com
  dois botões (Aula 4); um comando de comporta enterrado num submenu.
- **Golfo da avaliação** ("o que aconteceu?"): o esforço de perceber o
  estado do sistema a partir do que ele mostra. Ex.: o botão da passadeira
  sem luz; "A guardar..." sem progresso; uma comporta que leva três
  minutos e não mostra nada.

O desenho atravessa os dois golfos com **comandos que correspondem às
intenções** e **mostradores que respondem às perguntas** (Norman, em *User
Centered System Design*, 1986).
:::

O golfo da execução cobre as fases 2--4; o da avaliação, as fases 5--7.
Os sete conceitos encaixam aqui: visibilidade, *affordance*, mapeamento,
restrições e transferência estreitam sobretudo o golfo da execução;
*feedback* e visibilidade do estado estreitam o da avaliação†.

### Quando se aplicam as sete fases

- **Servem melhor para a aprendizagem exploratória:** primeiro uso, ou uma
  situação nova. O utilizador não tem expectativas fortes, por isso cada
  fase é consciente e pode falhar (o primeiro dia no COL, a primeira
  cheia).
- **Servem menos para comportamento automático:** tarefas muito
  aprendidas, semiautomáticas. O utilizador já espera o que vai acontecer
  e as fases encolhem em ciclos minúsculos e rápidos (conduzir para o
  trabalho; uma terça-feira normal no COL).
- ...**a não ser que aconteça algo inesperado**: então as sete fases voltam
  por inteiro (o aviso de pouco combustível na autoestrada, o primeiro
  alarme de uma noite de cheia). O mesmo ecrã tem de servir os dois dias
  (a "variabilidade" da Aula 4).

**Consequência para o método:** o *cognitive walkthrough* (Aula 6)
avalia o **primeiro uso**, fase a fase; os **testes de usabilidade**
(Módulo 11) olham para o uso repetido e para o tempo.

::: {.exemplo title="--- O frigorífico (Norman)"}
O painel tem dois controlos, um com a etiqueta **FREEZER** (congelador) e
outro **FRESH FOOD** (frigorífico), uma tabela de combinações e uma
instrução: acertar os dois e esperar 24 horas para estabilizar. Pergunta:
o congelador está demasiado quente e o frigorífico está bem. O que se
muda?

![](figuras/frigorifico_modelos.pdf){width=92%}

**O modelo do utilizador:** duas unidades independentes, cada controlo com
a sua unidade de frio. Resposta "óbvia": rodar só o controlo FREEZER.

**O modelo real:** há **uma só unidade de frio**. O controlo A (etiqueta
FREEZER) regula o compressor, isto é, a quantidade de frio total; o
controlo B (etiqueta FRESH FOOD) regula uma válvula que **divide** o ar
frio entre os dois compartimentos. Mudar qualquer um muda **os dois**
compartimentos, e **nada no painel o diz**.

**Os dois golfos de uma vez.** Execução: que botão, e quanto? Avaliação:
só se sabe daqui a 24 horas. **Não é erro do utilizador: o desenhador
escondeu o mecanismo.**
:::

::: {.pratica title="--- As sete fases e os dois golfos"}
**Exercício P.7** (inventado a partir do Módulo 05 e do enunciado do COL).
Técnica: as sete fases, os dois golfos e os sete conceitos.

**(a)** Faz a tabela das sete fases (fase, o que o operador faz, o que o
painel tem de oferecer) para a missão "**abrir a descarga de fundo de
Touvedo**", com o total largado a ficar abaixo de 300 m³/s. Usa os
estados obrigatórios da descarga de fundo (Aula 1).

**(b)** Diz se cada caso é sobretudo um problema do golfo da execução ou
do da avaliação, e o que o atravessa: **(1)** o comando Leitz (um botão,
toque longo recua); **(2)** o `*72` do telefone de escritório (ver se o
reencaminhamento ficou ligado); **(3)** "A guardar..." sem progresso;
**(4)** quatro bicos num quadrado e quatro botões em linha.

**(c)** O frigorífico: com o modelo real, o que se muda para arrefecer o
congelador sem estragar o frigorífico? Propõe um redesenho do painel que
estreite os dois golfos.

**(d)** Porque é que o *walkthrough* avalia o primeiro uso? Dá um
elemento de um painel do COL que sirva ao mesmo tempo uma terça-feira
normal e a primeira noite de cheia.
:::

## Processamento de informação e carga

### O processamento de informação

O terceiro quadro interno vê o **humano como um processador de
informação**:

![](figuras/processamento_informacao.pdf){width=100%}

- Há **etapas ordenadas**, cada uma com entrada e saída.
- Dentro de cada etapa, há processos (comparar, emparelhar) que **atuam
  sobre representações mentais**.
- **Serve para fazer previsões e encontrar estrangulamentos**: como se
  verifica que foi feito? Qual é a capacidade?

Leva ao **Model Human Processor**: perceção, cognição e ação motora como
**três processadores**, cada um com memórias e tempos de ciclo (os números
ficam para o Módulo 09). (A pergunta "a computação é mudança de estado; a
cognição será uma série de mudanças de estado?" é, segundo o slide, para o
café e não para o exame.)

### Carga cognitiva e carga atencional

::: {.definicao title="--- Carga, carga cognitiva e carga atencional"}
- **Carga:** a quantidade de recursos mentais que é precisa para
  processar informação.
- **Carga cognitiva:** quanto "poder cerebral" uma tarefa gasta: perceber,
  decidir, calcular. Ex.: um slide denso; uma decisão de descarga numa
  noite de cheia.
- **Carga atencional:** quanta atenção uma tarefa gasta: vigiar, reparar,
  manter-se nela. Ex.: duas horas de aula; doze ecrãs numa parede o dia
  todo.
:::

A pergunta do slide (o que custa mais, seguir duas horas de aula ou
perceber um slide denso?) não tem resposta única porque **não são o mesmo
tipo de custo**: as duas horas gastam sobretudo atenção; o slide gasta
sobretudo cognição.

**Regra de desenho:** manter **baixa a carga atencional da parede** (poucas
coisas mexem, poucas piscam), para que a capacidade cognitiva do operador
esteja intacta quando chegar a decisão. O Módulo 09 põe números nas duas.

::: {.pratica title="--- Processamento de informação e carga"}
**Exercício P.8** (inventado a partir do Módulo 05). Técnica: as etapas do
processamento de informação e os dois tipos de carga.

**(a)** Diz se cada tarefa pesa sobretudo na carga cognitiva ou na
atencional: **(1)** vigiar a parede de 12 ecrãs durante um turno de 8
horas sem incidentes; **(2)** decidir quanto largar em Touvedo com o nível
a subir em dois troços; **(3)** encontrar um alarme novo entre vários
indicadores a piscar; **(4)** ler uma tabela com 30 valores de sensores
para escolher o troço mais crítico.

**(b)** Percorre as seis etapas do processamento de informação para "o
operador vê um alarme novo na parede e reconhece-o". Em que etapa está o
estrangulamento mais provável às 3 da manhã, e que decisão de desenho o
alivia?
:::

## Cognição fora da cabeça

### Três quadros externos

::: {.definicao title="--- Cognição distribuída, externa e incorporada"}
| Quadro | O que diz | Exemplo |
|:------------|:-------------------------|:-------------------------|
| **Cognição distribuída** | A cognição acontece entre pessoas, artefactos e tempo. A unidade é a tripulação, a sala de controlo, a equipa, não uma cabeça. | O *cockpit*: a altitude vive na chamada de rádio, no mostrador, nas mãos do piloto e no olhar do comandante. |
| **Cognição externa** | Usar representações externas (livros, mapas, diagramas, listas, post-its) para trabalhar com as internas. | Uma lista de compras; um quadro branco; a multiplicação longa que não se consegue fazer de cabeça. |
| **Interação incorporada** (*embodied*) | O significado forma-se pela interação física e social com o mundo. | Apontar para a parede para que todos vejam o que tu vês; parar num dado momento para pensar e para que os outros te vejam. |
:::

### Cognição distribuída: como um *cockpit* se lembra

Hutchins (*How a cockpit remembers its speeds*, 1995) descreve a
**propagação de estados representacionais**: a mesma informação ("subir
para a altitude X") passa por vários meios.

| Passo | O que acontece | Meio |
|:-:|:--------------------------------------------|:------------------|
| 1 | O controlo aéreo autoriza a subida para uma altitude maior | verbal |
| 2 | O piloto muda o indicador de altitude | mental e físico |
| 3 | O comandante observa o piloto | visual |
| 4 | O comandante sobe para a nova altitude | mental e físico |

A cognição distribuída estuda:

- como as pessoas **trabalham juntas** para resolver um problema e como o
  conhecimento é **partilhado e acedido**;
- o comportamento **verbal e não verbal**: o que não se diz fica implícito
  em olhares e gestos;
- os **mecanismos de coordenação**: regras, procedimentos, listas de
  verificação.

No COL: **onde fica guardada a última ordem de descarga?** Na cabeça do
operador, no ecrã, no registo, na chamada para Touvedo? **É a interface
que decide.**

### Cognição externa: três mecanismos

::: {.definicao title="--- Os três mecanismos da cognição externa"}
1. **Externalizar para reduzir a carga de memória:** diários, calendários,
   listas de tarefas, alarmes. Lembram *que* é preciso fazer algo, *o quê*
   e *quando*.
2. **Descarga computacional** (*computational offloading*): uma ferramenta
   mais uma representação faz parte da conta por nós.
3. **Anotação e rastreio cognitivo:** anotar é riscar itens, sublinhar,
   circundar; rastrear é mudar itens de ordem ou de monte, como uma parede
   de post-its.
:::

**Experimenta (30 s):** $3 \times 2$ de cabeça; $234 \times 456$ de
cabeça; $234 \times 456$ em papel; com calculadora; e
$\text{CCXXXIV} \times \text{CDLVI}$ em papel. É **o mesmo problema** com
**quatro dificuldades diferentes**: **a representação muda a tarefa**.

**O projeto vive de representações externas:** os post-its de três cores
da S4 (expandir e depois contrair), os *storyboards* da S5 e o caderno de
esboços o semestre todo. Não são papelada: é onde o grupo pensa, onde está
a sua memória, e o que o *walkthrough* da Fase 1 vai ler. Um grupo cujas
ideias só estão nas cabeças não tem um modelo partilhado. **A parede é o
modelo.**

### Interação incorporada

**Perceber a interação como envolvimento prático num ambiente social e
físico** (Dourish, *Where the Action Is*, 2001). Nasceu de observar como
as pessoas fazem as coisas em situações reais, não no laboratório.

- **A qualidade emocional das interações:** um aparelho que parece hostil
  usa-se menos e pior (o relógio de ginásio da Aula 4).
- **Ações públicas em espaços partilhados:** quando o operador se levanta
  e aponta para a parede, a sala toda percebe que se passa alguma coisa.
- **O corpo faz a mediação da interação:** um grande botão vermelho e uma
  opção de menu fazem a mesma coisa, mas **não são a mesma ação** (o
  Kinect, Aula 4).

No COL, **a parede é pública e os dois ecrãs são privados**. Decide o que
vai para cada lado: o que é que a sala inteira tem de ver de uma vez, e o
que é só assunto de um operador?

::: {.pratica title="--- Cognição fora da cabeça"}
**Exercício P.9** (inventado a partir do Módulo 05 e do enunciado do COL).
Técnica: os três quadros externos.

**(a)** À maneira do *cockpit*, escreve a propagação de estados
representacionais de uma descarga em Touvedo que **precisa de
autorização** (vai passar de 280 para 420 m³/s): passos, o que acontece e
o meio. No fim, diz onde fica guardada a ordem.

**(b)** Faz $234 \times 456$ em papel, mostrando as parcelas. Explica, com
a descarga computacional, porque é que $\text{CCXXXIV} \times
\text{CDLVI}$ é muito mais difícil, se o problema é o mesmo.

**(c)** Para cada elemento, diz se vai para a parede (pública) ou para os
ecrãs (privados) e porquê: **(1)** o estado de alerta dos troços do rio;
**(2)** o rascunho de um aviso público ainda por enviar; **(3)** uma
manobra à espera de autorização; **(4)** o formulário para enviar uma
equipa.
:::

## Onde ficou cada parte do Módulo 05

| Conteúdo do Módulo 05 | Onde está neste resumo |
|------------------------------------|----------------------------------------|
| Três modelos (desenhador, imagem do sistema, utilizador) e um só canal | Aula 2, T3, "Desenho conceptual" |
| Tudo o resto | Esta aula |


# Aula 6 --- O *cognitive walkthrough*

## Porquê avaliar um esboço

Cada fase do projeto avalia um artefacto mais acabado, e **corrigir um
problema fica mais caro de fase para fase**:

| Fase | Método | Sessão | Corrigir um problema custa |
|:-:|:------------------|:-----------|:------------------|
| 1 | *Cognitive walkthrough* sobre os **esboços** | S6 (esta aula) | redesenhar: minutos |
| 2 | Avaliação heurística sobre os ***wireframes*** | S8 (Módulo 10) | uma hora no Figma |
| 3 | Testes de usabilidade sobre o **protótipo** | S9, com 5 pessoas de fora (Módulo 11) | um dia |

Os **métodos de inspeção** (um avaliador examina a interface, sem
utilizadores reais) encontram **30 a 90 %** dos problemas que os testes
com utilizadores encontram. Um avaliador sozinho encontra cerca de **um
terço**, por isso a Fase 1 usa **dois ou três avaliadores por esboço**.
Não há laboratório nem recrutamento: custa horas, não uma semana.

## O que é o *cognitive walkthrough*

::: {.definicao title="--- Cognitive walkthrough"}
Um avaliador **que não desenhou a interface** simula um **utilizador de
primeira vez** a fazer **uma tarefa**, **um passo de cada vez**, sobre o
esboço, e pergunta em cada passo: **este utilizador saberia o que fazer?**
E **perceberia o que aconteceu?**

| Quem o faz | O que encontra | O que não encontra |
|:----------------------|:----------------------|:----------------------|
| Pessoas **com distância** do desenho (outro grupo, um colega, um analista de fora). Quanto mais distância, mais veem: não sabem o que o desenhador "queria dizer". Não é preciso serem peritos; 2 ou 3 por esboço | Confusão, becos sem saída, *feedback* em falta, etiquetas erradas, **passos que ninguém desenhou** (escrever a sequência correta de ações expõe ecrãs que faltam). Encontra-os passo a passo, não por impressão geral | **Rapidez** e os **erros de quem já está treinado** (precisam de utilizadores reais, Módulo 11). Só vê **as tarefas escolhidas**: escolhem-se as três missões que importam. Cada avaliador encontra parte dos problemas, com alguns **falsos alarmes** |
:::

**Porquê o primeiro uso.** Na Aula 5, as sete fases de Norman só são
**todas conscientes** na fase exploratória (primeiro uso, situação
inesperada); no uso automático encolhem. O *walkthrough* avalia
exatamente essa fase, por isso pode pôr uma pergunta a cada fase. A
primeira semana de um operador no COL, com uma interface nova, é o caso
típico.

## As quatro perguntas

Em cada passo da sequência correta, o avaliador responde **sim ou não** a
quatro perguntas (Wharton, Rieman, Lewis e Polson), **sempre com a
razão**:

![](figuras/cw_quatro_perguntas.pdf){width=72%}

*Cada pergunta verifica um grupo de fases de Norman; a fase 3 entra em Q2
(ver a ação) e em Q3 (percebê-la).*

| | Pergunta | Fases | Falha típica (slides) |
|:-:|:----------------|:------------|:----------------------------|
| **Q1** | O utilizador vai tentar atingir o **efeito certo**? | 1--2, objetivo e intenção | Botão START que não faz nada sem carregar no travão: ninguém sabe que esse passo existe, ninguém o tenta |
| **Q2** | Vai **reparar que a ação certa está disponível**? | 3, sequência (visibilidade) | "Rejeitar tudo" escondido atrás de "Gerir preferências" num aviso de *cookies*: a ação existe e ninguém a vê |
| **Q3** | Vai **associar a ação certa ao efeito** que quer? | 3--4, etiquetas e mapeamento | Quatro bicos de fogão e quatro botões em linha: qual aquece qual? |
| **Q4** | Depois de a fazer, **vê que está a progredir**? | 5--7, *feedback* e avaliação | O botão do elevador que não acende: toda a gente carrega três vezes |

**Versão curta (Spencer)**, para quando falta tempo, com duas perguntas:
"o utilizador vai saber o que fazer neste passo?" (Q1--Q3) e "se fizer a
coisa certa, vai saber que a fez e que está a progredir?" (Q4).

**Um "sim" também precisa de razão:** o que, no esboço, faz o utilizador
acertar? "Ele saberia" não é evidência. **Se não consegues apontar para
nada no esboço, a resposta é não.**

::: {.definicao title="--- Escala de severidade (Nielsen)"}
Cada "não" é um problema, com uma severidade (a mesma escala volta na
Fase 2):

| 0 | 1 | 2 | 3 | 4 |
|:-:|:-:|:-:|:-:|:-:|
| não é problema de usabilidade | cosmético | menor | **maior**: importante corrigir | **catástrofe**: bloqueia a tarefa |
:::

**O resultado é uma tabela**, uma linha por passo: o passo, Q1 a Q4
(sim/não), a razão de cada "não" e a severidade.

## Exemplo do módulo: o Tiago em Touvedo

::: {.exemplo title="--- O caso: persona, missão, sequência correta e esboço"}
**Persona:** Tiago, operador do COL, **primeira semana** na interface nova.
Treinado no sistema antigo: conhece o rio e as comportas, não estes
ecrãs.

**Missão** (a da Aula 5): subir a descarga de Touvedo de **80 para 120
m³/s** (fica abaixo de 300 m³/s, decide sozinho).

**Sequência correta**, escrita pelo grupo que desenhou: **1** selecionar
Touvedo no mapa do rio; **2** encontrar os comandos das comportas no
painel; **3** escrever 120 no campo do caudal; **4** verificar Ponte da
Barca antes de confirmar; **5** confirmar a ordem.

![](figuras/cw_esboco_touvedo.pdf){width=85%}

*Esboço hipotético do painel de comportas (monitor 1 de 2). "Setpoint
(%)" é a abertura da comporta, em percentagem; os valores parecem todos
iguais, só de leitura.*
:::

::: {.exemplo title="--- O walkthrough, passos 1 a 3"}
| Passo | Q | Resp. | Razão (o que está no esboço) |
|:-------------|:-:|:-:|:------------------------------------------|
| **1** Selecionar Touvedo | Q1 | sim | A missão diz Touvedo, e o Tiago sabe que a descarga se muda lá |
| | Q2 | sim | O mapa é a primeira coisa no ecrã e Touvedo está nele |
| | Q3 | sim | Uma barragem num mapa: tocar-lhe abre a barragem. O sistema antigo era igual |
| | Q4 | sim | Touvedo fica realçado e o cabeçalho diz "Barragem de Touvedo" |
| **2** Encontrar os comandos | Q1 | sim | Sabe que a descarga se muda nas comportas |
| | Q2 | **não** | Os *setpoints* são números simples, no mesmo estilo dos valores só de leitura à volta. Nada mostra que se podem editar |
| | Q3 | sim | Quando toca num, a etiqueta "Setpoint" diz o que é |
| | Q4 | sim | Aparece um cursor e o número pode ser mudado |
| **3** Escrever 120 | Q1 | sim | Quer 120 m³/s e procura onde o escrever |
| | Q2 | sim | Há um só campo editável no painel |
| | Q3 | **não** | O campo diz "Setpoint (%)": abertura em percentagem. O Tiago quer m³/s e não sabe a curva abertura → caudal |
| | Q4 | sim | O valor escrito aparece no campo (mas ver o passo 5) |

- **Passo 1:** nenhum problema. O mapa, o realce e o cabeçalho são a razão
  do sucesso.
- **Passo 2 (Q2), severidade 3, maior:** **um comando que parece um
  mostrador**. O Tiago lê o painel e não vê nada em que possa agir.
- **Passo 3 (Q3), severidade 4, bloqueia:** **um termo do mecanismo onde ele
  espera um termo da tarefa.** Pode escrever 120 %, que abre a comporta
  toda, ou desistir.
:::

::: {.exemplo title="--- O walkthrough, passos 4 e 5, e a tabela final"}
| Passo | Q | Resp. | Razão (o que está no esboço) |
|:-------------|:-:|:-:|:------------------------------------------|
| **4** Verificar Ponte da Barca | Q1 | **não** | Nada no painel diz para verificar a jusante antes de confirmar. No sistema antigo, era um colega que telefonava para Ponte da Barca |
| | Q2 | sim | O painel das estações está no ecrã, por baixo das comportas |
| | Q3 | sim | Ponte da Barca é a primeira estação da lista |
| | Q4 | sim | O painel mostra o nível e o caudal |
| **5** Confirmar | Q1 | sim | Sabe que uma ordem tem de ser confirmada |
| | Q2 | sim | *Apply* é o único botão do painel |
| | Q3 | sim | "*Apply*" (aplicar) é o que ele quer fazer |
| | Q4 | **não** | O ecrã mostra 120 logo, como se estivesse feito. A comporta demora cerca de 3 minutos a mexer-se. Não há "pedido 120, atual 92" |

- **Passo 4 (Q1), severidade 3:** a regra "verificar a jusante antes de
  subir a descarga" **vive na cabeça das pessoas, não no ecrã**. O Tiago
  nunca chega a formar o objetivo.
- **Passo 5 (Q4), severidade 3:** não distingue uma **ordem aceite** de uma
  **ordem executada** e pode carregar outra vez em *Apply*.

**Tabela final** (a que se entrega):

| Passo | Q1 | Q2 | Q3 | Q4 | Problema | Sev. |
|:--|:-:|:-:|:-:|:-:|:-------------------------|:-:|
| 1 Selecionar Touvedo | sim | sim | sim | sim | --- | --- |
| 2 Encontrar os comandos | sim | não | sim | sim | Comando que parece mostrador | 3 |
| 3 Escrever 120 | sim | sim | não | sim | % onde se esperava m³/s | 4 |
| 4 Verificar Ponte da Barca | não | sim | sim | sim | Regra só na cabeça das pessoas | 3 |
| 5 Confirmar | sim | sim | sim | não | Valor mostrado como se já estivesse feito | 3 |

Cinco passos, quatro problemas, **um por pergunta**.
:::

::: {.pratica title="--- Fazer um walkthrough"}
**Exercício P.10** (atividade do Módulo 06 e exemplos inventados).
Técnica: as quatro perguntas, passo a passo, com a razão e a severidade.

**(a)** Máquina do Andante (ecrãs simplificados). Persona: visitante no
primeiro dia no Porto. Tarefa: comprar um bilhete para **uma viagem** de
Trindade a Campanhã. Ecrãs: **1** Idioma (PT, EN, ES, FR); **2** "O que
quer?" (Comprar um cartão novo / Carregar o meu cartão); **3** "Escolha o
seu título" (Z2, Z3, ..., Z8, Andante 24); **4** "Quantas viagens?" (1 a
10); **5** Pagar (Moedas / Cartão), depois "Retire o seu cartão". Faz a
tabela. Que ecrã falha primeiro, em que pergunta e porquê?

**(b)** Diz que pergunta falha (Q1--Q4) e porquê: **(1)** um micro-ondas
que não apita nem muda nada no visor quando se carrega em "Iniciar";
**(2)** uma app de comboios em que o lugar só se escolhe **depois** de
pagar, num ecrã a que só se chega por "Os meus bilhetes", sem nada que o
diga; **(3)** um termóstato em que o modo férias só existe dentro de
"Definições → Avançadas"; **(4)** no COL, um botão com a etiqueta "DF+"
para abrir a descarga de fundo.

**(c)** Para cada um dos quatro problemas do esboço do Tiago, propõe uma
mudança no esboço e diz que resposta passa a "sim".
:::

## O procedimento: papéis e regras

| Papel | Quem | O que faz |
|:----------|:----------|:------------------------------------|
| **Facilitador** | grupo que desenhou | Mostra o esboço de cada passo e diz o que está nele. **Mais nada** |
| **Avaliadores** (2 ou 3) | outro grupo | Põem-se no lugar da persona e respondem às quatro perguntas **em voz alta, com a razão** |
| **Registador** | grupo que desenhou | Escreve a tabela, uma linha por passo, **todas** as falhas |
| **Cronometrista** (opcional) | --- | Máximo de 3 minutos por passo, depois passa-se ao seguinte |

**Regras de Spencer:**

1. **Não se desenha durante o *walkthrough*.** A ideia vai para um post-it
   e discute-se no fim.
2. **Não se defende o desenho.** O facilitador diz o que está no esboço e
   nada mais.
3. **Regista-se todas as falhas**, mesmo as que os desenhadores acham
   óbvias.
4. **Três minutos por passo.** Se a discussão se alonga, escreve-se como
   problema e segue-se.

Sem estas regras, o *walkthrough* transforma-se numa reunião de desenho e
deixa de avaliar.

## A Fase 1 do projeto

| Antes (o grupo que desenhou prepara) | Durante (S6, novembro) | Depois (o que se entrega) |
|:----------------------|:----------------------|:----------------------|
| A **persona**: quem é o operador e o que já sabe | O grupo A percorre os esboços do grupo B durante cerca de **15 minutos**, depois trocam | As **três tabelas** preenchidas e **meia página com os três piores problemas**, dadas ao grupo que desenhou **no mesmo dia** |
| **Três missões** do enunciado: uma de **rotina**, uma de **alarme**, uma com o **coordenador** | Facilitador e registador do grupo que desenhou; 2 ou 3 avaliadores do outro | O grupo que desenhou decide o que muda antes dos *wireframes* da S7 |
| A **sequência correta** de cada missão, **5 a 10 passos**, escrita (é aqui que aparecem os ecrãs em falta) | As quatro perguntas em todos os passos; 3 minutos por passo; regras de Spencer | Guardam-se as duas coisas: as tabelas que escreveram para o outro grupo e a lista do que mudaram nos vossos esboços (evidência do R1, item 7) |
| Os esboços de **todos** os ecrãs, pela ordem da sequência, e **uma tabela em branco por missão** | Ideias em post-its, discutidas só no fim | |

**Ligação à Fase 2.** A avaliação heurística (Módulo 10) olha para os
mesmos ecrãs com outra pergunta: o *walkthrough* pergunta "esta persona
conseguiria passar?", a heurística pergunta "este ecrã viola uma regra
conhecida?". As duas juntas formam o ***heuristic walkthrough*** (Sears).

::: {.pratica title="--- Preparar e conduzir a Fase 1"}
**Exercício P.11** (inventado; usa também as quatro perguntas e os papéis).
Técnica: escrever a sequência correta e percorrê-la.

**(a)** Missão com o coordenador: subir a descarga de Touvedo de **280
para 420 m³/s**. Escreve a sequência correta de ações no esboço do Tiago
(ver os estados de uma manobra, Aula 1) e faz o *walkthrough* dos passos
que o esboço não cobre. Que ecrã falta?

**(b)** A meio da sessão, um desenhador diz: "é óbvio que o *setpoint* é a
abertura; isso explica-se na formação". Que regras quebra, e o que fazem
o facilitador e o registador?

**(c)** Se um avaliador encontra cerca de um terço dos problemas,
quantos encontram três avaliadores? Supõe† que cada um encontra cada
problema com probabilidade 1/3, independentemente dos outros.
:::
