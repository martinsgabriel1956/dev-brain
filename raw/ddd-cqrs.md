---
date: 2026-04-17
tags: [tech-mentor, ddd, cqrs, arquitetura, backend]
skill: tech-mentor-system-design/references/ddd
level: avançado
---

# DDD com CQRS

## Contexto
DDD e CQRS são frequentemente mencionados juntos mas têm responsabilidades distintas: **DDD** define *como modelar o domínio*, **CQRS** define *como estruturar as operações sobre esse domínio*. A combinação é poderosa porque resolve uma tensão real: o modelo de domínio otimizado para *escrita* (invariantes, aggregates, consistência) raramente é ideal para *leitura* (queries desnormalizadas, filtros complexos, performance).

## O Problema Sem CQRS

```typescript
// Aggregate rico — correto para escrita
class Order {
  private items: OrderItem[] = [];
  private status: OrderStatus;

  addItem(product: Product, quantity: number) {
    // validações, invariantes, eventos de domínio...
  }
}

// Mas para exibir "lista de pedidos do usuário com total e status"
// o mesmo aggregate vira um pesadelo — N+1, joins complexos,
// dados desnormalizados necessários
const orders = await orderRepository.findByUser(userId);
// carrega aggregates completos só para mostrar uma listagem
```

## A Solução: Separar Command Model do Query Model

```
                    ┌──────────────────────┐
                    │    Application Layer  │
                    └──────────┬───────────┘
                   ┌───────────┴───────────┐
                   ▼                       ▼
          ┌────────────────┐    ┌─────────────────────┐
          │  Command Side  │    │     Query Side       │
          │                │    │                      │
          │  Aggregate     │    │  Read Model          │
          │  Domain Events │    │  (desnormalizado)    │
          │  Repository    │    │  Query Service       │
          └───────┬────────┘    └──────────┬───────────┘
                  │                        │
          ┌───────▼────────┐    ┌──────────▼───────────┐
          │  Write DB      │    │  Read DB             │
          │  (PostgreSQL   │    │  (PostgreSQL view,   │
          │   normalized)  │    │   Redis, ES, etc.)   │
          └────────────────┘    └──────────────────────┘
                  │
                  │ Domain Event → projeção
                  └──────────────────────────────────►
```

## Código de Referência

### Command Side — mantém o Aggregate

```typescript
// Command
type PlaceOrderCommand = {
  customerId: string;
  items: Array<{ productId: string; quantity: number }>;
};

// Command Handler — usa o Aggregate para aplicar regras de negócio
class PlaceOrderCommandHandler {
  constructor(private orderRepo: OrderRepository) {}

  async handle(command: PlaceOrderCommand) {
    const customer = await this.customerRepo.findById(command.customerId);
    const order = Order.create(customer, command.items); // invariantes validadas aqui
    await this.orderRepo.save(order);
    // order.domainEvents → publicados após salvar
  }
}
```

### Query Side — Read Model otimizado para leitura

```typescript
// Read Model — estrutura flat para a UI
type OrderSummary = {
  id: string;
  customerId: string;
  customerName: string;   // desnormalizado
  totalAmount: number;    // pré-calculado
  itemCount: number;      // pré-calculado
  status: string;
  createdAt: Date;
};

// Query Service — direto ao banco de leitura, sem passar pelo aggregate
class OrderQueryService {
  async getOrdersByCustomer(customerId: string): Promise<OrderSummary[]> {
    return this.db.query<OrderSummary[]>(`
      SELECT
        o.id,
        o.customer_id,
        c.name AS customer_name,
        SUM(oi.price * oi.quantity) AS total_amount,
        COUNT(oi.id) AS item_count,
        o.status,
        o.created_at
      FROM orders o
      JOIN customers c ON c.id = o.customer_id
      JOIN order_items oi ON oi.order_id = o.id
      WHERE o.customer_id = $1
      GROUP BY o.id, c.name, o.status, o.created_at
    `, [customerId]);
  }
}
```

### Projeção — sincroniza Command para Query Side

```typescript
// Event Handler que atualiza o Read Model
class OrderPlacedProjector {
  async on(event: OrderPlacedEvent) {
    await this.readDb.query(`
      INSERT INTO order_summaries (id, customer_id, customer_name, total_amount, item_count, status, created_at)
      VALUES ($1, $2, $3, $4, $5, $6, $7)
      ON CONFLICT (id) DO UPDATE SET
        total_amount = EXCLUDED.total_amount,
        status = EXCLUDED.status
    `, [
      event.orderId,
      event.customerId,
      event.customerName,
      event.totalAmount,
      event.itemCount,
      "placed",
      event.occurredAt
    ]);
  }
}
```

## Consistência Eventual no Read Model

O Read Model é **eventually consistent** — há um lag entre o Command ser processado e o Read Model ser atualizado. Para a maioria dos casos isso é aceitável. Para casos onde não é (ex: "não exibir o mesmo produto disponível para dois compradores"), a leitura deve ir direto ao Write DB ou usar CQRS com consistência síncrona (mais raro).

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Performance | Read Model otimizado, sem joins complexos | Duplicação de dados entre Write e Read |
| Complexidade de domínio | Aggregate focus em regras, não em queries | Mais código: Commands, Handlers, Projectors |
| Escalabilidade | Read e Write escalados independentemente | Consistência eventual exige tratamento de lag |
| Testabilidade | Command Handlers testáveis sem infraestrutura de query | Projectors precisam de testes próprios |

## Quando Usar / Quando Evitar

**Usar quando:**
- O modelo de leitura difere significativamente do modelo de escrita (relatórios, dashboards)
- Read é 10x+ mais frequente que Write — justifica otimização de leitura separada
- Já há Event Sourcing — CQRS é natural nesse contexto

**Evitar quando:**
- CRUD simples onde o mesmo modelo serve leitura e escrita
- Time sem experiência com consistência eventual — bugs sutis são comuns
- A projeção adiciona complexidade sem ganho real de performance

## Conceitos Relacionados
[[cqrs]] · [[event-sourcing]] · [[ddd-tactical]] · [[ddd-strategic]] · [[outbox-pattern]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-17*
