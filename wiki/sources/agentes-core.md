---
type: source
title: "Agentes — Core"
aliases: ["agentes core", "react pattern", "ai agents"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/agentes-core.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [agentes, llm, react-pattern, tool-use, human-in-the-loop, scaffolding, computer-use]
skill: tech-mentor-ai
status: stable
---

## TL;DR

Um agente é um LLM em loop: decide, age via tools, observa resultado, itera. A diferença para um pipeline é a capacidade de roteamento dinâmico — o LLM escolhe o próximo passo. Complexidade emergente: quanto mais autonomia, maior o risco de propagação de erros.

## Key Claims

**Claim:** Agente vs pipeline — a distinção fundamental é controle de fluxo.
**Evidence:** Pipeline tem fluxo fixo (A→B→C). Agente tem fluxo dinâmico — o LLM decide `if/else`, `loops` e qual tool chamar. O loop básico: percebe → raciocina → age → observa → repete.
**Confidence:** alta

**Claim:** ReAct Pattern (Reasoning + Acting) é o loop de agente mais adotado.
**Evidence:** Intercala raciocínio (`Thought:`) com ações (`Action:`) e observações (`Observation:`). Permite debug via trace do raciocínio. Modelos treinados com ReAct têm melhor seguimento de formato que prompt zero-shot.
**Confidence:** alta

**Claim:** Tool design é o gargalo de qualidade em agentes — não o modelo.
**Evidence:** Tool com nome ambíguo ou parâmetros sem description = LLM escolhe errado 30–40% das vezes. Regra: uma tool = uma responsabilidade, nome em snake_case que descreve a ação, description com exemplos de quando usar e quando NÃO usar.
**Confidence:** alta

**Claim:** Tool Selection via Embedding resolve agentes com 20+ tools.
**Evidence:** Em vez de listar todas as tools no contexto (caro e confuso), embeddar descriptions das tools e fazer busca semântica para injetar apenas as N mais relevantes. Reduz tokens e melhora precisão de seleção.
**Confidence:** alta

**Claim:** HITL (Human-in-the-Loop) deve ser baseado em risco, não aplicado em tudo.
**Evidence:** HITL em cada passo elimina o valor do agente. A regra: ações irreversíveis (deletar, enviar e-mail, cobrar cartão) exigem confirmação. Ações reversíveis (rascunho, read-only, preview) podem ser automáticas.
**Confidence:** alta

**Claim:** Scaffolding customizado supera frameworks em produção.
**Evidence:** LangChain/CrewAI abstraem demais — debugging é difícil, upgrade quebra tudo, comportamento interno é opaco. Em produção, a recomendação é: framework para prototipagem, scaffolding customizado quando o agente vai ser mantido.
**Confidence:** média-alta

## Entities & Concepts Touched

- [[concepts/react-pattern]]
- [[concepts/tool-use-agents]]
- [[concepts/human-in-the-loop]]
- [[concepts/agent-scaffolding]]
- [[concepts/computer-use]]
- [[concepts/prompt-injection]]

## Open Questions

- Qual o threshold de "risco" que justifica HITL? Quem define essa política em produção?
- Como medir degradação de qualidade quando tool selection via embedding perde uma tool relevante?
