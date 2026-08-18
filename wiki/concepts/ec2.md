---
type: concept
title: "Amazon EC2"
aliases: ["EC2", "Elastic Compute Cloud"]
date_created: 2026-08-04
date_updated: 2026-08-17
source_count: 2
tags: ["aws", "ec2", "compute", "servidor", "infra", "cloud"]
skill: tech-mentor-infra
status: stub
---

# Amazon EC2 (Elastic Compute Cloud)

Building block básico de computação da AWS: uma instância de servidor (máquina virtual) de tamanho e especificação escolhidos pelo usuário. Usado no sentido amplo de "servidor" — web ou não, incluindo processamento em background. Outros serviços de compute mais gerenciados da AWS ([[wiki/concepts/ecs]], [[wiki/concepts/aws-fargate]], [[wiki/concepts/elastic-beanstalk]]) se apoiam em EC2 por baixo (ou existem como alternativa a ele).

## Modelo de custo

Cobra pelo **tempo de máquina alocada**, não pela computação de fato realizada — uma instância ociosa custa o mesmo que uma sob carga máxima. Esse é o contraste central com [[wiki/concepts/aws-lambda]], que cobra por invocação/tempo de execução.

- Vantagem: uso intenso e constante da máquina paga exatamente pelo que foi alugado.
- Desvantagem: capacidade ociosa (madrugada, baixo tráfego) é desperdício de custo, a não ser que haja algum mecanismo de scaling em cima da instância.

## Por que raramente se roda uma única EC2 em produção

Uma única instância é um single point of failure — se ela cai, cai o tráfego todo. Por isso EC2 costuma aparecer atrás de orquestração ([[wiki/concepts/ecs]]) e de um [[wiki/concepts/load-balancer]], formando um cluster.

## Relação com outros conceitos

- [[wiki/concepts/ecs]] — orquestra clusters de EC2
- [[wiki/concepts/aws-fargate]] — alternativa serverless a gerenciar EC2 diretamente
- [[wiki/concepts/elastic-beanstalk]] — PaaS que provisiona EC2 por trás das cenas
- [[wiki/concepts/load-balancer]] — distribui tráfego entre múltiplas EC2
- [[wiki/concepts/escalabilidade-horizontal]]

## Famílias de Instância e Modelos de Preço

Famílias mais comuns: **T** (workload variável, dev/teste), **M** (uso geral em produção), **C** (computação pesada), **R** (memória intensiva). Três modelos de preço, cada um para um perfil de carga diferente:
- **On-Demand** — paga pelo uso, sem compromisso, mais caro.
- **Reserved** — compromisso de 1-3 anos, desconto até 70%. Ideal para produção estável.
- **Spot** — usa capacidade ociosa, desconto até 90%, mas pode ser interrompido a qualquer momento. Ideal para batch/workloads tolerantes a interrupção.

Regra prática: produção estável em Reserved, picos em On-Demand, batch em Spot. Armazenamento em bloco (EBS): GP3 para a maioria dos casos, io2 quando IOPS garantido é necessário (bancos exigentes). Ver [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]].

## Key Sources

- [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]]
- [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]] — famílias de instância (T/M/C/R) e os três modelos de preço com regra de uso por perfil de carga
