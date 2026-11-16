---
type: concept
title: "Modelos de cor"
aliases: ["Modelos de cor (HSB, RGB, hexadecimal, CSS)", "modelo de cor", "color model", "color models", "representação de cores em código", "representação da cor", "HSB", "HSV", "HSL", "RGB", "RGBA", "CMYK", "hexadecimal", "hex color", "cor hexadecimal", "canal alfa"]
date_created: 2026-11-14
date_updated: 2026-11-15
source_count: 2
tags: [ui, ui-design, cor, modelos-de-cor, hsb, rgb, cmyk, hexadecimal, css, figma, design-tokens]
skill: ux-ui-mentor
status: stub
---

# Modelos de cor

Formas de escrever a mesma cor em números. O slide da abertura do módulo de [[wiki/concepts/teoria-das-cores]] lista HSB, hexadecimal e RGB x CMYK, e deixa a prática no Figma para a aula seguinte ([[wiki/sources/teoria-das-cores-introducao-natureza-objetivos-fenomeno-fisico]]). Na aula de representação da cor, [[wiki/entities/nasser|Násser]] divide por uso: **HSB para compor a paleta, hexadecimal e RGB para o código** ([[wiki/sources/representacao-da-cor-em-codigos-hsb-hexadecimal-rgb]]).

| Modelo | Componentes | Faixa | Para quê, segundo a aula |
|---|---|---|---|
| HSB (= HSV) | hue (matiz), saturação, brilho | 0–359, 0–100, 0–100 | compor a paleta e as variações; é o que o [[wiki/entities/figma]] mostra no seletor de cor |
| RGB | vermelho, verde, azul | 0–255 cada | código |
| Hexadecimal | `#RRGGBB`, um par em base 16 por canal | `00`–`FF` cada | código |
| CSS (no Figma) | RGB + alfa | alfa = transparência | código, quando há opacidade |

Fontes: [[wiki/sources/teoria-das-cores-introducao-natureza-objetivos-fenomeno-fisico]] (HSB com as faixas, hexadecimal, Figma) e [[wiki/sources/representacao-da-cor-em-codigos-hsb-hexadecimal-rgb]] (tabela completa).

## HSB: as três alavancas

O modelo tem página própria, com as regras de bolso da aula prática: [[wiki/concepts/modelo-de-cor-hsb]]. Na aula de representação ([[wiki/sources/representacao-da-cor-em-codigos-hsb-hexadecimal-rgb]]):

- **Hue (matiz)**: posição no círculo cromático; 360 e 0 são o mesmo ponto.
- **Saturação**: "a presença de determinada cor no objeto". No mínimo, cinza; no máximo, cor "mais pura".
- **Brilho**: no 0, preto puro; no máximo, cor "mais estourada".

A regra de Násser: não usar o canto do seletor (saturação e brilho no máximo), porque "esse tipo de cor aqui a gente não acha na natureza". Ver [[wiki/concepts/harmonia-visual]].

## Hex e RGB são o mesmo número

`#8FFF00` = RGB (143, 255, 0). Cada par hex é um byte, de 0 a 255, escrito em [[wiki/concepts/sistema-hexadecimal|base 16]]; ver também [[wiki/concepts/sistema-binario-bit-byte]]. A aula faz a conversão na mão e chega a 144 porque usa F = 16. O certo é F = 15, o que dá 143 ([[wiki/sources/representacao-da-cor-em-codigos-hsb-hexadecimal-rgb]]).

## RGB x CMYK

Luz (aditivo, tela) contra tinta (subtrativo, impressão). Explica por que "branco é todas as cores" na luz e não na tinta ([[wiki/concepts/espectro-visivel]], [[wiki/sources/teoria-das-cores-introducao-natureza-objetivos-fenomeno-fisico]]). Na aula de representação, o par está no slide mas fica para depois ([[wiki/sources/representacao-da-cor-em-codigos-hsb-hexadecimal-rgb]]); a explicação aditivo/subtrativo é `[external]` nessa página de origem.

## Olhar de dev

`[skill: ux-ui-mentor]` Para escalas de cor em CSS, a skill prefere **HSL** a HSB: `hsl()` existe no CSS e permite variar só o L (`--blue-100` a `--blue-900`). Para paletas novas, prefere **OKLCH**, que é perceptualmente uniforme (mesmo L = mesmo brilho percebido entre matizes): no HSL/HSB, amarelo e azul com o mesmo L ou B parecem ter brilhos diferentes. Os valores crus (primitivos) viram tokens semânticos antes de entrar nos componentes; ver [[wiki/concepts/cor-semantica]].

`[external]` O alfa também cabe no hex de oito dígitos (`#RRGGBBAA`) e na sintaxe moderna de `rgb(r g b / a)`. O `rgba()` ficou como alias (https://developer.mozilla.org/en-US/docs/Web/CSS/hex-color, https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/rgb).

## Armadilha

Brilho (B) ou lightness (L) alto não garante legibilidade. O [[wiki/concepts/contraste]] se mede pela luminância relativa (WCAG), não pelo número do seletor.

## Key Sources

- [[wiki/sources/teoria-das-cores-introducao-natureza-objetivos-fenomeno-fisico]] — slide com HSB, hexadecimal e RGB x CMYK; prática prometida no Figma
- [[wiki/sources/representacao-da-cor-em-codigos-hsb-hexadecimal-rgb]] — HSB para compor, hex e RGB para o código, modo CSS com alfa; a conta `8F` → 143
