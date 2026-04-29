---
type: source
title: "MongoDB — Aggregation Pipeline, Change Streams e Schema Validation"
aliases: ["mongodb", "aggregation pipeline", "change streams", "schema validation", "embed vs reference"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mongodb.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [mongodb, aggregation-pipeline, change-streams, schema-validation, embed-vs-reference, indexes, faceted-search, sharding]
skill: tech-mentor-data
status: stable
---

## TL;DR

MongoDB é ideal para documentos hierárquicos com schema variável. Embed vs Reference: embed para dados lidos juntos e raramente atualizados separadamente; reference para N:M ou dados muito grandes. Aggregation Pipeline é o SQL dos documentos. Change Streams substituem polling para reatividade. Schema Validation garante integridade no banco.

## Key Claims

**Claim:** Embed vs Reference — a decisão define performance de todo o modelo de dados.
**Evidence:** Embed: 1 query para buscar o documento completo. Reference: $lookup (JOIN) necessário. Embed quando: dados lidos juntos 90%+ do tempo, cardinalidade limitada (max ~100 items). Reference quando: subdocumento atualizado independentemente, ou unbounded array (risco de documento > 16MB).
**Confidence:** alta

**Claim:** Aggregation Pipeline é mais poderoso que SQL para processamento de documentos hierárquicos.
**Evidence:** `$unwind` + `$group` + `$project` + `$lookup` permitem transformações que SQL exigiria múltiplos JOINs e subqueries. Faceted search ($facet) retorna múltiplas agregações em uma única query — ideal para filtros de e-commerce.
**Confidence:** alta

**Claim:** Change Streams substituem polling para detecção de mudanças em tempo real.
**Evidence:** `collection.watch()` abre um cursor que recebe eventos INSERT/UPDATE/DELETE em tempo real. Requer replica set (mesmo com 1 nó em dev via `rs.initiate()`). Resume token permite reconectar sem perder eventos.
**Confidence:** alta

**Claim:** MongoDB tem trade-offs reais vs PostgreSQL — não é escolha neutra.
**Evidence:** PostgreSQL vence em: JOINs complexos, analytics, full-text search, ACID multi-documento (mais robusto). MongoDB vence em: documentos hierárquicos, schema flexível, sharding horizontal nativo, write-heavy workloads com documentos grandes.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/mongodb]]
- [[concepts/embed-vs-reference]]
- [[concepts/aggregation-pipeline]]
- [[concepts/change-streams]]
- [[concepts/schema-validation]]
- [[concepts/faceted-search]]

## Open Questions

- MongoDB com Prisma — Prisma ORM suporta MongoDB mas sem transaction nativo. Quais operações são safe sem transação?
- Change Streams com resume token — como armazenar o token de forma que não se perca entre deploys?
