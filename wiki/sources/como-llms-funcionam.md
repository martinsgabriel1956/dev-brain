---
type: source
title: "Como LLMs Funcionam"
aliases: ["como llms funcionam", "transformers fundamentos", "tokenizacao"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/como-llms-funcionam.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [llms, transformers, tokenizacao, context-window, temperatura, moe, mamba, flash-attention, text-diffusion]
skill: tech-mentor-ai
status: stable
---

## TL;DR

LLMs são previsores de próximo token treinados em escala. Arquitetura Transformer: self-attention (O(n²)) + FFN. Tokens ≠ palavras — ~0.75 palavras/token. Context window é o limite físico de "memória de trabalho". MoE reduz custo ativando apenas sub-redes. Mamba/SSM são alternativas O(n) para sequências longas.

## Key Claims

**Claim:** A tarefa central de LLMs é trivial: prever o próximo token. A inteligência emerge da escala.
**Evidence:** Pré-treino em trilhões de tokens força o modelo a aprender representações internas do mundo para prever bem. Capabilities como raciocínio, código, e tradução são efeitos emergentes, não objetivos de treino explícitos.
**Confidence:** alta

**Claim:** Self-attention é O(n²) — o gargalo para contextos longos.
**Evidence:** Para sequência de n tokens, a matriz de atenção é n×n. 100k tokens = 10B operações por layer. FlashAttention 2/3 resolve isso com IO-aware computation (lê/escreve HBM menos vezes), mas a complexidade assintótica não muda.
**Confidence:** alta

**Claim:** Temperatura controla aleatoriedade — não é simplesmente "criatividade".
**Evidence:** T=0: determinístico (greedy decoding). T>1: distribuição mais plana, mais surpresas mas mais erros. T<1: distribuição mais apontada, mais conservador. Para código ou SQL: T=0. Para escrita criativa: T=0.7–1.0.
**Confidence:** alta

**Claim:** Mixture of Experts (MoE) reduz custo ativando apenas 10–20% dos parâmetros por token.
**Evidence:** GPT-4, Gemini 1.5, Mixtral usam MoE. Router seleciona K experts por token. Parâmetros totais grandes (capacidade), parâmetros ativos pequenos (custo). Trade-off: comunicação entre GPUs mais complexa.
**Confidence:** alta

**Claim:** Text Diffusion (Mercury) tem latência 5–10× menor que modelos AR com qualidade ~10–15% abaixo.
**Evidence:** Geração paralela em vez de token-a-token. Estado: Mercury (Inception Labs, fev/2025) é relevante para código quando latência < 200ms é requerida e qualidade pode ser menor.
**Confidence:** média

## Entities & Concepts Touched

- [[concepts/transformer-architecture]]
- [[concepts/tokenizacao]]
- [[concepts/context-window]]
- [[concepts/mixture-of-experts]]
- [[concepts/mamba-ssm]]
- [[concepts/flash-attention]]
- [[concepts/text-diffusion]]

## Open Questions

- Modelos híbridos Transformer+SSM (Jamba, Zamba) — qual o ponto de inflexão de tamanho de contexto em que SSM vence?
- Como temperatura interage com thinking/reasoning models que têm CoT interno?
