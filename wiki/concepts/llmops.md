---
type: concept
title: "LLMOps"
aliases: ["llm ops", "operações de llm", "ai ops"]
date_created: 2026-05-18
date_updated: 2026-06-01
source_count: 3
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

## LLMOps e o ROI Organizacional

Na [[era-agentica]], LLMOps passou de "prática de engenharia" para "problema de CFO". O custo por dev passou de dezenas para centenas de dólares/mês em tokens. Dados do Google (DORA) mostram que leva **8 meses** para o investimento em IA começar a dar retorno.

LLMOps bem feito — governança, observabilidade, controle de custo, harness de qualidade — é o que fecha o [[learning-gap-organizacional]] e converte ganho individual em [[roi-de-ia]] real. Sem isso, [[ai-washing]]: licença + pressão + cortes sem resultado.

## Gestão de Arquivos de Contexto como Problema de LLMOps

Manter `agents.md` / `CLAUDE.md` é uma decisão de LLMOps com trade-off mensurável:

- Sem arquivo → agente alucina, ignora convenções do projeto, gera código fora do padrão
- Com arquivo muito grande → +19–20% de custo por sessão, latência maior
- Com arquivo enxuto + links sob demanda → equilíbrio entre controle e custo

Paper de Zurique (Universidade de Zurique) quantificou o custo. A estratégia recomendada: base mínima no arquivo principal, arquivos específicos linkados e carregados sob demanda. Ver [[claude-md]] e [[instruction-budget]].

## Key Sources

- [[wiki/sources/token-anxiety-agentes-ia-comportamento-devs]]
- [[wiki/sources/ia-custo-roi-bolha-ou-realidade]]
- [[wiki/sources/agents-md-vale-a-pena-paper-zurique]] — paper de Zurique; custo de arquivos de contexto; estratégia enxuto + links
