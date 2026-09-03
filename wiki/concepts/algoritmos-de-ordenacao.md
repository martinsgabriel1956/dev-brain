---
type: concept
title: "Algoritmos de Ordenação"
aliases: ["sorting algorithms", "sorting", "ordenação"]
date_created: 2026-07-09
date_updated: 2026-09-03
source_count: 4
tags: [cs-fundamentals, algoritmos, sorting, big-o, bubble-sort, insertion-sort, selection-sort, merge-sort, quicksort, heapsort]
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

## Selection Sort

Varre o arranjo **inteiro** a cada passada em busca do menor valor restante e o fixa na posição corrente — diferente do Insertion Sort, que agrega um elemento novo por vez ao subconjunto já ordenado, o Selection Sort já olha para todos os elementos de uma vez em cada passada. Exemplo de campo: `[7, 4, 5, 9, 8, 2, 1]` → acha o menor (1), fixa na posição 0; acha o segundo menor (2) no restante, fixa na posição 1; e assim sucessivamente até ordenar. Ver [[wiki/sources/algoritmos-de-ordenacao-bubble-insertion-selection-merge-quicksort-heapsort]].

- **Tempo médio/pior/melhor caso:** O(n²) — sempre varre o restante inteiro, mesmo se já estiver ordenado
- **Espaço:** O(1), in-place
- Não estável (a busca do menor pode trocar elementos iguais de ordem relativa)

## Merge Sort

Algoritmo recursivo, dividir-para-conquistar: divide o array ao meio recursivamente até restar um elemento, depois mescla as metades ordenadas comparando os elementos par a par — a cada *merge*, o subarranjo resultante já sai ordenado, então a mesclagem final dos dois maiores subarranjos produz o array completo ordenado.

- **Tempo:** O(n log n) em todos os casos — sem degradação de pior caso
- **Espaço:** O(n) — precisa de array auxiliar para o merge
- **Estável** (preserva ordem relativa de elementos iguais)

## Quicksort

Também dividir-para-conquistar, mas particiona em vez de mesclar: escolhe um **pivô**, reorganiza o arranjo em subarranjo de elementos menores que o pivô (esquerda) e maiores (direita), depois repete recursivamente em cada subarranjo até tudo ordenado. Exemplo: `[6, 5, 12, 10, 9, 1]` com pivô 5 particiona em `[1]` (esquerda) e `[6, 9, 10, 12]` (direita). *In-place* (pouca memória extra) — ao contrário do Merge Sort, que sacrifica espaço por estabilidade e previsibilidade de pior caso.

- **Tempo médio:** O(n log n) | **Pior caso:** O(n²)
- **Pior caso ocorre quando o pivô escolhido é sempre um extremo do arranjo** (o maior ou o menor valor) — a partição fica desbalanceada, um subarranjo fica vazio e o outro recebe quase todos os elementos, degenerando para o comportamento de um Bubble/Insertion Sort. Mitigação (não coberta na fonte de campo, ver `references/algorithms-complexity.md`): pivô aleatório ou mediana de três.
- **Espaço:** O(log n) amortizado (stack de recursão) | Não estável

## Heapsort

Constrói um **Max Heap** — uma árvore binária armazenada em array onde todo elemento pai é maior que seus filhos, logo a raiz é sempre o maior valor — e extrai a raiz repetidamente, rebalanceando a árvore a cada extração, até obter o array ordenado. Exemplo de construção do Max Heap: `[1, 12, ...]` → compara pai-filho e sobe o maior — `12` vai para a raiz, `1` desce; depois `[5, 1, 6]` → `6` (o maior dos três) sobe para a raiz da subárvore, ficando `[6, 5, 1]`. Ver [[wiki/sources/algoritmos-de-ordenacao-bubble-insertion-selection-merge-quicksort-heapsort]] (mostra a construção do heap, mas não o passo de extração-e-rebalanceamento repetido).

- **Tempo:** O(n log n) em todos os casos
- **Espaço:** O(1), in-place — vantagem sobre Merge Sort quando memória extra é proibida
- Não é cache-friendly (acesso randômico ao heap fragmenta cache), diferente do Quicksort

## Tabela de decisão

| Cenário | Melhor escolha |
|---|---|
| Dados quase ordenados | Insertion Sort |
| Dados invertidos | Merge Sort (Insertion Sort degrada para O(n²)) |
| Estabilidade obrigatória | Merge Sort |
| Memória extra proibida | Heapsort (Quicksort é in-place mas O(n²) no pior caso) |
| Aprendizado / didática | Bubble Sort |
| Array pequeno, poucas trocas aceitáveis | Selection Sort (número de trocas é O(n), menor que Bubble Sort) |

## Custo escondido em soluções de entrevista

Um erro comum em entrevistas de coding: propor uma solução que ordena o array e depois o percorre uma única vez, contando só o loop final como custo — mas a ordenação prévia já é O(n log n) e domina a complexidade total. Documentado em [[wiki/sources/resolvendo-3-problemas-classicos-entrevista-coding-dsa]] com o problema Longest Consecutive Sequence: uma solução por ordenação é O(n log n) no total, contra O(n) de uma alternativa com [[wiki/concepts/hashmap|hash set]].

## Alternativa sem comparação: Bucket Sort

Quando o valor de ordenação tem teto conhecido (ex.: frequência de um elemento, que nunca excede o tamanho `n` do array), é possível ordenar sem nenhuma comparação usando [[wiki/concepts/bucket-sort]] — O(n) em vez de O(n log n). Ver [[wiki/sources/resolvendo-3-problemas-classicos-entrevista-coding-dsa]] (Top K Frequent Elements).

## Relação com outros conceitos

- [[wiki/concepts/big-o]] — a notação usada para comparar esses algoritmos
- [[wiki/concepts/algoritmos-e-estruturas-de-dados]] — hub que lista ordenação como segundo passo da sequência de aprendizado de DSA
- [[wiki/concepts/algoritmos-de-busca]] — Binary Search exige que o array já esteja ordenado, dependência direta destes algoritmos
- [[wiki/concepts/recursao]] — Merge Sort e Quicksort são os exemplos canônicos de dividir-para-conquistar recursivo
- [[wiki/concepts/bucket-sort]] — alternativa não-comparativa quando o domínio de valores tem teto conhecido
- [[wiki/concepts/hashmap]] — hash set como alternativa a ordenar quando o objetivo é só membership check, não ordem

## Key sources

- [[wiki/sources/9-algoritmos-que-todo-programador-deveria-saber]]
- [[wiki/sources/resolvendo-3-problemas-classicos-entrevista-coding-dsa]] — custo escondido de `sort()` numa solução que parece O(n); bucket sort por frequência como alternativa O(n) sem comparação
- [[wiki/sources/busca-linear-e-binaria-giovana]] — ordenação prévia (ex.: Quicksort) como pré-requisito da busca binária
- [[wiki/sources/algoritmos-de-ordenacao-bubble-insertion-selection-merge-quicksort-heapsort]] — Selection Sort (novo); mecanismo de partição do Quicksort (pivô, causa do pior caso); construção do Max Heap no Heapsort
