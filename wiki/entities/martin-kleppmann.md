---
type: entity
title: "Martin Kleppmann"
aliases: ["kleppmann"]
date_created: 2026-04-23
date_updated: 2026-09-22
source_count: 3
tags: [distributed-systems, author, redlock, crdt, designing-data-intensive-applications]
skill: tech-mentor-system-design
status: stub
---

# Martin Kleppmann

Pesquisador e autor britânico especializado em sistemas distribuídos. Professor na Universidade de Cambridge.

**Obras principais:**
- "Designing Data-Intensive Applications" (O'Reilly, 2017) — referência definitiva em sistemas distribuídos
- Post "How to do distributed locking" (2016) — crítica formal ao Redlock do Redis

**Contribuições relevantes no wiki:**
- Crítica ao Redlock: demonstrou que GC pause e clock skew tornam o Redlock inseguro para operações de correção estrita.
- Pesquisa em CRDTs: contribuições ao Y.js e formalização de algoritmos de colaboração em tempo real.

## Designing Data-Intensive Applications Como Leitura em Andamento

[[wiki/sources/o-que-estudar-vale-a-pena-aprender-programar-com-ia]] cita *Designing Data-Intensive Applications* como compra recente, primeira leitura em andamento — endossado como referência para conceitos de escala de enterprise (streaming de eventos, multitenancy, joins, locks, transações, índices, snapshots), consistente com a descrição já registrada nesta entity como "referência definitiva em sistemas distribuídos". Ver também [[wiki/concepts/livros-recomendados-programador]] e [[wiki/concepts/arquitetura-de-software]].

## Key Sources

- [[wiki/sources/redis-avancado]] — Redis Streams é o log de eventos persistente com consumer groups e ACK — superior ao Pub/Sub para entrega garantida. Redlock é o distributed lock sem SPOF (5 nós, maioria). Eviction policies...
- [[wiki/sources/o-que-estudar-vale-a-pena-aprender-programar-com-ia]] — DDIA citado como leitura recente/em andamento, endossado para conceitos de escala enterprise
- [[sources/distributed-locks-raft]]
