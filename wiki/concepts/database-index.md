---
type: concept
title: "Database Index"
aliases: ["índice de banco de dados", "índice composto", "índice parcial"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [banco-de-dados, performance, postgresql, index, system-design]
skill: tech-mentor-system-design
status: stable
---

# Database Index

Estrutura de dados que acelera queries ao custo de overhead em escritas.

## Tipos

```sql
-- Simples
CREATE INDEX idx_orders_user_id ON orders(user_id);

-- Composto — otimiza WHERE user_id = ? AND status = ?
CREATE INDEX idx_orders_user_status ON orders(user_id, status);

-- Parcial — indexa apenas subset dos dados
CREATE INDEX idx_orders_pending ON orders(created_at)
WHERE status = 'pending';
```

## Diagnóstico

```sql
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = '123';
-- Seq Scan       → full table scan → precisa de índice
-- Index Scan     → usando índice → OK
-- Index Only Scan → resposta direto do índice → melhor caso
```

## Regra

Indexe colunas em `WHERE`, `JOIN ON`, `ORDER BY`, `GROUP BY`. **Índice tem custo**: cada `INSERT`/`UPDATE`/`DELETE` atualiza todos os índices. Tabela com 15 índices faz 15x mais trabalho por escrita.

## Key Sources

- [[sources/banco-de-dados]]
