---
type: concept
title: "SVG (Scalable Vector Graphics)"
aliases: ["svg", "scalable vector graphics", "imagem vetorial", "vector image"]
date_created: 2026-07-29
date_updated: 2026-11-13
source_count: 12
tags: [formatos-de-imagem, svg, vetorial, frontend]
skill: cs-fundamentals
status: stub
---

# SVG

Formato criado pelo W3C em 2001, estruturalmente diferente de todos os formatos raster (JPEG, PNG, GIF, WebP, HEIC, AVIF). Em vez de armazenar uma grade de pixels, armazena **instruções matemáticas** — linhas, curvas, formas geométricas e preenchimentos. É essencialmente uma "receita de desenho" em vez de uma foto do resultado já pronto.

## Por que isso importa

Como o conteúdo é reconstruído a partir de equações, um SVG pode ser ampliado infinitamente sem perda de nitidez — o mesmo arquivo serve para um ícone de 32px ou para um outdoor. É por isso que a maioria dos sites modernos usa SVG para logotipos, ícones e elementos de interface: ocupa pouco espaço e se adapta a qualquer resolução de tela sem precisar de múltiplos assets por densidade de pixel.

## Ver também

- [[wiki/concepts/formato-png]], [[wiki/concepts/formato-jpeg]] — contraponto raster: pixels fixos, escala com perda de nitidez

## Na prática de UI

[[wiki/entities/nasser|Násser]] manda usar SVG para ícones, ilustrações e backgrounds, e reserva a fotografia realista para formatos raster. Demonstração no [[wiki/entities/figma]]: um ícone de 64×64 escalado para 96 mantém as proporções, e o SVG exportado, aberto no VS Code, é "somente alguns números" num plano cartesiano, um arquivo de bytes. No [[wiki/entities/frontpush]] todas as animações são SVG ([[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]]).

Na parte 2, ele chama ícone em PNG de "modelo mais arcaico": se dá para fazer no Figma e não é foto realista, vetorize, "principalmente logo"; logo de cliente em baixa definição se refaz com a Pen Tool ([[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]]).

`[skill: ux-ui-mentor]` Trade-off de implementação: SVG inline renderiza no navegador junto do HTML; via `<img>` ganha cache.

## Ilustrações e cor da marca

Na parte 4, SVG é "o formato mais adequado para ilustrações" e "imprescindível" porque permite trocar as cores: no [[wiki/entities/undraw]], o hexadecimal da marca recolore todas as ilustrações ([[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]]). Ver [[wiki/concepts/ilustracoes-em-interfaces]].

## Tamanho de ícone

Na parte 2 da aula de ícones ([[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]]): "o tamanho não é a coisa que mais importa" porque o ícone "deve ser exportado como SVG" e o vetor escala; pode desenhar em 24×24 e usar em 56. Ressalva: o Material 3 pede desenhar para 100% e oferece tamanhos ópticos (20, 24, 40, 48dp), porque o stroke escala junto (inferência do agente; https://m3.material.io/styles/icons/designing-icons).

## Caminhos manipuláveis por CSS e motion

Para [[wiki/entities/nasser|Násser]], SVG é "o grande queridinho" e "só alegria": não perde resolução, é leve e cada elemento é um caminho separado que o CSS manipula. Quase todas as ilustrações e animações dele (site, landing page, criações do FrontPUSH no Instagram) são SVG, com o caminho já traçado no Figma pensando na animação ([[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]]). `[external]` O CSS da página só alcança os `<path>` com o SVG inline; via `<img>` ou `background-image` ele é opaco.

## O SVG por dentro

Na edição "W7", [[wiki/entities/nasser|Násser]] abre no VS Code um mockup exportado do Figma (2KB): `defs` com o gradiente linear, filtros "inclusive de sombra" configurados via código, um ID ("paint-linear") aplicado aos caminhos (círculos, retângulos) e preenchimentos em hex. "Por isso que é leve", e por ter tags o CSS manipula: "a magia do Motion surgiu daqui" ([[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]]). `[external]` Filtros SVG são rasterizados pelo navegador e custam mais que caminhos simples.

## Vetorizar à mão

Na edição "W7", [[wiki/entities/nasser|Násser]] mostra que os ícones animados dele são vetores traçados no Figma com a [[wiki/concepts/vetorizacao-com-pen-tool|Pen Tool]] e a Bend Tool sobre uma imagem de referência, com o mínimo de pontos, e depois exportados "tudo, tudo, tudo para SVG" ([[wiki/sources/imagens-e-ilustracoes-vetorizar-icones-figma-pen-tool-bend-tool]]).

## Legibilidade de ícones

Na aula teórica de ícones "W7" ([[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia]]), o SVG é metade da legibilidade (a outra é a simplicidade): o ícone "pode ser colocado em vários tamanhos e resoluções diferentes" sem perder resolução.

## Key Sources

- [[wiki/sources/historia-dos-formatos-de-imagem]]
- [[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]] — SVG para ícones, ilustrações e backgrounds; ícone escalado no Figma
- [[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]] — ícone em SVG em vez de PNG; vetorizar logo de cliente com a Pen Tool
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]] — SVG para ilustrações; recolorir com o hexadecimal da marca
- [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]] — ícone em SVG escala, então o tamanho de desenho importa pouco
- [[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]] — SVG como base do motion do autor; caminhos manipuláveis por CSS
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-compreensao-consistencia-svg-tinyimage]] — preferir sites que exportam SVG; recolorir no unDraw com o hex da marca
- [[wiki/sources/imagens-e-ilustracoes-pratica-figma-importar-editor-plugins-exportacao]] — plugin de ondas que gera SVG; export de ícone dentro de frame
- [[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]] — SVG por dentro: defs com gradiente linear e filtros de sombra, ID aplicado aos caminhos, hex; manipulável por CSS; mockup exportado com 2KB
- [[wiki/sources/imagens-e-ilustracoes-vetorizar-icones-figma-pen-tool-bend-tool]] — vetorizar ícone de telefone com Pen Tool e Bend Tool e exportar em SVG
- [[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia]] — ícone legível = simples + SVG
- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]] — Feather exporta SVG ("sempre isso é muito bom"); ícone do módulo "propriedade do SVG"
