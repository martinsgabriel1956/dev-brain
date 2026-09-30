---
type: concept
title: "Terminal Web (Broker WebSocket + SSH)"
aliases: ['terminal web', 'web terminal', 'broker ssh', 'omxterm architecture']
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [terminal-web, websocket, ssh, xterm-js, arquitetura, seguranca, tech-mentor-security]
skill: tech-mentor-security
status: draft
---

# Terminal Web (Broker WebSocket + SSH)

A web não fala com PTY nem com SSH, então o terminal web é uma variação: **navegador (xterm.js) → WebSocket → broker (backend) → SSH → sshd → line discipline → Bash**. Cada tecla vira uma mensagem input no WebSocket; a saída volta como output; o resize da janela também é enviado (com *debounce* no servidor). Descrito em [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]] para o [[wiki/entities/omxterm]].

**Fluxo de autenticação em duas fases** (mistura HTTP com cookies e WebSocket sem cookies):

1. Token → cookies de sessão (`HttpOnly`, `Secure`, `SameSite=Strict`) — ver [[wiki/concepts/sessoes-http-cookies]].
2. Formulário SSH → o broker busca o *fingerprint* do host destino; o usuário confere e confia.
3. Broker valida ([[wiki/concepts/allowlist-de-destino-ssh]], [[wiki/concepts/dns-rebinding]]) e emite um [[wiki/concepts/ticket-de-uso-unico-websocket|ticket de uso único]].
4. WebSocket abre com o ticket, **sem cookies** — defesa contra [[wiki/concepts/cross-site-websocket-hijacking]]. Recarregar a página perde a sessão.

Regra de projeto: [[wiki/concepts/design-efemero-zero-persistencia]]. O broker é ponto crítico: recebe a chave privada SSH do usuário em trânsito `[inferência: exige confiar no broker]`. Ver [[wiki/concepts/websocket-vs-polling]], [[wiki/concepts/ssh]], [[wiki/concepts/emulador-de-terminal]].

## Key Sources

- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]
