---
type: concept
title: "matrix() e matrix3d() no transform"
aliases: ["matrix", "matrix()", "matrix3d", "matrix3d()", "matriz de transformação", "transform matrix"]
date_created: 2026-11-20
date_updated: 2026-11-20
source_count: 1
tags: [css, transform, matrix, svg, matematica, frontend]
skill: tech-mentor-frontend
status: stub
---

# matrix() e matrix3d() no transform

Toda combinação de `translate`, `scale`, `rotate` e `skew` vira, por baixo, uma matriz. `matrix(a, b, c, d, e, f)` é a forma 2D com seis números; `matrix3d()` é a 4×4 com dezesseis. Quase ninguém escreve à mão: é o que ferramentas exportam e o que o navegador devolve.

## Os seis números

`[external]` (CSS Transforms Level 1, w3.org/TR/css-transforms-1; confiança alta)

```
| a  c  e |
| b  d  f |
| 0  0  1 |
```

- `a`, `d`: escala em x e y quando não há rotação.
- `b`, `c`: **tangentes** do skew em y e em x (não ângulos).
- `e`, `f`: translação em px, sem unidade.
- Rotação também mora em `a`–`d`: `rotate(θ)` = `matrix(cos θ, sin θ, −sin θ, cos θ, 0, 0)`.

Por isso a leitura "a = scaleX, b = skewY, c = skewX, d = scaleY" só vale quando cada função aparece sozinha. Combinadas, os números se misturam, e a ordem das funções muda o resultado (multiplicação de matrizes não comuta).

## Onde ela aparece

- **DevTools:** `getComputedStyle(el).transform` devolve `matrix(...)` ou `matrix3d(...)`, nunca a lista original.
- **SVG exportado:** `transform="matrix(a b c d e f)"` em grupos e caminhos do Illustrator e do [[wiki/entities/figma]] ([[wiki/concepts/formato-svg]]).
- **Bibliotecas de animação** leem a matriz computada para interpolar a partir do estado atual.

## Na aula de transform do FrontPUSH (Násser)

Em [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]], [[wiki/entities/nasser|Násser]] lista a ordem "scale x, skew y, skew x, scale y, translate x, translate y" e avisa: "quase você não vai aplicar, porque não é muito intuitivo, são mais ferramentas que utilizam o matrix". O valor está em reconhecer: "quando você bater o olho nessa propriedade matrix, em algum objeto SVG, você já fala, ele está aplicando a propriedade transform". O `matrix3d` ficou prometido. Ver [[wiki/concepts/transition-e-transform-css]].

## Key sources

- [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 01: matrix como "resumo das propriedades"
