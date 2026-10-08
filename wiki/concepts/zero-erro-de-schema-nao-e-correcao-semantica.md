---
type: concept
title: "Zero Erro de Schema ≠ Correção Semântica"
aliases: ["schema valido nao e correto"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_count: 1
tags: [ia, validacao, alucinacao, confianca]
skill: tech-mentor-ai
status: draft
---

# Zero erro de schema ≠ correção semântica

"Zero erro de schema" garante que o valor respeita o tipo, **não** que a decisão está certa: uma resposta pode ser estruturalmente válida e semanticamente errada. O mesmo vale para [[wiki/concepts/saida-estruturada-llm]]. O ganho do [[wiki/entities/jev]] é expor **probabilidade e confiança** para o código tratar baixa confiança (revisão, fallback, [[wiki/concepts/human-in-the-loop]]), o que mitiga, mas não elimina, [[wiki/concepts/alucinacao-llm]]. Confiança calibrada é alegação do fornecedor ([[wiki/concepts/rlcd]]).

## Key sources
- [[wiki/sources/jev-typesafe-ai-system-one-model-decisoes-tipadas-codigo-fonte-tv]]
