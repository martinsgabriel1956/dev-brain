---
type: concept
title: "Chain of Responsibility Pattern"
aliases: ["chain of responsibility", "corrente de responsabilidade", "middleware pattern"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 1
tags: [design-patterns, behavioral, chain-of-responsibility, gof, middleware]
skill: tech-mentor-backend
status: stub
---

# Chain of Responsibility Pattern

Padrão [[behavioral-patterns|comportamental]] que passa um pedido por uma **corrente dinâmica de handlers** até que um deles o processe. Cada handler decide processar o pedido ou passá-lo para o próximo na corrente.

## Mecanismo

```
Request → Handler A → Handler B → Handler C → (fim)
               ↓           ↓           ↓
           processa?   processa?   processa?
```

Cada handler tem referência para o próximo. Pode processar e parar, ou delegar para o próximo sem processar.

## Exemplo real — Middleware HTTP

A base do padrão de middleware em Express, Fastify, Koa:

```typescript
app.use(authMiddleware)       // verifica autenticação
app.use(rateLimitMiddleware)  // verifica rate limit
app.use(validationMiddleware) // valida body
app.use(routeHandler)        // processa a requisição
```

Cada middleware chama `next()` para passar adiante ou responde diretamente para interromper a corrente.

## Distinção do Observer

| | Chain of Responsibility | [[observer-pattern]] |
|---|---|---|
| Fluxo | Sequencial — um handler por vez | Broadcast — todos notificados |
| Quem processa? | Geralmente apenas um | Todos os assinantes |
| Pode parar? | Sim — handler interrompe a corrente | Não — todos são notificados |

## Quando usar

- Quando mais de um objeto pode tratar um pedido e o handler não é conhecido a priori
- Quando quer emitir um pedido para vários handlers sem especificar o receptor
- Pipelines de processamento (middlewares, filtros, validações)

## Key Sources

- [[sources/design-pattern-observer]] — mencionado nas relações com outros padrões
