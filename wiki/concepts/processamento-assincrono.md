---
type: concept
title: "Processamento Assincrono"
aliases: ["processamento assíncrono", "background processing"]
date_created: 2026-09-22
date_updated: 2026-09-30
source_count: 4
tags: [processamento-assincrono, comunicacao-assincrona, workers, filas]
skill: tech-mentor-backend
status: draft
---

# Processamento Assincrono

Receptor processa a solicitação **em background**, sem devolver o resultado na mesma chamada. É o lado do *receptor* da [[wiki/concepts/comunicacao-assincrona]]: quem recebe a mensagem aceita, enfileira e processa depois (workers + fila), e o resultado é entregue por notificação ([[wiki/concepts/webhook]]), consulta de status ([[wiki/concepts/async-request-reply]]) ou evento ([[wiki/concepts/mensageria]]).

## Usos citados

- Workers + message queue para tarefas pesadas — [[wiki/sources/listen-notes-good-enough-engineering]]
- Workers Celery + RabbitMQ para tarefas pesadas — [[wiki/sources/listen-notes-one-person-startup]]
- Serviços de Estoque e Faturamento processando o evento "pedido criado" de forma independente — [[wiki/sources/comunicacao-assincrona-arquiteturas-distribuidas-bernardo-lobato]]

Ver também [[wiki/concepts/filas-e-workers]].

## Caso: Miniatura de Imagem

Geração de miniatura após upload como trabalho assíncrono via fila + worker, enquanto o usuário continua navegando ([[wiki/concepts/filas-e-workers]]).

## Key sources

- [[wiki/sources/listen-notes-good-enough-engineering]]
- [[wiki/sources/listen-notes-one-person-startup]]
- [[wiki/sources/comunicacao-assincrona-arquiteturas-distribuidas-bernardo-lobato]] — receptor processa em background e notifica depois
- [[wiki/sources/como-estudar-system-design-building-blocks-instagram-simplificado]] — geração de miniatura de imagem em background via fila/worker
