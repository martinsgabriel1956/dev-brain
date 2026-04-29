---
type: source
title: "Schema Registry"
aliases: ["schema registry", "confluent schema registry", "avro", "protobuf schema", "schema evolution", "schema compatibility"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/schema-registry.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [schema-registry, avro, protobuf, json-schema, kafka, backward-compatibility, forward-compatibility, asyncapi]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Schema Registry centraliza e versiona schemas de eventos Kafka. Sem ele, producer pode mudar formato e quebrar consumers silenciosamente. Confluent Schema Registry (open source) suporta Avro, Protobuf e JSON Schema. Compatibilidade: BACKWARD (consumers antigos leem novos eventos), FORWARD (consumers novos leem eventos antigos), FULL (ambos). Producer valida contra schema antes de publicar — falha rápido se breaking change.

## Key Claims

**Claim:** Schema Registry previne breaking changes silenciosas em eventos — validação acontece antes de publicar.
**Evidence:** Sem Schema Registry: producer publica `{ "orderId": "123", "total": 100 }`, consumer espera `total` como número. Producer muda para string → desserialização falha em runtime, potencialmente horas depois. Com Schema Registry: producer tenta registrar novo schema, recebe erro de incompatibilidade IMEDIATAMENTE, antes de publicar.
**Confidence:** alta

**Claim:** BACKWARD compatibility é o modo mais comum — consumers antigos devem conseguir ler eventos novos.
**Evidence:** BACKWARD: pode ADICIONAR campos com default, pode REMOVER campos opcionais. Não pode REMOVER campos obrigatórios nem MUDAR tipos. Consumer antigo lê evento novo: ignora campos desconhecidos, usa default para campos removidos. FORWARD: consumer novo lê evento antigo. FULL: ambos.
**Confidence:** alta

**Claim:** Avro com Schema Registry usa schema ID no payload — não inclui o schema completo em cada mensagem.
**Evidence:** Sem Schema Registry: cada mensagem carrega o schema completo (overhead). Com Schema Registry: mensagem = `[magic byte][schema_id (4 bytes)][avro payload]`. Consumer busca schema pelo ID (cacheado localmente). Overhead de rede mínimo; schema compartilhado entre todas as mensagens do mesmo tipo.
**Confidence:** alta

**Claim:** AsyncAPI é o contrato de documentação; Schema Registry é o enforcement em runtime — complementares, não concorrentes.
**Evidence:** AsyncAPI: descreve canais, operações, schemas em YAML (como OpenAPI para events). Documentação para humanos e geração de clientes. Schema Registry: valida schemas em tempo de publicação, armazena versões. AsyncAPI documenta O QUE o sistema faz; Schema Registry garante que o producer respeita o contrato.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/schema-registry]]
- [[concepts/avro]]
- [[concepts/protobuf]]
- [[concepts/backward-compatibility]]
- [[concepts/forward-compatibility]]
- [[concepts/event-versioning]]
- [[entities/confluent]]
- [[concepts/asyncapi]]

## Open Questions

- Schema Registry multi-datacenter — como lidar com replicação de schemas em setups multi-region?
- JSON Schema no Schema Registry vs Avro — quando vale o overhead de Avro vs simplicidade do JSON?
