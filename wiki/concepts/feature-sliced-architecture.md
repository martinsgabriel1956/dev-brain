---
type: concept
title: "Feature-Sliced Architecture"
aliases: ["feature-based structure", "arquitetura por feature React", "feature slices"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [react, arquitetura, organização, escalabilidade, frontend-architecture]
skill: tech-mentor-frontend
status: stable
---

# Feature-Sliced Architecture

Organização de código React por **domínio/feature** em vez de por tipo de arquivo. Escala bem em aplicações médias e grandes.

## Estrutura

```
src/
  features/
    orders/
      components/   # OrderList, OrderCard, OrderForm
      hooks/        # useOrders, useOrderMutation
      api/          # queries TanStack Query
      types/        # order.types.ts
      index.ts      # barrel — API pública da feature
    customers/
    payments/
  shared/
    components/     # Button, Modal, Input — UI genérico
    hooks/          # useDebounce, useLocalStorage
    lib/            # queryClient, axios instance
    types/          # tipos globais
  app/              # routing, providers, layout
```

## Regras

- Features **não importam de outras features diretamente** — comunicam via `shared/` ou eventos
- `index.ts` exporta só a API pública — internals ficam encapsulados
- `shared/` contém apenas código genuinamente reutilizável

## Barrel export

```typescript
// features/orders/index.ts
export { OrderList } from "./components/OrderList";
export { useOrders } from "./hooks/useOrders";
export type { Order } from "./types/order.types";
// NÃO exporta internals
```

## Vs estrutura por tipo

```
❌ Por tipo (não escala):          ✅ Por feature (escala):
src/components/                    src/features/orders/
src/hooks/                         src/features/customers/
src/utils/                         src/shared/
```

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
