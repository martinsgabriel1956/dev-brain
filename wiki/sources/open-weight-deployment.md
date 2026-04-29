---
type: source
title: "Open-Weight Deployment em Produção (2026)"
aliases: ["open weight deployment", "self-hosted llm", "vllm", "sglang", "qwen", "llama4"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/open-weight-deployment.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [open-weight, self-hosted, vllm, sglang, gemma4, qwen35, llama4, quantizacao, lora, licenciamento, finops, multi-tier]
skill: tech-mentor-ai
status: stable
---

## TL;DR

Em 2026, self-hosted open-weight é viável para workloads > 10M tokens/dia — abaixo disso API é mais barato. Qwen3.5 (Apache 2.0) e Gemma 4 (Apache 2.0) são os melhores para produção sem restrição jurídica. vLLM para workloads genéricos, SGLang para throughput máximo em MoE. Estratégia multi-tier: open-weight para tarefas simples + API para complexas.

## Key Claims

**Claim:** Break-even self-hosted vs API está em ~10M tokens/dia em 2026.
**Evidence:** Abaixo de 10M tokens/dia: custo de GPU + operação + DevOps > custo de API. Acima: self-hosted começa a economizar. Cálculo inclui: GPU spot (A10G ~$1.5/h), custo de operação (DevOps, monitoring), disponibilidade (API tem SLA de 99.9%, self-hosted requer HA próprio).
**Confidence:** média-alta

**Claim:** Apache 2.0 é o único licenciamento sem restrições para produção comercial.
**Evidence:** Llama 4 Community License proíbe uso acima de 700M MAU. Qwen3.5-72B e Gemma 4 são Apache 2.0 — zero fricção jurídica. Para enterprise, validar com legal antes de usar qualquer modelo não-Apache.
**Confidence:** alta

**Claim:** SGLang supera vLLM em throughput para modelos MoE grandes (>30B parâmetros).
**Evidence:** RadixAttention (prefix caching automático) + otimizações específicas para MoE. Em benchmarks Q1 2026: SGLang 1.2–1.8× throughput vs vLLM para Qwen3.5-MoE. vLLM tem ecossistema mais maduro e melhor integração com cloud.
**Confidence:** média

**Claim:** Multi-tier strategy é o padrão de produção: open-weight para simples + API para complexo.
**Evidence:** Tier 1: modelo local quantizado (4-bit) para classificação, extração, FAQ — zero custo marginal. Tier 2: API mid-tier (Sonnet, GPT-4o-mini) para tasks médias. Tier 3: API top-tier (Opus, GPT-4o) para raciocínio complexo. Router por complexidade distribui 70–80% para tier 1.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/open-weight-models]]
- [[concepts/vllm]]
- [[concepts/sglang]]
- [[concepts/quantizacao-llm]]
- [[concepts/multi-tier-routing]]
- [[concepts/cascade-pattern-llm]]

## Open Questions

- Como medir "complexidade" de uma query para o router multi-tier sem gastar tokens de modelo caro para classificar?
- SGLang RadixAttention — qual o impacto em workloads sem repetição de prefix (queries totalmente únicas)?
