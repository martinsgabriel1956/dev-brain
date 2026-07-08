---
type: concept
title: "Solid Queue"
aliases: ["solidqueue", "fila da 37signals"]
date_created: 2026-07-07
date_updated: 2026-07-07
source_count: 1
tags: [background-jobs, rails, banco-de-dados, mysql, postgresql, sqlite, 37signals, grande-rollback]
skill: tech-mentor-backend
status: stub
---

# Solid Queue

Biblioteca de fila de processamento (background jobs) da [[wiki/entities/37signals]] que roda inteiramente sobre banco relacional (MySQL, PostgreSQL ou SQLite) — sem Redis, sem Kafka, sem broker externo dedicado. Citada como exemplo de que filas de trabalho não exigem necessariamente infraestrutura de mensageria separada; ver [[wiki/concepts/skip-locked]] como uma das primitivas típicas desse tipo de implementação (workers consomem jobs via `SELECT ... FOR UPDATE SKIP LOCKED` ou equivalente).

## Por Que Existe

Nasceu do mesmo movimento arquitetural da 37signals de sair do cloud gerenciado e simplificar a stack — a tese é que, até um determinado volume de throughput, um banco relacional bem modelado é suficiente para uma fila de jobs, e evita o custo operacional de manter Redis/Kafka como um sistema à parte.

## Contraste com Filas Tradicionais (ver [[wiki/sources/background-jobs]])

| Aspecto | Broker dedicado (Kafka, SQS, RabbitMQ) | Fila baseada em banco relacional (Solid Queue) |
|---|---|---|
| Infraestrutura adicional | Sim | Não — reusa o banco já existente |
| Throughput máximo | Muito alto (milhões/s) | Moderado (dezenas de milhares/s) |
| Garantias | Depende do broker | ACID nativo da transação |
| Visibilidade/debug | Dashboard do broker | Query direta na tabela |
| Complexidade operacional | Alta | Baixa |

## Key Sources

- [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]] — citado como precedente/inspiração para o redesenho de estoque da Shopify
