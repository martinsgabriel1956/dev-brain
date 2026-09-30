---
type: concept
title: "Ticket de Uso Único para WebSocket"
aliases: ['one-time ticket', 'ws ticket', 'ticket de websocket']
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [websocket, autenticacao, seguranca, ticket, tech-mentor-security]
skill: tech-mentor-security
status: draft
---

# Ticket de Uso Único para WebSocket

Padrão descrito em [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]: em vez de autenticar o WebSocket por cookie, o servidor, após validar tudo por HTTP (cookies + regras de destino), devolve `URL do WebSocket + ticket + tempo de expiração` (**60 s** no exemplo). O cliente abre o WebSocket com o ticket, e o servidor **apaga** o ticket ao usá-lo (uso único).

**Por quê:** (1) quem obtiver o ticket não pode reusá-lo; (2) como o WebSocket não depende de cookies, o navegador não anexa credencial ambiente a um handshake iniciado por outro site — mitiga [[wiki/concepts/cross-site-websocket-hijacking]]. **Custo:** recarregar a página derruba a sessão. Ver [[wiki/concepts/terminal-web-broker-websocket-ssh]], [[wiki/concepts/sessoes-http-cookies]].

## Key Sources

- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]
