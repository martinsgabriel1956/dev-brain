---
type: concept
title: "Bubble Sort"
aliases: ["bubble sort", "ordenação por bolha"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [cs-fundamentals, algoritmos, sorting, bubble-sort, big-o]
skill: cs-fundamentals
status: draft
---

# Bubble Sort

Algoritmo de ordenação por trocas: dois loops aninhados percorrem o array comparando pares e fazendo *swap* (com variável temporária) quando um está fora de ordem, até tudo ficar ordenado.

## Complexidade

- **Pior caso: O(n²)** — dois `for` sobre todos os elementos.
- **Melhor caso: O(n)** segundo a tabela do GeeksforGeeks citada na fonte — mas isso só vale para a variante otimizada que encerra quando uma passada não realiza trocas; a versão de dois `for` completos é O(n²) em qualquer entrada [external] https://www.geeksforgeeks.org/bubble-sort-algorithm/.
- Espaço O(1), in-place, estável [skill: cs-fundamentals].

## Contraste com o Quicksort

O [[wiki/concepts/quicksort]] é recursivo e particiona o array a cada chamada; o Bubble Sort é iterativo, sem recursão. No pior caso (pivô ruim) o Quicksort chega ao mesmo O(n²) do Bubble Sort — a vantagem dele depende da [[wiki/concepts/escolha-de-pivo]].

## Ver também

- [[wiki/concepts/algoritmos-de-ordenacao]] · [[wiki/concepts/melhor-caso-pior-caso-caso-medio]] · [[wiki/concepts/big-o]]

## Key sources

- [[wiki/sources/ordenacao-selection-quicksort-bubble-sort-live-coding]] — for dentro de for + swap com variável temporária; melhor O(n) / pior O(n²); contraste com Quicksort recursivo
