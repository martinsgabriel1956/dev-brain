---
type: source
title: "LLMOps & Observabilidade"
aliases: ["llmops", "observabilidade llm", "langfuse", "langsmith", "prompt versioning"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/llmops-observabilidade.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [llmops, observabilidade, traces, spans, ttft, cost-attribution, langfuse, langsmith, arize, helicone, opentelemetry, prompt-versioning, slo, evals-online, prompt-drift, session-replay]
skill: tech-mentor-ai
status: stable
---

## TL;DR

LLMOps é observabilidade adaptada para LLMs: traces hierárquicos (trace→span por LLM call), métricas específicas (TTFT, TPS, tokens, qualidade), cost attribution por tenant/feature, evals online em tráfego real. Langfuse é o padrão open source. SLOs para LLM devem incluir latência (TTFT < 500ms p95) e qualidade (score > 0.75).

## Key Claims

**Claim:** Traces LLM têm estrutura hierárquica diferente de HTTP — spans aninhados com custo e qualidade.
**Evidence:** Trace agrupa todo o request do usuário. Spans capturam cada LLM call, tool call, retrieval. Métricas por span: TTFT, tokens input/output, custo em USD, score de qualidade. Visualização em árvore é essencial para debugging de agentes.
**Confidence:** alta

**Claim:** Langfuse é o padrão open source para LLM tracing — self-hostável, zero lock-in.
**Evidence:** SDK para Python/JS, LangChain, LlamaIndex. Prompt management com versioning linkado a traces. Cost tracking por modelo/usuário/feature. Evals online com score automático. Exporta para Prometheus/Grafana.
**Confidence:** alta

**Claim:** Cost Attribution granular por tenant/feature é obrigatório para produtos multi-tenant.
**Evidence:** Sem attribution, impossível saber qual feature ou cliente está custando mais. Padrão: tag cada trace com user_id, feature, team, tier. Agrega por sliding window no Redis para budget enforcement em tempo real.
**Confidence:** alta

**Claim:** Prompt Drift Detection é necessário em prompts com dados dinâmicos.
**Evidence:** Qualidade de resposta degrada quando distribuição de inputs muda (novos tipos de pergunta, novos produtos, linguagem diferente). Detectar: monitorar score de qualidade por janela temporal, comparar distribuição de embeddings de inputs (KL divergence).
**Confidence:** alta

**Claim:** Session Replay de agentes é essencial para debugging — reproduzir a sequência exata de steps.
**Evidence:** Agentes falham de formas não-determinísticas. Sem replay (todas as tool calls, contexto em cada step, tokens usados), impossível reproduzir o bug. Langfuse e LangSmith oferecem isso nativamente.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/llmops]]
- [[concepts/prompt-drift]]
- [[concepts/cost-attribution]]
- [[concepts/evals-llm]]
- [[entities/langfuse]]
- [[entities/langsmith]]
- [[concepts/slo]]
- [[concepts/prompt-versioning]]

## Open Questions

- Como definir SLO de qualidade (score > threshold) quando o critério de qualidade muda por feature?
- Prompt drift detection baseado em KL divergence de embeddings — qual o threshold de alarme sem muitos falsos positivos?
