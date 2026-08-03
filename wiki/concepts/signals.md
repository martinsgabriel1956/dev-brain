---
type: concept
title: "Signals (Reatividade Fine-Grained)"
aliases: ["fine-grained reactivity", "reatividade granular", "signals reativos"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
tags: [frontend, signals, reatividade, solid-js, svelte, performance]
skill: tech-mentor-frontend
status: stable
---

# Signals

Abordagem de reatividade em que o framework liga uma variável reativa **diretamente** ao(s) nó(s) de [[wiki/concepts/dom]] que dependem dela, em vez de comparar árvores inteiras a cada mudança como no [[wiki/concepts/virtual-dom]].

## Como difere do Virtual DOM

- **Virtual DOM**: a cada mudança de estado, recria a árvore inteira em memória, faz diff contra a anterior ([[wiki/concepts/reconciliacao]]), aplica só as diferenças.
- **Signals**: quando o valor muda, o framework já sabe exatamente qual instrução de DOM executar — sem recriar árvore, sem diff, sem varredura.

Algumas implementações resolvem isso em tempo de execução via proxies (ex. `ref`/`reactive` do Vue); outras vão além e resolvem em tempo de compilação, gerando JavaScript que já embute as instruções de atualização de DOM para cada mudança de estado (Solid.js, Svelte via runes `$state`/`$derived`/`$effect`).

## Trade-off prático

Virtual DOM é suficiente e ergonômico para a maioria das aplicações. Signals tendem a ganhar em listas com milhares de itens ou animações de alta frequência, porque eliminam a etapa de comparação — o custo cresce com o tamanho da árvore no VDOM, mas não em reatividade granular.

## Ver também

- [[wiki/concepts/virtual-dom]] — a abordagem concorrente baseada em diffing

## Key Sources

- [[wiki/sources/10-conceitos-internos-frameworks-frontend]]
