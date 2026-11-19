---
type: concept
title: "Code Splitting"
aliases: ["lazy loading de componentes", "chunking de bundle"]
date_created: 2026-08-03
date_updated: 2026-11-19
source_count: 5
tags: [frontend, bundler, code-splitting, lazy-loading, performance]
skill: tech-mentor-frontend
status: stable
---

# Code Splitting

Técnica de dividir o bundle de JavaScript em pedaços (chunks) menores, carregados sob demanda em vez de tudo de uma vez no carregamento inicial.

## Como funciona na prática

Um usuário que acessa a Home baixa só o JavaScript necessário para a Home; ao navegar para o Dashboard, o chunk do Dashboard é baixado nesse momento. Todo framework moderno expõe uma forma de marcar um componente como *lazy* (ex. `React.lazy` + `Suspense`, `defineAsyncComponent` no Vue, `import()` dinâmico), e o bundler automaticamente separa esse componente em seu próprio chunk.

## Complementar a: tree shaking

[[wiki/concepts/tree-shaking]] remove código que nunca é usado; code splitting reorganiza código que **é** usado em pedaços menores carregados conforme a necessidade. Juntos, reduzem o tempo até a aplicação ficar visível e interativa (relacionado a Core Web Vitals como LCP e TTI).

## Ver também

- [[wiki/concepts/tree-shaking]]
- [[wiki/concepts/hydration]] — outra técnica que reduz JavaScript enviado/executado desnecessariamente (islands architecture)

## O "CSS quebrado" do web app (FrontPUSH, otimização aula 02)

Em [[wiki/sources/frontpush-cache-e-cdn-css-js-inline-incorporado-externo]], "cada componente tem o seu respectivo CSS" e "o CSS quebrado lá é mais vantajoso" no web app. É code splitting (CSS e JS da rota baixados quando ela é visitada), embora a aula atribua ao Virtual DOM. Vale também para página normal, com um CSS por página.

## "JavaScript não utilizado" (FrontPUSH, otimização aula 06)

Em [[wiki/sources/frontpush-relatorio-pagespeed-imagens-render-blocking-dom-regra-80-20]], JS sem uso é confundido com render-blocking. São avisos diferentes: código que nunca executa se resolve com code splitting e [[wiki/concepts/tree-shaking]]; o bloqueio, com `defer`/`async`.

## Key Sources

- [[wiki/sources/10-conceitos-internos-frameworks-frontend]]

## Key sources (adição 2026-11-10)

- [[wiki/sources/lazy-load-eager-load-economia-dados-react-trpc]] — lazy loading de JavaScript e embeds pesados como extensão de [[wiki/concepts/lazy-vs-eager-loading]]
- [[wiki/sources/frontpush-spa-componentes-estrutura-app-js-componentizacao]]: FrontPUSH, React aula 05: "carregando somente o que é realmente necessário" só vale para o código com lazy
- [[wiki/sources/frontpush-cache-e-cdn-css-js-inline-incorporado-externo]]: FrontPUSH, otimização aula 02: CSS dividido no web app
- [[wiki/sources/frontpush-relatorio-pagespeed-imagens-render-blocking-dom-regra-80-20]]: FrontPUSH, otimização aula 06: JS sem uso × render-blocking
