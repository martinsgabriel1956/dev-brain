---
type: entity
title: "Figma"
aliases: ["figma.com"]
date_created: 2026-04-22
date_updated: 2026-07-21
source_count: 2
tags: [figma, design, ferramenta, design-first]
skill: tech-mentor-frontend
status: stub
---

# Figma

Ferramenta de design colaborativo baseada em browser. Principal ferramenta da abordagem [[design-first]].

## Papel por abordagem

| Abordagem | Papel do Figma |
|---|---|
| Design First | Fonte de verdade — tudo começa aqui |
| Code First | Pouco ou nenhum uso |
| Design Engineer | Ferramenta de teste e validação, não fonte de verdade |

## Risco em times pequenos

Em times onde a mesma pessoa faz design e código, o Figma tende a ficar desatualizado conforme o código evolui — ver [[design-first]].

## Como ponto intermediário de um pipeline com IA

Fluxo observado: ferramenta de geração de UI por IA (ex.: [[wiki/entities/ux-pilot]]) gera o conceito de UI/UX → exporta para o Figma → o Figma é conectado, via MCP, a uma IA de código (Cursor, Claude Code) para implementação. Nesse pipeline, o Figma deixa de ser o ponto de partida (como no design-first clássico) e passa a ser um artefato intermediário de handoff entre a ferramenta de concepção e a IA de implementação.

## Key Sources

- [[wiki/sources/design-first-vs-code-first-referencias]]
- [[wiki/sources/5-boas-praticas-uiux-ux-pilot]]
