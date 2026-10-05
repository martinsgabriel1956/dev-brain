---
type: concept
title: "Modelo Mental do RabbitMQ (Producer → Exchange → Fila → Consumer)"
aliases: ["producer exchange fila consumer"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_count: 1
tags: [rabbitmq, mensageria, exchange, producer, consumer]
skill: tech-mentor-backend
status: draft
---

# Modelo Mental do RabbitMQ

Quatro peças: **producer** (API, console app, processo em background), **[[wiki/concepts/exchange-rabbitmq|exchange]]**, **[[wiki/concepts/fila|fila]]** (FIFO) e **consumer** (serviço/API; pode até ser o próprio serviço que publicou).

O erro mais comum: achar que o produtor manda **direto para a fila**. Não — publica na exchange, e é ela que decide para quais filas a mensagem vai (via [[wiki/concepts/routing-key-e-binding-key]]). A configuração do roteamento mora na exchange. O consumidor confirma a leitura com [[wiki/concepts/ack-de-mensagem]].

Efeito de desenho: Pedidos publica "pedido criado" e segue; Pagamentos, Estoque e Notificações reagem por conta própria — desacoplamento descrito em [[wiki/concepts/mensageria]] e [[wiki/concepts/comunicacao-assincrona]].

## Key sources

- [[wiki/sources/rabbitmq-como-funciona-producer-exchange-fila-consumer-simulador]] — origem do modelo e do alerta "producer → exchange, não → fila"
