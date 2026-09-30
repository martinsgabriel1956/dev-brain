---
type: concept
title: "Dimensionamento para o Pico"
aliases: ["capacidade ociosa", "superestimar capacidade", "peak provisioning"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [capacidade, infraestrutura, cloud, elasticidade, custo]
skill: tech-mentor-infra
status: stub
---

# Dimensionamento para o Pico

Problema clássico da infraestrutura própria: a capacidade precisa atender o **pico** (ex.: Black Friday), mas na maior parte do tempo a demanda é bem menor (uma terça qualquer de agosto), então o excedente fica **ocioso** — "dinheiro parado", capital imobilizado ([[wiki/concepts/capex-vs-opex]]). Serviços elásticos ([[wiki/concepts/mainframe-as-a-service]], cloud pública) contratam capacidade com margem sobre o histórico e pagam pelo uso, transformando a ociosidade em economia operacional.

Relacionados: [[wiki/concepts/planejamento-de-capacidade]] (como dimensionar com dados) e [[wiki/concepts/finops]] (nota: gastar mais capacidade pode ser a decisão mais barata quando o pico gera receita). Sem números na fonte — o gráfico de MIPS é hipotético.

## Key Sources

- [[wiki/sources/mainframe-as-a-service-casas-bahia-sulamerica-kyndryl]] — capacidade para o pico × ociosidade, gráfico hipotético de MIPS
