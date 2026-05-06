---
type: concept
title: "Zona de Disponibilidade"
aliases: ["AZ", "Availability Zone", "Zona de Disponibilidade AWS"]
date_created: 2026-05-06
date_updated: 2026-05-06
source_count: 1
tags: ["aws", "infraestrutura", "alta-disponibilidade", "resiliência"]
skill: tech-mentor-infra
status: stable
---

# Zona de Disponibilidade (AZ)

Data center (ou cluster de data centers) fisicamente isolado dentro de uma [[regiao-aws|Região AWS]]. AZs são interconectadas por links de fibra dedicados de baixa latência, alta capacidade e totalmente redundantes.

## Características

- Energia, resfriamento e rede **completamente independentes** entre AZs
- Interconectadas com latência **< 2ms** entre si (dentro da mesma região)
- Mínimo de **3 AZs por região** — falha de uma AZ não derruba a região
- Identificadas por sufixo: `us-east-1a`, `us-east-1b`, `us-east-1c`

## Números Atuais (2025)

- **123 AZs** globalmente
- +7 AZs anunciadas

## Padrão de Uso para Alta Disponibilidade

```
Região us-east-1
├── AZ us-east-1a  →  instância primária + RDS primary
├── AZ us-east-1b  →  instância standby + RDS replica
└── AZ us-east-1c  →  instância standby + RDS replica
```

Multi-AZ é o padrão mínimo para workloads de produção. Permite:
- Failover automático em caso de falha de hardware
- Manutenção sem downtime (rolling updates por AZ)
- SLAs de disponibilidade acima de 99,99%

## Diferença: AZ vs. Região

| | AZ | Região |
|---|---|---|
| Escopo | Data center(s) | Múltiplas AZs |
| Isolamento | Energia/rede independentes | Geograficamente isoladas |
| Latência intra | < 2ms | Dezenas de ms |
| Failover | Automático (Multi-AZ) | Manual (multi-region) |

## Key Sources

- [[wiki/sources/aws-infraestrutura-global]]
