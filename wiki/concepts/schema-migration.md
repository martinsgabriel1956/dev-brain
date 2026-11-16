---
type: concept
title: "Schema Migration"
aliases: []
date_created: 2026-09-22
date_updated: 2026-11-16
source_count: 4
tags: [schema-migration]
skill: tech-mentor-backend
status: stub
---

# Schema Migration

Stub criado durante sweep de lint (links quebrados) a partir de referências em 2 página(s) da wiki — conteúdo completo pendente de ingest dedicado.

## Contexto das citações

- Em [[wiki/sources/expand-contract]]: [[wiki/concepts/schema-migration]]
- Em [[wiki/sources/migrations-schema-evolution]]: [[wiki/concepts/schema-migration]]

## Pendências

Página não nasceu de um ingest próprio; TL;DR acima é reconstruído apenas a partir do texto das páginas que a citam. Precisa de fonte dedicada para virar `draft`/`stable`.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: arquivos numerados à mão (`00_`, `01_`, `02_`) para respeitar a dependência da pivô; `knex migrate:latest`; e as tabelas `knex_migrations` e `knex_migrations_lock`.

## Key sources

- [[wiki/sources/expand-contract]]
- [[wiki/sources/migrations-schema-evolution]]
- [[wiki/sources/migrations-flyway-spring-boot-versionamento-de-banco]] — demo prático de migrations versionadas com [[wiki/entities/flyway]] (stub segue pendente de conteúdo próprio)
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: ordem por prefixo numérico; tabelas de controle do Knex
