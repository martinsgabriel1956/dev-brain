---
type: concept
title: "Big O"
aliases: ["complexidade de algoritmos", "Big-O notation", "O(n)", "complexidade assintótica"]
date_created: 2026-06-26
date_updated: 2026-07-20
source_count: 4
tags: [cs-fundamentals, algoritmos, big-o, complexidade, performance]
skill: cs-fundamentals
status: draft
---

# Big O

Notação que descreve como o **tempo de execução** (ou uso de memória) de um algoritmo cresce conforme o tamanho da entrada cresce. Responde: "se eu dobrar os dados, o que acontece com o tempo?"

Medir performance só em milissegundos engana — o resultado muda com máquina, linguagem, banco, cache e ambiente. Big O troca essa medida instável por uma pergunta genérica: quando a entrada dobra, o número de passos fica quase igual, dobra, ou cresce muito mais que o dobro?

## As quatro curvas essenciais para começar

Antes de decorar a tabela completa, quatro curvas já cobrem a maioria dos casos do dia a dia:

- **O(1)** — aumentar os dados quase não muda a quantidade de passos.
- **O(n)** — o código olha item por item; dobrar a lista dobra o trabalho. Um loop simples tem essa cara.
- **O(log n)** — cada passo corta uma parte grande do problema (ex: busca que descarta metade das opções a cada iteração).
- **O(n²)** — cada item é comparado com vários outros; dois loops aninhados geram essa curva, que cresce muito mais rápido que o dobro quando a entrada dobra.

## Tabela de complexidades

| Notação | Nome | Exemplo canônico | 10⁶ elementos |
|---|---|---|---|
| O(1) | Constante | Acesso por índice em [[array]] | ~1 op |
| O(log n) | Logarítmico | Busca binária | ~20 ops |
| O(n) | Linear | Busca sequencial | 10⁶ ops |
| O(n log n) | Log-linear | Mergesort, Timsort | ~2×10⁷ ops |
| O(n²) | Quadrático | Bubble sort, nested loops | 10¹² ops |
| O(2ⁿ) | Exponencial | Subsets de força bruta | impossível |
| O(n!) | Fatorial | Problema do Caixeiro Viajante (brute force) | impossível |

## O caso do O(log n)

Busca binária em 1 bilhão de elementos: log₂(10⁹) ≈ **30 comparações**. Isso é possível porque a cada passo metade dos elementos é descartada. Requer que os dados estejam ordenados.

```
1.000.000.000 → 500.000.000 → 250.000.000 → ... → 1 (30 passos)
```

## O caso do O(n!)

Com apenas 20 cidades no Problema do Caixeiro Viajante (qual rota menor passa por todas?), o brute-force exige 20! ≈ **2,4 × 10¹⁸ operações** — mais do que qualquer computador atual processa em anos.

## Como usar na prática

1. Identifique o que cresce — é o tamanho da lista? O número de nós? O número de conexões?
2. Conte o número de operações em função desse tamanho.
3. Ignore constantes e termos menores — O(2n + 5) é O(n).
4. Pergunte: funciona com 10× mais dados? 100×?

## Uso Prático em Entrevista de Coding

Fora do cálculo formal, Big O tem uma utilidade direta em [[wiki/concepts/entrevista-tecnica-coding|entrevistas técnicas de coding]]: saber a complexidade das estruturas e algoritmos comuns ajuda a saber **que perguntas de esclarecimento fazer** antes de codar. Exemplo: perguntar ao entrevistador se o input já está ordenado permite descartar de saída qualquer algoritmo de ordenação (O(n log n)) do conjunto de abordagens possíveis, em vez de reaprender essa decisão do zero durante a resolução.

No framework [[wiki/concepts/seis-passos-mock-interview|"Os Seis Passos"]], estimar a complexidade da solução ideal é um passo explícito *anterior* à implementação: perguntar "existe uma solução O(1)? O(log n)?" antes de escrever qualquer código, e só então gerar 2–3 soluções candidatas prevendo o Big-O de cada uma.

## Big O ≠ tempo real

O(1) pode ser mais lento que O(n) para entradas pequenas se a constante for grande (ex: hash table com custo fixo alto vs array de 5 elementos). Big O é relevante para entradas **grandes**.

## Relação com outros conceitos

- [[algoritmos-e-estruturas-de-dados]] — a escolha da estrutura determina a complexidade das operações
- [[arvore]] — BST oferece O(log n) para busca; árvore degenerada (lista) vira O(n)
- [[array]] — acesso O(1), busca O(n)
- [[hashmap]] — busca O(1) amortizado
- [[recursao]] — a complexidade de algoritmos recursivos é calculada pela relação de recorrência
- [[wiki/concepts/algoritmos-de-ordenacao]] — Bubble/Insertion Sort O(n²) vs Merge Sort O(n log n) como exemplo concreto da tabela acima
- [[wiki/concepts/algoritmos-de-busca]] — Linear Search O(n) vs Binary Search O(log n), o mesmo salto ilustrado no "caso do O(log n)" acima
- [[wiki/concepts/algoritmos-de-grafo]] — DFS/BFS O(V+E), Dijkstra O((V+E) log V)
- [[wiki/concepts/melhor-caso-pior-caso-caso-medio]] — a mesma operação tem complexidade diferente dependendo do cenário medido
- [[wiki/concepts/time-space-tradeoff]] — Big O também mede espaço, não só tempo; menor notação nem sempre é a melhor escolha

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-computacao]]
- [[wiki/sources/9-algoritmos-que-todo-programador-deveria-saber]]
- [[wiki/sources/estruturas-de-dados-algoritmos-big-o-como-escolher]] — framing das "quatro curvas essenciais" e introdução informal via "quantos passos a mais quando os dados dobram"
- [[wiki/sources/leetcode-como-se-preparar-entrevistas-coding-anthony-mays]] — Big O como ferramenta para saber que perguntas fazer numa entrevista, não só para calcular complexidade
- [[wiki/sources/como-praticar-leetcode-da-forma-certa-anthony-mays]] — estimar Big-O da solução ideal antes de implementar, como passo explícito do framework "Os Seis Passos"
