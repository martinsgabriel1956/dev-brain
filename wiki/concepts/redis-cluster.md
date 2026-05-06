---
type: concept
title: "Redis Cluster"
aliases: ["redis cluster", "redis hash slots", "redis distributed"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 1
tags: [redis, cluster, hash-slots, cache, distributed-systems, infra]
skill: tech-mentor-infra
status: stub
---

# Redis Cluster

Modo distribuído do Redis que divide o keyspace em **16.384 hash slots** distribuídos entre nodes. Cada node é responsável por um range contínuo de slots.

**Como funciona:** `HASH_SLOT = CRC16(key) % 16384`. O client calcula o slot e redireciona a request para o node correto (ou o node redireciona via `MOVED`/`ASK`).

**Failover:** cada node primário tem ao menos uma réplica. Se o primário cai, a réplica assume. Nodes se comunicam via **gossip protocol** — sem coordinator centralizado.

**Limitações:**
- Multi-key operations só funcionam se todas as keys estão no mesmo slot (use hash tags `{user}:id`)
- Resharding requer migração de slots — pode ser feito sem downtime com `CLUSTER SETSLOT`

Relacionado a [[concepts/db-sharding]] — mesma lógica de consistent hashing, aplicada a cache.

## Key Sources

- [[sources/clusters]]
