---
type: source
title: "Bulkhead"
aliases: ["bulkhead pattern", "thread pool isolation", "isolamento de recursos"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [resiliencia, bulkhead, thread-pool, isolamento, concorrencia, system-design]
skill: tech-mentor-system-design
source_file: /home/gabriel-martins/Documentos/dev-study/raw/bulkhead.md
source_url: ""
author: "tech-mentor skill"
date_published: 2026-03-27
date_ingested: 2026-04-22
status: stable
---

# Bulkhead

## TL;DR

Isola recursos (threads, conexões, semáforos) por downstream. Um serviço lento não esgota o pool dos outros. Analogia naval: compartimentos estanques — um inunda, o navio não afunda inteiro.

## Key Claims

- **Pool compartilhado sem bulkhead = blast radius total** — 1 serviço lento drena todas as threads; serviços críticos ficam sem recursos. → [[concepts/blast-radius]]
- **Bulkhead + Circuit Breaker são complementares** — circuit breaker decide SE tenta; bulkhead decide QUANTOS tentam ao mesmo tempo. Ordem: bulkhead envolve circuit breaker. → [[concepts/circuit-breaker]] [[concepts/bulkhead]]
- **Fail fast quando pool está cheio** — rejeitar em 1s é melhor que esperar 30s para falhar. `Promise.race` com timeout. → [[concepts/fail-fast]]
- **Dimensionamento via Little's Law** — `concorrência = throughput × latência_média`. Com margem de 2×. → [[concepts/littles-law]]
- **Chamadas assíncronas via fila já têm bulkhead implícito** — a fila é o compartimento. Bulkhead só é necessário com chamadas síncronas/concorrentes.
- **Métricas obrigatórias** — `pool_active`, `pool_queued`, `rejected_total` por serviço. Pool constantemente cheio = downstream lento ou pool subdimensionado.

## Entities

- [[entities/resilience4j]]
- [[entities/hystrix]]

## Concepts

[[concepts/bulkhead]] · [[concepts/circuit-breaker]] · [[concepts/blast-radius]] · [[concepts/fail-fast]] · [[concepts/littles-law]] · [[concepts/graceful-degradation]]

## Open Questions

- Qual o overhead de gerenciar N pools separados em serviços com 20+ downstreams?
- Bulkhead de semáforo (sem thread separada) vs pool de threads — quando cada um?

## Raw Quotes

> "Um serviço lento consumiu tudo — blast radius: 1 derrubou 3"

> "Circuit Breaker → decide SE tenta / Bulkhead → decide QUANTOS tentam ao mesmo tempo"

> "Rejeitar em 1s é melhor que esperar 30s para falhar"

> "Chamadas completamente assíncronas via fila — a fila já é o bulkhead"
