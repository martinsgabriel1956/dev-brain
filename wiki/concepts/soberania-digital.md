---
type: concept
title: "Soberania Digital"
aliases: ["Digital Sovereignty", "Residência de Dados", "Data Residency"]
date_created: 2026-05-06
date_updated: 2026-05-06
source_count: 1
tags: ["soberania-digital", "compliance", "regulação", "dados", "cloud"]
skill: tech-mentor-infra
status: stub
---

# Soberania Digital

Capacidade de uma organização ou governo de manter controle total sobre seus dados, aplicações e infraestrutura dentro de fronteiras nacionais ou jurisdicionais definidas. No contexto de cloud pública, implica garantir que dados não saiam de um território específico e que a infraestrutura esteja sujeita às leis locais.

## Dimensões

| Dimensão | Descrição |
|---|---|
| **Residência de dados** | Dados armazenados e processados apenas em território específico |
| **Portabilidade** | Capacidade de migrar dados sem dependência de fornecedor (vendor lock-in) |
| **Controle operacional** | Quem tem acesso ao hardware/software que processa os dados |
| **Conformidade regulatória** | Aderência a leis locais (LGPD, GDPR, CLOUD Act) |

## Soluções AWS para Soberania Digital

- **[[zona-local-dedicada|Dedicated Local Zones]]** — infraestrutura dedicada e isolada, operada pela AWS
- **[[aws-outposts|AWS Outposts]]** — hardware AWS dentro das instalações do cliente
- **AWS GovCloud** — regiões isoladas para governo dos EUA (FedRAMP/ITAR)
- **Controles de região** — políticas IAM que impedem workloads de cruzar fronteiras

## Regulações Relevantes

| Regulação | Jurisdição | Impacto |
|---|---|---|
| LGPD | Brasil | Dados de brasileiros devem ter proteção equivalente |
| GDPR | União Europeia | Transferência de dados fora da UE é restrita |
| CLOUD Act (EUA) | EUA | Governo americano pode exigir acesso a dados em provedores dos EUA |
| ITAR | EUA | Dados de defesa/armamento com controles rígidos |

## Tensão: Soberania vs. Escala Cloud

O modelo multi-tenant da cloud pública por natureza compartilha infraestrutura. Soberania plena exige isolamento que aumenta custo e reduz elasticidade — é um trade-off arquitetural explícito.

## Key Sources

- [[wiki/sources/aws-infraestrutura-global]]
