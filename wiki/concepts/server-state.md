---
type: concept
title: "Server State"
aliases: ["estado do servidor", "remote state", "server data"]
date_created: 2026-04-22
date_updated: 2026-11-16
source_count: 4
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

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]], os itens, as UFs e as cidades são estado de servidor guardados à mão em `useState` + `useEffect`. `[skill: tech-mentor-frontend]` A skill recomenda TanStack Query para cache, deduplicação, cancelamento e estados de loading e erro.

## Na NLW #2, dia 3 (Diego Fernandes)

Lista de professores e total de conexões em `useState` + chamada manual: sem loading, sem erro e sem estado vazio. A skill sugere TanStack Query para esse tipo de dado. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]].

## Na NLW #2, dia 5 (Diego Fernandes)

Os favoritos guardam o objeto inteiro do professor, que fica desatualizado; a lista não tem loading, erro nem estado vazio (Diego sente falta da "mensagem de vazio"). Ver [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]].

## Key Sources

- [[wiki/sources/tanstack-query-tudo-que-voce-precisa-saber]]
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: fetch manual em useState no Ecoleta
- [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]]: NLW #2, Diego, dia 3: teachers e totalConnections em useState
- [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]]: NLW #2, Diego, dia 5: favorito congelado e lista sem estados
