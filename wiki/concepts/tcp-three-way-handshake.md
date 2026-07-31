---
type: concept
title: "TCP Three-Way Handshake"
aliases: ["handshake TCP", "SYN-SYN/ACK-ACK"]
date_created: 2026-07-28
date_updated: 2026-07-31
source_count: 2
tags: [rede, tcp, handshake, browser, critical-rendering-path, syn-flood, syn-cookies, seguranca]
skill: tech-mentor-frontend
status: draft
---
# TCP Three-Way Handshake

Sequência de três mensagens que estabelece uma conexão TCP antes de qualquer troca de dados HTTP:

1. Cliente envia **SYN**.
2. Servidor responde **SYN-ACK**.
3. Cliente confirma com **ACK**.

No fluxo de carregamento de uma página web, acontece depois da resolução [[wiki/concepts/dns]] e antes do [[wiki/concepts/tls-handshake]] (se HTTPS) e do request HTTP. Faz parte da fase de rede do [[wiki/concepts/critical-rendering-path]].

## Abuso do handshake: SYN flood

O mesmo mecanismo que garante uma conexão confiável é o alvo de um [[wiki/concepts/ddos-syn-flood|SYN flood]]: o atacante envia o `SYN` inicial em massa e nunca responde ao `SYN-ACK` do servidor com o `ACK` final. Se o servidor reserva memória/socket assim que recebe cada `SYN`, uma fila de conexões "meio-abertas" cresce até esgotar recursos. **SYN cookies** resolvem isso adiando a alocação de memória até o terceiro passo do handshake de fato se completar — o servidor responde ao `SYN` com um `SYN-ACK` cujo número de sequência é derivado criptograficamente, sem guardar estado, e só materializa a conexão quando (e se) o `ACK` final confirma esse valor.

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
- [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]]
