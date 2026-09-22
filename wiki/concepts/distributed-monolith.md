---
type: concept
title: "Distributed Monolith"
aliases: []
date_created: 2026-09-22
date_updated: 2026-09-22
source_count: 3
tags: [distributed-monolith]
skill: tech-mentor-backend
status: stub
---

# Distributed Monolith

Stub criado durante sweep de lint (links quebrados) a partir de referências em 4 página(s) da wiki — conteúdo completo pendente de ingest dedicado.

## Contexto das citações

- Em [[wiki/concepts/microsservicos]]: O critério correto é decompor por **[[wiki/concepts/ddd-strategic|bounded context]]** (domínio de negócio), não por camada técnica. "Serviço de dados" + "Serviço de API" é um [[wiki/concepts/distributed-monolith|distributed monolith]] técnico disfarçado de microsserviços; "Orders Service" + "Payments Service" é decomposição real por domínio, com dados isolados e deploy independente.
- Em [[wiki/sources/anti-patterns]]: [[concepts/distributed-monolith]]
- Em [[wiki/sources/microsservicos-historia-soa-esb-bernardo-lobato]]: **Confiança:** Alta — idêntico ao princípio de **database per service** já central em [[wiki/concepts/microsservicos]] (seção "Decomposição Correta": "Serviço de dados" + "Serviço de API" é [[wiki/concepts/distributed-monolith]] disfarçado) e ao anti-padrão "Shared Database" listado em `references/architecture-foundations.md` da skill. O autor promete um vídeo futuro questionando essa regra aplica
- Em [[wiki/sources/microsservicos]]: [[concepts/distributed-monolith]]

## Pendências

Página não nasceu de um ingest próprio; TL;DR acima é reconstruído apenas a partir do texto das páginas que a citam. Precisa de fonte dedicada para virar `draft`/`stable`.

## Key sources

- [[wiki/concepts/microsservicos]]
- [[wiki/sources/anti-patterns]]
- [[wiki/sources/microsservicos-historia-soa-esb-bernardo-lobato]]
- [[wiki/sources/microsservicos]]
