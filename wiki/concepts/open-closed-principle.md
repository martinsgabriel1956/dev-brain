---
type: concept
title: "Open/Closed Principle (OCP)"
aliases: ["OCP", "open closed principle", "aberto fechado", "open-closed"]
date_created: 2026-05-01
date_updated: 2026-08-18
source_count: 5
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

## Exemplo — Processador de Pagamentos

Via [[wiki/sources/principios-solid-ilustrados]]: um `processarPagamento` que valida e cobra cartão de crédito também funciona para débito (campos parecidos). Ao chegar boleto (campos diferentes, sem antifraude convencional), a saída errada é abrir a classe base e adicionar um `if` — cada novo método de pagamento voltaria a exigir mexer nela. A correção é a classe base não conhecer os campos específicos de cada produto: ela só recebe um objeto de pagamento e pede para ele se validar e se cobrar, via interface comum. O mesmo raciocínio se aplica a um ORM: os métodos genéricos (salvar, atualizar, deletar) não mudam ao adicionar suporte a um novo banco.

## Exemplo negativo — Facade que depende de implementações concretas

[[wiki/sources/design-pattern-facade-codigo-fonte-tv]] mostra o lado inverso do OCP funcionando: um `ClientFacade` que depende de classes concretas de serviço (`AvatarService`, `DocumentService`) em vez de interfaces quebra OCP porque adicionar um novo canal (ex.: enviar SMS além de e-mail) exige abrir e modificar o método existente — cada novo requisito é mais uma linha inserida direto no fluxo, em vez de uma extensão isolada.

## Definição Formal (Fonte Primária)

Via [[wiki/sources/solid-principles-in-pictures-ugonna-thelma]]: "classes devem estar abertas para extensão, mas fechadas para modificação" — modificar o comportamento de uma classe já existente impacta todo sistema que depende dela; estender com métodos novos evita quebrar quem já a usa.

## Key Sources

- [[wiki/sources/design-pattern-proxy]]
- [[sources/sete-padroes-de-design-de-software]]
- [[sources/design-pattern-strategy]]
- [[wiki/sources/principios-solid-ilustrados]]
- [[wiki/sources/solid-principles-in-pictures-ugonna-thelma]]
- [[wiki/sources/design-pattern-decorator-renato-augusto]] — OCP como justificativa direta do [[wiki/concepts/decorator-pattern|Decorator]]: estender por wrapping em vez de modificar a classe em produção
- [[wiki/sources/design-pattern-facade-codigo-fonte-tv]] — exemplo negativo: Facade acoplada a implementações concretas quebra OCP ao adicionar um canal novo (SMS)
