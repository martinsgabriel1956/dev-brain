---
type: entity
title: "RabbitMQ"
aliases: ["rabbitmq", "rabbit mq"]
date_created: 2026-07-30
date_updated: 2026-09-30
source_count: 2
tags: [mensageria, message-broker, saga-pattern, event-driven]
skill: tech-mentor-backend
status: stub
---

# RabbitMQ

Message broker open-source que implementa AMQP. Usado como fila (queue) para desacoplar serviços — produtor publica mensagem, broker garante entrega e ordem, consumidor processa de forma assíncrona.

## Uso em Saga Pattern

Citado como peça central para implementar [[wiki/concepts/saga-pattern]] sem [[wiki/concepts/two-phase-commit|two-phase commit]]: em vez de um coordinator síncrono bloqueando participantes, cada serviço publica na fila e o RabbitMQ garante que as mensagens sejam processadas em ordem, sem criar gargalo — o custo fica em implementar manualmente a compensação/rollback de cada serviço caso uma etapa falhe. Ver [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]].

## RabbitMQ como Exemplo de Broker Assíncrono

Citado por [[wiki/entities/bernardo-lobato]] (ao lado de Kafka) como broker de mensageria para [[wiki/concepts/comunicacao-assincrona]], em contraste com REST síncrono.

## Key Sources

- [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]] — RabbitMQ como fila que viabiliza Saga Pattern coreografado, citado como exemplo de broker que evita gargalo de coordenação síncrona
- [[wiki/sources/comunicacao-assincrona-arquiteturas-distribuidas-bernardo-lobato]] — RabbitMQ/Kafka como exemplos de broker
