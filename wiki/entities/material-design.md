---
type: entity
title: "Material Design"
aliases: ["Material", "Material Design 2", "Material Design 3", "M2", "M3"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 5
tags: [design-system, google, diretrizes, imagens, acessibilidade]
skill: ux-ui-mentor
status: stub
---

# Material Design

Sistema de design do [[wiki/entities/google]], com diretrizes, componentes e código aberto. [[wiki/entities/nasser|Násser]] recomenda as diretrizes de imagem ("images material design") como complemento das aulas de [[wiki/concepts/imagens-em-interfaces|imagens]]: reiteram o [[wiki/concepts/ponto-focal-em-fotografia|ponto focal]] (com exemplos de certo e errado), o [[wiki/concepts/aspect-ratio]] (16:9, 3:4, 1:1) e o [[wiki/concepts/texto-alternativo]] ("seja acessível") ([[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]]).

Não verificado: a página de imagens do Material 2 (https://m2.material.io/design/communication/imagery.html) não exibe mais o conteúdo, e a do Material 3 (`/styles/images/overview`) dá 404 (2026-11-13). As afirmações acima são as da aula.

## Iconografia

Násser recomenda a página de iconografia: ícones de sistema "simple, modern, friendly and sometimes quirky", sem detalhe demais, geométricos, com templates e tamanhos padronizados ([[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]]). A página do M2 não traz o texto no HTML estático e não foi conferida.

## Tamanhos e grid de ícones

Na parte 2 ([[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]]), Násser cita "System icons are displayed 24 por 24" e a área útil de 20×20, mas não segue ao pé da letra (56 e 32; círculo mais folgado). `[external]` Conferido no M3: 24dp, live area 20dp com 2dp de padding, tamanhos 20/24/40/48dp, keylines de quadrado 18, círculo 20, retângulos 16×20 e 20×16, stroke de 2dp (https://m3.material.io/styles/icons/designing-icons, 2026-11-13). Ver [[wiki/concepts/grid-de-icones]].

## Ícones retos (parte 3)

Em [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]], Násser indica a documentação e diz que os ícones do Material são "bem mais retos que os meus", sem arredondado na ponta. `[external]` Vale para o estilo Sharp do Material Symbols, que também tem Outlined e Rounded (https://fonts.google.com/icons).

## Key Sources

- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]] — diretrizes de imagem recomendadas no fim da aula
- [[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]] — página de iconografia: simple, modern, friendly
- [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]] — 24×24, área útil 20×20, margem (conferido no M3)
- [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]] — documentação recomendada; ícones "bem retinhos"
- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]] — plugin Material Design Icons no Figma
