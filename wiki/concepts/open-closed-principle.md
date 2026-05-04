---
type: concept
title: "Open/Closed Principle (OCP)"
aliases: ["OCP", "open closed principle", "aberto fechado"]
date_created: 2026-05-01
date_updated: 2026-05-01
source_count: 1
tags: [solid, oop, architecture]
skill: tech-mentor-backend
status: stub
---

## Definição

Classes devem estar **abertas para extensão** e **fechadas para modificação**. Adicionar comportamento novo não deve exigir alterar código que já funciona em produção.

## Relação com Proxy

O [[proxy-pattern]] é uma aplicação direta do OCP: ao invés de modificar `ReportGenerator` para adicionar cache, cria-se `ReportGeneratorProxy` — o original não é tocado.

## Key Sources

- [[wiki/sources/design-pattern-proxy]]
