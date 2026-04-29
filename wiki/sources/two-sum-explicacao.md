---
type: source
title: "Two Sum — Explicação Completa"
aliases: ["two sum", "hash map complemento", "two sum algorithm", "produtor consumidor hash map"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/two-sum-explicacao.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [algorithms, hash-map, two-sum, complement-pattern, cs-fundamentals]
skill: cs-fundamentals
status: stable
---

## TL;DR

Two Sum: dado um array e um target, retornar índices de dois números que somam o target. Solução naïve O(n²) usa dois loops. Solução ótima O(n) usa um hash map para armazenar o complemento (target - valor atual) enquanto itera. A lógica central é produtor/consumidor: cada elemento deixa um "pedido" no map; o par o encontra nas iterações seguintes.

## Key Claims

**Claim:** Hash map transforma Two Sum de O(n²) para O(n) eliminando o loop interno.
**Evidence:** Solução naïve: para cada elemento i, iterar de i+1 até n procurando o complemento → O(n²). Solução ótima: para cada elemento, verificar se `map.has(target - current)` → O(1) lookup. Uma única passagem pelo array resolve o problema. Space trade-off: O(n) de memória adicional para o map.
**Confidence:** alta

**Claim:** A lógica produtor/consumidor explica o algoritmo de forma intuitiva — o encontro sempre acontece no segundo elemento do par.
**Evidence:** Iteração passada produz um "pedido" no hash map: `map.set(target - current, index)` ou `map.set(current, index)`. Iteração futura consulta se ela mesma é o complemento pedido: `map.has(target - current)`. O segundo elemento do par é quem olha para trás, encontra o recado, e encerra o algoritmo. O primeiro elemento nunca sabe quem é seu par — apenas deixa registrado o que está faltando.
**Confidence:** alta

**Claim:** Python e TypeScript invertem quando a subtração acontece, mas o resultado é idêntico.
**Evidence:** Python: armazena `target - i` como chave (o complemento), consulta se `i` existe. TypeScript: armazena `i` (valor atual) como chave, consulta se `target - current` existe. Ambas as abordagens respondem a mesma pergunta: "já vi o complemento antes?" — apenas invertem qual lado da equação vai para a chave do map.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/hash-map]]
- [[concepts/complement-pattern]]
- [[concepts/time-space-tradeoff]]
- [[concepts/two-pointer]]

## Open Questions

- Variantes: Two Sum com array ordenado — two pointers O(n) sem espaço extra, vale a pena?
- Three Sum generaliza o mesmo padrão com sort + two pointers — qual é o limite dessa generalização?
