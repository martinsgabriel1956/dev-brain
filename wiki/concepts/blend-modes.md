---
type: concept
title: "Blend modes (modos de mesclagem)"
aliases: ["blend mode", "modos de mesclagem", "modo de mesclagem", "mix-blend-mode", "background-blend-mode", "color dodge", "lighten", "screen", "multiply", "overlay", "difference"]
date_created: 2026-11-13
date_updated: 2026-11-22
source_count: 5
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

## Overlay para tingir neutros

Na aula prática de cores, o overlay da cor de base sobre o branco e o preto tinge os neutros; no preto, a saturação sobe demais e ele baixa a opacidade para 50% e 10% ([[wiki/sources/paleta-de-cores-na-pratica-dribbble-hsb-variacoes-cores-neutras]]). Ver [[wiki/concepts/neutros-tingidos]]. `[external]` Sobre FFFFFF puro o overlay não muda nada (https://www.w3.org/TR/compositing-1/#blendingoverlay); funciona porque o branco de partida é F1/F2.

## Luminosity para ler o brilho das cores

Na aula de variação de cores, uma barra com o ciclo cromático muda de pass-through para luminosity e vira escala de cinza: o brilho de cada matiz fica visível (amarelo 89%, azul 11%) ([[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]]). Ver [[wiki/concepts/luminosidade-das-cores]]. `[external]` No modo luminosity, a camada cede só a luminosidade e mantém matiz e saturação do que está embaixo; sobre fundo neutro, sobra o cinza.

## Ruído em overlay (FrontPUSH, mentoria de ID visual)

Na [[wiki/sources/frontpush-mentoria-identidade-visual-marca-minimalista-gradiente-paleta-tipografia|mentoria de identidade visual]], a textura granulada do style guide do FrontPUSH: plugin Noise da Figma Community, camada em overlay (mais clara que Pass-through), opacidade de 20% a 30%, sempre por cima e com a layer travada. "Dá um requinte."

## Key Sources

- [[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]] — máscara com gradiente radial, color dodge e lighten para tirar o fundo preto, wallpapers do FrontPUSH
- [[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]] — as outras camadas da ambiência do FrontPUSH
- [[wiki/sources/paleta-de-cores-na-pratica-dribbble-hsb-variacoes-cores-neutras]] — overlay da cor de base sobre branco e preto
- [[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]] — modo luminosity revela o brilho de cada matiz
- [[wiki/sources/frontpush-mentoria-identidade-visual-marca-minimalista-gradiente-paleta-tipografia]]: plugin Noise em overlay, 20–30% de opacidade
