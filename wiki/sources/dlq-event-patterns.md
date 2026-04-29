---
type: source
title: "DLQ, At-Least-Once vs Exactly-Once e Event Versioning"
aliases: ["dlq", "dead letter queue", "at-least-once", "exactly-once", "event versioning", "poison pill", "idempotency"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/dlq-event-patterns.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [dlq, dead-letter-queue, at-least-once, exactly-once, idempotency, event-versioning, kafka, poison-pill]
skill: tech-mentor-backend
status: stable
---

## TL;DR

DLQ captura mensagens que falham repetidamente — sem DLQ, poison pills bloqueiam o consumer group inteiro. At-least-once + idempotência é o padrão correto: exactly-once no Kafka (transações) tem overhead alto e raramente vale. Event Versioning: Tolerant Reader absorve campos desconhecidos; versionamento explícito (`v2/`) para mudanças breaking; Upcasting migra eventos antigos em runtime.

## Key Claims

**Claim:** DLQ é obrigatório — sem ela, uma mensagem poison pill paralisa o consumer group.
**Evidence:** Consumer tenta processar mensagem malformada, falha, volta para fila, tenta de novo — loop infinito. Com DLQ configurada (maxReceiveCount no SQS, max.poll.interval.ms no Kafka), após N tentativas a mensagem vai para o tópico de DLQ. Consumer group avança; operações inspecionam e reprocessam a DLQ manualmente.
**Confidence:** alta

**Claim:** At-least-once + idempotência é o padrão correto — exactly-once tem overhead que raramente justifica.
**Evidence:** Exactly-once no Kafka requer transações (producer + consumer em transaction scope), reduz throughput em 10-30%. At-least-once: mensagem pode ser entregue mais de uma vez em retry. Com `idempotencyKey` ou `UNIQUE(event_id)` no banco, duplicatas são absorvidas silenciosamente. Para 99% dos casos, at-least-once + idempotência é equivalente a exactly-once.
**Confidence:** alta

**Claim:** Tolerant Reader é a estratégia de event versioning mais resiliente — ignore o que não conhece.
**Evidence:** Consumer que falha ao receber campos desconhecidos é frágil. Tolerant Reader: deserializar apenas os campos que o consumer conhece, ignorar o resto. Producer pode adicionar campos sem quebrar consumers antigos. Padrão compatível com backward compatibility.
**Confidence:** alta

**Claim:** Upcasting migra eventos antigos para versão nova em runtime — sem re-escrever o event store.
**Evidence:** EventStore armazena `{ version: 1, orderId: "123" }`. Novo consumer espera `{ version: 2, orderId: "123", currency: "BRL" }`. Upcaster intercepta eventos v1 no pipeline de deserialização e transforma para v2 (adicionando `currency: "BRL"` como default). Event store inalterado.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/dlq]]
- [[concepts/at-least-once]]
- [[concepts/exactly-once]]
- [[concepts/idempotency]]
- [[concepts/event-versioning]]
- [[concepts/tolerant-reader]]
- [[concepts/upcasting]]
- [[concepts/poison-pill]]

## Open Questions

- Reprocessamento automático de DLQ vs manual — como decidir quais classes de erro são auto-retriable?
- Exactly-once no Kafka em produção — em quais cenários reais o overhead de transações é justificável?
