---
type: concept
title: "Zero-Shot Learning"
aliases: ["zero-shot", "zero-shot prompting", "aprendizado zero-shot"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_count: 1
tags: [llm, zero-shot, in-context-learning, prompt-engineering]
skill: tech-mentor-ai
status: stable
---

# Zero-Shot Learning

## Definição

Variante de [[in-context-learning]] em que o prompt contém apenas a instrução da tarefa — **sem nenhum exemplo** demonstrativo. O modelo generaliza diretamente do pré-treinamento.

Distinto de [[few-shot-learning]] (múltiplos exemplos) e one-shot (exatamente um exemplo).

## Quando Usar

- Tarefa simples e bem conhecida pelo modelo (ex: tradução, classificação de sentimento).
- Quando não há exemplos disponíveis.
- Primeira tentativa antes de escalar para few-shot.

## Limitações

- Para tarefas com padrão de output muito específico, zero-shot frequentemente gera formato inconsistente.
- Performance inferior ao few-shot em tarefas que exigem raciocínio estruturado.
- Modelos menores ou menos capazes se beneficiam mais de exemplos.

## Relação com a Hierarquia de Prompting

```
Zero-shot → Few-shot → Chain-of-Thought → Fine-tuning
(tente sempre zero-shot primeiro)
```

## Fontes

- [[wiki/sources/microsoft-prompt-engineering-guide]]
- [[wiki/sources/gpt3-language-models-are-few-shot-learners]]
