---
type: concept
title: "RabbitMQ vs Kafka"
aliases: ["rabbitmq vs kafka", "tarefa vs stream"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_count: 1
tags: [rabbitmq, kafka, mensageria, comparacao]
skill: tech-mentor-backend
status: draft
---

# RabbitMQ vs Kafka

Visão da fonte ([[wiki/sources/rabbitmq-como-funciona-producer-exchange-fila-consumer-simulador]]): ambos fazem pub/sub, mas o [[wiki/entities/rabbitmq]] tenta garantir que a mensagem seja **lida** e a **remove** depois ([[wiki/concepts/ack-de-mensagem]]); o [[wiki/concepts/kafka]] **mantém histórico** relido quando e quantas vezes quiser. Síntese: **RabbitMQ = tarefa; Kafka = stream de eventos**; trocar um pelo outro "é pedir para arrumar problema".

Complementos já na wiki: throughput, replay e latência em [[wiki/sources/rabbitmq]]; consumers competindo na mesma fila vs. partições em [[wiki/concepts/mensageria]]; preferência didática por RabbitMQ em [[wiki/entities/rabbitmq]].

## Key sources

- [[wiki/sources/rabbitmq-como-funciona-producer-exchange-fila-consumer-simulador]]
