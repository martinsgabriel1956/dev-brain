---
type: concept
title: "AWS Elastic Beanstalk"
aliases: ["Elastic Beanstalk", "Beanstalk"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 1
tags: ["aws", "elastic-beanstalk", "paas", "infra", "cloud", "deploy"]
skill: tech-mentor-infra
status: stub
---

# AWS Elastic Beanstalk

Platform as a Service (PaaS) da AWS: permite deployar aplicações sem se preocupar diretamente com a infraestrutura — ele provisiona infra e escalabilidade automaticamente, mas continua permitindo customização (load balancers, [[wiki/concepts/ec2]], RDS, S3 por trás das cenas).

## Quando compensa

Para aplicações web relativamente simples (front-end + back-end, sem grande complexidade, em qualquer framework), tende a ter uma configuração mais simples e um custo mais atrativo do que orquestrar manualmente via [[wiki/concepts/ecs]] — porque aloca infraestrutura de forma mais próxima da necessidade real. Como a infra subjacente costuma ser EC2 (não necessariamente serverless), o custo tende a ficar baixo para aplicações de tráfego moderado.

## Contras

- [[wiki/concepts/vendor-lock-in-cloud|Vendor lock-in]]: migrar de Elastic Beanstalk para outra infra é difícil.
- Simples para o caso básico, mas casos de uso mais avançados adicionam complexidade de configuração significativa.
- Como [[wiki/concepts/aws-fargate]], tende a ser "caixa preta" — nem sempre fica claro o que deu certo ou errado por baixo do capô.

## Relação com outros conceitos

- [[wiki/concepts/ecs]] — alternativa com mais controle explícito sobre orquestração de containers
- [[wiki/concepts/ec2]] — infraestrutura subjacente mais comum do Beanstalk

## Key Sources

- [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]]
