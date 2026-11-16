---
type: concept
title: "Modelos de cor (HSB, RGB, hexadecimal, CSS)"
aliases: ["modelo de cor", "color model", "HSB", "HSV", "RGB", "RGBA", "hex color", "cor hexadecimal", "canal alfa", "representação da cor"]
date_created: 2026-11-14
date_updated: 2026-11-14
source_count: 1
tags: [ui, ui-design, cor, modelos-de-cor, hsb, rgb, hexadecimal, css, design-tokens]
skill: ux-ui-mentor
status: stub
---

# Modelos de cor (HSB, RGB, hexadecimal, CSS)

Formas de escrever a mesma cor em números. Na aula de [[wiki/entities/nasser|Násser]] ([[wiki/sources/representacao-da-cor-em-codigos-hsb-hexadecimal-rgb]]), a divisão é de uso: **HSB para compor a paleta, hexadecimal e RGB para o código**.

| Modelo | Componentes | Faixa | Para quê, segundo a aula |
|---|---|---|---|
| HSB (= HSV) | hue, saturação, brilho | 0–359, 0–100, 0–100 | compor a paleta e as variações |
| RGB | vermelho, verde, azul | 0–255 cada | código |
| Hexadecimal | `#RRGGBB`, um par em base 16 por canal | `00`–`FF` cada | código |
| CSS (no Figma) | RGB + alfa | alfa = transparência | código, quando há opacidade |

## HSB: as três alavancas

- **Hue (matiz)**: posição no círculo cromático; 360 e 0 são o mesmo ponto.
- **Saturação**: "a presença de determinada cor no objeto". No mínimo, cinza; no máximo, cor "mais pura".
- **Brilho**: no 0, preto puro; no máximo, cor "mais estourada".

A regra de Násser: não usar o canto do seletor (saturação e brilho no máximo), porque "esse tipo de cor aqui a gente não acha na natureza". Ver [[wiki/concepts/harmonia-visual]].

## Hex e RGB são o mesmo número

`#8FFF00` = RGB (143, 255, 0). Cada par hex é um byte, de 0 a 255, escrito em [[wiki/concepts/sistema-hexadecimal|base 16]]; ver também [[wiki/concepts/sistema-binario-bit-byte]]. A aula faz a conversão na mão e chega a 144 porque usa F = 16. O certo é F = 15, o que dá 143.

## Olhar de dev

`[skill: ux-ui-mentor]` Para escalas de cor em CSS, a skill prefere **HSL** a HSB: `hsl()` existe no CSS e permite variar só o L (`--blue-100` a `--blue-900`). Para paletas novas, prefere **OKLCH**, que é perceptualmente uniforme: no HSL/HSB, amarelo e azul com o mesmo L ou B parecem ter brilhos diferentes. Os valores crus (primitivos) viram tokens semânticos antes de entrar nos componentes; ver [[wiki/concepts/cor-semantica]].

`[external]` O alfa também cabe no hex de oito dígitos (`#RRGGBBAA`) e na sintaxe moderna de `rgb(r g b / a)`. O `rgba()` ficou como alias (https://developer.mozilla.org/en-US/docs/Web/CSS/hex-color, https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/rgb).

## Armadilha

Brilho (B) ou lightness (L) alto não garante legibilidade. O [[wiki/concepts/contraste]] se mede pela luminância relativa (WCAG), não pelo número do seletor.

## Pendente

**RGB x CMYK** está no slide da aula, mas fica para depois. RGB é modelo aditivo (luz, telas); CMYK é subtrativo (tinta, impressão) `[external]`.

## Key Sources

- [[wiki/sources/representacao-da-cor-em-codigos-hsb-hexadecimal-rgb]]: HSB para compor, hex e RGB para o código, modo CSS com alfa; a conta `8F` → 143
