---
type: source
title: "Agentes em Produção — Pilot-to-Production Gap"
aliases: ["agentes producao", "pilot production gap"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/agentes-em-producao.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [agentes, producao, state-management, governanca, auditabilidade, circuit-breaker, scaling, llmops]
skill: tech-mentor-ai
status: stable
---

## TL;DR

Pilotos de agentes funcionam. Produção quebra em 3 pontos: integração com sistemas legados (APIs internas sem docs), state management (sessões longas não cabem no contexto), e governança (auditoria, rollback, controle de custo). O gap é infra, não IA.

## Key Claims

**Claim:** Os 3 obstáculos reais de produção são infra, não modelo.
**Evidence:** (1) Legacy integration: APIs internas sem OpenAPI spec, retornam HTML de erro em vez de JSON, sem idempotência. (2) State externalizado: agentes long-running precisam de checkpointing — contexto não sobrevive crash. (3) Governança: quem aprovou essa ação? qual prompt foi usado? como reverter?
**Confidence:** alta

**Claim:** Circuit Breaker para tool calls é obrigatório em produção.
**Evidence:** Tool de API externa down → agente fica em retry loop, consome tokens, acumula custo. Circuit Breaker: após N falhas consecutivas, abre o circuito por X segundos e retorna erro controlado imediatamente.
**Confidence:** alta

**Claim:** Agentes escalam horizontalmente, mas state precisa ser externalizado.
**Evidence:** Sessão de agente com estado em memória = não escala. Padrão: Redis para working memory de curta duração, PostgreSQL para histórico persistente, fila (SQS/RabbitMQ) para tasks assíncronas.
**Confidence:** alta

**Claim:** Self-Healing IT Ops Agents têm ROI mensurável.
**Evidence:** Padrão: agente monitora alertas, diagnóstica com tools (kubectl, logs, métricas), tenta auto-remediação, escala para humano se falhar. Casos reais: redução de 60–70% em tickets de L1 em empresas que implementaram.
**Confidence:** média

**Claim:** Métricas de ROI para aprovação executiva: custo por tarefa, taxa de resolução sem humano, MTTR.
**Evidence:** Cost per task = (tokens × preço + infra) / tasks completadas. Taxa de resolução automática é o KPI principal. MTTR (Mean Time to Resolve) mede o valor em incidents.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/circuit-breaker]]
- [[concepts/agent-state-management]]
- [[concepts/llmops]]
- [[concepts/checkpointing-agents]]

## Open Questions

- Como auditar decisões de agente que envolvem dados sensíveis sem logar o conteúdo completo?
- Qual o critério de escalamento para humano — número de tentativas, tipo de erro, ou custo acumulado?
