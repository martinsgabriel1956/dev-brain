---
type: concept
title: "CSRF (Cross-Site Request Forgery)"
aliases: ['csrf', 'xsrf', 'cross-site request forgery']
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [csrf, seguranca, cookies, owasp, tech-mentor-security]
skill: tech-mentor-security
status: stub
---

# CSRF (Cross-Site Request Forgery)

Um site malicioso aproveita os cookies de um usuário logado na aplicação para executar ações em nome dele, se a aplicação não estiver protegida ([[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]). Mitigação demonstrada na fonte: cookies **`SameSite=Strict`** (só enviados quando o domínio de destino é o da aplicação), além de `HttpOnly` e `Secure` ([[wiki/concepts/sessoes-http-cookies]]). `[skill: tech-mentor-security]` `SameSite=Lax` mitiga a maioria dos casos e CSRF token é a alternativa clássica. Correlato: [[wiki/concepts/cross-site-websocket-hijacking]], [[wiki/concepts/xss]], [[wiki/concepts/cors-misconfiguration]].

## Key Sources

- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]
