---
type: concept
title: "Fine-Tuning"
aliases: ["fine-tune", "ajuste fino", "task-specific fine-tuning"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_count: 3
tags: [llm, treinamento, fine-tuning, adaptação]
skill: tech-mentor-ai
status: draft
---

# Fine-Tuning

## Definição

Processo de continuar o treinamento de um modelo pré-treinado ([[foundation-model]]) em um dataset específico de tarefa, atualizando alguns ou todos os pesos do modelo via gradient descent.

## Problema que GPT-3 Endereça

Conforme [[wiki/sources/gpt3-language-models-are-few-shot-learners]], fine-tuning tem três limitações:

1. **Requer dados rotulados por tarefa** — milhares a dezenas de milhares de exemplos.
2. **Risco de overfitting** à distribuição do dataset de fine-tuning.
3. **Correlações espúrias** — o modelo pode aprender artefatos do dataset que não generalizam.

[[in-context-learning]] via [[few-shot-learning]] é a alternativa proposta: sem gradient updates, apenas exemplos no contexto.

## Quando Fine-Tuning Ainda Faz Sentido

- Tarefa muito específica com distribuição distante do pré-treino.
- Dataset rotulado grande disponível.
- Necessidade de performance máxima (ICL tem teto abaixo do fine-tuned SOTA em muitos casos).
- Latência e custo de inferência críticos (modelo menor fine-tuned pode superar modelo maior via ICL).

## Variantes Modernas

- **LoRA / QLoRA** — fine-tuning de matrizes de baixo rank, muito mais barato.
- **Instruction tuning** — fine-tuning em pares instrução→resposta para alinhar comportamento.
- **RLHF** — fine-tuning com feedback humano via reinforcement learning.

## Hierarquia de Abordagens (custo crescente)

```
Zero-shot → Few-shot ICL → Fine-tuning (LoRA) → Full fine-tuning → RLHF
```

## CoT Prompting vs Fine-Tuning

[[wiki/sources/chain-of-thought-prompting]] (Wei et al., 2022) mostrou que PaLM 540B com CoT few-shot supera GPT-3 fine-tuned com verificador no benchmark GSM8K (~57% vs ~35%) — sem nenhum gradient update. Isso reforça a hierarquia: tente CoT com modelo grande antes de partir para fine-tuning em tarefas de raciocínio.

## Fontes

- [[wiki/sources/gpt3-language-models-are-few-shot-learners]]
- [[wiki/sources/microsoft-prompt-engineering-guide]]
- [[wiki/sources/chain-of-thought-prompting]]
