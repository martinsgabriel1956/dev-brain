---
type: concept
title: "Open/Closed Principle (OCP)"
aliases: ["OCP", "open closed principle", "aberto fechado", "open-closed"]
date_created: 2026-05-01
date_updated: 2026-05-05
source_count: 2
tags: [solid, oop, architecture, design-patterns]
skill: tech-mentor-backend
status: stable
---

# Open/Closed Principle (OCP)

Um dos cinco princípios [[solid]]. Entidades de software devem ser **abertas para extensão** e **fechadas para modificação** — adicionar comportamento novo não deve exigir alterar código que já funciona em produção.

## Exemplo — Strategy como aplicação direta

```typescript
// ANTES: adicionar "bike" = modificar Commuter ❌
class Commuter {
  goToWork(transport: string) {
    if (transport === "car") { ... }
    else if (transport === "bus") { ... }
  }
}

// DEPOIS: adicionar "bike" = nova classe, Commuter intocado ✅
interface TransportStrategy { execute(): void; }
class CarStrategy implements TransportStrategy { execute() { ... } }
class BikeStrategy implements TransportStrategy { execute() { ... } } // extensão pura

class Commuter {
  setStrategy(s: TransportStrategy) { this.strategy = s; }
  goToWork() { this.strategy.execute(); }
}
```

## Aplicações no dia a dia

- [[strategy-pattern]] — nova estratégia = nova classe, código cliente intocado
- [[proxy-pattern]] — `ReportGeneratorProxy` adiciona cache sem modificar `ReportGenerator`
- [[factory-pattern]] — novos tipos adicionados na factory sem mudar código cliente

## Limitações

OCP não é absoluto. Aplique nas **dimensões de variação real** do sistema, não em toda abstração possível. Abstração prematura tem custo real de complexidade.

## Key Sources

- [[wiki/sources/design-pattern-proxy]]
- [[sources/sete-padroes-de-design-de-software]]
- [[sources/design-pattern-strategy]]
