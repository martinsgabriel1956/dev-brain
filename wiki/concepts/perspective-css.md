---
type: concept
title: "Perspectiva e 3D no CSS (perspective)"
aliases: ["perspective", "perspectiva CSS", "perspective()", "3D no CSS", "flip 3D", "rotateX", "preserve-3d"]
date_created: 2026-11-20
date_updated: 2026-11-20
source_count: 1
tags: [css, transform, perspective, 3d, rotatex, animacao, frontend]
skill: tech-mentor-frontend
status: stub
---

# Perspectiva e 3D no CSS (perspective)

A tela é 2D. Funções 3D de `transform` (`rotateX`, `rotateY`, `translateZ`, `scaleZ`) só parecem 3D quando há perspectiva: uma distância entre o "olho" e o plano z = 0 que faz o que está longe ficar menor. Sem ela, o navegador projeta em ortográfico: `rotateX(θ)` vira um achatamento vertical igual a `scaleY(cos θ)`, e `translateZ` não aparece.

## Duas formas

`[external]` (CSS Transforms Level 2, w3.org/TR/css-transforms-2; confiança alta)

| | Onde vai | Efeito |
|---|---|---|
| Propriedade `perspective: 400px` | No **pai** | Um ponto de fuga comum a todos os filhos; ajustável com `perspective-origin` |
| Função `transform: perspective(400px) rotateY(30deg)` | No **próprio elemento**, primeiro na lista | Cada elemento com seu próprio ponto de fuga |

Valor menor = olho mais perto = distorção mais forte. Valor grande tende ao ortográfico.

Para 3D aninhado (um cubo com seis faces filhas), o pai precisa de `transform-style: preserve-3d`; sem isso, os filhos achatam no plano dele. Cartas que viram usam `backface-visibility: hidden` para esconder o verso.

## Na aula de transform do FrontPUSH (Násser)

Em [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]], [[wiki/entities/nasser|Násser]] mostra o problema antes da solução: `rotateX(50deg)` "só diminuiu", parece `scaleY(0,7)` (a conta dá 0,64). Depois põe `perspective: 400px` no body, pai da caixa: "essa parte que teoricamente está mais longe, ela está menor, então dá a ideia de que ele literalmente está fazendo um flip 3D". A regra dele, "a gente nunca aplica na div que a gente está olhando", vale para a propriedade; a função `perspective()` vai justamente no elemento. A analogia do celular girado perto ou longe do olho é a da tabela acima: perto, distorção maior.

Isso responde em parte à aula 04, onde 3D com perspectiva parecia pedir biblioteca JS ([[wiki/concepts/css-puro-vs-biblioteca-de-animacao]]). Flips, cubos e cartões saem em CSS puro; malhas, luz e câmera pedem [[wiki/concepts/webgl]].

## Performance e acessibilidade

`[skill: tech-mentor-frontend]` Transformações 3D rodam no compositor como as 2D ([[wiki/concepts/transition-e-transform-css]]). Flips e rotações grandes estão entre os movimentos que `prefers-reduced-motion: reduce` deve desligar ([[wiki/concepts/acessibilidade]]).

## Key sources

- [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 01: `rotateX` sem e com `perspective: 400px` no pai
