---
type: concept
title: "Perguntas Tipadas: choice, score, no"
aliases: ["choice score no", "typed questions"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_count: 1
tags: [ia, decisoes-tipadas, api, jev]
skill: tech-mentor-ai
status: draft
---

# Perguntas tipadas: choice, score, no

Três primitivas da API do [[wiki/entities/jev]] ([[wiki/concepts/system-one-model]]), enviadas junto com um **state** (só o contexto necessário) e avaliadas em paralelo na mesma chamada:

- **choice**: lista fechada de opções (qual time atende?), só escolhe entre as enviadas.
- **score**: valor numa escala conforme um critério (nível de frustração do cliente).
- **no** (`[external]` "noul"): sim/não como probabilidade (chamado urgente?).

Resposta: valor + `probabilities` + `confidence`, já no tipo do programa. Anatomia: state → questions → answers.

## Key sources
- [[wiki/sources/jev-typesafe-ai-system-one-model-decisoes-tipadas-codigo-fonte-tv]]
