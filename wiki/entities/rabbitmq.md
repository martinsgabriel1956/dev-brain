---
type: entity
title: "RabbitMQ"
aliases: ["rabbitmq", "rabbit mq"]
date_created: 2026-07-30
date_updated: 2026-10-08
source_count: 7
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

## Preferência Didática: RabbitMQ vs Kafka

O autor da fonte prefere RabbitMQ por ser "mais simplificado" que o Kafka ("muito grande"), ressalvando que depende do contexto; usado no caso para a fila de geração de miniaturas. Opinião, sem benchmark.

## Código Fonte TV — cinco tipos de armazenamento

Citado com Amazon SQS e Apache Kafka como exemplo de mensageria no mapa de armazenamento.

## Modelo e exchanges

Modelo producer → exchange → fila → consumer, quatro tipos de exchange ([[wiki/concepts/exchange-rabbitmq]]), [[wiki/concepts/ack-de-mensagem]] e comparação 'tarefa vs stream' ([[wiki/concepts/rabbitmq-vs-kafka]]). Ver [[wiki/concepts/modelo-mental-rabbitmq]]. [[wiki/sources/rabbitmq-como-funciona-producer-exchange-fila-consumer-simulador]]

## Key Sources


- [[wiki/sources/cinco-tipos-de-armazenamento-de-dados-qual-usar-codigo-fonte-tv]] — RabbitMQ no mapa de mensageria
- [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]] — RabbitMQ como fila que viabiliza Saga Pattern coreografado, citado como exemplo de broker que evita gargalo de coordenação síncrona
- [[wiki/sources/comunicacao-assincrona-arquiteturas-distribuidas-bernardo-lobato]] — RabbitMQ/Kafka como exemplos de broker
- [[wiki/sources/como-estudar-system-design-building-blocks-instagram-simplificado]] — fila de miniaturas; preferência do autor por RabbitMQ em relação a Kafka, dependente de contexto
- [[wiki/sources/cqrs-desbalanco-leitura-escrita-banco-de-leitura-eventos]] — exemplo de message broker que enfileira os eventos de cadastro consumidos de forma assíncrona para atualizar o banco de leitura
- [[wiki/sources/rabbitmq-como-funciona-producer-exchange-fila-consumer-simulador]] — modelo mental, exchanges, ack e quando usar
- [[wiki/sources/arquitetura-orientada-a-eventos-luiz-gago-faria-otavio-santana-eduardo-macris]] — comentário (ASR ambíguo) de que não propaga trace automaticamente em EDA
