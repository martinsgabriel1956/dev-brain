---
type: concept
title: "AWS VPC (Virtual Private Cloud)"
aliases: ["VPC", "Virtual Private Cloud", "rede isolada AWS"]
date_created: 2026-08-17
date_updated: 2026-08-17
source_count: 1
tags: ["aws", "vpc", "rede", "subnet", "security-group", "infra", "cloud"]
skill: tech-mentor-infra
status: stub
---

# AWS VPC (Virtual Private Cloud)

Rede isolada dentro da AWS. Antes de subir qualquer serviço de computação ([[wiki/concepts/ec2|EC2]], [[wiki/concepts/ecs|ECS]], [[wiki/concepts/aws-lambda|Lambda]] em VPC), é preciso definir a VPC: um range de IPs, subnets, e controle de quem entra e sai. É o segundo passo lógico de uma pilha AWS, logo depois de configurar o [[wiki/concepts/aws-iam|IAM]].

## Subnets Públicas e Privadas

- **Pública** — tem rota para o Internet Gateway, recebe tráfego direto da internet.
- **Privada** — isolada, só sai pela internet via NAT Gateway (não recebe conexões de entrada não solicitadas).

## Security Groups

Firewalls no nível da instância: regras de entrada (inbound) e saída (outbound) definidas explicitamente. Diferente de uma ACL de rede (nível de subnet), o Security Group opera por instância/recurso.

## Arquitetura Típica de Três Camadas

```
Internet
  └── Load Balancer (subnet pública)
        └── Aplicação (subnet privada)
              └── Banco de dados (subnet privada, ainda mais isolada)
```

Três camadas de defesa: cada camada só é alcançável pela camada imediatamente anterior, nunca diretamente da internet (exceto o load balancer).

## Relação com outros conceitos

- [[wiki/concepts/aws-iam]] — controla quem pode fazer o quê; VPC controla o que pode se conectar a quê na rede
- [[wiki/concepts/load-balancer]] — tipicamente vive na subnet pública, distribuindo tráfego para a aplicação na subnet privada
- [[wiki/concepts/ec2]] — instâncias rodam dentro de subnets da VPC

## Key Sources

- [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]] — subnets públicas/privadas, Security Groups, e a arquitetura de três camadas (LB público → app privada → banco ainda mais isolado)
