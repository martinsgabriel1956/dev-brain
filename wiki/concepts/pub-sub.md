---
type: concept
title: "Pub/Sub (Publish-Subscribe)"
aliases: ["publish-subscribe", "pub sub", "publicador-assinante"]
date_created: 2026-05-05
date_updated: 2026-07-09
source_count: 4
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

## Distinção de Message Queue: quem depende de quem

Pub/Sub publica um **fato**; message queue publica um **trabalho a ser feito**. A diferença mais útil na prática não é técnica, é de dependência: numa [[wiki/concepts/filas-e-workers|message queue]], quem depende é o publisher — o serviço precisa que o job seja executado (ex.: comprimir uma imagem), e não faz sentido dois workers processarem o mesmo job. Em Pub/Sub, quem depende é o subscriber — o publicador ("pagamento feito com sucesso") não liga se alguém está ouvindo, e cada assinante recebe sua própria cópia via fan-out. Os dois modelos são comumente combinados: um evento Pub/Sub ("pagamento aprovado") dispara um serviço que, por sua vez, enfileira um job numa message queue (ex.: enviar e-mail) para garantir entrega e retry. Ver [[wiki/concepts/bullmq]] para uma implementação concreta do lado message queue. Ver [[wiki/sources/pub-sub-message-queue-bullmq-na-pratica]].

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
- [[wiki/concepts/filas-e-workers]] — modelo mental oposto: message queue distribui trabalho, não fatos
- [[wiki/concepts/bullmq]] — implementação concreta do lado message queue, contrastada com Pub/Sub na fonte que introduziu essa distinção

## Key Sources

- [[sources/design-pattern-observer]] — distinção Observer vs Pub/Sub
- [[wiki/sources/server-sent-events-sse-tempo-real]] — Redis Pub/Sub notificando um endpoint SSE em arquitetura de microsserviços
- [[wiki/sources/updates-tempo-real-polling-sse-websocket]] — padrão de tópico por usuário/grupo para chat distribuído via WebSocket
- [[wiki/sources/pub-sub-message-queue-bullmq-na-pratica]] — distinção Pub/Sub vs message queue pelo modelo de dependência (quem depende de quem)
