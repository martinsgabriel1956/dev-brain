---
type: concept
title: "Comprehension Debt"
aliases: ["comprehension debt", "dívida de compreensão", "dívida cognitiva código ia"]
date_created: 2026-04-23
date_updated: 2026-08-03
source_count: 5
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

**Correção (2026-07-16, a partir da fonte primária de Storey):** a estatística de +14% de esforço mental vem de uma pesquisa citada pela HBR sobre supervisão de IA, não do post original de Margaret-Anne Storey. Na fonte primária de Storey, dívida cognitiva é definida de forma mais ampla e sem essa métrica: é a distância entre a velocidade de geração de código da IA e a capacidade real do time de reter a *teoria do programa* (ver [[wiki/concepts/teoria-do-programa-naur]]) — ou seja, um fenômeno **coletivo/de time**. Comprehension debt, por outro lado, é a erosão *individual e progressiva* da capacidade da pessoa de entender o próprio código que ela mesma aprovou. São facetas do mesmo problema em escalas diferentes: dívida cognitiva é o risco de time perder a teoria compartilhada; comprehension debt é o mecanismo pelo qual um indivíduo perde a sua própria.

## Como Mitigar

- **Leia o código, não só os testes:** 48% dos devs não checam o código antes de commitar
- **Escreva testes que documentam comportamento,** não implementação — força entendimento
- **Explique o código em voz alta (rubber duck)** antes de aprovar
- **Reveze código manual + código de agente** para manter a capacidade de escrever

## Nota de Atribuição: "Dívida de Compreensão" em Terceira Fonte

[[wiki/sources/cinco-escolas-programacao-com-ia]] cita o mesmo fenômeno sob o nome "dívida de compreensão", atribuindo-o a Addy Osmani (Google). A wiki já registra, a partir da fonte primária ([[wiki/sources/addy-osmani-80-problem-agentic-coding]]), que quem **cunhou** o termo foi Jeremy Twei — Osmani é o autor do artigo que **popularizou** o conceito. Não é uma contradição de fato (cunhar ≠ popularizar), mas a nova fonte reforça que a atribuição a Osmani, isoladamente, tende a se espalhar de forma imprecisa — vale manter a distinção cunhagem/popularização explícita em fontes futuras.

## Key Sources

- [[sources/addy-osmani-80-problem-agentic-coding]]
- [[sources/erros-workflow-research-plan-implement]] — não ler o código durante o research é o caminho direto para comprehension debt
- [[sources/context-engineering-avancado-para-coding-agents]] — mental alignment como antídoto coletivo
- [[wiki/sources/cognitive-debt-margaret-storey]] — fonte primária de "cognitive debt"; corrige a atribuição da estatística de +14% (é da HBR, não de Storey) e fundamenta a distinção individual/coletivo com a teoria do programa de Naur
- [[wiki/sources/cinco-escolas-programacao-com-ia]] — terceira fonte independente para o mesmo fenômeno ("dívida de compreensão"), com nota de atribuição a corrigir (cunhagem vs. popularização)
