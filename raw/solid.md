---
date: 2026-04-13
tags: [tech-mentor, arquitetura, principios, solid, oop]
skill: tech-mentor-backend/references/design-principles
level: fundamento
---

# SOLID

## Contexto

SOLID é um acrônimo para cinco princípios de design orientado a objetos propostos por Robert Martin. São **heurísticas, não leis** — violações são às vezes a escolha certa, mas exigem justificativa.

O valor prático: código que segue SOLID tende a ser mais fácil de testar (S, D), mais fácil de estender sem quebrar (O, L), e mais fácil de compor (I, D).

## Os 5 Princípios

### S — Single Responsibility Principle

**"Uma classe deve ter um único motivo para mudar."**

Motivo para mudar = ator que manda mudar. Se o RH manda mudar as regras de salário e o Financeiro manda mudar as regras de relatório, esses são dois atores — dois motivos — logo, duas classes.

```typescript
// ❌ Viola SRP — Report mudaria por razões de negócio E de formato
class UserReport {
  generateSalaryReport(user: User): string { ... }  // regra de negócio
  formatAsPDF(content: string): Buffer { ... }       // infraestrutura
  sendByEmail(pdf: Buffer, to: string): void { ... } // entrega
}

// ✅ Cada classe tem uma responsabilidade
class SalaryCalculator {
  calculate(user: User): number { ... }  // regra de negócio
}

class ReportFormatter {
  formatAsPDF(content: string): Buffer { ... }  // formatação
}

class EmailSender {
  send(attachment: Buffer, to: string): Promise<void> { ... }  // entrega
}
```

### O — Open/Closed Principle

**"Aberto para extensão, fechado para modificação."**

Adicione comportamento novo sem alterar código existente. Em TypeScript, alcançado com interfaces e polimorfismo:

```typescript
// ❌ Viola OCP — nova forma de pagamento exige modificar PaymentProcessor
class PaymentProcessor {
  process(method: "credit_card" | "pix" | "boleto", amount: number): void {
    if (method === "credit_card") { /* ... */ }
    else if (method === "pix") { /* ... */ }
    // adicionar boleto = modificar esta classe
  }
}

// ✅ Respeita OCP — nova forma de pagamento = nova classe, sem modificar existentes
type PaymentStrategy = {
  process(amount: number): Promise<void>;
};

class CreditCardPayment implements PaymentStrategy {
  async process(amount: number): Promise<void> { /* ... */ }
}

class PixPayment implements PaymentStrategy {
  async process(amount: number): Promise<void> { /* ... */ }
}

// BoletoPayment é adicionado sem tocar nas classes acima
class BoletoPayment implements PaymentStrategy {
  async process(amount: number): Promise<void> { /* ... */ }
}

class PaymentProcessor {
  constructor(private strategy: PaymentStrategy) {}

  async process(amount: number): Promise<void> {
    await this.strategy.process(amount);
  }
}
```

### L — Liskov Substitution Principle

**"Subtipos devem ser substituíveis por seus tipos base."**

Se `B` extends `A`, qualquer código que funciona com `A` deve funcionar com `B` sem comportamento inesperado. Violação típica: subclasse lança exceção onde a base não, ou ignora parâmetros, ou tem precondições mais fortes.

```typescript
// ❌ Viola LSP — ReadOnlyList não pode substituir List
class List<T> {
  add(item: T): void { this.items.push(item); }
  remove(item: T): void { /* ... */ }
}

class ReadOnlyList<T> extends List<T> {
  add(item: T): void {
    throw new Error("Cannot add to read-only list"); // quebra o contrato
  }
}

// ✅ Respeita LSP — separar as interfaces
type ReadableList<T> = {
  get(index: number): T;
  size(): number;
};

type MutableList<T> = ReadableList<T> & {
  add(item: T): void;
  remove(item: T): void;
};
```

### I — Interface Segregation Principle

**"Clientes não devem ser forçados a depender de interfaces que não usam."**

Interfaces gordas criam acoplamento desnecessário. Prefira interfaces pequenas e específicas:

```typescript
// ❌ Interface gorda — EmailService é forçado a implementar métodos que não usa
type NotificationService = {
  sendEmail(to: string, content: string): Promise<void>;
  sendSMS(to: string, content: string): Promise<void>;
  sendPush(deviceId: string, content: string): Promise<void>;
};

class EmailService implements NotificationService {
  async sendEmail(to: string, content: string): Promise<void> { /* ... */ }
  async sendSMS(): Promise<void> { throw new Error("Not implemented"); }  // não faz sentido
  async sendPush(): Promise<void> { throw new Error("Not implemented"); }
}

// ✅ Interfaces segregadas
type EmailSender = {
  sendEmail(to: string, content: string): Promise<void>;
};

type SMSSender = {
  sendSMS(to: string, content: string): Promise<void>;
};

type PushSender = {
  sendPush(deviceId: string, content: string): Promise<void>;
};

// UseCase depende só do que usa
class OrderConfirmationUseCase {
  constructor(
    private emailSender: EmailSender  // não precisa de SMS nem Push
  ) {}
}
```

### D — Dependency Inversion Principle

**"Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações."**

Este é o mais impactante — é a base da testabilidade e da Hexagonal Architecture:

```typescript
// ❌ Viola DIP — UseCase de alto nível depende diretamente do Prisma (baixo nível)
class PlaceOrderUseCase {
  async execute(input: PlaceOrderInput): Promise<void> {
    const order = new Order(input);
    // acoplamento direto com Prisma
    await prisma.order.create({ data: { id: order.id, total: order.total } });
  }
}

// ✅ Respeita DIP — UseCase depende de abstração (interface), não de implementação
type OrderRepository = {
  save(order: Order): Promise<void>;
};

class PlaceOrderUseCase {
  constructor(
    private orderRepository: OrderRepository  // abstração
  ) {}

  async execute(input: PlaceOrderInput): Promise<void> {
    const order = new Order(input);
    await this.orderRepository.save(order);  // sem saber se é Prisma, Mongo, In-Memory...
  }
}

// Implementação concreta na camada de infra
class PrismaOrderRepository implements OrderRepository {
  async save(order: Order): Promise<void> {
    await prisma.order.create({ data: { id: order.id, total: order.total } });
  }
}

// Teste usa In-Memory — UseCase não sabe a diferença
class InMemoryOrderRepository implements OrderRepository {
  private store: Order[] = [];
  async save(order: Order): Promise<void> { this.store.push(order); }
}
```

## Relação entre os Princípios

```
SRP → define boundaries da classe
OCP → permite extensão via polimorfismo
LSP → garante que polimorfismo funciona corretamente
ISP → mantém interfaces coesas e pequenas
DIP → inverte dependências para abstrações testáveis
```

D é o mais poderoso — sem ele, testes unitários reais são impossíveis.

## Trade-offs

| Princípio | Benefício | Custo se mal aplicado |
|---|---|---|
| SRP | Código focado, fácil de testar | Over-engineering com classes triviais |
| OCP | Extensível sem regressão | Abstração prematura desnecessária |
| LSP | Polimorfismo correto | Hierarquias de herança profundas |
| ISP | Interfaces mínimas | Proliferação de interfaces pequenas demais |
| DIP | Testabilidade e flexibilidade | Verbosidade de injeção de dependência |

## Conceitos Relacionados

[[clean-architecture]] · [[hexagonal-architecture]] · [[design-patterns-gof]] · [[dependency-injection]]
