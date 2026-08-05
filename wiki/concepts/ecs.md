---
type: concept
title: "Amazon ECS"
aliases: ["ECS", "Elastic Container Service"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 1
tags: ["aws", "ecs", "containers", "orquestracao", "docker", "infra", "cloud"]
skill: tech-mentor-infra
status: stub
---

# Amazon ECS (Elastic Container Service)

Serviço de orquestração de containers Docker da AWS, geralmente usado em cima de [[wiki/concepts/ec2]] (embora não seja obrigatório — também roda sobre [[wiki/concepts/aws-fargate]]). Em vez de subir e gerenciar instâncias EC2 manualmente uma a uma, o ECS permite deployar aplicações num **cluster** e simplifica escalar servidores/aplicações baseado em demanda.

## Por que existe

Uma única EC2 em produção é um single point of failure. O ECS resolve isso permitindo clusterização: múltiplas instâncias EC2 (ou tasks Fargate) rodando a mesma aplicação, com provisionamento de instâncias extras acompanhando a demanda — o que permite otimização de recursos (menos capacidade de madrugada, mais no pico).

## Contras

- Mais complexo de configurar do que rodar num único servidor grande.
- Escalar automaticamente também escala custo — se o tráfego explodir sem ser monetizado proporcionalmente, o custo cresce junto.
- [[wiki/concepts/vendor-lock-in-cloud|Vendor lock-in]]: mais um serviço proprietário da AWS a que a aplicação fica atrelada.

## Relação com outros conceitos

- [[wiki/concepts/ec2]] — infraestrutura subjacente mais comum do ECS
- [[wiki/concepts/aws-fargate]] — alternativa serverless para rodar tasks do ECS sem gerenciar EC2
- [[wiki/concepts/load-balancer]] — tipicamente distribui tráfego entre as tasks/instâncias do cluster ECS
- [[wiki/concepts/escalabilidade-horizontal]]

## Key Sources

- [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]]
