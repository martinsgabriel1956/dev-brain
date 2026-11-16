---
type: concept
title: "Modelo de cor HSB"
aliases: ["HSB", "HSV", "hue saturation brightness", "matiz saturação brilho", "modo HSB", "primeiro quadrante"]
date_created: 2026-11-15
date_updated: 2026-11-16
source_count: 3
tags: [ui, ui-design, cor, hsb, figma, paleta-de-cores]
skill: ux-ui-mentor
status: stub
---

# Modelo de cor HSB

Descreve a cor por **matiz** (H, a volta do círculo), **saturação** (S, de cinza a cor pura) e **brilho** (B, de preto a cheio). É o modo que [[wiki/entities/nasser|Násser]] deixa ligado no seletor do [[wiki/entities/figma]] para compor a paleta ([[wiki/sources/paleta-de-cores-na-pratica-dribbble-hsb-variacoes-cores-neutras]]). Comparação com RGB, hexadecimal e CMYK em [[wiki/concepts/modelos-de-cor]].

## Regras de bolso da aula

- **Primeiro quadrante:** divida o quadrado do seletor em quatro e prefira o primeiro. "Não é uma regra, mas são boas práticas."
- **Nada no máximo:** não "topar" saturação nem brilho na cor de partida; fica difícil gerar as [[wiki/concepts/variacao-de-cores|variações]].
- **Pastel é leve:** um tom mais para o pastel "transmite isso de ser mais leve, de ser mais suave".
- **A referência é ponto de partida:** mexa na matiz "até você achar um tom que seja parecido".
- **Neutros com a matiz da base:** branco na matiz da cor de base, com saturação 2–4 ([[wiki/concepts/neutros-tingidos]]).

## HSB não é HSL

`[external]` HSB (= HSV) e HSL são modelos diferentes: no HSB, brilho 100 com saturação alta é a cor pura; no HSL, luminosidade 100 é sempre branco (https://en.wikipedia.org/wiki/HSL_and_HSV). Uma receita escrita em HSB não vale igual em HSL.

`[skill: ux-ui-mentor]` Para código, a skill indica HSL (escala mudando só L) ou OKLCH, que é perceptualmente uniforme: no HSB e no HSL, amarelo e roxo com o mesmo brilho não parecem igualmente claros.

## Matiz trocada por descuido (FrontPUSH, Sass)

Em [[wiki/sources/frontpush-variaveis-sass]], dois roxos parecidos com matiz 277 e 286 no HSB: "é variação de cor" quando a matiz fica; mudá-la é outra cor.

## adjust-hue no Sass (FrontPUSH)

Em [[wiki/sources/frontpush-funcoes-sass]]: `adjust-hue` gira a matiz em graus ("60 deg") no círculo cromático, a mesma operação do H do HSB. Hoje, `color.adjust($c, $hue: 60deg)`.

## Key Sources

- [[wiki/sources/paleta-de-cores-na-pratica-dribbble-hsb-variacoes-cores-neutras]] — modo HSB, primeiro quadrante, não topar S nem B
- [[wiki/sources/frontpush-variaveis-sass]]: roxos de matiz 277 × 286
- [[wiki/sources/frontpush-funcoes-sass]]: `adjust-hue` em graus
