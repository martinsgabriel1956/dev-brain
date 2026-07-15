---
type: concept
title: "DNS — Domain Name System"
aliases: [Domain Name System]
date_created: 2026-04-22
date_updated: 2026-07-15
source_count: 2
tags: [dns, rede, infraestrutura]
skill: tech-mentor-system-design
status: stub
---
# DNS — Domain Name System

Sistema que traduz nomes de domínio legíveis (ex: `api.empresa.com`) em endereços IP. É o primeiro componente atravessado por qualquer requisição. O fluxo de resolução percorre cache local → resolver recursivo → root NS → TLD NS → authoritative NS, cacheando cada nível pelo TTL configurado.

DNS e [[wiki/concepts/porta-de-rede|porta]] resolvem endereçamento em camadas diferentes e complementares: DNS resolve nome → IP (qual host); a porta resolve IP → serviço (qual processo dentro daquele host). Uma requisição só chega ao destino final depois das duas resoluções.

## Key sources
- [[sources/dns]]
- [[wiki/sources/portas-de-rede-como-funcionam]] — DNS como resolução de nome, complementar à porta como resolução de serviço
