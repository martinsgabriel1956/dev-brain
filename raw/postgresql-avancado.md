---
date: 2026-04-13
tags: [tech-mentor, backend, postgresql, banco-de-dados, performance, sql]
skill: tech-mentor-backend/references/database
level: avançado
---

# PostgreSQL Avançado

## Contexto

PostgreSQL é o banco relacional de referência para produção. Esta nota cobre os mecanismos internos e features avançadas que diferenciam um dev que "sabe SQL" de um arquiteto que entende como o banco funciona e como extrair o máximo de performance.

## MVCC — Multi-Version Concurrency Control

### Como Funciona

PostgreSQL usa MVCC para garantir que **leituras nunca bloqueiam escritas** e vice-versa. Em vez de locks em linhas, cada transaction vê um snapshot consistente do banco.

```
Cada linha tem:
  xmin: ID da transaction que criou a linha
  xmax: ID da transaction que deletou/atualizou a linha (0 = linha viva)

Transaction 100 faz SELECT:
  Vê linhas onde xmin <= 100 AND (xmax = 0 OR xmax > 100)
  → Vê apenas o que existia quando a transaction começou
```

```sql
-- Verificar xmin/xmax de linhas
SELECT id, name, xmin, xmax FROM users WHERE id = 1;
```

### Vacuum — Limpeza de Dead Tuples

UPDATE e DELETE não removem fisicamente as linhas — criam novas versões. As versões antigas (dead tuples) são limpas pelo Vacuum:

```sql
-- Verificar bloat de uma tabela
SELECT
  schemaname,
  tablename,
  pg_size_pretty(pg_total_relation_size(schemaname || '.' || tablename)) AS total_size,
  n_dead_tup AS dead_tuples,
  n_live_tup AS live_tuples,
  round(100 * n_dead_tup::numeric / NULLIF(n_live_tup + n_dead_tup, 0), 2) AS dead_ratio
FROM pg_stat_user_tables
WHERE n_dead_tup > 1000
ORDER BY dead_ratio DESC;

-- Forçar vacuum em tabela específica
VACUUM ANALYZE orders;

-- Vacuum com bloat recovery (reescreve a tabela)
VACUUM FULL orders;  -- cuidado: lock exclusivo!
```

**Autovacuum tuning para tabelas de alta escrita:**
```sql
ALTER TABLE orders SET (
  autovacuum_vacuum_scale_factor = 0.01,   -- vacuum quando 1% de dead tuples (padrão: 20%)
  autovacuum_analyze_scale_factor = 0.005, -- analyze quando 0.5% de novas linhas
  autovacuum_vacuum_cost_delay = 2         -- ms de delay (reduz impacto em I/O)
);
```

## WAL — Write-Ahead Log

O WAL é o mecanismo de durabilidade do PostgreSQL. **Toda mudança é escrita no WAL antes de ser aplicada nos data files**. Permite:
- Recovery após crash (replay do WAL)
- Replicação física/lógica
- Change Data Capture (CDC com Debezium)

```sql
-- Verificar posição atual no WAL
SELECT pg_current_wal_lsn();

-- Verificar lag de replicação
SELECT
  client_addr,
  state,
  sent_lsn,
  write_lsn,
  flush_lsn,
  replay_lsn,
  pg_size_pretty(sent_lsn - replay_lsn) AS replication_lag
FROM pg_stat_replication;
```

## EXPLAIN ANALYZE — Lendo Planos de Execução

```sql
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT u.name, COUNT(o.id) AS order_count
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
WHERE u.status = 'active'
  AND o.created_at > NOW() - INTERVAL '30 days'
GROUP BY u.id;
```

**O que procurar:**

```
Seq Scan → ausência de índice ou seletividade baixa
  custo: (seq scan em 1M linhas) > (index scan em 1000 linhas)

Hash Join / Merge Join → joins eficientes
Nested Loop → problemático para tabelas grandes

Buffers: shared hit=X read=Y
  hit = dados já em cache (shared_buffers)
  read = I/O do disco (evitar!)

Rows Removed by Filter: 999000
  → índice existe mas não está sendo usado corretamente
```

**Índice composto para queries frequentes:**
```sql
-- Query: WHERE status = 'active' AND created_at > X ORDER BY created_at DESC
CREATE INDEX CONCURRENTLY idx_orders_status_created
  ON orders (status, created_at DESC)
  WHERE status IN ('placed', 'processing');  -- Partial Index
```

## Índices Especializados

### B-tree (padrão)

```sql
-- Equality e range queries
CREATE INDEX idx_users_email ON users (email);
CREATE INDEX idx_orders_created ON orders (created_at DESC);

-- Covering Index — inclui colunas extras para evitar heap scan
CREATE INDEX idx_orders_user_covering ON orders (user_id)
  INCLUDE (status, total, created_at);
-- SELECT user_id, status, total, created_at FROM orders WHERE user_id = $1
-- → Apenas index scan, sem acessar a tabela (heap)
```

