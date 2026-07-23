---
type: concept
title: "Reinventar a Roda"
aliases: ["not invented here", "reinventing the wheel", "nih syndrome"]
date_created: 2026-07-23
date_updated: 2026-07-23
source_count: 1
tags: [arquitetura, build-vs-buy, manutencao, ferramentas, anti-pattern]
skill: tech-mentor-leadership
status: draft
---

# Reinventar a Roda

Criar uma solução do zero para um problema que já tem soluções maduras, testadas e documentadas disponíveis — geralmente motivado por preferência estética/de convenção (ex.: "eles usam camelCase, eu prefiro snake_case") em vez de uma lacuna funcional real.

## O Argumento Central

O que costuma ser percebido como inovação, na maior parte das vezes, é remix de ideias já existentes — não invenção genuína. O custo real de reinventar a roda não está no esforço inicial de criação, está na **manutenção**: bugs próprios para corrigir, documentação própria para escrever, e a ausência de um time dedicado (que soluções maduras de mercado costumam ter) para manter tudo atualizado.

[[wiki/entities/pedro-nauke]] usa a analogia de tentar "reinventar um novo tipo de pizza" — pode-se trocar os toppings, mas a base continua sendo pizza.

## Quando a Inovação Vale a Pena

O ponto não é nunca construir nada — é direcionar o esforço de inovação para onde ele realmente conta: o problema de negócio específico da empresa, não para recriar uma peça de infraestrutura genérica (ex.: mais uma biblioteca de gerenciamento de estado em React) que o mercado já resolveu de forma madura.

## Relação com Outros Conceitos

- [[wiki/concepts/over-engineering]] — reinventar a roda é frequentemente um vetor de over-engineering: complexidade extra assumida sem necessidade comprovada
- [[wiki/concepts/apego-a-ferramentas]] — fenômeno relacionado mas inverso: apego a ferramentas é resistência a *trocar* de ferramenta; reinventar a roda é resistência a *adotar* uma ferramenta madura desde o início

## Key Sources

- [[wiki/sources/verdades-duras-programador-20-anos-pedro-nauck]]
