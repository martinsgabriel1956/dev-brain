---
type: concept
title: "KV Cache"
aliases: ["KV Cache", "key-value cache", "cache de atenção"]
date_created: 2026-07-21
date_updated: 2026-07-21
source_count: 1
tags: [inferencia, llm, atencao, custo, performance]
skill: tech-mentor-ai
status: stub
---

# KV Cache

Estrutura que armazena as chaves (K) e valores (V) de atenção dos tokens já processados por um LLM durante a inferência. Sem cache, cada novo token exigiria reprocessar o contexto inteiro do zero; com cache, o modelo computa apenas o novo token a cada passo, reaproveitando o que já foi calculado — speedup da ordem de ~1000x para contextos longos.

O tamanho do KV Cache cresce com o comprimento do contexto e é um dos principais limitadores de throughput e memória (VRAM) em produção — por isso é alvo constante de técnicas de otimização (ex.: PagedAttention do vLLM, RadixAttention do SGLang para reuso de prefixos compartilhados).

## Economia de KV Cache como vantagem competitiva

O [[wiki/sources/kimi-k3-china-mercado-ia-open-source|Kimi K3]] (Moonshot AI) divulgou um novo método de inferência que promete até 75% de economia no KV Cache, com leve perda de precisão considerada irrelevante nos benchmarks divulgados. Essa economia é um dos motivos técnicos por trás do custo de inferência mais baixo de modelos [[wiki/concepts/mixture-of-experts|MoE]] open source chineses frente a modelos frontier fechados.

## Key Sources

- [[wiki/sources/kimi-k3-china-mercado-ia-open-source]]
