---
type: source
title: "Distributed Locks, Redlock, Fencing Token e Consensus (Raft)"
aliases: ["redlock kleppmann", "raft leader election redis", "distributed lock raft"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 0
tags: [distributed-locks, redlock, fencing-token, raft, leader-election, martin-kleppmann, system-design]
skill: tech-mentor-system-design
status: draft
source_file: /home/nemomartins/Documentos/new/dev-study/raw/distributed-locks-raft.md
source_url:
author:
date_published:
date_ingested: 2026-04-23
---

# Distributed Locks, Redlock, Fencing Token e Consensus (Raft)

## TL;DR

Aprofundamento sobre locks distribuídos com foco na crítica de Martin Kleppmann ao Redlock (2016): GC pause e clock skew tornam o Redlock inseguro para operações de correção. Fencing token é a solução correta para ops críticas não-idempotentes. Leader election via Raft (etcd) é a alternativa para infraestrutura que exige consenso real.

## Key Claims

| Claim | Evidência |
|---|---|
| Redlock falha por GC pause — processo pausa após checar lock, lock expira, outro processo assume | Kleppmann 2016 — "How to do distributed locking" |
| Redlock falha por clock skew — instância Redis com clock adiantado expira TTL antes do esperado | Mesma fonte |
| Antirez (autor do Redis) responde: Redlock é adequado para locks de "eficiência", não "correção" | Post de resposta no blog do Redis |
| Fencing token é monotônico — recurso rejeita token menor que o último visto | Solução formal de Kleppmann |
| etcd implementa Raft com garantias linearizáveis | Usado por Kubernetes, CockroachDB, Consul |

## Conceitos

- [[concepts/distributed-lock]] — mecanismo geral
- [[concepts/fencing-token]] — proteção correta contra falhas de lock
- [[concepts/raft-paxos]] — consenso com garantias formais
- [[concepts/idempotencia]] — quando o lock simples é suficiente

## Entidades

- [[entities/martin-kleppmann]] — autor da crítica ao Redlock, "Designing Data-Intensive Applications"

## Key Sources

_Este é o documento primário._
