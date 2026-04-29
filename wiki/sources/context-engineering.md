---
type: source
title: "Context Engineering"
aliases: ["context engineering", "prompt caching", "lost in the middle", "sliding window"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/context-engineering.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [context-engineering, prompt-caching, sliding-window, summarization, lost-in-the-middle, token-budget, semantic-cache, long-context, rag]
skill: tech-mentor-ai
status: stable
---

## TL;DR

Context Engineering é a disciplina de gerenciar o que entra na context window para maximizar qualidade e minimizar custo. 5 estratégias: Sliding Window (descarta antigo), Summarization (comprime), Vector Memory (busca semântica), Selective Context (injeta só o necessário), Map-Reduce (processa em partes). Prompt Caching reduz custo em 80–90% para prefixes estáveis.

## Key Claims

**Claim:** Lost-in-the-Middle é o problema central de contextos longos — modelos degradam no meio.
**Evidence:** Experimentos mostram que LLMs têm melhor recall para informações no início e no fim do contexto. Informação crítica no meio de 100k tokens tem recall 20–40% menor. Solução: posicionar informação crítica no início ou fim, usar RAG para extrair trechos relevantes.
**Confidence:** alta

**Claim:** Prompt Caching reduz custo em 80–90% para prefixes estáveis.
**Evidence:** Anthropic: cache breakpoints explícitos com `cache_control`. OpenAI: cache automático para prefixes > 1024 tokens. Cache hit = 90% desconto (Anthropic) ou 50% (OpenAI). Requisito: o prefix cacheado deve ser imutável entre chamadas.
**Confidence:** alta

**Claim:** Long Context vs RAG — a decisão é custo vs simplicidade.
**Evidence:** Long Context: mais simples, sem pipeline de indexação, melhor para documentos < 200k tokens. RAG: mais barato em escala, mais complexo, melhor para bases grandes e dinâmicas. Hybrid (RAG + Long Context): padrão emergente — RAG para retrieval, long context para raciocínio sobre trechos recuperados.
**Confidence:** alta

**Claim:** Sliding Window é a estratégia mais simples mas perde contexto histórico.
**Evidence:** Mantém apenas as últimas N mensagens. Simples de implementar. Problema: conversa longa perde informação do início. Solução parcial: sempre incluir system prompt + primeira mensagem do usuário + últimas N.
**Confidence:** alta

**Claim:** Summarization comprime histórico sem perder informação crítica — mas adiciona latência e custo.
**Evidence:** Quando contexto atinge 80% do limite, sumariza as mensagens mais antigas em um bloco. A sumarização em si custa tokens. Trade-off: qualidade de compressão vs velocidade vs custo.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/context-engineering]]
- [[concepts/prompt-caching]]
- [[concepts/lost-in-the-middle]]
- [[concepts/sliding-window-context]]
- [[concepts/token-budget]]
- [[concepts/rag-retrieval]]
- [[concepts/semantic-cache]]

## Open Questions

- Como medir empiricamente a degradação de qualidade por posição no contexto para um modelo específico?
- Break-even analysis de prompt caching: qual o mínimo de cache hit rate para justificar refatorar o prompt?
