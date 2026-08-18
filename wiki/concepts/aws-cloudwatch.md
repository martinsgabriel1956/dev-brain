---
type: concept
title: "AWS CloudWatch"
aliases: ["CloudWatch", "Amazon CloudWatch"]
date_created: 2026-08-17
date_updated: 2026-08-17
source_count: 1
tags: ["aws", "cloudwatch", "observabilidade", "metricas", "logs", "alarmes", "x-ray", "infra", "cloud"]
skill: tech-mentor-infra
status: stub
---

# AWS CloudWatch

Hub de observabilidade nativo da AWS, baseado em três pilares: **métricas, logs e alarmes**. Serviços AWS publicam métricas automaticamente (CPU, latência, erros, número de requests); aplicações também podem publicar métricas customizadas.

## Logs e Retention

Logs vão para **Log Groups** — configurar a retention é importante, senão os logs acumulam indefinidamente e o custo cresce sem limite. **Logs Insights** permite pesquisar e agregar logs com uma query language própria.

## Alarmes

Monitoram métricas e disparam ações automaticamente. Exemplo clássico: CPU passa de 80% → alarme dispara → [[wiki/concepts/aws-sns|SNS]] notifica → [[wiki/concepts/auto-scaling|Auto Scaling Group]] escala.

## X-Ray — Tracing Distribuído

Cada request recebe um trace ID que mostra o caminho completo pela arquitetura (ex.: [[wiki/concepts/api-gateway|API Gateway]] → [[wiki/concepts/aws-lambda|Lambda]] → [[wiki/concepts/dynamodb|DynamoDB]]), permitindo identificar gargalos e erros por componente — equivalente AWS-nativo do conceito geral de tracing distribuído.

## Trade-offs vs. Stack de Observabilidade Própria

CloudWatch tem zero configuração para serviços AWS e integração nativa com alarmes/auto-scaling/dashboards, mas Logs Insights fica caro e lento em volumes altos, tem vendor lock-in e interface inferior a Grafana/Kibana. Estratégia híbrida comum: CloudWatch para métricas de infraestrutura AWS (automático), Prometheus+Grafana para métricas de aplicação, Loki/OpenSearch para logs de aplicação.

## Relação com outros conceitos

- [[wiki/concepts/observabilidade]] — CloudWatch é a implementação nativa AWS dos três pilares (métricas/logs/traces)
- [[wiki/concepts/aws-sns]] — canal mais comum de notificação de alarmes CloudWatch
- [[wiki/concepts/auto-scaling]] — alarmes CloudWatch são o gatilho mais comum de scaling actions

## Key Sources

- [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]] — três pilares (métricas/logs/alarmes), Log Groups + retention, Logs Insights, alarmes disparando SNS/Auto Scaling, e X-Ray como tracing distribuído
