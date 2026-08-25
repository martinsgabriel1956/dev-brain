---
type: concept
title: "Logaritmo"
aliases: ["logaritmo binário", "log n", "log2", "logarithm"]
date_created: 2026-08-12
date_updated: 2026-08-25
source_count: 2
tags: [cs-fundamentals, matematica, big-o, logaritmo, complexidade]
skill: cs-fundamentals
status: draft
---

# Logaritmo

Operação inversa da exponenciação: `log_a(B) = x` significa `a^x = B`, onde `a` é a **base** e `B` é o **logaritimando**. Responde à pergunta "a que potência preciso elevar a base para chegar em B?".

## Por que aparece em complexidade de algoritmos

Sempre que um algoritmo **descarta uma fração constante do problema a cada passo**, o número de passos cresce logaritmicamente com o tamanho da entrada. Na [[wiki/concepts/algoritmos-de-busca|busca binária]], cada iteração corta o intervalo pela metade, então o número de passos é `log₂(n)`.

- **Base 2 (logaritmo binário):** por isso a notação [[wiki/concepts/big-o|Big O]] escreve apenas `O(log n)` sem indicar a base — em complexidade a base é uma constante multiplicativa e é descartada (mudar de base só muda o resultado por um fator constante).
- Derivação prática: para achar quantos passos a busca binária leva em `n` elementos, resolve-se `2^x = n`. Ex.: `n = 8` → `2^x = 8` → `x = 3`.

O crescimento logarítmico é o que torna a busca binária tão eficiente: dobrar o tamanho da entrada adiciona apenas **um** passo (8→~4 passos, 64→~7, 128→~8), contra o crescimento linear O(n) da busca linear.

## Relação com outros conceitos

- [[wiki/concepts/big-o]] — O(log n) como uma das curvas fundamentais de complexidade
- [[wiki/concepts/algoritmos-de-busca]] — busca binária como o exemplo canônico de complexidade logarítmica
- [[wiki/concepts/algoritmos-de-ordenacao]] — O(n log n) dos algoritmos de ordenação eficientes (ex.: Quicksort, Merge Sort)

### Analogia didática (log₁₀)

`log₁₀(100)` responde "quantos 10 eu consigo multiplicar para chegar a 100?" — a resposta é 2 (`10 × 10 = 100`). É a mesma pergunta feita em base 2 na busca binária: "quantas vezes eu divido n por 2 até sobrar 1?"

## Key sources

- [[wiki/sources/busca-linear-e-binaria-giovana]] — derivação `2^x = n`, base 2 do logaritmo binário e por que o `+1` de O(log n + 1) é descartado
- [[wiki/sources/busca-binaria-fila-protocolos-atendimento-live-coding]] — analogia log₁₀(100) = 2 ("quantos 10 para chegar a 100") como ponte didática para log₂(n) em busca binária
