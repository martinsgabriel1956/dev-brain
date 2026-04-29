---
type: concept
title: "SWR"
aliases: ["stale-while-revalidate", "vercel swr"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [swr, server-state, cache, frontend, vercel]
skill: tech-mentor-frontend
status: stable
---

# SWR

Biblioteca de server state da Vercel, alternativa mais leve ao [[tanstack-query]]. Nome vem da estratégia HTTP `stale-while-revalidate`: retorna dado do cache (stale) enquanto revalida em background.

## Uso básico

```typescript
import useSWR from "swr";

const fetcher = (url: string) => fetch(url).then(r => r.json());

function Orders() {
  const { data, error, isLoading, mutate } = useSWR("/api/orders", fetcher, {
    revalidateOnFocus: true,
    revalidateOnReconnect: true,
    refreshInterval: 30_000
  });

  // Refetch manual
  await mutate();

  // Atualiza cache sem refetch (optimistic)
  await mutate(updatedData, false);
}
```

## Comparativo com TanStack Query

| | SWR | TanStack Query |
|---|---|---|
| Bundle size | ~4KB | ~13KB |
| Mutations | `mutate` básico | `useMutation` completo |
| Optimistic updates | Manual | `onMutate` nativo |
| Infinite scroll | `useSWRInfinite` | `useInfiniteQuery` |
| Devtools | Não oficial | Oficial, excelente |
| Suspense | Sim | `useSuspenseQuery` |

## Quando usar SWR

✅ Projetos simples com poucos endpoints
✅ Bundle size crítico (ex: microfrontends, libs)
✅ Time pequeno, sem necessidade de devtools avançado

## Quando preferir TanStack Query

✅ Mutations complexas com callbacks
✅ Optimistic updates nativos
✅ Devtools visuais
✅ Projetos maiores com múltiplos domínios de cache

## Key Sources

- [[wiki/sources/tanstack-query-tudo-que-voce-precisa-saber]]
