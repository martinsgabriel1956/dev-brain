---
type: concept
title: "Connection Pooling"
aliases: ["pgbouncer", "pool de conexões", "database pool"]
date_created: 2026-04-22
date_updated: 2026-07-07
source_count: 2
tags: [banco-de-dados, performance, pgbouncer, postgresql, mysql, escalabilidade]
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

## Diagnóstico: Tempo de Conexão Segurada, Não Latência de Query

Um sistema pode ter CPU baixa e queries individuais rápidas e ainda assim bater um teto de escalabilidade — porque o gargalo real é uma parte do código segurando conexões do pool por mais tempo do que deveria, esgotando o pool para todo o resto. Otimizar a query em si não resolve, porque a query não é o problema. A técnica de diagnóstico é etiquetar cada operação SQL por origem (ex: "checkout", "reserva") e medir **quanto tempo cada uma segura uma conexão aberta**, não sua latência de execução. Foi assim que a [[wiki/entities/shopify]] descobriu que o gargalo de escalabilidade estava em código legado do checkout, não nas queries de reserva de estoque que pareciam ser o problema. Ver [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]].

## Key Sources

- [[sources/banco-de-dados]]
- [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]] — instrumentação por tempo de conexão segurada, não latência de query
