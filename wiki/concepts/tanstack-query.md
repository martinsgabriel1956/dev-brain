---
type: concept
title: "TanStack Query"
aliases: ["React Query", "react-query", "tanstack-query", "@tanstack/react-query"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [tanstack-query, server-state, cache, frontend, react]
skill: tech-mentor-frontend
status: stable
---

# TanStack Query

Biblioteca de **gerenciamento de server state** para React. Resolve busca, cache, revalidação e sincronização de dados do servidor sem boilerplate manual.

## Modelo mental

Dados do servidor não são estado do cliente — são um **snapshot remoto** que envelhece. TanStack Query gerencia esse ciclo de vida automaticamente.

## O que você ganha de graça

- Cache automático por `queryKey`
- Deduplicação de requests simultâneos
- Retry automático em falha (padrão: 3x)
- Refetch ao focar janela / reconectar rede
- Loading, error e success states prontos
- Devtools visuais oficiais

## Setup

```typescript
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 60 * 1000,
      retry: 2
    }
  }
});

<QueryClientProvider client={queryClient}>
  <App />
  <ReactQueryDevtools />
</QueryClientProvider>
```

## Hooks principais

| Hook | Uso |
|---|---|
| `useQuery` | Leitura de dados |
| `useMutation` | Escrita / ações |
| `useInfiniteQuery` | Paginação / scroll infinito |
| `useSuspenseQuery` | Leitura com Suspense |
| `useQueryClient` | Acesso imperativo ao cache |

## staleTime vs gcTime

```
staleTime → quanto tempo o dado é "fresco" (sem refetch automático)
gcTime    → quanto tempo o dado fica no cache após não ter consumidores
```

## Vs useState + useEffect para fetch

`useState` + `useEffect` = sem cache, sem retry, sem deduplicação, sem devtools. TanStack Query resolve tudo isso.

## Ver também

- [[useQuery]] — detalhes de leitura
- [[useMutation]] — detalhes de escrita
- [[query-key]] — estratégia de cache
- [[optimistic-updates]] — UX de atualização instantânea
- [[swr]] — alternativa mais leve
- [[server-state]] — conceito base

## Key Sources

- [[wiki/sources/tanstack-query-tudo-que-voce-precisa-saber]]
