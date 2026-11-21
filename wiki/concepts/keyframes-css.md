---
type: concept
title: "Keyframes e animation no CSS"
aliases: ["@keyframes", "keyframe", "quadro-chave", "CSS Animations", "animation CSS", "linha do tempo no CSS"]
date_created: 2026-11-20
date_updated: 2026-11-20
source_count: 5
tags: [keyframes, animacao, css, motion-design, linha-do-tempo, frontend]
skill: tech-mentor-frontend
status: stub
---

# Keyframes e animation no CSS

Keyframe (quadro-chave) é um ponto na linha do tempo de uma animação onde se fixa o valor de uma propriedade; os valores entre um ponto e outro são interpolados. Para [[wiki/entities/nasser|Násser]], "o keyframe é literalmente os pontos que você estabelece na linha do tempo que você consegue construir o seu motion" ([[wiki/sources/frontpush-principios-motion-linha-do-tempo-keyframes-transicao-entre-estados]]). É um dos três princípios de [[wiki/concepts/motion-design]] do mini curso, ao lado da linha do tempo e do [[wiki/concepts/easing]].

## No CSS

A regra `@keyframes` define os pontos em porcentagem da duração; a propriedade `animation` liga a regra ao elemento e define a linha do tempo:

```css
@keyframes aparecer {
  0%   { opacity: 0; transform: scale(0.3); }
  50%  { opacity: 1; transform: scale(1); }
  70%  { transform: scale(0.9); }
  100% { transform: scale(1); }
}

.bolinha {
  /* nome | duração | easing | delay | repetições | fill-mode */
  animation: aparecer 2s ease-out 0.5s 1 forwards;
}
```

- **Linha do tempo = `animation-duration`.** "Eu quero que essa animação dure dois segundos."
- **N estados.** Qualquer porcentagem vale, inclusive 0,5% ("quantos estados eu quiser").
- **Várias animações no mesmo elemento** separadas por vírgula. Se duas animam `transform`, a última da lista vence; separar em elemento-pai e filho ou usar as propriedades individuais `scale`, `rotate`, `translate`. `[skill: tech-mentor-frontend]`
- **`animation-fill-mode: forwards`** mantém o último keyframe ao terminar ("como é para terminar essa animação").
- **`transition` × `animation`.** `transition` vai de um estado a outro quando algo muda (hover, classe); `@keyframes` encadeia N estados e pode rodar sozinho ou em loop ([[wiki/concepts/transition-e-transform-css]]).

## Keyframes não são fps

O navegador gera os quadros intermediários a cada atualização da tela. Três keyframes rodam a 60 fps do mesmo jeito que trinta; o que define a fluidez é o custo de cada quadro ([[wiki/concepts/taxa-de-quadros-60fps]]). Animar `transform` e `opacity` mantém o custo baixo.

## Origem do termo

`[external]` Na animação tradicional, o animador principal desenhava as poses-chave e os assistentes faziam os intermediários (*in-betweens*). Ferramentas como o [[wiki/entities/after-effects|After Effects]] e o CSS herdaram o modelo: quem anima define as chaves, e o software faz os intermediários.

## Keyframes sem JavaScript (FrontPUSH, motion aula 04)

Em [[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]], o keyframe "appear" da aula 03 (opacidade 0 e escala 30% → opacidade 1 e escala 100%) é o exemplo de animação "puramente implementada em CSS". Bibliotecas CSS entregam classes com keyframes prontos ([[wiki/concepts/css-puro-vs-biblioteca-de-animacao]]).

## As subpropriedades de animation (FrontPUSH, básico CSS aula 03)

Em [[wiki/sources/frontpush-propriedade-animation-parte-1-keyframes-from-to-duration-direction-fill-mode]], [[wiki/entities/nasser|Násser]] passa por todas, com os exemplos do [[wiki/entities/w3schools]]:

| Propriedade | Valores | Nota `[external]` |
|---|---|---|
| `animation-name` | nome do `@keyframes` | evite palavras-chave como nome |
| `animation-duration` | s ou ms | a "linha do tempo" |
| `animation-timing-function` | `linear`, `ease`, `ease-in`, `ease-out`, `ease-in-out`, `cubic-bezier()`, `steps()` | vale **por intervalo** entre keyframes ([[wiki/concepts/easing]]) |
| `animation-delay` | s ou ms | negativo começa no meio |
| `animation-iteration-count` | número (aceita fração) ou `infinite` | `infinity` é inválido |
| `animation-direction` | `normal`, `reverse`, `alternate`, `alternate-reverse` | `alternate` pede 2+ repetições |
| `animation-fill-mode` | `none` (padrão), `forwards`, `backwards`, `both` | `forwards` guarda o último keyframe *executado* e vence a cascata |
| `animation-play-state` | `running`, `paused` | pausar no hover ou por classe |

`from`/`to` = `0%`/`100%`; três pontos ou mais pedem porcentagem. Ele usa o shorthand `animation: box 3s ease infinite alternate` e diz que "infinite e alternate" é o padrão da maioria das animações dele; loops assim pedem um jeito de pausar (WCAG 2.2.2). A demo anima `width`, que refaz layout a cada quadro.

## A curva da animation (FrontPUSH, básico CSS aula 04)

Em [[wiki/sources/frontpush-propriedade-animation-parte-2-curvas-cubic-bezier-editor-chrome]], a `animation-timing-function` do shorthand troca `ease` por um `cubic-bezier()` copiado de [[wiki/entities/cubic-bezier-com]] ([[wiki/concepts/easing]]).

## Na prática: dois keyframes e várias animações (FrontPUSH, básico CSS aula 05)

Em [[wiki/sources/frontpush-propriedade-animation-pratica-keyframes-parent-box-varias-animacoes]]: `@keyframes box` (`rotateX` 0 → 360deg) na `.box` e `@keyframes parent` (`rotateY`) na `.parent`, com `animation: box 3s ease infinite alternate` e 10 s no pai. Com `iteration-count` 3, para e volta ao estilo da classe. Uma segunda animação, `changeColor` (`background-color` red → blue), entra na mesma classe separada por vírgula, "totalmente independente" porque mexe em outra propriedade. `[external]` Para giro contínuo, `linear` com direção `normal` evita o efeito pêndulo de `ease alternate`.

## Key sources

- [[wiki/sources/frontpush-principios-motion-linha-do-tempo-keyframes-transicao-entre-estados]]: FrontPUSH, mini curso de CSS Animations, aula 03: linha do tempo, N estados, bolinha `bounce in` e órbitas
- [[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]]: FrontPUSH, mini curso de CSS Animations, aula 04: keyframe appear em CSS puro; bibliotecas CSS
- [[wiki/sources/frontpush-propriedade-animation-parte-1-keyframes-from-to-duration-direction-fill-mode]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 03: todas as subpropriedades de animation; from/to; shorthand
- [[wiki/sources/frontpush-propriedade-animation-parte-2-curvas-cubic-bezier-editor-chrome]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 04: timing function trocada por cubic-bezier
- [[wiki/sources/frontpush-propriedade-animation-pratica-keyframes-parent-box-varias-animacoes]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 05: dois keyframes, várias animações por vírgula, contagem finita
