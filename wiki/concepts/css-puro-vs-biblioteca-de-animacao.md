---
type: concept
title: "CSS puro vs. biblioteca de animação"
aliases: ["biblioteca ou CSS puro", "Bib JS vs. CSS puro", "otimização vs. facilidade", "CSS vs JavaScript para animação"]
date_created: 2026-11-20
date_updated: 2026-11-20
source_count: 1
tags: [animacao, css, javascript, biblioteca, performance, trade-off, motion-design, frontend]
skill: tech-mentor-frontend
status: stub
---

# CSS puro vs. biblioteca de animação

A escolha entre animar com CSS nativo (`transition`, `@keyframes`) ou com uma biblioteca (JavaScript como [[wiki/entities/gsap|GSAP]] e [[wiki/entities/anime-js|anime.js]], ou CSS com classes prontas). Para [[wiki/entities/nasser|Násser]], a resposta é "depende", medida pela dualidade **otimização × facilidade** ([[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]]).

## O quadro de Násser

| | Bibliotecas CSS/JS | CSS puro |
|---|---|---|
| **Otimização** | ✗ uso excessivo gera conflitos e mais código | ✓ nativo, "não há outra tecnologia como mediadora" |
| **Facilidade** | ✓ tutoriais e boa documentação | código "na unha"; exige linha do tempo, [[wiki/concepts/keyframes-css\|keyframes]], [[wiki/concepts/easing\|easing]] |

Regra dele: animação simples ("só quero transladar", "só quero fazer aparecer") → CSS puro; 3D com perspectiva → biblioteca JS.

## O que decide de fato

`[skill: tech-mentor-frontend]` O critério de desempenho não é "CSS × JS", e sim **onde roda a interpolação e o que ela muda**:

- **CSS ou Web Animations API animando `transform`/`opacity`:** o navegador interpola e pode rodar no compositor, fluido mesmo com a thread principal ocupada ([[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]], [[wiki/concepts/taxa-de-quadros-60fps]]).
- **CSS animando `width`, `top`, `box-shadow`:** layout ou pintura a cada quadro, na thread principal. Ser CSS não ajuda.
- **Biblioteca JS com `requestAnimationFrame`:** calcula cada quadro na thread principal e escreve estilos; se o JS travar, a animação trava. É o caso do GSAP e do anime.js no modo padrão.

O critério de facilidade é **o que a animação precisa**:

| Precisa de | Melhor caminho |
|---|---|
| hover, entrada, saída, loop simples | `transition` / `@keyframes` |
| controle de reprodução (pausar, reverter, ir a um ponto) | Web Animations API ou biblioteca |
| muitos elementos sincronizados numa linha do tempo | `gsap.timeline()` / anime.js timeline |
| animação ligada à rolagem | CSS `animation-timeline: scroll()`/`view()` ou GSAP ScrollTrigger |
| física (mola, inércia), arrastar | biblioteca (GSAP, Motion) |
| canvas, WebGL, 3D com malhas | [[wiki/entities/three-js]], [[wiki/entities/spline]] |
| componentes React com saída animada | Framer Motion / Motion |

## Peso

"Você carrega uma porrada de código para poder utilizar uma animação" vale para script inteiro por `<script>`/[[wiki/concepts/cdn]]. Com ES modules e [[wiki/concepts/tree-shaking]], o bundler leva só o que é importado. Uma biblioteca de dezenas de KB pesa pouco perto das imagens, mas o JS também custa parse e execução na thread principal.

## Key sources

- [[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]]: FrontPUSH, mini curso de CSS Animations, aula 04: "depende", otimização × facilidade, anime.js, 3D
