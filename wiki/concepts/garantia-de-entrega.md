---
type: concept
title: "Garantia de Entrega"
aliases: ["delivery guarantee", "delivery semantics", "at-least-once"]
date_created: 2026-09-30
date_updated: 2026-10-05
source_count: 2
tags: [mensageria, comunicacao-assincrona, confiabilidade, broker]
skill: tech-mentor-backend
status: stub
---

# Garantia de Entrega

Segundo desafio da [[wiki/concepts/comunicacao-assincrona]] em [[wiki/sources/comunicacao-assincrona-arquiteturas-distribuidas-bernardo-lobato]]: muitos brokers **não vêm, por padrão, configurados** para garantir que a mensagem chegue a todos os receptores; é cuidado do desenvolvedor planejar isso. O vídeo não detalha a configuração.

Complemento [[wiki/concepts/mensageria]]: at-least-once exige consumidor idempotente ([[wiki/concepts/idempotencia]]), mensagens que falham N vezes vão para [[wiki/concepts/dlq]], e exactly-once é raro e caro. Publicar após um INSERT não é atômico por padrão ([[wiki/concepts/outbox-pattern]]).

## Ack como mecanismo de entrega

[[wiki/concepts/ack-de-mensagem]]: sem confirmação a mensagem volta à fila; implica reentrega (at-least-once) — inferência. [[wiki/sources/rabbitmq-como-funciona-producer-exchange-fila-consumer-simulador]]

## Key sources

- [[wiki/sources/comunicacao-assincrona-arquiteturas-distribuidas-bernardo-lobato]] — apenas a nomeação do desafio
- [[wiki/sources/rabbitmq-como-funciona-producer-exchange-fila-consumer-simulador]] — ack e reentrega
