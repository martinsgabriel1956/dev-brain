---
type: concept
title: "Read-Your-Writes"
aliases: ["read your own writes", "consistency after write"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 2
tags: [banco-de-dados, consistência, read-replicas, redis, system-design, sistemas-distribuidos]
skill: tech-mentor-system-design
status: stable
---

# Read-Your-Writes

Garantia de que após escrever, o mesmo cliente sempre lê o valor escrito — mesmo com [[concepts/read-replicas]].

## Problema

Réplica tem replication lag. Usuário cria pedido, faz refresh, lê da réplica, não vê o pedido. Parece bug.

## Solução com Redis

```typescript
async function createOrder(data: CreateOrderDTO) {
  const order = await primary.order.create({ data });
  await redis.set(`force_primary:${data.userId}`, "1", "EX", 2); // força primário por 2s
  return order;
}

async function getOrders(userId: string) {
  const forcePrimary = await redis.get(`force_primary:${userId}`);
  const db = forcePrimary ? primary : replica;
  return db.order.findMany({ where: { userId } });
}
```

## Trade-off

Aumenta carga no primário temporariamente após escritas. Para workloads muito write-heavy, avalie se [[concepts/read-replicas]] fazem sentido.

## Contexto mais amplo

Submodelo de [[concepts/consistency-models]] — eventual consistency com a garantia mínima de que um cliente vê suas próprias escritas.

## Key Sources

- [[sources/banco-de-dados]]
- [[sources/modelos-de-consistencia]]
