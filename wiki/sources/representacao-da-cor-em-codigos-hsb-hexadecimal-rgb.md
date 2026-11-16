---
type: source
title: "Representação da cor em códigos: HSB, hexadecimal e RGB"
aliases: ["aula de representação da cor", "cor em códigos", "HSB hexadecimal RGB", "representação em códigos"]
date_created: 2026-11-14
date_updated: 2026-11-14
source_count: 0
tags: [ui, ui-design, design, cor, modelos-de-cor, hsb, rgb, hexadecimal, css, figma, cs-fundamentals]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/representacao-da-cor-em-codigos-hsb-hexadecimal-rgb.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-14
---

# Representação da cor em códigos: HSB, hexadecimal e RGB

## TL;DR

Aula prática (cerca de 11 min) do bloco de cor, feita no seletor de cor do [[wiki/entities/figma]]. Explica os [[wiki/concepts/modelos-de-cor|modelos de cor]] que aparecem no design e no código. **HSB** serve para *compor* a paleta: hue de 0 a 359 (o círculo cromático), saturação de 0 a 100 (a "presença" da cor; no mínimo vira cinza) e brilho de 0 a 100 (no 0, preto puro). **Hexadecimal** e **RGB** são o que se encontra no desenvolvimento: `#RRGGBB` são três pares em [[wiki/concepts/sistema-hexadecimal|base 16]], cada um de 0 a 255. O modo **CSS** do Figma é o RGB com o canal alfa (transparência). O exemplo é o verde `8F FF 00`: ele faz a conta na mão e chega a vermelho 144, mas o Figma mostra **143**. O erro está na aula: F vale 15, não 16. O slide anexado anuncia ainda "RGB x CMYK", que fica para depois.

## Key Claims

### HSB para compor

- **Três componentes**: "o H significa hue, matiz, o S saturação e o B de brightness, brilho". Hue vai "de 0 até 359", com "aquela ideia do círculo cromático, 360 graus"; saturação e brilho vão de 0 a 100 (slide: Hue 0–359, Saturation 0–100, Brightness 0–100). Ver [[wiki/concepts/modelos-de-cor]].
- **Hue é um círculo**: no seletor, "360 e 0, onde ele vai e volta no mesmo ponto", passando "por todo o espectro visível" da aula anterior.
- **Saturação é horizontal**: arrastando o cursor para os lados, o hue (72, 73) não muda. Saturação mede "a presença de determinada cor no objeto": no máximo, a cor fica "mais pura"; no mínimo, tende "a escala de cinza".
- **Brilho é vertical**: no 0, "o preto puro"; no máximo, a cor fica "um pouquinho mais estourada".
- **Não usar cor pura** (saturação e brilho no máximo): "eu sempre indico não utilizar, porque esse tipo de cor aqui a gente não acha na natureza". Ver [[wiki/concepts/harmonia-visual]].
- **HSB compõe, hex e RGB vão para o código**: HSB "é mais utilizado para a gente compor as cores com a paleta de cores", mas "no ambiente de desenvolvimento" aparecem "o hexadecimal e o modo RGB".

### Hexadecimal

- **Formato**: "sempre é acompanhado de um hashtag" e se decompõe em `RRGGBB`. No exemplo, azul `00` (zerado), verde `FF` (máximo), vermelho `8F`.
- **Por que hexa**: "hexa vem de 6 [...] decimal ao número 10", então o sistema precisa de 16 algarismos: 0 a 9 e A a F, com "o A representa 10, o B 11, o C 12, D 13, 14, 15". Ver [[wiki/concepts/sistema-hexadecimal]].
- **Cada canal vai de 0 a 255**: "0 até 255 de vermelho, 0 até 255 de verde e 0 até 255 de azul".
- **Notação posicional**: as posições contam "da direita para a esquerda"; a da esquerda vale 16¹ e a da direita, 16⁰. O 8 em `8F` dá 8 × 16 = 128.
- **A conta errada**: ele diz que F "significa 16 no nosso sistema" e soma 128 + 16 = **144**. Pela tabela que ele mesmo deu (F = 15), o certo é 128 + 15 = **143**. O Figma mostra 143, e ele chama de "justamente essa conta". Ver Tensões.
- **Ninguém precisa fazer a conta**: "vocês não vão precisar fazer ela, mas eu preciso explicar uma vez".

### RGB e o modo CSS

- **Resultado**: a cor é RGB (143, 255, 0) no Figma; ele anuncia (144, 255, 0).
- **Os dois modos do código**: "na maioria das vezes vocês vão ver ou o modo RGB ou o modo hexadecimal quando a gente estiver programando".
- **Modo CSS** = "o modo RGB normal, normalíssimo, só que o A indica o caráter alfa, que é o quanto transparente é essa cor".

## Entities

