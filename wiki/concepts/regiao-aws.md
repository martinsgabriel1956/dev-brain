---
type: concept
title: "Região AWS"
aliases: ["AWS Region", "Region", "Região Geográfica AWS"]
date_created: 2026-05-06
date_updated: 2026-05-06
source_count: 1
tags: ["aws", "infraestrutura", "região", "cloud"]
skill: tech-mentor-infra
status: stable
---

# Região AWS

Área geográfica independente que contém múltiplas [[zona-de-disponibilidade|Zonas de Disponibilidade]] fisicamente separadas. Cada região é completamente isolada das demais — falhas não se propagam entre regiões.

## Características

- Mínimo de **3 AZs** por região
- Isolamento total entre regiões (fault isolation boundary)
- Dados não replicam entre regiões sem configuração explícita
- Cada região tem um endpoint de serviço próprio (ex: `us-east-1`)

## Números Atuais (2025)

- **39 regiões** lançadas globalmente
- +2 regiões anunciadas: Arábia Saudita e Chile

## Distribuição por Continente

| Continente | Regiões |
|---|---|
| América do Norte | 9 |
| Europa | 8 |
| Ásia-Pacífico | 9+ |
| América do Sul | 1 (São Paulo) |
| Oriente Médio | 3 |
| África | 1 |
| Austrália e Nova Zelândia | 2 |

## Como Escolher uma Região

1. **Latência** — proximidade dos usuários finais
2. **Conformidade** — requisitos regulatórios (LGPD, GDPR, HIPAA)
3. **Disponibilidade de serviços** — nem todo serviço está em todas as regiões
4. **Custo** — preços variam por região (us-east-1 costuma ser o mais barato)

## Key Sources

- [[wiki/sources/aws-infraestrutura-global]]
