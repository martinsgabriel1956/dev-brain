---
type: source
title: "CQRS — Command Query Responsibility Segregation"
aliases: ["Command Query Responsibility Segregation"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/cqrs.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-22
source_count: 0
tags: [cqrs, arquitetura, escalabilidade, read-model, write-model, eventual-consistency]
skill: tech-mentor-backend
status: stable
---

# CQRS — Command Query Responsibility Segregation

## TL;DR
CQRS separa operações que mudam estado (Commands) de operações que leem estado (Queries) em modelos distintos. O write model é normalizado e otimizado para integridade; o read model é desnormalizado e otimizado por query. A sincronização entre eles ocorre via eventos assíncronos.

## Claims Principais
| Claim | Confiança |
|---|---|
| Otimizar leitura e escrita no mesmo schema é um trade-off impossível de evitar sem separação | Alta |
| CQRS é um padrão para bounded contexts específicos, não para o sistema inteiro | Alta |
| A sincronização assíncrona implica eventual consistency no read model | Alta |
| O read model pode residir em bancos diferentes (Redis, Elasticsearch, MongoDB) do write model | Alta |
| Commands retornam void ou ID — nunca os dados completos | Média |

## Conceitos Abordados
- [[cqrs]]
- [[event-sourcing]]
- [[eventual-consistency]]
- [[read-model]]
- [[write-model]]
- [[projecao]]
- [[bounded-context]]
