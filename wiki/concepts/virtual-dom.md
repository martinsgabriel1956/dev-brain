---
type: concept
title: "Virtual DOM"
aliases: ["VDOM", "virtual dom diffing"]
date_created: 2026-08-03
date_updated: 2026-08-04
source_count: 2
tags: [frontend, virtual-dom, reatividade, react, vue, performance]
skill: tech-mentor-frontend
status: stable
---

# Virtual DOM

Cópia leve da árvore de componentes mantida em memória (objetos JS), usada por frameworks como React e Vue para decidir **o que** mudou antes de tocar o [[wiki/concepts/dom]] real.

## Como funciona

1. Estado muda.
2. O framework re-executa as funções de render e produz uma **nova árvore virtual**.
3. Compara (diff) a árvore nova com a anterior — esse passo é a [[wiki/concepts/reconciliacao]].
4. Aplica só as diferenças encontradas no DOM real.

A vantagem de modelo mental: o dev escreve como se a UI inteira fosse recriada a cada render, mas o framework garante que só os nós que de fato mudaram sofrem mutação real de DOM — que é a operação cara.

## Alternativa: signals

Frameworks baseados em [[wiki/concepts/signals]] (Solid.js, Svelte, Vue via `ref`/`reactive`, Angular Signals) pulam o diffing inteiramente: ligam a variável reativa diretamente ao nó de DOM que depende dela. Não há árvore para comparar. Em benchmarks qualitativos, isso tende a vencer o Virtual DOM em listas muito grandes ou animações de alta frequência, porque elimina a etapa de comparação — o Virtual DOM continua adequado para a maioria das aplicações.

## Ver também

- [[wiki/concepts/reconciliacao]] — o algoritmo de diffing em si
- [[wiki/concepts/signals]] — abordagem concorrente sem diffing
- [[wiki/concepts/dom]] — o que está sendo evitado de tocar sem necessidade

## Key Sources

- [[wiki/sources/10-conceitos-internos-frameworks-frontend]]
- [[wiki/sources/react-reconciliacao-memo-usememo-usecallback]] — demonstração prática no React DevTools Profiler de que gerar uma nova versão na Virtual DOM não implica tocar o DOM real
