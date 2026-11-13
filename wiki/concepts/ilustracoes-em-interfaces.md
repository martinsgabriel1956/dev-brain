---
type: concept
title: "Ilustrações em interfaces"
aliases: ["ilustração em UI", "ilustrações", "illustration", "ilustração vetorial", "família de ilustrações"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 8
tags: [ui, ui-design, elementos-da-interface, ilustracoes, svg, onboarding, consistencia, identidade-visual]
skill: ux-ui-mentor
status: stub
---

# Ilustrações em interfaces

Desenho (em geral vetorial) usado na UI para informar, conduzir e ambientar. Irmã da fotografia em [[wiki/concepts/imagens-em-interfaces]]: "muitos dos conceitos que eu falei para imagens se aplicam também a ilustrações" ([[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]]).

## Para que serve

Segundo [[wiki/entities/nasser|Násser]], a ilustração:

- passa informação e indica ao usuário o que fazer;
- conduz o usuário numa parte da jornada (onboarding);
- complementa o texto, traz ambientação e reconhecimento;
- preenche o [[wiki/concepts/espaco-em-branco]] de telas com pouco texto e "comunica com o texto";
- cria identidade, sobretudo na forma de [[wiki/concepts/mascote-de-marca|mascote]].
- ajuda na compreensão do conteúdo: seções como "o que fazemos" ou "workflow" vêm com texto de um lado e ilustração do outro ([[wiki/sources/imagens-e-ilustracoes-ilustracoes-compreensao-consistencia-svg-tinyimage]]).

Tipos citados: ilustrações de pessoas e de mascotes.

## Regras práticas

| Regra | Página |
|---|---|
| Formato: SVG; dá para fazer no Figma | [[wiki/concepts/formato-svg]] |
| Uma família de ilustrações, mesmo traço; não misturar sites | [[wiki/concepts/consistencia-visual]] |
| Trocar as cores para as da marca (ex.: [[wiki/entities/undraw]]) | [[wiki/concepts/harmonia-visual]] |
| Conferir a licença de uso de cada biblioteca | [[wiki/concepts/banco-de-imagens]] |
| Texto de um lado, ilustração do outro, em hero e em apps | [[wiki/concepts/wireframe]] |
| Texto alternativo quando informa | [[wiki/concepts/texto-alternativo]] |
| Fundo em escala de cinza, destaque só na cor da marca (onde vai o motion) | [[wiki/concepts/contraste]] |

Bibliotecas citadas: [[wiki/entities/humaaans]], [[wiki/entities/undraw]], Free Illustrations.

"Designer e ilustrador são duas coisas diferentes": ninguém precisa ilustrar do zero, basta escolher bem a família.

## Olhar de dev

`[skill: ux-ui-mentor]` Ilustração aparece nos padrões de empty state (first-run: "mostre o que o produto parece com dados") e de página de erro ("ilustração com personalidade"); animações de ilustração ou hero ficam em 500–800 ms, com Lottie como formato comum. `[external]` Recolorir SVG em código é trivial quando o desenho usa `fill="currentColor"` ou variáveis CSS: a cor da marca vira token, sem exportar uma versão por tema.

## Ícones

A regra de família vale também para ícones: "foi o mesmo cara que fez com o mesmo traço" ([[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]]). Ver [[wiki/concepts/familia-de-icones]].

## Empty screens

Ilustrações são uma das formas de compor telas vazias, ao lado de elementos da natureza e outros [[wiki/concepts/elementos-de-composicao]] ([[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]]). Ver [[wiki/concepts/empty-state]].

## Ferramentas no Figma

Na prática "W7", as ilustrações do site do autor saem de plugins: Blobs para bolhas de composição, plugins de [[wiki/concepts/ilustracao-isometrica|isometria]] e um gerador de ondas em SVG ([[wiki/sources/imagens-e-ilustracoes-pratica-figma-importar-editor-plugins-exportacao]]).

## Ilustração é um conjunto de formas

"O grande pulo do gato": uma ilustração do [[wiki/entities/undraw]] em SVG é só formas, toda editável no Figma; dá para trocar a cor, pegar trechos ou construir a sua com retângulos e [[wiki/concepts/operacoes-booleanas-em-formas|operações booleanas]], como o mockup de iPhone de [[wiki/entities/nasser|Násser]] ([[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]]).

## Traçar sobre uma referência

Quando a forma não sai de retângulos e booleanas, traça-se: Pen Tool nos pontos onde reto vira curvo, Bend Tool para arredondar, alças para refinar. "É paciência, é a grande realidade" ([[wiki/sources/imagens-e-ilustracoes-vetorizar-icones-figma-pen-tool-bend-tool]]; ver [[wiki/concepts/vetorizacao-com-pen-tool]]).

## Key Sources

- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]] — aula de ilustrações: SVG, mascotes, consistência, cor da marca
- [[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]] — a regra de família de ilustrações estendida a ícones
- [[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]] — ilustração para compor empty screens
- [[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]] — abertura da edição "W7": ilustrações em SVG como base do motion; slide lista compreensão, consistência, plugins do Figma e licença
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-compreensao-consistencia-svg-tinyimage]] — aula de ilustrações da edição "W7": compreensão do conteúdo; fundo cinza com destaque na cor da marca; uma biblioteca só
- [[wiki/sources/imagens-e-ilustracoes-pratica-figma-importar-editor-plugins-exportacao]] — prática da edição "W7": plugins Blobs, isométricos, ondas e "skill-depth"
- [[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]] — ilustração é um conjunto de formas: editar trechos do unDraw ou construir a sua (mockup de iPhone)
- [[wiki/sources/imagens-e-ilustracoes-vetorizar-icones-figma-pen-tool-bend-tool]] — traçar a forma sobre uma imagem com Pen Tool e Bend Tool
