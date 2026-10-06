---
type: concept
title: "Análise Estática como Âncora de LLM"
aliases: ["static analysis grounding", "LLM sobre fatos determinísticos"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [llm, analise-estatica, alucinacao, grounding, legado]
skill: tech-mentor-ai
status: draft
---

# Análise Estática como Âncora de LLM

Padrão: uma ferramenta **determinística** extrai fatos do código (estrutura, dependências, uso de dados) e o LLM só **explica/sintetiza** esses fatos, em vez de ler o código cru. O contexto restrito reduz [[wiki/concepts/alucinacao-llm]]; o LLM contribui com a linguagem humana que técnicos e negócio entendem.

No [[wiki/entities/california-dmv]]: [[wiki/entities/ibm-arc]] (estática) → [[wiki/entities/watsonx]] (LLM) → revisão humana. Segundo a fonte ([[wiki/sources/dmv-california-ia-descoberta-regras-negocio-mainframe-cobol]]), isso eliminou "boa parte" das alucinações, mas não todas — por isso o ciclo de [[wiki/concepts/human-in-the-loop]]. Sem métrica publicada (lacuna).

Por que importa: o LLM é probabilístico e pode ser coerente e errado; o fato determinístico dá algo verificável para o revisor comparar. Aplicação ao [[wiki/concepts/descoberta-de-regras-de-negocio-legado]]. Ligação com a ideia de verificadores determinísticos em IA é **inferência minha**.

## Key sources

- [[wiki/sources/dmv-california-ia-descoberta-regras-negocio-mainframe-cobol]]
