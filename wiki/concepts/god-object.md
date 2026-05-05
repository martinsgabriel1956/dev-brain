---
type: concept
title: "God Object"
aliases: ["god class", "objeto deus", "god object anti-pattern"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 2
tags: [anti-patterns, god-object, design-patterns, solid, coesao]
skill: tech-mentor-backend
status: stable
---

# God Object (Anti-pattern)

Classe ou objeto que sabe demais e faz demais. Concentra responsabilidades que deveriam estar distribuídas por múltiplas classes, violando o [[single-responsibility-principle]] e tornando o sistema difícil de testar, manter e estender.

## Sintomas

- Classe com centenas de métodos não relacionados entre si
- Toda alteração no sistema exige tocar nessa classe
- Nenhuma outra classe pode funcionar sem ela
- Difícil de testar isoladamente

## Relação com Facade

O [[facade-pattern]] tem risco explícito de virar um God Object se não houver disciplina:

> "Uma fachada pode se tornar um objeto deus acoplado a todas as classes de uma aplicação." — [[sources/design-pattern-facade]]

A diferença: uma Facade *bem feita* delega para o subsistema e não contém lógica própria. Quando começa a acumular lógica de negócio, vira God Object.

## Como resolver

- Aplicar [[single-responsibility-principle]]: cada classe com uma razão para mudar
- Extrair responsabilidades para classes especializadas
- Usar [[facade-pattern]] (com disciplina) ou [[mediator-pattern]] para coordenação

## Key Sources

- [[sources/design-pattern-facade]]
- [[sources/sete-padroes-de-design-de-software]]
