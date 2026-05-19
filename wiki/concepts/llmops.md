---
type: concept
title: "LLMOps"
aliases: ["llm ops", "operações de llm", "ai ops"]
date_created: 2026-05-18
date_updated: 2026-05-18
source_count: 1
tags: [llm, agentes-ia, mlops, infraestrutura, operacoes]
skill: tech-mentor-ai
status: stub
---

## Definição

Conjunto de práticas, ferramentas e cultura organizacional para operar sistemas baseados em LLMs em produção — analogia ao MLOps para modelos de machine learning tradicionais e ao DevOps para software geral.

Inclui: gestão de prompts, monitoramento de qualidade de outputs, controle de custos (tokens), orquestração de agentes, versionamento de contexto e observabilidade de fluxos agênticos.

---

## Contexto de Uso Cotidiano

O fenômeno [[token-anxiety]] emerge justamente no nível de LLMOps do dia a dia do desenvolvedor individual: gerenciar janelas de contexto ([[janela-de-contexto]]), decidir quais agentes rodar em paralelo, monitorar outputs e planejar resets.

O vocabulário de LLMOps ainda está em formação — o uso de metáforas de controle de animais (*harness*, *reins*, *leash*) para descrever orquestração de agentes reflete essa imaturidade conceitual.

## Ferramentas Relevantes

- **Claude Code** ([[claude-code]]): CLI com agentes e janela de contexto com reset programado
- Orquestradores multi-agent (LangGraph, AutoGen, CrewAI)
- Observabilidade: LangSmith, Helicone, Langfuse

---

## Key Sources

- [[wiki/sources/token-anxiety-agentes-ia-comportamento-devs]]
