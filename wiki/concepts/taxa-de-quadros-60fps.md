---
type: concept
title: "Taxa de quadros e orçamento de 16 ms"
aliases: ["60 fps", "frame budget", "orçamento de quadro", "queda de frame", "jank", "16,6 ms"]
date_created: 2026-11-19
date_updated: 2026-11-19
source_count: 1
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

## Key sources

- [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]]: FrontPUSH, otimização aula 07: 60 fps e 16,6 ms
