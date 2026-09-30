---
type: concept
title: "CAPEX vs. OPEX"
aliases: ["capex", "opex", "capital imobilizado vs custo operacional"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [finops, capex, opex, cloud, custo, infraestrutura]
skill: tech-mentor-infra
status: stub
---

# CAPEX vs. OPEX

**CAPEX:** capital imobilizado em ativos (ex.: comprar e manter um mainframe/servidores dimensionados para o pico). **OPEX:** custo operacional recorrente (pagar por capacidade consumida como serviço). Terceirizar infra em modelo como [[wiki/concepts/mainframe-as-a-service]] ou cloud pública converte CAPEX em OPEX e elimina a capacidade ociosa paga antecipadamente ([[wiki/concepts/dimensionamento-para-o-pico]]).

Trade-off (skill [skill: tech-mentor-infra], `cloud/cloud-agnostic.md`): cloud não tem CapEx inicial, mas em workloads estáveis e grandes o break-even contra hardware próprio costuma ficar em 18–36 meses — OPEX não é automaticamente mais barato. Ver [[wiki/concepts/finops]]. A fonte não quantifica a economia.

## Key Sources

- [[wiki/sources/mainframe-as-a-service-casas-bahia-sulamerica-kyndryl]] — CAPEX imobilizado vira OPEX no modelo MaaS
