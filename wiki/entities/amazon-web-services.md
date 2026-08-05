---
type: entity
title: "Amazon Web Services"
aliases: ["AWS", "Amazon Cloud"]
date_created: 2026-05-06
date_updated: 2026-08-04
source_count: 2
tags: ["aws", "cloud-provider", "amazon", "infraestrutura"]
skill: tech-mentor-infra
status: stable
---

# Amazon Web Services (AWS)

Divisão de computação em nuvem da Amazon.com. Maior provedor de infraestrutura cloud do mundo por receita e abrangência geográfica. Lançado publicamente em 2006 com S3 e EC2.

## Infraestrutura Global (2025)

- 39 regiões geográficas · 123 AZs · 750+ POPs CloudFront
- Backbone privado de fibra óptica: 9+ milhões de km
- Ver: [[wiki/sources/aws-infraestrutura-global]]

## Principais Produtos por Categoria

| Categoria | Serviços |
|---|---|
| Compute | EC2, Lambda, ECS, EKS, Fargate |
| Storage | S3, EBS, EFS, Glacier |
| Database | RDS, Aurora, DynamoDB, ElastiCache |
| Rede | VPC, CloudFront, Route 53, Direct Connect |
| Edge | Local Zones, Wavelength, Outposts |
| Segurança | IAM, GuardDuty, Security Hub, WAF |

## Conceitos de Infraestrutura

- [[regiao-aws]] — unidades geográficas de deploy
- [[zona-de-disponibilidade]] — data centers isolados por região
- [[zona-local-aws]] — extensões metropolitanas de baixa latência
- [[aws-wavelength]] — edge embutido em redes 5G
- [[aws-outposts]] — hardware AWS on-premises
- [[zona-local-dedicada]] — infraestrutura dedicada para soberania digital
- [[aws-cloudfront]] — CDN global
- [[backbone-de-rede-aws]] — rede privada de fibra global

## IAM

Serviço de identidade e controle de acesso. Ver [[aws-iam]].

## Toolkit Essencial (Compute, Deploy, Dados)

Cobertura de "80/20" dos serviços mais usados na prática para aplicações web escaláveis, sem entrar no console:

| Categoria | Serviços |
|---|---|
| Compute | [[wiki/concepts/ec2]], [[wiki/concepts/aws-fargate]], [[wiki/concepts/aws-lambda]] |
| Orquestração/Deploy | [[wiki/concepts/ecs]], [[wiki/concepts/elastic-beanstalk]] |
| Roteamento | [[wiki/concepts/load-balancer|ALB]], [[wiki/concepts/api-gateway]] |
| Workflow | [[wiki/concepts/step-functions]] |
| Dados | [[wiki/concepts/rds]], [[wiki/concepts/dynamodb]] |
| Storage | [[wiki/concepts/amazon-s3]] |

Tema recorrente: [[wiki/concepts/vendor-lock-in-cloud]] — quanto mais desses serviços proprietários um sistema adota, mais caro fica migrar depois. Ver [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]].

## Key Sources

- [[wiki/sources/aws-infraestrutura-global]]
- [[wiki/sources/iam-introduction-users-groups-policies]]
- [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]]
