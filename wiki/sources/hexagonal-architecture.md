---
type: source
title: "Hexagonal Architecture (Ports & Adapters)"
aliases: ["hexagonal architecture", "ports and adapters", "alistair cockburn", "driving ports", "driven ports"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/hexagonal-architecture.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [hexagonal-architecture, ports-adapters, driving-ports, driven-ports, in-memory-adapters, domain-isolation]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Hexagonal Architecture (Alistair Cockburn) isola o domínio de todas as dependências externas via Ports (interfaces) e Adapters (implementações). Driving Ports: o domínio é chamado (HTTP, CLI, testes). Driven Ports: o domínio chama (banco, email, APIs externas). In-Memory Adapters são o superpoder: permitem testes ultrarrápidos sem infra.

## Key Claims

**Claim:** Hexagonal Architecture é o mesmo princípio que Clean Architecture — terminologia diferente.
**Evidence:** Ports = Interfaces da camada de Application. Adapters = implementações da camada de Frameworks. Driving (Primary) Ports = Controllers. Driven (Secondary) Ports = Repositories, gateways externos. A Dependency Rule é idêntica.
**Confidence:** alta

**Claim:** In-Memory Adapters são o principal valor prático — testes sem banco, sem rede, em < 1ms.
**Evidence:** `InMemoryOrderRepository` implementa `OrderRepository` com Map em memória. Teste passa o adapter in-memory para o use case. Executa em < 1ms. Sem Docker, sem cleanup de banco, sem flakiness de rede. 1000 testes = < 1s.
**Confidence:** alta

**Claim:** Driven Ports protegem o domínio de mudanças na infraestrutura.
**Evidence:** Migrar de PostgreSQL para MongoDB = criar `MongoOrderRepository`, registrar no container. Use case não muda. Sem Driven Ports: `import prisma from "../../lib/prisma"` direto no use case = acoplamento fatal.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/hexagonal-architecture]]
- [[concepts/ports-adapters]]
- [[concepts/in-memory-adapters]]
- [[concepts/driving-ports]]
- [[concepts/driven-ports]]
- [[concepts/clean-architecture]]

## Open Questions

- Hexagonal vs Onion vs Clean Architecture — qual a diferença prática além de nomenclatura?
- In-Memory adapters que precisam simular transações — como implementar rollback em memória?
