---
type: source
title: "Algoritmos de Ordenação: Bubble, Insertion, Selection, Merge, Quicksort e Heapsort"
aliases: ["6 algoritmos de ordenação", "bubble insertion selection merge quicksort heapsort", "aula ordenação concurso"]
date_created: 2026-09-03
date_updated: 2026-09-03
source_count: 0
tags: [cs-fundamentals, algoritmos, sorting, big-o, bubble-sort, insertion-sort, selection-sort, merge-sort, quicksort, heapsort, arvore-binaria, concurso]
skill: cs-fundamentals
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/algoritmos-de-ordenacao-bubble-insertion-selection-merge-quicksort-heapsort.md
source_url: ""
author: "desconhecido (aula com framing de preparação para concurso/prova)"
date_published: "desconhecida"
date_ingested: 2026-09-03
---

# Algoritmos de Ordenação: Bubble, Insertion, Selection, Merge, Quicksort e Heapsort

## TL;DR

Aula (autor não identificado, framing explícito de preparação para concurso) percorre seis algoritmos de ordenação com exemplos numéricos passo a passo: **Bubble Sort** (troca adjacentes, "borbulha" o maior para a direita, O(n²)), **Insertion Sort** (analogia com ordenar cartas de baralho, insere um elemento de cada vez na posição correta entre os já ordenados), **Selection Sort** (varre o arranjo inteiro a cada passada para achar o menor valor restante e fixá-lo na posição corrente — ao contrário do Insertion Sort, que agrega um elemento novo por vez), **Merge Sort** (divide recursivamente até restarem elementos únicos, depois mescla em ordem — a aula ancora a lembrança do algoritmo na tradução literal de "merge" = mesclar), **Quicksort** (escolhe um pivô, particiona em menores-à-esquerda/maiores-à-direita, repete recursivamente; pior caso quando o pivô escolhido é sempre um extremo do arranjo) e **Heapsort** (constrói um Max Heap sobre uma árvore binária armazenada em array, extrai a raiz — sempre o maior elemento — e rebalanceia). Complementa [[wiki/sources/9-algoritmos-que-todo-programador-deveria-saber]] (que já cobria Bubble, Insertion e Merge) com três algoritmos novos para a wiki: Selection Sort, Quicksort (mecanismo de partição, não só citação por contraste) e Heapsort.

## Key Claims

| Claim | Evidence | Confidence |
|---|---|---|
| Bubble Sort troca elementos adjacentes quando o da esquerda é maior, empurrando o maior valor para a direita a cada passagem | Exemplo passo a passo com `[-2, 45, 0, 11, -9]` até chegar em `[-9, -2, 0, 11, 45]` | Alta |
| Melhor caso do Bubble Sort é o arranjo já ordenado; pior caso é a ordem inversa | "para qual que é a melhor situação possível... o arranjo já ordenado e o pior caso o arranjo na ordem inversa" | Alta |
| Insertion Sort agrega um elemento de cada vez ao subconjunto já ordenado, inserindo na posição correta | Exemplo com cartas `[4, 2, 6, 0]` → `[0, 2, 4, 6]`, com o novo elemento sempre reposicionado à esquerda dos maiores | Alta |
| Selection Sort compara o arranjo inteiro a cada passada (diferente do Insertion Sort, que agrega incrementalmente) e fixa o menor valor restante na posição corrente | Exemplo com `[7, 4, 5, 9, 8, 2, 1]` → menor (1) fixado na posição 0, depois 2ª posição recebe o 2º menor (2), e assim sucessivamente | Alta |
| Merge Sort divide recursivamente o arranjo ao meio até restar um elemento, depois mescla em ordem crescente comparando par a par | Exemplo com `[6, 5, 12, 10, 9, 1]` dividido em subarranjos até elementos únicos, depois remontado como `[1, 5, 6, 9, 10, 12]` | Alta |
| Quicksort escolhe um pivô e particiona o arranjo em subarranjo de menores (esquerda) e maiores (direita) que o pivô, recursivamente | Exemplo com `[6, 5, 12, 10, 9, 1]` e pivô 5, produzindo subarranjo esquerdo `[1]` e direito `[6, 9, 10, 12]` | Alta |
| Pior caso do Quicksort ocorre quando o pivô escolhido é sempre um valor extremo do arranjo (maior ou menor), gerando partição desbalanceada | "qual que seria o pior caso... quando os pivôs eles são os extremos" — um dos lados fica vazio, sem segundo subarranjo real | Alta — mecanismo correto, mas a aula não nomeia explicitamente a complexidade O(n²) resultante, nem menciona estratégias de mitigação (pivô aleatório, mediana de três) |
| Heapsort usa uma estrutura auxiliar (heap) sobre uma árvore binária; o algoritmo constrói um Max Heap (raiz sempre o maior valor) e extrai a raiz repetidamente | Exemplo de rebalanceamento comparando pares pai-filho: `[1, 12]` → `[12, 1]`, depois `[5, 1, 6]` → `[6, 5, 1]`, mantendo a invariante "elemento pai maior que os filhos" | Alta — mecanismo de construção do Max Heap está correto; a aula não chega a demonstrar o passo de extração-e-rebalanceamento repetido que produz o array ordenado final, só a construção do heap |

