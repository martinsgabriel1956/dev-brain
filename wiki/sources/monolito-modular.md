---
type: source
title: "Monolito Modular"
aliases: ["monolito modular", "modular monolith", "bounded modules", "majestic monolith"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/monolito-modular.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [monolito-modular, bounded-modules, modular-monolith, comunicacao-modulos, migracao-microsservicos, domain-isolation]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Monolito Modular é a arquitetura ideal para a maioria dos projetos — deploy único, sem complexidade distribuída, mas com isolamento de domínio via módulos. Cada módulo tem public API bem definida, dados isolados (mesmo banco, schemas separados), e comunicação via eventos in-process. Permite migrar para microsserviços gradualmente quando necessário.

## Key Claims

**Claim:** Monolito Modular é melhor que microsserviços para times pequenos — sem overhead distribuído.
**Evidence:** Sem service discovery, sem distributed tracing complexo, sem latência de rede entre módulos, sem eventual consistency forçada. Deploy único. Mesmo banco (schemas separados por módulo). Performance de chamada entre módulos: nanoseconds vs milliseconds.
**Confidence:** alta

**Claim:** Módulos devem ter API pública bem definida — acesso ao módulo só via index.ts.
**Evidence:** `import { PlaceOrderUseCase } from "../orders"` (via index.ts) vs `import { ... } from "../orders/domain/order.entity"` (acesso interno). O segundo é violação de encapsulamento. ESLint rule `import/no-internal-modules` enforça a regra.
**Confidence:** alta

**Claim:** Comunicação entre módulos via eventos in-process é mais limpa que imports diretos de use cases.
**Evidence:** Orders module publica `OrderPlaced` event. Inventory module reage sem conhecer Orders. Desacoplamento sem broker externo. Quando extrair para microsserviços: substitui EventEmitter por Kafka, sem mudar a lógica dos módulos.
**Confidence:** alta

**Claim:** Migração para microsserviços de um Monolito Modular é 10× mais simples que de um Big Ball of Mud.
**Evidence:** Módulo bem isolado = extrai o diretório, adiciona HTTP/gRPC handler, troca EventEmitter por Kafka. Módulo acoplado = reescreve tudo. O investimento em isolamento no monolito é o que possibilita a migração.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/monolito-modular]]
- [[concepts/bounded-modules]]
- [[concepts/domain-isolation]]
- [[concepts/event-driven-architecture]]
- [[concepts/microsservicos]]
- [[concepts/strangler-fig]]

## Open Questions

- Banco único com schemas por módulo — como lidar com queries que precisam de dados de múltiplos módulos (JOIN cross-schema)?
- Quando um módulo está pronto para ser extraído como microsserviço? Qual o critério objetivo?
