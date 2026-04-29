---
date: 2026-04-13
tags: [tech-mentor, arquitetura, monolito-modular, bounded-modules]
skill: tech-mentor-system-design/references/architecture-patterns
level: intermediário
---
# Monolito Modular

## Contexto

Um Monolito Modular é um sistema **implantado como uma única unidade** mas com **boundaries de domínio bem definidos internamente**. É a resposta pragmática ao dilema "microsserviços vs monolito": você ganha organização de domínio sem pagar o custo operacional de rede distribuída.

O insight principal: **a maioria dos problemas atribuídos a monolitos são problemas de organização de código**, não de implantação. Microsserviços distribuem o problema para a rede — que é mais difícil de debugar.

Sam Newman (autor de "Building Microservices") defende: comece como monolito modular, extraia para serviços só quando houver razão concreta (escala independente, autonomia de deploy por time, falhas de isolamento).

## Como Funciona

### Princípio de Bounded Modules

Cada módulo (feature/domínio) é tratado como se fosse um microsserviço potencial:
- Tem seu próprio namespace/diretório
- Não acessa o banco de dados de outros módulos diretamente
- Se comunica via interfaces públicas bem definidas
- Contém seus próprios tipos, use cases, repositórios

```
src/
├── modules/
│   ├── orders/
│   │   ├── index.ts          ← public API do módulo
│   │   ├── domain/
│   │   │   └── order.entity.ts
│   │   ├── application/
│   │   │   ├── place-order.usecase.ts
│   │   │   └── cancel-order.usecase.ts
│   │   ├── infrastructure/
│   │   │   └── prisma-order.repository.ts
│   │   └── http/
│   │       └── order.controller.ts
│   ├── payments/
│   │   ├── index.ts          ← public API do módulo
│   │   └── ...
│   └── users/
│       ├── index.ts
│       └── ...
└── shared/
    ├── events/               ← eventos de integração entre módulos
    └── types/
```

### Comunicação Entre Módulos

**Regra de ouro: módulos se comunicam via interfaces públicas, nunca via imports diretos de internals.**

```typescript
// ❌ ERRADO — payments importa diretamente do internal de orders
import { OrderRepository } from "../orders/infrastructure/prisma-order.repository";

// ✅ CORRETO — payments usa a API pública de orders
import { OrdersModule } from "../orders";

// orders/index.ts — public API
export type { OrderId, OrderStatus } from "./domain/order.entity";
export { GetOrderByIdUseCase } from "./application/get-order-by-id.usecase";
// NÃO exporta: repositories, entities internas, queries de banco
```

### Comunicação via Eventos (In-Process)

Para comunicação assíncrona entre módulos sem criar acoplamento:

```typescript
// shared/events/event-bus.ts
type EventHandler<T> = (event: T) => Promise<void>;

class InProcessEventBus {
  private handlers = new Map<string, EventHandler<unknown>[]>();

  subscribe<T>(eventType: string, handler: EventHandler<T>): void {
    const existing = this.handlers.get(eventType) ?? [];
    this.handlers.set(eventType, [...existing, handler as EventHandler<unknown>]);
  }

  async publish<T>(eventType: string, event: T): Promise<void> {
    const handlers = this.handlers.get(eventType) ?? [];
    await Promise.all(handlers.map(h => h(event)));
  }
}

// orders/application/place-order.usecase.ts
class PlaceOrderUseCase {
  async execute(input: PlaceOrderInput): Promise<void> {
    const order = new Order(input);
    await this.orderRepository.save(order);

    // Publica evento — payments vai reagir sem acoplamento direto
    await this.eventBus.publish("order.placed", { orderId: order.id, total: order.total });
  }
}

// payments/application/payment-listener.ts
class PaymentListener {
  constructor(private eventBus: InProcessEventBus) {
    this.eventBus.subscribe("order.placed", this.handleOrderPlaced.bind(this));
  }

  private async handleOrderPlaced(event: { orderId: string; total: number }): Promise<void> {
    await this.processPayment(event.orderId, event.total);
  }
}
```

### Estratégia de Banco de Dados

**Opção 1 — Schema por módulo (recomendado):**

```sql
-- Cada módulo tem seu schema no PostgreSQL
CREATE SCHEMA orders;
CREATE SCHEMA payments;
CREATE SCHEMA users;

-- Tabelas ficam isoladas por namespace
CREATE TABLE orders.orders (id UUID PRIMARY KEY, ...);
CREATE TABLE payments.transactions (id UUID PRIMARY KEY, order_id UUID, ...);
```

**Opção 2 — Prefixo de tabela:**

```
orders_orders, orders_items
payments_transactions
users_accounts
```

**Regra:** módulo `payments` nunca executa `SELECT` diretamente em `orders.orders`. Se precisar de dados, chama a API pública do módulo `orders`.
### Migração para Microsserviços

Quando extrair um módulo para serviço separado:

```
Fase 1 (Monolito Modular):
  orders ←→ payments (via EventBus in-process)

Fase 2 (Extração):
  - Substitua InProcessEventBus por Kafka
  - Implante payments como serviço separado
  - orders continua publicando eventos (mesma interface)
  - payments agora consome do Kafka em vez do event bus local

Nada no código de orders muda — só a implementação do EventBus.
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Operacional | Deploy único, sem overhead de rede | Escala toda a aplicação junta |
| Desenvolvimento | Debugging local simples, sem service mesh | Risco de acoplamento silencioso entre módulos |
| Latência | Chamadas in-process (μs vs ms) | Falha de um módulo pode derrubar tudo |
| Migração | Boundaries já definidos facilitam extração | Banco compartilhado exige disciplina de isolamento |
| Time | Onboarding simples, uma única codebase | Times grandes brigam por branches |

## Quando Usar / Quando Evitar

**Usar quando:**
- Produto em fase inicial ou médio porte
- Time pequeno/médio (até ~50 devs)
- Lógica de negócio complexa que se beneficia de transactions locais
- Não há razão clara para escala independente entre domínios

**Considerar extração para microsserviços quando:**
- Um módulo específico tem carga desproporcionalmente maior
- Times diferentes precisam de autonomia de deploy para o mesmo módulo
- Falha de um módulo não pode afetar os demais (isolamento de blast radius)

## Vocabulário

### Boundary

Limite que separa responsabilidades, modelos ou sistemas — define o que entra, o que sai e quem é dono de cada pedaço. No Monolito Modular, boundaries são implementadas via interfaces públicas (`index.ts`) e isolamento de schema no banco.

Boundary que não está no código é só intenção — e intenções vazam. Uma boundary real impede imports diretos de internals, não apenas recomenda.

Boundaries aparecem em vários níveis:

| Nível | Mecanismo | Exemplo |
|---|---|---|
| Módulo | `index.ts` exporta só a API pública | `payments` importa de `orders/index`, nunca de `orders/infrastructure/...` |
| Banco | Schema por módulo no PostgreSQL | `payments` nunca faz `SELECT` em `orders.orders` |
| Domínio (DDD) | Bounded Context | Modelo `Order` em `Billing` ≠ modelo `Order` em `Fulfillment` |
| Serviço | API HTTP ou eventos | Microsserviço expõe contrato, não implementação |
| Arquitetura | Interface (port) | `UseCase` depende de `IOrderRepository`, não de `PrismaOrderRepository` |

## Conceitos Relacionados

[[clean-architecture]] · [[ddd-strategic]] · [[microsservicos]] · [[event-driven-architecture]] · [[bounded-context]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-13*
