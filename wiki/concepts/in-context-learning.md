---
type: concept
title: "In-Context Learning"
aliases: ["ICL", "aprendizado em contexto"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_count: 3
tags: [llm, few-shot, in-context-learning, prompt-engineering]
skill: tech-mentor-ai
status: stable
---

# In-Context Learning

## Definição

Capacidade de um modelo de linguagem de aprender a realizar uma tarefa a partir de exemplos ou instruções presentes no prompt — **sem atualização de pesos**. O "aprendizado" acontece no forward pass, via atenção ao contexto, não via gradient descent.

Formalizado em [[wiki/sources/gpt3-language-models-are-few-shot-learners]] (Brown et al., 2020).

## Variantes

| Modo | Descrição |
|---|---|
| **Zero-shot** | Apenas instrução em linguagem natural, sem exemplos |
| **One-shot** | Um único exemplo demonstrativo |
| **Few-shot** | Alguns exemplos (tipicamente 10–100) |

Ver [[few-shot-learning]] para detalhes do caso few-shot.

## Por que funciona

A hipótese dominante é que o pré-treinamento em web-scale data faz o modelo absorver "meta-padrões" de tarefas. No momento da inferência, os exemplos no contexto ativam esses padrões — o modelo não aprende do zero, mas reconhece e aplica estruturas que já viu durante o treinamento.

Questão em aberto: ICL é aprendizado genuíno ou recuperação sofisticada de padrões do pré-treino?

## Relação com Scaling Laws

[[scaling-laws]] mostram que modelos maiores são progressivamente mais eficientes no uso de informação de contexto. Performance few-shot cresce mais steeply com tamanho do que zero-shot.

## Implicações Práticas

- Alternativa barata a [[fine-tuning]]: para muitos casos de uso, few-shot ICL é suficiente.
- Hierarquia de custo/esforço: `zero-shot → few-shot → fine-tuning`.
- Qualidade dos exemplos importa mais do que quantidade (sweet spot: 3–5 exemplos).
- Limitação: o contexto tem tamanho finito (context window).

## Fontes

- [[wiki/sources/gpt3-language-models-are-few-shot-learners]]
- [[wiki/sources/microsoft-prompt-engineering-guide]]
- [[wiki/sources/chain-of-thought-prompting]] — CoT como ICL com passos intermediários; nenhum fine-tuning realizado
