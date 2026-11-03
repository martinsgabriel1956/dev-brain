---
type: concept
title: "Kubernetes"
aliases: ["k8s", "orquestrador de contêineres"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_count: 1
tags: [kubernetes, conteineres, orquestracao, infra]
skill: tech-mentor-infra
status: stub
---

# Kubernetes

Orquestrador de contêineres: gerencia onde e como os contêineres rodam, cria réplicas para escalar horizontalmente, balanceia carga e centraliza configuração. Componentes de aplicação e de plataforma (coleta de métricas, API Gateway) podem rodar e ser gerenciados no mesmo lugar. [[wiki/sources/utilizar-ou-nao-kubernetes-fluxo-de-decisao-cloud]]

A fonte o trata como a principal ferramenta do mercado, mas **não como obrigatória**: ver [[wiki/concepts/conteineres-gerenciados-sem-kubernetes]]. Ele tem [[wiki/concepts/conteinerizacao]] como pré-requisito de estudo.

## Quando talvez não compense

Segundo a fonte: projeto que não precisa de tanta escalabilidade, de criticidade baixa (tolera downtime) ou que precisa de custo inicial baixo. Os critérios são qualitativos, sem número de corte. Ver [[wiki/concepts/criterios-de-adocao-de-servico-cloud]].

## Portabilidade

A fonte diz que Kubernetes evita lock-in porque todos os grandes provedores o oferecem. Na mesma frase, ela fala em portabilidade "mais fácil", que é a leitura mais segura. Inferência: a API é comum, mas identidade, ingress, storage e add-ons continuam específicos do provedor. Ver [[wiki/concepts/vendor-lock-in-cloud]].

## Key Sources

- [[wiki/sources/utilizar-ou-nao-kubernetes-fluxo-de-decisao-cloud]] — quando usar e quando não usar
- [[wiki/sources/kubernetes-core]] — Pods, Deployments, StatefulSets, probes e HPA
- [[wiki/sources/kubernetes-security]] — segurança em cinco camadas
- [[wiki/sources/k8s-autoscaling]] — autoscaling
