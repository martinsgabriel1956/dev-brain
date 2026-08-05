---
type: concept
title: "Algoritmos de Busca"
aliases: ["searching algorithms", "search", "busca", "linear search", "binary search"]
date_created: 2026-07-09
date_updated: 2026-08-04
source_count: 3
tags: [cs-fundamentals, algoritmos, searching, big-o, linear-search, binary-search, two-pointer]
skill: cs-fundamentals
status: draft
---

# Algoritmos de Busca

Métodos para encontrar um elemento em uma estrutura de dados ou confirmar sua existência/localização. A escolha certa depende de uma pergunta simples: os dados estão ordenados?

## Linear Search (Busca Linear)

Verifica cada elemento em sequência até encontrar o alvo ou a lista terminar. Não exige nenhuma ordenação prévia.

- **Melhor caso:** O(1) — alvo na primeira posição
- **Pior caso / caso médio:** O(n)
- Bom se o alvo tende a estar perto do início; ruim se está no fim ou ausente. Ver [[wiki/concepts/melhor-caso-pior-caso-caso-medio]] para a distinção formal entre os três cenários.

## Binary Search (Busca Binária)

Divide repetidamente o intervalo de busca ao meio, comparando o elemento do meio com o alvo e descartando a metade que não pode conter o resultado.

- **Tempo médio/pior caso:** O(log n)
- **Pré-requisito obrigatório:** o array precisa estar ordenado.
- Significativamente mais rápida que a busca linear para conjuntos grandes — em 1 bilhão de elementos, ~30 comparações (ver [[wiki/concepts/big-o]]).

### Implementação real: two pointers, não recursão com recriação de array

A alternativa recursiva "óbvia" — fatiar/recriar um novo sub-array a cada chamada — é computacionalmente cara por causa da cópia repetida. A implementação padrão usa a técnica [[wiki/concepts/two-pointer]]: dois índices (`left`, `right`) delimitam a região de busca atual sem nunca recriar o array original.

```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1
```

Cuidado de implementação: em linguagens com inteiro de tamanho fixo, `(left + right) // 2` pode estourar (overflow) — Python não sofre com isso, mas outras linguagens devem preferir `left + (right - left) // 2`.

## Outras variantes citadas na fonte

Jump search, exponential search, Fibonacci search, e busca em hash table (O(1) esperado, buscando a chave diretamente — mas não garantido em todos os casos, ex: colisões).

## O trade-off central

Binary Search só é possível porque alguém pagou o custo de ordenar os dados primeiro (ver [[wiki/concepts/algoritmos-de-ordenacao]]). Se os dados mudam com frequência e a ordenação tem que ser refeita a cada busca, Linear Search pode acabar sendo mais barato no total.

## Relação com outros conceitos

- [[wiki/concepts/big-o]] — O(log n) vs O(n): a diferença prática em datasets grandes
- [[wiki/concepts/algoritmos-de-ordenacao]] — pré-requisito de Binary Search
- [[wiki/concepts/algoritmos-e-estruturas-de-dados]] — hub que lista busca como terceiro passo da sequência de aprendizado de DSA
- [[wiki/concepts/hashmap]] — busca por chave O(1) amortizado como alternativa a busca em array
- [[wiki/concepts/melhor-caso-pior-caso-caso-medio]] — busca linear como exemplo didático dos três cenários de complexidade
- [[wiki/concepts/two-pointer]] — técnica usada na implementação real de binary search (evita recriação recursiva de sub-arrays)

## Key sources

- [[wiki/sources/9-algoritmos-que-todo-programador-deveria-saber]]
- [[wiki/sources/estruturas-de-dados-algoritmos-big-o-como-escolher]] — busca binária como exemplo canônico de O(log n) (cada passo descarta metade do problema); distinção melhor/pior/caso médio
- [[wiki/sources/binary-search-em-5-minutos]] — implementação two pointers completa, resolvida ao vivo no LeetCode em menos de 5 minutos
