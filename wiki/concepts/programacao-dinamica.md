---
type: concept
title: "Programação Dinâmica (DP)"
aliases: ["dynamic programming", "DP", "programacao dinamica", "memoização"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_count: 1
tags: [cs-fundamentals, algoritmos, recursao, memoizacao, otimizacao]
skill: cs-fundamentals
status: stub
---

# Programação Dinâmica (DP)

Técnica para problemas com **subproblemas sobrepostos** e **subestrutura ótima**: resolve cada subproblema uma única vez e **guarda o resultado** (memoização top-down ou tabulação bottom-up), evitando a explosão exponencial da recursão ingênua. O exemplo canônico de entrada é o **Fibonacci**: a versão recursiva pura recomputa os mesmos valores em O(2ⁿ); com memoização cai para O(n).

A fonte de estudo de [[wiki/entities/leetcode|LeetCode]] recomenda **começar por Fibonacci em DP** para pegar a intuição antes de partir para problemas mais difíceis (mochila, LCS, edit distance).

## Relação com outros conceitos

- [[wiki/concepts/backtracking]] — DP frequentemente otimiza um backtracking exponencial cujos subproblemas se repetem
- [[wiki/concepts/big-o]] — o ganho de DP se lê justamente na complexidade: de exponencial para polinomial
- [[wiki/concepts/reconhecimento-de-padroes]] — "há subproblemas repetidos?" é o gatilho para reconhecer DP

## Key Sources

- [[wiki/sources/como-ficar-bom-em-leetcode]] — DP entre os padrões prioritários; recomendação de começar pelo Fibonacci
