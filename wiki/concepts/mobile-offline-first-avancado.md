---
type: concept
title: "Offline-First Avançado — Sync e Conflict Resolution"
aliases: ["mobile sync", "conflict resolution mobile", "delta sync mobile", "crdt mobile"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [mobile, offline-first, sync, conflict-resolution, crdt, delta-sync, idempotency]
skill: tech-mentor-mobile
status: stable
---

# Offline-First Avançado

## Delta Sync com Watermark

```sql
-- Buscar apenas registros alterados desde o último sync
SELECT * FROM products WHERE updated_at > :lastSyncTimestamp;
```

```ts
async function syncProducts(lastSync: Date) {
    const updated = await api.getProductsDelta(lastSync);
    await db.upsertProducts(updated);
    await storage.set('last_sync', new Date().toISOString());
}
```

Timestamp deve ser do **servidor** — não do cliente (clock skew).

## Fila de Operações Offline

```ts
type PendingOperation = {
    id: string; // idempotency key
    type: 'CREATE_ORDER' | 'UPDATE_CART';
    payload: unknown;
    createdAt: string;
};

async function processQueue() {
    const ops = await db.getPendingOps();
    for (const op of ops) {
        await api.execute(op); // idempotency key no header
        await db.deletePendingOp(op.id);
    }
}

NetInfo.addEventListener(state => {
    if (state.isConnected) processQueue();
});
```

## Conflict Resolution

| Estratégia | Quando usar | Risco |
|---|---|---|
| Last-Write-Wins (server timestamp) | Dados simples, um editor | Perde edições simultâneas |
| Last-Write-Wins (server authority) | Maioria dos casos | Justo mas pode surpreender |
| CRDT | Colaboração simultânea | Complexidade alta |
| Merge com review | Dados críticos (médico, financeiro) | Intervenção do usuário |

## CRDT para Colaboração

Y.js / Automerge para edição simultânea sem conflito — texto, listas, counters. Servidor armazena CRDT state, não snapshot final.

## Ver também

- [[mobile-offline-first-basico]] — fundamentos
- [[crdt-colaboracao-tempo-real]] — CRDT em profundidade
- [[idempotencia]] — idempotency key em operações

## Key Sources

- [[wiki/sources/mobile-offline-first-avancado]]
