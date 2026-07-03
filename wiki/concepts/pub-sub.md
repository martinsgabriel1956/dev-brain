---
type: concept
title: "Pub/Sub (Publish-Subscribe)"
aliases: ["publish-subscribe", "pub sub", "publicador-assinante"]
date_created: 2026-05-05
date_updated: 2026-07-03
source_count: 3
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

## Exemplo: Redis Pub/Sub como ponte entre microsserviços e SSE

Um back end com um endpoint [[wiki/concepts/server-sent-events|SSE]] pode se inscrever num canal Redis (`SUBSCRIBE notifications`) e repassar cada mensagem recebida para os clientes conectados. Outro microsserviço publica (`PUBLISH notifications "evento"`) sem precisar declarar o canal antecipadamente — o Redis cria o canal implicitamente na primeira publicação. Cuidado: cada requisição SSE não deve abrir sua própria conexão Redis — ver [[wiki/concepts/singleton-pattern]].

## Padrão: um tópico por usuário para chat/WebSocket

Quando servidores WebSocket são replicados atrás de um [[wiki/concepts/load-balancer|load balancer]], dois usuários conectados a instâncias diferentes não se enxergam sem um broker. O padrão comum: cada usuário se inscreve, ao conectar, em um tópico com o próprio ID (`user:<id>`); para mandar uma mensagem, o remetente publica no tópico do **destinatário**, não no seu próprio. O mesmo padrão escala para grupos (`group:<id>`), com N assinantes recebendo o mesmo evento — é assim que [[wiki/concepts/chat-distribuido]] resolve o roteamento cross-server. Ver [[wiki/sources/updates-tempo-real-polling-sse-websocket]].

## Conexões

- [[mensageria]] — Pub/Sub é o modelo central de mensageria assíncrona
- [[observer-pattern]] — precursor in-process do Pub/Sub distribuído
- [[fanout-pattern]] — estratégia de distribuição usada em Pub/Sub
- [[wiki/concepts/server-sent-events]] — SSE como consumidor final de eventos publicados via Redis Pub/Sub
- [[wiki/concepts/chat-distribuido]] — tópico por usuário/grupo como solução de roteamento cross-server

## Key Sources

- [[sources/design-pattern-observer]] — distinção Observer vs Pub/Sub
- [[wiki/sources/server-sent-events-sse-tempo-real]] — Redis Pub/Sub notificando um endpoint SSE em arquitetura de microsserviços
- [[wiki/sources/updates-tempo-real-polling-sse-websocket]] — padrão de tópico por usuário/grupo para chat distribuído via WebSocket
