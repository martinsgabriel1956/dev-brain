---
type: concept
title: "Estado Global em Servidor"
aliases: ["global state", "estado global", "estado global no servidor"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [estado-global, stateless, backend, singleton, cache]
skill: tech-mentor-backend
status: draft
---

# Estado Global em Servidor

Estado mutável acessível por qualquer requisição de um processo servidor: cache in-memory (`Map`, Redis instanciado no processo), variável no topo de um módulo (módulos JS se comportam como [[wiki/concepts/singleton-pattern]]), config mutável, `currency`/`discount` fora de função ou numa classe compartilhada. Se uma requisição altera, altera para **todos os usuários**, o que quebra o princípio [[wiki/concepts/stateless]] do HTTP.

## Consequências

- Contaminação entre requests e dependência da **ordem das chamadas** (ver [[wiki/concepts/efeito-colateral]]).
- [[wiki/concepts/race-condition]] com requests paralelos.
- Bugs não reproduzíveis ([[wiki/concepts/reprodutibilidade-de-bugs]]).
- Bugs **sutis**: o exemplo óbvio (`currentUser`) é raro; o comum é `currency`/`discount` ou cache.

## Remédios

[[wiki/concepts/request-context]], estado local passado explicitamente ([[wiki/concepts/dependencia-externa-oculta]]), [[wiki/concepts/dependency-injection]]. Exceção: [[wiki/concepts/estado-global-inofensivo]].

Ver também [[wiki/concepts/estado-compartilhado]] (versão mais geral, sem foco em servidor).

## Key sources

- [[wiki/sources/estado-global-stateless-side-effects-reprodutibilidade-galego]]
