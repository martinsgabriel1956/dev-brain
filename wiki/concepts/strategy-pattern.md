---
type: concept
title: "Strategy Pattern"
aliases: ["strategy", "padrão estratégia"]
date_created: 2026-05-05
date_updated: 2026-11-03
source_count: 8
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

## Parente mais leve: Pluggable (Method) Selector

[[wiki/sources/pluggable-behavior-xunitpatterns]] descreve o **Pluggable (Method) Selector**, uma variação do padrão [[wiki/concepts/pluggable-behavior|Pluggable Behavior]] (Kent Beck, *Smalltalk Best Practice Patterns*) com a mesma motivação do Strategy — evitar `if/else`/subclasses ao variar comportamento — mas mais leve: em vez de um objeto Strategy completo trocável por composição, basta guardar o **nome** de um método já existente na classe e resolvê-lo por reflection em runtime. É o mecanismo usado pelo [[wiki/concepts/testcase-object|Testcase Object]] do xUnit para despachar o [[wiki/concepts/test-method|Test Method]] correto.

## Trade-offs

| ✅ | ❌ |
|---|---|
| Elimina if/else aninhado | Mais classes (uma por estratégia) |
| Extensível sem modificar código existente | Cliente precisa conhecer as estratégias disponíveis |
| Testável isoladamente por estratégia | |

## Exemplos reais

- Estratégias de pricing (regular, premium, promo) — [[wiki/sources/sete-padroes-de-design-de-software]]
- Algoritmos de sorting intercambiáveis
- Gateways de pagamento (Stripe, PayPal, Mercado Pago)
- Estratégias de notificação (push, email, SMS)
- Validação de formulário por campo — cada regra (CPF, telefone, senha) vira uma strategy que o validador usa, em vez de um `if/else` gigante — [[wiki/sources/seis-design-patterns-mais-usados-na-pratica]]

## Testar sem efeito colateral e combinar com Adapter

[[wiki/sources/cinco-design-patterns-strategy-observer-adapter-state-machine-retry-circuit-breaker]] destaca um ganho além de trocar de algoritmo: cada estratégia pode ser instanciada com a dependência injetada e testada sozinha, sem mandar e-mail de verdade a um cliente (ver [[wiki/concepts/efeito-colateral]] e [[wiki/concepts/dependency-injection]]). A fonte também admite que `if/elif` funciona no início; o problema aparece quando as variações crescem. Para pagamentos, a estratégia escolhe o provedor e um Adapter esconde o SDK: [[wiki/concepts/strategy-com-adapter]].

## Key Sources

- [[wiki/sources/sete-padroes-de-design-de-software]]
- [[wiki/sources/design-pattern-strategy]]
- [[wiki/sources/principios-solid-ilustrados]] — mesma solução (objeto injetado que se auto-valida/processa) aplicada ao exemplo de processador de pagamentos
- [[wiki/sources/seis-design-patterns-mais-usados-na-pratica]] — analogia das opções de rota do GPS; exemplo de validação de formulário por campo (CPF, telefone, senha); regra prática de quando usar classe (estado/múltiplos métodos) vs. função isolada (operação simples)
- [[wiki/sources/extrair-melhor-codigo-de-agentes-ia-planejamento-plan-mode-skills]] — Strategy aplicado a múltiplos gateways de pagamento (Stripe, Abacate Pay) por uma IA em modo plan: interface `PaymentStrategy` com tipos agnósticos (sem importar SDK direto), payment context que carrega a strategy correspondente por rota — inclui a motivação de tolerância a falhas (trocar de provedor se um cair)
- [[wiki/sources/pluggable-behavior-xunitpatterns]] — Pluggable (Method) Selector (Kent Beck, SBPP), variação mais leve com a mesma motivação: nome de método + reflection em vez de objeto Strategy completo
- [[wiki/sources/o-que-diferencia-pleno-de-junior-decisoes-legibilidade-modelagem]] — regra de desconto por tipo de cliente como candidata a variação (modelagem não mostrada no vídeo)
- [[wiki/sources/cinco-design-patterns-strategy-observer-adapter-state-machine-retry-circuit-breaker]] — notificação por e-mail, SMS e push com método `send`; testabilidade sem efeito colateral; combinação com Adapter
