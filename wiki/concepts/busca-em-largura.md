---
type: concept
title: "Busca em Largura (BFS)"
aliases: ["BFS", "breadth-first search", "busca em largura"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_count: 1
tags: [cs-fundamentals, algoritmos, arvore, grafo, bfs, fila]
skill: cs-fundamentals
status: stub
---

# Busca em Largura (BFS)

Algoritmo de travessia de árvores e grafos que **explora todos os nós de uma camada antes de descer para a próxima**. Implementado com uma fila (queue): visita um nó, enfileira seus filhos, repete. É a escolha natural para problemas de menor caminho em grafos não ponderados e para varredura nível a nível de uma árvore.

Junto com a [[wiki/concepts/busca-em-profundidade|DFS]], forma o par que resolve quase todo problema de [[wiki/concepts/binary-search-tree|árvore binária]] no [[wiki/entities/leetcode|LeetCode]]. O padrão a treinar é reconhecer, pelo enunciado, quando o problema pede varredura por camadas (BFS) versus mergulho por ramo (DFS).

## Relação com outros conceitos

- [[wiki/concepts/busca-em-profundidade]] — o par complementar; DFS usa pilha/recursão, BFS usa fila
- [[wiki/concepts/reconhecimento-de-padroes]] — reconhecer "isto pede BFS" é o objetivo prático

## Key Sources

- [[wiki/sources/como-ficar-bom-em-leetcode]] — BFS/DFS como os dois padrões que cobrem a maioria dos problemas de árvore binária
