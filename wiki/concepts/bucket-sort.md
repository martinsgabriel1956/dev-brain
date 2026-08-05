---
type: concept
title: "Bucket Sort"
aliases: ["bucket sort", "ordenação por baldes", "counting sort por frequência"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 1
tags: [cs-fundamentals, algoritmos, sorting, big-o, hashmap, array]
skill: cs-fundamentals
status: stub
---

# Bucket Sort

Técnica de ordenação que evita comparações: em vez de comparar elementos entre si (como quicksort ou merge sort, O(n log n)), distribui cada elemento diretamente num "balde" (posição de array) cujo índice já representa seu valor de ordenação — tornando a inserção O(1) por elemento e o algoritmo inteiro O(n).

## Quando é possível usar

Só funciona quando o valor de ordenação tem um teto conhecido e pequeno o suficiente para virar índice de array. O exemplo canônico: ordenar elementos por **frequência de aparição** num array de tamanho `n` — a frequência de qualquer elemento nunca pode ser maior que `n`, então um array de `n + 1` baldes (índice = frequência) cobre todos os casos possíveis.

## Exemplo: Top K Frequent Elements

Documentado em [[wiki/sources/resolvendo-3-problemas-classicos-entrevista-coding-dsa]]: depois de montar um [[wiki/concepts/hashmap|hash map]] de frequências (`elemento → contagem`), em vez de ordenar esse mapa por frequência (O(n log n)), cada elemento é colocado diretamente no balde `buckets[frequência]`. Percorrer os baldes do maior índice (mais frequente) para o menor produz o resultado ordenado por frequência sem nenhuma comparação — O(n) total.

```python
n = len(nums)
buckets = [[] for _ in range(n + 1)]  # índice = frequência
for num, freq in frequency_map.items():
    buckets[freq].append(num)
```

## Trade-off não discutido na fonte

O array de `n + 1` baldes é alocado independentemente de quantos baldes realmente serão usados — se a distribuição de frequências for muito desigual (um elemento aparece `n` vezes, todos os outros aparecem 1 vez), a maioria dos baldes fica vazia, mas o espaço O(n) é reservado do mesmo jeito. A alternativa clássica para "top-k eficiente" é um heap de tamanho `k`, com custo O(n log k) — mais lento assintoticamente que bucket sort quando `k` é próximo de `n`, mas com uso de espaço proporcional a `k`, não a `n`.

## Relação com outros conceitos

- [[wiki/concepts/algoritmos-de-ordenacao]] — bucket sort troca comparação por indexação direta, fora da família de algoritmos comparativos O(n log n)
- [[wiki/concepts/hashmap]] — o mapa de frequências é o passo que precede a distribuição nos baldes
- [[wiki/concepts/big-o]] — exemplo de como conhecer um teto no domínio dos valores (frequência ≤ n) elimina a necessidade de comparação
- [[wiki/concepts/time-space-tradeoff]] — troca espaço garantido (array de tamanho n+1) por tempo de ordenação O(n) em vez de O(n log n)

## Key sources

- [[wiki/sources/resolvendo-3-problemas-classicos-entrevista-coding-dsa]] — Top K Frequent Elements resolvido com bucket sort por frequência, evitando o requisito de complexidade O(n log n) do follow-up
