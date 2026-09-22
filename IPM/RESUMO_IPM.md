---
title: "Interação Pessoa-Máquina (IPM) --- Resumo Teórico"
author: "Gonçalo Sousa"
date: "Atualizado: Semana 1 (Aulas 1--2, Módulos 01--02)"
---

<!-- processado: Teoricas/IPM_M01.pdf, Teoricas/IPM_M02.pdf -->

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

::: atencao
Referências bibliográficas dadas como opcionais pelo professor (não são
obrigatórias, mas são a bibliografia de referência do campo):

- *Sketching User Experiences: The Workbook* --- Greenberg, Carpendale,
  Marquardt, Buxton (Morgan Kaufmann, 2012).
- *About Face: The Essentials of Interaction Design* --- Cooper, Reimann,
  Cronin, Noessel (4.ª ed., 2014; a 3.ª ed. existe em PDF online).
- *Interaction Design: Beyond Human-Computer Interaction* --- Preece,
  Sharp, Rogers (5.ª ed. 2019, 6.ª ed. 2023).
- *Measuring the User Experience* --- Tullis, Albert (3.ª ed., 2022).
:::

## Frequência e regras de assiduidade

- **Aulas teóricas**: presenciais. O professor sublinha que é importante
  frequentá-las mesmo não sendo avaliadas por assiduidade diretamente,
  porque o conteúdo é a base do exame.
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

com a condição **FE $\geq$ 35%** (isto é, dos 10 pontos possíveis no exame, o
Gonçalo tem de obter pelo menos 3,5 valores *no próprio exame* — é um
patamar mínimo sobre a componente do exame, não sobre a nota final total).
Os 10 pontos de trabalho contínuo (R1 + PR2) são feitos em grupo; os 10
pontos do exame são individuais.
:::

::: exame
O critério **FE $\geq$ 35%** é uma condição de exclusão independente da nota
das componentes de grupo: mesmo com R1 e PR2 perfeitos, não atingir 3,5/10
no exame impede a aprovação pela fórmula normal. Vale a pena confirmar
sempre nas normas oficiais da disciplina se este mínimo se mantém igual ao
longo do semestre.
:::

### R1 --- Primeiro relatório (4 pontos)

Trabalho de grupo baseado no **estudo e desenho** de um sistema capaz de
fazer interação pessoa-máquina. Envolve: investigação (*research*), análise
de requisitos, metodologia de implementação e resultados preliminares de
avaliação. Feito em **grupos de 4**. Não há nota mínima, mas é avaliado de
forma contínua ao longo do trabalho (não só no entregável final). Há uma
apresentação intercalar do relatório (data a confirmar).

### PR2 --- Protótipo + Segundo relatório (6 pontos)

Trabalho baseado numa **implementação de protótipo**, associado ao trabalho
anterior (R1). Envolve: materiais e ferramentas de prototipagem rápida, uso
de software (**Figma**), e detalhes de implementação decididos caso a caso
com o professor. É feito **pelo mesmo grupo** do R1. Também sem nota
mínima, mas avaliado continuamente. Há uma apresentação final do protótipo
desenvolvido + segundo relatório.

### Exame final (10 pontos)

- Feito no **Moodle**, individual.
- Perguntas de escolha múltipla, perguntas de associação, perguntas de
  arrastar e largar (*drag and drop*).
- Duração aproximada: 70 a 90 minutos.
- Mínimo: **35%** da nota do exame (ver caixa de exame acima).

## O projeto: um sistema, três fases, três avaliações

Há **um projeto para toda a turma**: todos os grupos desenham um sistema
dentro do mesmo domínio/tema geral, mas cada grupo tem de construir a sua
própria abordagem e trazer algo que os outros grupos não têm — isso é o
"ouro" do grupo (o seu diferencial).

::: {.definicao title="--- As três fases do projeto"}
| Fase | Mês | Artefacto (fidelidade) | Avaliação |
|---|---|---|---|
| Fase 1 | outubro | Esboços (*sketches*), baixa fidelidade | *Cognitive walkthrough* |
| Fase 2 | novembro | *Wireframes*, fidelidade média | Avaliação heurística |
| Fase 3 | dezembro | Protótipo interativo, alta fidelidade | Testes de usabilidade |

Depois de cada fase: outros grupos avaliam o artefacto → escrevem
conclusões → o grupo melhora o artefacto com base nisso. As datas exatas
são publicadas no Moodle.
:::

::: atencao
**Nota adicional (não estava explicado em detalhe nestes slides):** os
três métodos de avaliação do projeto só são explicados em profundidade
mais tarde na disciplina (aparecem apenas nomeados no Módulo 02, secção T4
abaixo), mas já aqui fica o significado geral, para perceber a lógica do
calendário:

- **Cognitive walkthrough** (Fase 1): outros grupos "percorrem" passo a
  passo uma sequência de ações (uma *missão*) que um utilizador faria no
  teu esboço, e para cada passo avaliam se seria óbvio o que fazer a
  seguir (pontuação 0 / 1 / 2 por passo). Não precisa de utilizadores reais
  nem de protótipo funcional — só o esboço e o percurso mental do
  avaliador.
- **Avaliação heurística**: um avaliador (ou vários) compara o design
  contra uma lista de princípios de usabilidade já conhecidos — as
  **heurísticas de Nielsen**, mais heurísticas próprias do grupo — e regista
  a **severidade** e a **extensão** (quantas partes do sistema são afetadas)
  de cada problema encontrado.
- **Testes de usabilidade**: utilizadores reais (neste projeto, vindos de
  *outros grupos*) tentam completar tarefas reais no protótipo, e
  regista-se sucesso/insucesso, tempo, erros e frases ditas (*quotes*)
  durante a tarefa.

