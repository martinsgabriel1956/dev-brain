---
type: concept
title: "Mensageria"
aliases: ["message broker", "queue", "stream", "eda", "event driven"]
date_created: 2026-04-23
date_updated: 2026-07-09
source_count: 4
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

**Redis Pub/Sub como notificador leve:** não é fila nem stream — mensagens não persistem, sem replay, sem consumer groups. Se o assinante não estiver conectado no momento do `PUBLISH`, a mensagem se perde. Serve bem para notificar múltiplas instâncias de um serviço (ex: propagar evento para clientes [[wiki/concepts/server-sent-events|SSE]] conectados em pods diferentes), mas não substitui Kafka/SQS/RabbitMQ quando entrega garantida importa.

**BullMQ como implementação de queue em Node.js/Bun:** producer e worker são processos independentes que só se comunicam via Redis — nunca por chamada de função direta. Ver [[wiki/concepts/bullmq]] e [[wiki/concepts/filas-e-workers]].

## Key Sources

- [[sources/mensageria]]
- [[sources/design-pattern-observer]] — distinção Observer (in-process) vs Pub/Sub (broker distribuído)
- [[wiki/sources/server-sent-events-sse-tempo-real]] — Redis Pub/Sub como notificador entre microsserviços, sem persistência nem replay
- [[wiki/sources/updates-tempo-real-polling-sse-websocket]] — mitigação da perda de mensagem via tabela de pendentes, quando o assinante Redis Pub/Sub está offline
- [[wiki/sources/pub-sub-message-queue-bullmq-na-pratica]] — distinção prática Pub/Sub vs queue e quickstart de BullMQ sobre Redis
