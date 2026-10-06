---
type: concept
title: "Flyway Schema History"
aliases: ["flyway_schema_history", "tabela de histórico do Flyway"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [flyway, migrations, controle-de-versao, postgresql]
skill: tech-mentor-backend
status: draft
---

# Flyway Schema History

Tabela `flyway_schema_history`, criada pelo [[wiki/entities/flyway]] no próprio banco. É o registro do que já foi executado: a cada subida da aplicação, o Flyway compara os scripts do projeto com ela e roda só os pendentes.

## Conteúdo

No demo de [[wiki/sources/migrations-flyway-spring-boot-versionamento-de-banco]]: versão, tipo (SQL), descrição (ex.: "create cliente"), **checksum**, quem instalou (usuário `postgres`) e data/hora. `[skill: tech-mentor-backend]` acrescenta `script` e `success`.

## Por que importa

- Reiniciar o servidor não reaplica nada: o banco "sabe" em que versão está (parecido com o contador de versão de [[wiki/concepts/database-migration]]).
- O checksum guardado ali é o que detecta edição de script já aplicado: [[wiki/concepts/imutabilidade-de-migration]].
- O estado do schema fica **dentro do banco**, então cada ambiente carrega o seu próprio histórico. Isso sustenta a promessa de ambientes evoluindo igual e ajuda a combater o [[wiki/concepts/drift-de-schema-entre-ambientes]].

## Key sources

- [[wiki/sources/migrations-flyway-spring-boot-versionamento-de-banco]]
