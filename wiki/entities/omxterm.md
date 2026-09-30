---
type: entity
title: "OMXTerm"
aliases: ['omxterm web']
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [terminal-web, projeto, ssh, websocket, fastify, react, tech-mentor-security]
skill: tech-mentor-security
status: stub
---

# OMXTerm

Terminal web de fim de semana (MVP) de [[wiki/entities/otavio-miranda]]: monorepo com core, backend (Fastify, SSH2, WebSocket, Zod) e frontend (Vite, React, [[wiki/entities/xterm-js]]). Para **uma pessoa, um token**; sem RBAC, sem DoS/DDoS, sem `known_hosts`, sem addon WebGL. Rate limit interno (10 tentativas/60 s bloqueiam o IP) mais o do [[wiki/entities/traefik]]. Arquitetura em [[wiki/concepts/terminal-web-broker-websocket-ssh]]; regra [[wiki/concepts/design-efemero-zero-persistencia]]. Código escrito por agentes ([[wiki/concepts/auditoria-de-issue-por-agente-de-contexto-limpo]]); repositório não acessado, nada verificado no código.

## Key Sources

- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]
