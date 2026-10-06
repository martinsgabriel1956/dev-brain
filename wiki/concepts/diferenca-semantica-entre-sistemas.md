---
type: concept
title: "Diferença semântica entre sistemas (quando não usar ACL)"
aliases: ["gap semântico legado novo", "versão intermediária de migração"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [anti-corruption-layer, semantica, migracao, ddd, strangler-fig]
skill: tech-mentor-backend
status: stub
---

# Diferença semântica entre sistemas (quando não usar ACL)

Principal contraindicação à [[wiki/concepts/anti-corruption-layer]] segundo [[wiki/sources/anti-corruption-layer-microsservicos-requisitos-arquiteturais]] (que diz ter visto na literatura): quando a **semântica** dos dois sistemas é muito diferente. Exemplo: legado modular orientado a **linhas de negócio (LOBs)**; sistema novo orientado a **jornadas** e domínios. Traduzir entre estruturas de negócio tão distintas dói, e até o [[wiki/concepts/strangler-fig-pattern|Strangler]] fica difícil; pode valer mais "tombar" tudo.

Exceções em que vale: existe uma **versão intermediária** semanticamente mais próxima (desliga-se o legado e só depois se faz a mudança semântica final); ou vários temas com semânticas diferentes precisam conversar. Em planejamento de migração por etapas, o autor diz que "na maioria dos casos vale".

Relação com a tradução de vocabulário do [[wiki/concepts/context-map]] é inferência minha. Critério complementar: [[wiki/concepts/acl-requisitos-arquiteturais]].

## Key sources

- [[wiki/sources/anti-corruption-layer-microsservicos-requisitos-arquiteturais]]
