---
type: source
title: "RabbitMQ"
aliases: ["rabbitmq", "amqp", "exchange", "fanout", "topic exchange", "dlx", "quorum queues"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/rabbitmq.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [rabbitmq, amqp, exchange, fanout, topic, dlx, quorum-queues, messaging, task-queue]
skill: tech-mentor-backend
status: stable
---

## TL;DR

RabbitMQ é um message broker AMQP com roteamento flexível via Exchanges (Direct, Fanout, Topic, Headers). Vence Kafka em: latência sub-milissegundo, roteamento complexo, task queues e RPC assíncrono. Perde em: replay, múltiplos consumer groups independentes e throughput (cap ~100k msg/s vs milhões no Kafka). Quorum Queues para HA. DLX (Dead Letter Exchange) para mensagens que falham ou expiram.

## Key Claims

**Claim:** Exchange é o diferencial do RabbitMQ — roteamento flexível sem lógica no producer.
**Evidence:** Direct (routing key exata), Fanout (broadcast para todas as filas), Topic (wildcards `*` e `#`), Headers (por headers AMQP). Producer publica para Exchange; bindings determinam para quais filas vai. Kafka só tem topic + partition key — sem roteamento por conteúdo.
**Confidence:** alta

**Claim:** Mensagem consumida no RabbitMQ é removida — sem replay nativo.
**Evidence:** Semântica de fila: consumer recebe, faz ack, mensagem é deletada. Para múltiplos consumidores independentes receberem a mesma mensagem, é preciso múltiplas filas com bindings no Fanout Exchange. Kafka preserva a mensagem no log e permite replay desde qualquer offset.
**Confidence:** alta

**Claim:** Quorum Queues substituem Classic Mirrored Queues para HA — Raft-based, mais confiável.
**Evidence:** Classic Mirrored Queues tinham split-brain em partições de rede. Quorum Queues usam Raft consensus: maioria (quorum) de nós deve confirmar antes do ack ao producer. Mais lento que classic, mais seguro. Recomendado para cargas de produção desde RabbitMQ 3.8+.
**Confidence:** alta

**Claim:** DLX (Dead Letter Exchange) é o padrão correto para tratamento de falhas no RabbitMQ.
**Evidence:** Mensagem vai para DLX quando: ack é negado (nack + requeue=false), TTL expira, ou fila atinge max-length. DLX roteia para uma fila de dead letters onde pode ser inspecionada, reprocessada ou alertar. Alternativa ao DLQ manual que exige lógica no consumer.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/rabbitmq]]
- [[concepts/amqp]]
- [[concepts/exchange-types]]
- [[concepts/dlq]]
- [[concepts/quorum-queues]]
- [[concepts/task-queue]]

## Open Questions

- Quorum Queues em clusters grandes (5+ nós) — qual o impacto de latência vs Classic Queues em produção?
- RabbitMQ Streams (novo em 3.9+) — quando preferir sobre JetStream ou Kafka para casos de replay?
