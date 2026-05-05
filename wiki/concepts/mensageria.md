---
type: concept
title: "Mensageria"
aliases: ["message broker", "queue", "stream", "eda", "event driven"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 1
tags: [mensageria, kafka, rabbitmq, sqs, queue, stream, eda, at-least-once, dlq]
skill: tech-mentor-backend
status: stub
---

# Mensageria

Comunicação assíncrona entre serviços via broker de mensagens. Resolve acoplamento síncrono, absorve picos de tráfego e isola falhas.

**Queue vs Stream:**
- **Queue (fila):** cada mensagem consumida uma vez — workers competem. Para jobs únicos (email, pagamento). Ex: RabbitMQ, SQS.
- **Stream:** cada consumer lê com seu próprio offset — replay possível. Para eventos de negócio com múltiplos consumidores. Ex: Kafka, Kinesis.

**Os três grandes:**
- **Kafka:** throughput massivo, replay, durável — operação complexa.
- **SQS:** zero ops, gerenciado, HA automático — sem replay, FIFO limitado.
- **RabbitMQ:** roteamento flexível AMQP — mais infra para operar.

**DLQ (Dead Letter Queue):** obrigatória — mensagens que falham N vezes não ficam em retry infinito.

**Garantias:** at-least-once exige consumer idempotente. Exactly-once é raro e caro.

## Key Sources

- [[sources/mensageria]]
- [[sources/design-pattern-observer]] — distinção Observer (in-process) vs Pub/Sub (broker distribuído)
