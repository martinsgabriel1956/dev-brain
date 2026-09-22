---
type: concept
title: "Padrões Estruturais (GoF)"
aliases: ["structural patterns", "padrões estruturais", "structural-patterns"]
date_created: 2026-05-01
date_updated: 2026-09-08
source_count: 5
tags: [design-patterns, structural, gof, oop]
skill: tech-mentor-backend
status: stable
---

# Structural Patterns (Padrões Estruturais)

Uma das três categorias dos 23 padrões [[entities/gang-of-four]]. Tratam de **como objetos se relacionam e se compõem** para formar estruturas maiores — como Legos.

## Os 7 Padrões Estruturais GoF

| Padrão | Problema que resolve |
|---|---|
| [[adapter-pattern]] | Compatibiliza interfaces incompatíveis |
| [[facade-pattern]] | Interface simplificada sobre subsistema complexo |
| [[decorator-pattern]] | Adiciona comportamento sem alterar a classe |
| [[proxy-pattern]] | Controla acesso ao objeto real (cache, auth, lazy load) |
| Bridge | Separa abstração de implementação |
| [[composite-pattern|Composite]] | Trata objetos individuais e composições uniformemente |
| Flyweight | Compartilha estado para suportar grande número de objetos |

## Distinção de Criacionais

Padrões criacionais tratam de *como* objetos nascem. Padrões estruturais tratam de *como* eles se organizam e colaboram depois de existir.

## Key Sources

- [[wiki/sources/design-pattern-proxy]]
- [[sources/sete-padroes-de-design-de-software]]
- [[wiki/sources/design-pattern-facade-codigo-fonte-tv]]
- [[wiki/sources/decorator-xunitpatterns]] — xUnitPatterns.com (Meszaros) cita a definição original do GOF para o [[wiki/concepts/decorator-pattern|Decorator]]
- [[wiki/sources/clean-architecture-frontend-vue-diagrama-camadas-login]] — primeiro exemplo próprio de Composite na wiki (`ValidationComposite` agrupando validadores de formulário)
