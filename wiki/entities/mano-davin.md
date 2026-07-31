---
type: entity
title: "Mano Davin (Find My SaaS)"
aliases: ["davin", "mano davin", "find my saas", "manodeivin"]
date_created: 2026-07-31
date_updated: 2026-07-31
source_count: 1
tags: [criador-conteudo, youtube, saas, seguranca, devops]
skill: tech-mentor-security
status: stub
---

# Mano Davin (Find My SaaS)

Criador de conteúdo de tecnologia no YouTube (canal descrito como "o canal mais chorume de tecnologia do YouTube", com lives regulares terças e quintas 10h; Instagram @manodeivin), autor e operador do SaaS "Find My SaaS". Trata conteúdo técnico com forte foco recente em segurança — vazamentos de empresas, vulnerabilidades em ferramentas populares — descrito como "novo hiperfoco" do canal.

## Incidente relatado

Em [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]], narra em primeira pessoa um ataque de [[wiki/concepts/ddos-syn-flood|SYN flood]] de 260 milhões de requests em um dia contra o próprio Find My SaaS — 6 horas de indisponibilidade, servidor não recuperado (reconstruído do zero), causado pela combinação de modo Under Attack desativado no [[wiki/concepts/waf|Cloudflare]] com um bug de CPU/memory leak no Traefik (auto-atualizado pelo [[wiki/concepts/coolify]]). Usou [[wiki/entities/hostinger]] como provedora de VPS antes e depois do incidente.

## Key Sources

- [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]]
