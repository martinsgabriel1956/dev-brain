---
type: source
title: "CDC — Change Data Capture com Debezium"
aliases: ["cdc", "change data capture", "debezium", "logical replication", "wal tailing"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/cdc-debezium.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [cdc, debezium, change-data-capture, wal, logical-replication, kafka, outbox, schema-registry]
skill: tech-mentor-backend
status: stable
---

## TL;DR

CDC (Change Data Capture) captura toda alteração no banco em tempo real via WAL (Write-Ahead Log). Debezium: conector Kafka Connect que lê o WAL do PostgreSQL e publica eventos de INSERT/UPDATE/DELETE em tópicos Kafka. Casos de uso: sincronização entre sistemas, Outbox Pattern robusto, cache invalidation, audit log. Requer `wal_level = logical` no PostgreSQL.

## Key Claims

**Claim:** Debezium lê o WAL diretamente — captura 100% das mudanças sem impacto nas queries da aplicação.
**Evidence:** WAL é o log transacional do PostgreSQL. Debezium usa replication slot para ler o WAL sem polling. Cada INSERT/UPDATE/DELETE vira um evento com before/after state. Sem triggers, sem polling de tabelas, sem overhead de queries extras. Latência de milissegundos do commit ao Kafka.
**Confidence:** alta

**Claim:** CDC + Outbox Pattern é a combinação mais robusta para transactional messaging — sem polling.
**Evidence:** Outbox polling: query periódica `WHERE status = 'pending'` — latência configurável, overhead de lock. CDC + Outbox: Debezium lê INSERT na tabela outbox diretamente do WAL. Zero polling, latência sub-segundo, sem lock na tabela. Debezium marca LSN (Log Sequence Number) como processado — at-least-once garantido.
**Confidence:** alta

**Claim:** Formato de evento do Debezium inclui before/after state — audit log completo por padrão.
**Evidence:** Evento: `{ op: "u", before: { status: "pending" }, after: { status: "shipped" }, source: { table: "orders", lsn: 12345 } }`. `op`: c (create), u (update), d (delete), r (read/snapshot). Antes e depois do estado permitem event sourcing retroativo e auditoria completa.
**Confidence:** alta

**Claim:** Schema Registry com Avro é essencial em CDC de produção — mudanças de schema no banco podem quebrar consumers.
**Evidence:** Sem Schema Registry: ADD COLUMN no PostgreSQL → evento Debezium muda formato → consumers Kafka falham. Com Schema Registry: novo schema é registrado, compatibilidade BACKWARD verificada, consumers antigos ignoram campo novo. Debezium integra nativamente com Confluent Schema Registry.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/cdc]]
- [[entities/debezium]]
- [[concepts/wal]]
- [[concepts/outbox-pattern]]
- [[concepts/schema-registry]]
- [[concepts/logical-replication]]
- [[entities/kafka]]

## Open Questions

- Debezium em RDS PostgreSQL — limitações do replication slot gerenciado pela AWS?
- Debezium com múltiplas versões de schema no mesmo tópico — como fazer upcasting de eventos antigos?
