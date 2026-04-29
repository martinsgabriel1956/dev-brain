---
type: concept
title: "Tenant Context"
aliases: ["tenant context", "tenant middleware", "tenant resolution", "asynclocalstorage tenant"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [multi-tenancy, saas, middleware, nodejs, contexto]
skill: tech-mentor-system-design
status: stable
---

# Tenant Context

Mecanismo para identificar o tenant na borda da requisição e propagar esse contexto por toda a stack sem passar por parâmetro em cada função.

## Identificação na Borda

```typescript
// Por subdomain: acme.myapp.com → "acme"
function extractTenantFromSubdomain(host: string): string {
  return host.split(".")[0];
}

// Alternativas:
// JWT claim: { "tenant_id": "uuid-acme" }
// API key mapeada para tenant no banco
// Path prefix: myapp.com/t/acme/dashboard
```

## Middleware com AsyncLocalStorage

```typescript
async function tenantMiddleware(req: Request, res: Response, next: NextFunction) {
  const tenantId = await resolveTenant(req);
  if (!tenantId) return res.status(401).json({ error: "Unknown tenant" });

  const config = await getTenantConfig(tenantId); // cache no Redis
  req.tenant = config;

  // AsyncLocalStorage: acesso ao tenant em qualquer camada sem prop drilling
  tenantContext.run({ tenantId, config }, next);
}

// Use case, repository, qualquer lugar — sem receber tenantId por parâmetro:
const { tenantId } = tenantContext.getStore();
```

## TenantConfig

```typescript
type TenantConfig = {
  features: Record<string, boolean>;           // feature flags por tenant
  limits: { maxUsers: number; storageGb: number };
  integrations: { sso?: SSOConfig; webhooks?: string[] };
  branding: { logoUrl: string; primaryColor: string };
  dataResidency: "us-east" | "eu-west" | "ap-southeast";
};
```

`dataResidency` é crítico para GDPR — determina em qual região os dados do tenant são armazenados e processados.

## Key Sources

- [[sources/multi-tenancy]]