## Entidades e Conceitos Tocados

- [[wiki/concepts/algoritmos-de-ordenacao]]
- [[wiki/concepts/big-o]]
- [[wiki/concepts/recursao]]
- [[wiki/concepts/algoritmos-de-busca]]

## Contradições / Reforços com o Resto da Wiki

**Reforço direto, sem contradição:** [[wiki/concepts/algoritmos-de-ordenacao]] já cobria Bubble Sort (O(n²)), Insertion Sort (O(n²)/O(n) melhor caso) e Merge Sort (O(n log n), estável, O(n) de espaço) via [[wiki/sources/9-algoritmos-que-todo-programador-deveria-saber]]. Esta fonte confirma o mesmo mecanismo para os três com exemplos numéricos diferentes, e adiciona três algoritmos que a página só citava por contraste ou não tinha: Selection Sort (ausente até agora), Quicksort com mecanismo de partição detalhado (antes só citado como "in-place, quase tão bom quanto Merge Sort", sem exemplo do pivô), e Heapsort (ausente até agora, apesar de já referenciado como linha da tabela de complexidade em `references/algorithms-complexity.md`, skill `cs-fundamentals`).

**Gap não coberto pela fonte, mas coberto pela skill:** a aula não menciona a complexidade de tempo/espaço formal (O grande) de nenhum dos seis algoritmos — foco total em mecanismo passo a passo, sem análise assintótica. Os valores de complexidade citados nas páginas da wiki vêm de `references/algorithms-complexity.md` (skill `cs-fundamentals`), marcados como `[skill: cs-fundamentals]`, não desta fonte.

## Open Questions

- **Heapsort: extração e rebalanceamento repetidos não demonstrados.** A fonte mostra em detalhe a construção do Max Heap (comparações pai-filho, "sift up"), mas não chega a demonstrar o passo seguinte do algoritmo — extrair a raiz repetidamente e rebalancear ("sift down") até obter o array totalmente ordenado. O mecanismo completo do Heapsort fica incompleto nesta fonte.
- **Quicksort: nenhuma estratégia de mitigação do pior caso é mencionada** (pivô aleatório, mediana de três, introsort) — a fonte identifica corretamente a causa do pior caso (pivô sempre extremo), mas não cobre como implementações reais evitam isso na prática.
- **Autoria e contexto não identificados** — a transcrição tem framing de preparação para concurso público ("já pode te auxiliar na hora de resolver a questão do concurso"), mas não há nome de autor, canal ou curso na transcrição fornecida.

## Raw Quotes

> "A ideia é sempre passar o elemento maior para a direita."

> "É como se você tivesse ordenando ali um conjunto de cartas que você acabou de receber num jogo."

> "Lembra quando fala de *merge*, lembra que tem esse processo de mesclar — então só de saber a tradução da palavra *merge* já pode te auxiliar na hora de resolver a questão do concurso."

> "Sempre a raiz tem que ser maior do que os elementos filhos."
