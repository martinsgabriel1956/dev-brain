---
type: source
title: "Distributed Locks"
aliases: ["distributed lock", "redis lock", "redlock", "advisory lock"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 0
tags: [distributed-locks, redis, redlock, fencing-token, postgresql, skip-locked, system-design]
skill: tech-mentor-system-design
status: draft
source_file: /home/nemomartins/Documentos/new/dev-study/raw/distributed-locks.md
source_url:
author:
date_published:
date_ingested: 2026-04-23
---

# Distributed Locks

## TL;DR

Locks distribuídos garantem exclusão mútua entre processos em diferentes máquinas. Redis SET NX EX é a solução mais comum para operações idempotentes. Redlock (multi-nó) oferece mais garantias mas não é seguro para operações críticas não-idempotentes por causa de GC pause e clock skew. Para operações críticas, usar fencing token. Para filas no banco, SKIP LOCKED. Para consenso real, etcd/ZooKeeper.

## Key Claims

| Claim | Evidência |
|---|---|
| Redis SET NX é atômico e suficiente para ops idempotentes | Single-node, SET key "1" NX EX TTL |
| Redlock não é seguro para correção estrita | GC pause pode expirar o lock antes do processo executar |
| Fencing token rejeita escritas de lock expirado | Token monotônico validado pelo recurso, não pelo cliente |
| SKIP LOCKED permite fila sem broker externo | SELECT FOR UPDATE SKIP LOCKED no PostgreSQL, até ~10k/s |
| PostgreSQL advisory lock é session-scoped | Libera automaticamente se a conexão cair |

## Conceitos

- [[concepts/distributed-lock]] — exclusão mútua distribuída
- [[concepts/fencing-token]] — proteção contra lock fantasma
- [[concepts/skip-locked]] — fila no PostgreSQL
- [[concepts/idempotencia]] — pré-requisito para locks mais simples
- [[concepts/raft-paxos]] — consenso real via etcd/ZooKeeper

## Key Sources

_Este é o documento primário._
