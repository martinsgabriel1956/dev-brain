---
type: concept
title: "TCP Three-Way Handshake"
aliases: ["handshake TCP", "SYN-SYN/ACK-ACK"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [rede, tcp, handshake, browser, critical-rendering-path]
skill: tech-mentor-frontend
status: draft
---
# TCP Three-Way Handshake

Sequência de três mensagens que estabelece uma conexão TCP antes de qualquer troca de dados HTTP:

1. Cliente envia **SYN**.
2. Servidor responde **SYN-ACK**.
3. Cliente confirma com **ACK**.

No fluxo de carregamento de uma página web, acontece depois da resolução [[wiki/concepts/dns]] e antes do [[wiki/concepts/tls-handshake]] (se HTTPS) e do request HTTP. Faz parte da fase de rede do [[wiki/concepts/critical-rendering-path]].

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
