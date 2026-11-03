---
type: concept
title: "Strategy com Adapter"
aliases: ["strategy + adapter", "combinação strategy e adapter", "provedor atrás de adaptador"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_count: 1
tags: [design-patterns, strategy, adapter, pagamentos, desacoplamento, integracao]
skill: tech-mentor-backend
status: stub
---

# Strategy com Adapter

Combinação de dois padrões que se parecem, mas respondem a perguntas diferentes:

- **[[wiki/concepts/strategy-pattern|Strategy]] — qual caminho usar?** Decide o provedor em tempo de execução.
- **[[wiki/concepts/adapter-pattern|Adapter]] — como falar com ele?** Traduz a interface do provedor para a que o código espera.

## Exemplo

No fluxo de pagamento de [[wiki/sources/cinco-design-patterns-strategy-observer-adapter-state-machine-retry-circuit-breaker]], a estratégia escolhe pelo meio de pagamento: cartão vai para [[wiki/entities/stripe|Stripe]], e Pix vai para AbacatePay. Cada provedor fica atrás de um adaptador, e o SDK só é chamado no último momento possível.

```
fluxo de pagamento
  └─ strategy (cartão ou Pix)
       ├─ StripeAdapter      → SDK da Stripe
       └─ AbacatePayAdapter  → SDK da AbacatePay
```

Para trocar um provedor, basta remover o SDK e criar outro adaptador. O restante da aplicação não muda.

## Custo

A fonte não trata do custo. Pela wiki, são duas camadas de indireção. Com um único provedor sem troca prevista, o Adapter pode bastar, e a estratégia só se paga a partir da segunda variação (inferência; ver [[wiki/concepts/yagni]]).

## Relação com outros conceitos

- [[wiki/concepts/ports-adapters]] aplica a mesma separação no nível da arquitetura.
- [[wiki/sources/extrair-melhor-codigo-de-agentes-ia-planejamento-plan-mode-skills]] traz um caso próximo: `PaymentStrategy` com tipos agnósticos, sem importar o SDK diretamente, para Stripe e Abacate Pay.

## Key Sources

- [[wiki/sources/cinco-design-patterns-strategy-observer-adapter-state-machine-retry-circuit-breaker]]
