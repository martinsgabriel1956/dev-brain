---
type: source
title: "gRPC"
aliases: ["grpc", "protobuf", "protocol buffers", "streaming rpc", "unary rpc"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/grpc.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [grpc, protobuf, streaming, unary, server-streaming, bidirectional-streaming, interceptors, status-codes]
skill: tech-mentor-backend
status: stable
---

## TL;DR

gRPC usa HTTP/2 + Protobuf para comunicação entre serviços. Schema-first via `.proto`. 4 padrões de comunicação: Unary, Server Streaming, Client Streaming, Bidirectional Streaming. Vantagens vs REST: contrato fortemente tipado, código gerado automaticamente, multiplexing HTTP/2, 5–10× menor payload que JSON. Use para: comunicação interna entre microsserviços com alta frequência.

## Key Claims

**Claim:** Protobuf é 5–10× mais compacto que JSON e mais rápido de serializar/deserializar.
**Evidence:** Campo numérico `int32` = 1–5 bytes em Protobuf vs 1–10 bytes de texto em JSON. Serialização Protobuf: ~100ns. JSON: ~1μs. Para microsserviços com milhares de chamadas/segundo, a diferença é significativa em latência acumulada.
**Confidence:** alta

**Claim:** Código gerado automaticamente elimina inconsistências de contrato entre cliente e servidor.
**Evidence:** Mesmo `.proto` gera código tipado para ambos os lados. Mudança no `.proto` = regenera ambos. Impossível ter cliente usando campo que o servidor não retorna (como acontece com REST + OpenAPI desincronizado).
**Confidence:** alta

**Claim:** gRPC Streaming (bidirectional) resolve casos que REST não consegue elegantemente.
**Evidence:** Chat em tempo real: cliente e servidor enviam streams de mensagens. Tracking de pedido: servidor envia updates à medida que status muda. Bulk import: cliente envia stream de records, servidor confirma cada um. REST exigiria polling ou WebSocket customizado.
**Confidence:** alta

**Claim:** gRPC é pior que REST para: APIs públicas, browser (grpc-web tem limitações), proxies HTTP simples.
**Evidence:** Browser não suporta HTTP/2 Trailers nativos — requer grpc-web (proxy). APIs públicas: REST tem melhor suporte em ferramentas externas (Postman, Insomnia, curl). Load balancers simples não entendem gRPC sem configuração.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/grpc]]
- [[concepts/protobuf]]
- [[concepts/http2]]
- [[concepts/bidirectional-streaming]]
- [[concepts/service-mesh]]

## Open Questions

- Protobuf backward compatibility — campo removido pode reutilizar o field number? (não pode — porquê?)
- gRPC Load balancing no Kubernetes — quando usar headless service vs service mesh?
