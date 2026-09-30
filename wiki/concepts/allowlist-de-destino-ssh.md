---
type: concept
title: "Allowlist de Destino SSH (Egress)"
aliases: ['allowlist ssh', 'allowed cidr', 'egress allowlist', 'omxterm_ssh_allowed_cidr']
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [allowlist, ssh, seguranca, firewall, ssrf, tech-mentor-security]
skill: tech-mentor-security
status: draft
---

# Allowlist de Destino SSH (Egress)

Um broker que abre SSH para onde o usuário mandar é um vetor de SSRF/pivô. Em [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]] a variável `OMXTERM_SSH_ALLOWED_CIDR` lista os destinos permitidos; o autor libera **IP por IP** (VPN, residência, outras VPS) em vez de `/24`, o que segue "allowlist > blocklist" `[skill: tech-mentor-security]` ([[wiki/concepts/principio-do-menor-privilegio]]).

Armadilha operacional: a regra vale em duas camadas — no app e no **UFW** — e o IP interno da rede Docker precisa ser conhecido por ambos; por isso o autor fixou IPs de Traefik e OMXTerm numa rede Docker dedicada (IP dinâmico causou falhas). Ver [[wiki/concepts/dns-rebinding]], [[wiki/concepts/hardening-de-servidor]], [[wiki/concepts/defense-in-depth]].

## Key Sources

- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]