### GIN — Full-Text Search e JSONB

```sql
-- Full-text search em português
ALTER TABLE products ADD COLUMN tsv tsvector
  GENERATED ALWAYS AS (to_tsvector('portuguese', name || ' ' || description)) STORED;

CREATE INDEX idx_products_tsv ON products USING GIN (tsv);

-- Query
SELECT * FROM products
WHERE tsv @@ plainto_tsquery('portuguese', 'tênis corrida');

-- JSONB queries
CREATE INDEX idx_orders_metadata ON orders USING GIN (metadata);
SELECT * FROM orders WHERE metadata @> '{"source": "mobile"}';
```

### BRIN — Para Dados Ordenados Naturalmente

```sql
-- Bom para tabelas de logs/eventos onde inserted_at é crescente
CREATE INDEX idx_events_created_brin ON events USING BRIN (created_at)
  WITH (pages_per_range = 128);
-- Muito menor que B-tree, eficiente para range queries em dados sequenciais
```

## SQL Avançado

### Window Functions

```sql
-- Ranking de pedidos por cliente
SELECT
  order_id,
  user_id,
  total,
  RANK() OVER (PARTITION BY user_id ORDER BY total DESC) AS rank_in_user,
  ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_at DESC) AS recency_rank,
  LAG(total, 1) OVER (PARTITION BY user_id ORDER BY created_at) AS prev_order_total,
  LEAD(total, 1) OVER (PARTITION BY user_id ORDER BY created_at) AS next_order_total,
  SUM(total) OVER (PARTITION BY user_id) AS total_spent
FROM orders
WHERE status = 'completed';
```

```sql
-- Running total (totalizador acumulado)
SELECT
  date_trunc('day', created_at) AS day,
  COUNT(*) AS daily_orders,
  SUM(COUNT(*)) OVER (ORDER BY date_trunc('day', created_at)
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_orders
FROM orders
GROUP BY 1
ORDER BY 1;
```

### CTEs Recursivas

```sql
-- Hierarquia de categorias (árvore)
WITH RECURSIVE category_tree AS (
  -- Base case: categorias raiz
  SELECT id, name, parent_id, 0 AS depth, ARRAY[id] AS path
  FROM categories
  WHERE parent_id IS NULL

  UNION ALL

  -- Recursive case: filhos
  SELECT c.id, c.name, c.parent_id, ct.depth + 1, ct.path || c.id
  FROM categories c
  JOIN category_tree ct ON c.parent_id = ct.id
  WHERE NOT c.id = ANY(ct.path)  -- evita loops
)
SELECT * FROM category_tree ORDER BY path;
```

### SKIP LOCKED — Filas no Banco

```sql
-- Pattern de fila de jobs sem SELECT FOR UPDATE blocking
SELECT id, payload
FROM jobs
WHERE status = 'pending'
  AND scheduled_at <= NOW()
ORDER BY scheduled_at
LIMIT 10
FOR UPDATE SKIP LOCKED;

-- Worker processa e atualiza
UPDATE jobs SET status = 'processing', started_at = NOW()
WHERE id = ANY($1);
```

### Upsert com Idempotência

```sql
-- Criar ou atualizar sem perder dados existentes
INSERT INTO user_settings (user_id, key, value, updated_at)
VALUES ($1, $2, $3, NOW())
ON CONFLICT (user_id, key)
DO UPDATE SET
  value = EXCLUDED.value,
  updated_at = NOW()
WHERE user_settings.value != EXCLUDED.value;  -- evita update desnecessário
```

## ACID e Isolation Levels

```sql
-- Read Committed (padrão) — vê commits de outras transactions no meio da sua
-- Repeatable Read — snapshot no início da transaction, evita phantom reads
-- Serializable — completamente isolado, mais lento

-- Para operações financeiras críticas:
BEGIN;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
  SELECT balance FROM accounts WHERE id = $1 FOR UPDATE;
  UPDATE accounts SET balance = balance - $2 WHERE id = $1;
  UPDATE accounts SET balance = balance + $2 WHERE id = $3;
COMMIT;
```

## pg_stat_statements — Análise de Performance

```sql
-- Top 10 queries por tempo total
SELECT
  round(total_exec_time::numeric, 2) AS total_ms,
  calls,
  round(mean_exec_time::numeric, 2) AS mean_ms,
  round(stddev_exec_time::numeric, 2) AS stddev_ms,
  rows,
  substring(query, 1, 100) AS query
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;
```

## Conceitos Relacionados

[[banco-de-dados]] · [[prisma]] · [[redis]] · [[cqrs]] · [[outbox-pattern]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-13*
