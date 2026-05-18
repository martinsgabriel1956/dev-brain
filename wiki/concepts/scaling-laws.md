---
type: concept
title: "Scaling Laws"
aliases: ["leis de escala", "neural scaling laws", "power law LLM"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_count: 2
tags: [llm, scaling, treinamento, foundation-model]
skill: tech-mentor-ai
status: stable
---

# Scaling Laws

## Definição

Relações empíricas que mostram que a performance de modelos de linguagem segue uma **lei de potência (power law)** previsível em função de três variáveis:

1. **N** — número de parâmetros do modelo
2. **D** — quantidade de dados de treinamento (tokens)
3. **C** — compute total (FLOPs)

Formalizadas em "Scaling Laws for Neural Language Models" (Kaplan et al., 2020) e aplicadas em [[wiki/sources/gpt3-language-models-are-few-shot-learners]].

## Formulação

```
Loss ∝ N^(-α)   # loss cai como potência do nº de parâmetros
Loss ∝ D^(-β)   # loss cai como potência do nº de tokens
Loss ∝ C^(-γ)   # loss cai como potência do compute
```

O importante: as curvas são **smooth e previsíveis** — sem cliffs ou thresholds óbvios na maioria dos casos.

## Implicações

- **Modelos maiores** = melhor performance por FLOP no regime de compute limitado.
- **Dados importam tanto quanto parâmetros** — um modelo menor treinado em mais dados pode superar um modelo maior com menos dados (hipótese Chinchilla, 2022).
- **Few-shot melhora mais rápido do que zero-shot** com o aumento de escala — implicação direta para [[in-context-learning]].

## Limites das Scaling Laws

- Não garantem performance em **[[emergent-ability|tarefas emergentes]]** — capacidades como [[chain-of-thought]] aparecem abruptamente em ~100B parâmetros, não de forma suave. Ver [[wiki/sources/chain-of-thought-prompting]].
- Não modelam bem **eficiência de inferência** — um modelo 10x maior custa muito mais do que 10x para rodar.
- Diminishing returns existem — GPT-4, Claude 3, Gemini sugerem que a curva continua, mas com ganhos marginais decrescentes.

## Relação com outros conceitos

- [[foundation-model]] — modelos treinados a escala suficiente para emergência de capacidades
- [[in-context-learning]] — capacidade que melhora com escala de forma desproporcionalmente rápida
- [[fine-tuning]] — alternativa quando compute de pré-treino não está disponível

## Fontes

- [[wiki/sources/gpt3-language-models-are-few-shot-learners]]
- [[wiki/sources/chain-of-thought-prompting]] — CoT como exemplo de capacidade que não segue scaling law suave
- Kaplan et al. (2020) — "Scaling Laws for Neural Language Models" [external]
- Hoffmann et al. (2022) — "Training Compute-Optimal Large Language Models" (Chinchilla) [external]
