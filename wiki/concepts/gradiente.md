---
type: concept
title: "Gradiente"
aliases: ["gradientes", "degradê", "gradient", "bad gradient", "gradiente ruim", "gradiente monocromático", "gradientes suaves"]
date_created: 2026-11-22
date_updated: 2026-11-22
source_count: 1
tags: [ui-design, design, cor, gradiente, harmonia-de-cores, circulo-cromatico, matiz, oklch, css]
skill: ux-ui-mentor
status: stub
---

# Gradiente

Transição contínua entre duas ou mais cores. A wiki tratava gradiente dentro de [[wiki/concepts/harmonia-de-cores]] (seção "Análoga e gradiente"); a mentoria de identidade visual do FrontPUSH ([[wiki/sources/frontpush-mentoria-identidade-visual-marca-minimalista-gradiente-paleta-tipografia]]) dá regras próprias.

## O "bad gradient"

Para [[wiki/entities/nasser|Násser]], o gradiente ruim "é aquele que a transição não é suave". De vermelho para ciano, a transição tem de "passar pelo laranja, passar pelo amarelo, passar pelo verde" ou dar a volta pelo rosa, magenta, roxo e azul: "a transição no espectro é muito grande". A referência é o círculo cromático.

## Duas receitas

1. **Vizinhas no círculo** (troca de matiz curta): vermelho → rosa, azul → ciano, rosa → roxo. "Não precisa necessariamente ser vizinha": verde → azul "pegam o ciano, mas não é tão distante".
2. **Mesma matiz** (monocromático): uma escala do mesmo hexadecimal, de tom escuro a claro, sem rotação de matiz ([[wiki/concepts/variacao-de-cores]]).

Nas duas, evitar cores "topadas" (saturação e brilho no máximo), "porque elas ficam muito saturadas"; preferir "um tom um pouquinho mais pastel". Ele avisa: "não entenda tudo que eu estou falando aqui como uma regra".

## Referências

WebGradients e `dribbble.com/colors` com filtro de cor ([[wiki/entities/dribbble]]); "quando você achar um gradiente que toca no seu coração, [...] você separa ele e pega lá no Figma".

## Olhar de dev

`[external]` O "bad gradient" também depende do espaço de cor. Em sRGB, a interpolação entre cores distantes passa por uma faixa acinzentada no meio; `linear-gradient(in oklch, red, cyan)` (CSS Color 4: https://www.w3.org/TR/css-color-4/#interpolation) anda por matiz e luminosidade perceptuais. `in oklch longer hue` dá a volta pelo outro lado da roda (alta). A regra da aula (cores próximas) evita o problema em qualquer espaço.

## Ver também

[[wiki/concepts/harmonia-de-cores]], [[wiki/concepts/luminosidade-das-cores]], [[wiki/concepts/paleta-de-cores]], [[wiki/concepts/blend-modes]], [[wiki/concepts/modelo-de-cor-hsb]]

## Key Sources

- [[wiki/sources/frontpush-mentoria-identidade-visual-marca-minimalista-gradiente-paleta-tipografia]]: bad gradient vermelho → ciano, vizinhas, monocromático no "scale", cores não topadas
