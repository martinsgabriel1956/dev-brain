---
type: source
title: "Migrations e Schema Evolution"
aliases: ["migrations", "schema evolution", "flyway", "prisma migrate", "zero downtime migration", "ddl lock"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/migrations-schema-evolution.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [migrations, schema-evolution, flyway, prisma-migrate, zero-downtime, ddl-lock, expand-contract, database]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Migrations são código — versionadas, revisadas, testadas. Ferramentas: Flyway (SQL puro, multi-DB), Prisma Migrate (DX TypeScript), Alembic (Python/SQLAlchemy). DDL sem lock: `ADD COLUMN NULL` é safe; `ADD COLUMN NOT NULL` sem default é lock; `DROP COLUMN` após remover referências é safe. Expand-Contract para mudanças breaking. Testar migrations com banco real em CI (Testcontainers).

## Key Claims

**Claim:** `ADD COLUMN NOT NULL` sem default causa lock de tabela em PostgreSQL — é a operação mais perigosa em tabelas grandes.
**Evidence:** PostgreSQL reescreve a tabela inteira ao adicionar coluna NOT NULL sem default. Em tabela de 100M rows: lock de minutos. Safe alternative: `ADD COLUMN NULL` (instantâneo), backfill em lotes pequenos, `ALTER COLUMN SET NOT NULL` após 100% preenchido (PostgreSQL 12+ checa constraint sem reescrita se não há NULLs).
**Confidence:** alta

**Claim:** Migrations devem ser testadas com banco real em CI — SQLite não emula PostgreSQL com fidelidade.
**Evidence:** SQLite: sem tipos de dados reais (JSONB, UUID, ARRAY), sem constraints avançadas, sem locks de DDL. Migration que passa em SQLite pode falhar em PostgreSQL prod com erro de tipo ou constraint. Testcontainers: sobe PostgreSQL real em Docker no CI, aplica todas as migrations, roda testes. Zero falso positivo.
**Confidence:** alta

**Claim:** Migrations nunca devem ser editadas após merge — criar nova migration para corrigir, não amend.
**Evidence:** Flyway e Liquibase verificam checksum das migrations já aplicadas. Se editada após aplicar em produção: checksum mismatch → deploy falha com erro. Convenção: migration é append-only. Bug na migration anterior → nova migration que corrige o estado. Git history como auditoria.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/schema-migration]]
- [[concepts/expand-contract]]
- [[concepts/ddl-lock]]
- [[entities/flyway]]
- [[entities/prisma-migrate]]
- [[concepts/zero-downtime]]
- [[concepts/testcontainers]]

## Open Questions

- Migrations em multi-tenant com schema-per-tenant — como aplicar migrations para 1000 schemas em paralelo sem impacto?
- Rollback de migration que apagou dados — como lidar com rollback impossível sem backup point-in-time?

## Fontes Relacionadas

- [[wiki/sources/database-migrations-sql-cru-vs-orm-drizzle]] — ângulo complementar: por que migrations manuais via SSH são consideradas errado (auditabilidade/reprodutibilidade), demonstração prática de migrate up/down com SQL cru e com Drizzle ORM. Não contradiz as claims desta página, mas foca em processo/versionamento em vez de mecânica de lock de DDL.
