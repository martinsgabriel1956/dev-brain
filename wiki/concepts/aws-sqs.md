---
type: concept
title: "AWS SQS (Simple Queue Service)"
aliases: ["SQS", "Simple Queue Service", "fila AWS"]
date_created: 2026-08-17
date_updated: 2026-08-17
source_count: 1
tags: ["aws", "sqs", "fila", "mensageria", "event-driven", "infra", "cloud"]
skill: tech-mentor-infra
status: stub
---

# AWS SQS (Simple Queue Service)

Fila gerenciada da AWS: o produtor manda mensagem, o consumidor processa quando puder. Se o consumidor cai, a mensagem espera na fila — mecanismo de desacoplamento entre sistemas e absorção de picos de tráfego, instância concreta do padrão geral de [[wiki/concepts/fila|fila]] e [[wiki/concepts/filas-e-workers|filas e workers]].

## Tipos de Fila

- **Standard** — throughput ilimitado, entrega **pelo menos uma vez** (at-least-once — mensagens podem chegar duplicadas, o consumidor precisa ser idempotente).
- **FIFO** — ordem garantida, processamento **exactly-once**, throughput limitado.

## Dead Letter Queue (DLQ)

Captura mensagens que falharam repetidamente no processamento, permitindo análise posterior sem bloquear a fila principal.

## SQS vs. SNS vs. EventBridge

SQS entrega para **um** consumidor por mensagem (fila). Ver [[wiki/concepts/aws-sns|SNS]] para entrega a múltiplos consumidores (fan-out) e EventBridge para arquiteturas event-driven mais complexas com filtragem e replay. Regra prática: SQS para desacoplamento simples.

## Relação com outros conceitos

- [[wiki/concepts/fila]] / [[wiki/concepts/filas-e-workers]] — SQS é a implementação gerenciada AWS do padrão
- [[wiki/concepts/aws-sns]] — SNS costuma publicar num tópico consumido por múltiplas filas SQS em paralelo (fan-out)
- [[wiki/concepts/back-pressure]] — filas como mecanismo de absorção de picos, relacionado a controle de back-pressure
- [[wiki/concepts/amazon-s3]] — S3 Event Notifications podem mandar mensagem para uma fila SQS na deleção de um objeto

## Key Sources

- [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]] — Standard vs. FIFO, Dead Letter Queue, e a comparação de papéis SQS vs. SNS vs. EventBridge
