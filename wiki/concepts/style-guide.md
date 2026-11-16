---
type: concept
title: "Style guide"
aliases: ["guia de estilo", "styleguide", "style guide de interface", "mapa de design"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [ui, ui-design, style-guide, design-system, documentacao, handoff, figma, css]
skill: ux-ui-mentor
status: stub
---

# Style guide

Documento que fixa os padrões visuais de um projeto (estilos de texto, cor e efeito, dimensões, radius, estados) para que o design fique consistente no arquivo de design e na implementação. Em [[wiki/sources/style-guide-pratica-parte-2-documentacao-para-dev-sombra-gradiente-estados]], o objetivo é "consistência tanto no Figma, tanto na documentação", e o style guide é "o mapa que traduz o design para o CSS". Ver [[wiki/concepts/consistencia-visual]].

## No Figma

A aula 15 do curso (não ingerida) cria três tipos de estilo no [[wiki/entities/figma]]: texto, cor e efeito. A aula 16 parte deles para a documentação voltada ao desenvolvedor ([[wiki/concepts/handoff-design-dev]]).

## O que entra

Segundo a aula 16:

- **Sempre:** gradiente (ângulo e paradas), camadas de `box-shadow` ([[wiki/concepts/sombra-em-interfaces]]), cor em RGBA e hexadecimal, [[wiki/concepts/border-radius]] por tamanho de componente.
- **Quando importa:** dimensões e padding. No botão, padding em vez de largura fixa ([[wiki/concepts/botoes-em-interfaces]]).
- **Não entra:** o `position` gerado pelo Figma; o layout vai para flexbox e grid.
- **Estados de cada módulo:** normal, hover e clicável ([[wiki/concepts/feedback-do-sistema]], [[wiki/concepts/maquina-de-estados-ui]]).

## Style guide e design system

`[skill: ux-ui-mentor]` Um style guide documenta a linguagem visual; um design system junta essa linguagem a componentes reutilizáveis, tokens com nome e regras de uso, mantidos como produto. O style guide da aula está no meio do caminho: tem estilos e estados, mas valores sem nome de token. Ver [[wiki/concepts/mobile-design-system]] para tokens em camadas.

## Key Sources

- [[wiki/sources/style-guide-pratica-parte-2-documentacao-para-dev-sombra-gradiente-estados]]: objetivo do style guide, o que documentar, três estados, "mapa de design"
- [[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]]: hover a documentar "muito bem claro no meu style guide"; style guide para download prometido
- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]]: seção de style guide para ícones próprios prometida
