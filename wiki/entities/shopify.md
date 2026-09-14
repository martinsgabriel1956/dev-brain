---
type: entity
title: "Shopify"
aliases: ["shopify inc"]
date_created: 2026-07-07
date_updated: 2026-09-14
source_count: 2
tags: [e-commerce, mysql, redis, skip-locked, escala, grande-rollback, claude-code, agents-md, agentes-ia]
skill: tech-mentor-backend
status: stub
---

# Shopify

Plataforma de e-commerce que hospeda ~14% das lojas online americanas. Em 2025, redesenhou seu sistema de reserva de estoque, saindo de uma arquitetura híbrida [[wiki/concepts/redis]] + [[wiki/concepts/mysql]] para um modelo 100% MySQL usando [[wiki/concepts/skip-locked]], onde cada unidade de estoque é uma linha física na tabela em vez de um contador numa coluna.

## Escala Citada

Na Black Friday de 2025, a Shopify processou vendas na ordem de **US$ 5,1 milhões por minuto**. O redesenho de estoque reduziu leituras em 50% e transações em 33%, mantendo a CPU do banco abaixo de 50% nos picos.

## CEO Técnico e Adoção Agressiva de Agentes de IA

Segundo [[wiki/sources/guia-claude-code-para-startups-anthropic-ai-native-sdlc]], a Shopify foi uma das primeiras empresas a adotar agentes de IA pesadamente dentro da operação, com contrato firmado com a [[wiki/entities/openai]] antes da adoção em massa de agentes em outras corporações. Seu CEO, [[wiki/entities/tobi-lutke|Tobi Lütke]], é citado como exemplo de fundador com background técnico forte que faz *commits* diretos em produção — contraponto ao risco de CEOs não técnicos fazendo o mesmo (ver [[wiki/concepts/everyone-ships]]).

## Controvérsia AGENTS.md vs. CLAUDE.md

Tobi Lütke declarou publicamente estar considerando banir o [[wiki/entities/claude-code|Claude Code]] dentro da Shopify até a [[wiki/entities/anthropic]] passar a suportar o formato compartilhado `AGENTS.md`. Ver detalhamento e nota de verificação em [[wiki/concepts/agents-md-vs-claude-md]].

## Ver Também

- [[wiki/concepts/grande-rollback]] — a Shopify como um dos casos citados dessa tendência
- [[wiki/entities/37signals]] — referenciada como precedente/inspiração no artigo técnico da Shopify
- [[wiki/concepts/agents-md-vs-claude-md]] — controvérsia pública sobre configuração de agentes

## Key Sources

- [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]]
- [[wiki/sources/guia-claude-code-para-startups-anthropic-ai-native-sdlc]] — CEO técnico shipando código, contrato antecipado com OpenAI, controvérsia AGENTS.md
