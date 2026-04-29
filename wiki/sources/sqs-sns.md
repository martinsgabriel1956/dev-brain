---
type: source
title: "SQS e SNS (AWS)"
aliases: ["sqs", "sns", "aws sqs", "aws sns", "sqs fifo", "fanout aws"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/sqs-sns.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [sqs, sns, aws, fifo, fanout, visibility-timeout, dlq, serverless, messaging]
skill: tech-mentor-backend
status: stable
---

## TL;DR

SQS é uma fila gerenciada AWS (zero operação). Standard: alta throughput, ordenação best-effort. FIFO: ordering garantido por MessageGroupId, deduplicação nativa (5 min window), limitado a 3k msg/s (com batching). SNS + SQS = fanout: SNS distribui para N filas SQS independentes. Visibility Timeout é o mecanismo central de at-least-once. Sem replay — mensagem consumida é deletada.

## Key Claims

**Claim:** Visibility Timeout é o mecanismo de at-least-once do SQS — não é ACK explícito.
**Evidence:** Consumer recebe mensagem; ela fica "invisível" por `VisibilityTimeout` (default 30s). Se consumer não deletar antes do timeout, a mensagem reaparece. MaxReceiveCount define quantas tentativas antes de ir para DLQ. Diferente de Kafka/RabbitMQ que têm ACK explícito.
**Confidence:** alta

**Claim:** SNS + múltiplas SQS filas = fanout pattern AWS nativo — substitui exchanges Fanout do RabbitMQ.
**Evidence:** SNS topic recebe a mensagem. Subscriptions entregam para N SQS filas independentemente. Cada serviço tem sua própria fila; processa no seu ritmo. Suporta filter policies para entregar apenas subsets de mensagens para cada subscriber.
**Confidence:** alta

**Claim:** SQS FIFO com MessageGroupId garante ordering mas limita throughput — escolha consciente.
**Evidence:** FIFO: 3.000 msg/s com batching (300 sem). Standard: nearly unlimited throughput. MessageGroupId é a "partition key" do SQS — mensagens com mesmo GroupId são entregues em ordem FIFO. MessageDeduplicationId previne duplicatas na janela de 5 minutos.
**Confidence:** alta

**Claim:** SQS é a escolha correta para arquiteturas serverless AWS — Kafka e RabbitMQ requerem infra.
**Evidence:** SQS integra nativamente com Lambda (event source mapping), sem polling manual. Pay-per-message. Kafka requer cluster MSK ($$$) ou self-managed. RabbitMQ requer Amazon MQ. Para workloads event-driven no ecossistema AWS, SQS/SNS elimina overhead operacional.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/sqs]]
- [[concepts/sns]]
- [[concepts/visibility-timeout]]
- [[concepts/fanout-pattern]]
- [[concepts/dlq]]
- [[concepts/fifo-queue]]
- [[entities/aws]]

## Open Questions

- SQS vs EventBridge para event-driven interno na AWS — quando cada um é mais adequado?
- Long polling vs short polling em SQS com alto volume — impacto real em custo e latência?
