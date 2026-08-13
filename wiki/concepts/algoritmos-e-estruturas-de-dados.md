---
type: concept
title: "Algoritmos e Estruturas de Dados"
aliases: ["DSA", "data structures", "estruturas de dados", "algoritmos"]
date_created: 2026-05-16
date_updated: 2026-08-13
source_count: 14
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
2. [[wiki/concepts/algoritmos-de-ordenacao|Algoritmos de ordenação]]: QuickSort, MergeSort
3. [[wiki/concepts/algoritmos-de-busca|Busca]]: binary search, BFS, DFS
4. Estruturas avançadas: Bloom Filters, consistent hashing
5. [[wiki/concepts/algoritmos-de-grafo|Grafos]] e suas representações

## Por que Pascal e C eram boas linguagens iniciais

Você era *obrigado* a lidar com ponteiros, alocação de memória e estruturas manuais para fazer qualquer coisa. A linguagem não escondia nada. Linguagens modernas como Python ou JavaScript abstraem tudo isso — conveniente para produção, ruim para aprendizado da fundação.

## Relação com [[wiki/concepts/fundacao-tecnica]]

DSA *é* a fundação técnica. Sem ela, estudar [[wiki/concepts/design-patterns|Design Patterns]], frameworks, ou arquitetura de sistemas é construir em cima de areia.

## DSA como parte — não o todo — da lógica de programação

DSA amplia o [[repertorio]] e melhora a capacidade de resolver problemas, mas confundir DSA com "lógica de programação" é leviano. Os outros pilares — [[decomposicao-de-problemas]], habilidade de pesquisa, projetos variados e intuição — são igualmente ou mais importantes para competência profissional real.

## Como escolher a estrutura certa: operação primeiro

A pergunta que precede qualquer escolha de estrutura não é "qual estrutura é melhor?" — é "qual operação eu preciso otimizar?". Toda estrutura prioriza algumas operações (buscar, inserir, remover, percorrer, manter ordem, consultar por chave) e torna outras mais caras. Se o sistema busca o tempo todo, escolha pensando em busca; se insere e remove o tempo todo, escolha pensando nisso; se precisa manter ordem, saiba que essa ordem tem custo.

### Quatro perguntas antes de escrever a solução

1. Qual é o N (tamanho da entrada)?
2. Qual a operação mais comum?
3. Qual estrutura de dados ajuda essa operação?
4. Como esse custo aumenta quando o N cresce? (ver [[wiki/concepts/big-o]])

### Estrutura de dados vs. algoritmo

A estrutura de dados é *como* os dados ficam guardados; o algoritmo é a sequência de passos executada sobre eles. Os dois andam juntos: às vezes a melhoria vem de mudar o algoritmo, às vezes vem de guardar os dados de outro jeito — e a estrutura certa costuma tornar o algoritmo necessário muito mais simples e direto (ex: buscar por e-mail numa lista exige testar item por item; com um índice por e-mail, o algoritmo vai direto à chave).

## DSA em [[wiki/concepts/entrevista-tecnica-coding|entrevista técnica de coding]]

O valor de DSA numa entrevista ao vivo não é só "resolver o problema" — é usar o vocabulário de estruturas e algoritmos para fazer as perguntas certas de esclarecimento antes de codar (ex.: perguntar se o input já está ordenado descarta algoritmos de ordenação do conjunto de opções). Entrevistadores tendem a evitar problemas prontos de plataformas de prática justamente para observar esse processo de raciocínio, não a resposta memorizada — ver [[wiki/concepts/reconhecimento-de-padroes]] sobre por que memorizar o padrão importa mais que memorizar o problema específico.

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
- [[wiki/sources/9-algoritmos-que-todo-programador-deveria-saber]] — nove algoritmos concretos das três categorias citadas na sequência de aprendizado acima: ordenação, busca e grafo, com mecanismo, complexidade e caso de uso de cada um
- [[wiki/sources/estruturas-de-dados-algoritmos-big-o-como-escolher]] — continuação direta de "estruturas de dados na prática"; framework de escolha por operação, distinção estrutura/algoritmo, e as quatro perguntas antes de escrever a solução
- [[wiki/sources/leetcode-como-se-preparar-entrevistas-coding-anthony-mays]] — DSA/Big O como ferramenta para saber que perguntas fazer numa entrevista técnica, pela perspectiva de um ex-entrevistador
- [[wiki/sources/como-praticar-leetcode-da-forma-certa-anthony-mays]] — estudo de DSA prepara o brainstorm de soluções (etapa 7 de "Os Seis Passos"), incluindo o princípio de trocar espaço por velocidade
- [[wiki/sources/tres-projetos-para-aprender-programar]] — Pathfinding como projeto que introduz algoritmos como estratégia de resolução de problema, não como sintaxe
- [[wiki/sources/binary-search-em-5-minutos]] — binary search (passo 3 da sequência de aprendizado acima) resolvido do zero até implementação real, com técnica de two pointers
- [[wiki/sources/resolvendo-3-problemas-classicos-entrevista-coding-dsa]] — três problemas de entrevista resolvidos em versão ingênua e versão ótima (array+hash set, hashmap+bucket sort, two pointers), com ênfase em por que a explicação do raciocínio importa mais que a resposta
- [[wiki/sources/busca-linear-e-binaria-giovana]] — busca (passo 3 da sequência) via analogia física + código JS, defendendo o método "teoria no papel antes do código"
- [[wiki/sources/como-ficar-bom-em-leetcode]] — lista das estruturas que "cobrem quase tudo" (array, linked list, queue, stack, binary tree, hash map, graph) e o loop estrutura→padrão→repetição para dominá-las; ênfase em implementar cada uma por conta própria
- [[wiki/sources/por-que-comecar-com-c-em-2026-cs50-david-malan]] — David Malan (CS50): construir as próprias estruturas (hash tables, listas ligadas, tries, árvores, pilhas, filas) em [[wiki/concepts/linguagem-c|C]] porque a linguagem não as oferece prontas; valor não é reusar a implementação, mas entender design e diagnóstico por primeiros princípios
