---
type: concept
title: "Tradução de Lógica para Código"
aliases: ["código como tradução", "logic to code", "implementação como tradução"]
date_created: 2026-05-13
date_updated: 2026-05-13
source_count: 1
tags: [traducao, implementacao, fundamentos, cs-fundamentals]
skill: cs-fundamentals
status: draft
---

# Tradução de Lógica para Código

O princípio de que escrever código é um ato de **tradução** — não de criação. Quando o problema foi entendido, decomposto e o [[fluxo-logico]] foi desenhado, cada linha de código corresponde a uma decisão já tomada.

## Por que isso importa

Programadores que "criam" código enquanto pensam no problema descobrem as decisões no momento mais caro possível. Programadores que "traduzem" um fluxo já mapeado escrevem código mais rápido, com menos bugs e mais fácil de revisar.

## O que muda entre linguagens

A lógica **não muda**. O mesmo fluxo de autenticação do caixa eletrônico pode ser escrito em Python, Java ou JavaScript. O que muda é apenas a sintaxe — as palavras usadas para expressar as mesmas decisões.

## Correspondência decisão → código

| Decisão no fluxo | Linha de código |
|---|---|
| "o cartão existe?" | `if not cartao_existe(cartao)` |
| "permite até 3 tentativas" | `while tentativas < MAX_TENTATIVAS` |
| "bloqueia se esgotou tentativas" | `bloquear_cartao(cartao)` |

## Relação com outros conceitos

- É o passo 4 (e final) de [[logica-de-programacao]]
- Depende de [[fluxo-logico]] como entrada
- Usa [[fluxo-de-controle]] como vocabulário
- O [[estado]] identificado no fluxo vira variáveis no código

## Key sources

- [[wiki/sources/logica-de-programacao-quatro-passos]]
