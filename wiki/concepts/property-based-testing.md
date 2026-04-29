---
type: concept
title: "Property-Based Testing"
aliases: ["property based testing", "teste baseado em propriedades", "hypothesis", "fast-check"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_count: 1
tags: [testes, race-condition, confiabilidade, hypothesis, fast-check, concorrencia]
skill: tech-mentor-ai
status: stub
---

## TL;DR

Em vez de testar "dado input X, espero output Y", você define uma **propriedade invariante** que deve ser verdadeira em qualquer situação (ex: "o saldo nunca deve ser negativo"). A biblioteca gera e bombardeia a função com inputs aleatórios — incluindo combinações concorrentes — e falha se a propriedade for violada.

## Por que é Eficaz para Race Conditions

Race conditions aparecem em combinações específicas de timing que testes manuais raramente cobrem. Property-based testing gera essas combinações automaticamente, encontrando os casos que você não pensou em testar.

## Bibliotecas

| Stack | Biblioteca |
|---|---|
| Python | `hypothesis` |
| JavaScript/Node | `fast-check` |
| Java | `jqwik` |
| Go | `gopter` |
| Haskell | `QuickCheck` (original) |

## Relacionado

- [[piramide-de-testes]] — onde property-based testing se encaixa
- [[vibe-coding]] — técnica especialmente útil para verificar código gerado por IA

## Key Sources

- [[sources/apagao-de-seniors-vibe-coding]]
