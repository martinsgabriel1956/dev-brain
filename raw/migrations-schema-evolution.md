---
date: 2026-04-17
tags: [tech-mentor, banco, migrations, schema, postgresql]
skill: tech-mentor-backend/references/databases
level: intermediário
---

# Migrations e Schema Evolution

## Contexto
Migrations são a forma controlada e versionada de evoluir o schema do banco ao longo do tempo. O desafio real não é rodar uma migration — é fazer isso **sem downtime**, sem perda de dados, e de forma reversível em sistemas com múltiplas instâncias.

## Ferramentas

| Ferramenta | Linguagem | Melhor para |
|---|---|---|
| **Flyway** | Java + SQL | Controle total em SQL, multi-DB |
| **Liquibase** | XML/YAML/JSON/SQL | Changelog estruturado, rollback automático |
| **Alembic** | Python | SQLAlchemy — geração automática de diff |
| **Prisma Migrate** | TypeScript | DX excelente, integrado ao ORM |
| **golang-migrate** | Go | SQL puro, multi-driver |

## Flyway — Versionamento por Arquivo

```
db/migrations/
  V1__create_users_table.sql
  V2__add_email_index.sql
  V3__add_phone_column.sql
  R__refresh_analytics_view.sql   ← repeatable (re-executa se mudar)
```

```sql
-- V3__add_phone_column.sql
ALTER TABLE users ADD COLUMN phone TEXT;
-- Sem NOT NULL ainda — seria breaking change
-- NOT NULL vem após backfill (V4 ou V5)
```

## Prisma Migrate — DX para TypeScript

```typescript
// schema.prisma
model User {
  id        String   @id @default(uuid())
  email     String   @unique
  name      String
  phone     String?  // adicionado — nullable primeiro (Expand)
  createdAt DateTime @default(now()) @map("created_at")

  @@map("users")
}
```

```bash
# Gera SQL da migration e aplica
npx prisma migrate dev --name add_phone_to_users

# Em produção (sem interatividade)
npx prisma migrate deploy
```

## DDL sem Lock — Zero-Downtime Schema Changes

PostgreSQL bloqueia a tabela durante ALTER TABLE em algumas operações. Saber quais são seguras é crítico:

| Operação | Lock | Seguro em produção? |
|---|---|---|
| `ADD COLUMN` nullable sem default | AccessShare | ✅ Sim |
| `ADD COLUMN` com `DEFAULT` constante (PG 11+) | AccessShare | ✅ Sim |
| `ADD COLUMN NOT NULL` sem default | AccessExclusive | ❌ Bloqueia |
| `DROP COLUMN` | AccessExclusive | ⚠️ Rápido, mas bloqueia |
| `CREATE INDEX` | ShareLock | ❌ Bloqueia writes |
| `CREATE INDEX CONCURRENTLY` | nenhum exclusivo | ✅ Sim |
| `ADD CONSTRAINT CHECK` | AccessExclusive | ❌ Valida toda a tabela |
| `ADD CONSTRAINT CHECK NOT VALID` | ShareUpdateExclusive | ✅ Sim |

```sql
-- Adicionar índice sem bloquear writes
CREATE INDEX CONCURRENTLY idx_users_phone ON users (phone);

-- Adicionar constraint sem validar imediatamente
ALTER TABLE users ADD CONSTRAINT chk_phone_format
  CHECK (phone ~ '^\+[1-9]\d{1,14}$') NOT VALID;

-- Validar depois (em background, sem lock exclusivo)
ALTER TABLE users VALIDATE CONSTRAINT chk_phone_format;
```

## Expand-Contract no Banco — Fluxo Completo

```
1. Migration: ADD COLUMN full_name TEXT (nullable)
   App v2: escreve em name E full_name, lê full_name ?? name

2. Job de backfill:
   UPDATE users SET full_name = name WHERE full_name IS NULL LIMIT 1000;
   -- rodar em batches pequenos para não travar

3. Migration: ALTER COLUMN full_name SET NOT NULL
   (após backfill 100% e app v2 em produção)

4. Migration: DROP COLUMN name
   App v3: lê apenas full_name
```

## Database Testing

```typescript
// Testcontainers — banco real em testes
import { PostgreSqlContainer } from "@testcontainers/postgresql";

let container: StartedPostgreSqlContainer;

beforeAll(async () => {
  container = await new PostgreSqlContainer("postgres:16")
    .withDatabase("testdb")
    .start();

  // Rodar migrations no container de teste
  await runMigrations(container.getConnectionUri());
});

afterAll(async () => {
  await container.stop();
});

// Isolamento por teste via transaction rollback
beforeEach(async () => {
  await db.query("BEGIN");
});

afterEach(async () => {
  await db.query("ROLLBACK"); // descarta tudo — próximo teste começa limpo
});
```

## Conceitos Relacionados
[[postgresql-avancado]] · [[expand-contract]] · [[zero-downtime-deploy]] · [[postgresql-extensions]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-17*
