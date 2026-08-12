---
type: concept
title: "Backtracking"
aliases: ["backtracking", "retrocesso", "busca com retrocesso"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_count: 1
tags: [cs-fundamentals, algoritmos, recursao, dfs]
skill: cs-fundamentals
status: stub
---

# Backtracking

Estratégia de busca que constrói uma solução **incrementalmente** e **desfaz (retrocede)** a última escolha assim que percebe que ela não pode levar a uma solução válida. É uma [[wiki/concepts/busca-em-profundidade|DFS]] sobre a árvore de decisões do problema, com poda: em vez de enumerar todas as combinações, abandona ramos inviáveis cedo.

Padrão típico de problemas de combinações, permutações, subconjuntos e puzzles de restrição (N-Queens, Sudoku). Um dos padrões que a fonte de estudo de [[wiki/entities/leetcode|LeetCode]] recomenda dominar depois de two pointer e hash map.

## Relação com outros conceitos

- [[wiki/concepts/busca-em-profundidade]] — backtracking é DFS na árvore de decisões, com desfazer explícito da escolha
- [[wiki/concepts/programacao-dinamica]] — quando subproblemas se repetem, memoização/DP pode substituir o backtracking exponencial
- [[wiki/concepts/reconhecimento-de-padroes]] — "gerar todas as combinações/permutações válidas" ≈ backtracking

## Key Sources

- [[wiki/sources/como-ficar-bom-em-leetcode]] — listado entre os padrões prioritários a treinar
