---
type: source
title: "AI Gateway & Token Economics"
aliases: ["ai gateway", "token economics", "litellm", "portkey", "semantic cache"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/ai-gateway-token-economics.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [ai-gateway, token-economics, litellm, portkey, semantic-cache, cascade-pattern, batch-api, finops, budget-enforcement, roteamento]
skill: tech-mentor-ai
status: stable
---

## TL;DR

AI Gateway abstrai providers, roteia por custo/qualidade, implementa fallback e cache semântico. Token economics é sobre decidir programaticamente quando usar modelo caro vs barato. Cascade Pattern (cheap first, scale up) + Semantic Cache (50–70% cache hit) reduzem custo total em 60–80% sem degradação perceptível de qualidade.

## Key Claims

**Claim:** LiteLLM é o padrão open source para proxy multi-provider.
**Evidence:** Interface unificada para 100+ modelos. Roteamento por custo, fallback automático, load balancing, logging centralizado. Deploy como sidecar ou serviço standalone. Limitação: sem cache semântico nativo — requer Redis + implementação própria.
**Confidence:** alta

**Claim:** Cascade Pattern reduz custo sem degradar qualidade percebida.
**Evidence:** Roteamento por complexidade estimada: queries simples → modelo barato (Haiku, GPT-4o-mini). Queries complexas → modelo caro (Opus, GPT-4o). Com classificador de complexidade, 70–80% das queries vão para modelo barato.
**Confidence:** alta

**Claim:** Semantic Cache reduz chamadas ao LLM em 50–70% em workloads com consultas repetitivas.
**Evidence:** Cache por similaridade semântica (cosine similarity > 0.95). Queries semanticamente equivalentes retornam resposta cacheada. Funciona bem para FAQ, suporte, queries analíticas repetitivas. Não funciona para queries criativas ou sensíveis ao tempo.
**Confidence:** alta

**Claim:** Batch API oferece 50% de desconto para processamento assíncrono.
**Evidence:** Anthropic e OpenAI oferecem batch com retorno em até 24h a 50% do preço. Casos ideais: geração de embeddings em massa, análise de documentos offline, enriquecimento de dados.
**Confidence:** alta

**Claim:** Budget enforcement por tenant é obrigatório em produtos multi-tenant.
**Evidence:** Sem controle granular, um tenant com alto volume consome orçamento dos outros. Padrão: Redis com sliding window counter por tenant_id, hard limit com erro 429, soft limit com downgrade para modelo mais barato.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/ai-gateway]]
- [[concepts/cascade-pattern-llm]]
- [[concepts/semantic-cache]]
- [[concepts/token-economics]]
- [[concepts/finops]]
- [[entities/litellm]]
- [[entities/portkey]]

## Open Questions

- Como calibrar o threshold de complexidade para o Cascade Pattern sem um dataset de exemplos rotulados?
- Semantic cache com TTL curto em domínios que mudam rápido (notícias, preços) — como invalidar por domínio?
