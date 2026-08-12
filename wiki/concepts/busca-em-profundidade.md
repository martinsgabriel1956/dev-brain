---
type: concept
title: "Busca em Profundidade (DFS)"
aliases: ["DFS", "depth-first search", "busca em profundidade"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_count: 1
tags: [cs-fundamentals, algoritmos, arvore, grafo, dfs, recursao]
skill: cs-fundamentals
status: stub
---

# Busca em Profundidade (DFS)

Algoritmo de travessia de árvores e grafos que **explora o mais fundo possível por um ramo antes de retroceder** (backtrack) e tentar o próximo. Tipicamente implementado com recursão (usando a pilha de chamadas) ou com uma pilha explícita.

Em problemas de [[wiki/concepts/binary-search-tree|árvore binária]] no [[wiki/entities/leetcode|LeetCode]], quase todo problema cai em DFS ou em [[wiki/concepts/busca-em-largura|BFS]] — reconhecer qual dos dois o enunciado pede é o padrão central a treinar. DFS é a escolha natural quando a solução depende de percorrer um caminho da raiz até uma folha (ex.: somar nós num intervalo, *Sum Root to Leaf Numbers*).

## Relação com outros conceitos

- [[wiki/concepts/busca-em-largura]] — o par complementar; BFS explora por camadas (fila) em vez de por ramo (pilha)
- [[wiki/concepts/backtracking]] — DFS é o esqueleto de travessia sobre o qual o backtracking desfaz escolhas
- [[wiki/concepts/reconhecimento-de-padroes]] — o valor prático é reconhecer "isto é um problema de DFS" pelo enunciado

## Key Sources

- [[wiki/sources/como-ficar-bom-em-leetcode]] — "a maioria dos problemas de binary tree cai em DFS ou BFS"; DFS como primeiro padrão de árvore a dominar
