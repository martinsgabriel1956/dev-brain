---
type: concept
title: "Blend modes (modos de mesclagem)"
aliases: ["blend mode", "modos de mesclagem", "modo de mesclagem", "mix-blend-mode", "background-blend-mode", "color dodge", "lighten", "screen", "multiply", "overlay", "difference"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 2
tags: [ui-design, imagens, figma, composicao-de-imagens, blend-modes, css, gradiente]
skill: ux-ui-mentor
status: stub
---

# Blend modes

Regra que define como a cor de uma camada se combina com a cor do que está embaixo dela. No [[wiki/entities/figma]], [[wiki/entities/nasser|Násser]] usa os modos para compor imagens sem abrir o Photoshop: "isso aqui é literalmente experimentação" ([[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]]).

## Como o autor usa

- **Integrar uma foto a um fundo:** máscara com gradiente radial na foto, depois um modo (color dodge, overlay, soft light, hard light, difference) e gradientes ao redor.
- **Tirar o fundo preto:** foto de alto contraste com fundo preto puro (comum no [[wiki/entities/unsplash]]) em **lighten** ou **color dodge** some o preto, "como se fosse um PNG". Foi a receita dos wallpapers do [[wiki/entities/frontpush]], com temperatura puxada para o azul.
- **Escolher a foto pela temperatura:** fotos quentes (fogo, laranja) destoam num fundo azul com color dodge; difference funcionou melhor.
- **Os que mais usa:** lighten, screen, color dodge, overlay, difference, darken, multiply.

## Por que o preto some

`[external]` Na especificação W3C de compositing, cada modo é uma função da cor de cima (camada) e da de baixo (fundo), por canal, de 0 a 1 (https://www.w3.org/TR/compositing-1/):

| Modo | Fórmula (simplificada) | Cor neutra da camada |
|---|---|---|
| multiply | fundo × camada | branco |
| darken | min(fundo, camada) | branco |
| screen | 1 − (1 − fundo)(1 − camada) | preto |
| lighten | max(fundo, camada) | preto |
| color dodge | fundo ÷ (1 − camada) | preto |
| difference | \|fundo − camada\| | preto |
| overlay | multiply ou screen conforme o fundo | depende do fundo |

Cor neutra é a que deixa o fundo como está. Por isso o preto "desaparece" nos modos de clarear e no difference, e o branco desaparece em multiply e darken. Preto granulado ou acinzentado não é neutro e deixa marca, o que explica o fundo granulado que "não ficou muito bom" na aula.

## No código

`[external]` Os mesmos modos existem em CSS: `mix-blend-mode` mescla um elemento com o que está atrás dele, e `background-blend-mode` mescla camadas de `background` entre si (https://developer.mozilla.org/en-US/docs/Web/CSS/mix-blend-mode). Para um wallpaper estático, exportar a composição pronta costuma ser mais barato que mesclar em tempo real.

## Ver também

- [[wiki/concepts/imagens-em-interfaces]]
- [[wiki/concepts/texto-sobre-imagem]] (o outro uso de gradiente sobre foto)
- [[wiki/concepts/contraste]]

## Parente: elementos de composição

Os wallpapers feitos com blend modes são uma das camadas de ambiência do FrontPUSH; a aula de [[wiki/concepts/elementos-de-composicao]] mostra as outras (layer blur, preenchimento radial, estrelas) ([[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]]).

## Key Sources

- [[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]] — máscara com gradiente radial, color dodge e lighten para tirar o fundo preto, wallpapers do FrontPUSH
- [[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]] — as outras camadas da ambiência do FrontPUSH
