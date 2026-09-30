---
type: concept
title: "Cross-Site WebSocket Hijacking (CSWSH)"
aliases: ['cswsh', 'cross-site websocket hijacking', 'websocket hijacking']
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [websocket, seguranca, owasp, cookies, tech-mentor-security]
skill: tech-mentor-security
status: stub
---

# Cross-Site WebSocket Hijacking (CSWSH)

Variante de [[wiki/concepts/csrf]] para WebSocket: um site malicioso abre uma conexão WebSocket para a aplicação alvo e o navegador anexa os cookies da vítima ao handshake, dando ao atacante um canal autenticado `[external — conhecimento geral; a fonte só nomeia o ataque]`. Segundo [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]], o autor o conheceu no **OWASP Cheat Sheet Series** ([[wiki/concepts/owasp]]) antes de projetar o [[wiki/entities/omxterm]] e o evita **não usando cookies no WebSocket**, mas um [[wiki/concepts/ticket-de-uso-unico-websocket|ticket de uso único]]. `[external]` Checar o header `Origin` no handshake é outra mitigação comum, não citada na fonte.

## Key Sources

- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]
