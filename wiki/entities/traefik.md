---
type: entity
title: "Traefik"
aliases: ['traefik proxy']
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [proxy-reverso, docker, lets-encrypt, tech-mentor-infra]
skill: tech-mentor-security
status: stub
---

# Traefik

Proxy reverso usado no deploy do [[wiki/entities/omxterm]]: termina HTTPS com Let's Encrypt e aplica rate limit por middleware ([[wiki/concepts/reverse-proxy]], [[wiki/concepts/rate-limiting]]). O deploy usa rede Docker com IPs fixos para Traefik e app, para casar com o UFW ([[wiki/concepts/allowlist-de-destino-ssh]]). Em outra fonte, um bug do Traefik/Coolify esteve ligado a um incidente de SYN flood ([[wiki/concepts/ddos-syn-flood]]).

## Key Sources

- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]
