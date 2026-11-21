---
type: concept
title: "transition e transform no CSS (hover suave)"
aliases: ["transition", "transform", "scale", "transform: scale", "hover animado", "transição CSS"]
date_created: 2026-11-16
date_updated: 2026-11-20
source_count: 15
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

## transform no Can I use (FrontPUSH, Sass)

Em [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]], `transform` é o exemplo de prefixos: `-ms-` no IE 9, `-webkit-` no Safari antigo, `-moz-` no Firefox antigo; 98% de suporte com prefixo e 96% sem. Ver [[wiki/concepts/prefixo-de-fornecedor]].

## Sombra suave no hover (FrontPUSH, Sass)

Em [[wiki/sources/frontpush-variaveis-sass]]: `transition` de 0.5 s "para que essa transição seja suave" no `box-shadow` do hover. A legenda não diz se ficou na regra base; se ficou só no `:hover`, a volta é seca.

Em [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]], `transition: 1s ease` na classe `.red` suaviza a troca feita por `classList.toggle` no clique: o JavaScript troca a classe, o CSS anima.

## Otimização de animações (FrontPUSH, otimização aula 07)

Em [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]], "priorize o CSS puro" e anime `transform`/`opacity` em vez de `width`. Ressalvas: só `transform`/`opacity` (e às vezes `filter`) saem da thread principal; `@keyframes` de `width` ou `box-shadow` não. `will-change: transform` só pouco antes de animar e em poucos elementos. Falta `prefers-reduced-motion`.

## Transição entre estados (FrontPUSH, motion aula 01)

Em [[wiki/sources/frontpush-introducao-motion-design-css-animations-grade-do-curso]], [[wiki/entities/nasser|Násser]] define motion como "transição entre estados com determinados níveis de velocidade diferentes entre eles" ([[wiki/concepts/motion-design]]). Os "níveis de velocidade" são a função de temporização (`transition-timing-function`, `animation-timing-function`: `ease`, `cubic-bezier()`, `steps()`, `linear()`). `[skill: tech-mentor-frontend]`

## Keyframes e as propriedades do transform (FrontPUSH, motion aula 03)

Em [[wiki/sources/frontpush-principios-motion-linha-do-tempo-keyframes-transicao-entre-estados]], os [[wiki/concepts/keyframes-css]] mudam escala, opacidade, translado e skew ("deitar o objeto"), e as órbitas giram de 0 a 360deg em 7 s. `transition` liga dois estados; `@keyframes`, N estados. Duas animações de `transform` no mesmo elemento brigam: a última vence; usar pai e filho ou `scale`/`rotate` individuais. A velocidade entre estados é o [[wiki/concepts/easing]].

## Quem anima é o CSS (FrontPUSH, motion aula 04)

Em [[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]]: "é o CSS que manipula todo e qualquer elemento de Motion" (scale, opacity, translate, rotate). "Entortar [...] com a propriedade de scale" deveria ser `skew`. Precisão: bibliotecas JS escrevem essas propriedades, mas calculam os quadros na thread principal ([[wiki/concepts/css-puro-vs-biblioteca-de-animacao]]).

## As funções do transform, uma a uma (FrontPUSH, básico CSS aula 01)

Em [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]], [[wiki/entities/nasser|Násser]] passa pelo slide do `transform`: `rotate` em `deg` em torno do centro (o "ponto de ancoragem", `transform-origin`, fica para a próxima aula); `translate` em px a partir da posição inicial, com o Y invertido (positivo desce) e Z invisível sem perspectiva; `scale` como juros (1,2 = +20%, 0,7 = −30%); `skewX`/`skewY`; várias funções separadas por espaço; e `matrix` como resumo ([[wiki/concepts/transform-matrix-css]]). O 3D fica com [[wiki/concepts/perspective-css]]. Precisões: `translate(50px, 100px)` é um deslocamento só, não "primeiro x, depois y"; a ordem importa *entre* funções; `skew(50deg, 50deg)` espelha a caixa em vez de "esticar mais"; `transform` não mexe no fluxo, então o "hack" de layout deixa o espaço original reservado.

## transform-origin, transform-style e transition all (FrontPUSH, básico CSS aula 02)

Em [[wiki/sources/frontpush-propriedade-transform-parte-2-transform-origin-transform-style-preserve-3d]], as duas propriedades que "ajudam a configurar a propriedade transform": [[wiki/concepts/transform-origin-css]] (o eixo de rotação) e `transform-style` ([[wiki/concepts/perspective-css]]). A demo gira 180° no `:hover` com `transition: all 1s ease`, "para não ficar bruto". `all` anima qualquer propriedade que mude; nomear `transform` é mais seguro.

## transition = dois estados (FrontPUSH, básico CSS aula 03)

Em [[wiki/sources/frontpush-propriedade-animation-parte-1-keyframes-from-to-duration-direction-fill-mode]]: "a limitação do transition é que eu consigo utilizar apenas dois estados, um inicial e um final"; `animation` faz "essas configurações do transition e um pouco mais", com N estados ([[wiki/concepts/keyframes-css]]). O foco do módulo em `transform` é porque "com ela a gente vai conseguir fazer efeitos que com as propriedades básicas do CSS talvez a gente não consiga".

## Key sources

- [[wiki/sources/frontpush-layout-css-botao-hover-flexbox-media-query]]: `:hover` com `transform: scale` e `transition` de 1 s / 300 ms `ease`
- [[wiki/sources/frontpush-position-css-relative-absolute-coordenadas]]: bolinhas animadas por `top`/`left` (layout a cada quadro); `transform: translate()` faria o mesmo no compositor
- [[wiki/sources/frontpush-conclusao-modulo-css-estilo-layout-animacao-documentacao]]: `@keyframes` anunciado como "módulo de animação" para micro-interações
- [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]: NLW #2, dia 2: transition de background e opacity
- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: NLW #2, dia 3: transition sem propriedade; translateY
- [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]]: introdução ao Sass: suporte e prefixos de `transform`
- [[wiki/sources/frontpush-variaveis-sass]]: Sass aula 04: transition no box-shadow
- [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown]]: FrontPUSH, JavaScript aula 10: transition na classe trocada pelo JS
- [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]]: FrontPUSH, otimização aula 07: CSS puro, transform/opacity, will-change
- [[wiki/sources/frontpush-introducao-motion-design-css-animations-grade-do-curso]]: FrontPUSH, mini curso de CSS Animations, aula 01: motion como transição entre estados com velocidades diferentes (easing)
- [[wiki/sources/frontpush-principios-motion-linha-do-tempo-keyframes-transicao-entre-estados]]: FrontPUSH, mini curso de CSS Animations, aula 03: keyframes de scale, skew e rotate; transition × @keyframes
- [[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]]: FrontPUSH, mini curso de CSS Animations, aula 04: transform como base de todo motion
- [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 01: funções de transform uma a uma; Y invertido; scale como juros; matrix; perspectiva
- [[wiki/sources/frontpush-propriedade-transform-parte-2-transform-origin-transform-style-preserve-3d]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 02: transform-origin, transform-style, transition all 1s ease no hover
- [[wiki/sources/frontpush-propriedade-animation-parte-1-keyframes-from-to-duration-direction-fill-mode]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 03: transition limitada a dois estados; animation com N
