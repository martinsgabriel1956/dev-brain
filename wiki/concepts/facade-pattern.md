---
type: concept
title: "Facade Pattern"
aliases: ["padrão facade", "design pattern facade", "fachada"]
date_created: 2026-05-01
date_updated: 2026-07-27
source_count: 3
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

## Facade e o "S" do SOLID

Crítica comum: uma Facade que orquestra pagamento, notificação e estoque parece ferir a responsabilidade única. Contra-argumento (via [[wiki/sources/design-pattern-facade-renato-augusto]]): SRP é sobre ter **um único motivo para mudar**, não sobre "uma linha de código, uma ação". A razão de mudança da Facade é *o processo que ela orquestra* mudar (ex: adicionar um passo novo) — as classes internas que ela chama continuam com SRP estrito cada uma. O sintoma de que isso descamba para [[god-object]] é a Facade acumular responsabilidades **não relacionadas** ao fluxo que ela representa, não o fato de chamar várias classes.

### Sinal prático para extrair uma Facade

Quando o mesmo fluxo de orquestração (ex: processar um pedido) precisa ser repetido em mais de um Controller/rota, deixar a lógica solta em cada Controller cria risco de divergência — uma mudança de regra aplicada em um lugar e esquecida no outro. Esse é o gatilho concreto para migrar o fluxo para dentro de uma Facade: um único ponto de mudança.

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
- [[wiki/sources/design-pattern-facade-renato-augusto]]
