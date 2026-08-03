---
type: concept
title: "Code Splitting"
aliases: ["lazy loading de componentes", "chunking de bundle"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
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

## Key Sources

- [[wiki/sources/10-conceitos-internos-frameworks-frontend]]
