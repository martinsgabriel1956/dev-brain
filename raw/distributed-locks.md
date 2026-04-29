---
date: 2026-04-14
tags: [tech-mentor, backend, distributed-systems, concorrência, redis]
skill: tech-mentor-backend/references/distributed-systems
level: avançado
---

# Distributed Locks

## Contexto

Em sistemas distribuídos, múltiplas instâncias do mesmo serviço podem tentar modificar o mesmo recurso simultaneamente. Locks de banco de dados (SELECT FOR UPDATE) funcionam dentro de uma transação, mas não entre processos ou serviços. Locks distribuídos resolvem coordenação entre processos independentes.

Casos de uso clássicos: evitar que dois workers processem o mesma mensagem, garantir que um cron job rode em apenas uma instância, proteger operações de inventário.

## Como Funciona

### Redis NX (Set if Not Exists)

O padrão mais simples e pragmático. Usa a atomicidade do Redis para garantir que apenas um processo adquire o lock.

```typescript
type DistributedLock = {
  acquire: () => Promise<boolean>;
  release: () => Promise<void>;
};

function createDistributedLock(redis: Redis, key: string, ttlMs: number): DistributedLock {
  const lockKey = `lock:${key}`;
  const lockValue = crypto.randomUUID(); // valor único por processo/instância

  return {
    async acquire() {
      // SET key value NX PX ttl — atômico no Redis
      // NX = só seta se não existir
      // PX = TTL em milissegundos (evita lock eterno se processo crasha)
      const result = await redis.set(lockKey, lockValue, "NX", "PX", ttlMs);
      return result === "OK";
    },

    async release() {
      // Lua script garante atomicidade: só deleta se o valor é o mesmo que setamos
      // Evita deletar lock de outro processo que adquiriu após nosso TTL expirar
      const script = `
        if redis.call("get", KEYS[1]) == ARGV[1] then
          return redis.call("del", KEYS[1])
        else
          return 0
        end
      `;
      await redis.eval(script, 1, lockKey, lockValue);
    }
  };
}

// Uso
async function processInventory(productId: string) {
  const lock = createDistributedLock(redis, `inventory:${productId}`, 5000);

  const acquired = await lock.acquire();
  if (!acquired) {
    throw new LockNotAcquiredError(productId);
  }

  try {
    await updateInventory(productId);
  } finally {
    await lock.release(); // sempre libera, mesmo com erro
  }
}
```

### Redlock — Lock Multi-nó

Para ambientes com múltiplos nodes Redis independentes (sem replicação master-replica), Redlock oferece garantias de segurança mais fortes: adquire o lock em maioria dos nodes (N/2 + 1).

```typescript
import Redlock from "redlock";

const redlock = new Redlock([redis1, redis2, redis3], {
  retryCount: 3,
  retryDelay: 200,  // ms entre tentativas
  retryJitter: 100  // randomização para evitar thundering herd
});

async function processPayment(paymentId: string) {
  // acquirindo lock por 5 segundos
  const lock = await redlock.acquire([`payment:${paymentId}`], 5000);

  try {
    await chargeCard(paymentId);
    await lock.extend(5000); // estende se a operação demorar mais que o TTL
  } finally {
    await lock.release();
  }
}
```

**Limitação do Redlock:** Martin Kleppmann argumentou (2016) que Redlock não é seguro contra pausas de GC longas ou drift de relógio. Para sistemas financeiros críticos: use etcd ou PostgreSQL Advisory Locks.

### PostgreSQL Advisory Lock

Para operações que já estão em uma transação de banco de dados, Advisory Locks são mais simples e mais seguros:

```typescript
// Session-level: mantido até a conexão fechar
await prisma.$executeRaw`SELECT pg_advisory_lock(hashtext(${resourceId}))`;

try {
  await processResource(resourceId);
} finally {
  await prisma.$executeRaw`SELECT pg_advisory_unlock(hashtext(${resourceId}))`;
}

// Transaction-level: liberado automaticamente ao commit/rollback
await prisma.$transaction(async tx => {
  await tx.$executeRaw`SELECT pg_advisory_xact_lock(hashtext(${orderId}))`;
  // lock é liberado automaticamente no commit
  await processOrder(tx, orderId);
});
```

### SKIP LOCKED — Processamento de Filas no Banco

Para jobs em banco de dados, SKIP LOCKED permite que múltiplos workers processem jobs diferentes sem contenção:

```sql
-- Worker 1 pega o próximo job disponível sem bloquear outros workers
BEGIN;
SELECT id, payload FROM jobs
WHERE status = 'pending'
ORDER BY created_at
LIMIT 1
FOR UPDATE SKIP LOCKED;

-- Outros workers que executam a mesma query pulam este job e pegam o próximo
```

```typescript
async function claimNextJob(tx: PrismaTransaction) {
  // Prisma não suporta SKIP LOCKED nativamente — usar $queryRaw
  const [job] = await tx.$queryRaw<Job[]>`
    SELECT id, payload, type
    FROM jobs
    WHERE status = 'pending'
    ORDER BY created_at ASC
    LIMIT 1
    FOR UPDATE SKIP LOCKED
  `;

  if (!job) return null;

  await tx.$executeRaw`
    UPDATE jobs SET status = 'processing', started_at = NOW()
    WHERE id = ${job.id}
  `;

  return job;
}
```

### Fencing Token

Mesmo com lock distribuído, um processo pode segurar o lock além do TTL (GC pause, swap) e depois tentar escrever no recurso. Fencing Token previne isso.

```
Processo A adquire lock → token=33
Processo A fica pausado (GC)
Lock expira → Processo B adquire lock → token=34
Processo B escreve com token=34
Processo A "acorda" → tenta escrever com token=33
Servidor de storage rejeita: "token 33 < 34, operação rejeitada"
```

```typescript
// Servidor de storage verifica que o token é monotonicamente crescente
async function writeWithFencing(resourceId: string, data: unknown, fencingToken: number) {
  const current = await redis.get(`fence:${resourceId}`);
  const currentToken = current ? parseInt(current) : 0;

  if (fencingToken <= currentToken) {
    throw new StaleTokenError(`Token ${fencingToken} rejeitado, atual é ${currentToken}`);
  }

  await redis.set(`fence:${resourceId}`, fencingToken.toString());
  await writeToStorage(resourceId, data);
}
```

## Trade-offs

| Solução | Quando usar | Limitação |
|---|---|---|
| **Redis NX** | Locks simples com instância Redis única | Perde lock se Redis master cai antes de replicar |
| **Redlock** | Redis multi-node sem cluster | Vulnerável a GC pauses longas (argumento Kleppmann) |
| **PostgreSQL Advisory** | Operações já em transação de banco | Requer conexão ativa com banco |
| **SKIP LOCKED** | Fila de jobs em banco de dados | Só funciona para filas, não para recursos genéricos |
| **etcd/Consul** | Locks em infraestrutura crítica | Overhead operacional de manter cluster etcd |

## Quando Usar / Quando Evitar

**Usar quando:**
- Dois workers não podem processar o mesmo recurso simultaneamente
- Cron job distribuído (apenas uma instância deve executar)
- Reserva de estoque com múltiplos serviços simultâneos

**Evitar quando:**
- A operação pode ser tornada idempotente (preferível — não precisa de lock)
- O problema pode ser resolvido com SERIALIZABLE isolation no banco
- A critical section é muito longa → TTL curto causa expiração, TTL longo bloqueia muito

## Conceitos Relacionados

[[idempotencia]] · [[saga-pattern]] · [[cap-pacelc-consistencia]] · [[retry-backoff]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-14*
