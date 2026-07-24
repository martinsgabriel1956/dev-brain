---
type: source
title: "Presenters"
aliases: ["presenter", "presenters", "view model", "output port", "interface adapters", "clean architecture presenter"]
date_created: 2026-04-23
date_updated: 2026-07-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/presenters.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [presenters, view-model, output-port, clean-architecture, interface-adapters, transformation]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

Presenter é a camada que transforma a saída do UseCase em formato adequado para cada interface (REST, GraphQL, CLI). UseCase retorna `OutputData` puro (sem serialização). Presenter converte para `ViewModel` adequado: REST → JSON com campos renomeados, GraphQL → resolver types, CLI → texto formatado. Mesmo UseCase, múltiplos Presenters para diferentes interfaces.

## Key Claims

**Claim:** Presenter separa transformação de apresentação do UseCase — UseCase não conhece o formato de saída.
**Evidence:** UseCase `PlaceOrderUseCase` retorna `PlaceOrderOutput { orderId, total, placedAt }`. Presenter REST: transforma em `{ id: orderId, amount: total, created_at: placedAt.toISOString() }`. Presenter GraphQL: retorna o tipo `Order` conforme schema. UseCase imutável; múltiplas interfaces adicionadas sem modificar a lógica de negócio.
**Confidence:** alta

**Claim:** Presenter vale a pena quando há múltiplas interfaces ou transformações não triviais — overhead para API simples.
**Evidence:** API única com resposta direta: Presenter adiciona indireção sem benefício. Justifica quando: REST + GraphQL + CLI + WebSocket consomem o mesmo UseCase, ou transformação envolve formatação de datas por locale, moeda, computed fields. Clean Architecture formal: UseCase → Output Port (interface) → Presenter (implementação).
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/presenter]]
- [[concepts/view-model]]
- [[concepts/output-port]]
- [[concepts/clean-architecture]]
- [[concepts/interface-adapters]]

## Open Questions

- Presenter em NestJS com Interceptors — quando usar `ClassSerializerInterceptor` vs Presenter explícito?
- Presenter para streaming responses (SSE, WebSocket) — como modelar saída incremental vs saída completa?

## Nota de Atualização (2026-07-10)

[[wiki/sources/mappers-conversao-entre-camadas]] descreve o mesmo problema — divergência de formato da mesma entidade entre camadas — a partir do lado de persistência (Prisma), nomeando a solução genérica de [[wiki/concepts/mapper-pattern]]. Presenter é o caso específico desse padrão aplicado à camada HTTP/apresentação.

## Nota de Atualização (2026-07-24)

O link `[[concepts/clean-architecture]]` citado acima agora aponta para uma página real: [[wiki/concepts/clean-architecture]], criada a partir de [[wiki/sources/objetos-vs-estruturas-de-dados-clean-architecture]] — essa fonte nova descreve o fluxo completo de Clean Architecture numa aplicação web (Controller → Use Case → Entities → Presenter → View), do qual o Presenter/ViewModel descrito nesta página é apenas o trecho final (Output Data → Presenter → ViewModel → View).
