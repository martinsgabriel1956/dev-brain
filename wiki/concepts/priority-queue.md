---
type: concept
title: "Priority Queue (Fila de Prioridade) / Heap"
aliases: ["priority queue", "fila de prioridade", "heap", "min-heap", "max-heap"]
date_created: 2026-08-18
date_updated: 2026-09-02
source_count: 2
tags: [cs-fundamentals, estruturas-de-dados, heap, priority-queue, huffman-coding]
skill: cs-fundamentals
status: stub
---

# Priority Queue (Fila de Prioridade) / Heap

Estrutura de dados que, ao contrário de uma [[wiki/concepts/fila]] comum (FIFO), sempre entrega o elemento de **maior ou menor prioridade** primeiro, não o mais antigo. Normalmente implementada com um **heap** — uma árvore binária (representada internamente como array) onde o nó pai é sempre ≥ (max-heap) ou ≤ (min-heap) que seus filhos.

## Operações e Complexidade

| Operação | Complexidade |
|---|---|
| Insert (push) | O(log n) — "sobe" (*bubble up*) até restaurar a invariante do heap |
| Extract min/max (pop) | O(log n) — "desce" (*bubble down*) |
| Peek min/max | O(1) |
| Build heap a partir de array | O(n) — não O(n log n) |

## Onde Aparece na Prática

- **Construção da árvore de Huffman** — o passo central de [[wiki/concepts/compactacao-de-texto]] (algoritmo Huffman coding, usado pelo deflate/gzip): cada caractere entra numa min-priority-queue ordenada por frequência; repetidamente remove-se os dois nós de menor frequência, soma-se num nó novo, e reinsere-se o resultado na fila — até sobrar um único nó raiz. Ver [[wiki/sources/gzip-deflate-huffman-lz77]].
- **Algoritmo de Dijkstra** e **A\*** — sempre expandem o nó de menor custo acumulado conhecido primeiro.
- **Schedulers de sistema operacional** — processos com maior prioridade executam antes.
- **Event loops com deadlines** — filas de tarefas ordenadas por tempo de execução mais próximo.

## Relação com outros conceitos

- [[wiki/concepts/arvore]] — o heap é uma árvore binária especializada (heap-ordered, não busca-ordered como uma BST); a árvore de Huffman resultante da priority queue, porém, não é um heap em si — é o produto final da sequência de merges.
- [[wiki/concepts/fila]] — mesma interface conceitual (enqueue/dequeue), ordem de saída diferente (prioridade em vez de chegada).
- [[wiki/concepts/ambulance-pattern]] — **falso cognato em arquitetura de mensageria**: implementar priorização de mensagens como uma fila de prioridade única (heap ordenado por campo de prioridade) causa starvation do tráfego normal, exatamente porque o item de maior prioridade sempre sai primeiro. O Ambulance Pattern resolve isso evitando esse modelo — usa filas físicas separadas em vez de uma única priority queue.

## Key sources

- [[wiki/sources/gzip-deflate-huffman-lz77]] — uso de priority queue na construção passo a passo da árvore de Huffman dentro do deflate/gzip
- [[wiki/sources/ambulance-pattern-priorizacao-mensagens-mark-richards]] — contraste: por que usar uma priority queue única para priorizar mensagens em mensageria distribuída causa starvation, ao contrário do uso da estrutura de dados em algoritmos como Huffman/Dijkstra
