---
type: concept
title: "Bridge Pattern"
aliases: ["bridge", "ponte"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 1
tags: [design-patterns, structural, bridge, gof, composicao]
skill: tech-mentor-backend
status: stub
---

# Bridge Pattern

Padrão [[structural-patterns|estrutural]] que divide uma classe grande ou um conjunto de classes relacionadas em duas hierarquias separadas — **abstração** e **implementação** — que podem ser desenvolvidas independentemente.

## Mecanismo

Em vez de herança múltipla, usa composição: a abstração contém uma referência à implementação e delega para ela. Ambas as hierarquias crescem de forma independente.

## Distinção do Strategy

Bridge e [[strategy-pattern]] têm estrutura similar (composição + delegação), mas propósitos diferentes:

| | Bridge | [[strategy-pattern]] |
|---|---|---|
| Propósito | Separar abstração de implementação para evitar explosão de subclasses | Tornar algoritmos intercambiáveis em runtime |
| Quando projetar | Na fase de design (estrutural) | Quando há variação comportamental |

## Quando usar

- Quando você quer evitar vínculo permanente entre abstração e implementação
- Quando ambas devem ser extensíveis por subclasses independentemente
- Exemplo clássico: formas geométricas × mecanismos de renderização (SVG, Canvas, OpenGL)

## Key Sources

- [[sources/design-pattern-strategy]] — mencionado nas relações como padrão de estrutura similar
