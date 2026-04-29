---
type: source
title: "K8s Autoscaling — HPA, VPA, KEDA, Karpenter"
aliases: ["k8s autoscaling", "hpa", "vpa", "keda", "karpenter", "node autoscaler"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/k8s-autoscaling.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [kubernetes, autoscaling, hpa, vpa, keda, karpenter, event-driven-autoscaling, node-autoscaling, finops]
skill: tech-mentor-infra
status: stable
---

## TL;DR

4 dimensões de autoscaling no K8s: HPA (pods por CPU/memória), VPA (tamanho do pod por historial), KEDA (pods por eventos externos — fila Kafka, SQS, cron), Karpenter (nodes por demanda de pods pendentes). KEDA permite scale-to-zero — pods = 0 quando idle, custo zero.

## Key Claims

**Claim:** KEDA é o autoscaler mais flexível — escala por qualquer fonte de eventos externos.
**Evidence:** Triggers: Kafka lag, SQS queue depth, Redis list length, Prometheus metric, HTTP request rate, cron schedule. Scale-to-zero: pods = 0 quando fila vazia. Essencial para workloads batch e event-driven.
**Confidence:** alta

**Claim:** HPA e VPA não devem ser usados juntos na mesma dimensão de CPU — conflito de recomendações.
**Evidence:** HPA escala número de pods. VPA escala CPU/memória por pod. Se ambos gerenciam CPU simultaneamente, VPA pode diminuir CPU do pod enquanto HPA adiciona mais pods, resultando em comportamento imprevisível.
**Confidence:** alta

**Claim:** Karpenter substitui Cluster Autoscaler com seleção de instância mais inteligente.
**Evidence:** Cluster Autoscaler: escala node groups existentes. Karpenter: cria nodes com o tipo exato necessário para os pods pendentes (Spot, On-Demand, família específica). 40–60% de economia em clusters com workloads variados.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/hpa]]
- [[concepts/vpa]]
- [[concepts/keda]]
- [[concepts/karpenter]]
- [[concepts/scale-to-zero]]
- [[concepts/finops]]

## Open Questions

- KEDA scale-to-zero com HPA: como gerenciar o "cold start" quando os primeiros pods demoram para inicializar?
- Karpenter com Spot instances: como configurar tolerations para evitar que workloads críticos landem em Spot?
