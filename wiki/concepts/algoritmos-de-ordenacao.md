---
type: concept
title: "Algoritmos de Ordenação"
aliases: ["sorting algorithms", "sorting", "ordenação"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [cs-fundamentals, algoritmos, sorting, big-o, bubble-sort, insertion-sort, merge-sort]
skill: cs-fundamentals
status: draft
---

# Algoritmos de Ordenação

Métodos para reorganizar elementos de uma lista ou array em uma ordem definida (crescente, decrescente, ou baseada em regra). Não existe um algoritmo universalmente melhor — cada um se comporta de forma diferente conforme a condição inicial dos dados (aleatório, quase ordenado, invertido, poucos valores únicos).

## Bubble Sort

Compara elementos adjacentes e troca-os se estiverem fora de ordem, repetindo passagens até o array estar ordenado — o maior elemento "borbulha" até o topo a cada passagem.

- **Tempo médio/pior caso:** O(n²)
- Didático, mas raramente usado na prática.

## Insertion Sort

Constrói o array ordenado um elemento por vez: para cada elemento, desloca os elementos maiores da parte já ordenada para a direita até achar a posição correta.

- **Tempo médio/pior caso:** O(n²) | **Melhor caso:** O(n)
- Boa escolha quando os dados já estão quase ordenados; ruim quando estão invertidos.

## Merge Sort

Algoritmo recursivo, dividir-para-conquistar: divide o array ao meio recursivamente até restar um elemento, depois mescla as metades ordenadas comparando os elementos par a par.

- **Tempo:** O(n log n) em todos os casos — sem degradação de pior caso
- **Espaço:** O(n) — precisa de array auxiliar para o merge
- **Estável** (preserva ordem relativa de elementos iguais)

## Quicksort — citado por contraste

O vídeo-fonte cita o Quicksort como "quase sempre tão bom quanto o Merge Sort", mas *in-place* (pouca memória extra) — ao contrário do Merge Sort, que sacrifica espaço por estabilidade e previsibilidade de pior caso. Ver `references/algorithms-complexity.md` (skill `cs-fundamentals`) para a tabela completa incluindo Heapsort e Timsort.

## Tabela de decisão

| Cenário | Melhor escolha |
|---|---|
| Dados quase ordenados | Insertion Sort |
| Dados invertidos | Merge Sort (Insertion Sort degrada para O(n²)) |
| Estabilidade obrigatória | Merge Sort |
| Memória extra proibida | Quicksort (in-place) |
| Aprendizado / didática | Bubble Sort |

## Relação com outros conceitos

- [[wiki/concepts/big-o]] — a notação usada para comparar esses algoritmos
- [[wiki/concepts/algoritmos-e-estruturas-de-dados]] — hub que lista ordenação como segundo passo da sequência de aprendizado de DSA
- [[wiki/concepts/algoritmos-de-busca]] — Binary Search exige que o array já esteja ordenado, dependência direta destes algoritmos
- [[wiki/concepts/recursao]] — Merge Sort é o exemplo canônico de dividir-para-conquistar recursivo

## Key sources

- [[wiki/sources/9-algoritmos-que-todo-programador-deveria-saber]]
