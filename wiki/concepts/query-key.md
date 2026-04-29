---
type: concept
title: "Query Key"
aliases: ["queryKey", "chave de cache TanStack", "cache key"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [tanstack-query, cache, query-key]
skill: tech-mentor-frontend
status: stable
---

# Query Key

O `queryKey` é o **endereço do cache** no TanStack Query. Arrays são comparados por valor. Estruturar hierarquicamente permite invalidação granular.

## Fábrica de keys — padrão recomendado

```typescript
const orderKeys = {
  all: ["orders"] as const,
  lists: () => [...orderKeys.all, "list"] as const,
  list: (filters: OrderFilters) => [...orderKeys.lists(), filters] as const,
  details: () => [...orderKeys.all, "detail"] as const,
  detail: (id: string) => [...orderKeys.details(), id] as const
};
```

## Invalidação granular

```typescript
// Invalida todas as listas de orders (não os detalhes)
queryClient.invalidateQueries({ queryKey: orderKeys.lists() });

// Invalida só um pedido específico
queryClient.invalidateQueries({ queryKey: orderKeys.detail(id) });

// Invalida tudo relacionado a orders
queryClient.invalidateQueries({ queryKey: orderKeys.all });
```

## Regras

- Incluir todos os parâmetros que afetam o resultado no `queryKey`
- Filters, pagination, userId — tudo que muda o dado vai na key
- Keys iguais = mesmo cache = requests deduplicados

## Key Sources

- [[wiki/sources/tanstack-query-tudo-que-voce-precisa-saber]]
