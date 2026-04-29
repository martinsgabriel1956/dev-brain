---
type: source
title: "Event Versioning"
aliases: ["event versioning", "schema evolution", "tolerant reader", "upcasting", "copy-transform"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/event-versioning.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [event-versioning, schema-evolution, tolerant-reader, upcasting, copy-transform, weak-schema, backward-compatible]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Eventos em sistemas distribuídos nunca podem ser alterados destrutivamente — consumidores antigos ainda processam eventos velhos. 4 estratégias: Weak Schema (ignora campos desconhecidos, default para ausentes), Versioning Explícito (campo `version` + deserializador por versão), Upcasting (Event Sourcing: transforma evento antigo em novo formato), Copy-Transform (migração em background).

## Key Claims

**Claim:** Regra fundamental: nunca altere o tipo ou remova campos de eventos já publicados.
**Evidence:** Consumidores desserializam eventos antigos do broker/event store. Remover campo obrigatório = NullPointerException no consumidor. Mudar tipo = parse error. Seguro: adicionar campos opcionais com default, nunca remover ou mudar tipo.
**Confidence:** alta

**Claim:** Weak Schema (Tolerant Reader) é a estratégia mais simples — funciona para adição de campos opcionais.
**Evidence:** `z.object({...}).passthrough()` ignora campos extras. Campos novos com `.default("valor")` funcionam em eventos antigos. Limitação: não resolve mudança de tipo ou remoção de campo obrigatório.
**Confidence:** alta

**Claim:** Upcasting é a estratégia para Event Sourcing — transforma eventos antigos em novos no momento da leitura.
**Evidence:** Evento V1 armazenado com `total`. Upcaster transforma para V2 com `totalAmount` ao ler do event store. O evento no storage não muda — a transformação é na camada de deserialização. Permite evolução sem migração de dados históricos.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/event-versioning]]
- [[concepts/tolerant-reader]]
- [[concepts/upcasting]]
- [[concepts/schema-registry]]
- [[concepts/event-sourcing]]
- [[concepts/expand-contract]]

## Open Questions

- Copy-Transform em produção com bilhões de eventos — como fazer sem impacto no storage e processamento?
- Schema Registry com Avro vs. Versioning explícito no JSON — quando cada abordagem é melhor?
