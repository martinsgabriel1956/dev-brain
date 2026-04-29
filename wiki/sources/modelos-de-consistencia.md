---
type: source
title: "Modelos de Consistência"
aliases: ["modelos de consistencia", "consistency models", "linearizability", "eventual consistency"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 0
tags: [sistemas-distribuidos, consistencia, linearizability, eventual-consistency, causal, cap-theorem, vector-clocks]
skill: tech-mentor-system-design
status: stable
source_file: /home/gabriel-martins/Documentos/dev-study/raw/modelos-de-consistencia.md
source_url: ""
author: ""
date_published: 2026-04-16
date_ingested: 2026-04-22
---

# Modelos de Consistência

## TL;DR

Consistência em sistemas distribuídos é um espectro, não binário. Quatro modelos do mais forte ao mais fraco: Linearizable → Sequential → Causal → Eventual. Armadilha mais comum: usar eventual para inventário (overselling) ou linearizable para contagem de views (gargalo desnecessário).

## Key Claims

**Claim:** Linearizability garante que qualquer leitura após uma escrita confirmada a verá — em qualquer nó. Requer Raft/Paxos, alta latência, baixa disponibilidade sob partição.
**Evidence:** etcd, Zookeeper, CockroachDB (serializable). Leitura linearizável vai ao líder — não a réplica. Custo: round-trip ao líder em cada operação.
**Confidence:** alta

**Claim:** Causal consistency garante que operações com relação causa-efeito são vistas na ordem correta por todos os nós. Implementado via Vector Clocks.
**Evidence:** `happensBefore(a, b)`: todos os counters de `a` ≤ `b` e ao menos um `<`. DynamoDB causal sessions, MongoDB sessions. Operações sem relação causal podem divergir em ordem.
**Confidence:** alta

**Claim:** Eventual consistency garante apenas convergência — sem prazo, sem ordem. Submodelos (Monotonic Read, Read Your Writes, Monotonic Write) adicionam garantias específicas.
**Evidence:** Cassandra padrão, DynamoDB `ConsistentRead: false`. DNS. Feed de redes sociais. DynamoDB com `ConsistentRead: true` = linearizável ao custo de 2× o preço de leitura.
**Confidence:** alta

**Claim:** Read Your Writes é o problema mais frequente em produção com réplicas — usuário escreve e imediatamente lê stale de réplica desatualizada.
**Evidence:** Solução: ler do primário por N segundos após escrita, ou sticky session na mesma réplica, ou timestamp de escrita no cliente para comparar com réplica.
**Confidence:** alta

**Claim:** Armadilha clássica: eventual consistency para inventário = overselling; linearizable para contagem de views = gargalo desnecessário.
**Evidence:** Inventário com oversell proibido requer linearizability (lock + decrement atômico). View count de vídeo pode convergir eventualmente — stale de 1s é irrelevante.
**Confidence:** alta

## Concepts & Entities Touched

[[concepts/consistency-models]] · [[concepts/read-your-writes]] · [[concepts/raft-paxos]] · [[concepts/split-brain]] · [[concepts/two-phase-commit]]

## Open Questions

- PACELC como extensão do CAP — vale um source próprio?
- CRDTs (Conflict-free Replicated Data Types) como alternativa a vector clocks — quando usar?
- Cassandra tunable consistency (ONE/QUORUM/ALL) — como mapear para os modelos aqui?
