---
type: concept
title: "Selection Sort"
aliases: ["ordenação por seleção", "selection sort"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [cs-fundamentals, algoritmos, sorting, selection-sort, big-o]
skill: cs-fundamentals
status: draft
---

# Selection Sort

Algoritmo de ordenação mais simples: repete "achar o extremo (maior ou menor) do que sobrou e movê-lo para a posição correta" até esgotar a lista.

## Mecanismo (versão do livro *Entendendo Algoritmos*)

Exemplo: artistas com contagem de plays (Radiohead 156, Kishore Kumar 141, The Black Keys 35), do mais tocado ao menos tocado. Cria-se uma **nova lista** vazia; a cada rodada percorre-se a lista original, acha-se o artista com mais plays e ele é adicionado à nova lista. Repete-se até a original esgotar.

## Complexidade

- Achar o extremo = uma varredura, O(n).
- Repete-se n vezes → n × n = **O(n²)** (equivale a um `for` dentro de outro `for`).
- A cada rodada sobram menos elementos (n, n−1, n−2…, média ≈ n/2), mas a constante ½ é descartada — ver [[wiki/concepts/descarte-de-constantes-big-o]].
- Em campo (n = 1000, 10 ops/s): ~27 horas, contra ~996 s do [[wiki/concepts/quicksort]] [skill: cs-fundamentals — tempos ilustrativos].

## Ver também

- [[wiki/concepts/algoritmos-de-ordenacao]] — comparação com Bubble, Insertion, Merge, Quicksort e Heapsort (variante in-place, O(1) de espaço, não estável)
- [[wiki/concepts/bubble-sort]] — outro O(n²) com dois loops aninhados
- [[wiki/concepts/big-o]]

## Key sources

- [[wiki/sources/ordenacao-selection-quicksort-bubble-sort-live-coding]] — versão da lista-nova do livro; O(n) por seleção × n seleções = O(n²); por que a constante ½ cai
