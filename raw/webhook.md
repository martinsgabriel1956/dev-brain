---
date: 2026-04-16
tags: [tech-mentor, backend, apis, webhook, hmac, segurança, retry]
skill: tech-mentor-backend/references/apis
level: intermediário
---

# Webhooks — HMAC, Retry e Fanout

## Contexto

Webhook é o inverso de polling: em vez do consumer perguntar "tem novidade?", o producer empurra eventos HTTP quando algo acontece. É o padrão de integração mais simples para notificações assíncronas — mas tem armadilhas sérias: replay attacks, ordem de entrega, falhas de receiver, e fanout para múltiplos destinos.

---

## Assinatura HMAC — Verificação de Autenticidade

Sem verificação de assinatura, qualquer um pode enviar um POST para o endpoint do webhook. HMAC garante que a requisição veio de quem tem o segredo compartilhado.

### No Producer — Assinar o Payload

```typescript
import { createHmac } from "crypto";

type WebhookPayload = {
  event: string;
  data: Record<string, unknown>;
  timestamp: string;
};

function signWebhook(payload: WebhookPayload, secret: string): string {
  const body = JSON.stringify(payload);
  return createHmac("sha256", secret)
    .update(body)
    .digest("hex");
}

async function sendWebhook(
  endpoint: string,
  payload: WebhookPayload,
  secret: string
): Promise<void> {
  const signature = signWebhook(payload, secret);
  const body = JSON.stringify(payload);

  const response = await fetch(endpoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-Webhook-Signature": `sha256=${signature}`,
      "X-Webhook-Timestamp": payload.timestamp,
      "X-Webhook-Id": crypto.randomUUID()  // para deduplicação no receiver
    },
    body,
    signal: AbortSignal.timeout(10000)  // timeout de 10s
  });

  if (!response.ok) {
    throw new Error(`Webhook failed: ${response.status}`);
  }
}
```

### No Consumer — Verificar a Assinatura

```typescript
import { createHmac, timingSafeEqual } from "crypto";
import type { Request, Response } from "express";

const WEBHOOK_SECRET = process.env.WEBHOOK_SECRET!;
const MAX_TIMESTAMP_DIFF_SECONDS = 300;  // 5 minutos — previne replay attacks

function verifyWebhookSignature(
  rawBody: Buffer,
  signature: string,
  timestamp: string
): boolean {
  // 1. Verificar timestamp para prevenir replay attacks
  const now = Math.floor(Date.now() / 1000);
  const webhookTime = Math.floor(new Date(timestamp).getTime() / 1000);

  if (Math.abs(now - webhookTime) > MAX_TIMESTAMP_DIFF_SECONDS) {
    return false;
  }

  // 2. Recalcular HMAC com o body cru (antes de parsear JSON)
  const expectedSignature = `sha256=${createHmac("sha256", WEBHOOK_SECRET)
    .update(rawBody)
    .digest("hex")}`;

  const receivedSignature = Buffer.from(signature);
  const computedSignature = Buffer.from(expectedSignature);

  // 3. timingSafeEqual — previne timing attacks
  // Comparar strings diretamente vaza informação via tempo de execução
  if (receivedSignature.length !== computedSignature.length) return false;

  return timingSafeEqual(receivedSignature, computedSignature);
}

// Middleware Express — manter rawBody antes do json parser
function rawBodyMiddleware(req: Request, res: Response, next: () => void) {
  let data = Buffer.alloc(0);
  req.on("data", chunk => { data = Buffer.concat([data, chunk]); });
  req.on("end", () => {
    req.rawBody = data;
    next();
  });
}

// Handler do webhook
async function handleWebhook(req: Request, res: Response) {
  const signature = req.headers["x-webhook-signature"] as string;
  const timestamp = req.headers["x-webhook-timestamp"] as string;
  const webhookId = req.headers["x-webhook-id"] as string;

  if (!signature || !timestamp) {
    return res.status(400).json({ error: "Missing webhook headers" });
  }

  // Verificar assinatura ANTES de processar
  const isValid = verifyWebhookSignature(req.rawBody!, signature, timestamp);
  if (!isValid) {
    return res.status(401).json({ error: "Invalid signature" });
  }

  // Deduplicar por webhookId — evita processar duas vezes se producer fizer retry
  const alreadyProcessed = await redis.get(`webhook:${webhookId}`);
  if (alreadyProcessed) {
    return res.status(200).json({ status: "already_processed" });
  }

  // Responder imediatamente (200) e processar de forma assíncrona
  // O producer não deve aguardar o processamento completo
  res.status(200).json({ status: "received" });

  // Processar em background — falhar aqui não afeta o status 200
  setImmediate(async () => {
    try {
      await redis.setex(`webhook:${webhookId}`, 86400, "1");  // TTL 24h
      await processWebhookEvent(req.body);
    } catch (error) {
      console.log({ message: "Webhook processing failed", webhookId, error });
    }
  });
}
```

---

## Retry com Backoff Exponencial

O producer deve persistir o webhook e retentar em caso de falha do receiver:

