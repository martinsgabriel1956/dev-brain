---
type: concept
title: "Ack de Mensagem (acknowledgment)"
aliases: ["ack", "acknowledgment", "ack rabbitmq"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_count: 1
tags: [rabbitmq, ack, garantia-de-entrega, mensageria]
skill: tech-mentor-backend
status: draft
---

# Ack de Mensagem

O consumidor confirma (ack) que processou a mensagem; só então o broker a remove da [[wiki/concepts/fila]]. Se o serviço cair no meio do processamento, sem ack a mensagem **volta para a fila** e permanece disponível. O autor destaca que muitos tomam isso por bug, mas é a funcionalidade que evita perda de mensagem em produção ([[wiki/sources/rabbitmq-como-funciona-producer-exchange-fila-consumer-simulador]]).

**Inferência minha (não está no vídeo):** como a mensagem pode ser reentregue após falha, o consumidor precisa ser [[wiki/concepts/idempotencia|idempotente]]; ver [[wiki/concepts/garantia-de-entrega]]. Mensagens que falham sempre pedem [[wiki/concepts/dlq]].

Ver [[wiki/entities/rabbitmq]], [[wiki/concepts/modelo-mental-rabbitmq]].

## Key sources

- [[wiki/sources/rabbitmq-como-funciona-producer-exchange-fila-consumer-simulador]]
