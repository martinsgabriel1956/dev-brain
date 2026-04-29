---
type: source
title: "FinOps e Cost-Aware Architecture"
aliases: ["finops", "unit economics", "right-sizing", "spot instances", "egress cost"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 0
tags: [finops, cloud-cost, unit-economics, right-sizing, spot-instances, storage-tiering, egress, aws]
skill: tech-mentor-infra
status: draft
source_file: /home/nemomartins/Documentos/new/dev-study/raw/finops-cost-aware-architecture.md
source_url:
author:
date_published:
date_ingested: 2026-04-23
---

# FinOps e Cost-Aware Architecture

## TL;DR

FinOps é a prática de tornar custo de cloud uma variável de engenharia, não só de financeiro. Métrica correta: custo por unidade de negócio (por transação, por usuário ativo), não custo absoluto. Hierarquia: arquitetura > right-sizing > pricing model > otimização pontual. Batch vs Realtime é a decisão de maior impacto de custo. Egress é o custo invisível mais subestimado.

## Key Claims

| Claim | Evidência |
|---|---|
| Superprovisionamento por medo é o desperdício mais comum | CPU média < 20% → downsizing possível |
| Custo por unidade de negócio é a métrica correta, não custo absoluto | Crescer receita 2x com custo 1.5x é sucesso, não falha |
| Batch vs Realtime é a decisão de maior impacto de custo | Processar S3 em batch custa 10–100x menos que stream |
| Egress é o custo mais subestimado — transferência entre AZs e para internet | Arquitetura cross-AZ gera egress silencioso |
| Storage hierárquico (S3 → Glacier) economiza ~80% em dados frios | 90% do volume, <5% do tráfego |
| FinOps no CI/CD: custo por PR visível antes do merge | Infracost integrado na pipeline |

## Conceitos

- [[concepts/finops]] — disciplina de custo como engenharia
- [[concepts/unit-economics]] — custo por unidade de negócio
- [[concepts/storage-tiering]] — Hot/Warm/Cold já documentado
- [[concepts/right-sizing]] — dimensionamento adequado de instâncias
- [[concepts/spot-instances]] — arquitetura spot-aware para workloads tolerantes a interrupção

## Key Sources

_Este é o documento primário._
