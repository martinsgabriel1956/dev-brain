---
type: concept
title: "Core Web Vitals"
aliases: ["Web Vitals", "LCP INP CLS", "métricas de experiência do Google", "CrUX"]
date_created: 2026-11-19
date_updated: 2026-11-23
source_count: 7
tags: [performance, web-performance, core-web-vitals, seo, lcp, inp, cls, fcp, ttfb, lighthouse, crux]
skill: tech-mentor-frontend
status: stub
---

# Core Web Vitals

Métricas do Google para a experiência de carregamento e uso de uma página, medidas em usuários reais (dado de campo do CrUX, o Chrome UX Report) no 75º percentil. Desde 12/03/2024 são três (`[external]` https://web.dev/articles/vitals, https://web.dev/blog/inp-cwv-launch):

| Métrica | Mede | Bom |
|---|---|---|
| **LCP** (Largest Contentful Paint) | quando o maior elemento visível foi pintado | ≤ 2,5 s |
| **INP** (Interaction to Next Paint) | atraso entre interação e próxima pintura; substituiu o FID | ≤ 200 ms |
| **CLS** (Cumulative Layout Shift) | quanto o layout pula durante o uso | ≤ 0,1 |

Métricas de diagnóstico, fora do trio: **TTFB** (Time to First Byte, a resposta do servidor), **FCP** (First Contentful Paint, o primeiro conteúdo pintado). TTFB alto atrasa tudo; CSS e JS que bloqueiam a renderização atrasam FCP e LCP ([[wiki/concepts/critical-rendering-path]]).

## Campo × laboratório

O Lighthouse (DevTools, PageSpeed Insights) dá notas de 0 a 100 em Desempenho, Acessibilidade, Práticas recomendadas e SEO, numa simulação com rede e CPU lentas. O PageSpeed Insights mostra essas notas e, acima, o dado de campo do CrUX. O ranking do Google usa o campo, não a nota. `[skill: tech-mentor-frontend]`

## SEO

O Google usa os Core Web Vitals nos sistemas de ranking como parte da "experiência de página", mas diz que conteúdo relevante vem antes; não afetam a indexação. `[external]` https://developers.google.com/search/docs/appearance/page-experience

## No FrontPUSH

Em [[wiki/sources/frontpush-introducao-otimizacao-web-minificacao-css-js]], [[wiki/entities/nasser|Násser]] mostra uma página sua no PageSpeed (97/90/95/100) e o "relatório do UX, do Chrome", e promete aulas sobre FCP, INP e TTFB. Mistura métricas de diagnóstico com um Core Web Vital e não cita LCP nem CLS. A presença do INP ajuda a datar a aula em 2023–2024.

## Ver também

- [[wiki/concepts/pipeline-de-assets]]: arquivos menores chegam antes.
- [[wiki/concepts/otimizacao-de-imagens]]: a imagem do hero costuma ser o elemento do LCP.
- [[wiki/concepts/lazy-vs-eager-loading]]: lazy load ajuda, mas não na imagem do LCP.
- [[wiki/concepts/code-splitting]]: menos JS no começo, melhor INP.

## Lazy loading e LCP/CLS (FrontPUSH, otimização aula 03)

Em [[wiki/sources/frontpush-otimizacao-de-imagens-svg-webp-lazy-loading]], `loading="lazy"` "em todas as imagens", inclusive num logo. Lazy na imagem acima da dobra atrasa o LCP; lazy sem `width`/`height` causa CLS.

## Imagem por dispositivo e LCP (FrontPUSH, otimização aula 04)

Em [[wiki/sources/frontpush-otimizacao-de-imagens-mobile-desktop-classes-mixin]], a imagem grande no celular é o aviso do PageSpeed. Baixar as duas imagens (escondendo uma) ou trocar para `background-image` (descoberto só depois do CSS) pode piorar o LCP se for a imagem principal.

## FCP e FID no lugar de LCP e INP (FrontPUSH, otimização aula 05)

Em [[wiki/sources/frontpush-google-pagespeed-core-web-vitals-acessibilidade-meta-tags]], os três principais são "carregamento do primeiro elemento visível, tempo de interação e mudança de layout". A ideia bate com LCP, INP e CLS, mas os números não: o "primeiro elemento" é apresentado como FCP com limite de 2,5 s (que é o do LCP; o FCP bom é ≤ 1,8 s), e a interação com limite de 100 ms é o FID, aposentado em março de 2024 (o INP bom é ≤ 200 ms). CLS é chamado de "dark pattern"; a métrica mede o pulo do layout, não a intenção.

## Diagnósticos sem nome de métrica (FrontPUSH, otimização aula 06)

Em [[wiki/sources/frontpush-relatorio-pagespeed-imagens-render-blocking-dom-regra-80-20]], a aula lê só os avisos de diagnóstico (imagens, render-blocking, payload, fontes, DOM). Eles alimentam LCP, CLS e INP, mas a aula não liga cada aviso à métrica: render-blocking e imagens pesam no LCP, `font-display` no FCP e no CLS, DOM grande no INP.

## Loader e animação em JS (FrontPUSH, otimização aula 07)

Em [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]]: a tela de carregamento esconde a página e atrasa o LCP (maior elemento *visível*); site "montado às coxas" se corrige com `font-display`, `width`/`height` e CSS crítico. Animação dirigida por JS ocupa a thread principal e pesa no INP.

## Sequência de frames e vídeo pesado (FrontPUSH, módulo de IA)

O site do joystick em [[wiki/sources/frontpush-ia-como-eu-crio-imagens-e-videos-com-ia]] "dá umas travadinhas" e demora "para poder carregar algumas mídias" sob tráfego. É o custo de uma hero feita com [[wiki/concepts/animacao-por-sequencia-de-frames-no-scroll|frames no scroll]]: muitas imagens grandes pesam no LCP, e o desenho no scroll pesa no INP. A resposta da aula é baixar a resolução para 1080p30. Pré-carregamento, formato e quantidade de frames ficam sem resposta.

## Key sources

- [[wiki/sources/frontpush-introducao-otimizacao-web-minificacao-css-js]]: FrontPUSH, otimização aula 01: FCP, INP, TTFB e o PageSpeed
- [[wiki/sources/frontpush-otimizacao-de-imagens-svg-webp-lazy-loading]]: FrontPUSH, otimização aula 03: lazy loading mal aplicado piora LCP e CLS
- [[wiki/sources/frontpush-otimizacao-de-imagens-mobile-desktop-classes-mixin]]: FrontPUSH, otimização aula 04: imagem responsiva e LCP
- [[wiki/sources/frontpush-google-pagespeed-core-web-vitals-acessibilidade-meta-tags]]: FrontPUSH, otimização aula 05: os três principais, com FCP e FID
- [[wiki/sources/frontpush-relatorio-pagespeed-imagens-render-blocking-dom-regra-80-20]]: FrontPUSH, otimização aula 06: diagnósticos do relatório
- [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]]: FrontPUSH, otimização aula 07: loader × LCP; animação JS × INP
- [[wiki/sources/frontpush-ia-como-eu-crio-imagens-e-videos-com-ia]]: FrontPUSH, módulo de IA aula 01: mídia pesada na hero
