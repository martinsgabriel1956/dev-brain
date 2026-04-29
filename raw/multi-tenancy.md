---
date: 2026-03-29
tags: [tech-mentor, system-design, avançado, multi-tenancy, saas, isolamento]
skill: tech-mentor-system-design/references/multi-tenancy
level: arquiteto
---

# Multi-tenancy Patterns

## Contexto

Multi-tenancy é o modelo onde múltiplos clientes (tenants) compartilham a mesma infraestrutura. É o modelo padrão de SaaS. A escolha do modelo de isolamento é uma das decisões arquiteturais mais impactantes do produto — afeta custo, segurança, compliance, performance e complexidade operacional.

Errar essa escolha cedo é caro: migrar de shared schema para database-per-tenant com milhões de registros é um projeto de meses.

---

## Os 3 Modelos de Isolamento

### 1. Shared Database, Shared Schema

Todos os tenants no mesmo banco, mesmo schema. Separação apenas por coluna `tenant_id`.

```sql
CREATE TABLE orders (
  id         UUID PRIMARY KEY,
  tenant_id  UUID NOT NULL REFERENCES tenants(id),
  amount     DECIMAL(10,2),
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Index composto obrigatório — sem ele, queries por tenant fazem full scan
CREATE INDEX idx_orders_tenant ON orders(tenant_id, created_at DESC);

-- Row Level Security (PostgreSQL) — segunda linha de defesa contra bug na aplicação
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_isolation ON orders
  USING (tenant_id = current_setting('app.current_tenant_id')::UUID);
```

**Prós**: menor custo, operação simples, uma instância para manter, migrations únicas.

**Contras**: bug de isolamento na aplicação vaza dados entre tenants, "noisy neighbor" (query pesada de um tenant degrada todos), compliance enterprise difícil (GDPR right to erasure é complexo — precisa rastrear PII em todas as tabelas).

### 2. Shared Database, Schema-per-Tenant

Mesmo banco físico, mas cada tenant tem seu próprio schema PostgreSQL.

```sql
-- Provisionamento de novo tenant
CREATE SCHEMA tenant_acme;
CREATE TABLE tenant_acme.orders (
  id         UUID PRIMARY KEY,
  amount     DECIMAL(10,2),
  created_at TIMESTAMPTZ DEFAULT now()
  -- sem tenant_id — schema já é o isolamento
);

-- Aplicação seta o search_path por conexão
SET search_path TO tenant_acme, public;
SELECT * FROM orders; -- transparente, sem filtro de tenant_id
```

```typescript
// Pool de conexões por tenant (não criar nova a cada request)
function getConnectionForTenant(tenantId: string) {
  if (!connectionPools.has(tenantId)) {
    connectionPools.set(tenantId, createPool({
      searchPath: `tenant_${tenantId}`,
    }));
  }
  return connectionPools.get(tenantId);
}
```

**Prós**: isolamento lógico forte, migrations independentes por tenant, backup seletivo, GDPR erasure simples (`DROP SCHEMA tenant_x CASCADE`).

**Contras**: PostgreSQL tem limite prático de ~1.000 schemas performáticos, operações DDL multiplicam por número de tenants, connection pooling mais complexo (pool por tenant).

### 3. Database-per-Tenant

Cada tenant tem seu próprio banco de dados (ou instância de banco).

```
tenant_acme  → postgresql://db-acme.cluster/app
tenant_beta  → postgresql://db-beta.cluster/app
tenant_gamma → postgresql://db-shared-3.cluster/gamma  # host compartilhado, DB isolado
```

**Prós**: isolamento máximo, compliance trivial, performance dedicada, backup/restore por tenant sem afetar outros.

**Contras**: custo alto (N databases = N connection pools = N conjuntos de recursos), operações de schema precisam rodar em N bancos, onboarding mais lento.

---

## Comparação Direta

| Critério | Shared Schema | Schema-per-Tenant | DB-per-Tenant |
|---|---|---|---|
| **Custo infra** | Baixo | Médio | Alto |
| **Isolamento** | Fraco (só tenant_id) | Bom (schema) | Máximo |
| **GDPR erasure** | Complexo | Simples (DROP SCHEMA) | Trivial (DROP DB) |
| **Noisy neighbor** | Alto risco | Risco moderado | Sem risco |
| **Ops complexity** | Baixa | Média | Alta |
| **Max tenants** | Ilimitado | ~1.000 | Centenas |
| **Compliance enterprise** | Difícil | Possível | Fácil |

---

## Decisão por Perfil de Cliente

```
B2C / SMB (milhares de clientes pequenos, dados pouco sensíveis)
  → Shared Schema
  Custo domina; isolamento compensado com RLS + testes rigorosos

Mid-market (centenas de clientes, dados moderadamente sensíveis)
  → Schema-per-Tenant
  Equilíbrio custo vs isolamento; GDPR viável

Enterprise / Regulated (HIPAA, PCI-DSS, GDPR contractual)
  → DB-per-Tenant
  Isolamento é requisito de contrato, não de preferência
```

---

## Tenant Context — Identificação e Propagação

### Identificar o tenant na borda

```typescript
// Por subdomain: acme.myapp.com → tenant "acme"
function extractTenantFromSubdomain(host: string): string {
  return host.split(".")[0];
}

// Por JWT claim: { "tenant_id": "uuid-acme", "role": "admin" }
// Por API key mapeada para tenant no banco
// Por path: myapp.com/t/acme/dashboard
```

