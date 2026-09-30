---
type: concept
title: "Quicksort"
aliases: ["quick sort", "quicksort", "ordenação rápida"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [cs-fundamentals, algoritmos, sorting, quicksort, recursao, dividir-para-conquistar, big-o]
skill: cs-fundamentals
status: draft
---

# Quicksort

Algoritmo de ordenação de [[wiki/concepts/dividir-para-conquistar]]: escolhe um **pivô**, particiona o array em menores e maiores que o pivô e ordena cada parte recursivamente.

## Estrutura

1. **Caso base:** array vazio ou com 1 elemento (`len(array) < 2`) já está ordenado — retorna como está. (Array de 2 elementos não é caso base; é resolvido pela recursão.)
2. **Pivô:** escolhe um elemento — ver [[wiki/concepts/escolha-de-pivo]].
3. **Particionamento:** subarray dos menores + pivô + subarray dos maiores (ainda não ordenados).
4. **Recursão:** aplica o Quicksort nos dois subarrays; o resultado é `esquerdo_ordenado + [pivô] + direito_ordenado`.

Funciona com **qualquer** pivô; a escolha só muda a velocidade. Exemplo de [10, 15, 33, 7]: pivô 33 → menores [10, 15, 7], maiores []; recursão em [10, 15, 7] com pivô 10 → [7] e [15] (casos base).

## Por que O(n log n) (caso médio)

- Cada nível de recursão percorre todos os elementos uma vez para separar menores e maiores → **O(n) por nível**.
- Se o pivô divide o array ~ao meio, há ~**log n níveis** (comportamento de [[wiki/concepts/logaritmo]]).
- Total: n × log n.

## Pior caso O(n²)

Ocorre quando o pivô escolhido é sempre um extremo (partição desbalanceada: um subarray vazio, outro com n−1 elementos) — n níveis em vez de log n. Com pivô = primeiro elemento, um array já ordenado (ou invertido) provoca isso. Ver [[wiki/concepts/melhor-caso-pior-caso-caso-medio]].

## Uso e comparações

- O livro afirma que a `qsort` da biblioteca padrão de C implementa Quicksort (não verificado — o padrão C não fixa o algoritmo).
- vs. [[wiki/concepts/selection-sort]] (O(n²)): ~996 s vs. ~27 h para n = 1000 no quadro ilustrativo (10 ops/s).
- vs. [[wiki/concepts/bubble-sort]]: recursivo e particionador vs. iterativo com loops aninhados.
- Espaço O(log n) (pilha), in-place, não estável [skill: cs-fundamentals]; detalhes e código em [[wiki/concepts/algoritmos-de-ordenacao]].
- [[wiki/concepts/recursao]] é o mecanismo; o caso base é o que encerra a descida.

## Key sources

- [[wiki/sources/ordenacao-selection-quicksort-bubble-sort-live-coding]] — caso base `len < 2`, particionamento, n por nível × log n níveis, pior caso O(n²) dependente do pivô
