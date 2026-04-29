---
date: 2026-04-14
tags: [tech-mentor, backend, apis, graphql, federation]
skill: tech-mentor-backend/references/apis
level: avançado
---

# GraphQL

## Contexto

GraphQL é uma linguagem de query para APIs onde o cliente define exatamente quais campos quer — sem over-fetching (dados desnecessários) nem under-fetching (múltiplas chamadas para completar uma tela). Criado pelo Facebook em 2012 para resolver problemas de APIs mobile onde bandwidth é crítico e cada tela tem necessidades diferentes.

O ponto central de GraphQL não é substituir REST — é dar poder ao cliente de composição de dados.

## Como Funciona

### Schema First

```graphql
# schema.graphql — contrato da API
type Query {
  order(id: ID!): Order
  orders(userId: ID!, status: OrderStatus, first: Int, after: String): OrderConnection
}

type Mutation {
  createOrder(input: CreateOrderInput!): CreateOrderPayload
  cancelOrder(orderId: ID!): CancelOrderPayload
}

type Subscription {
  orderStatusChanged(orderId: ID!): Order
}

type Order {
  id: ID!
  user: User!
  items: [OrderItem!]!
  total: Float!
  status: OrderStatus!
  createdAt: DateTime!
}

type OrderItem {
  product: Product!
  quantity: Int!
  unitPrice: Float!
}

type User {
  id: ID!
  name: String!
  email: String!
}

enum OrderStatus {
  PENDING
  CONFIRMED
  SHIPPED
  DELIVERED
  CANCELLED
}

# Cursor-based pagination (padrão Relay)
type OrderConnection {
  edges: [OrderEdge!]!
  pageInfo: PageInfo!
}

type OrderEdge {
  node: Order!
  cursor: String!
}

type PageInfo {
  hasNextPage: Boolean!
  endCursor: String
}

input CreateOrderInput {
  items: [OrderItemInput!]!
  currency: String!
}

type CreateOrderPayload {
  order: Order
  errors: [UserError!]
}

type UserError {
  field: String
  message: String!
}
```

### Resolvers com DataLoader (N+1 Prevention)

O problema clássico de GraphQL: uma query que retorna 100 orders vai fazer 100 chamadas para buscar o `user` de cada order. DataLoader resolve com batching.

```typescript
import DataLoader from "dataloader";

// DataLoader cria um batch: em vez de 100 queries, faz 1 com WHERE id IN (...)
function createUserLoader(): DataLoader<string, User> {
  return new DataLoader(async (userIds: readonly string[]) => {
    const users = await prisma.user.findMany({
      where: { id: { in: [...userIds] } }
    });

    // DataLoader exige que o resultado esteja na mesma ordem dos IDs
    const userMap = new Map(users.map(u => [u.id, u]));
    return userIds.map(id => userMap.get(id) ?? new Error(`User ${id} not found`));
  });
}

// Context criado por request — cada request tem seu próprio DataLoader
type Context = {
  userLoader: DataLoader<string, User>;
  userId: string;
};

// Resolvers
const resolvers = {
  Query: {
    order: async (_: unknown, { id }: { id: string }, ctx: Context) => {
      return prisma.order.findUnique({ where: { id } });
    },

    orders: async (_: unknown, args: OrdersArgs, ctx: Context) => {
      const { userId, status, first = 10, after } = args;
      // Implementação de cursor-based pagination
      const orders = await prisma.order.findMany({
        where: { userId, status },
        take: first + 1,
        cursor: after ? { id: decodeCursor(after) } : undefined,
        orderBy: { createdAt: "desc" }
      });

      const hasNextPage = orders.length > first;
      const edges = orders.slice(0, first).map(order => ({
        node: order,
        cursor: encodeCursor(order.id)
      }));

      return { edges, pageInfo: { hasNextPage, endCursor: edges.at(-1)?.cursor } };
    }
  },

  Order: {
    // user field — batched pelo DataLoader
    user: (order: Order, _: unknown, ctx: Context) => {
      return ctx.userLoader.load(order.userId);
    },

    items: (order: Order) => {
      return prisma.orderItem.findMany({ where: { orderId: order.id } });
    }
  },

  Mutation: {
    createOrder: async (_: unknown, { input }: { input: CreateOrderInput }, ctx: Context) => {
      try {
        const order = await createOrderUseCase.execute({ userId: ctx.userId, ...input });
        return { order };
      } catch (error) {
        if (error instanceof ValidationError) {
          return { errors: [{ field: error.field, message: error.message }] };
        }
        throw error;
      }
    }
  }
};
```

