---
type: concept
title: "Comprehension Debt"
aliases: ["comprehension debt", "dívida de compreensão", "dívida cognitiva código ia"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 1
tags: [ia, agentes, qualidade, ownership, cognição, divida-tecnica]
skill: tech-mentor-ai
status: stable
---

# Comprehension Debt

Termo cunhado por Jeremy Twei: a dívida que se acumula quando você revisa e aprova código que entende superficialmente — até perder a capacidade de tomar decisões arquiteturais sobre seu próprio codebase.

## O Mecanismo

**Geração de código** (escrever) e **discriminação de código** (ler criticamente) são capacidades cognitivas distintas. Você pode revisar código competentemente mesmo após sua capacidade de escrevê-lo do zero ter atrofiado. Mas existe um threshold onde "revisão" vira "rubber stamping".

O agente não se cansa. Ele sprinta através de implementação após implementação com confiança inabalável. O código parece plausível. Os testes passam. Você está sob pressão. Você move em frente.

**Com o tempo, você entende menos do seu próprio codebase.**

## O Loop de Vício

> "O agente implementou uma feature incrível e errou talvez 10% da coisa, e você pensa: 'eu consigo arrumar isso com mais 5 minutos de prompt'. Isso foi 5 horas atrás." — Yoko Li

A promessa de estar "quase lá" é o hook psicológico. Cada iteração adicional aumenta a comprehension debt sem você perceber.

## Relação com Abstraction Bloat

[[concepts/abstraction-bloat]] e comprehension debt se reforçam: o agente gera complexidade desnecessária → você aprova porque "parece certo" → você entende cada vez menos → você aprova ainda mais sem questionar.

## Diferença de [[concepts/divida-cognitiva]]

Dívida cognitiva (Margaret Storey, 2026) é o esforço mental extra de supervisionar IA (+14%). Comprehension debt é a *erosão progressiva* da capacidade de entender o próprio código. São fenômenos relacionados mas distintos.

## Como Mitigar

- **Leia o código, não só os testes:** 48% dos devs não checam o código antes de commitar
- **Escreva testes que documentam comportamento,** não implementação — força entendimento
- **Explique o código em voz alta (rubber duck)** antes de aprovar
- **Reveze código manual + código de agente** para manter a capacidade de escrever

## Key Sources

- [[sources/addy-osmani-80-problem-agentic-coding]]
