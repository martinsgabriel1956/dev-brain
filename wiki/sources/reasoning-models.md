---
type: source
title: "Reasoning Models & Long Context"
aliases: ["reasoning models", "extended thinking", "o1", "o3", "deepseek r1", "chain of thought interno"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/reasoning-models.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [reasoning-models, extended-thinking, o1, o3, deepseek-r1, thinking-budget, swe-bench, long-context, computer-use, coding-agents, metr]
skill: tech-mentor-ai
status: stable
---

## TL;DR

Reasoning models gastam tokens extras em pensamento interno antes de responder. Claude Extended Thinking expõe o raciocínio explicitamente; o1/o3 (OpenAI) o esconde. DeepSeek R1 é open-weight com reasoning_content separado. Use para: provas matemáticas, arquitetura complexa, debugging difícil. Evite para: FAQ, extração, tasks simples — latência e custo são muito maiores.

## Key Claims

**Claim:** Reasoning models só valem quando a task requer raciocínio multi-passo ou validação interna.
**Evidence:** Para math, lógica formal, arquitetura complexa: reasoning models superam modelos padrão em 20–40% (SWE-bench, AIME). Para extração, classificação, FAQ: performance igual ou pior com custo 5–10× maior. Heurística: se a resposta certa exige verificar passo intermediário, use reasoning.
**Confidence:** alta

**Claim:** Claude Extended Thinking expõe o chain-of-thought — útil para debugging e confiança.
**Evidence:** Resposta contém bloco `thinking` separado do bloco `text`. Budget de tokens configurável (1k–16k). Quanto maior o budget, mais tempo de "pensar". Para arquitetura complexa, 4k–8k tokens de budget é suficiente.
**Confidence:** alta

**Claim:** DeepSeek R1 é o reasoning model open-weight mais capaz em 2026.
**Evidence:** Expõe `reasoning_content` explicitamente. Performance comparável ao o1 em math/coding. Apache 2.0 — self-hostável. Custo ~80% menor que API OpenAI em volumes altos. Destilações (R1-7B, R1-14B) viáveis em GPU consumer.
**Confidence:** alta

**Claim:** METR Task Length Metric mede autonomia de agente — minutos de trabalho equivalente que o agente executa sem erro.
**Evidence:** Métrica emergente para comparar agentes de coding. Claude Code, Devin, SWE-agent medidos em "minutos autônomos". Crescimento exponencial em 2024–2026: de 2min para 30–60min. Termômetro de maturidade da indústria.
**Confidence:** média

## Entities & Concepts Touched

- [[concepts/reasoning-models]]
- [[concepts/extended-thinking]]
- [[concepts/thinking-budget]]
- [[entities/deepseek-r1]]
- [[concepts/long-context]]
- [[concepts/computer-use]]
- [[concepts/coding-agents]]

## Open Questions

- Como calibrar thinking budget_tokens sem rodar múltiplos experimentos? Existe heurística por tipo de task?
- METR Task Length — como adaptar essa métrica para avaliar agentes de domínio não-coding?
