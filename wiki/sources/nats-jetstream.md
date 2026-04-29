---
type: source
title: "NATS e NATS JetStream"
aliases: ["nats", "nats jetstream", "nats core", "nats kv", "nats streaming"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/nats-jetstream.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [nats, jetstream, streaming, pub-sub, kv-store, edge-computing, request-reply]
skill: tech-mentor-backend
status: stable
---

## TL;DR

NATS é um sistema de mensageria cloud-native ultralleve. NATS Core: pub/sub fire-and-forget, sem persistência. JetStream adiciona persistência, consumers duráveis e ACK semântico (at-least-once). KV Store sobre JetStream para configurações distribuídas. Melhor opção para: edge/IoT, request-reply entre microserviços, sistemas que precisam de mensageria sem overhead operacional do Kafka.

## Key Claims

**Claim:** NATS Core é pub/sub fire-and-forget — JetStream é necessário para garantias de entrega.
**Evidence:** NATS Core: se não há subscriber quando a mensagem é publicada, ela é perdida. JetStream adiciona Streams (persistência configurável) e Consumers (durável, com ACK Explicit). `msg.ack()` confirma; `msg.nak()` recoloca para reprocessar; `msg.term()` descarta permanentemente.
**Confidence:** alta

**Claim:** NATS tem request-reply nativo — diferencial sobre Kafka e RabbitMQ para RPC assíncrono.
**Evidence:** `nc.request("service.action", payload)` publica e aguarda resposta em inbox temporário. Respondente usa `msg.respond(data)`. Sem precisar de reply-to queue manual (como no RabbitMQ) ou correlation ID gerenciado manualmente.
**Confidence:** alta

**Claim:** JetStream KV Store substitui Redis para configurações distribuídas sem dependência extra.
**Evidence:** `js.views.kv("CONFIG")` cria um KV Store sobre JetStream. Suporta watch (stream de mudanças), TTL por key, revisões históricas. Para casos simples de feature flags ou configuração distribuída, elimina Redis da stack.
**Confidence:** média

**Claim:** NATS perde para Kafka em particionamento explícito e para RabbitMQ em roteamento complexo.
**Evidence:** Kafka: partition key garante ordering por entidade. NATS JetStream: ordering por subject, mas sem particionamento explícito por chave de negócio. RabbitMQ: exchanges com bindings flexíveis. NATS tem subject wildcards mas sem lógica de roteamento avançada.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/nats]]
- [[concepts/nats-jetstream]]
- [[concepts/pub-sub]]
- [[concepts/request-reply]]
- [[concepts/at-least-once]]

## Open Questions

- NATS JetStream em produção com 100+ serviços — como evitar explosão de subjects e consumers órfãos?
- NATS vs Kafka para sistemas de IoT com 1M+ devices — qual escala melhor em edge nodes?
