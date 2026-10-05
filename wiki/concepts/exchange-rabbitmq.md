---
type: concept
title: "Exchange (RabbitMQ)"
aliases: ["exchange", "direct exchange", "fanout exchange", "topic exchange", "headers exchange"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_count: 1
tags: [rabbitmq, exchange, direct, fanout, topic, headers, roteamento]
skill: tech-mentor-backend
status: draft
---

# Exchange (RabbitMQ)

Componente que recebe as mensagens do producer e as roteia para filas. Quatro tipos ([[wiki/sources/rabbitmq-como-funciona-producer-exchange-fila-consumer-simulador]]):

| Tipo | Critério | Uso típico |
|---|---|---|
| **direct** | routing key == binding key (match exato) | `order.created`, `order.canceled`, `order.error` para filas/consumidores distintos |
| **fanout** | ignora a chave; entrega a **todas** as filas ligadas (broadcast) | "pedido criado" para Pagamentos, Estoque, Notificações; o mais usado pela simplicidade (opinião do autor) |
| **topic** | binding key é padrão: `*` = exatamente uma palavra; `#` = zero ou mais | `order.*` para notificações; `#` para audit log que recebe tudo |
| **headers** | roteia por cabeçalho da mensagem (ex.: `país=Brasil`), ignora a chave | menos comum; usado por bibliotecas como [[wiki/entities/masstransit]] |

Exemplo topic: pagamentos `order.created`, estoque `order.paid`, notificações `order.*` → `order.paid` chega a estoque e notificações; `order.paid.x` (duas palavras depois) **não** casa com `order.*`, mas casa com `order.#`.

Não precisa excluir consumidor "tirando-o da exchange" num fanout — para filtrar, use topic. Ver [[wiki/concepts/routing-key-e-binding-key]], [[wiki/concepts/modelo-mental-rabbitmq]], [[wiki/entities/rabbitmq]], [[wiki/concepts/pub-sub]].

**Lacuna:** o simulador do vídeo não implementava headers no momento da gravação.

## Key sources

- [[wiki/sources/rabbitmq-como-funciona-producer-exchange-fila-consumer-simulador]] — os quatro tipos com exemplos
- [[wiki/sources/rabbitmq]] — nota de referência (inclui DLX)
