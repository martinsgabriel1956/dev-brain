---
type: concept
title: "Idempotência"
aliases: ["idempotência", "idempotency", "idempotency key"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [distribuidos, resiliencia, api, retry, mensageria]
skill: tech-mentor-system-design
status: stable
---

# Idempotência

Propriedade de uma operação que produz o mesmo resultado independente do número de vezes que é executada. Pré-requisito para [[concepts/retry-backoff]] seguro.

## O Problema sem Idempotência

```typescript
// ❌ Retry cria cobrança duplicada
async function chargeCard(orderId: string, amountCents: number) {
  return stripe.charges.create({ amount: amountCents, currency: "brl" });
}
// 3 retries = 3 cobranças
```

## A Solução: Idempotency Key

```typescript
// ✅ Stripe processa exatamente uma vez — retries são seguros
async function chargeCard(orderId: string, amountCents: number) {
  return stripe.charges.create(
    { amount: amountCents, currency: "brl" },
    { idempotencyKey: `order-${orderId}` }
  );
}
```

## Como Implementar em APIs Próprias

```typescript
// Cliente envia Idempotency-Key no header
// Servidor armazena resultado por key (ex: Redis com TTL de 24h)
// Segunda request com mesma key retorna resultado cacheado sem re-executar

async function processPayment(idempotencyKey: string, data: PaymentData) {
  const cached = await redis.get(`idem:${idempotencyKey}`);
  if (cached) return JSON.parse(cached);

  const result = await executePayment(data);
  await redis.set(`idem:${idempotencyKey}`, JSON.stringify(result), "EX", 86400);
  return result;
}
```

## Operações Naturalmente Idempotentes

- GET, HEAD, OPTIONS (HTTP)
- DELETE (o recurso ou já não existe)
- UPDATE com valor absoluto (`SET balance = 100` vs `SET balance = balance - 10`)

## Operações que Precisam de Idempotency Key

- POST que cria recursos ou processa pagamentos
- Qualquer operação com efeito colateral financeiro

## Key Sources

- [[sources/retry-backoff]]
- [[wiki/sources/acoplamento-abstracao-estado]]
