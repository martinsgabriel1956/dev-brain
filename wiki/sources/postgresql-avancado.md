---
type: source
title: "PostgreSQL Avançado"
aliases: ["postgresql avancado", "mvcc", "vacuum", "wal", "explain analyze", "window functions", "ctes recursivas"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/postgresql-avancado.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [postgresql, mvcc, vacuum, wal, explain-analyze, btree, gin, brin, window-functions, cte-recursiva, skip-locked, acid, isolation-levels]
skill: tech-mentor-data
status: stable
---

## TL;DR

PostgreSQL usa MVCC: UPDATE/DELETE não sobrescrevem — criam novas versões. Vacuum limpa dead tuples. WAL garante durabilidade. EXPLAIN ANALYZE é obrigatório para diagnóstico de performance. Índices especializados: B-tree (padrão), GIN (JSONB/full-text), BRIN (dados temporais ordenados). Window Functions e CTEs Recursivas para analytics.

## Key Claims

**Claim:** MVCC permite leituras sem bloquear escritas — mas gera dead tuples que precisam de Vacuum.
**Evidence:** UPDATE cria nova versão da linha, não sobrescreve. Dead tuples acumulam, incham tabelas, degradam performance. Autovacuum resolve automaticamente, mas precisa de tuning para tabelas de alta escrita (scale_factor muito baixo).
**Confidence:** alta

**Claim:** EXPLAIN ANALYZE é a ferramenta principal de diagnóstico — ler e interpretar é skill obrigatório.
**Evidence:** Seq Scan em tabela grande = índice ausente ou não usado. Nested Loop com muitas iterações = N+1. Hash Join vs Merge Join vs Nested Loop: cada um tem casos ideais. Buffers compartilhados mostram cache hit ratio.
**Confidence:** alta

**Claim:** Índices GIN são obrigatórios para JSONB e full-text search — B-tree não funciona nesses casos.
**Evidence:** `WHERE data @> '{"status": "active"}'` sem GIN = Seq Scan. GIN indexa cada chave/valor do JSONB separadamente. Para full-text: GIN com `tsvector`. Trade-off: GIN é mais lento para escrita, muito mais rápido para leitura JSONB.
**Confidence:** alta

**Claim:** Window Functions substituem subqueries correlacionadas com performance muito superior.
**Evidence:** `ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY created_at DESC)` para ranquear pedidos por cliente. Alternativa sem window function: subquery correlacionada O(n²). Window function: O(n log n).
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/mvcc]]
- [[concepts/vacuum-postgresql]]
- [[concepts/wal]]
- [[concepts/explain-analyze]]
- [[concepts/gin-index]]
- [[concepts/window-functions]]
- [[concepts/cte-recursiva]]
- [[concepts/isolation-levels]]

## Open Questions

- Autovacuum agressivo em tabelas de alta escrita — como monitorar que o vacuum está acompanhando a taxa de inserção?
- BRIN index: qual o tamanho mínimo de tabela para justificar BRIN vs B-tree em colunas de timestamp?
