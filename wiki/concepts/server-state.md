---
type: concept
title: "Server State"
aliases: ["estado do servidor", "remote state", "server data"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [server-state, cache, frontend, tanstack-query]
skill: tech-mentor-frontend
status: stable
---

# Server State

Dados que **vivem no servidor** e são apenas uma cópia local (snapshot) no cliente. Diferente do client state, o server state pode ficar desatualizado e precisa de revalidação.

## Características

- Assíncrono por natureza (fetch, loading, error)
- Pode ficar stale (desatualizado) a qualquer momento
- Precisa de cache para evitar requests redundantes
- Pode ser compartilhado entre componentes sem duplicar requests

## Separação de responsabilidades

```
Server State  → TanStack Query / SWR
Client State  → useState / useReducer / Zustand / Jotai
URL State     → nuqs
Form State    → React Hook Form
```

## Anti-padrão comum

Guardar server state em Zustand/Redux:

```typescript
// ❌ Boilerplate enorme, cache manual, sem devtools
const store = create(set => ({
  orders: [],
  loading: false,
  fetchOrders: async () => { ... }
}));

// ✅ TanStack Query — tudo resolvido
const { data, isLoading } = useQuery({ queryKey: ["orders"], queryFn: fetchOrders });
```

## Key Sources

- [[wiki/sources/tanstack-query-tudo-que-voce-precisa-saber]]
