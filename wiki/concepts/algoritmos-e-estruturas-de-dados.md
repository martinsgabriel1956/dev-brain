---
type: concept
title: "Algoritmos e Estruturas de Dados"
aliases: ["DSA", "data structures", "estruturas de dados", "algoritmos"]
date_created: 2026-05-16
date_updated: 2026-07-03
source_count: 5
tags: [fundamentos, cs-fundamentals, algoritmos, programacao]
skill: tech-mentor-leadership
status: stable
---

# Algoritmos e Estruturas de Dados

A fundação inegociável de qualquer carreira séria em programação. É o que separa quem bate num teto rápido de quem continua crescendo.

## Por que é a fundação

Linguagens modernas escondem as estruturas de dados de você — você usa uma lista sem saber se é um array contíguo ou uma linked list, com implicações completamente diferentes de performance. Quem não entende a camada abaixo não consegue tomar decisões informadas sobre trade-offs.

Quando você entende estruturas de dados e algoritmos, coisas como:
- Computação distribuída
- Design de banco de dados
- Sistemas de cache
- Consenso distribuído

...começam a fazer sentido porque você enxerga os primitivos que estão por baixo.

## Exemplos de perguntas fundamentais

- Qual a diferença entre um array e uma lista ligada?
- Qual a diferença entre uma string imutável e uma mutável?
- O que é um stream?
- Quando usar uma hash table vs. uma árvore de busca?

## Sequência de aprendizado sugerida

1. Estruturas básicas: array, linked list, stack, queue, hash map, set
2. Algoritmos de ordenação: QuickSort, MergeSort
3. Busca: binary search, BFS, DFS
4. Estruturas avançadas: Bloom Filters, consistent hashing
5. Grafos e suas representações

## Por que Pascal e C eram boas linguagens iniciais

Você era *obrigado* a lidar com ponteiros, alocação de memória e estruturas manuais para fazer qualquer coisa. A linguagem não escondia nada. Linguagens modernas como Python ou JavaScript abstraem tudo isso — conveniente para produção, ruim para aprendizado da fundação.

## Relação com [[wiki/concepts/fundacao-tecnica]]

DSA *é* a fundação técnica. Sem ela, estudar [[wiki/concepts/design-patterns|Design Patterns]], frameworks, ou arquitetura de sistemas é construir em cima de areia.

## DSA como parte — não o todo — da lógica de programação

DSA amplia o [[repertorio]] e melhora a capacidade de resolver problemas, mas confundir DSA com "lógica de programação" é leviano. Os outros pilares — [[decomposicao-de-problemas]], habilidade de pesquisa, projetos variados e intuição — são igualmente ou mais importantes para competência profissional real.

## Conceitos Individuais

Cada estrutura tem sua própria página com complexidade, analogias e quando usar:

- [[array]] — O(1) por índice; fraco em inserção/remoção no meio
- [[hashmap]] — O(1) por chave; busca por identificador
- [[fila]] — FIFO; processamento em ordem de chegada
- [[pilha]] — LIFO; operações de undo, call stack
- [[arvore]] — O(log n); hierarquia, índices de banco de dados

## Key Sources

- [[wiki/sources/akita-como-aprender-programacao]] — afirmação de que DSA é o que separa amadores de profissionais; por que linguagens modernas escondem essas estruturas; sequência de aprendizado
- [[wiki/sources/logica-de-programacao-o-que-e-de-verdade]] — DSA é parte pequena do todo; confundir DSA com lógica de programação seria "leviano"
- [[wiki/sources/estruturas-de-dados-pratica-array-hashmap-fila-pilha-arvore]] — introdução prática às cinco estruturas; três perguntas de decisão; quando usar cada uma
- [[wiki/sources/engenheiro-vs-programador-mercado-ia]] — DSA como o primeiro dos fundamentos do "eixo vertical" da engenharia; explica por que sistemas degradam ao escalar de mil para cem mil usuários; livro-base Introduction to Algorithms (Cormen)
- [[wiki/sources/operador-de-crud-vs-engenheiro-repertorio]] — matemática (complexidade, probabilidade, cache) como "gramática por baixo do que você constrói"; exemplo do laço dentro do laço que derruba o sistema com 1000 usuários
