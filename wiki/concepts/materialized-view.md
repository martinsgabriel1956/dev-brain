---
type: concept
title: "Materialized View"
aliases: ["view materializada", "mv", "view com cache"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 1
tags: [banco-de-dados, sql, cache, performance, postgresql]
skill: tech-mentor-backend
status: stub
---

# Materialized View

View cujo resultado é persistido em disco (não recalculado a cada consulta), funcionando como uma camada de cache dentro do próprio banco. Diferente de uma view comum — que é só uma query salva, reexecutada a cada `SELECT` — a materialized view guarda o resultado e precisa ser atualizada explicitamente (`REFRESH MATERIALIZED VIEW` no PostgreSQL).

## Por Que Usar

Meio-termo entre extrair dado bruto repetidamente e cravar regra de negócio inteira em [[wiki/concepts/stored-procedure]]. Bom encaixe para agregações caras que não precisam de dado em tempo real (dashboards, relatórios).

## Trade-off

- ✅ Evita recalcular agregação pesada a cada request
- ✅ Mais simples de entender/depurar que lógica procedural
- ❌ Dado pode ficar desatualizado até o próximo refresh (staleness parecida com [[wiki/concepts/consistency-models|consistência eventual]])
- ❌ Refresh de MV grande pode ser custoso — avaliar `REFRESH ... CONCURRENTLY` no PostgreSQL

## Key Sources

- [[wiki/sources/orm-sql-organizacao-regras-negocio-bancos-dados]]
