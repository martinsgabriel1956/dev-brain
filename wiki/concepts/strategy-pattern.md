---
type: concept
title: "Strategy Pattern"
aliases: ["strategy", "padrão estratégia"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 1
tags: [design-patterns, behavioral, strategy, gof, open-closed, polimorfismo]
skill: tech-mentor-backend
status: stable
---

# Strategy Pattern

Padrão [[behavioral-patterns|comportamental]] que define uma **família de algoritmos**, encapsula cada um em sua própria classe e os torna intercambiáveis. Elimina `if/else` crescente para variações do mesmo comportamento.

## Como funciona

```typescript
interface TransportStrategy {
  execute(): void;
}

class CarStrategy implements TransportStrategy {
  execute() { /* lógica de carro */ }
}

class BusStrategy implements TransportStrategy {
  execute() { /* lógica de ônibus */ }
}

class BikeStrategy implements TransportStrategy {
  execute() { /* lógica de bicicleta */ }
}

class Commuter {
  private strategy: TransportStrategy;

  setStrategy(strategy: TransportStrategy) {
    this.strategy = strategy;
  }

  goToWork() {
    this.strategy.execute();
  }
}

const commuter = new Commuter();
commuter.setStrategy(new CarStrategy());
commuter.goToWork();

// Trocar estratégia sem mudar Commuter
commuter.setStrategy(new BikeStrategy());
commuter.goToWork();
```

## Quando usar

- Múltiplas formas de fazer a mesma coisa (pricing, sorting, notificação, pagamento, transporte)
- `if/else` ou `switch` cresce a cada nova variação
- Quando quer adicionar comportamentos sem modificar código existente

## Relação com princípios

Implementação direta do [[open-closed-principle]]: a classe `Commuter` está fechada para modificação, mas aberta para extensão — basta criar uma nova `Strategy`.

## Trade-offs

| ✅ | ❌ |
|---|---|
| Elimina if/else aninhado | Mais classes (uma por estratégia) |
| Extensível sem modificar código existente | Cliente precisa conhecer as estratégias disponíveis |
| Testável isoladamente por estratégia | |

## Exemplos reais

- Estratégias de pricing (regular, premium, promo) — [[sources/sete-padroes-de-design-de-software]]
- Algoritmos de sorting intercambiáveis
- Gateways de pagamento (Stripe, PayPal, Mercado Pago)
- Estratégias de notificação (push, email, SMS)

## Key Sources

- [[sources/sete-padroes-de-design-de-software]]
- [[sources/design-pattern-strategy]]
