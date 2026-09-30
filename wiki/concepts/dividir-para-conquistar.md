---
type: concept
title: "Dividir para Conquistar"
aliases: ["divide and conquer", "divide-and-conquer", "dividir e conquistar"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [cs-fundamentals, algoritmos, recursao, dividir-para-conquistar]
skill: cs-fundamentals
status: draft
---

# Dividir para Conquistar

Estratégia de projeto de algoritmos: quebrar o problema em subproblemas menores do mesmo tipo até chegar a um **caso base** trivial, resolver os pequenos e **combinar** os resultados.

## Receita (como apresentada na fonte)

1. Definir o caso base (o problema mais simples que não precisa ser dividido — ex.: array vazio ou de 1 elemento na ordenação).
2. Reduzir o problema a cada chamada até chegar nele.
3. Ao retornar da recursão, combinar as respostas parciais (no [[wiki/concepts/quicksort]]: `esquerdo + pivô + direito`).

O ganho de eficiência vem de o tamanho do problema **diminuir a cada chamada** (comportamento de [[wiki/concepts/logaritmo]]) — por isso o Quicksort é n·log n e não uma recursão sem controle.

## Exemplos na wiki

- [[wiki/concepts/quicksort]] — particiona por pivô, combina por concatenação
- Merge Sort — divide ao meio, combina por mesclagem ([[wiki/concepts/algoritmos-de-ordenacao]])
- [[wiki/concepts/algoritmos-de-busca]] — busca binária descarta metade a cada passo (variante sem combinação)
- Mecanismo: [[wiki/concepts/recursao]]

## Key sources

- [[wiki/sources/ordenacao-selection-quicksort-bubble-sort-live-coding]] — estratégia base do Quicksort; caso base + redução + combinação
