---
date: 2026-04-13
tags: [tech-mentor, backend, ddd, strategic-design, bounded-context]
skill: tech-mentor-backend/references/ddd
level: avançado
---
# DDD — Strategic Design

## Contexto

Strategic Design é a parte do DDD que responde: **"como dividir um sistema complexo em partes que possam evoluir de forma independente?"**

O resultado prático: Bounded Contexts bem definidos mapeiam para times autônomos, repositórios independentes e serviços que não se acoplam de formas inesperadas.

Sem Strategic Design, você tem microsserviços que são na verdade um "Distributed Monolith" — código separado mas fortemente acoplado via compartilhamento de banco ou chamadas síncronas em cascata.

## Conceitos Fundamentais

### Ubiquitous Language

Cada domínio tem seu próprio vocabulário. A **Linguagem Ubíqua** é o conjunto de termos compartilhado entre devs e domain experts dentro de um Bounded Context.

O mesmo conceito pode ter nomes diferentes em contextos diferentes — e isso é correto:

```
Contexto de Vendas:  "Cliente", "Pedido", "Produto"
Contexto Fiscal:     "Contribuinte", "Nota Fiscal", "Item Tributável"
Contexto de Entrega: "Destinatário", "Remessa", "SKU"
```

### Bounded Context

Um Bounded Context é um **limite explícito dentro do qual um modelo de domínio específico se aplica**. É o coração do Strategic Design.

```
┌─────────────────────┐    ┌─────────────────────┐    ┌─────────────────────┐
│   Sales Context      │    │   Inventory Context  │    │   Shipping Context  │
│                     │    │                     │    │                     │
│  Customer           │    │  Product            │    │  Package            │
│  Order              │    │  Stock              │    │  Shipment           │
│  OrderItem          │    │  Warehouse          │    │  TrackingEvent      │
│                     │    │                     │    │                     │
│  "Order" = contrato │    │ "Order" = reserva   │    │ "Order" = remessa   │
│  de compra          │    │ de estoque          │    │ a entregar          │
└─────────────────────┘    └─────────────────────┘    └─────────────────────┘
         │                           │                           │
         └──── Integration Events ───┴──── Integration Events ───┘
```

### Context Map

Documenta as relações entre Bounded Contexts. Tipos de relacionamento:

**Shared Kernel** — dois contextos compartilham um subconjunto do modelo:

```
Risco: mudanças no kernel afetam ambos os times
Quando usar: contextos muito próximos com time unificado
```

**Customer/Supplier** — upstream (fornecedor) e downstream (cliente) com negociação:

```
Shipping ← (upstream) Sales
Sales define o que Shipping precisa, Shipping adapta
```

**Conformist** — downstream se conforma com o modelo do upstream sem negociação:

```
Quando integrar com sistema legado ou externo sem poder negociar
Ex: integração com ERP corporativo
```

**Anti-Corruption Layer (ACL)** — tradução entre modelos para proteger o domínio:

```typescript
// ACL — converte modelo do Stripe para modelo do domínio
class StripePaymentACL {
  toDomainPayment(stripeCharge: Stripe.Charge): Payment {
    return {
      id: stripeCharge.id,
      amount: stripeCharge.amount / 100,  // Stripe usa centavos
      currency: stripeCharge.currency.toUpperCase(),
      status: this.mapStatus(stripeCharge.status),
      processedAt: new Date(stripeCharge.created * 1000)
    };
  }

  private mapStatus(stripeStatus: string): PaymentStatus {
    const map: Record<string, PaymentStatus> = {
      "succeeded": PaymentStatus.APPROVED,
      "pending": PaymentStatus.PENDING,
      "failed": PaymentStatus.REJECTED
    };
    return map[stripeStatus] ?? PaymentStatus.UNKNOWN;
  }
}
```

**Open Host Service** — contexto oferece API estável para múltiplos consumidores:
```
Catalog Service oferece API REST para: Sales, Marketing, Mobile, Partners
```

**Published Language** — protocolo canônico entre contextos (Avro, Protobuf, OpenAPI):
```
Sales publica OrderPlacedEvent via Kafka com schema Avro versionado
Todos os consumidores usam o mesmo schema
```

### Integração via Eventos de Domínio vs Integração

```typescript
// Domain Event — interno ao Bounded Context
// Só existe dentro de Sales Context
type OrderPlaced = {
  orderId: OrderId;
  customerId: CustomerId;
  items: OrderItem[];
  total: Money;
  placedAt: Date;
};

// Integration Event — cruza a fronteira do Bounded Context
// Publicado para outros contextos via broker
type OrderPlacedIntegrationEvent = {
  eventId: string;
  eventType: "sales.order.placed";
  version: 1;
  occurredAt: string;         // ISO 8601
  orderId: string;            // tipos primitivos — sem tipos de domínio
  customerId: string;
  totalAmount: number;
  currency: string;
  items: { sku: string; quantity: number; unitPrice: number }[];
};
```

A distinção é crucial: **Domain Events são ricos e tipados; Integration Events são primitivos e versionados**.

## Event Storming

Técnica colaborativa para descoberta de domínio. Participantes: devs + domain experts.

**Big Picture Event Storming:**
```
1. Escreva todos os Domain Events em laranja (post-its)
   ex: "OrderPlaced", "PaymentProcessed", "ShipmentDispatched"

2. Identifique os Commands que causam esses eventos (azul)
   ex: "PlaceOrder" → "OrderPlaced"

3. Identifique os Aggregates (amarelo)
   ex: "Order" agrega Order + OrderItems + Status

4. Agrupe por Bounded Context (linhas no quadro)
   ex: Sales | Inventory | Shipping | Billing

5. Identifique Policies (lilás) — "quando X acontece, faça Y"
   ex: "Quando OrderPlaced, reserve estoque"
```

Resultado: Context Map e estrutura inicial de eventos de integração.

## DDD com Microsserviços

A regra geral: **um Bounded Context = um microsserviço potencial**. Mas não necessariamente desde o início.

```
Fase 1: Monolito Modular com bounded modules
Fase 2: Extrair contextos com escala/autonomia diferentes
Fase 3: Microsserviços com comunicação via Integration Events

Bounded Context != Microsserviço necessariamente
Um microsserviço pode implementar múltiplos contextos pequenos
Um contexto grande pode ser múltiplos serviços
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Autonomia de times | Times trabalham em contextos independentes | Necessita governança de eventos de integração |
| Modelos locais | Cada contexto otimiza seu modelo | Duplicação intencional de dados entre contextos |
| Boundaries explícitos | Reduz acoplamento acidental | Overhead de mapeamento entre modelos |
| Linguagem ubíqua | Comunicação precisa entre dev e negócio | Requer investimento em workshops com domain experts |

## Conceitos Relacionados

[[ddd-tactical]] · [[monolito-modular]] · [[event-driven-architecture]] · [[bounded-context]] · [[microsservicos]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-13*
