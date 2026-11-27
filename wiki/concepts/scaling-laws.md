---
type: concept
title: "Scaling Laws"
aliases: ["leis de escala", "neural scaling laws", "power law LLM"]
date_created: 2026-05-17
date_updated: 2026-11-27
source_count: 4
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
- [[wiki/concepts/fine-tuning]] — alternativa quando compute de pré-treino não está disponível

## FrontPUSH: "a curva começou a deitar"

Em [[wiki/sources/frontpush-ia-o-futuro-da-ia-parte-1]] (gravado em julho de 2026): "quanto mais você aumenta os parâmetros [...] maior é o resultado", mas "essa curva começou a deitar", e as empresas "já chegaram mais ou menos em um platô com relação à quantidade de parâmetros". Slide: "Curva de energia x parâmetros: já chegou no limite". A corrida agora seria "a melhora dos modelos". Precisão: lei de potência é retorno decrescente, não teto. O platô reconhecido é o do pré-treino, e o ganho migrou para pós-treino e computação na inferência.

## Fontes

- [[wiki/sources/gpt3-language-models-are-few-shot-learners]]
- [[wiki/sources/chain-of-thought-prompting]] — CoT como exemplo de capacidade que não segue scaling law suave
- Kaplan et al. (2020) — "Scaling Laws for Neural Language Models" [external]
- Hoffmann et al. (2022) — "Training Compute-Optimal Large Language Models" (Chinchilla) [external]
- [[wiki/sources/frontpush-ia-o-que-sao-as-llms]]: FrontPUSH, módulo de IA, parte 2: "não adianta você colocar mais parâmetro, mais poder computacional" (retorno decrescente, não nulo); gráfico prometido para depois
- [[wiki/sources/frontpush-ia-o-futuro-da-ia-parte-1]]: FrontPUSH, módulo de IA, aula 5: platô de parâmetros e migração para "a melhora dos modelos"
