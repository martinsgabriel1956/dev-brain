---
type: source
title: "SKIP LOCKED e Fencing Token"
aliases: ["skip locked", "fencing token", "select for update skip locked"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 0
tags: [sistemas-distribuidos, concorrencia, banco, filas, postgresql, redis, distributed-locks]
skill: tech-mentor-system-design
status: stable
source_file: /home/gabriel-martins/Documentos/dev-study/raw/skip-locked-fencing-token.md
source_url: ""
author: ""
date_published: 2026-04-17
date_ingested: 2026-04-22
---

# SKIP LOCKED e Fencing Token

## TL;DR

SKIP LOCKED transforma PostgreSQL em fila de trabalho sem broker externo — múltiplos workers consomem jobs em paralelo sem contenção. Fencing Token resolve o problema de lock "fantasma": processo lento ressuscita após lock expirar e acha que ainda tem o lock — token monotônico rejeita escritas stale.

## Key Claims

**Claim:** `SELECT FOR UPDATE SKIP LOCKED` permite múltiplos workers consumirem uma fila no PostgreSQL sem contenção entre eles.
**Evidence:** Sem SKIP LOCKED, workers usam locks pessimistas e se bloqueiam mutuamente. Com SKIP LOCKED, cada worker pula linhas já travadas e adquire a próxima disponível atomicamente dentro de uma transação. Suportado por PostgreSQL 9.5+ e MySQL 8+.
**Confidence:** alta

**Claim:** Para throughput até ~10k jobs/s, SKIP LOCKED elimina a necessidade de broker externo (RabbitMQ, SQS).
**Evidence:** Comparativo: SKIP LOCKED = infraestrutura zero adicional, ACID, exatamente-uma-vez, visibilidade via query direta. Kafka/SQS = milhões/s mas requer broker separado, DLQ nativo, complexidade operacional maior.
**Confidence:** alta

**Claim:** Prisma não suporta SKIP LOCKED nativamente — requer `$queryRaw` para a cláusula de lock, combinado com `$transaction`.
**Evidence:** Código TypeScript: `tx.$queryRaw<...>` para o SELECT + SKIP LOCKED, depois `tx.jobQueue.update` para marcar como processing — tudo dentro de `prisma.$transaction`.
**Confidence:** alta

**Claim:** Fencing Token resolve o problema de lock fantasma: processo lento ressuscita após TTL expirar e ambos os processos acreditam ter o lock.
**Evidence:** Fluxo: Processo A obtém lock (token=33) → fica lento → lock expira → Processo B obtém lock (token=34) → B escreve com token=34 → A ressuscita e tenta escrever com token=33 → storage rejeita (33 < 34). Token é monotonicamente crescente.
**Confidence:** alta

**Claim:** Redlock não implementa fencing tokens — para recursos onde corretude importa mais que disponibilidade, usar etcd ou ZooKeeper.
**Evidence:** Sem fencing token, falha de nó Redis pode conceder o mesmo lock a dois processos. etcd e ZooKeeper têm semântica de lease com token monotônico nativo.
**Confidence:** alta

## Concepts & Entities Touched

[[concepts/skip-locked]] · [[concepts/fencing-token]] · [[concepts/distributed-lock]] · [[concepts/two-phase-commit]] · [[concepts/raft-paxos]]

## Open Questions

- Dead Letter Queue com SKIP LOCKED — melhor abordagem para jobs que falham repetidamente?
- SKIP LOCKED com particionamento de tabela no PostgreSQL — mantém semântica de lock?
- Fencing token em sistemas com múltiplos storage backends — quem mantém o `lastToken`?
