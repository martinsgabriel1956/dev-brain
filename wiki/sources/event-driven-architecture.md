---
type: source
title: "Event-Driven Architecture (EDA)"
aliases: ["eda", "event driven", "choreography", "orchestration", "temporal decoupling"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/event-driven-architecture.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [eda, event-driven, choreography, orchestration, temporal-decoupling, idempotencia, at-least-once, domain-events, integration-events]
skill: tech-mentor-backend
status: stable
---

## TL;DR

EDA desacopla produtores de consumidores via eventos — comunicação assíncrona, temporal decoupling. Dois padrões de coordenação: Choreography (cada serviço reage a eventos, sem coordenador) e Orchestration (saga orchestrator emite comandos). Idempotência no consumidor é obrigatória porque at-least-once delivery é a garantia padrão.

## Key Claims

**Claim:** EDA oferece temporal decoupling — produtor não espera o consumidor processar.
**Evidence:** OrderService publica `order.placed` e continua. PaymentService consome quando disponível. Se PaymentService estiver down, o evento fica no broker e será processado quando voltar. Isso é impossível com chamadas síncronas.
**Confidence:** alta

**Claim:** Choreography vs Orchestration — a escolha impacta observabilidade e acoplamento.
**Evidence:** Choreography: mais desacoplado, mais difícil de rastrear o fluxo completo. Orchestration: fluxo explícito no orchestrator, mais fácil de debugar, mas orchestrator vira ponto central de mudança. Para sagas complexas: orchestration. Para integrações simples: choreography.
**Confidence:** alta

**Claim:** Idempotência no consumidor é obrigatória — at-least-once delivery pode duplicar eventos.
**Evidence:** Broker garante que o evento será entregue pelo menos uma vez — pode ser entregue múltiplas vezes. Consumer deve verificar se já processou o evento antes de agir (idempotency key no banco, Redis, ou UUID do evento).
**Confidence:** alta

**Claim:** Domain Events vs Integration Events — distinção crítica para acoplamento.
**Evidence:** Domain Event: dentro do mesmo Bounded Context, in-process, síncrono. Integration Event: entre BCs via broker, assíncrono, formato estável. Misturar os dois = acoplar domínios internos ao contrato de integração externo.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/event-driven-architecture]]
- [[concepts/choreography]]
- [[concepts/orchestration]]
- [[concepts/temporal-decoupling]]
- [[concepts/idempotencia]]
- [[concepts/domain-events]]
- [[concepts/integration-events]]
- [[concepts/at-least-once-delivery]]

## Open Questions

- Como monitorar o fluxo de eventos em choreography sem um trace centralizado?
- Ordering de eventos quando múltiplos consumidores processam em paralelo — como garantir?
