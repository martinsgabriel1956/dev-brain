---
date: 2026-04-17
tags: [tech-mentor, system-design, fintech, ledger, antifraude, pagamento]
skill: tech-mentor-system-design/references/domain-design
level: arquiteto
---

# FinTech System Design — Ledger, Idempotência Financeira e Antifraude

## Ledger de Dupla Entrada

### Contexto
Todo sistema financeiro sério usa **double-entry bookkeeping** (partidas dobradas). Cada transação gera pelo menos dois lançamentos: um a débito e um a crédito. A soma de todos os lançamentos deve ser zero — isso é a garantia de integridade financeira.

```
Transferência de Alice → Bob: R$ 100

entries:
  account: alice-checking,  amount: -100, type: debit
  account: bob-checking,    amount: +100, type: credit

invariante: SUM(amount) = 0 sempre
```

### Schema

```sql
-- Imutável — nunca UPDATE ou DELETE
CREATE TABLE ledger_entries (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  transaction_id  UUID NOT NULL REFERENCES transactions(id),
  account_id      UUID NOT NULL,
  amount          NUMERIC(20, 8) NOT NULL,  -- cents ou satoshis
  entry_type      TEXT NOT NULL CHECK (entry_type IN ('debit', 'credit')),
  currency        TEXT NOT NULL DEFAULT 'BRL',
  created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Transação é o envelope que agrupa entries
CREATE TABLE transactions (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  idempotency_key TEXT NOT NULL UNIQUE,  -- chave de idempotência
  description     TEXT NOT NULL,
  status          TEXT NOT NULL DEFAULT 'pending',
  created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

```typescript
// Sempre usar $transaction para garantir atomicidade
async function transfer(fromAccountId: string, toAccountId: string, amount: number, idempotencyKey: string) {
  return await prisma.$transaction(async tx => {
    // Idempotência: se já processada, retorna o resultado anterior
    const existing = await tx.transaction.findUnique({ where: { idempotencyKey } });
    if (existing) return existing;

    // Verificar saldo antes de criar as entries
    const balance = await getBalance(fromAccountId, tx);
    if (balance < amount) throw new InsufficientFundsError();

    const transaction = await tx.transaction.create({
      data: { idempotencyKey, description: `Transfer ${fromAccountId} → ${toAccountId}`, status: "completed" }
    });

    // Dupla entrada — sempre balanceado
    await tx.ledgerEntry.createMany({
      data: [
        { transactionId: transaction.id, accountId: fromAccountId, amount: -amount, entryType: "debit", currency: "BRL" },
        { transactionId: transaction.id, accountId: toAccountId, amount: amount, entryType: "credit", currency: "BRL" }
      ]
    });

    return transaction;
  });
}

async function getBalance(accountId: string, tx = prisma): Promise<number> {
  const result = await tx.ledgerEntry.aggregate({
    where: { accountId },
    _sum: { amount: true }
  });
  return Number(result._sum.amount ?? 0);
}
```

---

## Idempotência Financeira

Toda operação financeira deve ser idempotente — chamar N vezes com o mesmo input deve ter o mesmo resultado que chamar 1 vez. Sem isso, retries causam cobranças duplicadas.

```typescript
// Padrão completo de Idempotency Key
async function processPayment(request: PaymentRequest, idempotencyKey: string) {
  // 1. Verificar se já foi processada (com lock para evitar race condition)
  const existing = await redis.get(`payment:${idempotencyKey}`);
  if (existing) return JSON.parse(existing); // retorna resultado cacheado

  // 2. Adquirir lock para evitar processamento paralelo da mesma key
  const lockAcquired = await redis.set(
    `lock:payment:${idempotencyKey}`, "1", { NX: true, EX: 30 }
  );
  if (!lockAcquired) throw new ConflictError("Payment processing in progress");

  try {
    // 3. Processar
    const result = await chargeCard(request);

    // 4. Salvar resultado com TTL longo (24h)
    await redis.setEx(`payment:${idempotencyKey}`, 86400, JSON.stringify(result));

    return result;
  } finally {
    await redis.del(`lock:payment:${idempotencyKey}`);
  }
}
```

---

## Antifraude — Arquitetura em Camadas

```
Request de pagamento
        │
  ┌─────▼──────────────────────────────┐
  │  Camada 1: Regras Síncronas        │ < 100ms
  │  - Velocidade (N transações/hora)  │
  │  - Valor atípico para o usuário    │
  │  - BIN de cartão bloqueado         │
  └─────┬──────────────────────────────┘
        │ passa
  ┌─────▼──────────────────────────────┐
  │  Camada 2: ML Score (síncrono)     │ < 200ms
  │  - Feature vector do usuário       │
  │  - Modelo XGBoost/LightGBM         │
  │  - Score 0-100                     │
  └─────┬──────────────────────────────┘
        │ score < threshold
  ┌─────▼──────────────────────────────┐
  │  Autorizar e continuar             │
  └─────────────────────────────────────┘
        │ score >= threshold
  ┌─────▼──────────────────────────────┐
  │  Camada 3: Revisão Manual / 3DS    │
  │  ou Rejeitar                       │
  └─────────────────────────────────────┘

  Assíncrono (pós-autorização):
  ┌─────────────────────────────────────┐
  │  Análise de grafo de relacionamento │
  │  - Dispositivos compartilhados      │
  │  - IPs em comum entre contas        │
  │  - Padrão de merchant suspeito      │
  │  → Bloquear conta retroativamente  │
  └─────────────────────────────────────┘
```

---

## Conciliação Financeira

Comparação periódica entre o ledger interno e os extratos dos processadores (Stripe, Adyen) para detectar divergências.

```typescript
async function reconcile(date: Date) {
  const [internalEntries, stripeTransactions] = await Promise.all([
    ledgerRepo.getByDate(date),
    stripe.balanceTransactions.list({ created: { gte: startOfDay(date), lte: endOfDay(date) } })
  ]);

  const discrepancies = [];

  for (const entry of internalEntries) {
    const stripeMatch = stripeTransactions.find(t => t.metadata.idempotencyKey === entry.idempotencyKey);
    
    if (!stripeMatch) {
      discrepancies.push({ type: "MISSING_IN_STRIPE", entry });
    } else if (Math.abs(stripeMatch.amount - entry.amountCents) > 0) {
      discrepancies.push({ type: "AMOUNT_MISMATCH", entry, stripeAmount: stripeMatch.amount });
    }
  }

  await discrepancyRepo.saveAll(discrepancies);
  await alertService.notifyIfCritical(discrepancies);
}
```

## Conceitos Relacionados
[[idempotencia]] · [[saga-pattern]] · [[outbox-pattern]] · [[two-phase-commit]] · [[estimativas-back-of-envelope]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-17*
