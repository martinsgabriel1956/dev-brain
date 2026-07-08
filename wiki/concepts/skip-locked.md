---
type: concept
title: "SKIP LOCKED"
aliases: ["select for update skip locked", "skip locked postgresql", "fila no banco"]
date_created: 2026-04-22
date_updated: 2026-07-07
source_count: 2
tags: [postgresql, mysql, concorrencia, filas, sistemas-distribuidos, banco, reserva-de-estoque]
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

## Além de Filas de Job: Reserva de Estoque

O mesmo padrão se aplica fora do contexto de fila de job. A [[wiki/entities/shopify]] usa `SKIP LOCKED` no MySQL para reserva de estoque em e-commerce: em vez de uma coluna `estoque` numérica, cada unidade física vira uma linha própria na tabela. Reservar N unidades = travar e mover N linhas específicas numa única transação — workers concorrentes pulam linhas já reservadas em vez de esperar. Para produtos com estoque muito grande, um pool limitado (ex: 1.000 linhas por produto/local) é reabastecido automaticamente conforme esvazia. Ver [[wiki/concepts/mysql]] para os problemas de gap locking que precisaram ser corrigidos antes desse padrão escalar, e [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]] para o case completo.

O **[[wiki/concepts/solid-queue]]** da [[wiki/entities/37signals]] é outro exemplo — fila de background jobs inteira sobre banco relacional (MySQL/PostgreSQL/SQLite), sem broker externo.

## Key Sources

- [[wiki/sources/skip-locked-fencing-token]]
- [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]] — SKIP LOCKED aplicado a reserva de estoque (não fila de job), em escala de US$ 5,1M/minuto
