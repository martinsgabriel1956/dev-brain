---
type: concept
title: "Ledger de Dupla Entrada"
aliases: ["double entry bookkeeping", "ledger", "razão contábil"]
date_created: 2026-04-23
date_updated: 2026-07-27
source_count: 2
tags: [fintech, ledger, double-entry, contabilidade, append-only, imutabilidade, idempotencia]
skill: tech-mentor-system-design
status: stub
---

# Ledger de Dupla Entrada

Modelo contábil onde cada transação gera exatamente duas entradas: um débito e um crédito de mesmo valor. A soma de todos os débitos sempre iguala a soma de todos os créditos.

**Regra fundamental:** ledger é append-only — nunca UPDATE ou DELETE em transações. Erros são corrigidos com estorno (nova entrada de compensação).

**Schema essencial:**
- `accounts` — contas (usuário, empresa, taxa, etc.)
- `transactions` — cabeçalho da transação com idempotency_key
- `ledger_entries` — entradas individuais (debit/credit) com referência à transaction

**Conciliação:** comparação periódica entre ledger interno e extrato da adquirente/banco para detectar discrepâncias.

**Por que double entry:** qualquer soma de entries por conta deve fechar a zero — invariante que detecta bugs.

## Lançamento e Chave de Idempotência na Mesma Transação

Quando o efeito financeiro mora no mesmo banco do ledger, o `ledger_entry` e a mudança do status da [[wiki/concepts/idempotencia|chave de idempotência]] para `completed` devem confirmar na mesma transação local. Isso evita dois estados inconsistentes: uma chave marcada como concluída sem lançamento correspondente, ou um lançamento confirmado com a chave ainda `processing`. Ver [[wiki/concepts/distributed-transactions]] para a distinção entre o que a transação garante (atomicidade do lançamento) e o que a idempotência garante (o lançamento não se repete em retry).

## Key Sources

- [[sources/fintech-system-design]]
- [[wiki/sources/idempotencia-pagamentos-retry-sistemas-distribuidos]] — lançamento e status da chave confirmando atomicamente na mesma transação local
