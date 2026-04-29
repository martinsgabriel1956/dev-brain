---
date: 2026-04-13
tags: [tech-mentor, arquitetura, eda, event-driven, async]
skill: tech-mentor-backend/references/messaging
level: intermediário
---
# Event-Driven Architecture (EDA)

## Contexto

Event-Driven Architecture é um estilo onde **componentes se comunicam publicando e consumindo eventos**, sem acoplamento direto entre produtor e consumidor. O broker de mensagens (Kafka, RabbitMQ, SNS/SQS) é o intermediário.

O princípio central: **temporal decoupling** — produtor não sabe quem vai consumir o evento, nem quando, nem quantos consumidores existem. Isso habilita escala, resiliência e evolução independente dos serviços.

É o backbone arquitetural de sistemas que precisam de: alta escala, processamento assíncrono, auditoria, integração entre domínios sem acoplamento forte.
## Como Funciona

### Anatomia de um Evento

Eventos devem ser **imutáveis, auto-contidos e significativos para o negócio**:

```typescript
// Evento de domínio — o que aconteceu no negócio
type OrderPlacedEvent = {
  // Metadata
  eventId: string;           // UUID v4 — para deduplicação
  eventType: "order.placed"; // tipo explícito
  occurredAt: string;        // ISO 8601 — quando aconteceu
  version: number;           // schema version para evolução

  // Payload
  orderId: string;
  customerId: string;
  items: { productId: string; quantity: number; unitPrice: number }[];
  total: number;
  currency: string;
};
```

### Padrões de Comunicação

**Simple Event Notification** — evento mínimo, consumidor busca detalhes se precisar:

```typescript
// Produtor publica só o essencial
const event = {
  eventType: "user.registered",
  userId: "uuid-123",
  occurredAt: new Date().toISOString()
};
```

**Event-Carried State Transfer** — evento carrega o estado completo para evitar queries:

```typescript
// Produtor embute os dados necessários
const event = {
  eventType: "order.placed",
  orderId: "uuid-456",
  customer: { id: "uuid-789", email: "alice@example.com", name: "Alice" },
  items: [...],
  total: 150.00,
  occurredAt: new Date().toISOString()
};
```

**Event Sourcing** — todos os eventos são fonte de verdade (ver nota dedicada).
### Topologias

**Choreography** — cada serviço reage a eventos sem coordenador central:

```
OrderService → [order.placed] → PaymentService → [payment.processed] → NotificationService
```

**Orchestration** — coordenador central (saga orchestrator) emite comandos:

```
SagaOrchestrator → [payment.charge.command] → PaymentService
SagaOrchestrator ← [payment.charged.event]  ← PaymentService
SagaOrchestrator → [inventory.reserve.command] → InventoryService
```

### Implementação com Kafka (TypeScript)

```typescript
import { Kafka, Producer, Consumer } from "kafkajs";

const kafka = new Kafka({ clientId: "order-service", brokers: ["kafka:9092"] });

// Produtor
class EventPublisher {
  private producer: Producer;

  constructor() {
    this.producer = kafka.producer();
  }

  async publish<T>(topic: string, event: T): Promise<void> {
    await this.producer.send({
      topic,
      messages: [{ value: JSON.stringify(event) }]
    });
  }
}

// Consumidor
class OrderEventConsumer {
  private consumer: Consumer;

  constructor() {
    this.consumer = kafka.consumer({ groupId: "notification-service" });
  }

  async start(): Promise<void> {
    await this.consumer.subscribe({ topic: "order.placed", fromBeginning: false });

    await this.consumer.run({
      eachMessage: async ({ message }) => {
        const event = JSON.parse(message.value!.toString()) as OrderPlacedEvent;
        await this.handleOrderPlaced(event);
      }
    });
  }

  private async handleOrderPlaced(event: OrderPlacedEvent): Promise<void> {
    await emailService.sendOrderConfirmation(event.customerId, event.orderId);
  }
}
```

### Idempotência no Consumidor

Eventos podem ser entregues mais de uma vez (at-least-once delivery). O consumidor deve ser idempotente:

