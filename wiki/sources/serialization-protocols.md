---
type: source
title: "Protocolos de Serialização — JSON, Protobuf, Avro, MessagePack"
aliases: ["serialização", "protobuf", "avro", "messagepack", "flatbuffers", "json serialization", "binary serialization"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/serialization-protocols.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [serialization, protobuf, avro, messagepack, flatbuffers, json, binary-protocol, schema-evolution]
skill: tech-mentor-backend
status: stable
---

## TL;DR

4 protocolos: JSON (human-readable, sem schema, universal), Protobuf (binário, schema .proto, gRPC, backward compatible), Avro (binário, schema no Registry, Kafka), MessagePack (JSON binário, sem schema, drop-in replacement). Performance: MessagePack ~2x JSON, Protobuf ~5x JSON. Schema evolution: Protobuf e Avro têm suporte nativo (field numbers e registry). JSON não tem.

## Key Claims

**Claim:** Protobuf garante backward compatibility via field numbers — nunca reutilizar um número de campo removido.
**Evidence:** `message Order { string id = 1; float total = 2; }`. Remover `total`: nunca reutilizar `= 2` para outro campo. `reserved 2;` previne reutilização acidental. Consumer v1 com campo `total` recebe mensagem v2 sem o campo: usa valor default (0). Consumer v2 recebe mensagem v1: ignora campos desconhecidos. Compatibilidade bidirecional garantida.
**Confidence:** alta

**Claim:** MessagePack é o substituto mais simples de JSON para performance — mesma semântica, binário 2x mais compacto.
**Evidence:** JSON: `{"status":"active","count":42}` = 26 bytes. MessagePack equivalente: ~15 bytes. Sem schema novo, sem geração de código. Drop-in replacement para APIs internas com alto volume. Trade-off: perde human-readability para debugging. Para APIs públicas ou onde DX importa mais que performance, JSON ainda é correto.
**Confidence:** alta

**Claim:** Avro com Schema Registry é o padrão para eventos Kafka — schema inferido do registry, payload mínimo.
**Evidence:** Sem schema no payload: Avro é estritamente binário sem metadados. Com Schema Registry: 5 bytes de schema ID + payload binário. Consumer busca schema pelo ID (cacheado). Avro suporta schema evolution (BACKWARD/FORWARD/FULL). Union types para campos opcionais. Melhor escolha quando Schema Registry já está no stack.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/protobuf]]
- [[concepts/avro]]
- [[concepts/messagepack]]
- [[concepts/flatbuffers]]
- [[concepts/schema-evolution]]
- [[concepts/schema-registry]]

## Open Questions

- Protobuf vs Avro para Kafka — quando Protobuf vence Avro apesar da integração nativa do Avro com Schema Registry?
- FlatBuffers para casos de zero-copy — em quais cenários o acesso direto ao buffer sem deserialização justifica a complexidade?
