---
type: concept
title: "Harmonia de cores"
aliases: ["harmonia cromática", "círculo cromático", "roda de cores", "color wheel", "cores complementares", "cores análogas", "complementar dividida", "split-complementary", "dividir complementar", "paleta triádica", "paleta monocromática"]
date_created: 2026-11-14
date_updated: 2026-11-14
source_count: 1
tags: [ui, ui-design, cor, harmonia-de-cores, circulo-cromatico, paleta-de-cores]
skill: ux-ui-mentor
status: stub
---

# Harmonia de cores

Relações entre cores lidas pela posição no círculo cromático. Na aula de paleta de [[wiki/entities/nasser|Násser]], é o que faz uma paleta "fazer sentido": "como as cores se conectam umas às outras" ([[wiki/sources/paleta-de-cores-base-enfoque-monocromatica-analoga-triadica]]). A aula própria de harmonia de cores, citada como anterior, ainda não está na wiki.

## Esquemas

| Esquema | Posição no círculo | Uso na aula |
|---|---|---|
| Monocromático | uma matiz, vários tons | contraste por claro x escuro + neutros |
| Análogo | vizinhas | uma escura, uma clara (azul + turquesa) |
| Complementar | opostas | base + enfoque (roxo ↔ amarelo; azul ↔ laranja) |
| Complementar dividido | as duas vizinhas do oposto | alternativa ao complementar na base + enfoque |
| Triádico | três equidistantes | uma predominante, duas de destaque |

`[external]` No círculo RYB (o de pintura, usado na aula), o complemento do violeta é o amarelo, e o complementar dividido do violeta são amarelo-laranja e amarelo-verde. A aula põe o dividido "no vermelho ou no laranja" (vizinhos do próprio violeta); o verde do slide é a leitura que bate com a teoria. Alguns exemplos falados também saem da definição (laranja e roxo como "análoga"; azul e verde como "complementar"). Ver as tensões em [[wiki/sources/paleta-de-cores-base-enfoque-monocromatica-analoga-triadica]].

## Princípio, não regra

A combinação "é tão vasta" que parece subjetiva, mas segue os esquemas. Mesma postura de [[wiki/concepts/harmonia-visual]], que trata da coerência de mensagem entre forma, tipografia e cor; harmonia de cores é o recorte da cor.

## Olhar de dev

`[skill: ux-ui-mentor]` Em HSL ou OKLCH, os esquemas viram aritmética de matiz (H): complementar = H + 180°, dividido = H + 150° e H + 210°, triádico = H + 120° e H + 240°, análogo = H ± 30°. O círculo HSL/OKLCH é o RGB, não o RYB: o complemento do violeta ali é um verde-amarelado, não o amarelo puro. Contraste (WCAG) não depende do esquema: duas cores complementares de mesma luminosidade podem falhar 4.5:1. Ver [[wiki/concepts/contraste]].

## Key Sources

- [[wiki/sources/paleta-de-cores-base-enfoque-monocromatica-analoga-triadica]] — círculo cromático aplicado a quatro tipos de paleta; exemplos falados sobre telas
