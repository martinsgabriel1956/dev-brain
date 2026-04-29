---
type: concept
title: "SKIP LOCKED"
aliases: ["select for update skip locked", "skip locked postgresql", "fila no banco"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [postgresql, concorrencia, filas, sistemas-distribuidos, banco]
skill: tech-mentor-system-design
status: stable
---

# SKIP LOCKED

`SELECT ... FOR UPDATE SKIP LOCKED` — instrução SQL que permite múltiplos workers consumirem uma fila de jobs no banco sem contenção. Cada worker pula linhas já travadas e adquire atomicamente a próxima disponível.

Suportado por PostgreSQL 9.5+ e MySQL 8+.

## Schema e Query

```sql
CREATE TABLE job_queue (
  id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  payload    JSONB NOT NULL,
  status     TEXT NOT NULL DEFAULT 'pending',
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  locked_at  TIMESTAMPTZ,
  locked_by  TEXT
);

BEGIN;
SELECT id, payload
FROM job_queue
WHERE status = 'pending'
ORDER BY created_at
LIMIT 1
FOR UPDATE SKIP LOCKED;

UPDATE job_queue
SET status = 'processing', locked_at = NOW(), locked_by = $worker_id
WHERE id = $job_id;
COMMIT;
```

## TypeScript com Prisma

Prisma não suporta SKIP LOCKED nativamente — usar `$queryRaw` dentro de `$transaction`:

```typescript
async function claimNextJob(workerId: string) {
  return await prisma.$transaction(async tx => {
    const [job] = await tx.$queryRaw<Array<{ id: string; payload: unknown }>>`
      SELECT id, payload
      FROM job_queue
      WHERE status = 'pending'
      ORDER BY created_at
      LIMIT 1
      FOR UPDATE SKIP LOCKED
    `;

    if (!job) return null;

    await tx.jobQueue.update({
      where: { id: job.id },
      data: { status: "processing", lockedAt: new Date(), lockedBy: workerId }
    });

    return job;
  });
}
```

## Quando Usar vs Broker Externo

| Critério | SKIP LOCKED | Kafka / SQS |
|---|---|---|
| Infraestrutura | Já tem PostgreSQL | Broker separado |
| Throughput | Até ~10k jobs/s | Milhões/s |
| Garantias | ACID, exatamente uma vez | Depende do broker |
| Visibilidade | Query direta na tabela | Dashboard do broker |
| Complexidade | Baixa | Alta |

## Key Sources

- [[sources/skip-locked-fencing-token]]
