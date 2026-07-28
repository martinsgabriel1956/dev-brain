---
type: entity
title: "Meta"
aliases: ["Facebook", "Meta Platforms"]
date_created: 2026-07-16
date_updated: 2026-07-28
source_count: 2
tags: [empresa, demissao, ai-washing, era-agentica, graphql, api-design]
skill: tech-mentor-ai
status: stub
---

# Meta

Big tech dona do Facebook, Instagram e WhatsApp. O CEO Mark Zuckerberg admitiu, em memorando interno, que a tecnologia de agentes de IA não progrediu tão rápido quanto esperado e que a empresa cometeu erros ao reestruturar equipes antecipando ganhos de produtividade por IA que ainda não se confirmaram — ver [[wiki/concepts/ai-washing]] e [[wiki/concepts/roi-de-ia]].

## O Memorando

> "Dada a complexidade dessas mudanças, cometemos erros e quase certamente cometeremos mais [...] não quero prometer demais, porque o mundo está mudando de maneiras que estão fora do nosso controle." — Mark Zuckerberg

Um exemplo concreto de erro citado: o assistente de recuperação de senha do Instagram, ao incorporar IA, passou a recitar senhas de usuários. Zuckerberg reiterou que a Meta não espera mais demissões em massa em toda a empresa neste ano — em contraste direto com a [[wiki/entities/microsoft]], que fez sua primeira grande onda de demissões dias antes.

## Criadora do GraphQL

A Meta (então Facebook) criou o [[wiki/concepts/graphql]], motivada pela necessidade de múltiplos frontends (mobile, web, iPad), evoluindo rapidamente, buscarem dados profundamente aninhados (usuário → post → comentário) sem multiplicar endpoints REST especializados por tela — e sem sofrer do problema de [[wiki/concepts/n-plus-one]] entre frontend e backend. Ver [[wiki/sources/problema-n-mais-1-graphql-orm-solucoes]].

## Key Sources

- [[wiki/sources/custo-real-ia-tokens-produtividade-demissoes]]
- [[wiki/sources/problema-n-mais-1-graphql-orm-solucoes]] — origem do GraphQL como resposta ao N+1/over-under-fetching
