---
type: concept
title: "Taxa de quadros e orçamento de 16 ms"
aliases: ["60 fps", "frame budget", "orçamento de quadro", "queda de frame", "jank", "16,6 ms"]
date_created: 2026-11-19
date_updated: 2026-11-20
source_count: 5
tags: [performance, animacao, rendering-pipeline, fps, jank, frontend]
skill: tech-mentor-frontend
status: stub
---

# Taxa de quadros e orçamento de 16 ms

Uma tela de 60 Hz mostra 60 quadros por segundo. Para a animação ficar fluida, o navegador precisa entregar um quadro novo a cada 1000/60 ≈ 16,7 ms. Se o trabalho de um quadro passa disso, o quadro é perdido e o movimento "engasga" (*jank*, queda de frame).

- **O orçamento real é menor.** O navegador também tem trabalho próprio a cada quadro, e o web.dev recomenda cerca de 10 ms para o código da página. `[external]` https://web.dev/articles/rendering-performance (sem fetch nesta sessão; confiança alta).
- **Telas mais rápidas apertam o prazo.** A 90 Hz o quadro tem 11,1 ms; a 120 Hz, 8,3 ms. Celulares com 120 Hz são comuns.
- **O que cabe num quadro depende do caminho do pipeline** ([[wiki/concepts/critical-rendering-path]]). Mudar `width` refaz layout, pintura e composição ([[wiki/concepts/reflow-layout]]). Mudar `box-shadow` refaz pintura e composição. Mudar `transform` ou `opacity` com camada própria só refaz a composição, que pode correr na thread do compositor mesmo com a thread principal ocupada ([[wiki/concepts/paint-composite]]).
- **Animação em JavaScript** (`requestAnimationFrame`, [[wiki/entities/gsap|GSAP]]) disputa os 16 ms com todo o resto da thread principal. Uma tarefa longa (> 50 ms) derruba vários quadros seguidos e atrasa cliques, o que pesa no INP ([[wiki/concepts/event-loop-performance-js]], [[wiki/concepts/core-web-vitals]]).
- **Para medir:** no Chrome DevTools, o painel Performance (quadros perdidos em vermelho) e o medidor de FPS em Rendering, com throttling de CPU para simular celular ([[wiki/concepts/mobile-animacoes-performaticas]]).

## No FrontPUSH

Em [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]], [[wiki/entities/nasser|Násser]] lê do artigo: "se o quadro não for concluído em 16.6 milissegundos, os usuários perceberão um atraso". Ele trata a queda de frame no celular com teste em aparelho real e, em último caso, cortando a animação no mobile.

## O preço do motion (FrontPUSH, motion aula 02)

Em [[wiki/sources/frontpush-como-usar-o-motion-vantagens-boas-praticas-pontos-de-atencao]]: "o preço que você paga pelo motion é [...] o sistema pode ficar mais lento". O custo depende do que se anima: `transform`/`opacity` no compositor custam pouco; layout, `box-shadow` e JS na thread principal disputam os 16 ms.

## Keyframes não são quadros (FrontPUSH, motion aula 03)

Em [[wiki/sources/frontpush-principios-motion-linha-do-tempo-keyframes-transicao-entre-estados]], Násser explica a fluidez dos [[wiki/concepts/keyframes-css]] pelo vídeo e jogos em 60 fps: "quanto mais frames você tem em um segundo, mais fluido parece". Precisão: o navegador interpola entre os keyframes a cada quadro da tela; três keyframes rodam a 60 fps como trinta. A taxa depende do custo de cada quadro, não do número de keyframes.

## CSS nativo × JS mediador (FrontPUSH, motion aula 04)

Em [[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]]: CSS puro é "tecnologia nativa", sem JS "como mediadora". Vale para `transform`/`opacity`; um `@keyframes` de `width` também gasta a thread principal. O custo é o trabalho por quadro, não o tamanho do código ([[wiki/concepts/css-puro-vs-biblioteca-de-animacao]]).

## A primeira demo de @keyframes anima width (FrontPUSH, básico CSS aula 03)

Em [[wiki/sources/frontpush-propriedade-animation-parte-1-keyframes-from-to-duration-direction-fill-mode]], o primeiro keyframe vai de `width: 0` a `100px`. Funciona, mas refaz layout a cada quadro; `transform: scaleX()` cresce no compositor.

## Key sources

- [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]]: FrontPUSH, otimização aula 07: 60 fps e 16,6 ms
- [[wiki/sources/frontpush-como-usar-o-motion-vantagens-boas-praticas-pontos-de-atencao]]: FrontPUSH, mini curso de CSS Animations, aula 02: "o sistema pode ficar mais lento"
- [[wiki/sources/frontpush-principios-motion-linha-do-tempo-keyframes-transicao-entre-estados]]: FrontPUSH, mini curso de CSS Animations, aula 03: 60 fps × número de keyframes
- [[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]]: FrontPUSH, mini curso de CSS Animations, aula 04: nativo × mediador; o custo é por quadro
- [[wiki/sources/frontpush-propriedade-animation-parte-1-keyframes-from-to-duration-direction-fill-mode]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 03: keyframe de width na primeira demo
