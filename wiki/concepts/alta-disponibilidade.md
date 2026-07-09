---
type: concept
title: "Alta Disponibilidade"
aliases: ["HA", "High Availability", "Alta Disponibilidade Cloud"]
date_created: 2026-05-06
date_updated: 2026-07-09
source_count: 2
tags: ["alta-disponibilidade", "resiliência", "aws", "arquitetura", "sre"]
skill: tech-mentor-infra
status: stub
---

# Alta Disponibilidade (HA)

Propriedade de um sistema de permanecer operacional por uma porcentagem definida do tempo, mesmo diante de falhas de componentes. Em cloud, é implementada através de redundância geográfica em múltiplas [[zona-de-disponibilidade|AZs]] e [[regiao-aws|Regiões]].

## Níveis de Disponibilidade AWS

| Nível | Abordagem | Downtime/ano |
|---|---|---|
| Single AZ | Sem redundância | Sem SLA |
| Multi-AZ | 2-3 AZs na mesma região | ~4 min (99,999%) |
| Multi-Region | Regiões distintas | Segundos (99,9999%+) |

## Padrão Multi-AZ (mínimo para produção)

```
Load Balancer (Regional)
├── AZ-a: App + DB primary
├── AZ-b: App + DB standby (failover automático)
└── AZ-c: App + DB standby (failover automático)
```

Serviços gerenciados da AWS (RDS Multi-AZ, Aurora, ElastiCache) fazem o failover automaticamente em < 60s.

## HA vs. Disaster Recovery (DR)

| | Alta Disponibilidade | Disaster Recovery |
|---|---|---|
| Escopo | Falha de componente/AZ | Falha de região inteira |
| RTO | Segundos a minutos | Minutos a horas |
| Custo | Moderado (2-3x por AZ) | Alto (infra duplicada em 2ª região) |
| Automação | Automático (gerenciado) | Geralmente manual ou semi-auto |

## Relação com a Infraestrutura AWS

O design com mínimo de **3 AZs por região** existe especificamente para suportar HA: qualquer serviço que distribua carga entre as 3 AZs sobrevive à perda de 1 AZ sem impacto no SLA.

## Key Sources

- [[wiki/sources/aws-infraestrutura-global]]
- [[wiki/sources/10-conceitos-fundamentais-backend]] — framing didático agnóstico de cloud: disponibilidade como "continuar rodando mesmo quando acontecem falhas", via load balancer que não manda tráfego a instância travada e deploy que não derruba todas as máquinas ao mesmo tempo
