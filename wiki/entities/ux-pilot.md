---
type: entity
title: "UX Pilot"
aliases: ["uxpilot", "ux pilot ai"]
date_created: 2026-07-21
date_updated: 2026-07-21
source_count: 1
tags: [ux-pilot, design, ferramenta, design-first, figma]
skill: tech-mentor-frontend
status: stub
---

# UX Pilot

Ferramenta de geração de UI/UX assistida por IA. Gera conceitos de interface (telas completas ou wireframes) a partir de prompts, permite selecionar seções específicas de um design para refinar iterativamente, e exporta o resultado para o [[wiki/entities/figma]] — de onde se conecta, via MCP do Figma, a uma IA de código (Cursor, Claude Code) para implementação.

## Fluxo de uso típico

```
Prompt → UX Pilot (conceito de UI/UX ou wireframe)
       → export → Figma
       → MCP do Figma → IA de código (Cursor / Claude Code)
       → implementação
```

## Características citadas

- Modo de imagem/UI completa e modo wireframe (blocos e posicionamento, sem estilo visual).
- Permite anexar um print como referência visual ("attach image with context") — mas a ferramenta tende a herdar cores e fontes desse print, então evitar usá-lo como referência quando o objetivo é fugir do estilo da versão anterior.
- Permite selecionar apenas uma seção da tela para reprocessar, preservando o restante do design já aprovado.
- Créditos gratuitos disponíveis para testes antes de decidir pela versão paga.

## Papel no fluxo Design First

Funciona como ferramenta de concepção de UI/UX que antecede o Figma — um passo a mais antes do fluxo clássico de [[wiki/concepts/design-first]], no qual o Figma passa a ser o artefato de exportação e handoff, não o ponto de partida.

## Key Sources

- [[wiki/sources/5-boas-praticas-uiux-ux-pilot]]
