---
type: concept
title: "Hibernate ddl-auto=validate"
aliases: ["spring.jpa.hibernate.ddl-auto", "ddl-auto validate"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [hibernate, jpa, spring-boot, migrations, orm]
skill: tech-mentor-backend
status: draft
---

# Hibernate `ddl-auto=validate`

Propriedade `spring.jpa.hibernate.ddl-auto` do Spring Boot. Com `validate`, o Hibernate **só confere** se o schema do banco bate com as entidades; não cria nem altera nada. Quem cria e altera estruturas passa a ser o [[wiki/entities/flyway]] ([[wiki/concepts/database-migration]]).

## Divisão de responsabilidade

| Quem | Faz |
|---|---|
| Migrations (Flyway) | criam e evoluem tabelas e colunas, com histórico |
| Hibernate (`validate`) | falha na subida se entidade e banco divergirem |

A fonte resume: "tirar essa responsabilidade do Hibernate" e dar controle de versão ao banco. Um efeito útil (**inferência minha**): entidade com campo novo sem a migration correspondente falha na inicialização em vez de em runtime.

## Contexto

Valores como `create`/`update` deixam o [[wiki/concepts/orm]] gerar DDL sozinho, sem histórico revisável nem reprodutível, o oposto do que [[wiki/concepts/database-migration]] defende. Valores exatos e comportamento **[external, não verificados: https://docs.spring.io/spring-boot/how-to/data-initialization.html]**.

## Key sources

- [[wiki/sources/migrations-flyway-spring-boot-versionamento-de-banco]]
