---
type: concept
title: "Critérios de Seleção de Provedor de LLM"
aliases: ["avaliar provedor openrouter","tabela de provedores"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [tech-mentor-ai, openrouter, selecao-de-provedor, trade-off, llm]
skill: tech-mentor-ai
status: draft
---

# Critérios de Seleção de Provedor de LLM

Checklist de [[wiki/sources/openrouter-como-profissional-provedores-quantizacao-retencao-fallback-ronald-hulk]] para comparar provedores do mesmo modelo (montar tabela à mão e classificar):

| Critério | O que revela | Nota |
|---|---|---|
| Quantização | Fidelidade do modelo servido | [[wiki/concepts/quantizacao-de-llm]] |
| Throughput (tokens/s) | Velocidade de saída, UX | tolera-se lento em jobs noturnos |
| Latência | Tempo até a resposta começar | ver [[wiki/concepts/time-to-first-token]] |
| Região | Distância (soma à latência), residência de dados | [[wiki/concepts/data-residency]] |
| Disponibilidade | Uptime do provedor | só aparece com o tempo |
| Retenção de dados | O que o provedor faz com o dado | [[wiki/concepts/zero-data-retention]], [[wiki/concepts/lgpd]] |
| **Preço** | Custo por token | **último**: decide-se depois dos demais, via trade-off |

Regra do autor: não existe bala de prata; o critério depende do problema. O resultado vira [[wiki/concepts/adr-architecture-decision-record|ADR]] e alimenta o [[wiki/concepts/pool-de-provedores-llm]].

[skill: tech-mentor-ai] Complementos não citados no vídeo: medir com evals próprios (`references/ai/production-evals.md`, LLM benchmarking de providers) e observar P90/P99, não só média.

## Key sources

- [[wiki/sources/openrouter-como-profissional-provedores-quantizacao-retencao-fallback-ronald-hulk]]
