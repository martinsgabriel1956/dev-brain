---
type: concept
title: "Liskov Substitution Principle (LSP)"
aliases: ["LSP", "liskov", "substituição de liskov"]
date_created: 2026-05-01
date_updated: 2026-05-01
source_count: 1
tags: [solid, oop, architecture]
skill: tech-mentor-backend
status: stub
---

## Definição

Objetos de uma subclasse (ou implementação de interface) devem poder substituir objetos da classe base sem quebrar o comportamento esperado.

## Relação com Proxy

O [[proxy-pattern]] depende do LSP: tanto o proxy quanto a classe real implementam a mesma interface. O código cliente (Controller) pode receber qualquer um dos dois sem saber a diferença — e o comportamento esperado é preservado.

## Key Sources

- [[wiki/sources/design-pattern-proxy]]
