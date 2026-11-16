---
type: concept
title: "Círculo cromático"
aliases: ["roda de cores", "color wheel", "disco cromático", "círculo de cores", "RYB", "círculo de Itten"]
date_created: 2026-11-14
date_updated: 2026-11-14
source_count: 1
tags: [ui, ui-design, cor, circulo-cromatico, harmonia-de-cores, ryb, rgb, hsl]
skill: ux-ui-mentor
status: stub
---

# Círculo cromático

As matizes dispostas em círculo. Tudo que a [[wiki/concepts/harmonia-de-cores]] define é posição nele: opostas (complementar), vizinhas (análoga), triângulo equidistante (triádica). "Muito da harmonia das cores, que a gente faz o estudo no círculo cromático, responde muito dos nossos questionamentos" ([[wiki/sources/harmonia-das-cores-monocromatica-complementar-analoga-triadica]]).

O slide da aula mostra um círculo de 12 fatias com pontos marcando cada harmonia; a ferramenta usada é o [[wiki/entities/adobe-color]].

## Dois círculos, opostos diferentes

`[external]` Existem dois círculos em uso, e eles discordam sobre o que é oposto:

| Círculo | Base | Pares opostos | Onde aparece |
|---|---|---|---|
| RYB (pigmento, de artista) | vermelho, amarelo, azul | vermelho/verde, **azul/laranja**, amarelo/roxo | ensino de arte; círculo de 12 matizes de Itten, descrito pela Adobe (https://www.adobe.com/express/learn/blog/color-wheel-explained) |
| RGB/HSL (luz, de tela) | vermelho, verde, azul | vermelho/ciano, verde/magenta, **azul/amarelo** | CSS `hsl()`, girar a matiz em 180° |

O azul ↔ laranja da aula é o par do RYB. Num seletor de cor HSL, somar 180° ao azul puro (240°) dá amarelo (60°). Para quem implementa: "complementar" depende do modelo, e a ferramenta precisa estar clara sobre qual usa.

## Saturação e o "feixe"

No Adobe Color, aproximar os pontos do centro dá "tons mais pastéis"; afastar satura e deixa as cores "mais presentes, mais puras". Arrastar os pontos estreita ou abre o "feixe" das análogas.

## Key Sources

- [[wiki/sources/harmonia-das-cores-monocromatica-complementar-analoga-triadica]] — base de todas as harmonias da aula
