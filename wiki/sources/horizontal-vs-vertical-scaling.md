---
type: source
title: "Horizontal vs Vertical Scaling"
aliases: []
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/horizontal-vs-vertical-scaling.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-22
source_count: 0
tags: [escalabilidade, scaling, stateless, auto-scaling, system-design]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

Vertical scaling é simples mas tem limite físico e gera SPOF. Horizontal scaling exige serviços stateless (estado em Redis/banco/S3), load balancer e atenção ao banco como novo gargalo. A ordem correta para banco: índices → cache → read replicas → vertical → connection pool → sharding. Comece sempre vertical; mude para horizontal quando disponibilidade ou limite de hardware exigirem.

## Claims Principais

| Claim | Confiança |
|---|---|
| Horizontal scaling é impossível sem serviços stateless — estado local não replica entre instâncias | Alta |
| Ordem correta para resolver gargalo de banco: índices → cache → réplicas → vertical → PgBouncer → sharding | Alta |
| Kubernetes HPA permite auto scaling horizontal baseado em CPU/memória | Alta |
| minReplicas: 2 é o mínimo para HA; nunca descer a zero para evitar cold start | Alta |
| Sharding é o último recurso, não a primeira solução | Alta |
| Deploy sem downtime exige scaling horizontal (rolling update) | Alta |

## Conceitos Abordados

- [[horizontal-scaling]]
- [[vertical-scaling]]
- [[stateless-service]]
- [[auto-scaling]]
- [[load-balancer]]
- [[connection-pooling]]
- [[db-sharding]]
