---
type: source
title: "Background Jobs — BullMQ, SKIP LOCKED e Estratégias de Queue"
aliases: ["background jobs", "bullmq", "skip locked", "job queue", "workers"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/background-jobs.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [background-jobs, bullmq, skip-locked, queues, workers, retry, dead-letter, fan-out, idempotencia]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Background jobs processam tasks fora do request/response cycle. BullMQ (Redis-backed) é o padrão para Node.js — concorrência configurável, retry exponencial, dead letter, observabilidade via BullMQ Board. SKIP LOCKED é a alternativa PostgreSQL — sem dependência de Redis, com consistência transacional. Fan-out e idempotência são os padrões mais importantes.

## Key Claims

**Claim:** BullMQ é o padrão para background jobs em Node.js — Redis-backed com retry e observabilidade nativos.
**Evidence:** Retry exponencial configurável por job/queue. Dead letter automático após N tentativas. Concorrência por worker. Rate limiting nativo. BullMQ Board para monitorar jobs em tempo real. Integra com Prisma, NestJS, e frameworks comuns.
**Confidence:** alta

**Claim:** SKIP LOCKED é a alternativa sem Redis — usa PostgreSQL como queue com garantia transacional.
**Evidence:** `SELECT FOR UPDATE SKIP LOCKED` pega o próximo job disponível sem travar outros workers. Vantagem: mesmo banco, sem infra adicional, consistência transacional (job só é removido após commit). Desvantagem: escala menos que Redis em volumes altos (>10k jobs/min).
**Confidence:** alta

**Claim:** Idempotência em jobs é obrigatória para retry seguro.
**Evidence:** Worker pode processar o mesmo job múltiplas vezes em caso de falha antes do ACK. Se o job não é idempotente (envia e-mail duplicado, debita duas vezes), retry causa bugs graves. Padrão: idempotency key no job data + check antes de executar.
**Confidence:** alta

**Claim:** Fan-out (um job → múltiplos jobs filhos) é o padrão para processamento paralelo escalável.
**Evidence:** Job pai cria N jobs filhos para processamento paralelo. Resultado agregado quando todos completam (BullMQ FlowProducer). Evita jobs monolíticos que processam listas inteiras em série.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/background-jobs]]
- [[concepts/bullmq]]
- [[concepts/skip-locked]]
- [[concepts/dead-letter-queue]]
- [[concepts/idempotencia]]
- [[concepts/fan-out-pattern]]

## Open Questions

- Como monitorar job lag (tempo entre criação e processamento) sem polling constante?
- SKIP LOCKED em alta concorrência — como evitar starvation de jobs específicos (prioridade)?
