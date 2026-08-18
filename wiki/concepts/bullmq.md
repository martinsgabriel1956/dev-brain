---
type: concept
title: "BullMQ"
aliases: ["Bull MQ", "Bull Queue"]
date_created: 2026-07-09
date_updated: 2026-08-14
source_count: 2
tags: [bullmq, redis, mensageria, filas, workers, nodejs, background-jobs, tech-mentor-backend]
skill: tech-mentor-backend
status: stub
---

# BullMQ

Biblioteca de filas de jobs para Node.js/Bun construída sobre **Redis**. Implementa o padrão producer → queue → worker: um processo cria (`Queue.add`) jobs numa fila, e um ou mais processos `Worker` os consomem e executam de forma assíncrona, fora do ciclo de request/response.

## Anatomia mínima

- **Producer**: instancia uma `Queue` apontando para um host/porta Redis e chama `.add(name, data, opts)` para enfileirar um job.
- **Broker**: o Redis em si — é o que persiste a fila; producer e worker precisam se conectar exatamente ao mesmo host/porta para se comunicarem.
- **Worker**: instancia um `Worker` sobre o mesmo nome de fila; processa jobs conforme chegam, sem chamada de função direta com o producer.

Producer e worker são processos independentes — param e retomam sem perder estado: um worker que reconecta continua de onde a fila estava; um producer parado não trava workers, que apenas drenam o que já foi enfileirado.

## Recursos além do básico (não demonstrados no quickstart, mas nativos da lib)

- Retry com backoff exponencial, priorização por score, scheduling (delay e cron via `repeat`), Flows (dependência entre jobs), Dead Letter Queue manual via `getFailed()`.
- Ver `references/background-jobs.md` (tech-mentor-backend) para padrões completos de DLQ, idempotência via `jobId`, graceful shutdown e observabilidade de filas com BullMQ.

## Relação com outros conceitos

- [[wiki/concepts/filas-e-workers]] — BullMQ é uma implementação concreta do padrão arquitetural de filas e workers no ecossistema Node.js
- [[wiki/concepts/mensageria]] — BullMQ opera no modelo *queue* (cada mensagem consumida por um único worker), não *stream* — comparável a RabbitMQ/SQS, diferente de Kafka
- [[wiki/concepts/fila]] — usa a estrutura FIFO como base, mas com garantias adicionais (retry, delay, persistência) fornecidas pelo Redis
- [[wiki/concepts/pub-sub]] — modelo mental oposto: em BullMQ um job é processado uma única vez por um worker; em Pub/Sub, cada assinante recebe sua própria cópia do evento

## Key sources

- [[wiki/sources/pub-sub-message-queue-bullmq-na-pratica]]
- [[wiki/sources/back-pressure-producer-consumer-filas-bounded-admission-control]] — demo de admission control com low/high watermark sobre uma fila BullMQ + Redis: o produtor pausa acima de 100 jobs e retoma abaixo de 30
