---
type: entity
title: "GSAP"
aliases: ["GreenSock", "GreenSock Animation Platform", "gsap.timeline", "ScrollTrigger"]
date_created: 2026-11-19
date_updated: 2026-11-21
source_count: 6
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

## Biblioteca ou CSS puro (FrontPUSH, motion aula 01)

Em [[wiki/sources/frontpush-introducao-motion-design-css-animations-grade-do-curso]], o mini curso de CSS Animations promete um módulo de bibliotecas JavaScript e a discussão "utilizar uma biblioteca ou CSS puro". O GSAP é a biblioteca que Násser já usou no curso (inferência: centro provável do módulo) ([[wiki/concepts/motion-design]]).

## Uma linha do tempo por elemento (FrontPUSH, motion aula 03)

Em [[wiki/sources/frontpush-principios-motion-linha-do-tempo-keyframes-transicao-entre-estados]], cada elemento da animação de lançamento tem "uma linha do tempo" própria em CSS, sincronizada por durações e delays. A `gsap.timeline()` junta tudo numa linha do tempo só, como no After Effects: um argumento do lado "biblioteca" do debate da aula 01 ([[wiki/concepts/keyframes-css]]).

## Biblioteca na balança (FrontPUSH, motion aula 04)

Em [[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]], a aula prometida na aula 01 responde "depende": biblioteca dá facilidade, CSS puro dá otimização. O GSAP não é citado pelo nome; o exemplo é o [[wiki/entities/anime-js|anime.js]] ([[wiki/concepts/css-puro-vs-biblioteca-de-animacao]]).

## No portfólio do autor (FrontPUSH, hospedagem aula 06)

Em [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]]: o portfólio usa GSAP, "porém eu adicionei a página como um script, eu não utilizei nenhum npm"; o site segue estático.

## Key sources

- [[wiki/sources/frontpush-cache-e-cdn-css-js-inline-incorporado-externo]]: FrontPUSH, otimização aula 02: GSAP e ScrollTrigger via CDN
- [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]]: FrontPUSH, otimização aula 07: timeline da tela de carregamento
- [[wiki/sources/frontpush-introducao-motion-design-css-animations-grade-do-curso]]: FrontPUSH, mini curso de CSS Animations, aula 01: módulo de bibliotecas e "biblioteca ou CSS puro"
- [[wiki/sources/frontpush-principios-motion-linha-do-tempo-keyframes-transicao-entre-estados]]: FrontPUSH, mini curso de CSS Animations, aula 03: timeline única × uma linha do tempo por elemento no CSS
- [[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]]: FrontPUSH, mini curso de CSS Animations, aula 04: otimização × facilidade
- [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]]: FrontPUSH, hospedagem aula 06: GSAP por script, sem npm
