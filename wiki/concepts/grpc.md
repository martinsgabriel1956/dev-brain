---
type: concept
title: "gRPC"
aliases: ["grpc", "protocol buffers", "protobuf rpc"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 2
tags: [grpc, rpc, protobuf, http2, apis, go, comunicacao-interna]
skill: tech-mentor-backend
status: stub
---

# gRPC

Framework de RPC (Remote Procedure Call) de alta performance criado pelo Google. Usa **Protocol Buffers (Protobuf)** como formato de serialização binária e **HTTP/2** como transporte, com suporte nativo a streaming bidirecional. Em vez do modelo REST (`POST /orders` → JSON), o cliente chama um método diretamente (`OrderService.CreateOrder(...)`) sobre um contrato gerado a partir de um arquivo `.proto`.

## Por que é rápido

- Protobuf é binário — 3 a 10x menor que JSON equivalente, serialização mais rápida
- HTTP/2 multiplexa múltiplas requisições numa única conexão TCP, com compressão de headers
- Código cliente/servidor é **gerado automaticamente** a partir do schema — menos boilerplate e menos risco de contrato divergente entre as pontas

## Caso de uso central: comunicação interna, não browser

gRPC nativo não é bem suportado em navegadores (exige um proxy tipo grpc-web ou Envoy para funcionar) — por isso o padrão comum é: **HTTP/REST** na borda (clientes externos, frontend) e **gRPC** para comunicação **serviço-a-serviço** dentro do sistema. Esse é exatamente o desenho adotado por [[wiki/entities/lucas-badico]] no seu sistema de mentoria em Go: o core expõe entry points HTTP e gRPC separados a partir dos mesmos módulos internos, com gRPC reservado para integrações internas. Ver [[wiki/sources/sistema-mentoria-golang-monolito-modular-live-lucas-badico]].

## Relação com Monolito Modular

Em [[wiki/concepts/monolito-modular]], a interface pública de um módulo pode ser exposta tanto como chamada de função in-process quanto, já de saída, como contrato gRPC — o que facilita a extração futura do módulo para microsserviço: a migração vira "trocar o transporte" (chamada direta → gRPC) em vez de reescrever a lógica de negócio.

## Origem: 2015, Google, resposta a microsserviços

Segundo [[wiki/sources/historia-e-evolucao-das-apis-bernardo-lobato]], o gRPC foi lançado pelo [[wiki/entities/google]] em 2015, na mesma década em que o [[wiki/concepts/graphql|GraphQL]] surgiu (Meta) — as duas tecnologias nascem em paralelo mas resolvem problemas diferentes: GraphQL ataca over-fetching no lado cliente-servidor (telas complexas), gRPC ataca performance na comunicação **serviço-a-serviço**, refletindo diretamente a transição da década para arquiteturas de [[wiki/concepts/microsservicos]], que passaram a depender de chamadas remotas para tudo.

## Key Sources

- [[wiki/sources/sistema-mentoria-golang-monolito-modular-live-lucas-badico]] — uso de gRPC para comunicação interna entre módulos, HTTP para clientes externos, em um monolito modular Go
- [[wiki/sources/historia-e-evolucao-das-apis-bernardo-lobato]] — origem do gRPC (Google, 2015) como resposta de performance à ascensão de arquiteturas de microsserviços, em paralelo ao surgimento do GraphQL
