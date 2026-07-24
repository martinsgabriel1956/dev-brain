---
type: concept
title: "API Composition"
aliases: ["api composer", "composição de apis", "agregação de endpoints"]
date_created: 2026-07-23
date_updated: 2026-07-23
source_count: 1
tags: [api-composition, fan-out, aggregation-layer, api-gateway, bff]
skill: tech-mentor-backend
status: draft
---

# API Composition

Padrão em que um componente central — o **API Composer** — orquestra chamadas a múltiplos serviços/APIs e devolve um único resultado agregado ao cliente, descartando dados desnecessários no contexto ou adicionando dados úteis para aquela etapa de uso.

## Problema que Resolve

Um [[wiki/concepts/api-gateway]] sozinho resolve o problema de ponto único de entrada e roteamento, mas não resolve, por si só: (1) a necessidade do cliente fazer múltiplas requisições sequenciais para montar uma única tela, e (2) a falta de um objeto de retorno já lapidado para o contexto do cliente. API Composition ataca exatamente esses dois pontos.

## Fan-out — a Técnica Central

Chamar os serviços em paralelo em vez de sequencialmente:

```typescript
// ❌ Sequencial — latência = A + B + C
const user    = await userService.getById(userId);
const orders  = await orderService.getByUser(userId);
const balance = await walletService.getBalance(userId);

// ✅ Fan-out — latência = max(A, B, C)
const [user, orders, balance] = await Promise.all([
  userService.getById(userId),
  orderService.getByUser(userId),
  walletService.getBalance(userId),
]);
```

Para tolerar falhas parciais (um serviço fora do ar não deve derrubar a resposta inteira), usar `Promise.allSettled` em vez de `Promise.all`.

## Request Collapsing

Quando múltiplas chamadas por ID estão dispersas no código (padrão N+1), DataLoader agrupa chamadas feitas no mesmo tick em uma única chamada batched — técnica que não é exclusiva de GraphQL, aplicável a qualquer camada de composição.

## Onde Vive

O API Composer pode ser um componente dedicado ou, mais comumente na prática, a própria lógica de um [[wiki/concepts/bff-pattern]] — o BFF é, funcionalmente, um API Composer especializado para um único tipo de cliente.

## Key Sources

- [[wiki/sources/api-gateway-padrao-essencial-arquiteturas-distribuidas]]
