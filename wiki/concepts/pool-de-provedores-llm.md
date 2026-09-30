---
type: concept
title: "Pool de Provedores de LLM (Provider Routing)"
aliases: ["provider pool","provider routing","pool de provedores"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [tech-mentor-ai, openrouter, fallback, provider-routing, resiliencia]
skill: tech-mentor-ai
status: draft
---

# Pool de Provedores de LLM

Conjunto restrito (≥3 segundo [[wiki/sources/openrouter-como-profissional-provedores-quantizacao-retencao-fallback-ronald-hulk]]) de provedores aprovados para um modelo, fixado no payload da [[wiki/entities/openrouter]] para que o fallback ocorra **só entre opções já validadas**.

## Por que ≥3

Com um provedor só, perde-se o fallback; com a API crua, o fallback vai a qualquer provedor (inclusive pior quantização ou com retenção de dados). O pool dá margem de [[wiki/concepts/failover]] sem abrir mão da política.

## Campos do payload (`provider`) [external: https://openrouter.ai/docs/features/provider-routing]

- `only` — provedores permitidos; `order` — ordem de tentativa
- `allow_fallbacks` (padrão `true`)
- `quantizations` — filtra por nível
- `max_price` — preço máximo
- `preferred_min_throughput` / `preferred_max_latency` — preferências com percentil (p50/p75/p90/p99); são preferências, não filtros rígidos
- `data_collection: "deny"` e `zdr: true` — política de dados (ver [[wiki/concepts/zero-data-retention]])

## Processo recomendado

Tabela de [[wiki/concepts/criterios-de-selecao-de-provedor-llm]] → ADR/PR → implementação com critérios explícitos.

Relacionados: [[wiki/concepts/ai-gateway-llm-router]], [[wiki/concepts/graceful-degradation]].

## Key sources

- [[wiki/sources/openrouter-como-profissional-provedores-quantizacao-retencao-fallback-ronald-hulk]]
