---
type: concept
title: "Recursão"
aliases: ["recursion", "função recursiva", "chamada recursiva"]
date_created: 2026-06-26
date_updated: 2026-06-26
source_count: 1
tags: [cs-fundamentals, algoritmos, recursao, pilha-de-execucao, dividir-e-conquistar]
skill: cs-fundamentals
status: draft
---

# Recursão

Uma função que **chama ela mesma** para resolver um subproblema menor, até chegar num caso simples o suficiente para responder diretamente.

## Anatomia de toda função recursiva

```python
def fatorial(n):
    if n == 1:          # caso base — para a recursão
        return 1
    return n * fatorial(n - 1)  # caso recursivo — divide o problema
```

Toda recursão tem **obrigatoriamente** duas partes:

| Parte | Papel | Consequência se ausente |
|---|---|---|
| **Caso base** | Condição de parada | Stack overflow — chamadas infinitas |
| **Caso recursivo** | Reduz o problema | Nunca chega ao caso base |

## Como a pilha funciona

Cada chamada recursiva é empilhada na **call stack**. Quando atinge o caso base, as chamadas começam a retornar de baixo para cima:

```
fatorial(5)
  fatorial(4)
    fatorial(3)
      fatorial(2)
        fatorial(1) → retorna 1
      retorna 2×1 = 2
    retorna 3×2 = 6
  retorna 4×6 = 24
retorna 5×24 = 120
```

## Quando usar recursão

- A estrutura do problema é **naturalmente hierárquica** (árvores, grafos, sistema de arquivos)
- O algoritmo se divide em subproblemas **idênticos e menores** (mergesort, quicksort)
- A solução iterativa exigiria gerenciar uma pilha manual

## Riscos

- **Stack overflow**: profundidade muito grande sem tail call optimization → pilha estoura
- **Complexidade oculta**: recursão em árvore pode ser O(2ⁿ) sem memoização
- **Memoização**: salvar resultados já calculados transforma exponencial em linear ([[big-o]])

## Onde aparece

- Percorrer [[arvore]] (DFS, BFS recursivo)
- Algoritmos de ordenação (mergesort, quicksort)
- Fractais e geração procedural
- Sistema de arquivos (diretórios dentro de diretórios)
- Backtracking (sudoku, N-rainhas)
- Dynamic Programming com memoização

## Relação com outros conceitos

- [[big-o]] — análise de complexidade recursiva usa relação de recorrência (ex: T(n) = 2T(n/2) + O(n) → O(n log n) para mergesort)
- [[arvore]] — árvore é a estrutura recursiva por excelência; percorrer uma árvore sem recursão é mais difícil
- [[abstracao]] — recursão é uma abstração: o problema de tamanho n é expresso em termos do mesmo problema de tamanho n-1

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-computacao]]
