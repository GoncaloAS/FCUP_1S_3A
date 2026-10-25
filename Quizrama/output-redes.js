/**
 * Banco de perguntas de REDES DE COMUNICAÇÃO (Teste 1) — orquestrador.
 *
 * Define o global `ALL` consumido pela app (em redes.html), ordenado
 * pedagogicamente pelo programa da matéria:
 *
 *   Capítulo 1 (Introdução):
 *     1. Internet e Comutação
 *     2. Atrasos e Débito (teoria + cálculos + problemas abertos)
 *     3. Camadas Protocolares & Diagramas Temporais
 *
 *   Capítulo 2 (Camada de Aplicação):
 *     4. Princípios das Aplicações
 *     5. Web e HTTP (teoria + cálculos de tempos + problemas abertos)
 *     6. FTP e Email (SMTP, POP3, IMAP)
 *     7. DNS (teoria + registos + resolução com caches)
 *     8. P2P (BitTorrent + tempos de distribuição)
 *     9. Sockets e Modelos de Servidores (TCP, UDP, iterativo, threads, multiplex)
 *
 *   Simulação de Exame:
 *     10. Teste · Modelo 1 (escolha múltipla oficial + desenvolvimento oficial)
 */
/* eslint-disable no-undef */

const ALL = [].concat(
  // ── Capítulo 1: Introdução ──
  Q_R_INTERNET,         // Internet e Comutação (15)
  Q_R_ATRASOS,          // Atrasos e Débito — teoria (15)
  Q_R_TREINO_ATRASOS,   // Parte II · Atrasos — cálculos (10)
  Q_R_ABERTAS_ATRASOS,  // Parte II · Atrasos — problemas de desenvolvimento (4)
  Q_R_CAMADAS,          // Camadas Protocolares — 5 camadas, encapsulamento, routers/switches (10)
  Q_R_TREINO_DIAGRAMAS, // Parte II · Diagramas — treino temporal (8)
  Q_R_ABERTAS_DIAGRAMAS,// Parte II · Diagramas — par de pacotes e estimativa de capacidade (1)

  // ── Capítulo 2: Camada de Aplicação ──
  Q_R_APLICACOES,       // Princípios das Aplicações (13)
  Q_R_HTTP,             // HTTP — teoria (20)
  Q_R_TREINO_HTTP,      // Parte II · HTTP — cálculos de tempos e MSC (7)
  Q_R_ABERTAS_HTTP,     // Parte II · HTTP — problema aberto de resposta (1)
  Q_R_FTP_EMAIL,        // FTP e Email (17)
  Q_R_DNS,              // DNS — teoria (14)
  Q_R_P2P,              // P2P — teoria (7)
  Q_R_ABERTAS_OUTROS,   // Parte II · DNS, email e P2P — problemas abertos práticos (4)
  Q_R_SOCKETS,          // Sockets e Servidores — TCP, UDP e concorrência (11)

  // ── Teste Modelo Oficial ──
  Q_R_MODELO1,          // Teste · Modelo 1 — escolha múltipla oficial (10)
  Q_R_MODELO1_DEV,      // Teste · Modelo 1 — desenvolvimento oficial (7)
);
