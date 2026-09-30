---
type: entity
title: "OpenRouter"
aliases: ["open router"]
date_created: 2026-08-05
date_updated: 2026-09-30
source_count: 4
tags: [tech-mentor-ai, ai-gateway, multi-provider, llm, prompt-caching]
skill: tech-mentor-ai
status: stub
---

# OpenRouter

Serviço/gateway que agrega acesso a múltiplos modelos de LLM (incluindo modelos chineses como GLM) por trás de uma única API, citado em [[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]] como um dos providers plugáveis num [[wiki/concepts/ai-gateway-llm-router|AI Gateway]] self-hosted — o autor da fonte descreve preferência pessoal por rodar seu setup via OpenRouter em vez de contas diretas dos providers originais.

## Prompt Caching Depende de Modelo + Provedor

[[wiki/sources/prompt-caching-kv-cache-engenharia-de-contexto-ronald-hulk]] descreve que, ao contrário de chamar um provider diretamente (Anthropic, OpenAI), o suporte a [[wiki/concepts/prompt-caching]] na OpenRouter precisa ser verificado caso a caso pela combinação específica de modelo e provedor real por trás dele — não existe uma regra única da OpenRouter em si.

## Seletor de Modelo em Prompt Manager

Em [[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]], o autor escolhe o modelo de cada versão de prompt pelo ID do OpenRouter, com presets no código ([[wiki/concepts/prompt-registry-local]]).

## Uso Profissional: Modelo + Provedor

Segundo [[wiki/sources/openrouter-como-profissional-provedores-quantizacao-retencao-fallback-ronald-hulk]], a chamada crua roteia para qualquer provedor; o uso profissional fixa um [[wiki/concepts/pool-de-provedores-llm|pool de ≥3 provedores]] avaliados por [[wiki/concepts/criterios-de-selecao-de-provedor-llm|seis critérios]] e restringe quantização, preço e retenção de dados no payload. Modelos [[wiki/concepts/open-weight-model|open weight]] têm preço distribuído por provedor.

## Key Sources

- [[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]]
- [[wiki/sources/prompt-caching-kv-cache-engenharia-de-contexto-ronald-hulk]] — suporte a prompt caching como propriedade da combinação modelo+provedor, não da OpenRouter isoladamente
- [[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]] — IDs de modelo do OpenRouter no registro de versões de prompt
- [[wiki/sources/openrouter-como-profissional-provedores-quantizacao-retencao-fallback-ronald-hulk]] — guia de uso profissional: modelo+provedor, pool, quantização, ZDR e payload `provider`