```typescript
import { Queue, Worker } from "bullmq";

type WebhookJob = {
  endpoint: string;
  payload: WebhookPayload;
  secret: string;
  webhookId: string;
};

const webhookQueue = new Queue<WebhookJob>("webhooks", {
  connection,
  defaultJobOptions: {
    attempts: 5,
    backoff: {
      type: "exponential",
      delay: 1000  // 1s, 2s, 4s, 8s, 16s
    },
    removeOnComplete: { count: 1000 },
    removeOnFail: false  // manter para inspeção
  }
});

// Enfileirar webhook ao invés de enviar diretamente
async function dispatchWebhook(endpoint: string, payload: WebhookPayload, secret: string) {
  const webhookId = crypto.randomUUID();
  await webhookQueue.add("send-webhook", { endpoint, payload, secret, webhookId });
}

// Worker que executa o envio
const webhookWorker = new Worker<WebhookJob>("webhooks", async job => {
  const { endpoint, payload, secret, webhookId } = job.data;

  try {
    await sendWebhook(endpoint, { ...payload, timestamp: new Date().toISOString() }, secret);
    console.log({ message: "Webhook delivered", webhookId, attempt: job.attemptsMade + 1 });
  } catch (error) {
    console.log({ message: "Webhook failed, will retry", webhookId, attempt: job.attemptsMade + 1 });
    throw error;  // BullMQ vai retentar conforme backoff configurado
  }
}, { connection, concurrency: 10 });

webhookWorker.on("failed", (job, error) => {
  if (job && job.attemptsMade >= 5) {
    // Notificar o usuário que o endpoint está falhando
    console.log({ message: "Webhook permanently failed", endpoint: job.data.endpoint });
  }
});
```

---

## Fanout — Um Evento para Múltiplos Subscribers

```typescript
type WebhookSubscription = {
  id: string;
  userId: string;
  endpoint: string;
  secret: string;
  events: string[];  // ["order.created", "order.cancelled"]
};

async function fanoutWebhook(
  eventType: string,
  payload: Record<string, unknown>
): Promise<void> {
  // Buscar todos os subscribers interessados neste evento
  const subscriptions = await prisma.webhookSubscription.findMany({
    where: {
      events: { has: eventType },
      isActive: true
    }
  });

  if (subscriptions.length === 0) return;

  const webhookPayload: WebhookPayload = {
    event: eventType,
    data: payload,
    timestamp: new Date().toISOString()
  };

  // Enfileirar em paralelo para todos os subscribers
  await Promise.all(
    subscriptions.map(sub =>
      dispatchWebhook(sub.endpoint, webhookPayload, sub.secret)
    )
  );

  console.log({ message: "Webhook fanout dispatched", eventType, subscribers: subscriptions.length });
}

// Chamada ao criar um pedido
await fanoutWebhook("order.created", { orderId: order.id, total: order.total });
```

---

## Modelo de Dados para Webhooks

```sql
-- Subscriptions — quem quer receber o quê
CREATE TABLE webhook_subscriptions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id),
  endpoint TEXT NOT NULL,
  secret TEXT NOT NULL,  -- armazenar criptografado (AES-256 ou KMS)
  events TEXT[] NOT NULL,  -- array de event types
  is_active BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Delivery log — auditoria e debug
CREATE TABLE webhook_deliveries (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  subscription_id UUID NOT NULL REFERENCES webhook_subscriptions(id),
  webhook_id UUID NOT NULL,  -- X-Webhook-Id
  event_type TEXT NOT NULL,
  payload JSONB NOT NULL,
  response_status INT,
  response_body TEXT,
  attempt_number INT NOT NULL DEFAULT 1,
  delivered_at TIMESTAMPTZ,
  failed_at TIMESTAMPTZ,
  error_message TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

---

## Trade-offs

| Aspecto | Webhook | Polling |
|---|---|---|
| **Latência de entrega** | Imediata (push) | Depende do intervalo de poll |
| **Carga no producer** | Alta com muitos subscribers (fanout) | Baixa — responde quando consultado |
| **Carga no consumer** | Precisa de endpoint público | Pode rodar em qualquer lugar |
| **Confiabilidade** | Requer retry + persistência | Pode perder eventos entre polls |
| **Debug** | Complexo (assinatura, timing, replay) | Simples — query qualquer hora |
| **Segurança** | HMAC obrigatório | Autenticação da API |

## Quando Usar / Quando Evitar

**Webhook:** integrações B2B, notificações de pagamento (Stripe, Mercado Pago), deploys CI/CD, sincronização entre sistemas externos.

**Evitar webhook quando:** o consumer não tem endpoint público (mobile, CLI), eventos têm volume muito alto (>1000/s por subscriber → usar Kafka), ou o receiver é instável (vai perder muitos webhooks — prefira polling).

**Segurança mínima obrigatória:** HMAC com `timingSafeEqual`, validação de timestamp contra replay, deduplicação por `X-Webhook-Id`.

## Conceitos Relacionados

[[rest-openapi]] · [[background-jobs]] · [[dlq-event-patterns]] · [[idempotencia]] · [[rate-limiting]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-16*
