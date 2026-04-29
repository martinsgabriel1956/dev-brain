---
type: source
title: "Memória de Agentes"
aliases: ["agent memory", "memoria agentes", "letta memgpt", "mem0"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/agent-memory.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [agentes, memoria, episodica, semantica, procedural, letta, memgpt, mem0, zep, memory-poisoning, memory-drift]
skill: tech-mentor-ai
status: stable
---

## TL;DR

Agentes têm 4 tipos de memória: working (in-context, volátil), episódica (eventos passados, vetorial), semântica (fatos do domínio, grafo), procedural (como agir, system prompt). Letta (MemGPT) é a arquitetura de referência — pagina automaticamente entre context window e external storage. Problemas críticos: memory poisoning e memory drift.

## Key Claims

**Claim:** A hierarquia de memória mapeia diretamente para custo e velocidade de acesso.
**Evidence:** Working memory (in-context): zero latência, custo alto por token, volátil. Episódica (vetorial): ~10ms, custo médio. Semântica (grafo): ~50ms, custo baixo, alta precisão. Procedural (system prompt): zero latência, imutável na sessão.
**Confidence:** alta

**Claim:** Letta (MemGPT) resolve o problema de contexto finito via paginação automática.
**Evidence:** O agente decide quando ler/escrever na external memory usando tools (memory_search, memory_insert, memory_replace). Quando o contexto enche, arquiva automaticamente. A decisão de acesso é do LLM, não do código.
**Confidence:** alta

**Claim:** Memory Poisoning é o risco de segurança mais crítico em agentes com memória persistente.
**Evidence:** Se o agente escreve na memória com base em output de ferramentas (páginas web, e-mails), um atacante pode injetar instruções maliciosas que persistem entre sessões. Defesa: sanitizar antes de escrever, não escrever conteúdo "instruction-like" na memória.
**Confidence:** alta

**Claim:** Memory Drift acumula inconsistências ao longo de muitas sessões sem manutenção.
**Evidence:** Fatos contraditórios coexistem, informações desatualizadas geram respostas erradas. Solução: TTL para fatos episódicos + job semanal de deduplicação e sumarização por LLM.
**Confidence:** alta

**Claim:** Memory Sharing em multi-agente requer namespace isolation.
**Evidence:** Shared memory sem controle de acesso → agentes sobrescrevem dados uns dos outros. Padrão: namespace por agente + shared namespace read-only para conhecimento global.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/agent-memory]]
- [[concepts/memory-poisoning]]
- [[concepts/memory-drift]]
- [[concepts/context-engineering]]
- [[entities/letta]]
- [[entities/mem0]]
- [[entities/zep]]

## Open Questions

- Como balancear retrieval recall (buscar mais) vs precisão (buscar menos) em memória semântica?
- Em multi-agente com memória compartilhada, quem tem permissão de deletar fatos?
