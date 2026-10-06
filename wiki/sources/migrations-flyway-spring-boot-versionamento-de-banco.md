---
type: source
title: "Migrations com Flyway e Spring Boot: versionamento do banco de dados"
aliases: ["flyway spring boot", "migrations flyway", "o que são migrations"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/migrations-flyway-spring-boot-versionamento-de-banco.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-10-06
source_count: 0
tags: [migrations, flyway, spring-boot, java, postgresql, hibernate, versionamento, checksum]
skill: tech-mentor-backend
status: draft
---

# Migrations com Flyway e Spring Boot: versionamento do banco de dados

## TL;DR

Coluna criada à mão no banco local funciona, mas quebra em produção: ninguém a criou lá. A resposta são [[wiki/concepts/database-migration|migrations]]: scripts versionados que criam/alteram a estrutura do banco e guardam o histórico do que foi aplicado. No demo (Java 21, Spring Boot, Spring Data JPA, PostgreSQL), o [[wiki/entities/flyway]] lê `V<n>__descricao.sql` ([[wiki/concepts/convencao-de-nomes-flyway]]), roda só o que ainda não foi aplicado e registra tudo em [[wiki/concepts/flyway-schema-history]]. Migration já aplicada não se edita: o checksum quebra a subida ([[wiki/concepts/imutabilidade-de-migration]]); mudança nova vira script novo. O Hibernate fica só validando ([[wiki/concepts/hibernate-ddl-auto-validate]]), e o banco passa a ter controle de versão como o código, evitando o [[wiki/concepts/drift-de-schema-entre-ambientes]].

## Key claims

**Claim:** migrations são versões do banco em forma de scripts que criam tabelas/colunas, alteram a estrutura e mantêm histórico do que foi aplicado.
**Evidence:** definição do vídeo; coincide com [[wiki/concepts/database-migration]] e com a skill `[skill: tech-mentor-backend]` (Flyway: cada arquivo executa uma vez e nunca é modificado).
**Confidence:** alta.

**Claim:** alterar o banco manualmente (ex.: criar a coluna `cpf` pelo pgAdmin) é errado, porque o resto do time e os outros ambientes não terão a coluna.
**Evidence:** cenário do vídeo (local funciona, produção quebra; "o meu parceirinho não vai ter essa coluna"). Mesma tese de [[wiki/sources/database-migrations-sql-cru-vs-orm-drizzle]], com outro argumento (reprodutibilidade entre pessoas e ambientes, não só auditoria). Ver [[wiki/concepts/drift-de-schema-entre-ambientes]].
**Confidence:** alta.

**Claim:** basta adicionar o Flyway ao `pom.xml` para o Spring Boot executar os scripts de `db/migration` na inicialização; o prefixo `V<n>__` é obrigatório.
**Evidence:** demo com `V1__create_cliente.sql` (tabela `cliente`: `id BIGSERIAL`, `nome VARCHAR(250)`, `email VARCHAR(150)`) e `V2__cpf_cliente.sql` (`ALTER TABLE cliente ADD COLUMN cpf VARCHAR(11)`). Ver [[wiki/concepts/convencao-de-nomes-flyway]].
**Confidence:** alta. Ressalva `[skill: tech-mentor-backend]`: o vídeo fala em pasta "criada" pelo Flyway; o caminho padrão é `classpath:db/migration` e normalmente é o dev que cria a pasta (leitura minha; o áudio é ambíguo).

**Claim:** o Flyway registra cada execução na tabela `flyway_schema_history` e, ao reiniciar, não reaplica versões já registradas.
**Evidence:** reinício do servidor sem nenhum comando novo no banco; `SELECT` mostrando versão, tipo, descrição, checksum, instalado por, data/hora. Ver [[wiki/concepts/flyway-schema-history]].
**Confidence:** alta (observado no demo).

**Claim:** migration já aplicada não pode ser editada; o Flyway acusa erro de checksum e a mudança vira um script novo (V3, V4...).
**Evidence:** explicação do autor; o demo não mostra o erro acontecendo, só o descreve. Skill: `validate-on-migrate` faz a subida falhar se o checksum mudou. Ver [[wiki/concepts/imutabilidade-de-migration]].
**Confidence:** alta no mecanismo; erro não demonstrado no vídeo.

**Claim:** o Flyway garante (1) mesmo banco para todo o time, (2) dev/homologação/produção evoluindo igual, (3) alterações rastreáveis e "às vezes reversíveis".
**Evidence:** fecho do vídeo. A ressalva "às vezes" confere com a skill `[skill: tech-mentor-backend]`: o Flyway não tem rollback automático na edição comunitária (comparativo com Liquibase) **[external, não verificado: https://documentation.red-gate.com/flyway]**.
**Confidence:** média-alta; garantias valem enquanto ninguém mexer no banco fora das migrations.

**Claim:** a ideia final é tirar do Hibernate a responsabilidade de criar o schema a partir das entidades e dar ao banco um controle de versão.
**Evidence:** `ddl-auto=validate` na configuração do demo. Ver [[wiki/concepts/hibernate-ddl-auto-validate]] e [[wiki/concepts/orm]].
**Confidence:** alta.

## Entities & Concepts Touched

Entidades: [[wiki/entities/flyway]], [[wiki/entities/spring-boot]].

Conceitos novos: [[wiki/concepts/flyway-schema-history]], [[wiki/concepts/imutabilidade-de-migration]], [[wiki/concepts/convencao-de-nomes-flyway]], [[wiki/concepts/hibernate-ddl-auto-validate]], [[wiki/concepts/drift-de-schema-entre-ambientes]].

Conceitos existentes: [[wiki/concepts/database-migration]], [[wiki/concepts/schema-migration]], [[wiki/concepts/orm]], [[wiki/concepts/expand-contract]], [[wiki/concepts/postgresql]], [[wiki/concepts/ci-cd]], [[wiki/concepts/checklist-primeiro-dia-projeto]], [[wiki/concepts/drift-detection]], [[wiki/concepts/idempotencia]], [[wiki/concepts/code-review]], [[wiki/concepts/git]], [[wiki/concepts/database-branching]].

## Open questions

- Reversão: o autor diz "reversíveis às vezes" sem explicar como. Com Flyway, desfazer costuma ser outra migration "para frente" (ex.: `V5` que remove a coluna); o par up/down de [[wiki/concepts/database-migration]] é outro modelo. **Inferência minha**, a confirmar na doc oficial.
- Ficam de fora: lock em tabela grande e deploy com duas versões do código ([[wiki/concepts/expand-contract]]); migration que falha no meio (transação por script no Postgres vs. banco sem DDL transacional); duas pessoas criando a mesma `V3` em branches paralelas (conflito de versão); migrations em CI/CD e antes ou depois do deploy.
- Versão "Spring Boot 4.1.1" é leitura provável do áudio ("411").
- O vídeo não mostra o erro de checksum nem o `baseline` para banco legado já existente.

## Raw quotes

- "Migrations nada mais são do que versões do banco de dados em forma de scripts."
- "Uma migração aplicada não é um arquivo que a gente pode ficar editando. Ela virou parte do histórico do seu banco de dados."
- "A gente tire essa responsabilidade do Hibernate ... e passe a ter um controle de versão também pro banco de dados."
