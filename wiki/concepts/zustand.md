---
type: concept
title: "Zustand"
aliases: ["zustand estado global", "create store zustand"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
tags: [react, zustand, estado-global, hooks, observer-pattern]
skill: tech-mentor-frontend
status: draft
---

# Zustand

Biblioteca de gerenciamento de estado global para React que **não exige `Provider`**: o estado vive num módulo, fora da árvore de componentes, e cada componente se conecta a ele via um Hook (`useStore`). Resolve o mesmo problema de [[wiki/concepts/context-api|prop drilling]] que Context API e Redux, mas sem re-render em cascata de providers aninhados e sem boilerplate de dispatch/reducer.

## Mecanismo essencial (por trás da API)

Na essência, uma store Zustand é a combinação de duas peças:

1. **Um [[wiki/concepts/observer-pattern|Observer]]** — uma lista de listeners (`subscribe`/`unsubscribe`) e uma função `emit`/`setState` que notifica todos eles quando o valor muda.
2. **Um Hook de sincronização** — usa `useState` (ou, na implementação oficial do Zustand, `useSyncExternalStore`) para espelhar o valor externo dentro do ciclo de render do React, inscrevendo-se no observer via `useEffect` e cancelando a inscrição no cleanup.

É possível recriar esse mecanismo central com ~40 linhas de JavaScript puro (`Set` para os listeners, `Map` para o valor, `useState` + `useEffect` para a sincronização) — ver [[wiki/sources/recriando-zustand-javascript-puro-sem-provider]] para uma implementação didática completa e testada.

## Por que não precisa de Provider

Diferente da Context API, a store não é criada dentro da árvore de componentes — é um módulo JavaScript comum, instanciado uma vez e importado onde for necessário (efetivamente um [[wiki/concepts/singleton-pattern|singleton]] de módulo). Qualquer componente que importa a store e chama o Hook se inscreve diretamente nela, sem precisar estar dentro de um `<Provider>` ancestral.

## Diferença para uma implementação artesanal (`useState` + `useEffect` manual)

A API real do Zustand usa `useSyncExternalStore` (React 18+) em vez de `useState` + `useEffect` manuais para essa sincronização. A diferença importa em Concurrent Mode: `useSyncExternalStore` garante que múltiplos componentes lendo a mesma store nunca "rasguem" (tearing) — ou seja, nunca renderizam com valores diferentes da mesma store dentro do mesmo commit. Uma implementação manual com `useState`/`useEffect`, como a de [[wiki/sources/recriando-zustand-javascript-puro-sem-provider]], reproduz o comportamento básico mas não dá essa garantia formal — o próprio vídeo-fonte reconhece "problemas de concorrência" e "de renderização" como limitações conhecidas.

## Quando usar (comparado a Context API)

| Frequência de mudança | Solução |
|---|---|
| Baixa (tema, auth, locale) | [[wiki/concepts/context-api]] |
| Alta (carrinho, filtros, UI state complexo) | Zustand / Jotai |
| Dados do servidor | TanStack Query |

## Key Sources

- [[wiki/sources/recriando-zustand-javascript-puro-sem-provider]] — reimplementação didática do mecanismo central (Observer + Map + useState/useEffect) sem Provider
