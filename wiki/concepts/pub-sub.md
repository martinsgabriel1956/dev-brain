---
type: concept
title: "Pub/Sub (Publish-Subscribe)"
aliases: ["publish-subscribe", "pub sub", "publicador-assinante"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 1
tags: [design-patterns, event-driven, pub-sub, mensageria, broker, observer]
skill: tech-mentor-backend
status: stable
---

# Pub/Sub (Publish-Subscribe)

Padrão de mensageria onde **publicadores** enviam mensagens para **canais/tópicos** e **assinantes** recebem mensagens dos canais de seu interesse — sem que publicador e assinante se conheçam diretamente. Um **broker** intermediário faz a mediação.

## Distinção do Observer

Frequentemente confundido com o [[observer-pattern]], mas são mecanismos diferentes:

| | [[observer-pattern]] | Pub/Sub |
|---|---|---|
| Comunicação | Direta — publicadora → assinante | Indireta — via broker/channel |
| Acoplamento | Publicadora mantém lista de assinantes | Desacoplamento total |
| Escopo | In-process (mesmo processo) | Cross-process, cross-service, distribuído |
| Ordem garantida? | Não (aleatória) | Depende do broker |
| Exemplos | Eventos DOM, listeners de estado React | Kafka, Redis Pub/Sub, AWS SNS/SQS, RabbitMQ |

## Quando usar Pub/Sub em vez de Observer

- Comunicação entre serviços diferentes (microsserviços)
- Fan-out para múltiplos consumidores desconhecidos
- Desacoplamento total entre produtor e consumidor
- Necessidade de persistência, replay ou garantia de entrega

## Conexões

- [[mensageria]] — Pub/Sub é o modelo central de mensageria assíncrona
- [[observer-pattern]] — precursor in-process do Pub/Sub distribuído
- [[fanout-pattern]] — estratégia de distribuição usada em Pub/Sub

## Key Sources

- [[sources/design-pattern-observer]] — distinção Observer vs Pub/Sub
