---
type: source
title: "Tolerant Reader"
aliases: ["tolerant reader", "robustness principle", "postel's law", "ignore unknown fields", "schema evolution consumer"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/tolerant-reader.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [tolerant-reader, robustness-principle, postel-law, schema-evolution, backward-compatibility, event-versioning]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Tolerant Reader (Martin Fowler): consumidores devem ser liberais no que aceitam — ignorar campos desconhecidos, usar defaults para campos ausentes. Oposto: consumidor que falha ao receber campos novos ou ao encontrar campos opcionais ausentes. Complemento do Expand-Contract: producer adiciona campo (Expand) sem quebrar consumers que seguem Tolerant Reader. Implementação: Zod `.passthrough()` ou `strip()` para campos extras.

## Key Claims

**Claim:** Consumidor Tolerant Reader ignora campos desconhecidos — producer pode adicionar campos sem coordenação.
**Evidence:** Consumer frágil: `JSON.parse(payload)` com `if (!data.newField) throw Error` — quebra quando producer adiciona `newField`. Tolerant Reader: deserializar apenas os campos que o consumer usa, ignorar o resto. Zod: `schema.strip()` remove campos extras silenciosamente. Permite evolução independente de producer e consumer em sistemas distribuídos.
**Confidence:** alta

**Claim:** Campos obrigatórios tornados opcionais quebram consumers Tolerant Reader se não tiverem default.
**Evidence:** Producer remove campo `currency` (antes obrigatório). Consumer Tolerant Reader: `currency = data.currency ?? "BRL"` — usa default se ausente. Consumer frágil: `const currency = data.currency` e usa em cálculo sem verificar → runtime error. Regra: todo campo lido por um consumer deve ter um default defensivo.
**Confidence:** alta

**Claim:** Tolerant Reader em Protobuf e Avro é garantido pelo protocolo — campos com número desconhecido são ignorados automaticamente.
**Evidence:** Protobuf: consumer com schema antigo recebe mensagem com campo `= 5` que não conhece. Protobuf parser ignora campos com field numbers desconhecidos. Avro com Schema Registry: consumer projeta o schema do writer para o schema do reader — campos no writer mas não no reader são ignorados. Diferente de JSON que exige implementação manual de Tolerant Reader.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/tolerant-reader]]
- [[concepts/robustness-principle]]
- [[concepts/expand-contract]]
- [[concepts/backward-compatibility]]
- [[concepts/event-versioning]]

## Open Questions

- Tolerant Reader com campos que mudam de tipo (int → float) — como lidar sem quebrar deserialização?
- Quando Tolerant Reader esconde bugs de contrato — como detectar que um campo importante foi removido por engano?
