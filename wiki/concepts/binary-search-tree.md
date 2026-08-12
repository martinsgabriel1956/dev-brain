---
type: concept
title: "Binary Search Tree (BST)"
aliases: ["BST", "árvore binária de busca", "binary search tree", "árvore binária"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_count: 1
tags: [cs-fundamentals, estruturas-de-dados, arvore, bst, busca]
skill: cs-fundamentals
status: stub
---

# Binary Search Tree (BST)

Árvore binária **ordenada para busca**: para qualquer nó, todos os valores na subárvore à **esquerda** são menores que ele, e todos à **direita** são maiores — recursivamente. Essa invariante permite busca, inserção e remoção em O(log n) numa árvore balanceada (e O(n) no pior caso degenerado).

Estrutura central nos problemas de árvore do [[wiki/entities/leetcode|LeetCode]], onde a maioria se resolve com [[wiki/concepts/busca-em-profundidade|DFS]] ou [[wiki/concepts/busca-em-largura|BFS]]. Exemplo trabalhado na fonte: somar todos os nós cujo valor está no intervalo `[low, high]` — a ordenação da BST permite podar ramos fora do intervalo em vez de visitar a árvore inteira.

## Relação com outros conceitos

- [[wiki/concepts/busca-em-profundidade]] / [[wiki/concepts/busca-em-largura]] — os dois padrões de travessia que resolvem a maioria dos problemas de árvore
- [[wiki/concepts/big-o]] — O(log n) balanceada vs. O(n) degenerada é o trade-off central
- [[wiki/concepts/algoritmos-e-estruturas-de-dados]] — uma das estruturas fundamentais a implementar por conta própria

## Key Sources

- [[wiki/sources/como-ficar-bom-em-leetcode]] — definição da invariante da BST e problema de soma no intervalo resolvido com DFS
