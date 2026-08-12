---
type: source
title: "Algoritmos de Busca: Busca Linear e Busca Binária (Giovana / Alura)"
aliases: ["busca linear e binária", "linear search binary search giovana", "algoritmos de busca alura"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_count: 0
tags: [cs-fundamentals, algoritmos, busca, linear-search, binary-search, big-o, logaritmo, javascript]
skill: cs-fundamentals
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/busca-linear-e-binaria-giovana.md
source_url:
author: Giovana (canal Alura)
date_published:
date_ingested: 2026-08-12
---

# Algoritmos de Busca: Busca Linear e Busca Binária (Giovana / Alura)

## TL;DR

Aula introdutória sobre [[wiki/concepts/algoritmos-de-busca|algoritmos de busca]] contrastando **busca linear** (percorre elemento por elemento, O(n)) e **busca binária** (divide o intervalo pela metade a cada passo, O(log n), exige array ordenado). Ancora a teoria em duas analogias concretas antes de qualquer código: procurar a página 310 num livro de 423 páginas (linear = ~310 etapas; binária = 4 etapas) e um array de 8 elementos buscando o valor 7. Implementa ambos em JavaScript com **contador de etapas** para tornar a diferença tangível (7 vs. 3 etapas no array de 8), e fecha com a derivação matemática da complexidade logarítmica: `2^x = n`, base 2 do [[wiki/concepts/logaritmo|logaritmo binário]], com tabela de crescimento (8→~4, 64→~7, 128→~8 etapas para a binária, contra n linear). Método pedagógico explícito: **teoria no papel antes do código**, e a linguagem como "última coisa com que se preocupar".

## Key Claims

| Claim | Evidence | Confidence |
|---|---|---|
| Busca linear percorre todos os elementos, verificando um a um | "Você percorre todos os elementos da lista e faz uma verificação para cada elemento" | Alta |
| Busca binária só funciona em lista ordenada | "esse algoritmo ele só funciona se a sua lista estiver ordenada... precisa ser ordenada" | Alta |
| Busca binária divide o intervalo pela metade a cada etapa | Analogia do livro: 200 → 332 → 277 → 310 em 4 etapas contra ~310 na linear | Alta |
| No pior caso a busca linear é O(n); complexidade sempre assume o pior cenário | "a gente sempre pega o pior cenário possível... por isso a complexidade é o n" | Alta |
| Busca binária é O(log n); o `+1` de O(log n + 1) é descartado | "em complexidade a gente sempre pega o maior fator, esse mais um se torna irrelevante" | Alta |
| A base do logaritmo na complexidade é sempre 2 (logaritmo binário), por isso omitida | "a base sempre vai ser dois quando a gente fala sobre complexidade logarítmica" | Alta |
| Ponto médio via `Math.floor((first + last) / 2)`; em JS inteiro/inteiro pode dar decimal | "no JavaScript... um inteiro dividindo por um inteiro dá um número decimal... a gente usa Math.floor" | Alta |
| Convenção de retornar `-1` quando o elemento não é encontrado (índice impossível) | "é uma boa prática... retornar o -1 porque é o index que é impossível de ser atingido" | Alta |
| Ordenação prévia (ex.: Quicksort) é pré-requisito da busca binária | "existem diversos algoritmos de ordenação que também são eficientes, como é o caso do Quicksort" | Alta ("PicsArt" no ASR = Quicksort) |

## Derivação da complexidade logarítmica

`a^x = B` com `a = 2` (base binária) e `B = n` (logaritimando). Logo `2^x = n`.
Para n = 8: `2^x = 8` → `x = 3`; somando o `+1` → **4 etapas** no máximo.

| Total de elementos | Busca binária (~log₂n) | Busca linear (n) |
|---|---|---|
| 8   | ~4  | 8   |
| 64  | ~7  | 64  |
| 128 | ~8  | 128 |

## Pseudocódigo central (busca binária iterativa)

```javascript
function buscaBinaria(array, target) {
  let firstIndex = 0;
  let lastIndex = array.length - 1;
  while (lastIndex >= firstIndex) {
    const midIndex = Math.floor((firstIndex + lastIndex) / 2);
    if (target > array[midIndex]) firstIndex = midIndex + 1;
    else if (target < array[midIndex]) lastIndex = midIndex - 1;
    else return midIndex;
  }
  return -1;
}
```

Note que esta é a mesma estrutura de dois índices (`first`/`last`) da técnica [[wiki/concepts/two-pointer|two pointers]] documentada em [[wiki/sources/binary-search-em-5-minutos]], apenas com nomes diferentes (`left`/`right`).

## Entidades Mencionadas

- [[wiki/entities/alura]] — escola de tecnologia; canal que publica o vídeo
- [[wiki/entities/uncle-bob]] — Robert C. Martin, autor de *Código Limpo* (*Clean Code*), o livro usado como analogia física da busca

## Conceitos Tocados

- [[wiki/concepts/algoritmos-de-busca]]
- [[wiki/concepts/big-o]]
- [[wiki/concepts/logaritmo]]
- [[wiki/concepts/melhor-caso-pior-caso-caso-medio]]
- [[wiki/concepts/algoritmos-de-ordenacao]]
- [[wiki/concepts/two-pointer]]
- [[wiki/concepts/algoritmos-e-estruturas-de-dados]]
- [[wiki/concepts/array]]

## Open Questions

- A fonte usa `Math.floor((first + last) / 2)` sem alertar para o **overflow de inteiros** em linguagens de tamanho fixo (JS não sofre, mas Java/C/etc. sim — forma segura `first + (last - first) / 2`). Lacuna coberta por `references/algorithms-complexity.md` da skill `cs-fundamentals` `[skill: cs-fundamentals]`.
- Não discute **variantes** de busca binária (`lower_bound`/`upper_bound`, busca em espaço de decisão monotônico) nem alternativas como jump/exponential/Fibonacci search citadas em [[wiki/sources/9-algoritmos-que-todo-programador-deveria-saber]].
- Diz "O(log n + 1)" como complexidade formal da busca binária: o `+1` reflete o número de iterações no pior caso, mas assintoticamente O(log n) já o absorve — a fonte trata isso corretamente ao descartá-lo.

## Raw Quotes

> "A busca linear eu preciso começar desde o primeiro elemento e ir fazendo uma verificação a cada elemento... O pior cenário possível é se o elemento que a gente tiver procurando for o último."

> "A gente vai fazendo uma divisão pela metade a cada etapa desse processo."

> "Esse algoritmo ele só funciona se a sua lista estiver ordenada."

> "A base sempre vai ser dois quando a gente fala sobre complexidade logarítmica, porque a gente está falando do logaritmo binário."

> "O código deve ser a última etapa desse processo."
