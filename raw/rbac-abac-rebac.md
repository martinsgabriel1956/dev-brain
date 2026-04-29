---
date: 2026-04-13
tags: [tech-mentor, auth, rbac, abac, rebac, autorizacao, zanzibar]
skill: tech-mentor-security/references/authorization
level: avançado
---

# RBAC, ABAC e ReBAC — Modelos de Autorização

## Contexto

Autenticação responde "quem é você?". **Autorização** responde "o que você pode fazer?". São problemas diferentes, resolvidos por mecanismos diferentes.

Os três modelos têm complexidade crescente:
- **RBAC** — papéis determinam permissões (simples, rígido)
- **ABAC** — atributos determinam permissões (flexível, complexo)
- **ReBAC** — relacionamentos determinam permissões (Google Zanzibar model)

## RBAC — Role-Based Access Control

### Modelo Básico

```
User → has Roles → Roles have Permissions → Permissions allow Actions on Resources
```

```typescript
// Implementação simples no banco
type Role = "admin" | "editor" | "viewer";

const PERMISSIONS: Record<Role, string[]> = {
  admin: ["posts:read", "posts:write", "posts:delete", "users:manage"],
  editor: ["posts:read", "posts:write"],
  viewer: ["posts:read"]
};

function hasPermission(userRoles: Role[], permission: string): boolean {
  return userRoles.some(role => PERMISSIONS[role].includes(permission));
}

// Middleware
function requirePermission(permission: string) {
  return (req: Request, res: Response, next: NextFunction) => {
    if (!hasPermission(req.user.roles, permission)) {
      return res.status(403).json({ error: "Forbidden" });
    }
    next();
  };
}

// Route
app.delete("/posts/:id", requirePermission("posts:delete"), deletePostHandler);
```

### Limitação do RBAC Básico

RBAC não resolve "o usuário pode editar apenas seus próprios posts" — isso requer contexto do recurso, não apenas do usuário.

## ABAC — Attribute-Based Access Control

Decisão de acesso baseada em **atributos** do sujeito (quem), do recurso (o quê) e do ambiente (quando/onde):

```typescript
type PolicyContext = {
  subject: {
    userId: string;
    roles: string[];
    department: string;
    tenantId: string;
  };
  resource: {
    type: string;
    id: string;
    ownerId: string;
    tenantId: string;
    status: string;
  };
  action: string;
  environment: {
    ipAddress: string;
    time: Date;
  };
};

type Policy = {
  name: string;
  evaluate(ctx: PolicyContext): boolean;
};

// Políticas compostas
const policies: Policy[] = [
  {
    name: "owner-can-edit-own-draft",
    evaluate: ({ subject, resource, action }) =>
      action === "posts:write" &&
      resource.type === "post" &&
      resource.ownerId === subject.userId &&
      resource.status === "draft"
  },
  {
    name: "admin-can-edit-any-post",
    evaluate: ({ subject, action }) =>
      action === "posts:write" &&
      subject.roles.includes("admin")
  },
  {
    name: "tenant-isolation",
    evaluate: ({ subject, resource }) =>
      subject.tenantId === resource.tenantId  // multi-tenant boundary
  }
];

function isAuthorized(ctx: PolicyContext): boolean {
  return policies.some(policy => policy.evaluate(ctx));
}
```

### OPA (Open Policy Agent) — ABAC em Produção

```rego
# posts.rego
package posts

default allow = false

# Admin pode fazer qualquer coisa
allow {
  input.subject.roles[_] == "admin"
}

# Dono pode editar seus próprios posts em draft
allow {
  input.action == "posts:write"
  input.resource.owner_id == input.subject.user_id
  input.resource.status == "draft"
}

# Isolamento de tenant — sempre obrigatório
allow {
  input.resource.tenant_id == input.subject.tenant_id
}
```

```typescript
// Avaliação via OPA HTTP API
async function checkOPA(ctx: PolicyContext): Promise<boolean> {
  const response = await fetch("http://opa:8181/v1/data/posts/allow", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ input: ctx })
  });
  const { result } = await response.json();
  return result === true;
}
```

## ReBAC — Relationship-Based Access Control (Google Zanzibar)

O modelo usado pelo Google para Drive, Docs, etc. Permissões baseadas em **grafos de relacionamentos**:

```
"Alice pode editar doc-123" porque:
  Alice → is member of → Team A
  Team A → has editor on → doc-123

Ou:
  Alice → is owner of → doc-123 (direct relationship)
```

### Tuples — O Modelo de Dados

```typescript
// Tudo é representado como tuples: (object, relation, user)
type Tuple = {
  object: string;   // "document:doc-123"
  relation: string; // "editor"
  user: string;     // "user:alice" ou "group:team-a#member"
};

// Exemplos:
const tuples: Tuple[] = [
  // Alice é owner do documento
  { object: "document:doc-123", relation: "owner", user: "user:alice" },

  // Team A tem editor no documento
  { object: "document:doc-123", relation: "editor", user: "group:team-a#member" },

  // Bob é membro do Team A
  { object: "group:team-a", relation: "member", user: "user:bob" }
];

// Bob pode editar doc-123 porque:
// user:bob → member of group:team-a → editor of document:doc-123
```

### Schema (OpenFGA)

```yaml
# schema.yaml
model:
  schema: 1.1

type user

type group
  relations:
    define member: [user]

type document
  relations:
    define owner: [user]
    define editor: [user, group#member] | owner
    define viewer: [user, group#member] | editor
    define can_edit: editor
    define can_view: viewer
```

### Consulta de Permissão

```typescript
import { OpenFgaApi } from "@openfga/sdk";

const fga = new OpenFgaApi({ storeId: env.FGA_STORE_ID });

async function canEdit(userId: string, documentId: string): Promise<boolean> {
  const { allowed } = await fga.check({
    tuple_key: {
      user: `user:${userId}`,
      relation: "can_edit",
      object: `document:${documentId}`
    }
  });
  return allowed ?? false;
}

// Listar todos os documentos que o usuário pode ver
async function listEditableDocuments(userId: string): Promise<string[]> {
  const { objects } = await fga.listObjects({
    user: `user:${userId}`,
    relation: "can_edit",
    type: "document"
  });
  return objects.map(obj => obj.replace("document:", ""));
}
```

## Comparação dos Modelos

| Aspecto | RBAC | ABAC | ReBAC |
|---|---|---|---|
| Complexidade | Baixa | Alta | Média-Alta |
| Granularidade | Por role | Por atributo | Por relacionamento |
| "Editar próprio post" | ❌ difícil | ✅ sim | ✅ sim |
| Multi-tenant isolation | ❌ manual | ✅ atributo | ✅ relacionamento |
| Performance | Alta | Média | Alta (cache) |
| Auditoria | Simples | Complexa | Natural (log de tuples) |
| Quando usar | Apps simples com papéis fixos | Compliance, LGPD, contexto complexo | Colaboração, hierarquias, sharing |

## Escolha Prática

```
Pergunta: "O acesso depende de quem possui/compartilhou o recurso?"
  → Sim → ReBAC (OpenFGA, Google Zanzibar, Casbin com relacionamentos)

Pergunta: "O acesso depende de atributos do usuário, recurso E contexto?"
  → Sim → ABAC (OPA, Casbin ABAC)

Pergunta: "Papéis fixos e regras simples são suficientes?"
  → Sim → RBAC (mais simples de implementar e auditar)
```

## Conceitos Relacionados

[[oauth2-oidc-jwt]] · [[zero-trust]] · [[autenticacao-segura]] · [[multi-tenancy]] · [[api-security]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-13*
