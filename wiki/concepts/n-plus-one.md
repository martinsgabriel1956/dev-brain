---
type: concept
title: "N+1 Query Problem"
aliases: ["n+1", "n mais um", "n plus one"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [banco-de-dados, performance, orm, prisma, n-plus-one]
skill: tech-mentor-system-design
status: stable
---

# N+1 Query Problem

Bug de performance onde 1 query busca N registros e depois dispara N queries adicionais — uma por registro.

## Exemplo

```typescript
// ❌ N+1: 1 query para orders + N queries para cada user
const orders = await db.order.findMany();
for (const order of orders) {
  const user = await db.user.findUnique({ where: { id: order.userId } });
  // 100 pedidos = 101 queries
}

// ✅ 1 query com JOIN
const orders = await db.order.findMany({
  include: { user: true },
});
```

## Por que Acontece

ORMs lazy-load relacionamentos por padrão. O loop parece inofensivo mas é uma query por iteração.

## Diagnóstico

Habilite query logging no Prisma ou use `EXPLAIN ANALYZE`. Se ver dezenas de queries idênticas com IDs diferentes — é N+1.

## Solução Geral

Use `include`/`join` para carregar relacionamentos em uma única query com JOIN no banco.

## Key Sources

- [[sources/banco-de-dados]]
