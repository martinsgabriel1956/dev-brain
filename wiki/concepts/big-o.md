---
type: concept
title: "Big O"
aliases: ["complexidade de algoritmos", "Big-O notation", "O(n)", "complexidade assintótica"]
date_created: 2026-06-26
date_updated: 2026-06-26
source_count: 1
tags: [cs-fundamentals, algoritmos, big-o, complexidade, performance]
skill: cs-fundamentals
status: draft
---

# Big O

Notação que descreve como o **tempo de execução** (ou uso de memória) de um algoritmo cresce conforme o tamanho da entrada cresce. Responde: "se eu dobrar os dados, o que acontece com o tempo?"

## Tabela de complexidades

| Notação | Nome | Exemplo canônico | 10⁶ elementos |
|---|---|---|---|
| O(1) | Constante | Acesso por índice em [[array]] | ~1 op |
| O(log n) | Logarítmico | Busca binária | ~20 ops |
| O(n) | Linear | Busca sequencial | 10⁶ ops |
| O(n log n) | Log-linear | Mergesort, Timsort | ~2×10⁷ ops |
| O(n²) | Quadrático | Bubble sort, nested loops | 10¹² ops |
| O(2ⁿ) | Exponencial | Subsets de força bruta | impossível |
| O(n!) | Fatorial | Problema do Caixeiro Viajante (brute force) | impossível |

## O caso do O(log n)

Busca binária em 1 bilhão de elementos: log₂(10⁹) ≈ **30 comparações**. Isso é possível porque a cada passo metade dos elementos é descartada. Requer que os dados estejam ordenados.

```
1.000.000.000 → 500.000.000 → 250.000.000 → ... → 1 (30 passos)
```

## O caso do O(n!)

Com apenas 20 cidades no Problema do Caixeiro Viajante (qual rota menor passa por todas?), o brute-force exige 20! ≈ **2,4 × 10¹⁸ operações** — mais do que qualquer computador atual processa em anos.

## Como usar na prática

1. Identifique o que cresce — é o tamanho da lista? O número de nós? O número de conexões?
2. Conte o número de operações em função desse tamanho.
3. Ignore constantes e termos menores — O(2n + 5) é O(n).
4. Pergunte: funciona com 10× mais dados? 100×?

## Big O ≠ tempo real

O(1) pode ser mais lento que O(n) para entradas pequenas se a constante for grande (ex: hash table com custo fixo alto vs array de 5 elementos). Big O é relevante para entradas **grandes**.

## Relação com outros conceitos

- [[algoritmos-e-estruturas-de-dados]] — a escolha da estrutura determina a complexidade das operações
- [[arvore]] — BST oferece O(log n) para busca; árvore degenerada (lista) vira O(n)
- [[array]] — acesso O(1), busca O(n)
- [[hashmap]] — busca O(1) amortizado
- [[recursao]] — a complexidade de algoritmos recursivos é calculada pela relação de recorrência

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-computacao]]
