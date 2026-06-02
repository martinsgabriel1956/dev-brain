---
type: concept
title: "Ledger Imutável"
aliases: ["immutable ledger", "double-entry bookkeeping", "contabilidade por partidas dobradas"]
date_created: 2026-05-31
date_updated: 2026-05-31
source_count: 1
tags: [ledger, fintech, imutabilidade, event-sourcing, auditoria]
skill: tech-mentor-backend
status: stable
---

# Ledger Imutável

## TL;DR

Em sistemas financeiros, o saldo nunca é um campo que se atualiza — é a **soma de todas as transações**. Entradas no ledger são imutáveis; erros se corrigem com entradas de estorno, nunca com UPDATE/DELETE. Isso é [[imutabilidade]] aplicada ao domínio financeiro.

## Modelo

```sql
-- Transferência de R$100 da conta A para B
INSERT INTO ledger_entries (account_id, amount, type, transaction_id) VALUES
  ('account_a', -100, 'debit',  'txn_xyz'),
  ('account_b', +100, 'credit', 'txn_xyz');

-- Saldo calculado por agregação (nunca campo mutable)
SELECT SUM(amount) AS saldo
FROM ledger_entries
WHERE account_id = 'account_a';

-- Invariante: soma de todas as entradas = 0 (double-entry)
SELECT SUM(amount) FROM ledger_entries;  -- deve retornar 0
```

## Por que Nunca UPDATE/DELETE

- **Auditoria** — reguladores exigem trilha completa
- **Compliance** — PCI-DSS, SOX, BACEN exigem histórico imutável
- **Reprodutibilidade** — dado qualquer ponto no tempo, o saldo é calculável
- **Confiança** — impossível "fazer desaparecer" uma transação

## Conexão com Event Sourcing

O ledger imutável é [[event-sourcing]] aplicado ao domínio financeiro:
- Cada entrada = um evento imutável
- Saldo atual = replay / soma de todos os eventos
- [[Datomic]] implementa esse padrão a nível de banco de dados

## Uso no Nubank

O [[nubank]] usa esse padrão como base do sistema financeiro. A imutabilidade do ledger, combinada com [[datomic]] e [[event-sourcing]], dá ao Nubank time-travel e auditoria nativa — algo que bancos legados não conseguem oferecer.

## Key Sources

- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
