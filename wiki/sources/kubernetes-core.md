---
type: source
title: "Kubernetes Core"
aliases: ["kubernetes", "k8s core", "pod", "deployment", "statefulset", "rbac", "probes"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/kubernetes-core.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [kubernetes, pod, deployment, statefulset, rbac, probes, liveness, readiness, configmap, secret, hpa]
skill: tech-mentor-infra
status: stable
---

## TL;DR

Kubernetes orquestra containers em Pods. Deployment para workloads stateless (rolling update). StatefulSet para workloads com estado (banco, Kafka). RBAC para controle de acesso. Probes (liveness, readiness, startup) para health checks. HPA para autoscaling por CPU/memória. Regra de ouro: Secrets via ExternalSecrets ou Vault, nunca hardcoded.

## Key Claims

**Claim:** Readiness Probe determina quando o Pod recebe tráfego — diferente de Liveness (quando reiniciar).
**Evidence:** Readiness failing = Pod removido do Service endpoints (sem tráfego). Liveness failing = Pod reiniciado. Startup Probe evita que liveness/readiness "matem" Pods durante startup lento. Configurar os três para zero downtime deploy.
**Confidence:** alta

**Claim:** StatefulSet garante identidade estável e ordem de inicialização para workloads com estado.
**Evidence:** Pods têm nomes previsíveis (pod-0, pod-1). PersistentVolumeClaims persistem após reinício. Inicialização/terminação em ordem (pod-0 antes de pod-1). Necessário para: Kafka, Zookeeper, PostgreSQL em K8s.
**Confidence:** alta

**Claim:** RBAC principle of least privilege: ServiceAccount por workload com apenas as permissões necessárias.
**Evidence:** Pod com ServiceAccount padrão = acesso a todos os secrets do namespace. ServiceAccount dedicado + Role com permissões específicas = blast radius controlado se o pod for comprometido.
**Confidence:** alta

**Claim:** Kubernetes é over-engineering para projetos pequenos — Docker Compose + VM é suficiente até ~10 serviços.
**Evidence:** K8s overhead: 3 master nodes, etcd, networking complexo, curva de aprendizado alta. Benefícios (autoscaling, self-healing, rolling updates) só se pagam com escala real. ECS Fargate ou App Runner são alternativas mais simples no AWS.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/kubernetes]]
- [[concepts/statefulset]]
- [[concepts/rbac-k8s]]
- [[concepts/health-probes]]
- [[concepts/hpa]]

## Open Questions

- Pod Disruption Budget — como configurar para garantir disponibilidade mínima durante node drains?
- Como fazer rolling update sem downtime quando o container tem startup lento (> 60s)?
