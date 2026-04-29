---
type: source
title: "DDD — Tactical Design"
aliases: ["ddd tactical", "entity", "value object", "aggregate", "domain service", "specification pattern"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/ddd-tactical.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [ddd, tactical-design, entity, value-object, aggregate, repository, domain-service, specification-pattern, anemic-domain-model]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Tactical Design são os building blocks: Entity (identidade única, mutável), Value Object (imutável, definido por atributos), Aggregate (raiz de consistência transacional), Repository (porta para persistência), Domain Service (lógica que não cabe em uma entidade). A regra de ouro: comportamento + dados na mesma classe. Anemic Domain Model = o anti-pattern.

## Key Claims

**Claim:** Value Object é imutável e definido por atributos — dois VOs com os mesmos valores são iguais.
**Evidence:** `Money.of(100, "BRL")` == `Money.of(100, "BRL")`. Não tem ID. Operações retornam novos VOs em vez de mutar. Vantagem: invariantes garantidos no construtor (ex: `amount < 0` lança exceção), eliminando estados inválidos.
**Confidence:** alta

**Claim:** Aggregate define a fronteira de consistência transacional — tudo dentro do Aggregate é consistente.
**Evidence:** Aggregate Root é o único ponto de entrada. Entidades internas não são acessadas diretamente — só via Aggregate Root. Uma transação não deve cruzar dois Aggregates. Se precisar, use eventual consistency via Domain Events.
**Confidence:** alta

**Claim:** Anemic Domain Model é o anti-pattern mais comum — entidades são DTOs glorificados.
**Evidence:** Entity com apenas getters/setters. Toda lógica de negócio em `OrderService`, `UserService`. Resultado: regras duplicadas em vários services, invariantes não garantidas, estado inválido possível de fora da entidade.
**Confidence:** alta

**Claim:** Specification Pattern extrai regras de negócio complexas para objetos reutilizáveis e combiníveis.
**Evidence:** `PremiumCustomerSpec.isSatisfiedBy(customer)` — reutilizável em qualquer contexto. `spec1.and(spec2)` para composição. Permite usar a mesma regra em queries (WHERE clause), validações, e condicionais sem duplicação.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/entity-ddd]]
- [[concepts/value-object]]
- [[concepts/aggregate]]
- [[concepts/aggregate-root]]
- [[concepts/domain-service]]
- [[concepts/specification-pattern]]
- [[concepts/anemic-domain-model]]
- [[concepts/repository-pattern]]

## Open Questions

- Aggregate size: quão grande pode ser antes de virar um Aggregate com muita responsabilidade?
- Domain Events dentro do Aggregate — como publicar sem acoplar ao event bus na camada de domain?
