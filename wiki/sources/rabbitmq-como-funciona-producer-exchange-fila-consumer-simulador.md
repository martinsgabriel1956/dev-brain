---
type: source
title: "RabbitMQ: como funciona, para que serve e quando usar (com simulador)"
aliases: ["rabbitmq simulador", "producer exchange fila consumer"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/rabbitmq-como-funciona-producer-exchange-fila-consumer-simulador.md
source_url: ""
author: "não identificado (canal não citado na transcrição)"
date_published: ""
date_ingested: 2026-10-05
source_count: 0
tags: [rabbitmq, mensageria, exchange, routing-key, ack, monolito-distribuido, kafka]
skill: tech-mentor-backend
status: draft
---

# RabbitMQ: como funciona, para que serve e quando usar (com simulador)

## TL;DR

Vídeo didático que parte de um fluxo de loja (pedido → pagamento → nota fiscal → estoque → e-mail) feito por HTTP síncrono, mostra que ele vira um [[wiki/concepts/monolito-distribuido]] preso a dependências externas, e resolve com [[wiki/entities/rabbitmq]]. A ideia central é o [[wiki/concepts/modelo-mental-rabbitmq]]: **producer → exchange → fila → consumer**, com a decisão de roteamento na [[wiki/concepts/exchange-rabbitmq]] (direct, fanout, topic, headers). Fecha com [[wiki/concepts/ack-de-mensagem]], [[wiki/concepts/rabbitmq-vs-kafka]] ("tarefa vs stream de eventos") e [[wiki/concepts/quando-usar-mensageria]].

## Key claims

1. **Microsserviço com dependência síncrona externa é monolito distribuído** — evidência: o encadeamento HTTP Pedidos→Pagamentos→Nota→Estoque→E-mail só responde ao usuário no fim e quebra se qualquer externo cair (exemplo: queda da AbacatePay, citada pelo autor). Ver [[wiki/concepts/monolito-distribuido]], [[wiki/concepts/comunicacao-sincrona]].
2. **O produtor publica na exchange, nunca direto na fila** — a exchange decide o destino. Ver [[wiki/concepts/modelo-mental-rabbitmq]].
3. **Direct = match exato; fanout = broadcast ignorando a chave; topic = padrão com `*` (uma palavra) e `#` (zero ou mais); headers = roteia por cabeçalho.** Ver [[wiki/concepts/exchange-rabbitmq]], [[wiki/concepts/routing-key-e-binding-key]].
4. **Fanout é o mais usado pela simplicidade**; topic é sinal de sistema escalando e organizado (opinião do autor, sem dados).
5. **Ack:** mensagem só sai da fila após confirmação; se o consumidor cair, ela volta — funcionalidade, não bug. Ver [[wiki/concepts/ack-de-mensagem]], [[wiki/concepts/garantia-de-entrega]].
6. **RabbitMQ remove o que foi lido (tarefa); Kafka retém histórico (stream).** Ver [[wiki/concepts/rabbitmq-vs-kafka]], [[wiki/concepts/kafka]].
7. **Usar para desacoplar, background e retentativas; sistema simples com poucas dependências externas → HTTP basta.** Ver [[wiki/concepts/quando-usar-mensageria]], [[wiki/concepts/over-engineering]].

## Entities

- [[wiki/entities/rabbitmq]]
- [[wiki/entities/masstransit]] — biblioteca .NET de pub/sub que, segundo o autor, usa bastante headers exchange.

## Concepts

[[wiki/concepts/mensageria]], [[wiki/concepts/fila]], [[wiki/concepts/pub-sub]], [[wiki/concepts/comunicacao-assincrona]], [[wiki/concepts/event-driven-architecture]], [[wiki/concepts/acoplamento]], [[wiki/concepts/microsservicos]], [[wiki/concepts/saga-pattern]]

## Open questions / lacunas

- Sem DLQ/retry/idempotência: o vídeo não cobre o que fazer com mensagem que falha repetidamente ([[wiki/concepts/dlq]], [[wiki/concepts/idempotencia]]). Ack manual implica entrega at-least-once, logo duplicatas — **inferência minha**.
- A parte "desfazer o processo se estoque/nota falhar" é só enunciada; a compensação ([[wiki/concepts/saga-pattern]]) não é mostrada.
- "RabbitMQ garante que a mensagem será lida" é simplificação: depende de filas duráveis, mensagens persistentes e publisher confirms **[external, não verificado]**.
- Autor/canal e link do simulador não identificados na transcrição.

## Contradições / tensões com a wiki

- Sem contradição. Reforça [[wiki/sources/rabbitmq]] (nota de referência: Kafka vence em replay/throughput; RabbitMQ em roteamento). Nota de nuance: a nota de referência trata `#` como "múltiplos segmentos"; o vídeo diz "zero ou mais" — a segunda é a semântica AMQP padrão **[external]**.

## Quotes

> "Microsserviços que têm dependências fora do microsserviço deles não são microsserviços de verdade; são monolitos distribuídos."

> "Producer → Exchange, e não para a fila. Quem pensa é a exchange."

> "RabbitMQ é tarefa; Kafka é stream de eventos."
