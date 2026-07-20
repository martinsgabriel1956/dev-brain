---
type: entity
title: "HostGator"
aliases: ["HostGator", "HostGator VPS"]
date_created: 2026-07-20
date_updated: 2026-07-20
source_count: 1
tags: [empresa, hosting, vps, infra, patrocinio]
skill: tech-mentor-infra
status: stub
---

# HostGator

Provedora de hospedagem/VPS, patrocinadora da demo de [[wiki/concepts/blue-green-deploy|deploy blue/green]] de [[wiki/entities/augusto-galego]]. Oferece planos de VPS com servidores localizados no Brasil (latência menor para público local) e terminal web integrado além de acesso via SSH.

## Contexto de uso na demo

- Plano de VPS mais barato usado como ambiente de teste — suficiente para rodar [[wiki/concepts/reverse-proxy|Nginx]] + duas instâncias Node em paralelo.
- Apresentado como opção viável tanto para aprendizado quanto para produção real (SaaS/site próprio), com upgrade de plano disponível se a carga crescer.

## Key Sources

- [[wiki/sources/deploy-blue-green-na-pratica-vps-nginx]]
