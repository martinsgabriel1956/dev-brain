---
date: 2026-04-17
tags: [tech-mentor, sistemas-distribuidos, concorrencia, banco, filas]
skill: tech-mentor-system-design/references/distributed-systems
level: avançado
---

# SKIP LOCKED e Fencing Token

## SKIP LOCKED

### Contexto
`SELECT ... FOR UPDATE SKIP LOCKED` é uma instrução SQL (suportada por PostgreSQL 9.5+ e MySQL 8+) que permite implementar **filas de trabalho diretamente no banco de dados** sem precisar de um broker externo como RabbitMQ ou SQS.

O problema clássico: múltiplos workers consultam a mesma tabela de jobs. Sem SKIP LOCKED, usam-se locks pessimistas — um worker trava e os outros esperam. Com SKIP LOCKED, cada worker pula linhas já travadas e pega a próxima disponível.

### Como Funciona

```sql
-- Schema da fila
CREATE TABLE job_queue (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  payload     JSONB NOT NULL,
  status      TEXT NOT NULL DEFAULT 'pending',
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  locked_at   TIMESTAMPTZ,
  locked_by   TEXT
);

-- Worker: busca o próximo job disponível e trava atomicamente
BEGIN;

SELECT id, payload
FROM job_queue
WHERE status = 'pending'
ORDER BY created_at
LIMIT 1
FOR UPDATE SKIP LOCKED;  -- pula linhas travadas por outros workers

-- Se encontrou um job:
UPDATE job_queue
SET status = 'processing', locked_at = NOW(), locked_by = $worker_id
WHERE id = $job_id;

COMMIT;
```

### Implementação em TypeScript (com Prisma)

```typescript
async function claimNextJob(workerId: string) {
  return await prisma.$transaction(async tx => {
    // Prisma não suporta SKIP LOCKED nativamente — usar $queryRaw
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

async function completeJob(jobId: string) {
  await prisma.jobQueue.update({
    where: { id: jobId },
    data: { status: "completed" }
  });
}

// Loop do worker
async function workerLoop(workerId: string) {
  while (true) {
    const job = await claimNextJob(workerId);
    if (!job) {
      await new Promise(r => setTimeout(r, 1000)); // sem job, aguarda
      continue;
    }
    await processJob(job);
    await completeJob(job.id);
  }
}
```

### Quando usar SKIP LOCKED vs. broker externo

| Critério | SKIP LOCKED (PostgreSQL) | Kafka / RabbitMQ / SQS |
|---|---|---|
| Infraestrutura | Já tem PostgreSQL | Precisa de broker separado |
| Throughput | Até ~10k jobs/s com tuning | Milhões/s |
| Garantias | ACID — exatamente uma vez | Depende do broker |
| Visibilidade | Query direta na tabela | Dashboard do broker |
| Dead Letter | UPDATE status = 'failed' manual | DLQ nativo |
| Complexidade | Baixa | Alta |

---

## Fencing Token

### Contexto
Problema clássico de Distributed Locks: um processo obtém o lock, fica lento (GC pause, swap, rede lenta), o lock expira, outro processo obtém o lock e começa a operar — aí o primeiro processo "ressuscita" e **ambos acreditam ter o lock simultaneamente**.

**Fencing Token** resolve isso: ao conceder o lock, o servidor retorna um **token monotonicamente crescente**. O recurso protegido verifica se o token é o mais recente — tokens antigos são rejeitados.

### Como Funciona

```
Processo A obtém lock → token = 33
Processo A fica lento (GC pause 30s)
Lock expira
Processo B obtém lock → token = 34
Processo B escreve com token=34 → aceito pelo storage

Processo A "ressuscita" e tenta escrever com token=33
Storage: "33 < 34, token antigo" → REJEITA
```

### Implementação

```typescript
// Servidor de lock (ex: Redis ou etcd)
class LockServer {
  private fenceCounter = 0;

  async acquireLock(key: string, ttl: number): Promise<{ token: number } | null> {
    const acquired = await redis.set(key, "locked", { NX: true, EX: ttl });
    if (!acquired) return null;

    this.fenceCounter++;
    await redis.set(`${key}:token`, this.fenceCounter);
    return { token: this.fenceCounter };
  }
}

// Storage protegido — verifica o token antes de aceitar escritas
class ProtectedStorage {
  private lastToken = 0;

  async write(data: unknown, fencingToken: number): Promise<void> {
    if (fencingToken <= this.lastToken) {
      throw new Error(`Stale lock: token ${fencingToken} ≤ current ${this.lastToken}`);
    }
    this.lastToken = fencingToken;
    // ... persiste os dados
  }
}

// Cliente
async function doWork(lockServer: LockServer, storage: ProtectedStorage) {
  const lock = await lockServer.acquireLock("resource:123", 30);
  if (!lock) return; // lock não disponível

  // Passa o token para todas as operações no recurso protegido
  await storage.write({ data: "..." }, lock.token);
}
```

### Limitação do Redlock
O **Redlock** (algoritmo de lock distribuído do Redis) é frequentemente criticado exatamente por não implementar fencing tokens. Em caso de falha de nó Redis, o mesmo lock pode ser concedido a dois processos. Para recursos críticos onde a corretude importa mais que a disponibilidade, use etcd ou ZooKeeper que têm semântica de lease com token monotônico.

## Conceitos Relacionados
[[distributed-locks]] · [[raft-leader-election]] · [[two-phase-commit]] · [[idempotencia]] · [[kafka]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-17*
