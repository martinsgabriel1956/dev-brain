---
date: 2026-04-13
tags: [tech-mentor, backend, ddd, tactical-design, aggregate, entity, value-object]
skill: tech-mentor-backend/references/ddd
level: avançado
---

# DDD — Tactical Design

## Contexto

Tactical Design é o conjunto de padrões de implementação do DDD: como modelar entities, value objects, aggregates e a lógica de negócio dentro de um Bounded Context.

É o que diferencia um modelo de domínio rico (com regras de negócio na entidade) de um Anemic Domain Model (entidade só com getters/setters, regras espalhadas em services).

## Blocos de Construção

### Entity

Tem **identidade** — dois objetos com mesmo ID são o mesmo, mesmo que todos os outros atributos sejam diferentes. Tem ciclo de vida (criado, atualizado, desativado).

```typescript
class User {
  private readonly _id: UserId;
  private _name: string;
  private _email: Email;  // Value Object
  private _status: UserStatus;

  private constructor(props: UserProps, id?: UserId) {
    this._id = id ?? UserId.generate();
    this._name = props.name;
    this._email = props.email;
    this._status = UserStatus.PENDING;
  }

  static create(props: UserProps): User {
    if (!props.name || props.name.trim().length < 2) {
      throw new InvalidUserNameError(props.name);
    }
    return new User(props);
  }

  static reconstitute(props: UserProps, id: UserId): User {
    return new User(props, id);  // para reconstruir do banco sem validações de criação
  }

  activate(): void {
    if (this._status !== UserStatus.PENDING) {
      throw new UserAlreadyActiveError(this._id.value);
    }
    this._status = UserStatus.ACTIVE;
  }

  get id(): UserId { return this._id; }
  get email(): Email { return this._email; }
}
```

### Value Object

Não tem identidade — é definido pelos seus **atributos**. É **imutável**. Dois Value Objects com os mesmos atributos são iguais.

```typescript
class Money {
  private constructor(
    private readonly _amount: number,
    private readonly _currency: string
  ) {}

  static of(amount: number, currency: string): Money {
    if (amount < 0) throw new NegativeAmountError(amount);
    if (!["BRL", "USD", "EUR"].includes(currency)) throw new InvalidCurrencyError(currency);
    return new Money(amount, currency);
  }

  add(other: Money): Money {
    if (this._currency !== other._currency) throw new CurrencyMismatchError();
    return Money.of(this._amount + other._amount, this._currency);
  }

  multiply(factor: number): Money {
    return Money.of(this._amount * factor, this._currency);
  }

  equals(other: Money): boolean {
    return this._amount === other._amount && this._currency === other._currency;
  }

  get amount(): number { return this._amount; }
  get currency(): string { return this._currency; }
}

class Email {
  private constructor(private readonly _value: string) {}

  static of(value: string): Email {
    const normalized = value.toLowerCase().trim();
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(normalized)) {
      throw new InvalidEmailError(value);
    }
    return new Email(normalized);
  }

  equals(other: Email): boolean { return this._value === other._value; }
  get value(): string { return this._value; }
}
```

### Aggregate

Um Aggregate é um **cluster de objetos** (Entities + Value Objects) tratado como uma unidade para fins de consistência de dados. O **Aggregate Root** é a entidade raiz que controla o acesso.

**Regras fundamentais:**
1. Objetos externos referenciam apenas o Aggregate Root (nunca entities internas)
2. Toda invariante do negócio é mantida dentro dos limites do Aggregate
3. Uma transaction = uma mudança em um Aggregate
4. Aggregates diferentes se comunicam via Domain Events

```typescript
// Order é o Aggregate Root
class Order {
  private readonly _id: OrderId;
  private _items: OrderItem[];  // Entity interna — não exposta diretamente
  private _status: OrderStatus;
  private _total: Money;
  private _domainEvents: DomainEvent[] = [];

  private constructor(id: OrderId, customerId: CustomerId) {
    this._id = id;
    this._customerId = customerId;
    this._items = [];
    this._status = OrderStatus.DRAFT;
    this._total = Money.of(0, "BRL");
  }

  static create(customerId: CustomerId): Order {
    const order = new Order(OrderId.generate(), customerId);
    order.addDomainEvent(new OrderCreatedEvent(order._id, customerId));
    return order;
  }

  addItem(productId: ProductId, quantity: number, unitPrice: Money): void {
    if (this._status !== OrderStatus.DRAFT) {
      throw new OrderNotEditableError(this._id.value);
    }
    if (quantity <= 0) throw new InvalidQuantityError(quantity);

    // Invariante: não permite item duplicado
    const existing = this._items.find(i => i.productId.equals(productId));
    if (existing) {
      existing.increaseQuantity(quantity);
    } else {
      this._items.push(OrderItem.create(productId, quantity, unitPrice));
    }

    this.recalculateTotal();
  }

  place(): void {
    if (this._items.length === 0) throw new EmptyOrderError();
    if (this._status !== OrderStatus.DRAFT) throw new OrderAlreadyPlacedError();

    this._status = OrderStatus.PLACED;
    this.addDomainEvent(new OrderPlacedEvent(this._id, this._customerId, this._total));
  }

  private recalculateTotal(): void {
    this._total = this._items.reduce(
      (acc, item) => acc.add(item.subtotal()),
      Money.of(0, "BRL")
    );
  }

  pullDomainEvents(): DomainEvent[] {
    const events = [...this._domainEvents];
    this._domainEvents = [];
    return events;
  }

  private addDomainEvent(event: DomainEvent): void {
    this._domainEvents.push(event);
  }

  get id(): OrderId { return this._id; }
  get total(): Money { return this._total; }
  get status(): OrderStatus { return this._status; }
  // ❌ NÃO expor: get items() — use casos específicos
}
```

