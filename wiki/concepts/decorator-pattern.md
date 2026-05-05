---
type: concept
title: "Decorator Pattern"
aliases: ["padrão decorator", "design pattern decorator"]
date_created: 2026-05-01
date_updated: 2026-05-01
source_count: 1
tags: [design-patterns, structural, decorator, oop]
skill: tech-mentor-backend
status: stub
---

## Definição

Padrão estrutural que adiciona comportamento a objetos em cadeia (wrapping recursivo), sem alterar a classe original. Foco em extensão funcional.

## Diferença do Proxy

| | Decorator | Proxy |
|---|---|---|
| Motivação | Extensão de comportamento em cadeia | Controle de acesso / interceptação |
| Instanciação | Recebe o objeto decorado externamente | Geralmente cria/recebe o objeto real internamente |
| Quantidade de wrappers | Múltiplos encadeados | Normalmente um único interceptador |

Ambos encapsulam um objeto e implementam a mesma interface — a diferença está na **intenção**.

## Key Sources

- [[wiki/sources/design-pattern-proxy]]
- [[sources/design-pattern-strategy]] — distinção Decorator (pele) vs Strategy (miolo/algoritmo)
