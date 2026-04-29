---
type: source
title: "Dependency Injection"
aliases: ["dependency injection", "di", "ioc", "inversion of control", "tsyringe"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/dependency-injection.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [dependency-injection, ioc, constructor-injection, di-container, tsyringe, nestjs, testabilidade]
skill: tech-mentor-backend
status: stable
---

## TL;DR

DI é o padrão de fornecer dependências externamente em vez de instanciá-las internamente. Constructor injection é o padrão preferido — dependências explícitas, testabilidade direta com mocks. DI Container (tsyringe, NestJS) automatiza o wiring em projetos grandes. Sem DI: acoplamento hard-coded, testes que precisam de infra real.

## Key Claims

**Claim:** Constructor injection é o tipo preferido — dependências explícitas na assinatura.
**Evidence:** Dependências visíveis na assinatura do constructor. Impossível instanciar a classe sem fornecer todas. Testes: passa mock no construtor, sem precisar de container. Property injection e method injection escondem dependências, dificultando testes.
**Confidence:** alta

**Claim:** DI Container só faz sentido quando o wiring manual vira overhead — projetos grandes.
**Evidence:** 5 classes: wiring manual é mais claro que container. 50 classes com dependências nested: container compensa. Container adiciona magia implícita — mais difícil de debugar quando algo é injetado errado.
**Confidence:** alta

**Claim:** DI é o enabler de testabilidade — sem ele, testar em isolamento requer infra real.
**Evidence:** Classe que instancia `new PrismaOrderRepository()` internamente = impossível testar sem banco. Com DI: passa `FakeOrderRepository` no teste. Testa a lógica do use case sem IO.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/dependency-injection]]
- [[concepts/ioc]]
- [[concepts/testabilidade]]
- [[concepts/clean-architecture]]
- [[concepts/hexagonal-architecture]]

## Open Questions

- Como testar código que usa DI Container (tsyringe/NestJS) sem inicializar o container inteiro?
- Property injection tem casos de uso legítimos? Quais?
