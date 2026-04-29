---
type: concept
title: "Infinite Query"
aliases: ["useInfiniteQuery", "infinite scroll", "paginação cursor"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [tanstack-query, paginação, infinite-scroll, ux]
skill: tech-mentor-frontend
status: stable
---

# Infinite Query

Hook do TanStack Query para **paginação baseada em cursor** e **scroll infinito**. Acumula páginas no cache conforme o usuário avança.

## useInfiniteQuery

```typescript
const {
  data,
  fetchNextPage,
  hasNextPage,
  isFetchingNextPage
} = useInfiniteQuery({
  queryKey: ["orders", "infinite"],
  queryFn: ({ pageParam }) => fetchOrders({ cursor: pageParam, limit: 20 }),
  initialPageParam: null,
  getNextPageParam: lastPage => lastPage.nextCursor ?? undefined
});

// Todas as páginas acumuladas
const allOrders = data?.pages.flatMap(page => page.orders) ?? [];
```

## Scroll automático com IntersectionObserver

```typescript
const sentinelRef = useRef<HTMLDivElement>(null);
const entry = useIntersectionObserver(sentinelRef, { threshold: 0.1 });

useEffect(() => {
  if (entry?.isIntersecting && hasNextPage && !isFetchingNextPage) {
    fetchNextPage();
  }
}, [entry?.isIntersecting, hasNextPage, isFetchingNextPage]);

return (
  <ul>
    {allOrders.map(o => <OrderItem key={o.id} order={o} />)}
    <div ref={sentinelRef}>
      {isFetchingNextPage && <Spinner />}
    </div>
  </ul>
);
```

## Cursor vs Offset pagination

| | Cursor | Offset (`page=1&limit=10`) |
|---|---|---|
| Consistência | Alta (não pula itens) | Baixa (inserts mudam páginas) |
| Performance DB | Alta (index scan) | Baixa em páginas tardias |
| Scroll infinito | Ideal | Problemático |
| Links diretos | Difícil | Fácil |

## Key Sources

- [[wiki/sources/tanstack-query-tudo-que-voce-precisa-saber]]
