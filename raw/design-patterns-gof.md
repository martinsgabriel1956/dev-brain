---
date: 2026-04-13
tags: [tech-mentor, arquitetura, design-patterns, gof, padroes]
skill: tech-mentor-backend/references/design-principles
level: intermediário
---

# Design Patterns (GoF) — Os Essenciais

## Contexto

O livro "Design Patterns" (Gang of Four, 1994) cataloga 23 padrões de design OO. Na prática diária de um engenheiro backend/fullstack, ~8 deles aparecem com frequência real. Os demais são contextuais.

Esta nota foca nos que um Solutions Architect usa e reconhece em code review.

## Padrões Criacionais

### Factory Method

Delegue a criação de objetos para subclasses ou funções fábrica, em vez de instanciar diretamente com `new`:

```typescript
// Sem factory — acoplamento direto com implementação
const notifier = new EmailNotifier(config);  // e se precisar de SMS?

// Com factory — desacoplado da implementação concreta
type Notifier = {
  notify(userId: string, message: string): Promise<void>;
};

function createNotifier(channel: "email" | "sms" | "push"): Notifier {
  if (channel === "email") return new EmailNotifier(env.SMTP_CONFIG);
  if (channel === "sms") return new SmsNotifier(env.TWILIO_CONFIG);
  return new PushNotifier(env.FCM_CONFIG);
}

// UseCase não sabe qual implementação está usando
const notifier = createNotifier(user.preferredChannel);
await notifier.notify(user.id, "Seu pedido foi confirmado");
```

### Builder

Constrói objetos complexos passo a passo, especialmente útil para objetos com muitos parâmetros opcionais:

```typescript
// Sem Builder — construtor com 10 parâmetros opcionais é ilegível
const query = new Query("users", ["id", "name"], { age: { gte: 18 } }, "name", "asc", 0, 10);

// Com Builder — legível e flexível
const query = new QueryBuilder("users")
  .select(["id", "name", "email"])
  .where({ status: "active", age: { gte: 18 } })
  .orderBy("name", "asc")
  .limit(10)
  .offset(0)
  .build();
```

## Padrões Estruturais

### Adapter

Adapta a interface de uma classe para outra que o cliente espera. Exatamente o que fazemos em Hexagonal Architecture com Secondary Adapters:

```typescript
// Interface que o domínio conhece (Port)
type PaymentGateway = {
  charge(amount: number, currency: string, source: string): Promise<{ transactionId: string }>;
};

// Adapter do Stripe para a interface do domínio
class StripeAdapter implements PaymentGateway {
  private stripe: Stripe;

  constructor(apiKey: string) {
    this.stripe = new Stripe(apiKey);
  }

  async charge(amount: number, currency: string, source: string): Promise<{ transactionId: string }> {
    const charge = await this.stripe.charges.create({
      amount: Math.round(amount * 100),  // Stripe usa centavos
      currency,
      source
    });
    return { transactionId: charge.id };
  }
}
```

### Decorator

Adiciona responsabilidades a um objeto dinamicamente, sem alterar a classe original. Muito usado para logging, cache, rate limiting:

```typescript
// Interface base
type UserRepository = {
  findById(id: string): Promise<User | null>;
};

// Implementação base
class PrismaUserRepository implements UserRepository {
  async findById(id: string): Promise<User | null> {
    return prisma.user.findUnique({ where: { id } });
  }
}

// Decorator de cache — adiciona cache sem modificar PrismaUserRepository
class CachedUserRepository implements UserRepository {
  constructor(
    private wrapped: UserRepository,
    private cache: Redis
  ) {}

  async findById(id: string): Promise<User | null> {
    const cached = await this.cache.get(`user:${id}`);
    if (cached) return JSON.parse(cached);

    const user = await this.wrapped.findById(id);
    if (user) await this.cache.setex(`user:${id}`, 300, JSON.stringify(user));
    return user;
  }
}

// Composição: Prisma → Cache → (opcionalmente) Logger
const repo = new CachedUserRepository(
  new PrismaUserRepository(),
  redis
);
```

## Padrões Comportamentais

### Strategy

Encapsula algoritmos intercambiáveis. O cliente seleciona a estratégia em runtime:

```typescript
type PricingStrategy = {
  calculate(basePrice: number, user: User): number;
};

class RegularPricing implements PricingStrategy {
  calculate(basePrice: number): number { return basePrice; }
}

class PremiumPricing implements PricingStrategy {
  calculate(basePrice: number): number { return basePrice * 0.8; }  // 20% desconto
}

class EmployeePricing implements PricingStrategy {
  calculate(basePrice: number): number { return basePrice * 0.5; }  // 50% desconto
}

class PriceCalculator {
  constructor(private strategy: PricingStrategy) {}

  getPrice(basePrice: number, user: User): number {
    return this.strategy.calculate(basePrice, user);
  }
}

// Seleção em runtime
function getPricingStrategy(user: User): PricingStrategy {
  if (user.isEmployee) return new EmployeePricing();
  if (user.isPremium) return new PremiumPricing();
  return new RegularPricing();
}
```

### Observer

Define dependência um-para-muitos. Quando um objeto muda, todos os dependentes são notificados. É a base de event systems, reactive programming e Domain Events:

```typescript
type EventHandler<T> = (event: T) => void;

class EventEmitter<T> {
  private handlers: EventHandler<T>[] = [];

  subscribe(handler: EventHandler<T>): void {
    this.handlers.push(handler);
  }

  emit(event: T): void {
    this.handlers.forEach(h => h(event));
  }
}

// Domain object com events
class Order {
  private onOrderPlaced = new EventEmitter<{ orderId: string; total: number }>();

  get orderPlaced() { return this.onOrderPlaced; }

  place(): void {
    // regra de negócio...
    this.onOrderPlaced.emit({ orderId: this.id, total: this.total });
  }
}

// Subscribers reagem ao evento
order.orderPlaced.subscribe(event => emailService.sendConfirmation(event.orderId));
order.orderPlaced.subscribe(event => analyticsService.track("order_placed", event));
```

### Command

Encapsula uma requisição como objeto. Permite fila, log, undo/redo de operações:

```typescript
type Command = {
  execute(): Promise<void>;
  undo(): Promise<void>;
};

class PlaceOrderCommand implements Command {
  constructor(
    private orderRepository: OrderRepository,
    private orderData: CreateOrderInput
  ) {}

  async execute(): Promise<void> {
    const order = new Order(this.orderData);
    await this.orderRepository.save(order);
    this.savedOrder = order;
  }

  async undo(): Promise<void> {
    if (this.savedOrder) {
      await this.orderRepository.delete(this.savedOrder.id);
    }
  }

  private savedOrder?: Order;
}

// Command Queue — serializa execução, permite retry
class CommandQueue {
  private queue: Command[] = [];

  enqueue(command: Command): void { this.queue.push(command); }

  async executeAll(): Promise<void> {
    for (const command of this.queue) {
      await command.execute();
    }
  }
}
```

## Mapa Mental dos Padrões

```
Quando você precisa de...             Use...
──────────────────────────────────────────────────
Criar objetos sem acoplar ao tipo    Factory Method
Objeto complexo com muitos params    Builder
Adaptar interface incompatível       Adapter
Adicionar comportamento dinamicamente Decorator
Algoritmos intercambiáveis           Strategy
Notificação um-para-muitos           Observer
Operação como objeto (queue/undo)    Command
```

## Conceitos Relacionados

[[solid]] · [[clean-architecture]] · [[hexagonal-architecture]] · [[event-driven-architecture]] · [[integration-patterns]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-13*
