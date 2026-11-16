---
type: concept
title: "Sistema hexadecimal (base 16)"
aliases: ["hexadecimal", "base 16", "hex", "notação hexadecimal", "notação posicional"]
date_created: 2026-11-14
date_updated: 2026-11-16
source_count: 4
tags: [cs-fundamentals, sistema-hexadecimal, base-16, notacao-posicional, representacao, cor, rgb]
skill: ux-ui-mentor
status: stub
---

# Sistema hexadecimal (base 16)

Sistema de numeração com 16 algarismos: `0`–`9` e `A`–`F`, com A = 10, B = 11, C = 12, D = 13, E = 14 e F = 15. "Hexa vem de 6 [...] decimal ao número 10", na explicação de [[wiki/entities/nasser|Násser]] ([[wiki/sources/representacao-da-cor-em-codigos-hsb-hexadecimal-rgb]]). As letras entram porque "o 10 [...] é o conjunto de dois algarismos".

## Notação posicional

Cada posição, contada da direita para a esquerda a partir do 0, vale 16 elevado à posição:

```
8F = 8 × 16¹ + F × 16⁰
   = 8 × 16  + 15 × 1
   = 128 + 15 = 143
```

A aula comete aqui um erro instrutivo. Usa F = 16 e chega a 144, mas o Figma exibe 143. O maior algarismo de uma base *n* é sempre *n* − 1: 9 na decimal, 1 na binária, F (15) na hexadecimal.

## Por que hex aparece no código

Inferência (fundamentos de CS; a aula não diz isto): um dígito hex = 4 bits (um nibble), e dois dígitos = 1 byte. Por isso `FF` = 255 = `11111111`, e a cor `#RRGGBB` são exatamente 3 bytes, como no RGB de 0–255 por canal de [[wiki/concepts/sistema-binario-bit-byte]]. É uma forma compacta e legível de escrever binário: o mesmo motivo de aparecer em endereços de memória, hashes e dumps. Com [[wiki/concepts/bitwise-operations]], `(cor >> 16) & 0xFF` extrai o vermelho de um inteiro `0xRRGGBB`.

## Na UI

O uso mais visível para quem faz interface é a cor em hex (`#8FFF00`). Ver [[wiki/concepts/modelos-de-cor]].

## Cor em CSS

Em [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]], `color: red` é "a cor em escrito", mas o mesmo valor poderia ir em hexadecimal ou RGBA. Ver [[wiki/concepts/regra-css]].

## Key Sources

- [[wiki/sources/representacao-da-cor-em-codigos-hsb-hexadecimal-rgb]]: por que 16 algarismos, notação posicional e a conversão de `8F` (com o erro F = 16)
- [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]] — cor por nome, hex ou RGBA no CSS
- [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]: extensão Color Highlight pinta `#FFF` de branco no editor
- [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]: `#0f0f0f` (quase preto), `#FFF`, `#EEE`, `#000`
