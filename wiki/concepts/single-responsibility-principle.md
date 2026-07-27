---
type: concept
title: "Single Responsibility Principle (SRP)"
aliases: ["SRP", "single responsibility", "responsabilidade única"]
date_created: 2026-05-01
date_updated: 2026-07-27
source_count: 2
tags: [solid, oop, architecture]
skill: tech-mentor-backend
status: stub
---

## Definição

Uma classe deve ter apenas uma razão para mudar — ou seja, uma única responsabilidade.

## Relação com Proxy

No exemplo do [[proxy-pattern]]: o Controller não deve carregar lógica de cache (sua responsabilidade é orquestrar a requisição HTTP). A classe `ReportGenerator` não deve carregar lógica de cache (sua responsabilidade é gerar relatórios). O proxy assume a responsabilidade de cache isoladamente.

## "Razão para mudar" vs. "faz só uma coisa"

Via [[wiki/sources/design-pattern-facade-renato-augusto]]: SRP é frequentemente mal interpretado como "cada trecho de código deve fazer literalmente uma única ação". A formulação correta é sobre **motivo único de mudança**. Uma [[facade-pattern|Facade]] que orquestra pagamento, notificação e estoque num pedido não fere SRP se o único motivo dela mudar for o *processo de pedido* mudar — mesmo orquestrando múltiplas chamadas, ela opera num nível de abstração diferente das classes que chama, cada uma delas com SRP estrito.

## Key Sources

- [[wiki/sources/design-pattern-proxy]]
- [[wiki/sources/design-pattern-facade-renato-augusto]]
