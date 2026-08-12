---
type: concept
title: "Sliding Window"
aliases: ["janela deslizante", "sliding window", "janela móvel"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_count: 1
tags: [cs-fundamentals, algoritmos, array, string, two-pointer]
skill: cs-fundamentals
status: stub
---

# Sliding Window

Padrão que mantém uma **janela contígua** (subarray/substring) sobre uma estrutura linear e a move avançando suas bordas, em vez de recomputar cada subintervalo do zero. Reduz problemas que pareceriam O(n²) — testar todos os subarranjos — para uma única passagem O(n), reaproveitando o trabalho da janela anterior a cada passo.

É parente próximo do [[wiki/concepts/two-pointer|two pointer]]: os dois índices delimitam a janela; um a expande, o outro a contrai conforme uma condição. Um dos padrões prioritários para treinar sobre [[wiki/concepts/array|arrays]] e strings no [[wiki/entities/leetcode|LeetCode]].

## Relação com outros conceitos

- [[wiki/concepts/two-pointer]] — a janela é delimitada por dois índices móveis; sliding window é uma especialização com semântica de "intervalo contíguo"
- [[wiki/concepts/array]] — depende de acesso O(1) por índice
- [[wiki/concepts/reconhecimento-de-padroes]] — reconhecer "subarray/substring contíguo ótimo" ≈ sliding window

## Key Sources

- [[wiki/sources/como-ficar-bom-em-leetcode]] — listado entre os padrões prioritários a dominar sobre arrays
