---
type: concept
title: "Drift de Schema entre Ambientes"
aliases: ["funciona na minha máquina banco", "schema divergente", "alteração manual no banco"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [migrations, banco-de-dados, ambientes, reprodutibilidade]
skill: tech-mentor-backend
status: draft
---

# Drift de Schema entre Ambientes

Quando o banco de um ambiente (ou de uma pessoa) tem estrutura diferente do outro porque alguém mudou o schema manualmente. Cenário da fonte: coluna criada no banco local, código funciona, **produção quebra** porque a coluna não existe lá; o colega também não a tem.

## Causa e remédio

- **Causa:** DDL executado direto no banco, fora do código versionado.
- **Remédio:** toda mudança vira script versionado ([[wiki/concepts/database-migration]]), aplicado igual em dev, homologação e produção por ferramenta como o [[wiki/entities/flyway]], com histórico em [[wiki/concepts/flyway-schema-history]].
- **Guarda-corpo:** [[wiki/concepts/imutabilidade-de-migration]] impede divergência por edição de script antigo.

## Relação com outros conceitos

Mesma família de [[wiki/concepts/drift-detection]] (infra descrita vs. real) e do problema de [[wiki/concepts/reprodutibilidade-de-bugs]] por ambientes diferentes. Também é o "ambiente criado à mão" que [[wiki/concepts/ci-cd]] tenta eliminar. Ligações **inferência minha**.

## Key sources

- [[wiki/sources/migrations-flyway-spring-boot-versionamento-de-banco]]
