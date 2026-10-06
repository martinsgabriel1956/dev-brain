---
type: question
title: "ACL: Facade vs. Adapter e uma camada por consumidor, critérios divergentes"
aliases: []
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 2
tags: [anti-corruption-layer, facade-pattern, adapter-pattern, open-host-service]
skill: tech-mentor-backend
status: draft
---

# ACL: critérios divergentes

1. **Facade vs. Adapter.** [[wiki/sources/anti-corruption-layer-microsservicos-requisitos-arquiteturais]]: Facade no lado do legado (interface estável), Adapters no lado dos microsserviços (versões, parametrização, 1..N chamadas). `[skill: tech-mentor-backend]`: Adapter traduz uma interface; Facade orquestra várias chamadas ([[wiki/concepts/anti-corruption-layer]]). Provavelmente eixos diferentes (posição vs. função); sem fonte que reconcilie.
2. **N consumidores.** Fonte: uma ACL por subsistema, mesmo duplicando código. Skill: Open Host Service + Published Language no legado. Escolha depende de quanto o legado pode ser alterado; não resolvido.

## Key sources

- [[wiki/sources/anti-corruption-layer-microsservicos-requisitos-arquiteturais]]
- [[wiki/sources/anti-corruption-layer-facade-adapter-sistema-legado]]
