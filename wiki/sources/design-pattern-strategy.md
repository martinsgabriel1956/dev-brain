---
type: source
title: "Strategy — Padrão de Projeto Comportamental (Refactoring Guru)"
aliases: ["refactoring guru strategy", "strategy pattern guru"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 0
tags: [design-patterns, behavioral, strategy, gof, algoritmos, composicao]
skill: tech-mentor-backend
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/design-pattern-strategy.md
source_url: https://refactoring.guru/pt-br/design-patterns/strategy
author: "Refactoring Guru"
date_published: ""
date_ingested: 2026-05-05
---

# Strategy — Padrão de Projeto Comportamental (Refactoring Guru)

Artigo canônico do Refactoring Guru sobre o padrão Strategy. Fonte primária com estrutura, pseudocódigo, aplicabilidade, prós/contras e relações com outros padrões.

## TL;DR

[[strategy-pattern]] extrai variantes de um algoritmo para classes separadas (estratégias) com uma interface comum. O contexto delega para a estratégia sem saber qual está usando. O cliente escolhe e troca a estratégia em tempo de execução. Aplica diretamente o [[open-closed-principle]]: novos algoritmos = novas classes, contexto intocado.

## Key Claims

| Claim | Evidence | Confidence |
|---|---|---|
| Strategy elimina condicionais gigantes | "O padrão Strategy permite que você se livre dessa condicional ao extrair todos os algoritmos para classes separadas" | Alto |
| Contexto não sabe qual estratégia usa | "O contexto não sabe qual tipo de estratégia ele está trabalhando ou como o algoritmo é executado" | Alto |
| Strategy usa composição, não herança | Contexto tem referência à interface; algoritmo é injetado. Contraste com Template Method (herança) | Alto |
| Clientes devem conhecer as estratégias | "Os Clientes devem estar cientes das diferenças entre as estratégias para serem capazes de selecionar a adequada" | Alto |
| Funções anônimas podem substituir Strategy | "Linguagens modernas têm suporte funcional que permite implementar versões de algoritmo em funções anônimas" | Médio |

## Estrutura

```
Cliente → setStrategy(ConcreteStrategy) → Contexto → Strategy.execute()
                                                           ▲
                                              ConcreteA  ConcreteB  (...)
```

**Participantes:**
- **Contexto** — mantém referência à estratégia, delega via interface, expõe setter
- **Interface Estratégia** — contrato único: método `execute`
- **Estratégias Concretas** — cada variante do algoritmo em sua própria classe
- **Cliente** — cria e injeta a estratégia; pode trocar durante execução

## Pseudocódigo Central

```
interface Strategy is
    method execute(a, b)

class ConcreteStrategyAdd implements Strategy is
    method execute(a, b) is return a + b

class ConcreteStrategyMultiply implements Strategy is
    method execute(a, b) is return a * b

class Context is
    private strategy: Strategy
    method setStrategy(s: Strategy) is this.strategy = s
    method executeStrategy(a, b) is return strategy.execute(a, b)

// Uso — troca em runtime
context.setStrategy(new ConcreteStrategyAdd())
context.executeStrategy(3, 4)       // 7

context.setStrategy(new ConcreteStrategyMultiply())
context.executeStrategy(3, 4)       // 12
```

## Aplicabilidade (4 casos)

1. Trocar variantes de algoritmo durante a execução
2. Muitas classes parecidas que diferem só no comportamento → extrair para hierarquia separada
3. Isolar lógica de negócio dos detalhes de implementação do algoritmo
4. Condicional enorme selecionando variantes do mesmo algoritmo → cada ramo vira uma estratégia

## Relações com Outros Padrões

- [[command-pattern]] — ambos parametrizam com ação; Command = operação como objeto (undo/queue/remote); Strategy = variantes do mesmo algoritmo
- [[template-method-pattern]] — mesmo propósito, mecanismo oposto: Template Method usa herança (estático), Strategy usa composição (dinâmico/runtime)
- [[state-pattern]] — estrutura similar; diferença de intenção: State gerencia transições automáticas entre estados; Strategy é trocada explicitamente pelo cliente
- [[decorator-pattern]] — Decorator muda a *pele* (adiciona camadas); Strategy muda o *miolo* (substitui algoritmo inteiro)
- [[bridge-pattern]] / [[adapter-pattern]] — estrutura parecida (composição), propósito diferente

## Questões em Aberto

- Em TypeScript/JavaScript, funções de primeira classe eliminam a necessidade das classes ConcreteStrategy — quando vale usar classes vs funções?
- Como testar um Contexto quando a estratégia tem efeitos colaterais (I/O, rede)?
