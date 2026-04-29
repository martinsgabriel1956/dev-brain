---
type: concept
title: "Connection Pooling"
aliases: ["pgbouncer", "pool de conexões", "database pool"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [banco-de-dados, performance, pgbouncer, postgresql, escalabilidade]
skill: tech-mentor-system-design
status: stable
---

# Connection Pooling

Reutiliza conexões abertas ao banco. Sem pool, cada request abre/fecha uma conexão — overhead de handshake TCP + autenticação.

## O Problema

```
50 pods × 20 conexões = 1000 conexões simultâneas no PostgreSQL
PostgreSQL não escala bem com >200-300 conexões — overhead de memória e locks
```

## Solução com PgBouncer

```
50 pods × 20 conexões = 1000 → PgBouncer → 20 conexões reais no PostgreSQL
```

```ini
[databases]
mydb = host=postgres port=5432 dbname=mydb

[pgbouncer]
pool_mode = transaction    # recomendado: pool por transação
max_client_conn = 1000     # máximo de conexões de entrada
default_pool_size = 20     # conexões reais no banco
```

## Pool Modes

- `session` — conexão fica com o cliente durante toda a sessão. Menos eficiente.
- `transaction` — conexão retorna ao pool após cada transação. **Recomendado.**
- `statement` — retorna após cada statement. Incompatível com transações multi-statement.

## Key Sources

- [[sources/banco-de-dados]]
