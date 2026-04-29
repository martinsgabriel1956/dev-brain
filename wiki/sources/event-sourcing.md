---
type: source
title: "Event Sourcing"
aliases: []
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/event-sourcing.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-22
source_count: 0
tags: [event-sourcing, cqrs, ddd, auditoria, aggregate, eventstore]
skill: tech-mentor-backend
status: stable
---

# Event Sourcing

## TL;DR
Em vez de armazenar o estado atual, Event Sourcing persiste a sequência imutável de eventos que levou a esse estado. O estado é sempre derivado via replay. Oferece auditoria completa, time-travel e múltiplas projeções como consequências naturais do modelo.

## Claims Principais
| Claim | Confiança |
|---|---|
| O estado de um aggregate é sempre derivável via replay de todos os eventos | Alta |
| Eventos persistidos nunca devem ser modificados — use upcasters para migração de schema | Alta |
| Snapshots evitam replay longo em aggregates com muitos eventos (threshold recomendado: 50) | Alta |
| Time-travel (estado em qualquer ponto no tempo) é impossível em bancos state-based sem CDC | Alta |
| Optimistic locking é implementado nativamente via UNIQUE(stream_id, version) no event store | Alta |

## Conceitos Abordados
- [[event-sourcing]]
- [[aggregate]]
- [[event-store]]
- [[snapshot]]
- [[projecao]]
- [[upcaster]]
- [[optimistic-locking]]
- [[time-travel-query]]
