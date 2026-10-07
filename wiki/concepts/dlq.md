---
type: concept
title: "Dlq"
aliases: []
date_created: 2026-09-22
date_updated: 2026-10-07
source_count: 5
tags: [dlq]
skill: tech-mentor-backend
status: stub
---

# Dlq

Stub criado durante sweep de lint (links quebrados) a partir de referências em 3 página(s) da wiki — conteúdo completo pendente de ingest dedicado.

## Contexto das citações

- Em [[wiki/sources/dlq-event-patterns]]: [[wiki/concepts/dlq]]
- Em [[wiki/sources/rabbitmq]]: [[wiki/concepts/dlq]]
- Em [[wiki/sources/sqs-sns]]: [[wiki/concepts/dlq]]

## Pendências

Página não nasceu de um ingest próprio; TL;DR acima é reconstruído apenas a partir do texto das páginas que a citam. Precisa de fonte dedicada para virar `draft`/`stable`.

## Nota: ack e mensagens que falham

Ack manual devolve a mensagem à fila quando o consumidor cai ([[wiki/concepts/ack-de-mensagem]]); o vídeo não cobre DLQ — lacuna. [[wiki/sources/rabbitmq-como-funciona-producer-exchange-fila-consumer-simulador]]

## Key sources

- [[wiki/sources/dlq-event-patterns]]
- [[wiki/sources/rabbitmq]]
- [[wiki/sources/sqs-sns]]
- [[wiki/sources/rabbitmq-como-funciona-producer-exchange-fila-consumer-simulador]] — reentrega por ack; DLQ não coberta


## Key sources (adição 2026-10-07)

- [[wiki/sources/desafio-sistema-notificacao-system-design-reprova-senior-ana]] — falhas de entrega alimentam reprocessamento/reconciliação.
