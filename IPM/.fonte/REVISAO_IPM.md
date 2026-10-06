---
title: "Interação Pessoa-Máquina --- Folha de revisão"
author: "Gonçalo Sousa"
date: "Aulas 1--4 (Módulos 01--04). As receitas do resumo, sem exemplos: para rever antes do exame."
---

## Avaliação e projeto

**Nota**: $FG = R1\,(4) + PR2\,(6) + FE\,(10)$, com **FE $\geq$ 35%** (3,5/10
no próprio exame), eliminatório. Labs: assiduidade $\geq$ 70%, máximo 3
faltas. O exame também avalia o trabalho de grupo.

**Fronteira R1/PR2**: o R1 vai até aos **modelos conceptuais e decisões**
(etapa 5). O PR2 começa no **protótipo** (etapa 6) e inclui a avaliação de
usabilidade e o relatório final. O R1 do COL já leva o *cognitive
walkthrough* sobre os esboços.

**Três fases de avaliação** (cada uma sobre um artefacto mais acabado):

| Fase | Método | Sobre | Regista-se |
|:-:|:-------|:------|:--------------|
| 1 | *Cognitive walkthrough* | esboços | cada passo da missão: 0 / 1 / 2 |
| 2 | Avaliação heurística (Nielsen + próprias) | *wireframes* | severidade e extensão |
| 3 | Testes de usabilidade | protótipo interativo | sucesso, tempo, erros, *quotes* |

**IA generativa**: pode rever textos, sugerir vocabulário *depois* de teres
a ideia, dar *snippets* e resumir o que já leste. Não pode gerar esboços,
conceitos, decisões, avaliações ou "evidência". Imagens geradas por IA só
ilustram um conceito já escolhido.

## Procedimento (8 etapas) e tarefas T1--T4

1 equipa → 2 estudos exploratórios + stakeholders → 3 recolher, agregar e
concluir dados → 4 utilizador + personas + tecnologia → 5 modelos
conceptuais + decisões (**R1**) → 6 protótipo → 7 avaliação de usabilidade
→ 8 relatório final (**PR2**). Cada passo produz evidência para o
seguinte.

**T1** personas e stakeholders → **T2** estudos iniciais → **T3** desenho
conceptual → **T4** avaliação, que **realimenta T3** (não recomeça em T1).

**Ciclo iterativo**: analisar → conceptualizar → prototipar → avaliar →
analisar..., até a evidência dizer que chega.

## Utilizadores (T1)

**Três eixos**: o que sabem da tarefa, o que sabem das ferramentas e que
modelo mental (e vocabulário) têm.

**Perícia**: principiante → **principiante avançado (80% ficam aqui:
otimiza-se para eles)** → competente → perito (raro).

**Métodos** em dois eixos: qualitativo (direto, responde a "porquê" e
"como resolver") vs. quantitativo (indireto, responde a "quantos" e
"quanto"); comportamental (o que fazem) vs. atitudinal (o que dizem).
**Observar mais do que perguntar.**

**Perguntas**:

- evitar perguntas indutoras, sim/não, duas em uma, hipotéticas ou com
  jargão;
- preferir perguntas abertas, sobre comportamento, uma coisa de cada vez,
  sobre episódios concretos e recentes;
- escrever as **palavras exatas** do utilizador.

**Enviesamentos**: confirmação, indução do entrevistador, desejabilidade
social, aquiescência, memória e amostragem. Cada um tem o seu antídoto.

**Persona**: um arquétipo com **objetivos, frustração, tecnologia e
contexto**. Não é demografia, nem *gut feeling*, nem estereótipo. A
segmentação só garante cobertura.

**10 regras**: memorável; separar por objetivos; audiência ampla; um
detalhe pessoal; 3--4 objetivos; contexto do projeto; padrões de
comportamento, não cargo; conjunto pequeno; sem correlação com segmentos
de mercado; objetivos, não tarefas.

## Desenho conceptual (T3)

**Três camadas**: funcionalidade (como o sistema é) → **modelo conceptual**
(como queres que o utilizador o veja) → imagem do sistema (o que o leva a
formar esse modelo).

**Pipeline (6 passos)**: perceber → criar vários modelos → esboçar
(depressa) → descrever por texto → avaliar → melhorar o mais promissor, e
voltar a esboçar.

**Grelhas de avaliação**: uma linha por modelo, uma coluna por critério e
uma grelha por avaliador. Quanto mais avaliadores, e mais diferentes,
melhor. Escala com um número **par** de níveis (1--4, sem meio) e uma regra
de agregação.

**Funil**: alterna geração e redução, com granularidade crescente (geral
→ grosseira → média → fina) até sobrar um conceito. ***Getting the Right
Design*** (escolher entre muitas ideias, por redução) vem antes de
***Getting the Design Right*** (elaborar a escolhida em profundidade).

**Método 10x10**:
1. enunciar o desafio;
2. $\geq$ 10 **conceitos diferentes** (expandir, sem julgar);
3. reduzir, ou repetir o passo 2;
4. escolher o(s) mais promissor(es), sem deitar fora os outros;
5. 10 **variações** de cada sobrevivente;
6. apresentar ao grupo e pedir *feedback*;
7. esboçar as mudanças e voltar ao passo 1 (ou 4), mais fundo no funil.

Dez variações de uma ideia **não** são dez conceitos.

## Esboçar

**Três razões**: criar, registar e refletir/partilhar/criticar/decidir.

**Atributos**: rápido, oportuno, descartável (mas guarda-se: é
evidência), abundante, vocabulário claro, resolução limitada, coerente com
o estado do desenho, sugere e explora, catalisador. **Um esboço, uma
ideia.**

**Esboço vs. protótipo**: o propósito distingue-os sempre (o esboço
**comunica**, o protótipo **verifica**); a forma, só normalmente. É um
contínuo.

| Esboço | Protótipo |
|:-----------------|:-----------------|
| evocativo, sugere, explora, pergunta, propõe, provoca | didático, descreve, refina, responde, testa, resolve, específico |

**Fidelidade**: quão parecido com o sistema final, no aspeto e no
comportamento. A fidelidade sobe com as fases: esboço → *wireframe* →
protótipo.

## Avaliação (T4)

***Task flow***: um objetivo e os seus passos, uma linha por passo (o que o
utilizador faz e o que o sistema mostra). Escreve-se a partir do objetivo
e não da interface, e termina num critério de sucesso verificável. Os
*flows* são as missões das avaliações.

## Porquê IPM e como as interfaces falham

**Moore vs. "Darwin"**: as máquinas melhoram exponencialmente, as pessoas
não. O desenho de interação vive no fosso entre as duas curvas.

**Quatro assuntos**:
1. tarefas partilhadas entre pessoa e máquina (decidir quem faz o quê);
2. comunicação (da máquina para a pessoa, e entre pessoas através da
   máquina);
3. métodos de desenho (especificar, desenhar, implementar, avaliar);
4. compromissos de desenho.

**Lista de verificação** (usar em cada painel):
- **informação**: o que mostrar, e quando;
- **apresentação**: como mostrar (ponteiro vs. número; vermelho só para
  perigo);
- **interação**: como manipular (encontra-se pelo tato?).

**Três falhas clássicas**: funções que não se veem, códigos que não se
conseguem lembrar e um estado que não se consegue verificar.

**Sinalizador** (*signifier*): um sinal da ação possível. Quando a forma
contradiz a ação real, nenhuma placa resolve o problema.
