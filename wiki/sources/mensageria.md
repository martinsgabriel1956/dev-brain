---
type: source
title: "Mensageria"
aliases: ["message broker", "kafka", "rabbitmq", "sqs", "queue", "stream", "eda"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 0
tags: [mensageria, kafka, rabbitmq, sqs, queue, stream, eda, outbox-pattern, dlq, at-least-once]
skill: tech-mentor-backend
status: draft
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mensageria.md
source_url:
author:
date_published:
date_ingested: 2026-04-23
---

# Mensageria

## TL;DR

Mensageria resolve o acoplamento síncrono entre serviços com comunicação assíncrona via broker. Distinção fundamental: Queue (cada mensagem consumida uma vez, competição entre workers) vs Stream (cada consumer lê seu próprio offset, replay possível). Os três grandes: Kafka (throughput massivo, replay, durável), SQS (zero ops, gerenciado), RabbitMQ (roteamento flexível, AMQP). Outbox Pattern garante que eventos são publicados atomicamente com a escrita no banco.

## Key Claims

| Claim | Evidência |
|---|---|
| Queue: uma mensagem, um consumer (competição) — ex: email, pagamento | RabbitMQ, SQS |
| Stream: todos os consumers leem com seu offset — replay possível | Kafka, Kinesis |
| Kafka tem operação complexa e custo alto em cluster pequeno | SQS é melhor para baixo volume sem equipe de operações |
| DLQ (Dead Letter Queue) é obrigatória — mensagens que falham N vezes | Sem DLQ, mensagem fica em retry infinito |
| Outbox Pattern: evento escrito na mesma transação do banco, publicado por CDC | Garante at-least-once sem 2PC |
| At-least-once exige consumer idempotente | Kafka não garante exactly-once por padrão |

## Conceitos

- [[concepts/mensageria]] — fundamentos e escolha de broker
- [[concepts/outbox-pattern]] — publicação atômica com escrita no banco
- [[concepts/idempotencia]] — pré-requisito para at-least-once seguro
- [[concepts/saga-pattern]] — orquestração/coreografia via mensageria
- [[concepts/event-sourcing]] — streams como fonte de verdade

## Key Sources

_Este é o documento primário._
