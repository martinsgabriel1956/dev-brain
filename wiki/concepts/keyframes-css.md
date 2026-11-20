---
type: concept
title: "Keyframes e animation no CSS"
aliases: ["@keyframes", "keyframe", "quadro-chave", "CSS Animations", "animation CSS", "linha do tempo no CSS"]
date_created: 2026-11-20
date_updated: 2026-11-20
source_count: 2
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

## Key sources

- [[wiki/sources/frontpush-principios-motion-linha-do-tempo-keyframes-transicao-entre-estados]]: FrontPUSH, mini curso de CSS Animations, aula 03: linha do tempo, N estados, bolinha `bounce in` e órbitas
- [[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]]: FrontPUSH, mini curso de CSS Animations, aula 04: keyframe appear em CSS puro; bibliotecas CSS