- [[wiki/entities/nasser]]: autor inferido. O nome não é dito. A legenda vem do mesmo lote das aulas "W7" já confirmadas (IDs `master-pkg-t-17453691…`), e o tom e o uso do Figma são os mesmos.
- [[wiki/entities/figma]]: seletor de cor com os modos Hex, RGB, CSS e HSB; ele lembra que a caixinha "é muito comum em toda e qualquer ferramenta de prototipagem".

## Concepts

- [[wiki/concepts/modelos-de-cor]] (novo)
- [[wiki/concepts/sistema-hexadecimal]] (novo)
- [[wiki/concepts/sistema-binario-bit-byte]]
- [[wiki/concepts/cor-semantica]]
- [[wiki/concepts/harmonia-visual]]
- [[wiki/concepts/contraste]]
- [[wiki/concepts/elementos-da-interface]]
- [[wiki/concepts/ui-design]]

## Tensões com a wiki

- **F = 16 (errado) e 144 em vez de 143.** A aula lista A = 10 … F = 15 e depois usa F = 16 na conta. `8F` = 8 × 16 + 15 = 143, que é o valor que o Figma exibe. A conta só serve se o aluno corrigir o F. Ver [[wiki/concepts/sistema-hexadecimal]].
- **"1, 2, 3 … 9" sem o zero**, depois corrigido com "tem o 0 aqui atrás". A ordem dos 16 algarismos é 0–9, A–F.
- **"Hue de 0 a 359" e "360 e 0" no seletor.** Os dois valem: 360° e 0° são o mesmo ponto do círculo, então o hue cobre 360 valores inteiros (0–359). O CSS aceita qualquer ângulo e faz o módulo `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/hue).
- **HSB não é HSL.** `[skill: ux-ui-mentor]` A skill recomenda **HSL** para escalas em CSS (`hsl()` existe no CSS, HSB/HSV não) e **OKLCH** para paletas perceptualmente uniformes. No HSB, o B = 100 com S = 0 dá branco; no HSL, branco é L = 100. E nenhum dos dois mede brilho percebido: amarelo e azul com o mesmo B parecem ter brilhos diferentes. Por isso o B do HSB não substitui a verificação de [[wiki/concepts/contraste]].
- **"Cor pura não existe na natureza."** É heurística estética, sem dado empírico citado. `[skill: ux-ui-mentor]` A versão prática é que saturação máxima em áreas grandes cansa e "vibra" ao lado de cores complementares. Paletas de UI trabalham com escalas de saturação e luminosidade, não com o canto do seletor.
- **Modo CSS = RGB + alfa.** `[external]` O CSS também aceita alfa no hex, com oito dígitos (`#RRGGBBAA`) (https://developer.mozilla.org/en-US/docs/Web/CSS/hex-color). E `rgb()` aceita alfa direto na sintaxe moderna (`rgb(143 255 0 / 50%)`); o `rgba()` virou alias (https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/rgb).
- **Mesma ideia em [[wiki/concepts/sistema-binario-bit-byte]]**: lá, cada canal RGB é 1 byte (0–255), e o hex é "só outra forma de representar os mesmos valores". Esta aula dá a conta de conversão, que lá faltava. 255 = FF porque dois dígitos hex = 8 bits.

## Open Questions

- **Lacuna de ~21 s** na legenda (00:31 → 00:52) depois de "hashtag, onde eu posso decompor em": a fala salta para "RRGGBB, os dois próximos é a cor verde". A frase sobre o par do vermelho provavelmente foi falada ou escrita na tela durante esse intervalo. Não foi inserida no raw.
- **"É 8FF00"**: a legenda tem cinco caracteres. A cor real é `#8FFF00` (8F FF 00), conforme a própria decomposição da aula. Mantido literal no raw: não dá para saber se foi lapso da fala ou da legenda.
- **"RGB x CMYK"** está no slide e é prometido ("Depois a gente vê a diferença de RGB para CMYK"). Não é tratado nesta aula.
- **"A aula passada"** sobre o espectro visível ainda não foi ingerida.
- **"Tem caráter 8"**, "o caráter alfa", "ele não é esse bem um algarismo": mantidos literais.

## Raw Quotes

- "esse modo HSB é mais utilizado para a gente compor as cores com a paleta de cores e tudo, mas quando passa para o ambiente de desenvolvimento, na maioria das vezes vai encontrar o hexadecimal e o modo RGB"
- "saturação é o quê? A presença de determinada cor no objeto"
- "aquela cor pura, que eu sempre indico não utilizar, porque esse tipo de cor aqui a gente não acha na natureza"
- "vocês não vão precisar fazer ela, mas eu preciso explicar uma vez para vocês entenderem"

## Ver também

- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]: a cor como elemento que informa
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-compreensao-consistencia-svg-tinyimage]]: SVG recolorido com o hex da marca
- [[wiki/sources/cs50-2026-semana-0-representacao-dados-algoritmos-scratch]]: RGB como 3 bytes, do lado da computação
