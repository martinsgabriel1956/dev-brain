---
type: entity
title: "GSAP"
aliases: ["GreenSock", "GreenSock Animation Platform", "gsap.timeline", "ScrollTrigger"]
date_created: 2026-11-19
date_updated: 2026-11-19
source_count: 2
tags: [biblioteca, javascript, animacao, timeline, scrolltrigger, frontend]
skill: tech-mentor-frontend
status: stub
---

# GSAP

Biblioteca JavaScript de animação (GreenSock Animation Platform). Anima qualquer propriedade numérica de elementos do DOM, SVG, canvas ou objetos JS. Ela se destaca pela `gsap.timeline()`, que encadeia e sobrepõe animações com controle de tempo, e por plugins como o ScrollTrigger, de animação por rolagem. A Webflow comprou a GreenSock em 2024, e desde então a biblioteca inteira, plugins pagos incluídos, ficou gratuita (sem fetch; confiança média-alta). `[skill: tech-mentor-frontend]`: GSAP para timelines complexas, scroll storytelling e animação de marketing; Framer Motion para interações de UI em React.

**Onde roda:** o GSAP atualiza os estilos a cada quadro via `requestAnimationFrame`, na thread principal. Animar `transform` e `opacity` com ele evita layout e pintura, mas não sai da thread principal como uma animação CSS ou da Web Animations API de `transform`/`opacity`. Se o JavaScript travar, a animação trava junto ([[wiki/concepts/paint-composite]], [[wiki/concepts/event-loop-performance-js]]).

## No FrontPUSH

- Em [[wiki/sources/frontpush-cache-e-cdn-css-js-inline-incorporado-externo]], o GSAP 3.12.2 com o ScrollTrigger é o exemplo de biblioteca carregada por [[wiki/concepts/cdn]].
- Em [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]], [[wiki/entities/nasser|Násser]] monta a tela de carregamento dos projetos ([[wiki/entities/spider-man-projeto-nasser|Spider-Man]], "Paybank") "só utilizando o GSAP e uma timeline", e na mesma aula recomenda CSS puro por rodar no compositor. As duas coisas puxam para lados opostos.

## Key sources

- [[wiki/sources/frontpush-cache-e-cdn-css-js-inline-incorporado-externo]]: FrontPUSH, otimização aula 02: GSAP e ScrollTrigger via CDN
- [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]]: FrontPUSH, otimização aula 07: timeline da tela de carregamento
