---
date: 2026-04-13
tags: [tech-mentor, arquitetura, clean-architecture, presenter, interface-adapters]
skill: tech-mentor-system-design/references/architecture-patterns
level: intermediário
---
# Presenters

## Contexto

Presenters vivem na camada de **Interface Adapters** da Clean Architecture. Responsabilidade única: **converter o output do Use Case para o formato esperado pelo cliente** (HTTP response, GraphQL payload, CLI output, etc.).

O domínio não sabe nada sobre JSON, snake_case, ISO 8601 ou códigos HTTP — o Presenter faz essa tradução.
## Como Funciona

### Fluxo Completo

```
Request → Controller → UseCase → OutputPort → Presenter → Response
                          ↑
                     domínio puro
                     (sem formato externo)
```

O Use Case escreve no `OutputPort` (uma interface). O Presenter implementa esse port e formata o dado para o cliente.
### Implementação

```typescript
// Output do UseCase — tipos de domínio
type PlaceOrderOutput = {
  orderId: OrderId;
  total: Money;
  status: OrderStatus;
  placedAt: Date;
};

// OutputPort — interface definida no Application layer
type PlaceOrderOutputPort = {
  present(output: PlaceOrderOutput): void;
};

// UseCase escreve no port, não sabe quem vai formatar
class PlaceOrderUseCase {
  constructor(
    private orderRepository: OrderRepository,
    private outputPort: PlaceOrderOutputPort
  ) {}

  async execute(input: PlaceOrderInput): Promise<void> {
    const order = Order.create(input);
    await this.orderRepository.save(order);
    this.outputPort.present({ orderId: order.id, total: order.total, status: order.status, placedAt: new Date() });
  }
}

// Presenter HTTP — converte domínio → JSON da API
class PlaceOrderHttpPresenter implements PlaceOrderOutputPort {
  private result: PlaceOrderHttpResponse | null = null;

  present(output: PlaceOrderOutput): void {
    this.result = {
      order_id: output.orderId.value,
      total: { amount: output.total.amount, currency: output.total.currency },
      status: output.status.toLowerCase(),
      placed_at: output.placedAt.toISOString()
    };
  }

  getResponse(): PlaceOrderHttpResponse {
    if (!this.result) throw new Error("present() not called");
    return this.result;
  }
}

// Controller — orquestra tudo
class OrderController {
  async placeOrder(req: Request, res: Response): Promise<void> {
    const presenter = new PlaceOrderHttpPresenter();
    const useCase = new PlaceOrderUseCase(this.orderRepository, presenter);

    await useCase.execute({ customerId: req.body.customer_id, items: req.body.items });

    res.status(201).json(presenter.getResponse());
  }
}
```

### Mesmo UseCase, Presenters Diferentes

O valor do padrão aparece quando o mesmo Use Case serve múltiplos clientes:

```typescript
// Presenter para GraphQL
class PlaceOrderGraphQLPresenter implements PlaceOrderOutputPort {
  present(output: PlaceOrderOutput): void {
    this.result = {
      orderId: output.orderId.value,
      totalAmount: output.total.amount,
      currency: output.total.currency,
      status: output.status,
      placedAt: output.placedAt
    };
  }
}

// Presenter para CLI
class PlaceOrderCliPresenter implements PlaceOrderOutputPort {
  present(output: PlaceOrderOutput): void {
    console.log(`Order ${output.orderId.value} placed — ${output.total.currency} ${output.total.amount}`);
  }
}

// Presenter para testes — captura o output para assertions
class PlaceOrderTestPresenter implements PlaceOrderOutputPort {
  public output: PlaceOrderOutput | null = null;

  present(output: PlaceOrderOutput): void {
    this.output = output;
  }
}

// No teste — sem HTTP, sem JSON, sem Controller
it("should place order and emit output", async () => {
  const presenter = new PlaceOrderTestPresenter();
  const useCase = new PlaceOrderUseCase(new InMemoryOrderRepository(), presenter);

  await useCase.execute({ customerId: "uuid-123", items: [{ productId: "p1", quantity: 2 }] });

  expect(presenter.output?.status).toBe(OrderStatus.PLACED);
  expect(presenter.output?.total.amount).toBeGreaterThan(0);
});
```

## Quando Vale a Pena

**Separar Presenter do Controller faz sentido quando:**
- O mesmo Use Case serve REST + GraphQL + WebSocket
- A transformação é complexa (localização, formatação por locale, campos condicionais)
- Você quer testar a serialização em isolamento

**Inline no Controller é pragmático e suficiente quando:**
- Um único tipo de cliente (só REST)
- Transformação trivial (poucos campos, tipos primitivos)
- Time pequeno, prazo curto

```typescript
// Versão pragmática — Presenter inline no Controller
class OrderController {
  async placeOrder(req: Request, res: Response): Promise<void> {
    const output = await this.placeOrderUseCase.execute(req.body);

    // "Presenter" inline — aceitável para casos simples
    res.status(201).json({
      order_id: output.orderId.value,
      total: output.total.amount,
      placed_at: output.placedAt.toISOString()
    });
  }
}
```

## Trade-offs

| Aspecto | Presenter separado | Inline no Controller |
|---|---|---|
| Testabilidade | UseCase testável sem HTTP | Requer mock do response |
| Reutilização | Mesmo UseCase → múltiplos formatos | Acoplado a um formato |
| Verbosidade | Mais arquivos e boilerplate | Conciso |
| Quando faz sentido | Múltiplos clientes, lógica complexa | CRUD simples, um cliente |

## Conceitos Relacionados

[[clean-architecture]] · [[hexagonal-architecture]] · [[ddd-tactical]] · [[solid]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-13*
