---
type: concept
title: "Recursão"
aliases: ["recursion", "função recursiva", "chamada recursiva"]
date_created: 2026-06-26
date_updated: 2026-08-18
source_count: 4
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
- **Custo de recriação de estrutura a cada chamada**: uma recursão "óbvia" para percorrer um array (ex: binary search) que fatia/recria um novo sub-array a cada nível é mais cara do que precisa ser — [[wiki/sources/binary-search-em-5-minutos]] usa isso como motivação explícita para preferir [[wiki/concepts/two-pointer|two pointer]] iterativo, que navega os mesmos índices sem nunca copiar o array original

## Trace passo a passo: fatorial e Fibonacci em JavaScript

Dois exemplos canônicos de recursão simples, úteis para visualizar o desenrolar da call stack:

```javascript
function fatorial(n) {
  if (n === 0 || n === 1) return 1;   // caso base
  return n * fatorial(n - 1);         // chamada recursiva
}

function fibonacci(p) {
  if (p === 1) return 0;              // caso base 1
  if (p === 2) return 1;              // caso base 2
  return fibonacci(p - 1) + fibonacci(p - 2); // chamada recursiva
}
```

A Fibonacci recursiva precisa de **dois** casos base (não um) porque cada chamada depende dos **dois** termos anteriores — com um caso base só, `fibonacci(p - 2)` estouraria para índices inválidos antes de a recursão conseguir parar.

**Cuidado com a categoria "recursão é mais lenta":** essa afirmação (comum em introduções ao tema) mistura duas coisas com custo bem diferente. O `fatorial` recursivo acima é O(n) — uma chamada por nível, sem repetição de trabalho. Já o `fibonacci` recursivo ingênuo é O(2ⁿ) — a árvore de chamadas recomputa os mesmos subproblemas repetidamente (`fibonacci(3)` é chamado de novo dentro de `fibonacci(5)` e de `fibonacci(4)`). A correção para esse segundo caso não é "trocar recursão por iteração", é [[wiki/concepts/programacao-dinamica|memoização]] — ver [[wiki/sources/recursao-fatorial-fibonacci-javascript]].

## Recursão vs. iteração com ponteiros

Nem todo problema "naturalmente recursivo" precisa de recursão de fato — binary search é recursivo na estrutura do raciocínio ("resolva no sub-array menor"), mas a implementação mais barata dispensa a chamada recursiva e a cópia de array, substituindo por dois índices que se movem sobre a mesma estrutura ([[wiki/concepts/two-pointer]]).

## Onde aparece

- Percorrer [[arvore]] (DFS, BFS recursivo) — ver [[wiki/concepts/algoritmos-de-grafo]] para o mecanismo completo de backtrack do DFS
- [[wiki/concepts/algoritmos-de-ordenacao|Algoritmos de ordenação]] (mergesort, quicksort)
- Fractais e geração procedural
- Sistema de arquivos (diretórios dentro de diretórios)
- Backtracking (sudoku, N-rainhas)
- Dynamic Programming com memoização

## Relação com outros conceitos

- [[big-o]] — análise de complexidade recursiva usa relação de recorrência (ex: T(n) = 2T(n/2) + O(n) → O(n log n) para mergesort)
- [[arvore]] — árvore é a estrutura recursiva por excelência; percorrer uma árvore sem recursão é mais difícil
- [[abstracao]] — recursão é uma abstração: o problema de tamanho n é expresso em termos do mesmo problema de tamanho n-1
- [[wiki/concepts/two-pointer]] — alternativa iterativa que dispensa recursão e cópia de estrutura em problemas de array

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-computacao]]
- [[wiki/sources/9-algoritmos-que-todo-programador-deveria-saber]]
- [[wiki/sources/binary-search-em-5-minutos]] — motivação explícita para trocar recursão com recriação de array por two pointer iterativo
- [[wiki/sources/recursao-fatorial-fibonacci-javascript]] — trace passo a passo de fatorial e Fibonacci recursivos em JavaScript, caso base vs. chamada recursiva
