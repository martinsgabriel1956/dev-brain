---
type: concept
title: "Autoregressive Language Model"
aliases: ["modelo autorregressivo", "decoder-only", "causal LM"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_count: 1
tags: [llm, transformer, arquitetura, autoregressive]
skill: tech-mentor-ai
status: draft
---

# Autoregressive Language Model

## Definição

Modelo que gera texto token a token, condicionando cada token nos tokens anteriores. Formalmente, modela a distribuição conjunta P(x₁, x₂, ..., xₙ) como produto de condicionais:

```
P(x₁...xₙ) = ∏ P(xᵢ | x₁...xᵢ₋₁)
```

## Arquitetura

Implementado tipicamente com um **Transformer decoder-only** (sem encoder):
- Atenção causal (masked self-attention) — cada posição só atende a posições anteriores.
- Treinado com objetivo de **next-token prediction** (language modeling loss).

GPT-3 ([[wiki/sources/gpt3-language-models-are-few-shot-learners]]) usa esta arquitetura com:
- Atenção alternando densa e esparsa (Sparse Transformer).
- Pré-normalização (LayerNorm antes da atenção, não depois).
- Tokenização reversível (BPE).

## Contraste com Encoder-Decoder

| Tipo | Exemplo | Melhor para |
|---|---|---|
| Decoder-only (autoregressive) | GPT-3, GPT-4, Llama | Geração de texto, ICL, completions |
| Encoder-only | BERT, RoBERTa | Classificação, extração |
| Encoder-decoder | T5, BART | Tradução, sumarização |

## Por que Decoder-only domina (2023+)

A descoberta de [[in-context-learning]] mostrou que modelos autorregressivos grandes são meta-aprendizes eficientes. O paradigma de fine-tuning encoder-decoder foi gradualmente substituído por ICL + instruction tuning em decoder-only.

## Fontes

- [[wiki/sources/gpt3-language-models-are-few-shot-learners]]
