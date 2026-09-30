---
type: concept
title: "Zero Data Retention (ZDR)"
aliases: ["zdr","retenção zero de dados","data retention llm"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [tech-mentor-ai, privacidade, lgpd, llm, openrouter, compliance]
skill: tech-mentor-ai
status: stub
---

# Zero Data Retention (ZDR)

Política em que o provedor de LLM não armazena prompts/respostas. Em [[wiki/sources/openrouter-como-profissional-provedores-quantizacao-retencao-fallback-ronald-hulk]]: sem política declarada ("no retention" ausente) não se sabe se o dado é guardado; um provedor com ZDR (exemplo mostrado: Together AI) permite justificar a solução ao cliente e apoiar conformidade com a [[wiki/concepts/lgpd]], "protegido por contrato".

No payload da [[wiki/entities/openrouter]]: `data_collection: "deny"` evita provedores que possam armazenar dados; `zdr: true` restringe a endpoints ZDR [external: https://openrouter.ai/docs/features/provider-routing]. Pode haver sobrepreço — razão pela qual preço é o último critério ([[wiki/concepts/criterios-de-selecao-de-provedor-llm]]).

Ressalva: o contrato/DPA do provedor é que vale; a flag não substitui leitura dos termos.

Relacionados: [[wiki/concepts/data-residency]], [[wiki/concepts/pool-de-provedores-llm]].

## Key sources

- [[wiki/sources/openrouter-como-profissional-provedores-quantizacao-retencao-fallback-ronald-hulk]]
