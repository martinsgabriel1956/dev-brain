---
type: concept
title: "transition e transform no CSS (hover suave)"
aliases: ["transition", "transform", "scale", "transform: scale", "hover animado", "transição CSS"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 5
tags: [css, transition, transform, animacao, hover, acessibilidade, performance, frontend]
skill: tech-mentor-frontend
status: stub
---

# transition e transform no CSS (hover suave)

`transform` muda a forma da caixa sem mexer no fluxo: `scale()` (tamanho), `translate()` (posição), `rotate()`. `transition` anima a troca de valor de uma propriedade ao longo de um tempo, com uma curva (`ease`, `linear`...). Juntos, fazem o hover "suave".

Na aula de layout do [[wiki/entities/frontpush]] ([[wiki/sources/frontpush-layout-css-botao-hover-flexbox-media-query]]), [[wiki/entities/nasser|Násser]] faz o botão crescer no `:hover` com `transform: scale` ("aumente 5%", depois 1.2) e `transition` de 1 s `ease`, depois 300 ms. `[external]` Aumentar 5% é `scale(1.05)`; `scale(0.05)` encolheria a 5%. Ver [[wiki/concepts/pseudo-classe-css]] e [[wiki/concepts/botoes-em-interfaces]].

## Onde pôr a transition

`[external]` Na regra base (`button { transition: transform 300ms ease }`) ela anima a ida e a volta; só no `:hover`, a volta é instantânea. Nomear a propriedade (`transform`) evita animar tudo por acidente: https://developer.mozilla.org/en-US/docs/Web/CSS/transition.

## Performance e acessibilidade

`[skill: tech-mentor-frontend]` `transform` e `opacity` animam no compositor, sem recalcular layout; animar `width`, `top` ou `margin` força reflow a cada quadro. Respeite `@media (prefers-reduced-motion: reduce)` desligando ou encurtando o movimento. Ver [[wiki/concepts/mobile-animacoes-performaticas]] e [[wiki/concepts/acessibilidade]].

## Na NLW #2, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]], `transition: background 0.2s` nos botões ("um segundo é muito, eu quero só aquele detalhezinho") e `transition: opacity 0.2s` no link de voltar, que no hover vai a 0.6 e "parece que ele tá tipo dando uma respirada". `transition` é shorthand de `transition-duration` e outras.

## Na NLW #2, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]], `transition: 0.2s` sem nome de propriedade anima todas as que mudarem (o padrão é `all`). De brincadeira, `:hover { transform: translateY(-5px) }` com 1 s faz o botão subir. A margem superior negativa do formulário também "sobe" a caixa sobre o header, mas pelo fluxo.

## Key sources

- [[wiki/sources/frontpush-layout-css-botao-hover-flexbox-media-query]]: `:hover` com `transform: scale` e `transition` de 1 s / 300 ms `ease`
- [[wiki/sources/frontpush-position-css-relative-absolute-coordenadas]]: bolinhas animadas por `top`/`left` (layout a cada quadro); `transform: translate()` faria o mesmo no compositor
- [[wiki/sources/frontpush-conclusao-modulo-css-estilo-layout-animacao-documentacao]]: `@keyframes` anunciado como "módulo de animação" para micro-interações
- [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]: NLW #2, dia 2: transition de background e opacity
- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: NLW #2, dia 3: transition sem propriedade; translateY
