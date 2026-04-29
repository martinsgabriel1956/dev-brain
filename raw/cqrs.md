---
date: 2026-03-27
tags: [tech-mentor, system-design, escalabilidade, cqrs, arquitetura, read-model, write-model]
skill: tech-mentor-system-design/references/messaging-patterns.md
level: intermediário
---

# CQRS — Command Query Responsibility Segregation

## Contexto

Operações que mudam estado (Commands) e operações que leem estado (Queries) têm requisitos tão diferentes que deveriam usar modelos separados. Otimizar para leitura (desnormalização, índices para joins complexos) conflita com otimizar para escrita (normalização, menos índices). A mesma tabela não pode ser perfeitamente otimizada para os dois.

## Como Funciona

### A Separação Fundamental

```
Command side (Write Model):        Query side (Read Model):

┌─────────────────────┐            ┌──────────────────────────┐
│  Normalized tables  │            │  Denormalized views       │
│  (ACID, constraints)│            │  (otimizadas por query)   │
│  orders             │   sync     │  order_summaries          │
│  order_items        │ ────────→  │  (order + user + items    │
│  users              │  (event)   │   já joinados e prontos)  │
└─────────────────────┘            └──────────────────────────┘
       ↑                                       ↑
  PlaceOrderCommand                   GetOrdersByUserQuery
  CancelOrderCommand                  GetOrderDashboardQuery
```

## Código de Referência

### Command — muda estado, retorna void ou ID

```typescript
type PlaceOrderCommand = {
  userId: string;
  items: OrderItem[];
  shippingAddress: Address;
};

async function placeOrder(command: PlaceOrderCommand): Promise<string> {
  const user = await userRepository.findById(command.userId);
  if (!user.isActive) throw new UserInactiveError(command.userId);

  const order = await db.$transaction(async tx => {
    const order = await tx.order.create({
      data: { userId: command.userId, status: "pending" }
    });
    await tx.orderItem.createMany({
      data: command.items.map(item => ({ ...item, orderId: order.id }))
    });
    return order;
  });

  // Publica evento para sincronizar o read model
  await eventBus.publish("order.placed", { orderId: order.id, ...command });

  return order.id; // só retorna o ID — não os dados
}
```

### Query — lê estado, nunca muda nada

```typescript
type GetOrdersByUserQuery = {
  userId: string;
  status?: string;
  page: number;
  limit: number;
};

async function getOrdersByUser(query: GetOrdersByUserQuery) {
  // Lê do read model — já desnormalizado, sem JOIN em runtime
  return db.orderSummary.findMany({
    where: { userId: query.userId, status: query.status },
    skip: (query.page - 1) * query.limit,
    take: query.limit
  });
}
```

### Sincronização Assíncrona via Eventos

```typescript
// Write side: publica evento, não sabe nada do read model
async function placeOrder(command: PlaceOrderCommand) {
  const order = await db.order.create({ data: { ... } });
  await eventBus.publish("order.placed", { orderId: order.id });
  return order.id;
}

// Projection: consome evento e atualiza read model independentemente
eventBus.subscribe("order.placed", async event => {
  const order = await db.order.findUnique({
    where: { id: event.orderId },
    include: { items: true, user: true }
  });

  await db.orderSummary.upsert({
    where: { orderId: event.orderId },
    create: {
      orderId: order.id,
      userId: order.userId,
      userName: order.user.name,
      itemCount: order.items.length,
      totalCents: order.items.reduce((sum, i) => sum + i.priceCents, 0),
      status: order.status
    },
    update: { status: order.status }
  });
});
```

### Read Model é um Banco Diferente

```
Write Model → PostgreSQL (ACID, normalizado)
                    ↓ eventos
Read Models:
  → Redis          (listas de feed, contadores)
  → Elasticsearch  (busca full-text)
  → PostgreSQL     (views materializadas simples)
  → MongoDB        (documentos desnormalizados)
```

## Trade-offs

| Aspecto | CRUD Tradicional | CQRS |
|---|---|---|
| **Complexidade** | Baixa | Alta — dois modelos, sync, eventual consistency |
| **Performance de leitura** | Limitada pelo schema normalizado | Read model otimizado por query |
| **Performance de escrita** | Boa | Igual ou melhor (menos índices no write model) |
| **Consistência** | Forte (imediata) | Eventual (assíncrono) ou forte (síncrono) |
| **Flexibilidade de query** | JOINs em runtime | Pré-computado — qualquer estrutura |
| **Audit/debug** | Difícil rastrear mudanças | Commands explícitos = audit log natural |

## Quando Usar / Quando Evitar

**Use CQRS quando:**
- ✅ Queries complexas degradam performance de writes na mesma tabela
- ✅ Read e write têm cargas muito diferentes (ex: 1000 leituras por 1 escrita)
- ✅ Múltiplas representações do mesmo dado para usos diferentes
- ✅ Você quer audit log natural (todo Command é um registro de intenção)

**Evite CQRS quando:**
- ❌ CRUD simples — criar/listar/editar/deletar sem regras complexas
- ❌ Time pequeno sem experiência com eventual consistency
- ❌ Consistência forte é requisito em todas as operações
- ❌ O domínio é simples demais para justificar dois modelos

> CQRS não é uma arquitetura para o sistema todo — é um padrão para **bounded contexts específicos** onde leitura e escrita têm requisitos genuinamente diferentes.

## Conceitos Relacionados

[[fase-2-escalabilidade]] · [[event-sourcing]] · [[mensageria]] · [[banco-de-dados]] · [[db-sharding]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-27*
