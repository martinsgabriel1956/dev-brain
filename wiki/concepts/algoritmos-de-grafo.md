---
type: concept
title: "Algoritmos de Grafo"
aliases: ["graph algorithms", "grafo", "DFS", "BFS", "Dijkstra", "A-star", "pathfinding"]
date_created: 2026-07-09
date_updated: 2026-08-05
source_count: 3
tags: [cs-fundamentals, algoritmos, graph, dfs, bfs, dijkstra, a-star, pathfinding, graph-engineering, edge-weight]
skill: cs-fundamentals
status: draft
---

# Algoritmos de Grafo

Instruções para resolver problemas de teoria dos grafos, onde dados são modelados como nós (vértices) conectados por arestas. Usados em redes de computadores, redes sociais e roteamento de mapas — a analogia canônica é nós como interseções e arestas como estradas.

## DFS — Depth-First Search (Busca em Profundidade)

Percorre o mais fundo possível por um único caminho, faz backtrack quando não dá mais, e tenta outro caminho. Recursivo.

- **Complexidade de espaço:** O(V) (V = vértices/nós, termos intercambiáveis)
- Encontra *um* caminho, não necessariamente o mais curto.
- Usos: detecção de ciclos, ordenação topológica, componentes conectados.

## BFS — Breadth-First Search (Busca em Largura)

Explora camada por camada a partir do nó inicial, expandindo simultaneamente em todas as direções antes de ir mais fundo.

- Mesma complexidade de tempo/espaço do DFS: O(V + E)
- Encontra o caminho mais curto **em número de arestas** — não necessariamente em distância/peso real, porque não considera pesos.

## Algoritmo de Dijkstra

Encontra o caminho de menor peso entre um nó fonte e todos os outros nós, levando em conta os pesos das arestas (ex: comprimento da via, trânsito, velocidade).

- **Tempo:** O((V+E) log V) com min-heap
- É o único dos três (DFS/BFS/Dijkstra) que "pensa à frente", recalculando a melhor rota a cada nó.
- Base histórica do roteamento do Google Maps, que evolui a partir dele.

## Algoritmo A* (A-star)

Mesma ideia do Dijkstra, mas usa uma **função heurística** para estimar o custo do nó atual até o destino, priorizando nós que parecem mais próximos do objetivo.

- Mais eficiente que Dijkstra puro na prática, porque não explora igualmente em todas as direções.
- Dijkstra é, na prática, um caso particular de A* com heurística zero.

## Progressão de eficiência (conforme a fonte)

```
DFS/BFS (ignoram peso) → Dijkstra (usa peso, sem heurística) → A* (usa peso + heurística)
```

Cada passo resolve uma limitação do anterior: DFS/BFS não sabem qual caminho é mais "barato" de verdade; Dijkstra sabe, mas explora sem direção; A* explora com direção.

## Pathfinding como projeto de aprendizado

Um projeto de labirinto onde o computador precisa descobrir sozinho o melhor caminho até a saída é citado como forma de exercitar essa família de algoritmos na prática, sem prescrever qual dos quatro (DFS, BFS, Dijkstra, A*) usar. O ganho pedagógico apontado não é a implementação em si, mas a mudança de raciocínio: sair de "como escrever a linha de código" para "como resolver o problema" — o que evitar caminhos bloqueados e não revisitar o mesmo nó duas vezes já é, na prática, reinventar a lógica de BFS/DFS. Ver [[wiki/concepts/projetos-fundamentais-para-aprender-a-programar]] para os outros dois projetos da mesma progressão (estado e modelagem).

## Pedagogia: Nó, Aresta e Peso em Exemplos Cotidianos

[[wiki/sources/graph-engineering-do-loop-ao-grafo]] introduz a mesma definição (nó = N, aresta = E) sem nenhum algoritmo de busca — só a estrutura crua — usando exemplos fora de código para fixar o conceito antes de aplicá-lo a agentes: uma rotina matinal (dormir → acordar → levantar → escovar os dentes → café, cada transição com um peso em minutos), uma rede social (pessoas como nós, relações com peso de amizade/trabalho/tópico em comum) e um funil de negócio (tráfego → signup → ativação → churn → LTV, ver [[wiki/concepts/ltv-cac]]). O ponto pedagógico: uma vez que o grafo tem pesos nas arestas, dá para aplicar buscas e otimizações sobre o processo — a mesma ideia central por trás de Dijkstra/A* acima, só que motivando **por que** alguém desenharia um grafo de informação (para um agente de IA navegar) antes mesmo de escolher qual algoritmo de busca rodar sobre ele.

## Relação com outros conceitos

- [[wiki/concepts/arvore]] — árvores são grafos acíclicos conectados; BFS/DFS se aplicam igualmente
- [[wiki/concepts/big-o]] — O(V+E) como notação padrão de complexidade em grafos
- [[wiki/concepts/recursao]] — DFS é tipicamente implementado recursivamente
- [[wiki/concepts/algoritmos-e-estruturas-de-dados]] — hub que lista BFS/DFS e grafos como passos 3 e 5 da sequência de aprendizado de DSA
- [[wiki/concepts/projetos-fundamentais-para-aprender-a-programar]] — Pathfinding como projeto de aprendizado que introduz esta família de algoritmos

## Key sources

- [[wiki/sources/9-algoritmos-que-todo-programador-deveria-saber]]
- [[wiki/sources/tres-projetos-para-aprender-programar]] — Pathfinding/labirinto como projeto de aprendizado de algoritmos de busca de caminho
- [[wiki/sources/graph-engineering-do-loop-ao-grafo]] — definição pedagógica de nó/aresta/peso com exemplos fora de código, motivando o uso de grafos para orquestração de agentes
