---
type: concept
title: "Singleton Pattern"
aliases: ["singleton"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 1
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

- Pool de conexões com banco de dados
- Logger centralizado
- Cache compartilhado em processo único

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
