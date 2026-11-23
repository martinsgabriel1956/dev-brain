---
type: concept
title: "Animação por sequência de frames no scroll"
aliases: ["scroll-driven image sequence", "scrollytelling estilo Apple", "vídeo controlado pelo scroll", "image sequence on scroll"]
date_created: 2026-11-23
date_updated: 2026-11-23
source_count: 1
tags: [frontend, animacao, scroll, canvas, performance, landing-page, hero]
skill: tech-mentor-ai
status: stub
---

# Animação por sequência de frames no scroll

Efeito de página de produto "estilo [[wiki/entities/apple|Apple]]": um vídeo parece tocar para frente e para trás conforme o usuário rola a página. Na prática, o vídeo é exportado como **sequência de imagens**, e o scroll escolhe qual frame mostrar.

Em [[wiki/sources/frontpush-ia-como-eu-crio-imagens-e-videos-com-ia]], [[wiki/entities/nasser|Násser]] gerou o vídeo com IA ([[wiki/concepts/pipeline-de-midia-com-ia]]), passou pelo Premiere, exportou os frames e os "coloquei em ordem". O efeito está na [[wiki/concepts/secao-hero|hero]] do site do joystick, feito em código nativo. Ele nota que o Framer tem algo parecido pronto.

## Como costuma ser implementado `[external]`

Confiança alta para a técnica e média para os números. Referência clássica: [CSS-Tricks, "Let's make one of those fancy scrolling animations used on Apple product pages"](https://css-tricks.com/lets-make-one-of-those-fancy-scrolling-animations-used-on-apple-product-pages/), sem fetch.

- Um `<canvas>` fixo (`position: sticky`). A cada scroll, calcula-se `frameIndex = round(progresso × (n − 1))` e desenha-se a imagem com `drawImage` dentro de `requestAnimationFrame`.
- As imagens são pré-carregadas (`new Image()`), para não piscar.
- Controlar um `<video>` pelo `currentTime` é a alternativa, mas trava se o vídeo não for codificado com keyframes frequentes (*all-intra*), porque o navegador só consegue saltar para quadros-chave.

## Custo

- Cem frames em 1080p, mesmo em WebP ou AVIF, somam vários MB. Ajuda reduzir o número de frames, servir uma versão menor no mobile e carregar sob demanda ([[wiki/concepts/otimizacao-de-imagens]]).
- O carregamento pesado bate no LCP, e o trabalho no scroll bate no INP ([[wiki/concepts/core-web-vitals]]). O próprio autor admite que o site "dá umas travadinhas" sob tráfego.

## Key Sources

- [[wiki/sources/frontpush-ia-como-eu-crio-imagens-e-videos-com-ia]]
