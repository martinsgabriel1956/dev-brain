---
type: concept
title: "Trade-off Tempo vs. Memória"
aliases: ["time-space tradeoff", "time complexity vs space complexity", "trade-off tempo x espaço"]
date_created: 2026-07-10
date_updated: 2026-08-04
source_count: 4
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

## Segundo exemplo: Longest Consecutive Sequence

[[wiki/sources/resolvendo-3-problemas-classicos-entrevista-coding-dsa]] documenta a mesma troca com outro par de soluções: transformar o array numa estrutura auxiliar (hash set, O(n) de espaço extra) permite checar membership em O(1) e resolver o problema inteiro em O(n) de tempo; a alternativa sem espaço extra (ordenar o array in-place) evita o custo de memória, mas paga O(n log n) de tempo pela ordenação. Mesmo raciocínio de Two Sum acima, aplicado a um problema diferente: gastar espaço para comprar velocidade.

## Big O mais baixo não é sempre a melhor opção

O trade-off deixa claro por que a notação assintoticamente menor nem sempre vence: se o espaço disponível é limitado, uma solução O(n²) em tempo mas O(1) em espaço pode ser a única viável. A escolha depende do limite real do problema — latência aceitável vs. memória disponível — não só da curva de crescimento. Ver [[wiki/concepts/big-o]].

## Índice de Banco de Dados como Exemplo Canônico

[[wiki/concepts/database-index]] é o mesmo trade-off aplicado a bancos de dados: a estrutura adicional (B-tree, hash, etc.) ocupa espaço em disco e torna cada `INSERT`/`UPDATE` mais lento (a árvore precisa se reordenar), em troca de busca em O(log n) ou O(1) em vez de O(n)/table scan. Por isso a regra de "só crie índice se o padrão de acesso justificar" — o trade-off só compensa quando há buscas suficientes sobre a coluna. Ver [[wiki/sources/indice-de-banco-de-dados]].

## Relação com outros conceitos

- [[wiki/concepts/big-o]] — a notação usada para expressar os dois lados do trade-off (complexidade de tempo e de espaço)
- [[wiki/concepts/hashmap]] — estrutura auxiliar clássica para trocar memória por velocidade de busca
- [[wiki/concepts/algoritmos-e-estruturas-de-dados]] — a escolha de estrutura já embute esse trade-off
- [[wiki/concepts/database-index]] — mesmo trade-off aplicado a índices de banco de dados

## Key sources

- [[wiki/sources/two-sum-explicacao]]
- [[wiki/sources/estruturas-de-dados-algoritmos-big-o-como-escolher]]
- [[wiki/sources/indice-de-banco-de-dados]] — índice de banco de dados como exemplo concreto de espaço/escrita trocado por velocidade de leitura
- [[wiki/sources/resolvendo-3-problemas-classicos-entrevista-coding-dsa]] — hash set (O(n) de espaço) trocado por O(n) de tempo em Longest Consecutive Sequence, contra O(n log n) de tempo sem espaço extra ao ordenar in-place
