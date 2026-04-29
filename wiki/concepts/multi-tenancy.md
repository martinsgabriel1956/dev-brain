---
type: concept
title: "Multi-tenancy"
aliases: ["multi-tenancy", "multitenancy", "tenant isolation", "saas isolation"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, saas, isolamento, postgresql, rls, gdpr, migrations, arquitetura]
skill: tech-mentor-system-design
status: stable
---

# Multi-tenancy

Modelo onde múltiplos clientes (tenants) compartilham a mesma infraestrutura. Padrão de SaaS. A escolha do modelo de isolamento é irreversível no curto prazo — errar cedo = migração de meses.

## Os 3 Modelos

### 1. Shared Database, Shared Schema

Todos os tenants no mesmo banco e schema. Separação por coluna `tenant_id`.

```sql
CREATE TABLE orders (
  id         UUID PRIMARY KEY,
  tenant_id  UUID NOT NULL REFERENCES tenants(id),
  amount     DECIMAL(10,2),
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Index composto obrigatório — sem ele, queries por tenant fazem full scan
CREATE INDEX idx_orders_tenant ON orders(tenant_id, created_at DESC);

-- RLS: segunda linha de defesa contra bug de isolamento na aplicação
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_isolation ON orders
  USING (tenant_id = current_setting('app.current_tenant_id')::UUID);
```

### 2. Shared Database, Schema-per-Tenant

Mesmo banco físico, schema PostgreSQL por tenant.

```sql
CREATE SCHEMA tenant_acme;
CREATE TABLE tenant_acme.orders (id UUID PRIMARY KEY, amount DECIMAL(10,2), created_at TIMESTAMPTZ);
-- sem tenant_id — schema é o isolamento
```

```typescript
function getConnectionForTenant(tenantId: string) {
  if (!connectionPools.has(tenantId)) {
    connectionPools.set(tenantId, createPool({ searchPath: `tenant_${tenantId}` }));
  }
  return connectionPools.get(tenantId);
}
```

Limite prático: ~1000 schemas. Connection pool por tenant → risco de connection exhaustion. Solução: PgBouncer + `search_path` dinâmico.

### 3. Database-per-Tenant

Cada tenant com banco próprio (ou instância dedicada).

```
tenant_acme  → postgresql://db-acme.cluster/app
tenant_beta  → postgresql://db-beta.cluster/app
```

## Comparativo

| Critério | Shared Schema | Schema-per-Tenant | DB-per-Tenant |
|---|---|---|---|
| Custo infra | Baixo | Médio | Alto |
| Isolamento | Fraco (tenant_id) | Bom (schema) | Máximo |
| GDPR erasure | Complexo | `DROP SCHEMA CASCADE` | `DROP DB` |
| Noisy neighbor | Alto risco | Moderado | Sem risco |
| Max tenants | Ilimitado | ~1.000 | Centenas |
| Compliance enterprise | Difícil | Possível | Fácil |

## Decisão por Perfil

```
B2C / SMB (muitos clientes pequenos)     → Shared Schema
Mid-market (centenas, dados moderados)   → Schema-per-Tenant
Enterprise / HIPAA / PCI-DSS / GDPR      → DB-per-Tenant
```

## Tenant Context — Identificação e Propagação

Ver [[concepts/tenant-context]].

## Migrations

**Shared Schema:** uma migration afeta todos simultaneamente. Usar Expand-Contract para evitar lock.

**Schema-per-Tenant:** rodar em paralelo controlado:
```typescript
await pLimit(5, tenants.map(t => () => migrateSchema(t.schemaName)));
// rastrear versão por tenant — alertar se ficou atrás
```

**DB-per-Tenant:** pipeline percorre cada banco com timeout explícito.

## Rate Limiting por Tenant

```typescript
const TENANT_LIMITS = {
  free:       { rpm: 60,    daily: 1_000 },
  pro:        { rpm: 600,   daily: 50_000 },
  enterprise: { rpm: 6_000, daily: Infinity }
} as const;

async function rateLimitMiddleware(req, res, next) {
  const key = `rl:${req.tenant.id}:${Math.floor(Date.now() / 60_000)}`;
  const count = await redis.incr(key);
  if (count === 1) await redis.expire(key, 60);
  if (count > TENANT_LIMITS[req.tenant.tier].rpm) {
    res.setHeader("Retry-After", "60");
    return res.status(429).json({ error: "Rate limit exceeded for your plan" });
  }
  next();
}
```

## GDPR Offboarding

```typescript
async offboard(tenantId: string) {
  await db.tenants.update(tenantId, { status: "offboarding" });
  await authService.revokeAllTokens(tenantId);
  // grace period de 30 dias antes da deleção definitiva
  await queue.add("tenant-data-deletion", { tenantId }, { delay: 30 * 24 * 60 * 60 * 1000 });
}

async deleteData(tenantId: string) {
  await db.raw(`DROP SCHEMA tenant_${tenantId} CASCADE`); // schema-per-tenant
  await s3.deletePrefix(`tenants/${tenantId}/`);
}
```

## Armadilhas

- **Cross-tenant leak:** query sem `tenant_id` retorna dados de todos — RLS é segunda linha, testes de isolamento são a primeira
- **Connection pool exhaustion:** 500 tenants × 5 conn = 2500 → PgBouncer obrigatório
- **Migrations parciais:** rastrear versão por tenant, ter rollback seletivo
- **Noisy neighbor silencioso:** instrumentar `pg_stat_statements` por `tenant_id` para identificar ofensores

## Key Sources

- [[sources/multi-tenancy]]
