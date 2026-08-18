---
type: concept
title: "AWS Fargate"
aliases: ["Fargate"]
date_created: 2026-08-04
date_updated: 2026-08-17
source_count: 2
tags: ["aws", "fargate", "serverless", "containers", "infra", "cloud"]
skill: tech-mentor-infra
status: stub
---

# AWS Fargate

Serverless compute engine para containers na AWS — elimina a necessidade de provisionar, configurar ou escalar clusters, ou de lidar diretamente com máquinas virtuais e instâncias [[wiki/concepts/ec2]]. Você define e deploya containers; a AWS cuida de infraestrutura, escalabilidade e patching por baixo. Geralmente usado junto com [[wiki/concepts/ecs]] (ou EKS) como o modo de execução das tasks.

## Prós

- Reduz complexidade operacional — não há EC2 para gerenciar diretamente.
- Custo escala com uso/demanda real, não com capacidade pré-alocada.

## Contras

- Custo pode ficar elevado dependendo do workload — para volumes altos e previsíveis, [[wiki/concepts/ec2]] tradicional ou [[wiki/concepts/aws-lambda]] podem sair mais baratos.
- Como todo serviço serverless gerenciado, é relativamente "caixa preta": mais difícil de depurar o que está acontecendo por baixo do capô do que uma EC2 que você administra diretamente.

## Relação com outros conceitos

- [[wiki/concepts/ecs]] — orquestrador mais comum que roda tasks sobre Fargate
- [[wiki/concepts/ec2]] — alternativa não-serverless (mais controle, potencialmente mais barato em alta utilização constante)
- [[wiki/concepts/aws-lambda]] — outra forma serverless de compute na AWS, unidade de função em vez de container

## Fargate como Launch Type do ECS

Um dos dois launch types do [[wiki/concepts/ecs|ECS]] (o outro é EC2 gerenciado diretamente). Fargate é o mais simples dos dois; EC2 faz sentido quando o workload precisa de GPU ou controle mais fino sobre a instância subjacente. Ver [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]].

## Key Sources

- [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]]
- [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]] — Fargate como o mais simples dos dois launch types do ECS, EC2 reservado para GPU/controle fino
