---
type: concept
title: "AWS SNS (Simple Notification Service)"
aliases: ["SNS", "Simple Notification Service", "pub/sub AWS"]
date_created: 2026-08-17
date_updated: 2026-08-17
source_count: 1
tags: ["aws", "sns", "pub-sub", "fan-out", "mensageria", "infra", "cloud"]
skill: tech-mentor-infra
status: stub
---

# AWS SNS (Simple Notification Service)

Serviço pub/sub gerenciado da AWS: você publica num tópico, e todos os inscritos recebem a mensagem — instância concreta do padrão [[wiki/concepts/pub-sub|Pub/Sub]]. Diferença central para [[wiki/concepts/aws-sqs|SQS]]: SQS entrega para um consumidor por mensagem, SNS entrega para todos os inscritos (fan-out).

## Padrão Mais Comum: Fan-out para Múltiplas Filas SQS

SNS publica num tópico, e múltiplas filas SQS estão inscritas nesse tópico — cada fila processa de forma independente e em paralelo. Permite que vários sistemas reajam ao mesmo evento sem acoplamento direto entre eles.

## Relação com outros conceitos

- [[wiki/concepts/pub-sub]] — SNS é a implementação gerenciada AWS do padrão publish-subscribe
- [[wiki/concepts/aws-sqs]] — combinação típica: SNS publica, múltiplas filas SQS consomem em paralelo
- [[wiki/concepts/aws-cloudwatch]] — alarmes do CloudWatch tipicamente notificam via SNS (ex.: CPU > 80% dispara alarme → SNS notifica → Auto Scaling escala)

## Key Sources

- [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]] — diferença SQS (um consumidor) vs. SNS (fan-out), padrão de múltiplas filas SQS inscritas no mesmo tópico, e SNS como canal de notificação de alarmes CloudWatch
