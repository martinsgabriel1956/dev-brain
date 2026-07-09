---
type: concept
title: "Algoritmos de Busca"
aliases: ["searching algorithms", "search", "busca", "linear search", "binary search"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [cs-fundamentals, algoritmos, searching, big-o, linear-search, binary-search]
skill: cs-fundamentals
status: draft
---

# Algoritmos de Busca

Métodos para encontrar um elemento em uma estrutura de dados ou confirmar sua existência/localização. A escolha certa depende de uma pergunta simples: os dados estão ordenados?

## Linear Search (Busca Linear)

Verifica cada elemento em sequência até encontrar o alvo ou a lista terminar. Não exige nenhuma ordenação prévia.

- **Tempo médio/pior caso:** O(n)
- Bom se o alvo tende a estar perto do início; ruim se está no fim ou ausente.

## Binary Search (Busca Binária)

Divide repetidamente o intervalo de busca ao meio, comparando o elemento do meio com o alvo e descartando a metade que não pode conter o resultado.

- **Tempo médio/pior caso:** O(log n)
- **Pré-requisito obrigatório:** o array precisa estar ordenado.
- Significativamente mais rápida que a busca linear para conjuntos grandes — em 1 bilhão de elementos, ~30 comparações (ver [[wiki/concepts/big-o]]).

## Outras variantes citadas na fonte

Jump search, exponential search, Fibonacci search, e busca em hash table (O(1) esperado, buscando a chave diretamente — mas não garantido em todos os casos, ex: colisões).

## O trade-off central

Binary Search só é possível porque alguém pagou o custo de ordenar os dados primeiro (ver [[wiki/concepts/algoritmos-de-ordenacao]]). Se os dados mudam com frequência e a ordenação tem que ser refeita a cada busca, Linear Search pode acabar sendo mais barato no total.

## Relação com outros conceitos

- [[wiki/concepts/big-o]] — O(log n) vs O(n): a diferença prática em datasets grandes
- [[wiki/concepts/algoritmos-de-ordenacao]] — pré-requisito de Binary Search
- [[wiki/concepts/algoritmos-e-estruturas-de-dados]] — hub que lista busca como terceiro passo da sequência de aprendizado de DSA
- [[wiki/concepts/hashmap]] — busca por chave O(1) amortizado como alternativa a busca em array

## Key sources

- [[wiki/sources/9-algoritmos-que-todo-programador-deveria-saber]]
