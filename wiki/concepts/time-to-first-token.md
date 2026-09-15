---
type: concept
title: "Time to First Token (TTFT)"
aliases: ["TTFT", "tempo para o primeiro token"]
date_created: 2026-09-15
date_updated: 2026-09-15
source_count: 2
tags: [ttft, latencia, llm-observability, custo-de-ia, tech-mentor-ai]
skill: tech-mentor-ai
status: stub
---

# Time to First Token (TTFT)

Métrica de latência que mede o tempo entre o envio de uma requisição a um LLM e o recebimento do primeiro token de resposta (antes da resposta começar a fazer streaming). É a métrica que mais afeta a percepção de "rapidez" de uma aplicação de IA, mesmo quando o tempo total de geração é maior.

## Relação com Prompt Caching

Um cache hit reduz o TTFT diretamente: se o prefixo do prompt (system prompt, ferramentas, documentos fixos) já está no [[wiki/concepts/kv-cache|KV Cache]], o provedor não precisa reprocessar essa parte antes de começar a gerar o primeiro token de resposta. Ver [[wiki/concepts/prompt-caching]] e [[wiki/sources/prompt-caching-kv-cache-engenharia-de-contexto-ronald-hulk]].

## Como Métrica de Observabilidade

[[wiki/sources/llmops-observabilidade]] cita TTFT como uma das métricas centrais de um trace de LLM (ao lado de TPS — tokens por segundo, contagem de tokens e score de qualidade), recomendando SLOs explícitos (ex.: TTFT < 500ms p95) como parte de uma prática de LLMOps madura.

## Key Sources

- [[wiki/sources/llmops-observabilidade]]
- [[wiki/sources/prompt-caching-kv-cache-engenharia-de-contexto-ronald-hulk]]
