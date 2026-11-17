---
type: concept
title: "Virtual DOM"
aliases: ["VDOM", "virtual dom diffing"]
date_created: 2026-08-03
date_updated: 2026-11-17
source_count: 8
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

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]], o aviso "Each child in a list should have a unique key prop" e a explicação: a `key` serve "pro React conseguir encontrar esse elemento na hora de atualizar".

Em [[wiki/sources/frontpush-dom-parte-2-criar-elementos-createelement-appendchild]], o React é apresentado como "tudo JavaScript" que "renderiza o HTML" com os princípios de `createElement`/`appendChild`. Por baixo são essas APIs, mas o React decide o que mudar comparando árvores, em vez de anexar nó a nó.

## Key Sources

- [[wiki/sources/10-conceitos-internos-frameworks-frontend]]
- [[wiki/sources/react-reconciliacao-memo-usememo-usecallback]] — demonstração prática no React DevTools Profiler de que gerar uma nova versão na Virtual DOM não implica tocar o DOM real

## Na NLW #2, dia 1 (Diego Fernandes)

Diego explica o React pela ideia de SPA ("só muda [...] as coisas que são diferentes de uma tela para outra"), sem citar a virtual DOM; o que o React trouxe foi a re-renderização declarativa de componentes, não a SPA em si. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]].

## Na NLW #2, dia 3 (Diego Fernandes)

"Each child in a list should have a unique key prop": a key vai no primeiro elemento do `map` e "ajuda o React a conseguir identificar os elementos". Nos horários, a key é o `week_day`, que duplica no primeiro clique (os dois itens começam com 0). Ver [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]].

## Key sources (adição 2026-10-14)
- [[wiki/sources/historia-do-front-end-akita-ep4]] — contexto histórico: mudar o estado e deixar o Virtual DOM redesenhar ([[wiki/concepts/single-page-application]])
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: key em listas para reconciliação
- [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]: NLW #2, Diego, dia 1: SPA × re-renderização declarativa
- [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]]: NLW #2, Diego, dia 3: key nas options e nos horários
- [[wiki/sources/frontpush-dom-parte-2-criar-elementos-createelement-appendchild]]: FrontPUSH, JavaScript aula 09: o princípio por baixo do React
- [[wiki/sources/frontpush-conceitos-gerais-react-interface-dinamica-spa-virtual-dom-jsx]]: FrontPUSH, React aula 03: "cópia virtual" para comparar antes de renderizar; o ganho é viabilizar o declarativo, não ser o mais rápido
