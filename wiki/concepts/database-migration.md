---
type: concept
title: "Database Migration"
aliases: ["migration", "migrations", "migrate up", "migrate down", "migração de banco de dados"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [banco-de-dados, migrations, versionamento, orm, postgresql, git]
skill: tech-mentor-backend
status: draft
---

# Database Migration

Mudança controlada e versionada no schema de um banco de dados (criar tabela, adicionar coluna, alterar tipo, adicionar constraint), aplicada de forma reproduzível em vez de executada manualmente contra o banco.

## A Prática Considerada Errada

Executar DDL manualmente via SSH direto no banco (criar tabela, adicionar coluna, mudar tipo) — mesmo por quem administra o banco — não é revisável, auditável, reproduzível nem automatizável. Isso não significa nunca escrever um arquivo de migration manual; significa que qualquer arquivo/script de migration deve passar pelos mesmos processos do código: pull request, code review, e controle de versão (git). Ver [[wiki/concepts/code-review]]. Fonte: [[wiki/sources/database-migrations-sql-cru-vs-orm-drizzle]].

## Migrate Up / Migrate Down

Toda migração é pensada como um par:
- **up**: aplica a mudança (ex.: `ALTER TABLE users ADD COLUMN nascimento`)
- **down**: reverte exatamente o que o up fez (ex.: `ALTER TABLE users DROP COLUMN nascimento`)

Cada migração recebe um número sequencial de versão, e o próprio banco armazena internamente em qual versão está — permitindo migrar para cima ou para baixo de forma determinística. Um script `migrate` típico identifica a versão atual do banco e aplica só as migrations pendentes até a versão alvo (idempotente: reaplicar não repete migrations já marcadas como aplicadas).

## Duas Formas de Gerar Migrations

| Abordagem | Fluxo | Exemplo |
|---|---|---|
| **SQL cru** | Escreve-se a migration diretamente (arquivos numerados com up/down) | Scripts SQL versionados manualmente |
| **Via [[wiki/concepts/orm]]** | Declara-se o **estado final** desejado do schema em código; a ferramenta deriva a migration a partir do diff entre estado atual (journal/snapshot) e estado descrito | [[wiki/concepts/drizzle-orm|Drizzle]], Prisma Migrate |

Com ORM, na maioria dos casos não é preciso escrever migrations manualmente — mas quando o resultado gerado não é o esperado, ajuste manual do arquivo gerado continua sendo necessário.

## Riscos Mesmo com Ferramenta

Ter uma ORM gerando a migration não garante que ela é segura em escala: adicionar uma constraint de unicidade ou um campo derivado em uma tabela grande (ex.: ~100k+ linhas) pode causar lock prolongado e travar a tabela em produção. Testar em staging com dados similares aos de produção antes de aplicar em produção é necessário independentemente da ferramenta usada. Para o padrão que evita lock e permite convivência de duas versões do código durante a transição, ver [[wiki/concepts/expand-contract]].

## Relacionado

- [[wiki/concepts/orm]] — fluxo inverso de definição de estado final → migration derivada
- [[wiki/concepts/expand-contract]] — padrão de 3 fases para mudanças breaking sem downtime
- [[wiki/concepts/postgresql]] — engine usado nos exemplos práticos
- [[wiki/concepts/code-review]] — migrations tratadas com a mesma seriedade que código de aplicação
- [[wiki/concepts/checklist-primeiro-dia-projeto]] — migrations automáticas desde o primeiro deploy

## Key Sources

- [[wiki/sources/database-migrations-sql-cru-vs-orm-drizzle]]
- [[wiki/sources/migrations-schema-evolution]] — aprofunda zero-downtime, expand-contract e locks de DDL especificamente
