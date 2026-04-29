---
type: source
title: "Idempotência"
aliases: ["idempotency", "idempotency key", "compare and swap", "deduplicacao"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 0
tags: [idempotencia, idempotency-key, retry, cas, mensageria, financeiro, resiliencia]
skill: tech-mentor-backend
status: draft
source_file: /home/nemomartins/Documentos/new/dev-study/raw/idempotencia.md
source_url:
author:
date_published:
date_ingested: 2026-04-23
---

# Idempotência

## TL;DR

Idempotência é a propriedade de operações que produzem o mesmo resultado independente de quantas vezes são executadas. É o pré-requisito para retry seguro. Implementada via: Idempotency Key (cliente gera UUID, servidor deduplicar via Redis), ON CONFLICT DO NOTHING no banco, Compare-and-Swap (CAS) para estado concurrent, e at-least-once delivery com deduplicação no consumer.

## Key Claims

| Claim | Evidência |
|---|---|
| Cliente deve gerar e persistir a idempotency key ANTES de enviar o request | Se o request falhar, o mesmo key é reutilizado no retry |
| Redis armazena o resultado por 24h — retorna cacheado sem reprocessar | TTL adequado para janela de retry realista |
| Idempotency Key financeira deve ser determinística por intenção (orderId, não requestId) | `payment-${orderId}` em vez de UUID aleatório |
| Compare-and-Swap (CAS): update WHERE version = expected — falha se outro processo atualizou | Optimistic locking sem lock real |
| At-least-once delivery em mensageria exige consumer idempotente | Kafka não garante exactly-once por padrão |

## Conceitos

- [[concepts/idempotencia]] — já existe no index
- [[concepts/retry-backoff]] — retry só é seguro com idempotência
- [[concepts/distributed-lock]] — lock por idempotency key para race condition
- [[concepts/outbox-pattern]] — garante publicação idempotente

## Key Sources

_Este é o documento primário._
