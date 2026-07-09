---
type: concept
title: "Idempotência"
aliases: ["idempotência", "idempotency", "idempotency key"]
date_created: 2026-04-22
date_updated: 2026-07-09
source_count: 3
tags: [distribuidos, resiliencia, api, retry, mensageria, double-spend, double-submit]
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

## Double Spend / Double Submit — a Chave Gerada pelo Servidor

Double spend (transações) e double submit (formulários) são o mesmo problema por ângulos diferentes: um request se duplica por bug, duplo clique acidental ou abuso deliberado.

Variante importante do padrão: em vez do **cliente** gerar e enviar a Idempotency Key (vulnerável — um atacante reenvia o request com uma chave diferente e burla a dedução), o **servidor** pode gerar a chave como um **hash dos campos submetidos** (ex.: origem, destino, data do voo). Isso torna a dedução robusta contra reenvio malicioso, não só contra duplo clique acidental.

A definição de quais campos entram no hash — e qual a janela de tempo que caracteriza duplicidade (a mesma compra hoje vs. amanhã pode ser legítima) — é uma **decisão de negócio**, não só técnica.

Camadas complementares, cada uma cobrindo um ângulo diferente do problema:

| Camada | Cobre duplo clique acidental? | Cobre abuso deliberado? |
|---|---|---|
| Desabilitar botão de submit no frontend | Sim | Não — atacante ignora o frontend |
| Redirect após POST (padrão [[wiki/concepts/post-redirect-get]]) | Sim | Não |
| Idempotency Key (hash gerado no servidor + storage compartilhado) | Sim | Sim |
| Unique Constraint no banco (quando existe campo genuinamente único) | Sim | Sim — mas só se há campo único aplicável |

## Key Sources

- [[sources/retry-backoff]]
- [[wiki/sources/acoplamento-abstracao-estado]]
- [[wiki/sources/operador-de-crud-vs-engenheiro-repertorio]] — idempotência como resposta ao webhook duplicado; errar at-least-once vs. exactly-once cobra o cliente em dobro ou perde o pedido
- [[wiki/sources/double-spend-double-submit]] — double spend/double submit como o mesmo problema; chave de idempotência gerada no servidor via hash dos campos (mais robusta que chave enviada pelo cliente); janela de tempo de duplicidade como decisão de negócio
