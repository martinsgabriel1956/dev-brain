---
type: source
title: "Design Patterns (GoF) — Os Essenciais"
aliases: ["design patterns", "gof", "factory method", "builder", "adapter", "decorator", "strategy", "observer", "command"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/design-patterns-gof.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [design-patterns, gof, factory-method, builder, adapter, decorator, strategy, observer, command, criacional, estrutural, comportamental]
skill: tech-mentor-backend
status: stable
---

## TL;DR

GoF tem 23 padrões em 3 categorias. Os essenciais para backend: Factory Method (criação sem acoplamento), Builder (objetos complexos), Adapter (interface incompatível), Decorator (comportamento dinâmico), Strategy (algoritmo intercambiável), Observer (event system), Command (encapsular ação como objeto). Patterns são vocabulário, não soluções obrigatórias.

## Key Claims

**Claim:** Strategy permite trocar algoritmos em tempo de execução sem `if/else` em cadeia.
**Evidence:** Interface `PaymentStrategy` com `charge()`. Implementações: `StripeStrategy`, `PayPalStrategy`, `MercadoPagoStrategy`. Controller recebe a estratégia via DI. Adicionar novo provider = nova classe, sem tocar no código existente.
**Confidence:** alta

**Claim:** Decorator adiciona comportamento dinamicamente sem herança — composição sobre herança.
**Evidence:** `Logger` wraps `Repository`, adicionando log sem modificar a implementação original. Decorators são chainable. Mais flexível que herança porque combina comportamentos arbitrariamente em runtime.
**Confidence:** alta

**Claim:** Observer é a base de todos os sistemas de eventos — publish/subscribe em memória.
**Evidence:** EventEmitter do Node.js é Observer. DOM events são Observer. A diferença para EDA: Observer é in-process (síncrono ou assíncrono em memória), EDA usa broker externo.
**Confidence:** alta

**Claim:** Patterns são vocabulário compartilhado — o maior valor é comunicação, não implementação.
**Evidence:** "Vamos usar Strategy aqui" comunica uma decisão de design completa em uma palavra. Sem o vocabulário, seria necessário explicar 3 parágrafos. O padrão em si é secundário ao entendimento compartilhado.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/strategy-pattern]]
- [[concepts/decorator-pattern]]
- [[concepts/observer-pattern]]
- [[concepts/factory-method]]
- [[concepts/command-pattern]]
- [[concepts/adapter-pattern]]
- [[concepts/builder-pattern]]

## Open Questions

- Command Pattern para undo/redo — como implementar em aplicações web com estado distribuído?
- Quando Decorator se torna mais complexo que herança direta? Qual o limite de chain de decorators?
