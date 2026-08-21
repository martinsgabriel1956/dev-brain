---
type: concept
title: "Programação Dinâmica (DP)"
aliases: ["dynamic programming", "DP", "programacao dinamica", "memoização"]
date_created: 2026-08-12
date_updated: 2026-08-18
source_count: 2
tags: [cs-fundamentals, algoritmos, recursao, memoizacao, otimizacao]
skill: cs-fundamentals
status: stub
---

# Programação Dinâmica (DP)

Técnica para problemas com **subproblemas sobrepostos** e **subestrutura ótima**: resolve cada subproblema uma única vez e **guarda o resultado** (memoização top-down ou tabulação bottom-up), evitando a explosão exponencial da recursão ingênua. O exemplo canônico de entrada é o **Fibonacci**: a versão recursiva pura recomputa os mesmos valores em O(2ⁿ); com memoização cai para O(n).

A fonte de estudo de [[wiki/entities/leetcode|LeetCode]] recomenda **começar por Fibonacci em DP** para pegar a intuição antes de partir para problemas mais difíceis (mochila, LCS, edit distance).

**Por que a Fibonacci recursiva ingênua é O(2ⁿ):** [[wiki/sources/recursao-fatorial-fibonacci-javascript]] traça a árvore de chamadas de `fibonacci(p - 1) + fibonacci(p - 2)` sem citar o custo, mas o padrão de recomputação já aparece implícito no trace — `fibonacci(3)` é recalculado do zero dentro de `fibonacci(5)` e de `fibonacci(4)`, sem reuso. Esse é exatamente o ponto onde a introdução didática de recursão pura precisa de um próximo passo: trocar a recursão ingênua por memoização (guardar `fibonacci(p)` já calculado num `Map`/array) transforma O(2ⁿ) em O(n).

## Relação com outros conceitos

- [[wiki/concepts/backtracking]] — DP frequentemente otimiza um backtracking exponencial cujos subproblemas se repetem
- [[wiki/concepts/big-o]] — o ganho de DP se lê justamente na complexidade: de exponencial para polinomial
- [[wiki/concepts/reconhecimento-de-padroes]] — "há subproblemas repetidos?" é o gatilho para reconhecer DP

## Key Sources

- [[wiki/sources/como-ficar-bom-em-leetcode]] — DP entre os padrões prioritários; recomendação de começar pelo Fibonacci
- [[wiki/sources/recursao-fatorial-fibonacci-javascript]] — trace da Fibonacci recursiva ingênua em JavaScript (sem memoização), base concreta para entender por que ela é O(2ⁿ)
