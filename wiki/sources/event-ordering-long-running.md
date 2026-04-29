---
type: source
title: "Event Ordering e Long-Running Processes"
aliases: ["event ordering", "long running process", "process manager", "saga state machine", "sequence numbers"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/event-ordering-long-running.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [event-ordering, long-running-process, process-manager, saga, state-machine, particionamento, sequence-numbers, timeout]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Event ordering: garantia de ordem só é possível dentro de uma partição (Kafka) ou para um correlation ID. Solução: particionar por entity ID (todos os eventos do pedido 123 vão para a mesma partição). Long-running processes: Process Manager com state machine persiste estado entre eventos e reage a timeouts.

## Key Claims

**Claim:** Ordering global de eventos é impossível em sistemas distribuídos — ordering por entidade é o padrão.
**Evidence:** Kafka garante ordem dentro de uma partição. Particionando por `order_id`, todos os eventos do pedido X ficam na mesma partição em ordem. Ordering entre entidades diferentes não é garantido — e na maioria dos casos não é necessário.
**Confidence:** alta

**Claim:** Process Manager com state machine resolve long-running processes que aguardam múltiplos eventos.
**Evidence:** Checkout que aguarda PaymentConfirmed + InventoryReserved + ShippingScheduled. State machine persiste o estado atual no banco. Cada evento dispara transição. Timeout explícito para casos onde um evento nunca chega.
**Confidence:** alta

**Claim:** Timeout em long-running processes é obrigatório — sem ele, processos ficam presos indefinidamente.
**Evidence:** PaymentService down por 2h = checkout aguardando para sempre. Timeout com compensação: após X minutos sem PaymentConfirmed, cancelar reserva de inventário e notificar usuário. Implementado com delayed message ou scheduled job.
**Confidence:** alta

**Claim:** Process Manager vs Saga: Process Manager tem estado explícito e correlaciona múltiplos tipos de evento; Saga é simples demais para processos com N etapas e condições.
**Evidence:** Saga funciona para fluxo linear simples. Process Manager funciona para fluxos com branches, timeouts, e correlação de eventos de diferentes tipos. Para checkout complexo: Process Manager é a escolha certa.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/event-ordering]]
- [[concepts/process-manager]]
- [[concepts/saga-pattern]]
- [[concepts/state-machine]]
- [[concepts/particionamento-kafka]]
- [[concepts/timeout-compensation]]

## Open Questions

- Como recuperar um Process Manager que ficou em estado inválido por bug na state machine?
- Sequence numbers para out-of-order events — quando é melhor usar vector clocks vs sequence simples?
