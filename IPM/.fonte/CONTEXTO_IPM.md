# CONTEXTO_IPM (convenções e factos; não gera PDF)

**Nomes.** Os slides vêm por módulos: `Module N · Lecture k` → `Aula_NN`, para
Aula N = Módulo N. Slides em inglês, resumo em português (os termos ingleses
ficam em itálico na 1.ª vez). Alguns módulos vêm em `.pptx` (o `extrair.sh`
trata disso).

**Exercícios.** `Exercício P.N` (próximo número: ver o `prep.sh`); alíneas
`**(a)**`. Exercícios de desenho → **resposta-modelo**, dita como tal.
Entregáveis avaliados do grupo (personas, missões): sem solução gerada (regras
de IA da disciplina), só uma grelha de verificação mais um contraexemplo.
Exemplo-modelo: `SOLUCOES_IPM.md`, `### P.5` (l. ~424).

**Projeto COL** (Centro de Operações do Lima; detalhe no RESUMO, Aula 1):
- Barragens: Alto Lindoso (6 comportas, descarga de fundo 400 m³/s, 2 grupos,
  630 MW) e Touvedo (3 comportas, descarga de fundo 50 m³/s, 1 grupo, 22 MW).
- O operador decide sozinho: reconhecer alertas, caudal turbinado, descarga de
  fundo, comportas de Touvedo com o total < 300 m³/s, análises, equipas.
  Precisa do coordenador (na interface): descargas > 300 m³/s, avisos à
  população, fechar pontes/parques/Passeio 25 de Abril.
- Estados de uma manobra: pedida, à espera de autorização, autorizada, em
  curso, concluída, cancelada. Descarga de fundo: fechada, a abrir, aberta,
  avariada. Troço: normal, vigilância, alerta amarelo/laranja/vermelho,
  emergência.
- Sala: operador sentado, 2 monitores de 27" (privados) + parede 4×3 (pública).
  Regras: sempre visível sem scroll, sem menus escondidos, comandos que mudam
  o rio difíceis de acionar por engano, perceber tudo num relance às 3 da manhã.
- Fases: 1 esboços + *cognitive walkthrough* (S6, 3 nov); 2 *wireframes* +
  avaliação heurística; 3 protótipo + testes de usabilidade.
