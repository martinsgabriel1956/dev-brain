---
type: concept
title: "AWS Outposts"
aliases: ["Outposts", "AWS Outposts Rack", "AWS Outposts Server"]
date_created: 2026-05-06
date_updated: 2026-05-06
source_count: 1
tags: ["aws", "hybrid-cloud", "on-premises", "infraestrutura"]
skill: tech-mentor-infra
status: stub
---

# AWS Outposts

Rack ou servidor de hardware AWS instalado fisicamente no data center do cliente (on-premises). Roda os mesmos serviços, APIs e ferramentas da AWS — mas dentro da infraestrutura local da organização. É a solução da AWS para nuvem híbrida verdadeiramente consistente.

## Variantes

| Formato | Descrição |
|---|---|
| **Outposts Rack** | Rack completo 42U entregue e instalado pela AWS |
| **Outposts Servers** | Servidores individuais 1U/2U para espaços menores |

## Por que usar

- Requisitos regulatórios que proíbem dados fora das instalações
- Latência ultra-baixa para sistemas locais (fábricas, hospitais, telecom)
- Workloads que precisam de processamento local por conectividade limitada
- Migração gradual: manter parte dos workloads on-prem enquanto migra para cloud

## Como Funciona

```
Data center do cliente
└── Outposts Rack
    ├── EC2, ECS, EKS, RDS, ElastiCache (subconjunto)
    ├── Conectado à AWS Region via Direct Connect ou VPN
    └── Gerenciado remotamente pela AWS (hardware + software)
```

A AWS gerencia o hardware, patches de firmware e substituição de componentes. O cliente provisiona e usa serviços normalmente via console/CLI.

## Diferença: Outposts vs. Wavelength vs. Local Zone

| | Outposts | Local Zone | Wavelength |
|---|---|---|---|
| Onde fica | Data center do **cliente** | Data center **AWS** metropolitano | Rede da **operadora 5G** |
| Quem gerencia hardware | AWS | AWS | AWS |
| Conectividade req. | Direct Connect / VPN | Internet / AWS backbone | Rede 5G |
| Casos de uso | Compliance/latência local | Latência metropolitana | Latência móvel 5G |

## Key Sources

- [[wiki/sources/aws-infraestrutura-global]]
