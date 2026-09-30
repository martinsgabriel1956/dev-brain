---
type: concept
title: "Descarte de Constantes em Big O"
aliases: ["dropping constants", "constantes em Big O", "ignorar constantes"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [cs-fundamentals, big-o, complexidade, algoritmos]
skill: cs-fundamentals
status: draft
---

# Descarte de Constantes em Big O

Regra da notação [[wiki/concepts/big-o]]: fatores constantes (½, 2, 3…) e termos menores são ignorados — O(n · ½ · n) é O(n²), O(2n) é O(n).

## Justificativa dada na fonte

Para entradas enormes (ex.: n = 500 milhões), n² é gigantesco e n²/2 continua da mesma ordem de grandeza — a constante "não faz cosquinha". Big O serve para comparar **crescimento em escala**, não medir 50 ou 100 elementos (onde qualquer algoritmo serve).

## Justificativa mais precisa [skill: cs-fundamentals]

Constantes não mudam a **classe de crescimento**: dobrar n multiplica o trabalho por 4 tanto em n² quanto em n²/2. Constantes ainda importam na prática entre algoritmos de mesma classe (ex.: Insertion Sort vence em arrays pequenos por ter constante baixa) — a fonte afirma o oposto de forma absoluta ao dizer que não importam em nenhuma análise; a regra vale para a *notação*, não para escolha de implementação em entradas pequenas.

## Onde aparece

- [[wiki/concepts/selection-sort]] — n + (n−1) + … ≈ n²/2 → O(n²)
- [[wiki/concepts/algoritmos-de-ordenacao]]

## Key sources

- [[wiki/sources/ordenacao-selection-quicksort-bubble-sort-live-coding]] — média de n/2 comparações no Selection Sort não muda O(n²); argumento de escala