### Persisted Queries — Performance em Produção

Queries inline são verbosas e repetitivas. Persisted Queries enviam apenas um hash, reduzindo payload drasticamente:

```typescript
// Cliente registra queries com hash SHA256
// Em vez de enviar a query completa, envia apenas o hash

// Cliente
const QUERY_HASH = "abc123def456"; // SHA256 da query
const response = await fetch("/graphql", {
  method: "POST",
  body: JSON.stringify({
    extensions: { persistedQuery: { version: 1, sha256Hash: QUERY_HASH } }
  })
});

// Servidor — Apollo Server com APQ (Automatic Persisted Queries)
import { ApolloServer } from "@apollo/server";
import { createPersistedQueryLink } from "@apollo/client/link/persisted-queries";

// Se hash não encontrado: cliente re-envia com a query completa
// Servidor armazena no cache (Redis) para próximas requests
```

### Schema-First com Proteção N+1 via Dataloader em Context

```typescript
import { ApolloServer } from "@apollo/server";

const server = new ApolloServer({
  typeDefs,
  resolvers,
  plugins: [
    // Depth limiting — previne queries maliciosas muito aninhadas
    // { user { orders { user { orders { ... } } } } }
    createDepthLimitPlugin({ maxDepth: 5 })
  ]
});

// Context factory — DataLoaders são por-request (não compartilhados entre requests)
const contextFactory = async ({ req }: { req: Request }): Promise<Context> => ({
  userId: extractUserId(req),
  userLoader: createUserLoader(),
  productLoader: createProductLoader()
});
```

### Federation v2 — GraphQL Distribuído

Em microsserviços, cada serviço pode expor seu próprio subgraph. O Apollo Router compõe em um único schema.

```graphql
# orders-service/schema.graphql
extend schema @link(url: "https://specs.apollo.dev/federation/v2.0")

type Order @key(fields: "id") {
  id: ID!
  userId: ID!
  total: Float!
  status: OrderStatus!
  # user é resolvido pelo users-service via @external
  user: User @requires(fields: "userId")
}

type User @key(fields: "id") @external {
  id: ID!
}
```

```graphql
# users-service/schema.graphql
type User @key(fields: "id") {
  id: ID!
  name: String!
  email: String!
  # orders são resolvidos pelo orders-service
  orders: [Order!]!
}

type Order @key(fields: "id") @external {
  id: ID!
}
```

## Trade-offs

| Aspecto | GraphQL | REST |
|---|---|---|
| **Flexibilidade do cliente** | Alta — cliente define exatamente o que quer | Baixa — servidor define o shape |
| **Cache HTTP** | Difícil — queries variam, POST não é cacheável nativamente | Fácil — GET com URL estável |
| **N+1** | Problema real — requer DataLoader | Menos comum — endpoints controlam joins |
| **Contrato** | Schema fortemente tipado | OpenAPI (opcional) |
| **File upload** | Workaround necessário (multipart) | Nativo |
| **Simplicidade** | Alta complexidade para times pequenos | Mais simples para APIs simples |
| **Tooling** | GraphiQL, Apollo Studio, Postman | Qualquer ferramenta HTTP |

## Quando Usar / Quando Evitar

**Usar GraphQL quando:**
- API consumida por múltiplos clientes com necessidades diferentes (web, mobile, third-party)
- Frontend precisa de composição flexível de dados sem N versões de endpoint
- Time grande com BFF pattern — GraphQL como aggregation layer
- Microsserviços com Federation — schema unificado sem gateway gigante

**Evitar quando:**
- API simples com poucos endpoints e shape estável — REST é mais direto
- Performance de cache HTTP é crítica — GraphQL não aproveita cache de borda nativamente
- Time não quer manter DataLoaders e gerenciar N+1 permanentemente
- API pública simples onde REST + OpenAPI é mais acessível para terceiros

## Conceitos Relacionados

[[api-gateway-bff]] · [[microsservicos]] · [[grpc]] · [[rate-limiting]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-14*