### Repository

Abstrai a persistência de um Aggregate. Uma interface por Aggregate:

```typescript
// Interface definida no domínio
type OrderRepository = {
  findById(id: OrderId): Promise<Order | null>;
  findByCustomerId(customerId: CustomerId): Promise<Order[]>;
  save(order: Order): Promise<void>;
};

// Implementação na infra
class PrismaOrderRepository implements OrderRepository {
  async findById(id: OrderId): Promise<Order | null> {
    const raw = await prisma.order.findUnique({
      where: { id: id.value },
      include: { items: true }
    });
    return raw ? OrderMapper.toDomain(raw) : null;
  }

  async save(order: Order): Promise<void> {
    const data = OrderMapper.toPersistence(order);
    await prisma.order.upsert({
      where: { id: data.id },
      update: data,
      create: data
    });
  }
}
```

### Domain Service

Lógica de negócio que não pertence naturalmente a nenhuma Entity:

```typescript
// ❌ Errado — lógica de pricing não pertence a nenhuma entity específica
class Order {
  calculateDiscountedTotal(coupon: Coupon, loyalty: LoyaltyAccount): Money { ... }
}

// ✅ Domain Service — coordena entre múltiplos aggregates
class PricingService {
  calculateFinalPrice(order: Order, coupon: Coupon | null, loyalty: LoyaltyAccount): Money {
    let total = order.total;

    if (coupon?.isValidFor(order)) {
      total = coupon.applyDiscount(total);
    }

    if (loyalty.hasPointsForDiscount()) {
      total = loyalty.applyPointsDiscount(total);
    }

    return total;
  }
}
```

### Specification Pattern

Encapsula uma regra de negócio como objeto combinável:

```typescript
type Specification<T> = {
  isSatisfiedBy(candidate: T): boolean;
  and(other: Specification<T>): Specification<T>;
  or(other: Specification<T>): Specification<T>;
  not(): Specification<T>;
};

class ActiveUserSpec implements Specification<User> {
  isSatisfiedBy(user: User): boolean { return user.status === UserStatus.ACTIVE; }

  and(other: Specification<User>): Specification<User> {
    return { isSatisfiedBy: u => this.isSatisfiedBy(u) && other.isSatisfiedBy(u), ... };
  }
  // ...
}

class PremiumUserSpec implements Specification<User> {
  isSatisfiedBy(user: User): boolean { return user.plan === Plan.PREMIUM; }
}

// Compondo especificações
const eligibleForDiscount = new ActiveUserSpec().and(new PremiumUserSpec());
const usersWithDiscount = users.filter(u => eligibleForDiscount.isSatisfiedBy(u));
```

## Anemic Domain Model — O Anti-Pattern

```typescript
// ❌ Anemic — entidade é só DTO, regras estão em "services" arbitrários
class OrderAnemic {
  id: string;
  items: OrderItemAnemic[];
  status: string;
  total: number;
  // sem métodos de negócio
}

// Regra de negócio vazando para serviço de aplicação
class OrderService {
  async placeOrder(orderId: string) {
    const order = await this.orderRepository.findById(orderId);
    if (order.items.length === 0) throw new Error("No items");  // regra fora da entidade
    if (order.status !== "draft") throw new Error("Already placed");
    order.status = "placed";  // mutação direta
    order.total = order.items.reduce((acc, i) => acc + i.price * i.qty, 0);
    await this.orderRepository.save(order);
  }
}
```

O problema: regras duplicadas, sem invariantes garantidas pelo tipo, impossível testar em isolamento.

## Conceitos Relacionados

[[ddd-strategic]] · [[clean-architecture]] · [[hexagonal-architecture]] · [[cqrs]] · [[event-sourcing]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-13*
