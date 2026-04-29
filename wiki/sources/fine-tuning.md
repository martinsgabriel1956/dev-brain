---
type: source
title: "Fine-tuning & Especialização"
aliases: ["fine-tuning", "lora", "qlora", "rlhf", "dpo", "instruction tuning"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/fine-tuning.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [fine-tuning, lora, qlora, peft, instruction-tuning, catastrophic-forgetting, rlhf, dpo, grpo, synthetic-data, knowledge-distillation, raft, model-merging]
skill: tech-mentor-ai
status: stable
---

## TL;DR

Fine-tuning só vale quando prompt engineering + RAG foram esgotados. LoRA é o método padrão — treina matrizes de baixo rank sem alterar pesos base. QLoRA permite fine-tuning em GPUs consumer (4-bit quantization). DPO substituiu RLHF em maioria dos casos — mais simples, sem reward model separado. Catastrophic forgetting é o risco principal.

## Key Claims

**Claim:** Fine-tuning é justificado em poucos cenários específicos.
**Evidence:** Use quando: formato de output muito específico (structured JSON customizado), estilo consistente que prompt não consegue manter, latência exige modelo menor, domínio especializado com vocabulário que o base model não conhece. NÃO use para injetar conhecimento factual — RAG é melhor para isso.
**Confidence:** alta

**Claim:** LoRA treina matrizes de baixo rank em vez dos pesos completos — reduz 100× os parâmetros treináveis.
**Evidence:** Peso original W (d×d) → decomposição W + ΔW onde ΔW = A×B (A: d×r, B: r×d, r<<d). Apenas A e B são treinados. r=8–64 cobre 99% dos casos. Merge com pesos base para zero overhead em inference.
**Confidence:** alta

**Claim:** DPO é o substituto prático do RLHF — mais estável e sem reward model separado.
**Evidence:** RLHF requer 3 etapas (SFT + RM + PPO). DPO colapsa em fine-tuning direto com pares de preferência (chosen/rejected). Resultados comparáveis em alinhamento de comportamento com 50% menos complexidade de treino.
**Confidence:** alta

**Claim:** Catastrophic Forgetting é o risco mais crítico — o modelo perde capacidades gerais.
**Evidence:** Fine-tuning em domínio específico degrada performance em outras tasks se o dataset for pequeno ou muito homogêneo. Mitigação: replay buffer (incluir 10–20% de dados gerais no treino), LoRA (pesos base preservados), avaliação em benchmarks gerais antes/depois.
**Confidence:** alta

**Claim:** Synthetic Data Generation resolve o cold start de datasets de fine-tuning.
**Evidence:** GPT-4 / Claude gera pares instruction-output de alta qualidade a baixo custo. Técnica: seed com 20–50 exemplos reais → gerar variações. Qualidade do sintético é suficiente para maioria dos casos de format adaptation.
**Confidence:** média-alta

## Entities & Concepts Touched

- [[concepts/lora]]
- [[concepts/qlora]]
- [[concepts/dpo]]
- [[concepts/rlhf]]
- [[concepts/catastrophic-forgetting]]
- [[concepts/knowledge-distillation]]
- [[concepts/model-merging]]

## Open Questions

- Como detectar catastrophic forgetting durante o treino, antes de fazer merge dos adaptadores?
- Model merging (SLERP/TIES/DARE) vs ensemble — quando merging degrada e qual o sinal de alerta?
