---
type: concept
title: "Ledger de Dupla Entrada"
aliases: ["double entry bookkeeping", "ledger", "razão contábil"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 1
tags: [fintech, ledger, double-entry, contabilidade, append-only, imutabilidade]
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

## Key Sources

- [[sources/fintech-system-design]]
