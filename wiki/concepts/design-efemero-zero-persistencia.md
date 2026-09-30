---
type: concept
title: "Design Efêmero (Zero Persistência)"
aliases: ['efêmero', 'zero persistência', 'não salvar nada']
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [seguranca, privacidade, arquitetura, minimizacao-de-dados, tech-mentor-security]
skill: tech-mentor-security
status: stub
---

# Design Efêmero (Zero Persistência)

Regra central do [[wiki/entities/omxterm]] ([[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]): **nada é salvo** no servidor nem no cliente; tudo é descartado assim que possível, ao fechar a conexão. Só ficam os **hashes dos tokens** de autenticação. Motivo declarado: não guardar chave privada SSH e afins. É também a única regra a remover se alguém quiser evoluir o core. Efeitos colaterais: sem `known_hosts` no MVP (o fingerprint é conferido a cada sessão) e refresh derruba a sessão ([[wiki/concepts/ticket-de-uso-unico-websocket]]). Ver [[wiki/concepts/terminal-web-broker-websocket-ssh]], [[wiki/concepts/defense-in-depth]].

## Key Sources

- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]
