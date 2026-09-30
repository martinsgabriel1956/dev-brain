---
type: concept
title: "Quantização de LLM (FP4 / FP8 / 16 bits)"
aliases: ["quantização","quantization","fp8","fp4"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [tech-mentor-ai, quantizacao, inferencia, llm, open-weight]
skill: tech-mentor-ai
status: stub
---

# Quantização de LLM

Redução da precisão numérica dos pesos (ex.: de 16 bits para FP8 ou FP4) para diminuir memória e aumentar velocidade/barateza de inferência, ao custo de alguma perda de qualidade.

## Por que importa ao usar um agregador

Em [[wiki/sources/openrouter-como-profissional-provedores-quantizacao-retencao-fallback-ronald-hulk]], a pegadinha é que **o mesmo modelo é servido por provedores com quantizações diferentes** (FP4, FP8, 16). Com roteamento automático, a qualidade pode variar entre chamadas porque o fallback caiu num provedor de quantização menor — sintoma: "às vezes responde bem, às vezes não". Por isso testes devem fixar modelo + provedor + quantização, e o payload pode restringir (`quantizations`).

Experiência do autor (não quantificada): FP8 geralmente muito bom; FP4 tem queda, às vezes aceitável pelo preço.

## [skill] Ordem de grandeza

Para MoE, a skill registra FP8 ≈ -0,5% de benchmark vs FP16 (-50% VRAM, ~+30% throughput) e INT4/AWQ ≈ -3% (`references/ai/open-weight-deployment-2026.md`). Não é FP4 nativo; usar como ordem de grandeza.

Relacionados: [[wiki/concepts/open-weight-model]], [[wiki/concepts/criterios-de-selecao-de-provedor-llm]], [[wiki/concepts/pool-de-provedores-llm]].

## Key sources

- [[wiki/sources/openrouter-como-profissional-provedores-quantizacao-retencao-fallback-ronald-hulk]]
