---
type: concept
title: "Escolha do Pivô (Quicksort)"
aliases: ["pivot selection", "escolha do pivô", "pivô do quicksort"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [cs-fundamentals, algoritmos, sorting, quicksort, big-o]
skill: cs-fundamentals
status: draft
---

# Escolha do Pivô (Quicksort)

Decisão de qual elemento serve de pivô em cada chamada do [[wiki/concepts/quicksort]]. Não afeta a **correção** (funciona com qualquer pivô), mas determina o **equilíbrio da partição** e, com ele, o tempo de execução.

## Estratégias citadas

- Primeiro elemento (usado nos exemplos da live)
- Elemento do meio
- Último elemento
- Elemento aleatório

## Impacto

- Pivô que divide ~ao meio → ~log n níveis → O(n log n).
- Pivô extremo (mínimo/máximo) repetidamente → partição desbalanceada → O(n²).
- A fonte afirma que, com pivô do meio, um array já ordenado ainda dá O(n log n) — correto, e é o motivo de o pior caso não ser "o formato da entrada" e sim o par entrada × estratégia: com pivô = primeiro, o array já ordenado é o pior caso.
- Mitigações usuais: pivô aleatório ou mediana de três (ver [[wiki/concepts/algoritmos-de-ordenacao]], [skill: cs-fundamentals]).

Ver [[wiki/concepts/melhor-caso-pior-caso-caso-medio]].

## Key sources

- [[wiki/sources/ordenacao-selection-quicksort-bubble-sort-live-coding]] — primeiro/meio/último/aleatório; a eficiência do Quicksort está atrelada ao pivô