### Middleware — propagar contexto pela stack

```typescript
async function tenantMiddleware(req: Request, res: Response, next: NextFunction) {
  const tenantId = await resolveTenant(req);
  if (!tenantId) return res.status(401).json({ error: "Unknown tenant" });

  const config = await getTenantConfig(tenantId); // cache no Redis
  req.tenant = config;

  // AsyncLocalStorage: acesso ao tenant em qualquer camada sem passar por parâmetro
  tenantContext.run({ tenantId, config }, next);
}

// Use case, repository, qualquer lugar:
const { tenantId } = tenantContext.getStore();
```

---

## Migrations em Multi-tenant

### Shared Schema

Migration normal — afeta todos os tenants simultaneamente. Risco: migration lenta em tabela grande → downtime para todos.

```bash
prisma migrate deploy  # roda uma vez, afeta todos
```

Mitigar com Expand-Contract: adicionar coluna nullable primeiro, popular em background, depois tornar NOT NULL.

### Schema-per-Tenant

Migration precisa rodar em cada schema. Controle de concorrência essencial:

```typescript
async function migrateAllTenants() {
  const tenants = await getAllTenants();

  // p-limit: no máximo 5 migrations em paralelo (não sobrecarregar o banco)
  await pLimit(5, tenants.map(t => () => migrateSchema(t.schemaName)));
}
```

Versionar qual migration cada tenant está — permite rollback seletivo e detectar tenants presos em versões antigas.

### DB-per-Tenant

Pipeline de migration percorre cada banco:

```bash
for tenant in $(list-tenants); do
  run-migration --db "$tenant" --target latest --timeout 300
done
```

---

## Rate Limiting por Tenant

Noisy neighbor em shared schema não é só problema de banco — queries pesadas de um tenant podem saturar CPU, conexões e cache. Rate limiting por tenant por tier:

```typescript
const TENANT_LIMITS = {
  free:       { rpm: 60,    daily: 1_000 },
  pro:        { rpm: 600,   daily: 50_000 },
  enterprise: { rpm: 6_000, daily: Infinity }
} as const;

async function rateLimitMiddleware(req: Request, res: Response, next: NextFunction) {
  const { id: tenantId, tier } = req.tenant;
  const limits = TENANT_LIMITS[tier];

  const key = `rl:${tenantId}:${Math.floor(Date.now() / 60_000)}`; // janela por minuto
  const count = await redis.incr(key);
  if (count === 1) await redis.expire(key, 60);

  if (count > limits.rpm) {
    res.setHeader("Retry-After", "60");
    return res.status(429).json({ error: "Rate limit exceeded for your plan" });
  }

  next();
}
```

---

## Customização por Tenant

Tenants enterprise frequentemente precisam de configuração específica — evitar hardcode, modelar explicitamente:

```typescript
type TenantConfig = {
  features: Record<string, boolean>;          // feature flags por tenant
  limits: { maxUsers: number; storageGb: number };
  integrations: { sso?: SSOConfig; webhooks?: string[] };
  branding: { logoUrl: string; primaryColor: string };
  dataResidency: "us-east" | "eu-west" | "ap-southeast"; // GDPR
};
```

---

## Offboarding e GDPR Right to Erasure

```typescript
class TenantOffboardingService {
  async offboard(tenantId: string) {
    // 1. Soft delete imediato — desativa acesso
    await db.tenants.update(tenantId, {
      status: "offboarding",
      offboardingStartedAt: new Date()
    });

    // 2. Revogar todos os tokens e sessões
    await authService.revokeAllTokens(tenantId);

    // 3. Agendar deleção após grace period (30 dias — permite reverter)
    await queue.add("tenant-data-deletion", { tenantId }, {
      delay: 30 * 24 * 60 * 60 * 1000
    });

    await events.emit("tenant.offboarding.started", { tenantId });
  }

  async deleteData(tenantId: string) {
    // Schema-per-tenant: trivial
    await db.raw(`DROP SCHEMA tenant_${tenantId} CASCADE`);

    // Limpar dados em sistemas externos
    await s3.deletePrefix(`tenants/${tenantId}/`);
    await elasticsearch.deleteByQuery({
      index: "events",
      query: { term: { tenant_id: tenantId } }
    });
  }
}
```

---

## Armadilhas

**Cross-tenant data leak**: query sem filtro de `tenant_id` retorna dados de todos. RLS é segunda linha de defesa — a primeira são testes de isolamento automatizados que verificam explicitamente que tenant A não acessa dados de tenant B.

**Connection pool exhaustion (schema-per-tenant)**: com 500 tenants ativos e pool de 5 conexões por tenant = 2.500 conexões abertas. PostgreSQL tem limite prático de ~1.000. Usar PgBouncer + pool compartilhado com `search_path` dinâmico.

**Migrations parciais**: falha no meio da pipeline deixa tenants em versões diferentes. Rastrear versão por tenant, ter rollback por tenant, alertar se tenant ficou mais de X versões atrás.

**Noisy neighbor não detectado**: um tenant fazendo queries lentas degrada todos os outros sem que ninguém saiba. Instrumentar `pg_stat_statements` por `tenant_id` (via `SET app.current_tenant_id`) para identificar ofensores.

---

## Conceitos Relacionados

[[banco-de-dados]] · [[rate-limiting]] · [[feature-flags]] · [[observabilidade]] · [[cap-pacelc-consistencia]]

---

*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-29*
