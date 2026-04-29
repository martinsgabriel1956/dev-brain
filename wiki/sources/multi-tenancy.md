---
type: source
title: "Multi-tenancy Patterns"
aliases: ["multi-tenancy", "multitenancy", "saas isolation", "tenant isolation"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 0
tags: [system-design, multi-tenancy, saas, isolamento, postgresql, rls, gdpr, migrations]
skill: tech-mentor-system-design
status: stable
source_file: /home/gabriel-martins/Documentos/dev-study/raw/multi-tenancy.md
source_url: ""
author: ""
date_published: 2026-03-29
date_ingested: 2026-04-22
---

# Multi-tenancy Patterns

## TL;DR

Três modelos de isolamento com trade-offs opostos: Shared Schema (custo mínimo, risco de leak), Schema-per-Tenant (equilíbrio, limite ~1000 schemas), DB-per-Tenant (isolamento máximo, custo alto). Decisão depende do perfil de cliente. Errar cedo = migração de meses. RLS é segunda linha de defesa, não a primeira.

## Key Claims

**Claim:** A escolha do modelo de isolamento é uma das decisões arquiteturais mais impactantes — migrar de shared schema para DB-per-tenant com milhões de registros é projeto de meses.
**Evidence:** Shared schema → schema-per-tenant requer mover dados entre schemas PostgreSQL para cada tenant ativo, coordenar com zero downtime, validar isolamento pós-migração. Não há caminho simples.
**Confidence:** alta

**Claim:** Row Level Security (PostgreSQL) é segunda linha de defesa — a primeira são testes de isolamento automatizados.
**Evidence:** RLS com `current_setting('app.current_tenant_id')` bloqueia leaks causados por bugs na aplicação. Mas RLS sozinho não substitui testes que verificam explicitamente que tenant A não acessa dados de tenant B.
**Confidence:** alta

**Claim:** Schema-per-tenant tem limite prático de ~1000 schemas performáticos no PostgreSQL.
**Evidence:** Cada schema ativo precisa de connection pool dedicado. 500 tenants × 5 conexões = 2500 conexões → PostgreSQL limite prático ~1000. Solução: PgBouncer + `search_path` dinâmico por request.
**Confidence:** alta

**Claim:** GDPR Right to Erasure é trivial em schema-per-tenant (`DROP SCHEMA CASCADE`) e complexo em shared schema (rastrear PII em todas as tabelas).
**Evidence:** Schema-per-tenant: `DROP SCHEMA tenant_x CASCADE` + S3 prefix delete. Shared schema: DELETE em cada tabela que contém PII do tenant, com risco de deixar referências órfãs.
**Confidence:** alta

**Claim:** Migrations em schema-per-tenant devem rodar em paralelo com concorrência limitada — falhas parciais deixam tenants em versões diferentes.
**Evidence:** `pLimit(5, tenants.map(t => () => migrateSchema(t.schemaName)))` — paralelo mas controlado. Rastrear versão por tenant, alertar se tenant ficou mais de X versões atrás.
**Confidence:** alta

**Claim:** Rate limiting por tenant por tier é obrigatório em shared schema — noisy neighbor afeta não só banco mas CPU, conexões e cache.
**Evidence:** Implementação via `redis.incr` com janela por minuto por tenant. Tiers free/pro/enterprise com RPM e daily limits diferentes. Header `Retry-After: 60` em 429.
**Confidence:** alta

## Concepts & Entities Touched

[[concepts/multi-tenancy]] · [[concepts/tenant-context]] · [[concepts/expand-contract]] · [[concepts/connection-pooling]] · [[concepts/database-transactions]] · [[concepts/feature-flags]]

## Open Questions

- Quando schema-per-tenant supera DB-per-tenant em compliance enterprise?
- Noisy neighbor em shared schema — `pg_stat_statements` por tenant_id é suficiente para isolar ofensores?
- TenantConfig com `dataResidency` — como rotear para instância na região certa sem aumentar latência?
