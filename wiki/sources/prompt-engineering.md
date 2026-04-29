---
type: source
title: "Prompt Engineering Sistemático"
aliases: ["prompt engineering", "chain of thought", "few-shot", "self-consistency", "dspy"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/prompt-engineering.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [prompt-engineering, chain-of-thought, few-shot, self-consistency, role-prompting, meta-prompting, dspy, prompt-caching, prompt-injection]
skill: tech-mentor-ai
status: stable
---

## TL;DR

Hierarquia: Zero-shot → Few-shot → CoT → Self-Consistency → Fine-tuning. Experimente da esquerda para direita antes de escalar custo. CoT com "pense passo a passo" melhora raciocínio em modelos grandes. Self-Consistency (vote majority com N amostras) melhora confiabilidade em tarefas com resposta única correta. DSPy compila prompts automaticamente como código.

## Key Claims

**Claim:** A hierarquia de complexidade deve ser seguida antes de escalar para fine-tuning.
**Evidence:** Zero-shot é gratuito e funciona para 70% dos casos. Few-shot resolve formato. CoT resolve raciocínio. Self-consistency resolve confiabilidade. Fine-tuning só quando nenhuma das anteriores é suficiente — custa 100× mais para implementar.
**Confidence:** alta

**Claim:** Chain-of-Thought (CoT) melhora significativamente tarefas multi-passo — mas só em modelos grandes.
**Evidence:** "Pense passo a passo" ou "Let's think step by step" ativa CoT implícito. Melhora em 20–40% em benchmarks de raciocínio para GPT-4o/Claude Sonnet+. Modelos pequenos (Haiku, mini) tendem a ignorar e pular para resposta.
**Confidence:** alta

**Claim:** Few-shot com 3–5 exemplos é o sweet spot — mais exemplos têm retorno decrescente.
**Evidence:** Exemplos ruins são piores que zero exemplos. Cubra variações de formato que existem em produção. Mais de 5 exemplos raramente melhora qualidade e aumenta custo de tokens linearmente.
**Confidence:** alta

**Claim:** Self-Consistency eleva confiabilidade para tasks com resposta única correta.
**Evidence:** Gera N amostras com temperatura > 0, extrai a resposta de cada, voto majoritário. Para N=5, erro cai ~40% em comparação com greedy decoding. Custo: N× tokens. Use quando qualidade > custo.
**Confidence:** alta

**Claim:** DSPy compila prompts automaticamente — substitui prompt engineering manual para pipelines complexos.
**Evidence:** Define o módulo (input/output), define a métrica, DSPy otimiza os prompts (e até few-shot examples) via algoritmo de compilação. Abordagem de software engineering para prompts — reproduzível e versionável.
**Confidence:** média

## Entities & Concepts Touched

- [[concepts/chain-of-thought]]
- [[concepts/few-shot-prompting]]
- [[concepts/self-consistency]]
- [[concepts/meta-prompting]]
- [[concepts/dspy]]
- [[concepts/prompt-caching]]

## Open Questions

- DSPy em produção: qual o overhead de compilação e como lidar com regressão quando o modelo base é atualizado?
- Self-Consistency com N=5 vs N=3 — o ganho de confiabilidade justifica o custo 1.67× maior?
