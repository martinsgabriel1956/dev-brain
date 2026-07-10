---
type: concept
title: "Trade-off Tempo vs. Memória"
aliases: ["time-space tradeoff", "time complexity vs space complexity", "trade-off tempo x espaço"]
date_created: 2026-07-10
date_updated: 2026-07-10
source_count: 2
tags: [cs-fundamentals, big-o, complexidade, algoritmos, memoria]
skill: cs-fundamentals
status: draft
---

# Trade-off Tempo vs. Memória

Padrão recorrente em algoritmos: gastar mais memória para reduzir o número de passos necessários numa operação. É o raciocínio por trás de índices, caches e estruturas auxiliares que "parecem estranhas" à primeira vista porque preparam dados antes de precisar deles.

## O raciocínio

- Guardar só a estrutura original (ex: uma lista) força buscas a percorrer item por item — barato em memória, caro em tempo.
- Manter uma estrutura auxiliar por fora (ex: um índice por chave) ocupa mais espaço, mas acelera o acesso — caro em memória, barato em tempo.

Você paga memória adiantada para não pagar a busca inteira toda vez que precisar do dado.

## Exemplo concreto: Two Sum

[[wiki/sources/two-sum-explicacao]] documenta o exemplo mais direto desse trade-off: a solução ingênua de Two Sum é O(n²) no tempo e O(1) em espaço extra; usar um [[hashmap]] para guardar o complemento durante a iteração leva a O(n) no tempo, ao custo de O(n) de memória adicional.

## Big O mais baixo não é sempre a melhor opção

O trade-off deixa claro por que a notação assintoticamente menor nem sempre vence: se o espaço disponível é limitado, uma solução O(n²) em tempo mas O(1) em espaço pode ser a única viável. A escolha depende do limite real do problema — latência aceitável vs. memória disponível — não só da curva de crescimento. Ver [[wiki/concepts/big-o]].

## Relação com outros conceitos

- [[wiki/concepts/big-o]] — a notação usada para expressar os dois lados do trade-off (complexidade de tempo e de espaço)
- [[wiki/concepts/hashmap]] — estrutura auxiliar clássica para trocar memória por velocidade de busca
- [[wiki/concepts/algoritmos-e-estruturas-de-dados]] — a escolha de estrutura já embute esse trade-off

## Key sources

- [[wiki/sources/two-sum-explicacao]]
- [[wiki/sources/estruturas-de-dados-algoritmos-big-o-como-escolher]]
