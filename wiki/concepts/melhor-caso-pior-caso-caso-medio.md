---
type: concept
title: "Melhor Caso, Pior Caso e Caso Médio"
aliases: ["best case", "worst case", "average case", "melhor caso", "pior caso", "caso médio"]
date_created: 2026-07-10
date_updated: 2026-08-25
source_count: 4
tags: [cs-fundamentals, big-o, complexidade, algoritmos]
skill: cs-fundamentals
status: draft
---

# Melhor Caso, Pior Caso e Caso Médio

A complexidade de um algoritmo não é um número único — depende de qual instância do problema você está medindo. Toda operação tem (pelo menos) três cenários possíveis, e confundir os três leva a expectativas erradas de performance.

## As três variantes

Exemplo canônico: busca linear numa lista.

| Cenário | O que acontece | Complexidade típica |
|---|---|---|
| **Melhor caso** | O item procurado está na primeira posição | O(1) |
| **Pior caso** | O item está na última posição ou não existe | O(n) |
| **Caso médio** | Comportamento típico ao longo de muitas execuções | O(n) |

## Convenção em entrevistas

Quando alguém pergunta "qual a complexidade desse algoritmo?" sem qualificar, a resposta esperada quase sempre é o **pior caso** — é o cenário que garante um teto de performance, independente da sorte da entrada.

## Por que caso médio importa na prática

Se uma operação roda milhares de vezes por dia em produção, o comportamento médio é o que efetivamente define custo e latência percebida — não o pior caso isolado, que pode ser raro. Ver [[wiki/concepts/big-o]] para a métrica que formaliza esse crescimento.

## Exemplo já registrado: Insertion Sort

[[wiki/sources/9-algoritmos-que-todo-programador-deveria-saber]] já documentou um caso concreto dessa distinção: Insertion Sort é O(n²) no caso médio e pior caso, mas **O(n) no melhor caso** (dados já quase ordenados) — por isso é uma boa escolha quando se sabe de antemão que a entrada está quase ordenada, e uma péssima escolha para dados invertidos.

## Relação com outros conceitos

- [[wiki/concepts/big-o]] — a notação que formaliza cada um desses casos
- [[wiki/concepts/algoritmos-de-busca]] — busca linear como exemplo didático dos três cenários
- [[wiki/concepts/algoritmos-e-estruturas-de-dados]] — escolher estrutura pensando na operação mais frequente é, na prática, otimizar para o caso médio

## Key sources

- [[wiki/sources/estruturas-de-dados-algoritmos-big-o-como-escolher]]
- [[wiki/sources/busca-linear-e-binaria-giovana]] — busca linear como exemplo dos três cenários (melhor caso O(1) na primeira posição; pior caso O(n) no fim/ausente), e o princípio de que a complexidade sempre assume o pior cenário
- [[wiki/sources/busca-binaria-fila-protocolos-atendimento-live-coding]] — "seja qual for o número, você adivinha em no máximo 7 tentativas" (100 itens) é uma garantia de pior caso, não de caso médio
- [[wiki/sources/como-calcular-complexidade-de-algoritmos-big-o-em-3-passos]] — define complexidade explicitamente como a contagem de passos "no pior caso possível", antes mesmo de introduzir a notação Big-O
