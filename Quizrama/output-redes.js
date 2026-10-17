/**
 * Banco de perguntas de REDES DE COMUNICAÇÃO (Teste 1) — orquestrador.
 *
 * Define o global `ALL` consumido pela app (em redes.html), concatenando os
 * arrays de `assets/js/data/questions-redes/`.
 *
 * Matéria do 1.º teste: Capítulo 1 (Introdução) e Capítulo 2 (Camada de
 * aplicação, até aos sockets), como no teste modelo de 2024. Os tópicos
 * "Parte II ·" treinam os cálculos da parte de desenvolvimento e o
 * "Teste · Modelo 1" é a escolha múltipla do modelo, com a grelha oficial.
 */
/* eslint-disable no-undef */

const ALL = [].concat(
  Q_R_INTERNET,         // Internet e Comutação
  Q_R_ATRASOS,          // Atrasos e Débito
  Q_R_CAMADAS,          // Camadas Protocolares
  Q_R_APLICACOES,       // Princípios das Aplicações
  Q_R_HTTP,             // HTTP
  Q_R_FTP_EMAIL,        // FTP e Email
  Q_R_DNS,              // DNS
  Q_R_P2P,              // P2P
  Q_R_SOCKETS,          // Sockets
  Q_R_TREINO_ATRASOS,   // Parte II · Atrasos
  Q_R_TREINO_HTTP,      // Parte II · HTTP
  Q_R_TREINO_DIAGRAMAS, // Parte II · Diagramas
  Q_R_ABERTAS_ATRASOS,  // Parte II · Atrasos (resposta aberta, das fichas)
  Q_R_ABERTAS_HTTP,     // Parte II · HTTP (resposta aberta)
  Q_R_ABERTAS_DIAGRAMAS,// Parte II · Diagramas (resposta aberta)
  Q_R_ABERTAS_OUTROS,   // Parte II · DNS, email e P2P (resposta aberta)
  Q_R_MODELO1,          // Teste · Modelo 1 (escolha múltipla)
  Q_R_MODELO1_DEV,      // Teste · Modelo 1 (desenvolvimento, resposta aberta)
);
