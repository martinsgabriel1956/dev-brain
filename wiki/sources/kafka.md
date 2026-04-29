---
type: source
title: "Apache Kafka"
aliases: ["kafka", "topics partitions", "consumer groups", "kafka producer", "kafka consumer"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/kafka.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [kafka, topics, partitions, consumer-groups, replication, isr, acks, schema-registry, dlq, rebalance, kafkajs]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Kafka é um log distribuído de eventos — persiste e permite replay. Partição é a unidade de paralelismo e ordenação. Partition Key garante ordenação por entidade. Consumer Groups compartilham partições (cada partição = 1 consumer por grupo). Configurações críticas: `acks=all`, `enable.idempotence=true`, `auto.offset.reset=earliest`.

## Key Claims

**Claim:** Partition Key garante ordenação por entidade — todos os eventos de order#123 na mesma partição.
**Evidence:** Sem partition key: distribuição round-robin, eventos da mesma order em partições diferentes = sem ordem. Com `key: order.id`: hash da key determina a partição, garantindo que todos os eventos do mesmo pedido cheguem em ordem ao mesmo consumer.
**Confidence:** alta

**Claim:** Paralelismo máximo = número de partições — não adianta mais consumers que partições.
**Evidence:** Consumer Group com 3 consumers e 2 partições: um consumer fica ocioso. Aumentar partições permite mais paralelismo. Trade-off: muitas partições aumentam overhead de rebalance e latência de liderança.
**Confidence:** alta

**Claim:** Kafka vence RabbitMQ em: throughput (milhões/s), replay, audit log, múltiplos consumer groups independentes.
**Evidence:** RabbitMQ vence em: roteamento complexo (exchanges), latência sub-milissegundo, simplicidade operacional. Kafka: cada consumer group lê o mesmo tópico independentemente — broadcast nativo. RabbitMQ: mensagem consumida é removida.
**Confidence:** alta

**Claim:** `acks=all` + `enable.idempotence=true` é a configuração de produtor mais segura para dados críticos.
**Evidence:** `acks=1`: ack apenas do líder. Réplicas podem perder a mensagem se o líder cair antes de replicar. `acks=all`: ack de todos os ISR. `enable.idempotence=true`: sequência numérica previne duplicatas em retry.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/kafka]]
- [[concepts/partitions-kafka]]
- [[concepts/consumer-groups]]
- [[concepts/isr-kafka]]
- [[concepts/schema-registry]]
- [[concepts/dlq]]

## Open Questions

- Kafka KRaft (sem ZooKeeper) está GA — quando migrar clusters existentes? Quais são os riscos?
- Partition rebalancing com CooperativeStickyAssignor vs EagerRebalanceAssignor — qual usar em produção?
