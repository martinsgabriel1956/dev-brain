---
type: source
title: "9 Algoritmos que Todo Programador Deveria Saber"
aliases: ["9 algorithms every programmer should know", "sorting searching graph algorithms"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 0
tags: [cs-fundamentals, algoritmos, sorting, searching, graph, big-o, bubble-sort, insertion-sort, merge-sort, binary-search, linear-search, dfs, bfs, dijkstra, a-star]
skill: cs-fundamentals
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/9-algoritmos-que-todo-programador-deveria-saber.md
source_url:
author: Forrest (canal de vídeo)
date_published:
date_ingested: 2026-07-09
---

# 9 Algoritmos que Todo Programador Deveria Saber

## TL;DR

Transcrição (traduzida do inglês) de vídeo que percorre nove algoritmos fundamentais agrupados em três categorias — ordenação (Bubble, Insertion, Merge Sort), busca (Linear, Binary Search) e grafo (DFS, BFS, Dijkstra, A*) — explicando mecanismo, complexidade e quando cada um é a escolha certa ou errada. Argumento central: não existe algoritmo universalmente melhor, apenas algoritmos melhores para determinadas condições iniciais dos dados (aleatório, quase ordenado, invertido, poucos valores únicos) — conhecer as alternativas é o que permite escolher a ferramenta certa em vez de martelar tudo com a mesma.

## Key Claims

1. **Três categorias cobrem os nove algoritmos** — ordenação (rearranjar elementos), busca (localizar/confirmar existência de um elemento) e grafo (resolver problemas de nós conectados por arestas).
2. **Bubble Sort é O(n²) médio e pior caso** — compara pares adjacentes e "borbulha" o maior elemento a cada passagem; didático, mas ruim na prática.
3. **Insertion Sort é O(n²) médio/pior, mas O(n) no melhor caso** — constrói o array ordenado um elemento por vez, deslocando elementos maiores para a direita; ótimo para dados quase ordenados, ruim para dados invertidos.
4. **Merge Sort é O(n log n) em todos os casos, mas O(n) de espaço extra** — dividir-para-conquistar recursivo, estável; Quicksort costuma ser tão bom quanto e é in-place (pouca memória extra), mas não é citado como estável.
5. **Linear Search é O(n)** — verifica elemento por elemento em sequência; bom se o alvo está perto do início, ruim se está no fim ou ausente.
6. **Binary Search é O(log n), mas exige array ordenado** — elimina metade do espaço de busca a cada iteração comparando com o elemento do meio.
7. **DFS tem complexidade de espaço O(V)** — vai fundo em um caminho até não dar mais, faz backtrack e tenta outro; recursivo; encontra um caminho mas não necessariamente o mais curto.
8. **BFS explora camada por camada** — mesma complexidade de tempo/espaço do DFS, mas encontra o caminho mais curto em número de arestas (não necessariamente em distância/peso real).
9. **Dijkstra encontra o caminho de menor peso considerando pesos de aresta** — é a base do roteamento do Google Maps; "pensa à frente" recalculando a melhor rota a cada nó, diferente de DFS/BFS.
10. **A* é Dijkstra + heurística** — usa uma função heurística para priorizar nós que parecem mais próximos do destino, tornando-o mais eficiente que Dijkstra puro na prática (mesma garantia de caminho ótimo se a heurística for admissível).

## Entidades Mencionadas

- Google Maps (algoritmo de roteamento citado como versão modificada de Dijkstra evoluindo para A* e depois para algoritmo proprietário)
- Apple Maps (citado como comparação de qualidade de roteamento, sem detalhamento técnico)

## Conceitos Tocados

- [[wiki/concepts/algoritmos-de-ordenacao]]
- [[wiki/concepts/algoritmos-de-busca]]
- [[wiki/concepts/algoritmos-de-grafo]]
- [[wiki/concepts/algoritmos-e-estruturas-de-dados]]
- [[wiki/concepts/big-o]]
- [[wiki/concepts/arvore]]
- [[wiki/concepts/recursao]]

## Open Questions

- Fonte não cita autor sobrenome, canal completo ou referências acadêmicas — didática mas sem rigor formal, mesmo padrão observado em outras fontes de vídeo já ingeridas nesta wiki.
- Não detalha a demonstração de estabilidade do Quicksort (a fonte menciona só o Merge Sort como estável) nem explica por que o Quicksort tem pior caso O(n²) — ver detalhamento formal em [[wiki/concepts/big-o]] e na referência técnica `cs-fundamentals/algorithms-complexity.md`.
- Não aprofunda a condição de admissibilidade da heurística do A* (o que garante que ele ainda encontra o caminho ótimo, e não só "um caminho rápido") — questão em aberto para uma futura fonte dedicada a pathfinding.
- Não menciona Dynamic Programming, Greedy nem Backtracking como categorias próprias além de citá-los de passagem no fechamento — oportunidade para uma fonte futura aprofundar esses três.

## Raw Quotes

> "Existem oito algoritmos de ordenação diferentes atuando sobre quatro condições iniciais diferentes... é uma representação bonita de como esses algoritmos são ótimos para ordenar algumas condições iniciais, mas ruins para outras."

> "Merge Sort tem complexidade de tempo O(n log n) em todos os casos — porém requer espaço adicional... Já um algoritmo como o Quicksort, que quase sempre é tão bom quanto o Merge Sort, é um algoritmo in-place que requer muito pouca memória extra."

> "Esse é o único dos três algoritmos de grafo aqui discutidos que de fato 'pensa à frente', recalculando a melhor rota conforme você se move de nó em nó." (sobre o algoritmo de Dijkstra)

> "É, em linhas gerais, a mesma coisa [que Dijkstra], exceto que ele [A*] usa uma função heurística, dando prioridade a nós que aparentam ser 'melhores' que os outros."
