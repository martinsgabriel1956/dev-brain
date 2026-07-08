---
type: entity
title: "Shopify"
aliases: ["shopify inc"]
date_created: 2026-07-07
date_updated: 2026-07-07
source_count: 1
tags: [e-commerce, mysql, redis, skip-locked, escala, grande-rollback]
skill: tech-mentor-backend
status: stub
---

# Shopify

Plataforma de e-commerce que hospeda ~14% das lojas online americanas. Em 2025, redesenhou seu sistema de reserva de estoque, saindo de uma arquitetura híbrida [[wiki/concepts/redis]] + [[wiki/concepts/mysql]] para um modelo 100% MySQL usando [[wiki/concepts/skip-locked]], onde cada unidade de estoque é uma linha física na tabela em vez de um contador numa coluna.

## Escala Citada

Na Black Friday de 2025, a Shopify processou vendas na ordem de **US$ 5,1 milhões por minuto**. O redesenho de estoque reduziu leituras em 50% e transações em 33%, mantendo a CPU do banco abaixo de 50% nos picos.

## Ver Também

- [[wiki/concepts/grande-rollback]] — a Shopify como um dos casos citados dessa tendência
- [[wiki/entities/37signals]] — referenciada como precedente/inspiração no artigo técnico da Shopify

## Key Sources

- [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]]
