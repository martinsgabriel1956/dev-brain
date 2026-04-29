---
date: 2026-04-18
tags: [tech-mentor, arquitetura, principios, solid, testabilidade, di]
skill: tech-mentor-system-design/references/architecture-principles
level: fundamento
---

# Dependency Injection

## Contexto
Dependency Injection (DI) é a prática de **fornecer as dependências de um objeto de fora**, em vez de o objeto criá-las internamente. É a implementação prática do **Dependency Inversion Principle** (o "D" do SOLID): módulos de alto nível não dependem de módulos de baixo nível — ambos dependem de abstrações.

O resultado direto: código **testável, substituível e desacoplado**. Trocar um repositório real por um in-memory em testes exige zero mudança na lógica de negócio.

## O Problema Sem DI

```typescript
// Acoplamento direto — impossível de testar sem o banco real
class OrderService {
  private repo: OrderRepository;

  constructor() {
    // OrderService decide qual implementação usar — viola DIP
    this.repo = new PostgresOrderRepository({
      host: process.env.DB_HOST,
      port: 5432
    });
  }

  async placeOrder(data: CreateOrderDTO) {
    return this.repo.save(Order.create(data));
  }
}

// Para testar: precisa de banco PostgreSQL real
// Para trocar por DynamoDB: editar OrderService
// Para usar mock: impossível sem alterar a classe
```

## DI Manual — Constructor Injection

```typescript
// 1. Definir a abstração (interface/type)
type OrderRepository = {
  save: (order: Order) => Promise<Order>;
  findById: (id: string) => Promise<Order | null>;
  findByCustomer: (customerId: string) => Promise<Order[]>;
};

// 2. OrderService depende da abstração, não da implementação
class OrderService {
  constructor(
    private orderRepo: OrderRepository,
    private eventBus: EventBus,
    private logger: Logger
  ) {}

  async placeOrder(data: CreateOrderDTO): Promise<Order> {
    const order = Order.create(data);
    const saved = await this.orderRepo.save(order);
    await this.eventBus.publish(new OrderPlacedEvent(saved));
    this.logger.info({ message: "Order placed", orderId: saved.id });
    return saved;
  }
}

// 3. Implementações concretas
class PostgresOrderRepository implements OrderRepository {
  async save(order: Order) { /* ... prisma ... */ }
  async findById(id: string) { /* ... prisma ... */ }
  async findByCustomer(customerId: string) { /* ... prisma ... */ }
}

class InMemoryOrderRepository implements OrderRepository {
  private store = new Map<string, Order>();

  async save(order: Order) {
    this.store.set(order.id, order);
    return order;
  }
  async findById(id: string) { return this.store.get(id) ?? null; }
  async findByCustomer(customerId: string) {
    return [...this.store.values()].filter(o => o.customerId === customerId);
  }
}

// 4. Composição — wiring feito na borda da aplicação (main/bootstrap)
const orderService = new OrderService(
  new PostgresOrderRepository(prisma),
  new KafkaEventBus(kafka),
  new StructuredLogger()
);

// 5. Em testes — troca sem tocar em OrderService
const orderService = new OrderService(
  new InMemoryOrderRepository(),
  new FakeEventBus(),
  new NoopLogger()
);
```

## Tipos de Injeção

| Tipo | Implementação | Quando usar |
|---|---|---|
| **Constructor** | Dependências no `constructor()` | Padrão — dependências obrigatórias |
| **Property/Setter** | Atribuição direta ou setter | Dependências opcionais (raramente) |
| **Method** | Passadas por parâmetro no método | Dependências específicas por operação |

**Constructor injection é o padrão preferido** — deixa as dependências explícitas e obrigatórias, impossibilitando criar o objeto em estado inválido.

## DI Container — Quando Faz Sentido

Em aplicações grandes com muitas dependências, o wiring manual fica verboso. Containers automatizam a resolução.

```typescript
// tsyringe — container leve para TypeScript
import { container, injectable, inject } from "tsyringe";

@injectable()
class OrderService {
  constructor(
    @inject("OrderRepository") private orderRepo: OrderRepository,
    @inject("EventBus") private eventBus: EventBus
  ) {}
}

// Registrar implementações uma vez
container.register("OrderRepository", { useClass: PostgresOrderRepository });
container.register("EventBus", { useClass: KafkaEventBus });

// Resolver — container injeta automaticamente
const service = container.resolve(OrderService);
```

```typescript
// NestJS — DI integrado ao framework
@Injectable()
export class OrderService {
  constructor(
    private readonly orderRepo: OrderRepository,  // NestJS injeta por tipo
    private readonly eventBus: EventBus
  ) {}
}

@Module({
  providers: [
    OrderService,
    { provide: OrderRepository, useClass: PostgresOrderRepository },
    { provide: EventBus, useClass: KafkaEventBus }
  ]
})
export class OrderModule {}
```

## DI e Testabilidade

A consequência mais importante do DI é que **testes unitários não precisam de infra**:

```typescript
describe("OrderService", () => {
  let service: OrderService;
  let orderRepo: InMemoryOrderRepository;
  let eventBus: FakeEventBus;

  beforeEach(() => {
    orderRepo = new InMemoryOrderRepository();
    eventBus = new FakeEventBus();
    service = new OrderService(orderRepo, eventBus, new NoopLogger());
  });

  it("should save the order and publish an event", async () => {
    const order = await service.placeOrder({ customerId: "123", items: [] });

    const saved = await orderRepo.findById(order.id);
    expect(saved).not.toBeNull();

    expect(eventBus.published).toHaveLength(1);
    expect(eventBus.published[0]).toBeInstanceOf(OrderPlacedEvent);
  });
});
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Testabilidade | Testes unitários sem infra real | Wiring manual verboso em apps grandes |
| Flexibilidade | Trocar implementação sem tocar na lógica | Container pode obscurecer o grafo de dependências |
| Separação de concerns | Lógica separada de construção | Curva de aprendizado com containers como NestJS |
| Explicitidade | Constructor deixa dependências visíveis | Property injection pode criar objetos inconsistentes |

## Quando Usar / Quando Evitar

**Usar sempre para:**
- Qualquer dependência externa (banco, cache, fila, email, logger)
- Código que precisa ser testado isoladamente
- Implementações que podem variar (ex: repositório real vs. in-memory)

**Evitar DI container quando:**
- Projeto pequeno — wiring manual é mais claro
- A inversão de controle do container esconde dependências difíceis de rastrear

## Conceitos Relacionados
[[solid]] · [[hexagonal-architecture]] · [[clean-architecture]] · [[tdd]] · [[architecture-fitness-functions]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-18*
