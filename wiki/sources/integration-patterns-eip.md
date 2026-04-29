---
type: source
title: "Integration Patterns (EIP)"
aliases: ["eip", "enterprise integration patterns", "claim check", "competing consumers", "routing slip"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/integration-patterns-eip.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [eip, integration-patterns, claim-check, competing-consumers, routing-slip, pipes-filters, content-based-router]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Enterprise Integration Patterns (Hohpe & Woolf) são padrões reutilizáveis para integração assíncrona. Os 3 mais práticos: Claim Check (armazena payload grande externamente, envia referência), Competing Consumers (múltiplos workers concorrem pela mesma fila), Routing Slip (roteamento dinâmico por pipeline de processamento).

## Key Claims

**Claim:** Claim Check resolve o problema de payloads grandes em mensageria — não coloque 10MB em uma mensagem Kafka.
**Evidence:** Salva o payload no S3/blob storage, publica referência (URL/chave) na mensagem. Consumer baixa o payload quando precisa. Broker não fica sobrecarregado. Mensagens menores = maior throughput.
**Confidence:** alta

**Claim:** Competing Consumers aumenta throughput sem código adicional — múltiplos workers na mesma fila.
**Evidence:** Fila única + N workers. Cada mensagem é consumida por apenas um worker (exclusividade garantida pelo broker). Escala horizontalmente adicionando workers. Requer idempotência pois partições podem ser rebalanceadas.
**Confidence:** alta

**Claim:** Routing Slip permite que o remetente defina dinamicamente o pipeline de processamento de cada mensagem.
**Evidence:** Mensagem carrega lista de paradas (`["validate", "enrich", "transform", "store"]`). Cada serviço processa e remove sua parada, passando para o próximo. Flexível para pipelines configuráveis por tipo de documento.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/claim-check-pattern]]
- [[concepts/competing-consumers]]
- [[concepts/routing-slip]]
- [[concepts/event-driven-architecture]]
- [[concepts/kafka]]
- [[concepts/dlq-event-patterns]]

## Open Questions

- Routing Slip com falha no meio do pipeline — como compensar as etapas já executadas?
- Competing Consumers com particionamento Kafka — como garantir que mensagens do mesmo usuário sejam processadas em ordem?
