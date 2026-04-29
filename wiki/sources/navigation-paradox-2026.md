---
type: source
title: "The Navigation Paradox in Large-Context Agentic Coding (2026)"
aliases: ["navigation paradox", "CodeCompass", "ACS benchmark"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 0
tags: [ia, agentes, arquitetura, clean-architecture, dependencias, tokens, pesquisa, mcp, benchmark]
skill: tech-mentor-ai
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/navigation-paradox-2026.md
source_url: https://arxiv.org/html/2602.20048v1
author: "Tarakanath Paipuru"
date_published: 2026-02
date_ingested: 2026-04-23
---

# The Navigation Paradox in Large-Context Agentic Coding (2026)

## TL;DR

Janelas de contexto maiores não resolvem dependências arquiteturais escondidas — apenas deslocam o modo de falha. Em codebases com Clean Architecture ritualística, o Claude Code perde 1 em cada 4 arquivos críticos silenciosamente. A ferramenta de navegação de grafos que resolve o problema é ignorada pelo agente 58% das vezes.

## Key Claims

**Claim:** O Navigation Paradox: contexto maior desloca a falha de "não cabe no contexto" para "não estava saliente o suficiente para o modelo notar".
**Evidence:** 258 trials com Claude Code em benchmark de 30 tarefas. ACS em tarefas com dependências escondidas (G3): 76.2% Vanilla, 78.2% BM25, 99.4% Graph.
**Source:** arxiv.org/html/2602.20048v1
**Confidence:** Alta (paper com benchmark controlado)

**Claim:** BM25 (keyword retrieval) não ajuda em dependências escondidas — performance idêntica ao Vanilla.
**Evidence:** G3 ACS: Vanilla 76.2% vs BM25 78.2% — diferença estatisticamente irrelevante.
**Source:** arxiv.org/html/2602.20048v1
**Confidence:** Alta

**Claim:** O agente ignora a ferramenta de navegação de grafos 58% das vezes, mesmo com prompt explícito instruindo o uso.
**Evidence:** Condition C: 42% de trials usaram a tool (ACS = 99.5%); 58% ignoraram (ACS = 80.2%, idêntico ao Vanilla).
**Source:** arxiv.org/html/2602.20048v1
**Confidence:** Alta

**Claim:** Dependency Injection containers criam conexões entre arquivos que não existem no código-fonte — apenas no runtime.
**Evidence:** AST estático não consegue rastrear vínculos criados por DI containers. CodeCompass usa graph traversal para surfaçar esses arquivos.
**Source:** arxiv.org/html/2602.20048v1
**Confidence:** Alta

**Claim:** G2 (structural dependencies via import chains) não foi beneficiado pelo graph tool — 0% de adoção em 30 trials.
**Evidence:** Adoção do graph tool: G1=22.2%, G2=0%, G3=100% (após melhoria de prompt).
**Source:** arxiv.org/html/2602.20048v1
**Confidence:** Alta (achado surpreendente, não explicado pelo paper)

## Tabela de Resultados

| Condição | G1 (semântico) | G2 (estrutural) | G3 (escondido) |
|---|---|---|---|
| Vanilla | 90.0% | 79.7% | 76.2% |
| BM25 | 100.0% | 85.1% | 78.2% |
| Graph (CodeCompass) | 88.9% | 76.4% | **99.4%** |

## Entities

- [[entities/tarakanath-paipuru]] — autor, pesquisador independente
- [[entities/codecompass]] — MCP server de navegação de grafos de dependência

## Concepts

- [[concepts/navigation-paradox]] — o paradoxo central do paper
- [[concepts/abstraction-bloat]] — relacionado: abstrações geram dependências escondidas
- [[concepts/dependency-injection]] — o caso mais crítico para dependências escondidas
- [[concepts/mcp]] — protocolo usado pelo CodeCompass
- [[concepts/yagni]] — princípio que previne a criação de dependências desnecessárias

## Open Questions

- Por que G2 (structural, import chains) teve 0% de adoção da graph tool se é exatamente o caso de uso dela?
- O comportamento se replica em outros agentes além do Claude Code?
- Como o resultado se generaliza para projetos fora do FastAPI RealWorld?

## Raw Quotes

> "Larger context windows do not eliminate the need for structural navigation; they shift the failure mode from retrieval capacity to navigational salience."

> "When the graph tool is actually invoked (42.0% of trials), mean ACS reaches 99.5%; the 58.0% of trials that skip the tool achieve only 80.2% — indistinguishable from the Vanilla baseline."
