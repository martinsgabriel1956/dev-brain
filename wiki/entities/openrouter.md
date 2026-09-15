---
type: entity
title: "OpenRouter"
aliases: ["open router"]
date_created: 2026-08-05
date_updated: 2026-09-15
source_count: 2
tags: [tech-mentor-ai, ai-gateway, multi-provider, llm, prompt-caching]
skill: tech-mentor-ai
status: stub
---

# OpenRouter

Serviço/gateway que agrega acesso a múltiplos modelos de LLM (incluindo modelos chineses como GLM) por trás de uma única API, citado em [[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]] como um dos providers plugáveis num [[wiki/concepts/ai-gateway-llm-router|AI Gateway]] self-hosted — o autor da fonte descreve preferência pessoal por rodar seu setup via OpenRouter em vez de contas diretas dos providers originais.

## Prompt Caching Depende de Modelo + Provedor

[[wiki/sources/prompt-caching-kv-cache-engenharia-de-contexto-ronald-hulk]] descreve que, ao contrário de chamar um provider diretamente (Anthropic, OpenAI), o suporte a [[wiki/concepts/prompt-caching]] na OpenRouter precisa ser verificado caso a caso pela combinação específica de modelo e provedor real por trás dele — não existe uma regra única da OpenRouter em si.

## Key Sources

- [[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]]
- [[wiki/sources/prompt-caching-kv-cache-engenharia-de-contexto-ronald-hulk]] — suporte a prompt caching como propriedade da combinação modelo+provedor, não da OpenRouter isoladamente
