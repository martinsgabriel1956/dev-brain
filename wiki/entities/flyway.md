---
type: entity
title: "Flyway"
aliases: ["Flyway Migration", "flywaydb"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [flyway, migrations, java, spring-boot, banco-de-dados]
skill: tech-mentor-backend
status: stub
---

# Flyway

Ferramenta de [[wiki/concepts/database-migration|migrations]] de banco de dados, muito usada no ecossistema Java/JVM e integrada ao [[wiki/entities/spring-boot]] (adicionar a dependência já faz a aplicação executar os scripts de `db/migration` na subida). Escolha declarada do autor em [[wiki/sources/migrations-flyway-spring-boot-versionamento-de-banco]], que a usa no dia a dia.

## Como funciona (segundo a fonte)

- Scripts SQL nomeados `V<n>__descricao.sql`: [[wiki/concepts/convencao-de-nomes-flyway]].
- Executa só o que ainda não foi aplicado e registra tudo em [[wiki/concepts/flyway-schema-history]].
- Compara checksums: script aplicado e editado derruba a subida ([[wiki/concepts/imutabilidade-de-migration]]).
- Convive com o Hibernate em modo de validação: [[wiki/concepts/hibernate-ddl-auto-validate]].

## Contraste com Liquibase `[skill: tech-mentor-backend]`

Flyway: SQL puro, simples, rollback só na edição paga. Liquibase: changelogs XML/YAML/JSON/SQL, rollback declarável, mais agnóstico de banco e mais complexo. Ambos têm auto-configuração no Spring Boot. **[external, não verificado nesta sessão]**

## Key sources

- [[wiki/sources/migrations-flyway-spring-boot-versionamento-de-banco]]
