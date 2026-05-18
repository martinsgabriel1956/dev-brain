---
date: 2026-05-17
tags: [tech-mentor, system-design, arquitetura, lld]
skill: tech-mentor-system-design/references/hld-lld-c4
level: intermediário
---

# Low Level Design (LLD)

## Contexto
LLD é o zoom dentro de um componente definido no HLD. Responde à pergunta **"como esse bloco é implementado?"** — e é o artefato que o time usa como referência direta antes e durante a implementação.

É onde decisões de HLD se tornam contratos concretos: schemas de banco, assinaturas de API, estrutura de classes, algoritmos críticos e tratamento de erro.

## Como Funciona

LLD opera no nível de **módulos, classes, endpoints e esquemas**. O objetivo é remover ambiguidade antes de codificar.

O que um LLD deve cobrir:
- Estrutura interna do componente (camadas, módulos, responsabilidades)
- Contratos de API (endpoints, request/response, status codes, erros)
- Schema do banco (tabelas, colunas, índices, constraints, FK)
- Fluxo de dados interno (sequência de chamadas entre classes/funções)
- Casos de borda e tratamento de erro
- Estratégias de retry, idempotência e consistência

### Exemplo — LLD do Order Service

**Schema do banco:**
```sql
CREATE TABLE orders (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id     UUID NOT NULL REFERENCES users(id),
  status      order_status NOT NULL DEFAULT 'pending',
  total       NUMERIC(10,2) NOT NULL,
  created_at  TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at  TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_status  ON orders(status);
```

**Contrato de API:**
```
POST /orders
Body: { userId: string, items: [{ productId: string, quantity: number }] }
Response 201: { id, status, total, createdAt }
Response 400: { error: "Item fora de estoque: {productId}" }
Response 422: { error: "Usuário sem endereço cadastrado" }
```

**Estrutura interna (Clean Architecture):**
```typescript
// Controller — recebe DTO, chama UseCase
type CreateOrderDTO = {
  userId: string;
  items: OrderItemDTO[];
};

// UseCase — regra de negócio
class CreateOrderUseCase {
  constructor(
    private orderRepository: OrderRepository,
    private stockService: StockService,    // infra
    private eventPublisher: EventPublisher  // infra
  ) {}

  async execute(dto: CreateOrderDTO): Promise<Order> {
    await this.stockService.validateStock(dto.items);

    const order = Order.create(dto);  // entidade valida invariantes

    await this.orderRepository.save(order);
    await this.eventPublisher.publish("order.created", order.toEvent());

    return order;
  }
}

// Entity — invariantes de negócio
class Order {
  static create(dto: CreateOrderDTO): Order {
    if (dto.items.length === 0) throw new EmptyOrderError();
    // calcula total, aplica regras de desconto, etc.
  }
}
```

**Diagrama de sequência (fluxo interno):**
```
Controller → CreateOrderUseCase
                → StockService.validateStock()
                → Order.create()           // domínio
                → OrderRepository.save()   // persiste
                → EventPublisher.publish() // notifica
             ← retorna Order
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Detalhe alto | Remove ambiguidade para o time | Custo de manutenção — diverge do código com o tempo |
| Contratos explícitos | Permite desenvolvimento paralelo entre times | Overhead de definição antes de ter clareza total |
| Schema de banco no LLD | Detecta problemas de modelagem cedo | Mudanças de requisito invalidam o artefato |
| Diagramas de sequência | Torna fluxos complexos navegáveis | Ficam obsoletos rapidamente se o código muda |

## Quando Usar / Quando Evitar

**Usar quando:**
- Implementando um serviço ou módulo novo de porte médio+
- Há dependência entre times (frontend precisa saber o contrato da API antes)
- A lógica de negócio é complexa e precisa ser revisada antes de codificar
- Design review formal antes de merge

**Evitar (ou simplificar) quando:**
- CRUD simples sem regra de negócio — o código é mais claro que o diagrama
- Time pequeno com contexto compartilhado e iteração rápida
- Protótipo — o LLD vira dívida se o design mudar

## Conceitos Relacionados
[[high-level-design]] · [[c4-model]] · [[clean-architecture]] · [[domain-driven-design]] · [[api-design]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-05-17*
