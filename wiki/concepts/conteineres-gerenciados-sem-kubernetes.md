---
type: concept
title: "Contêineres Gerenciados sem Kubernetes"
aliases: ["serverless containers", "contêineres serverless", "azure container apps", "cloud run"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_count: 1
tags: [conteineres, serverless, cloud, infra]
skill: tech-mentor-infra
status: stub
---

# Contêineres Gerenciados sem Kubernetes

Serviços em que o provedor executa o contêiner sem que o time opere um cluster. É o meio-termo que a fonte recomenda para quem quer contêineres, mas ainda não conhece [[wiki/concepts/kubernetes]]; no fluxograma do Azure, é onde termina o caminho: Azure Container Apps. [[wiki/sources/utilizar-ou-nao-kubernetes-fluxo-de-decisao-cloud]]

A fonte afirma que todos os grandes provedores têm um serviço assim, mas a transcrição não nomeia os equivalentes.

## Equivalentes

`[skill: tech-mentor-infra]` (`containers/serverless-containers.md`):

| Serviço | Escala a zero | Observação |
|---|---|---|
| Azure Container Apps | sim, com KEDA | camada sobre K8s, sem expor K8s; Dapr integrado |
| Google Cloud Run | sim | cobrança por request; concorrência por instância |
| [[wiki/concepts/aws-fargate]] sobre [[wiki/concepts/ecs]] | não (mínimo de 1 task) | cerca de 20–30% mais caro que EC2 equivalente |

## Trade-off

Menos operação em troca de mais [[wiki/concepts/vendor-lock-in-cloud|lock-in]]. Segundo a fonte, migrar não é tão transparente quanto entre Kubernetes, mas "não vai ser um mistério", porque o contêiner continua portável.

## Key Sources

- [[wiki/sources/utilizar-ou-nao-kubernetes-fluxo-de-decisao-cloud]]
