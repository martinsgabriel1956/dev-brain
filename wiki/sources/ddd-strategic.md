---
type: source
title: "DDD — Strategic Design"
aliases: ["ddd strategic", "bounded context", "ubiquitous language", "context map", "event storming"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/ddd-strategic.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [ddd, strategic-design, bounded-context, ubiquitous-language, context-map, event-storming, anti-corruption-layer, open-host-service]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Strategic Design define os limites do domínio (Bounded Contexts) e como eles se comunicam (Context Map). Cada BC tem sua Ubiquitous Language — o mesmo termo pode ter significados diferentes em contextos diferentes (e isso é correto). Event Storming é a técnica para descobrir os limites. Anti-Corruption Layer protege o BC das terminologias externas.

## Key Claims

**Claim:** Bounded Context é o limite onde uma Ubiquitous Language é consistente — fora dele, o termo pode mudar de significado.
**Evidence:** "Cliente" em Vendas ≠ "Contribuinte" em Fiscal ≠ "Destinatário" em Entrega. Mesmo objeto, vocabulários diferentes por contexto. Tentar usar um modelo único para todos os contextos = comprometer a linguagem de cada domínio.
**Confidence:** alta

**Claim:** Context Map documenta as relações entre Bounded Contexts — quem depende de quem e como.
**Evidence:** Padrões de integração: Shared Kernel (código compartilhado), Customer-Supplier (produtor/consumidor), Conformist (consumidor aceita o modelo do produtor), ACL (camada de tradução). A escolha impacta o grau de autonomia de cada time.
**Confidence:** alta

**Claim:** Anti-Corruption Layer (ACL) protege o BC interno da linguagem do sistema externo.
**Evidence:** Sistema externo usa "user_account". BC interno usa "Cliente". ACL traduz: `ExternalUserAdapter.toCliente(userAccount)`. Sem ACL, a linguagem do externo "contamina" o domínio interno, degradando a Ubiquitous Language.
**Confidence:** alta

**Claim:** Um Bounded Context = um microsserviço potencial — mas não necessariamente desde o início.
**Evidence:** Fase 1: Monolito Modular com módulos por BC. Fase 2: Extrair BCs com escala diferente. Fase 3: Microsserviços independentes. Pular direto para microsserviços sem descobrir os BCs = Distributed Monolith.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/bounded-context]]
- [[concepts/ubiquitous-language]]
- [[concepts/context-map]]
- [[concepts/anti-corruption-layer]]
- [[concepts/event-storming]]
- [[concepts/ddd-tactical]]

## Open Questions

- Como manter a Ubiquitous Language consistente quando o time troca pessoas constantemente?
- Event Storming com domínio desconhecido — como conduzir sem domain expert disponível?
