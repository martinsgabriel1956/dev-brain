---
type: concept
title: "Singleton Pattern"
aliases: ["singleton"]
date_created: 2026-05-05
date_updated: 2026-08-03
source_count: 4
tags: [design-patterns, creational, singleton, gof]
skill: tech-mentor-backend
status: stable
---

# Singleton Pattern

Padrão [[creational-patterns|criacional]] que garante que uma classe tenha **apenas uma instância** e fornece um ponto de acesso global a ela.

## Como funciona

```typescript
class Logger {
  private static instance: Logger;

  private constructor() {}

  static getInstance(): Logger {
    if (!Logger.instance) {
      Logger.instance = new Logger();
    }
    return Logger.instance;
  }

  log(message: string) { console.log({ message }); }
}

const logger1 = Logger.getInstance();
const logger2 = Logger.getInstance();
// logger1 === logger2 — mesma instância
```

## Quando usar

- Pool de conexões com banco de dados — em Node.js, o cache de módulo (`require`/`import`) já entrega esse comportamento "de graça": instanciar a pool fora do handler de rota, no nível do módulo, garante uma única instância reutilizada por todos os requests. Ver [[wiki/concepts/connection-pooling]] e [[wiki/sources/connection-pooling-pool-vs-polling-serverless]]
- Logger centralizado
- Cache compartilhado em processo único
- Conexão com [[wiki/concepts/redis]] em Pub/Sub — sem Singleton, cada requisição SSE/WebSocket que chega abriria sua própria conexão Redis, derrubando o Redis em escala. O Redis multiplexa uma única conexão entre muitos assinantes; ver [[wiki/concepts/server-sent-events]]
- Estado global no front end — uma store [[wiki/concepts/zustand|estilo Zustand]] é, na prática, um singleton de módulo: criada uma vez fora da árvore do React, importada e compartilhada por todos os componentes que a usam, sem precisar de `Provider`. Ver [[wiki/sources/recriando-zustand-javascript-puro-sem-provider]]

## Trade-offs

| ✅ | ❌ |
|---|---|
| Instância única garantida | Difícil de testar (mock complexo) |
| Acesso global | Multi-thread exige double-checked locking |
| | É uma variável global glorificada |

## Alerta

> "A Singleton is basically just a glorified global variable." — [[sources/sete-padroes-de-design-de-software]]

Use quando a unicidade é **genuinamente necessária**, não para ter estado global conveniente. Prefira injeção de dependência para passar instâncias compartilhadas.

## Key Sources

- [[sources/sete-padroes-de-design-de-software]]
- [[sources/design-pattern-facade]] — Facade frequentemente convertida em Singleton
- [[wiki/sources/server-sent-events-sse-tempo-real]] — conexão Redis compartilhada em arquitetura SSE/Pub-Sub
- [[wiki/sources/connection-pooling-pool-vs-polling-serverless]] — pool de conexões como singleton de módulo em Node.js
- [[wiki/sources/recriando-zustand-javascript-puro-sem-provider]] — store de estado global (estilo Zustand) como singleton de módulo no front end
