---
type: source
title: "Redis Avançado — Streams, Redlock, Eviction e Módulos"
aliases: ["redis avancado", "redis streams", "redlock", "eviction policies", "redis pub/sub", "redis modules"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/redis-avancado.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [redis, streams, redlock, eviction, pub-sub, consumer-groups, ack, pel, modules, redisvl, time-series]
skill: tech-mentor-data
status: stable
---

## TL;DR

Redis Streams é o log de eventos persistente com consumer groups e ACK — superior ao Pub/Sub para entrega garantida. Redlock é o distributed lock sem SPOF (5 nós, maioria). Eviction policies determinam o que acontece com dados quando memória fica cheia. Pub/Sub é fire-and-forget (sem persistência). Módulos: RedisSearch, TimeSeries, RedisVL (vetorial).

## Key Claims

**Claim:** Redis Streams >> Pub/Sub para entrega garantida — Pub/Sub é fire-and-forget.
**Evidence:** Pub/Sub: consumidor down = mensagens perdidas. Stream: mensagens persistidas, consumer group controla quem processou, ACK confirma processamento, PEL (Pending Entries List) rastreia mensagens não confirmadas. Para jobs críticos: Streams ou BullMQ (Redis-backed).
**Confidence:** alta

**Claim:** Redlock requer 5 nós independentes — 3 nós têm SPOF em caso de falha de rede.
**Evidence:** Algoritmo: adquire lock em maioria dos nós (≥3/5) com TTL curto. Se rede particiona e 2 nós ficam inacessíveis, o lock ainda é adquirido nos outros 3. Sem 5 nós: split-brain pode resultar em dois clientes com o lock simultaneamente.
**Confidence:** alta (com controvérsia — ver crítica de Martin Kleppmann)

**Claim:** Eviction policy errada pode destruir dados críticos — configurar por use case.
**Evidence:** `allkeys-lru`: remove qualquer key quando memória enche (cache puro). `volatile-lru`: remove apenas keys com TTL (preserva keys permanentes). `noeviction`: rejeita escritas quando cheio (útil para session store — não quer perder sessões). Configurar conscientemente.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/redis-streams]]
- [[concepts/redlock]]
- [[concepts/eviction-policies]]
- [[concepts/pub-sub-redis]]
- [[concepts/consumer-groups]]
- [[entities/martin-kleppmann]]

## Open Questions

- Redlock: Martin Kleppmann argumenta que Redlock não é safe sob clock drift — quando essa crítica é relevante em produção?
- Redis Streams vs Kafka: para qual volume de mensagens Redis Streams começa a ser limitante?
