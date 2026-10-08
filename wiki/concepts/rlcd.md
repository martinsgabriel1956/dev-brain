---
type: concept
title: "RLCD (Reinforcement Learning for Calibrated Decisions)"
aliases: ["rlcd", "calibrated decisions"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_count: 1
tags: [ia, treinamento, calibracao, rlcd]
skill: tech-mentor-ai
status: stub
---

# RLCD

Método de treino da [[wiki/entities/typesafe-ai]] para o [[wiki/entities/jev]]: o modelo é recompensado por **decidir certo e expressar corretamente a confiança**. Contrasta com RLHF, que otimiza respostas que humanos acham boas/úteis. Motivação: confiança auto-declarada por LLMs tende a ser inconsistente ou excessivamente confiante (alegação do fornecedor; ver [[wiki/concepts/alucinacao-llm]] sobre o incentivo de "chutar"). Permite que o código ramifique conforme a confiança ([[wiki/concepts/human-in-the-loop]] quando baixa).

## Key sources
- [[wiki/sources/jev-typesafe-ai-system-one-model-decisoes-tipadas-codigo-fonte-tv]]