```typescript
class IdempotentOrderConsumer {
  async handleOrderPlaced(event: OrderPlacedEvent): Promise<void> {
    // Verificar se já processamos este evento
    const alreadyProcessed = await this.processedEvents.exists(event.eventId);
    if (alreadyProcessed) return;

    // Processar e marcar como processado atomicamente
    await prisma.$transaction(async tx => {
      await tx.processedEvent.create({ data: { id: event.eventId, processedAt: new Date() } });
      await tx.notification.create({ data: { orderId: event.orderId, type: "order_confirmation" } });
    });
  }
}
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Acoplamento | Produtor e consumidor independentes | Fluxo de dados mais difícil de rastrear |
| Escala | Consumidores escalam independentemente | Eventual consistency por default |
| Resiliência | Falha de um consumidor não afeta o produtor | Debugging e observabilidade mais complexos |
| Evolução | Novos consumidores sem tocar produtor | Schema evolution exige governança (Schema Registry) |
| Auditoria | Log natural de todos os eventos | Overhead de infraestrutura (broker) |

## Quando Usar / Quando Evitar

**Usar quando:**
- Integração entre domínios/serviços com autonomia de deploy
- Processamento assíncrono (notificações, relatórios, etc.)
- Auditoria de estado ao longo do tempo é necessária
- Fan-out: múltiplos consumidores para o mesmo evento

**Evitar quando:**
- Fluxo precisa de resposta síncrona imediata (request/response é melhor)
- Sistema pequeno onde a complexidade do broker não compensa
- Equipe sem experiência com garantias de entrega e idempotência

## Vocabulário 

###  Backbone arquitetural

 Expressão informal para a infraestrutura de comunicação central que conecta todos os componentes do sistema — o "esqueleto" pelo qual dados e eventos trafegam.

Em sistemas event-driven, o broker (Kafka, RabbitMQ, SQS) é esse backbone: não existe um orquestrador central, o broker é o ponto de integração de tudo. Cada serviço publica e consome eventos por ele de forma independente.

A metáfora vale para outros contextos: em microsserviços com service mesh, o Envoy/Istio é o backbone de rede; em sistemas de dados, o pipeline (Flink, Spark) é o backbone de processamento.

---
### Temporal decoupling

Produtor e consumidor **não precisam estar disponíveis ao mesmo tempo** para que a comunicação aconteça.

No modelo síncrono (REST), há acoplamento temporal — se o PaymentService estiver down, o OrderService falha. No modelo assíncrono, o broker atua como buffer:

```
OrderService → publica [order.placed] → Kafka
                                            ↓
                              PaymentService consome quando voltar
```

O OrderService não sabe — e não precisa saber — se o PaymentService está up, lento ou em manutenção. O evento fica no broker até ser consumido.

Consequências diretas:
- **Resiliência**: falha de um consumidor não quebra o produtor
- **Escala independente**: consumidor processa no seu ritmo
- **Eventual consistency**: o estado converge, mas não instantaneamente

O trade-off: você ganha desacoplamento mas perde a garantia de que o efeito aconteceu agora. Se o fluxo precisa de resposta imediata ("o pagamento foi aprovado?"), temporal decoupling é o problema, não a solução — use request/response síncrono.

---
### Broker

Intermediário de mensagens — serviço que recebe mensagens de produtores, persiste e entrega para consumidores. O produtor não precisa esperar o consumidor estar disponível.

| Broker | Modelo | Forte em |
|---|---|---|
| Kafka | Log distribuído, pull | Alto throughput, replay, audit log |
| RabbitMQ | Fila tradicional, push | Roteamento complexo, baixa latência |
| SQS/SNS | Managed AWS, pull/push | Simplicidade operacional, serverless |
| NATS | Pub/Sub leve, push | Latência ultra-baixa, IoT, edge |

A escolha do broker define as garantias de entrega, a capacidade de replay e o custo operacional de toda a camada de eventos do sistema.

## Conceitos Relacionados

[[mensageria]] · [[kafka]] · [[outbox-pattern]] · [[saga]] · [[event-sourcing]] · [[cqrs]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-13*