Estes três métodos ficam cada vez mais dependentes de um artefacto mais
acabado (esboço → wireframe → protótipo interativo), o que explica a
ordem das fases.
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
- **Avaliação entre grupos**: usa missões, matrizes avaliador-por-objeto,
  pontuações independentes e conclusões escritas. Os avaliadores conhecem o
  domínio do problema (não são utilizadores totalmente ingénuos).

## Uso de Inteligência Artificial generativa na disciplina

::: {.atencao title="--- Regras sobre IA generativa"}
**Permitido** (como apoio instrumental):

- Reformular e rever os teus próprios textos.
- Explorar vocabulário e alternativas *depois* de teres a tua própria ideia.
- Pequenos trechos de código (*snippets*) e ajuda com as ferramentas de
  prototipagem.
- Resumir referências que já leste.

**Não permitido** (como substituto do teu próprio raciocínio):

- Gerar os esboços ou os conceitos de design.
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

::: atencao
Critério de bom/mau exemplo mostrado nos slides: uma foto **sem** as
anotações (nome, objeto, data) conta como mau exemplo mesmo que o objeto
fotografado seja interessante — a anotação é parte obrigatória do
exercício, não um extra.
:::

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

::: atencao
Nota importante repetida várias vezes nos slides: **escreve sempre as
palavras exatas usadas pelos utilizadores** durante a investigação — esse
vocabulário *é* o material com que se constrói o modelo conceptual mais
tarde (T3). Não parafrasear logo para "linguagem técnica".
:::

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

::: exame
**80% dos utilizadores ficam no nível "principiante avançado"** — este
número foi sublinhado nos slides como o critério prático para decidir para
quem se otimiza uma interface: não para o perito (que é raro e já se
adapta sozinho), nem só para o principiante total (que rapidamente evolui),
mas para quem já executa a tarefa mas não quer nem precisa de se tornar
"power user".
:::

### Métodos para investigar utilizadores

Os métodos de investigação de utilizadores organizam-se tipicamente em
dois eixos: um eixo **qualitativo (direto)** vs. **quantitativo
(indireto)**, e um eixo **comportamental** (o que as pessoas fazem) vs.
**atitudinal** (o que as pessoas dizem).

::: atencao
Nota adicional (não estava detalhado nos slides além do diagrama): a
pergunta que cada quadrante do eixo tende a responder é diferente —
qualitativo tende a responder **"porquê" e "como resolver"**, quantitativo
tende a responder **"quantos" e "quanto"**. Isto ajuda a escolher o método
certo consoante a pergunta de investigação que se tem.
:::

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

::: atencao
Regra geral sublinhada nos slides: **observar mais do que perguntar**.
Sempre que possível, vale mais ver alguém a fazer a tarefa do que perguntar
como a fazem — o relato de uma ação é sempre filtrado pela memória e pelos
enviesamentos acima; a observação direta não.
:::

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

::: atencao
**Uma persona NÃO é:**

- Baseada em dados demográficos ou segmentos de mercado.
- Feita a partir de "sensações à barriga" (*gut feelings*) sobre o público.
- Um perfil de utilizador genérico ou um estereótipo.
:::

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
objetivos — nada mais do que isto é necessário nesta fase.
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

![O utilizador nunca vê o sistema real: só vê a imagem do sistema, construída para levar a um determinado modelo mental](figuras/modelo_conceptual_imagem_sistema.pdf){width=90%}

*O utilizador só vê a imagem do sistema. Esboços e protótipos são a forma
mais barata de testar se essa imagem produz o modelo conceptual certo.*

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
desenho, e engenharia.

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

::: exame
**Muito importante, sublinhado explicitamente nos slides: evita misturar
ideias diferentes no mesmo esboço.** Cada esboço deve corresponder a uma
única ideia — misturar ideias no mesmo desenho torna difícil depois
avaliar, comparar ou escolher entre elas individualmente.
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
para uma primeira revisão formal (informalmente chamado o "modelo 10x10":
gerar muitas variações, tipicamente da ordem de 10, e ir reduzindo).

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

::: atencao
Nota adicional (útil para perceber porque isto não é contraditório com
"getting the design right"): os dois modos não se excluem — na prática,
usa-se **redução** (Getting the Right Design, entre várias ideias) para
escolher em que ideia vale a pena investir tempo a **elaborar em
profundidade** (Getting the Design Right, dentro dessa ideia). O funil de
desenho abaixo mostra exatamente essa alternância.
:::

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

::: atencao
Nesta disciplina, a sequência de métodos de avaliação usada ao longo do
projeto é: **cognitive walkthrough → avaliação heurística → testes de
usabilidade** — exatamente as três fases do projeto descritas na Aula 1
(ver secção "O projeto: um sistema, três fases, três avaliações"). Os
métodos em si (como se conduz cada um passo a passo) ainda não foram
explicados em detalhe — isso fica para módulos futuros; aqui fica só o
mapeamento entre a teoria (T4) e o calendário do projeto.
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

::: atencao
Nota adicional: os slides terminam com fotografias de esboços em quadro
branco de projetos de anos anteriores (conceitos de *smartwatch* para
diferentes públicos — pessoas invisuais, controlo de dispositivos IoT,
identificação bancária, etc.). Servem só como ilustração do nível de
detalhe e da quantidade de ideias geradas numa sessão real de
*brainstorming* em grupo (ligado à regra "gerar ~5-10 ideias" acima) — não
introduzem conceito teórico novo, por isso não são reproduzidos aqui em
detalhe.
:::
