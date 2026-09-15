---
type: concept
title: "Prompt Caching"
aliases: ["prompt cache", "cache de prompt", "cache breakpoints"]
date_created: 2026-09-15
date_updated: 2026-09-15
source_count: 1
tags: [prompt-caching, kv-cache, custo-de-ia, ttft, inferencia, tech-mentor-ai]
skill: tech-mentor-ai
status: draft
---

# Prompt Caching

Técnica de engenharia de prompt que explora o [[wiki/concepts/kv-cache|KV Cache]] de inferência para reaproveitar o processamento de um prefixo de prompt (system prompt, descrição de ferramentas, documentos fixos) entre chamadas sucessivas, em vez de reprocessar tudo do zero a cada requisição. Enquanto o KV Cache é o mecanismo interno de inferência, prompt caching é a prática de produção de estruturar e chamar o prompt de forma a acionar esse mecanismo de propósito.

## Por que Existe

Sem cache, cada chamada de API reprocessa o prompt inteiro — mesmo que 90% dele (system prompt, ferramentas, documentos de base) seja idêntico à chamada anterior. Isso desperdiça computação, aumenta custo e aumenta o [[wiki/concepts/time-to-first-token|time to first token]] (TTFT). Prompt caching evita esse reprocessamento reaproveitando o que já foi computado, desde que o prefixo da nova chamada seja idêntico ao que já está no cache.

## Diferenças por Provider

| Provider | Mecanismo | Mínimo de tokens | TTL |
|---|---|---|---|
| Anthropic | Explícito — marcação de `cache_control` ("ephemeral") no bloco a ser cacheado | 1024 tokens (skill tech-mentor-ai); [[wiki/sources/prompt-caching-kv-cache-engenharia-de-contexto-ronald-hulk|uma fonte]] cita 4096 (modelos antigos) e 512 (Opus 5), não verificado | 5 min padrão, extended 1h |
| OpenAI | Implícito/automático — sem configuração, ativa sozinho acima do mínimo | 1024 tokens, granularidade de 128 | Não documentado publicamente (~1-5 min estimado) |
| Google Gemini | Explícito — objeto de cache nomeado, TTL configurável na criação | 4096 (Flash) / 32768 (Pro) | Configurável (min. 1 min, até dias) |
| OpenRouter | Depende da combinação modelo + provedor real por trás | Varia por modelo (ex.: DeepSeek aceita prompts pequenos) | Varia por modelo |

Fonte da coluna de mínimos/TTL: `references/ai/context-engineering.md` (skill tech-mentor-ai), complementado por [[wiki/sources/prompt-caching-kv-cache-engenharia-de-contexto-ronald-hulk]].

## Economia

Cache write costuma custar mais que um token normal (ex.: 3.75x na Anthropic, pago só na 1ª chamada); cache read é muito mais barato (ex.: 0.1x na Anthropic, 50% de desconto na OpenAI). O breakeven costuma ocorrer já na 2ª chamada dentro do TTL quando o prefixo é grande o suficiente (ver fórmula de breakeven em `references/ai/context-engineering.md`, skill tech-mentor-ai).

## Antipadrão: Conteúdo Dinâmico no Início do Prompt

Colocar timestamp, ID de sessão ou qualquer dado que mude a cada chamada logo no início do prompt (ex.: junto ao system prompt) invalida o prefixo cacheável — a nova chamada nunca bate exatamente com o que está no cache, forçando reprocessamento completo. Correção: estrutura em blocos, do mais estático para o mais variável — `[system prompt estático] → [ferramentas] → [documentos fixos] → [histórico] → [query/dado dinâmico do usuário]`. Documentado em [[wiki/sources/prompt-caching-kv-cache-engenharia-de-contexto-ronald-hulk]] e em `references/ai/context-engineering.md` (skill tech-mentor-ai) de forma quase idêntica.

## Requisitos Mínimos para Cache Hit

1. **Suporte** — confirmar se o modelo e o provedor (ex.: combinação específica na OpenRouter) suportam prompt caching.
2. **Prefixo estruturado** — estático primeiro, variável por último.
3. **Tamanho mínimo de tokens** — varia por provider e possivelmente por modelo/geração.
4. **Continuidade/TTL** — saber por quanto tempo o cache persiste antes de expirar.
5. **Medição confiável** — idealmente via telemetria independente do provider (ver [[wiki/sources/llmops-observabilidade]]), já que cada provider expõe a informação de cache hit/miss em um formato diferente no payload de resposta (`CacheUsage` na Anthropic vs. `cached_tokens` na OpenAI).

## Relação com Outros Conceitos

- [[wiki/concepts/kv-cache]] — mecanismo de inferência que o prompt caching explora
- [[wiki/concepts/time-to-first-token]] — métrica de latência diretamente reduzida por cache hit
- [[wiki/concepts/autoregressive-language-model]] — explica por que reprocessar o prefixo do zero é caro (geração/processamento recursivo)
- [[wiki/concepts/ai-gateway-llm-router]] — cache de tokens/contexto listado como uma das alavancas concretas de controle de custo num pipeline multi-provider

## Key Sources

- [[wiki/sources/prompt-caching-kv-cache-engenharia-de-contexto-ronald-hulk]]
