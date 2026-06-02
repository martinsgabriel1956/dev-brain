---
type: entity
title: "Edsger Dijkstra"
aliases: ["Dijkstra", "EWD"]
date_created: 2026-06-01
date_updated: 2026-06-01
source_count: 1
tags: [cs-fundamentals, linguagem, programacao, matematica]
skill: cs-fundamentals
status: stub
---

# Edsger Dijkstra

Cientista da computação holandês (1930–2002). Criador do algoritmo de caminho mínimo (Dijkstra's algorithm), Turing Award 1972. Defensor rigoroso da programação formal e da precisão matemática em software.

## Argumento sobre linguagem natural em programação

Dijkstra criticava a presunção de que programar em linguagem natural seria mais fácil ou mais poderoso. Seu argumento, via analogia com a notação matemática:

> Uma linguagem de programação é uma interface propositalmente pequena, com número limitado de instruções e estrutura rígida. Ao remover tudo de humano e deixar só o necessário para executar a tarefa, a linguagem se torna mais poderosa — não menos.

Exemplo direto: `let x = 0` é mais curto, mais preciso e menos ambíguo do que "inicialize uma variável com valor zero" ou "defina um número zero".

## Relevância para LLMs

O argumento de Dijkstra prediz exatamente o comportamento observado em LLMs: uma LLM replicará as ambiguidades presentes na descrição em linguagem natural. Se o texto não especifica mutabilidade, validação ou paralelismo, o código gerado também não especificará.

## Key sources

- [[wiki/sources/logica-de-programacao-o-que-e-de-verdade]] — argumento sobre notação matemática vs. linguagem natural
