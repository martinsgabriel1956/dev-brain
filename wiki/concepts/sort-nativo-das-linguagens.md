---
type: concept
title: "Sort Nativo das Linguagens"
aliases: ["sort nativo", "built-in sort", "Array.prototype.sort", "list.sort"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [cs-fundamentals, algoritmos, sorting, javascript, python, timsort, performance]
skill: cs-fundamentals
status: draft
---

# Sort Nativo das Linguagens

Funções como `.sort()` de JavaScript, Python e Java são algoritmos de ordenação já embalados. A tese da fonte: não tratá-las como caixa-preta — saber **qual algoritmo roda, qual sua complexidade e até que tamanho de entrada serve ao caso de uso**. A fonte levanta a pergunta mas não a responde.

## O que se sabe (fora da fonte)

- **JavaScript (V8, desde v7.0 / Chrome 70):** Timsort, "variante adaptativa e estável do Mergesort", O(n log n) no pior caso; antes usava Quicksort com Insertion Sort para arrays pequenos (instável, com pior caso O(n²)) [external] https://v8.dev/blog/array-sort.
- **Armadilha do JS:** sem função comparadora, os valores são convertidos com `toString()` e comparados lexicograficamente — ordenar números exige comparador (`(a, b) => a - b`) [external] mesma fonte.
- **Python:** Timsort (híbrido Merge + Insertion, estável, O(n) em dados quase ordenados); **Java:** `Arrays.sort` de objetos usa Timsort [skill: cs-fundamentals]. Para primitivos em Java o algoritmo é outro (não verificado aqui).

## Implicação prática

Para a maioria dos casos (até milhões de itens) o sort nativo já é O(n log n) e bem otimizado; "otimizar" costuma significar trocar a **chave/comparador** ou evitar ordenar (ex.: [[wiki/concepts/bucket-sort]], heap para top-k), não reescrever o algoritmo. Ver custo escondido em [[wiki/concepts/algoritmos-de-ordenacao]].

Relacionados: [[wiki/concepts/big-o]], [[wiki/concepts/algoritmos-de-busca]] (busca binária exige lista ordenada).

## Key sources

- [[wiki/sources/ordenacao-selection-quicksort-bubble-sort-live-coding]] — pergunta de abertura: qual algoritmo está por trás de `.sort` e até onde é eficiente (resposta não fornecida pela fonte)
