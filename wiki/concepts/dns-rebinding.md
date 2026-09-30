---
type: concept
title: "DNS Rebinding"
aliases: ['dns rebinding', 'dns rebinding attack']
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [dns, seguranca, ssrf, tech-mentor-security]
skill: tech-mentor-security
status: stub
---

# DNS Rebinding

Ataque em que um nome de domínio passa a resolver para um IP diferente entre a validação e o uso, burlando checagens de destino `[external — conhecimento geral]`. Defesa descrita em [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]: na **primeira** vez que o broker vê um domínio, resolve o IP, valida-o contra a [[wiki/concepts/allowlist-de-destino-ssh|allowlist]] e **passa a usar só o IP**, sem nova consulta DNS. Ver [[wiki/concepts/dns]], [[wiki/concepts/terminal-web-broker-websocket-ssh]].

## Key Sources

- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]
