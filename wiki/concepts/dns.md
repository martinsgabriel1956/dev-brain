---
type: concept
title: "DNS — Domain Name System"
aliases: [Domain Name System]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [dns, rede, infraestrutura]
skill: tech-mentor-system-design
status: stub
---
# DNS — Domain Name System

Sistema que traduz nomes de domínio legíveis (ex: `api.empresa.com`) em endereços IP. É o primeiro componente atravessado por qualquer requisição. O fluxo de resolução percorre cache local → resolver recursivo → root NS → TLD NS → authoritative NS, cacheando cada nível pelo TTL configurado.

## Key sources
- [[sources/dns]]
