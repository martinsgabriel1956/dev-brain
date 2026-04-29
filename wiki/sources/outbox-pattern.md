---
type: source
title: "Outbox Pattern"
aliases: ["outbox", "outbox pattern", "transactional outbox", "inbox pattern", "dual-write"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/outbox-pattern.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [outbox, transactional-messaging, cdc, debezium, dual-write, consistency, inbox]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Outbox Pattern resolve o problema de dual-write: salvar no banco E publicar no broker na mesma operação de forma confiável. Solução: gravar o evento na tabela `outbox_events` dentro da mesma transação do banco. Um poller/relay lê e publica no broker, marcando como processado. CDC com Debezium é a abordagem mais robusta — reage ao WAL sem polling. Inbox Pattern é o complementar para idempotência no consumer.

## Key Claims

**Claim:** Dual-write sem Outbox cria janela de inconsistência — salvar no banco e publicar no broker não é atômico.
**Evidence:** Cenário 1: banco commitado, broker fora do ar → evento perdido. Cenário 2: broker publicado, banco rollback → evento fantasma. Sem transação que englobe ambos, qualquer falha entre os dois steps gera estado inconsistente. Outbox resolve usando o banco como intermediário confiável.
**Confidence:** alta

**Claim:** Tabela outbox dentro da mesma transação garante atomicidade — evento só existe se a operação de negócio persistiu.
**Evidence:** `BEGIN TRANSACTION; INSERT INTO orders ...; INSERT INTO outbox_events (event_type, aggregate_id, payload, status) VALUES (...); COMMIT;`. Se o commit falhar, nenhum evento é gerado. O relay lê a tabela separadamente e publica no broker, atualizando status para "processed".
**Confidence:** alta

**Claim:** CDC com Debezium é mais robusto que polling — lê o WAL do PostgreSQL sem overhead de query.
**Evidence:** Polling: query periódica `WHERE status = 'pending'` — latência de até N segundos, overhead de lock. Debezium: conecta ao WAL do PostgreSQL, captura cada INSERT na tabela outbox em tempo real, publica no Kafka. Sem polling, sem lock, latência de milissegundos.
**Confidence:** alta

**Claim:** Inbox Pattern é o complementar do Outbox — garante idempotência no consumer side.
**Evidence:** Consumer recebe o evento e tenta inserir em `inbox_events (event_id, processed_at)` com UNIQUE constraint. Se o event_id já existe (retry), a inserção falha silenciosamente — evento ignorado. Garante que o mesmo evento não seja processado duas vezes mesmo com at-least-once delivery.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/outbox-pattern]]
- [[concepts/transactional-messaging]]
- [[concepts/cdc]]
- [[concepts/debezium]]
- [[concepts/inbox-pattern]]
- [[concepts/idempotency]]
- [[concepts/dual-write]]

## Open Questions

- Outbox com múltiplos brokers (Kafka + SQS) — como o relay lida com entrega para múltiplos destinos?
- Debezium em RDS PostgreSQL vs self-managed — há limitações no WAL level para CDC no managed DB?
