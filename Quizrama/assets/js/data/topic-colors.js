/* eslint-disable no-unused-vars */
/**
 * TOPIC_COLORS — paleta por tópico (badges, pontos, barras de erro); tons de tinta legíveis em papel e em ardósia.
 * Helpers `tc(topic)` e `tb(topic)` devolvem cor de texto e cor de fundo,
 * com fallback em "General OS" se o tópico for desconhecido.
 */
const TOPIC_COLORS = {
  "Scheduling":                    {color:"#2f5bd3",bg:"transparent"},
  "Synchronization":               {color:"#0f7c8a",bg:"transparent"},
  "Deadlocks":                     {color:"#6b4fbf",bg:"transparent"},
  "Memory Management":             {color:"#b5651d",bg:"transparent"},
  "File Systems":                  {color:"#b8337a",bg:"transparent"},
  "I/O Systems":                   {color:"#1e7a4c",bg:"transparent"},
  "Processes":                     {color:"#8a6d00",bg:"transparent"},
  "IPC":                           {color:"#3b6e8f",bg:"transparent"},
  "System Calls":                  {color:"#9c4221",bg:"transparent"},
  "Security":                      {color:"#5a5fd6",bg:"transparent"},
  "General OS":                    {color:"#2f5bd3",bg:"transparent"},
  "Linguagem C":                   {color:"#0f7c8a",bg:"transparent"},
  "Conceitos Básicos":             {color:"#6b4fbf",bg:"transparent"},
  "I/O e Interrupções":            {color:"#b5651d",bg:"transparent"},
  "Processos":                     {color:"#b8337a",bg:"transparent"},
  "Escalonamento":                 {color:"#1e7a4c",bg:"transparent"},
  "Sincronização":                 {color:"#8a6d00",bg:"transparent"},
  "Treino · fork()":               {color:"#c0392b",bg:"transparent"},
  "Treino · Pipes":                {color:"#c0392b",bg:"transparent"},
  "Treino · Scheduling":           {color:"#c0392b",bg:"transparent"},
  "Treino · Sinais":               {color:"#c0392b",bg:"transparent"},
  "Exame · Parte I":               {color:"#8a6d00",bg:"transparent"},
  "Exame · Parte II":              {color:"#8a6d00",bg:"transparent"},
  "Exame · Parte III":             {color:"#8a6d00",bg:"transparent"},
  "Exame · Parte IV":              {color:"#8a6d00",bg:"transparent"},
  "Exame · Parte V":               {color:"#8a6d00",bg:"transparent"},
  "Exame · Parte VI":              {color:"#8a6d00",bg:"transparent"},
  // ── Teste 2 (slides #06–#10) ──
  "Threads":                       {color:"#3b6e8f",bg:"transparent"},
  "Sistema de Ficheiros":          {color:"#9c4221",bg:"transparent"},
  "Dispositivos de Armazenamento": {color:"#5a5fd6",bg:"transparent"},
  "Gestão de Memória":             {color:"#2f5bd3",bg:"transparent"},
  "Memória Virtual":               {color:"#0f7c8a",bg:"transparent"},
  // ── Redes de Comunicação · Teste 1 ──
  "Internet e Comutação":          {color:"#6b4fbf",bg:"transparent"},
  "Atrasos e Débito":              {color:"#b5651d",bg:"transparent"},
  "Camadas Protocolares":          {color:"#b8337a",bg:"transparent"},
  "Princípios das Aplicações":     {color:"#1e7a4c",bg:"transparent"},
  "HTTP":                          {color:"#8a6d00",bg:"transparent"},
  "FTP e Email":                   {color:"#3b6e8f",bg:"transparent"},
  "DNS":                           {color:"#9c4221",bg:"transparent"},
  "P2P":                           {color:"#5a5fd6",bg:"transparent"},
  "Sockets":                       {color:"#2f5bd3",bg:"transparent"},
  "Parte II · Atrasos":            {color:"#c0392b",bg:"transparent"},
  "Parte II · Diagramas":        {color:"#c0392b",bg:"transparent"},
  "Parte II · HTTP":               {color:"#c0392b",bg:"transparent"},
  "Teste · Modelo 1":              {color:"#8a6d00",bg:"transparent"},
};
const tc = t => (TOPIC_COLORS[t]||TOPIC_COLORS["General OS"]).color;
const tb = t => (TOPIC_COLORS[t]||TOPIC_COLORS["General OS"]).bg;
