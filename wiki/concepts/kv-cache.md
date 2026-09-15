---
type: concept
title: "KV Cache"
aliases: ["KV Cache", "key-value cache", "cache de atenção"]
date_created: 2026-07-21
date_updated: 2026-09-15
source_count: 3
tags: [inferencia, llm, atencao, custo, performance]
skill: tech-mentor-ai
status: stub
---

# KV Cache

Estrutura que armazena as chaves (K) e valores (V) de atenção dos tokens já processados por um LLM durante a inferência. Sem cache, cada novo token exigiria reprocessar o contexto inteiro do zero; com cache, o modelo computa apenas o novo token a cada passo, reaproveitando o que já foi calculado — speedup da ordem de ~1000x para contextos longos.

O tamanho do KV Cache cresce com o comprimento do contexto e é um dos principais limitadores de throughput e memória (VRAM) em produção — por isso é alvo constante de técnicas de otimização (ex.: PagedAttention do vLLM, RadixAttention do SGLang para reuso de prefixos compartilhados).

## Economia de KV Cache como vantagem competitiva

O [[wiki/sources/kimi-k3-china-mercado-ia-open-source|Kimi K3]] (Moonshot AI) divulgou um novo método de inferência que promete até 75% de economia no KV Cache, com leve perda de precisão considerada irrelevante nos benchmarks divulgados. Essa economia é um dos motivos técnicos por trás do custo de inferência mais baixo de modelos [[wiki/concepts/mixture-of-experts|MoE]] open source chineses frente a modelos frontier fechados.

## Por que Existe: o Custo do Reprocessamento Autorregressivo

[[wiki/concepts/autoregressive-language-model]] explica o problema de base que o KV Cache mitiga: sem cache, cada token gerado exigiria reprocessar do zero toda a sequência anterior (prompt + tokens já gerados), porque a geração é recursiva por natureza. [[wiki/sources/tokens-o-que-sao-e-por-que-custam-caro]] descreve esse reprocessamento token a token de forma didática (sem mencionar o KV Cache diretamente) como a razão estrutural pela qual o token de output custa mais que o de input em todos os providers — o KV Cache é a técnica de produção que existe justamente para evitar recalcular o que já foi computado, amortizando (mas não eliminando) esse custo.

## Prompt Caching: Explorando o KV Cache de Propósito em Produção

[[wiki/concepts/prompt-caching]] é a prática de estruturar prompts e chamadas de API deliberadamente para acionar reuso do KV Cache entre requisições com o mesmo prefixo (system prompt, ferramentas, documentos fixos), em vez de deixar o reaproveitamento como efeito colateral. [[wiki/sources/prompt-caching-kv-cache-engenharia-de-contexto-ronald-hulk]] documenta as diferenças de implementação entre providers (Anthropic com cache mais explícito e TTL configurável, OpenAI com cache implícito, OpenRouter dependendo de modelo+provedor), os antipadrões que quebram o cache (dado dinâmico no início do prompt) e o impacto direto na redução do [[wiki/concepts/time-to-first-token|time to first token]].

## Key Sources

- [[wiki/sources/kimi-k3-china-mercado-ia-open-source]]
- [[wiki/sources/tokens-o-que-sao-e-por-que-custam-caro]] — explicação didática do problema de reprocessamento autorregressivo que motiva a existência do KV Cache
- [[wiki/sources/prompt-caching-kv-cache-engenharia-de-contexto-ronald-hulk]] — prompt caching como prática de produção que explora o KV Cache de propósito, com diferenças por provider e antipadrões comuns
