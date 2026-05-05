---
type: concept
title: "Facade Pattern"
aliases: ["padrão facade", "design pattern facade", "fachada"]
date_created: 2026-05-01
date_updated: 2026-05-05
source_count: 2
tags: [design-patterns, structural, facade, oop, encapsulamento]
skill: tech-mentor-backend
status: stable
---

# Facade Pattern

Padrão [[structural-patterns|estrutural]] que fornece uma **interface simplificada** para um conjunto de interfaces em um subsistema complexo. O cliente fala com a Facade; ela coordena os componentes internos.

## Como funciona

```typescript
class OrderFacade {
  private paymentProcessor = new PaymentProcessor();
  private inventorySystem = new InventorySystem();
  private fraudChecker = new FraudChecker();
  private shippingCalculator = new ShippingCalculator();

  placeOrder(order: Order) {
    if (!this.fraudChecker.check(order)) return;
    if (!this.inventorySystem.hasStock(order)) return;
    if (!this.paymentProcessor.charge(order)) return;
    this.shippingCalculator.calculate(order);
  }
}

// Uso: complexidade zero para o consumidor
const facade = new OrderFacade();
facade.placeOrder(order);
```

## Quando usar

- Subsistemas complexos com muitos passos de orquestração
- Para reduzir acoplamento entre camadas
- Para criar uma API de alto nível sobre libs ou módulos de baixo nível

## Trade-offs

| ✅ | ❌ |
|---|---|
| Simplicidade para o consumidor | Pode virar [[god-object]] se fizer demais |
| Reduz acoplamento | Pode esconder complexidade que deveria ser visível |
| Ponto único de mudança para a orquestração | |

## Diferença do Proxy

O Facade simplifica acesso a **múltiplos** componentes. O [[proxy-pattern]] substitui **um único** objeto e controla o acesso a ele.

## Façades implícitas no dia a dia

- `fetch()` — esconde TCP, retry, header parsing
- `ArrayList` Java — esconde resize de array
- Qualquer ORM — esconde SQL gerado

## Key Sources

- [[wiki/sources/design-pattern-proxy]]
- [[sources/sete-padroes-de-design-de-software]]
- [[sources/design-pattern-facade]]
