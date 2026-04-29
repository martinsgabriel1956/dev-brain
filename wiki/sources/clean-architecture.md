---
type: source
title: "Clean Architecture"
aliases: ["clean architecture", "dependency rule", "use cases", "ports and adapters"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/clean-architecture.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [clean-architecture, dependency-rule, use-cases, ports-adapters, inversao-de-controle, camadas]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Clean Architecture organiza código em camadas concêntricas onde dependências só apontam para dentro (Dependency Rule). 4 camadas: Domain (entities), Application (use cases), Interface Adapters (controllers, presenters), Frameworks (DB, web, UI). Use Cases dependem de interfaces — implementações concretas são injetadas na composição (Main).

## Key Claims

**Claim:** A Dependency Rule é a única regra não negociável — dependências só apontam para dentro.
**Evidence:** Domain não conhece Application. Application não conhece Frameworks. Frameworks podem conhecer tudo. Violar essa regra = acoplar lógica de negócio a detalhes de implementação (DB, framework web) — impossível trocar sem reescrever.
**Confidence:** alta

**Claim:** Use Cases são o coração da arquitetura — contêm as regras de negócio da aplicação.
**Evidence:** Um Use Case orquestra entities do domain para executar um caso de uso específico. Não conhece HTTP, DB, frameworks. Recebe/retorna DTOs. Testável em isolamento com mocks de repositórios.
**Confidence:** alta

**Claim:** Ports são interfaces no Application; Adapters são implementações nos Frameworks.
**Evidence:** `OrderRepository` (port/interface) definido em Application. `PrismaOrderRepository` (adapter) implementado em Frameworks. Main injeta o adapter no use case. Trocar PostgreSQL por MongoDB = trocar o adapter, sem tocar no use case.
**Confidence:** alta

**Claim:** Clean Architecture é over-engineering para CRUDs simples — vale para domínios complexos.
**Evidence:** Se a lógica é basicamente "salvar e listar", as camadas adicionam burocracia sem benefício. O valor aparece quando as regras de negócio são complexas, mudam frequentemente, ou precisam ser testadas em isolamento.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/clean-architecture]]
- [[concepts/dependency-rule]]
- [[concepts/use-cases]]
- [[concepts/ports-adapters]]
- [[concepts/dependency-injection]]
- [[concepts/hexagonal-architecture]]

## Open Questions

- Como aplicar Clean Architecture em Next.js App Router onde Server Components cruzam as camadas?
- Qual o critério de "domínio complexo suficiente" para justificar Clean Architecture vs CRUD simples?
