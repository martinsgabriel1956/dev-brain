---
type: concept
title: "Materialized View"
aliases: ["view materializada", "mv", "view com cache"]
date_created: 2026-07-03
date_updated: 2026-08-27
source_count: 2
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

## Como "CQRS-Like": Resolve Modelo, Não Volume

[[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]] usa materialized views (comando faz `UPDATE` na tabela, leitura faz `SELECT` na view) como a forma mais simples de separar comando e consulta dentro de [[wiki/concepts/cqrs]] sem trocar de banco de dados — mas classifica isso como "CQRS-like", não CQRS pleno: como tabela e view compartilham a mesma base física, o gargalo de banco permanece, então essa técnica resolve a divergência de **modelo** mas não a de **volume** (escalar a escrita ainda impacta a leitura).

## Key Sources

- [[wiki/sources/orm-sql-organizacao-regras-negocio-bancos-dados]]
- [[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]] — materialized views como opção de consistência forte no CQRS, classificada como "CQRS-like": resolve modelo, não resolve volume
