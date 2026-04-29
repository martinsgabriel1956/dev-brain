---
type: source
title: "Saga Pattern"
aliases: ["saga", "saga pattern", "choreography", "orchestration", "distributed transactions", "compensating transactions"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/saga-pattern.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [saga, distributed-transactions, choreography, orchestration, compensation, temporal, event-driven]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Saga é o padrão para transações distribuídas sem 2PC. Duas abordagens: Choreography (cada serviço reage a eventos, sem coordenador — simples mas difícil de debugar) e Orchestration (orchestrator central coordena a saga — visível mas moderadamente acoplado). Compensações são obrigatórias e devem ser idempotentes. Temporal resolve sagas longas com durable execution.

## Key Claims

**Claim:** Choreography escala bem para fluxos simples; Orchestration é melhor para fluxos complexos com muitas compensações.
**Evidence:** Choreography: cada serviço emite evento de sucesso ou falha; outros reagem. Sem coordenador central. Difícil rastrear estado global — precisa de distributed tracing. Orchestration: orchestrator conhece o estado completo da saga, facilita debugging e auditoria. Trade-off: orchestrator vira SPOF se não for resiliente.
**Confidence:** alta

**Claim:** Compensações em Sagas devem ser idempotentes — a mesma compensação pode ser executada N vezes.
**Evidence:** Em at-least-once delivery, uma compensação pode ser acionada mais de uma vez (retry após falha do broker). `cancelOrder(orderId)` deve ser safe de chamar múltiplas vezes: se já cancelado, retorna sem erro. Sem idempotência, dupla compensação pode gerar estado inválido (ex: reembolsar duas vezes).
**Confidence:** alta

**Claim:** Temporal é a melhor solução para Sagas longas (horas/dias) com múltiplos passos e retries.
**Evidence:** Temporal persiste estado da saga no banco interno. Workflow define steps em código Go/TypeScript. Retries configuráveis por Activity. Sem precisar de state machine explícita no código da aplicação. Alternativas: Inngest (serverless), AWS Step Functions (AWS-locked).
**Confidence:** alta

**Claim:** Sagas travadas precisam de DLQ + alertas — sem isso, o sistema fica em estado parcialmente aplicado indefinidamente.
**Evidence:** Falha permanente em um step (serviço down por dias) sem DLQ = saga nunca compensa. Estado do pedido fica "pagamento processado, estoque não reservado" para sempre. DLQ captura a mensagem após maxReceiveCount, alerta equipe, permite reprocessamento manual ou compensação forçada.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/saga-pattern]]
- [[concepts/choreography]]
- [[concepts/orchestration]]
- [[concepts/compensating-transaction]]
- [[concepts/idempotency]]
- [[entities/temporal]]
- [[concepts/distributed-transactions]]

## Open Questions

- Saga com Temporal vs Step Functions em produção — qual tem melhor DX e menor custo operacional?
- Como fazer rollback parcial em Orchestration quando compensation também falha (double failure)?
