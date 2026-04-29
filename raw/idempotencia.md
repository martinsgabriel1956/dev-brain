---
date: 2026-04-14
tags: [tech-mentor, backend, distributed-systems, idempotência, resiliência]
skill: tech-mentor-backend/references/distributed-systems
level: avançado
---

# Idempotência

## Contexto

Uma operação é **idempotente** quando executá-la múltiplas vezes produz o mesmo resultado que executá-la uma única vez. Em sistemas distribuídos, isso é fundamental porque **retries são inevitáveis** — timeouts, falhas de rede e crashes fazem com que o cliente não saiba se a operação chegou a ser executada ou não.

Sem idempotência: cobrar o cartão duas vezes, criar dois pedidos, enviar dois emails.

## Como Funciona

### O Problema

```
Client                    Server
  │                         │
  │── POST /payments ──────►│
  │                         │ (processa, cobra cartão)
  │◄── timeout ─────────────│ (resposta nunca chega)
  │
  │ Client não sabe: operação executou ou não?
  │ → Retry: POST /payments ──────►│
  │                                │ (cobra cartão de novo!)
```

### Idempotency Key

O padrão canônico: o cliente gera um ID único para a intenção de operação. O servidor usa esse ID para deduplicar.

```typescript
// Cliente gera e persiste a idempotency key antes de enviar
const idempotencyKey = crypto.randomUUID(); // salvo no client antes do request

const response = await fetch("/api/payments", {
  method: "POST",
  headers: {
    "Idempotency-Key": idempotencyKey,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ amount: 10000, currency: "BRL" })
});
```

```typescript
// Servidor: middleware de idempotência
type IdempotencyRecord = {
  key: string;
  responseStatus: number;
  responseBody: unknown;
  createdAt: Date;
};

async function idempotencyMiddleware(req: Request, res: Response, next: NextFunction) {
  const key = req.headers["idempotency-key"] as string;

  if (!key) return next(); // operações sem key passam direto (GET, por exemplo)

  const existing = await redis.get(`idempotency:${key}`);

  if (existing) {
    const record: IdempotencyRecord = JSON.parse(existing);
    // Retorna a resposta original armazenada — sem reprocessar
    return res.status(record.responseStatus).json(record.responseBody);
  }

  // Sobrescreve res.json para capturar a resposta
  const originalJson = res.json.bind(res);
  res.json = (body) => {
    const TTL_SECONDS = 86400; // 24h
    redis.setex(
      `idempotency:${key}`,
      TTL_SECONDS,
      JSON.stringify({ key, responseStatus: res.statusCode, responseBody: body, createdAt: new Date() })
    );
    return originalJson(body);
  };

  next();
}
```

### Idempotência em Banco de Dados

Para operações de escrita, use `ON CONFLICT DO NOTHING` ou `ON CONFLICT DO UPDATE` no PostgreSQL:

```sql
-- INSERT idempotente: se já existe, ignora
INSERT INTO payments (id, order_id, amount, status)
VALUES ($1, $2, $3, 'pending')
ON CONFLICT (id) DO NOTHING;

-- INSERT idempotente com upsert: atualiza apenas se o estado permite
INSERT INTO payments (id, order_id, amount, status)
VALUES ($1, $2, $3, 'pending')
ON CONFLICT (id) DO UPDATE
  SET status = EXCLUDED.status
  WHERE payments.status = 'pending'; -- só atualiza se ainda está pendente
```

### Compare-and-Swap (CAS)

Para operações condicionais, use versionamento para garantir que você está atualizando o estado que você leu:

```typescript
// Atualiza payment somente se version bate (evita lost update)
const result = await prisma.payment.updateMany({
  where: {
    id: paymentId,
    version: currentVersion  // condição de CAS
  },
  data: {
    status: "confirmed",
    version: { increment: 1 }
  }
});

if (result.count === 0) {
  throw new StalePaymentStateError(paymentId);
}
```

### Idempotência em Mensageria

Consumers de Kafka/SQS devem ser idempotentes porque `at-least-once delivery` garante que a mesma mensagem pode chegar mais de uma vez.

```typescript
// Consumer idempotente com deduplicação via Redis
async function processOrderCreated(event: OrderCreatedEvent) {
  const dedupKey = `processed:order-created:${event.id}`;

  // SET NX (set if not exists) — operação atômica
  const wasAlreadyProcessed = !(await redis.set(dedupKey, "1", "EX", 86400, "NX"));

  if (wasAlreadyProcessed) {
    console.log({ message: "Duplicate event skipped", eventId: event.id });
    return;
  }

  await createOrderInDatabase(event);
}
```

### Idempotência Financeira

Operações financeiras têm requisitos adicionais: a Idempotency Key deve ser associada a uma intent, não a uma transação. O valor não pode mudar entre retries.

```typescript
// Stripe: idempotency key gerada no frontend, enviada para o backend, repassada para Stripe
const payment = await stripe.paymentIntents.create(
  {
    amount: 10000,
    currency: "brl",
    customer: customerId
  },
  {
    idempotencyKey: `payment-${orderId}` // determinístico por pedido
  }
);
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| **Segurança de retry** | Elimina duplicações em falhas transitórias | Storage adicional para registros de dedup |
| **TTL da key** | Controla por quanto tempo a dedup é válida | TTL curto → janela de retry limitada; TTL longo → storage cresce |
| **Granularidade** | Idempotência por operação vs. por intent | Intent muito ampla pode mascarar requests legítimos diferentes |
| **Distribuído** | Redis centralizado resolve sem race condition | Ponto de falha se Redis cair (mitigar com Redis Cluster) |

## Quando Usar / Quando Evitar

**Sempre implementar em:**
- APIs de pagamento e operações financeiras
- Envio de emails/notificações
- Criação de recursos (POST) que podem ser retentados
- Consumers de mensageria (at-least-once delivery)
- Integrações com webhooks de terceiros

**Não é necessário em:**
- GET, HEAD — naturalmente idempotentes (não mudam estado)
- PUT com o objeto completo — por definição idempotente se o resultado é sempre o mesmo
- Operações onde duplicata é inócua e detectável via business logic

## Conceitos Relacionados

[[outbox-pattern]] · [[retry-backoff]] · [[saga-pattern]] · [[kafka]] · [[cqrs]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-14*
