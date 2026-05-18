---
type: concept
title: "Few-Shot Learning"
aliases: ["few-shot", "aprendizado com poucos exemplos"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_count: 3
tags: [llm, few-shot, in-context-learning, prompt-engineering]
skill: tech-mentor-ai
status: stable
---

# Few-Shot Learning

## Definição

Variante de [[in-context-learning]] em que o prompt contém alguns exemplos demonstrativos (tipicamente 10–100) do padrão entrada→saída desejado. O modelo generaliza o padrão sem atualizar pesos.

Distinto de **zero-shot** (nenhum exemplo) e **one-shot** (exatamente um exemplo).

## Como Usar

```
# Estrutura básica de um prompt few-shot
<instrução>

Exemplos:
Input: <exemplo 1 entrada>
Output: <exemplo 1 saída>

Input: <exemplo 2 entrada>
Output: <exemplo 2 saída>

Input: <entrada real>
Output:
```

**Sweet spot prático:** 3–5 exemplos. Mais exemplos aumentam custo de tokens sem ganho proporcional.

## Resultados do GPT-3 (2020)

| Benchmark | Zero-Shot | Few-Shot | SOTA Fine-tuned |
|---|---|---|---|
| TriviaQA | 64.3% | **71.2%** | 68.0% (RAG) |
| PIQA | 80.5% | **82.8%** | 79.4% |
| Winogrande | 70.2% | 77.7% | 84.6% |

Few-shot sem fine-tuning superou o SOTA fine-tuned em TriviaQA e PIQA.

## Quando Usar vs Fine-tuning

| Critério | Few-Shot ICL | Fine-tuning |
|---|---|---|
| Dataset rotulado disponível | Não necessário | Necessário (milhares de exemplos) |
| Custo de iteração | Baixo (muda o prompt) | Alto (re-treino) |
| Performance máxima | Boa | Melhor (na maioria dos casos) |
| Generalização | Depende do modelo base | Pode overfit à distribuição |

## Few-Shot CoT

[[chain-of-thought]] prompting é uma extensão direta do few-shot: em vez de exemplares `input → output`, usa-se `input → passos de raciocínio → output`. Com 8 exemplares, PaLM 540B supera GPT-3 fine-tuned no GSM8K. Ver [[wiki/sources/chain-of-thought-prompting]].

## Fontes

- [[wiki/sources/gpt3-language-models-are-few-shot-learners]]
- [[wiki/sources/microsoft-prompt-engineering-guide]]
- [[wiki/sources/chain-of-thought-prompting]]
