---
type: source
title: "3PC — Three-Phase Commit"
aliases: ["three phase commit", "3pc", "protocolo de três fases"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [sistemas-distribuidos, consistencia, transacoes, 3pc, 2pc, raft, saga, system-design]
skill: tech-mentor-system-design
source_file: /home/gabriel-martins/Documentos/dev-study/raw/3pc.md
source_url: ""
author: "tech-mentor skill"
date_published: 2026-04-17
date_ingested: 2026-04-22
status: stable
---

# 3PC — Three-Phase Commit

## TL;DR

3PC adiciona fase intermediária (PreCommit) ao 2PC para evitar blocking quando o coordinator cai. Na prática, não é usado em produção porque assume ausência de partições de rede — que são comuns. Raft/Paxos resolvem o problema real. É conceito principalmente acadêmico.

## Key Claims

- **2PC tem blocking crítico** — se coordinator cai durante commit, participants ficam bloqueados com lock ativo indefinidamente. → [[concepts/two-phase-commit]]
- **3PC adiciona fase PreCommit** — permite participants se recuperar consultando uns aos outros sem o coordinator. → [[concepts/three-phase-commit]]
- **3PC não tolera partições de rede** — split-brain: A commita, B aborta, inconsistência. → [[concepts/split-brain]]
- **Raft e Paxos resolvem com quorum** — toleram partições, são usados em produção (etcd, CockroachDB, Kafka KRaft). → [[concepts/raft-paxos]]
- **Alternativas práticas para transações distribuídas** — Saga Pattern (compensação), Outbox + CDC (entrega sem locks), CockroachDB/Spanner (consenso correto). → [[concepts/saga-pattern]] [[concepts/outbox-pattern]] [[concepts/distributed-transactions]]

## Entities

- [[entities/etcd]]
- [[entities/cockroachdb]]
- [[entities/kafka]]

## Concepts

[[concepts/three-phase-commit]] · [[concepts/two-phase-commit]] · [[concepts/split-brain]] · [[concepts/raft-paxos]] · [[concepts/saga-pattern]] · [[concepts/outbox-pattern]] · [[concepts/distributed-transactions]]

## Open Questions

- Em quais bancos relacionais o 2PC ainda é usado em produção hoje?
- Saga orquestrado vs coreografado — quando cada um?

## Raw Quotes

> "3PC assume que partições de rede não ocorrem — só lida com falhas de crash."

> "Raft e Paxos resolvem com quorum — toleram partições de rede, algo que o 3PC não consegue."

> "Uso real do 3PC: acadêmico."
