---
type: concept
title: "FinOps — Cost-Aware Architecture"
aliases: ["finops", "cloud cost", "unit economics", "cost optimization"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 1
tags: [finops, cloud-cost, unit-economics, right-sizing, spot-instances, egress, aws]
skill: tech-mentor-infra
status: stub
---

# FinOps

Prática de tratar custo de cloud como variável de engenharia — não só responsabilidade do financeiro.

**Métrica correta:** custo por unidade de negócio (por transação, por usuário ativo) — não custo absoluto. Crescer receita 2x com custo 1.5x é sucesso.

**Hierarquia de otimização:**
1. Arquitetura (maior impacto) — batch vs realtime, storage tier
2. Right-sizing — CPU/memória adequados ao workload real
3. Modelo de pricing — Reserved vs On-demand vs Spot
4. Otimizações pontuais (menor impacto)

**Batch vs Realtime:** maior decisão de custo — processar S3 em batch é 10–100x mais barato que stream.

**Egress:** o custo invisível mais subestimado — transferência entre AZs e para internet.

**Storage hierárquico:** Hot (S3) → Warm (S3 IA) → Cold (Glacier) economiza ~80% em dados raramente acessados.

**CI/CD:** Infracost integrado na pipeline mostra custo por PR antes do merge.

## Key Sources

- [[sources/finops-cost-aware-architecture]]
