---
type: concept
title: "Tese de Church-Turing"
aliases: ["Church-Turing thesis", "tese de church-turing", "Turing complete", "Turing-completo"]
date_created: 2026-09-03
date_updated: 2026-09-03
source_count: 1
tags: [cs-fundamentals, teoria-da-computacao, church-turing, computabilidade]
skill: cs-fundamentals
status: stub
---

# Tese de Church-Turing

Tese (não um teorema formalmente demonstrável, mas amplamente aceita) que estabelece uma equivalência de poder computacional entre dois modelos independentes de computação criados na década de 1930: o **lambda calculus** de **[[wiki/entities/alonso-church|Alonso Church]]** e a **[[wiki/concepts/maquina-de-turing|máquina de Turing]]** de **[[wiki/entities/alan-turing|Alan Turing]]**.

## O que ela diz

Qualquer função computável por um algoritmo pode ser computada tanto por lambda calculus quanto por uma máquina de Turing — os dois modelos, apesar de formulados de maneiras completamente diferentes, têm exatamente o mesmo poder expressivo. Nenhum modelo de computação já proposto consegue computar algo que esses dois não consigam.

## Turing-completude

Uma linguagem (ou sistema) é dita **Turing-completa** quando, dado tempo e memória suficientes, ela pode computar tudo aquilo que é computável — ou seja, ela tem o mesmo poder expressivo de uma máquina de Turing.

Praticamente todas as linguagens de programação de propósito geral usadas no mercado (Python, JavaScript, C, Java, Go, etc.) são Turing-completas. Exceções notáveis: HTML puro e CSS puro (por si só) não são Turing-completos — são linguagens declarativas sem os mecanismos de controle de fluxo/memória necessários.

## Consequência prática: recursão ⇔ iteração

Uma decorrência direta da tese de Church-Turing é que **todo algoritmo recursivo pode ser convertido em um algoritmo iterativo equivalente, e vice-versa** — nenhuma das duas formas tem poder computacional a mais que a outra. A diferença entre elas está em **onde e como a estrutura de suporte (a call stack) é alocada**: numa recursão "crua", o compilador/runtime aloca e administra a stack para você via `call`/`return`; numa versão iterativa, você aloca e administra essa estrutura manualmente. Ver [[wiki/concepts/tail-call-optimization]] para o caso em que o compilador consegue eliminar essa alocação por completo.

## Relação com outros conceitos

- [[wiki/concepts/maquina-de-turing]] — um dos dois modelos equivalentes da tese
- [[wiki/concepts/recursao]] — recursão e iteração são formas intercambiáveis de expressar o mesmo algoritmo, garantido pela tese
- [[wiki/concepts/tail-call-optimization]] — mecanismo concreto de compilador que realiza essa conversão recursão→iteração automaticamente em certos casos
- [[wiki/concepts/complexidade-computacional]] — a tese define o que é computável; complexidade computacional mede quão caro é computar

## Key sources

- [[wiki/sources/recursao-vs-iteracao-call-stack-tail-call-optimization]] — introdução da tese como justificativa formal para "toda recursão é conversível em iteração", com demonstração prática convertendo fatorial recursivo em iterativo em Python
