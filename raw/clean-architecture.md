---
date: 2026-04-13
tags: [tech-mentor, arquitetura, clean-architecture]
skill: tech-mentor-system-design/references/architecture-patterns
level: intermediário
---
# Clean Architecture

## Contexto

Proposta por Robert Martin (Uncle Bob), a Clean Architecture define **onde as regras de negócio vivem** e como o código se organiza para que a lógica de domínio seja independente de frameworks, bancos de dados, UI e qualquer detalhe externo. É uma evolução direta da Hexagonal Architecture e da Onion Architecture — todas compartilham o mesmo princípio central.

O valor prático: você consegue substituir o banco de dados, trocar de framework HTTP ou testar toda a lógica de negócio sem subir nenhuma infraestrutura.
## Como Funciona

### A Dependency Rule

A regra fundamental: **dependências só apontam para dentro**. Camadas externas dependem de camadas internas, nunca o contrário.

```
           ┌────────────────────────────────┐
           │  Frameworks & Drivers          │  ← Web, DB, UI, devices
           │  ┌──────────────────────────┐  │
           │  │  Interface Adapters      │  │  ← Controllers, Presenters, Gateways
           │  │  ┌────────────────────┐  │  │
           │  │  │  Application       │  │  │  ← Use Cases
           │  │  │  ┌──────────────┐  │  │  │
           │  │  │  │  Entities    │  │  │  │  ← Domain (Enterprise Business Rules)
           │  │  │  └──────────────┘  │  │  │
           │  │  └────────────────────┘  │  │
           │  └──────────────────────────┘  │
           └────────────────────────────────┘
```

### As 4 Camadas

**Entities (Domain)**
- Regras de negócio puras da empresa
- Não dependem de nada externo
- Mudam só quando as regras do negócio mudam

```typescript
// Entity — lógica de negócio pura, sem import externo
class Order {
  private items: OrderItem[];
  private status: OrderStatus;

  addItem(item: OrderItem): void {
    if (this.status !== OrderStatus.DRAFT) {
      throw new OrderNotEditableError(this.id);
    }
    this.items.push(item);
  }

  calculateTotal(): Money {
    return this.items.reduce((acc, item) => acc.add(item.subtotal()), Money.zero());
  }
}
```

**Use Cases (Application)**
- Regras de negócio específicas da aplicação
- Orquestram entities e chamam ports (interfaces de saída)
- Um Use Case = uma regra de negócio = um arquivo

```typescript
// Use Case — orquestração, sem conhecer Express, Prisma, etc.
class PlaceOrderUseCase {
  constructor(
    private orderRepository: OrderRepository,  // interface, não implementação
    private paymentGateway: PaymentGateway,
    private eventBus: EventBus
  ) {}

  async execute(input: PlaceOrderInput): Promise<PlaceOrderOutput> {
    const order = await this.orderRepository.findById(input.orderId);
    if (!order) throw new OrderNotFoundError(input.orderId);

    const payment = await this.paymentGateway.charge(order.calculateTotal(), input.paymentMethod);

    order.markAsPaid(payment.transactionId);
    await this.orderRepository.save(order);
    await this.eventBus.publish(new OrderPlacedEvent(order));

    return { orderId: order.id, status: order.status };
  }
}
```

**Interface Adapters**
- Convertem dados entre o formato dos Use Cases e o formato externo (HTTP, DB, etc.)
- Controllers, Presenters, Repository implementations

```typescript
// Controller — converte HTTP → UseCase input
class OrderController {
  constructor(private placeOrderUseCase: PlaceOrderUseCase) {}

  async placeOrder(req: Request, res: Response): Promise<void> {
    const input: PlaceOrderInput = {
      orderId: req.params.id,
      paymentMethod: req.body.paymentMethod
    };

    const output = await this.placeOrderUseCase.execute(input);
    res.json({ success: true, data: output });
  }
}
```

**Frameworks & Drivers**
- Express, Fastify, Prisma, Stripe SDK, etc.
- Detalhes de implementação que não devem vazar para dentro

### Inversão de Controle (DI)

Use Cases dependem de **interfaces** (ports), não de implementações concretas. A implementação concreta é injetada na composição (Main):

```typescript
// Port (interface definida na camada de Application)
type OrderRepository = {
  findById(id: string): Promise<Order | null>;
  save(order: Order): Promise<void>;
};

// Adapter (implementação na camada de Frameworks)
class PrismaOrderRepository implements OrderRepository {
  async findById(id: string): Promise<Order | null> {
    const raw = await prisma.order.findUnique({ where: { id } });
    return raw ? OrderMapper.toDomain(raw) : null;
  }

  async save(order: Order): Promise<void> {
    await prisma.order.upsert({
      where: { id: order.id },
      update: OrderMapper.toPersistence(order),
      create: OrderMapper.toPersistence(order)
    });
  }
}

// Main — composição (único lugar que conhece tudo)
const orderRepository = new PrismaOrderRepository();
const paymentGateway = new StripePaymentGateway(process.env.STRIPE_KEY);
const placeOrderUseCase = new PlaceOrderUseCase(orderRepository, paymentGateway, eventBus);
const orderController = new OrderController(placeOrderUseCase);
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Testabilidade | Use Cases testáveis com mocks simples | Mais arquivos e boilerplate inicial |
| Manutenibilidade | Mudança de banco não afeta regras de negócio | Curva de aprendizado para o time |
| Independência de framework | Troca de Express por Fastify sem tocar domínio | Overhead de mapeamento Domain ↔ Persistence |
| Boundaries explícitos | Fica óbvio onde cada coisa pertence | Verbosidade em CRUD simples |

## Quando Usar / Quando Evitar

**Usar quando:**
- Lógica de negócio complexa com muitas regras
- Time grande que precisa de boundaries claros
- Expectativa de trocar infraestrutura (banco, framework, etc.)
- Cobertura de testes é prioridade

**Evitar quando:**
- CRUD simples sem regras de negócio reais (over-engineering)
- Time pequeno ou protótipo com prazo curto
- Regras de negócio triviais que não justificam o overhead de mapeamento

## Conceitos Relacionados

[[hexagonal-architecture]] · [[ddd-tactical]] · [[dependency-injection]] · [[solid]] · [[use-cases]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-13*
