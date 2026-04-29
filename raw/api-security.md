---
date: 2026-04-01
tags: [tech-mentor, security, appsec, api-security, owasp-api, bola, rate-limiting, graphql]
skill: tech-mentor-security/references/appsec-api
level: intermediário
---

# API Security

## Contexto

O OWASP tem um Top 10 específico para APIs — diferente do Web Top 10. O padrão de acesso a dados em APIs REST/GraphQL/gRPC cria vulnerabilidades que não existem em aplicações web tradicionais.

## Como Funciona

### OWASP API Security Top 10

| # | Vulnerabilidade | Exemplo |
|---|---|---|
| API1 | BOLA | Acessar pedido de outro usuário trocando o ID na URL |
| API2 | Broken Authentication | Token sem expiração, endpoint de reset previsível |
| API3 | Mass Assignment | `{ isAdmin: true }` no body aceito pelo server |
| API4 | Unrestricted Resource Consumption | `/users` sem paginação retorna 1M rows |
| API5 | Broken Function Level Authorization | `DELETE /users/42` sem verificar role ADMIN |
| API6 | Unrestricted Business Flow | Bot comprando ingressos antes de humanos |
| API7 | SSRF | Parâmetro `url` que faz o server buscar recursos internos |
| API8 | Security Misconfiguration | Stack trace em produção, CORS `*` |
| API9 | Improper Inventory | API v1 esquecida sem os fixes de segurança da v2 |
| API10 | Unsafe Consumption | Confiar cegamente em resposta de API de terceiro |

## Código de Referência

### API1 — BOLA (Broken Object Level Authorization)

A vulnerabilidade mais crítica e mais comum em APIs.

```typescript
// VULNERÁVEL: qualquer usuário autenticado acessa qualquer pedido
app.get('/api/orders/:orderId', async req => {
  return db.query('SELECT * FROM orders WHERE id = $1', [req.params.orderId]);
});

// CORRETO: sempre filtrar pelo dono
app.get('/api/orders/:orderId', async req => {
  const order = await db.query(
    'SELECT * FROM orders WHERE id = $1 AND user_id = $2',
    [req.params.orderId, req.user.id]
  );
  if (!order) throw new NotFoundError();
  return order;
});
```

**Regra:** toda query que acessa recurso por ID deve incluir o `owner_id` do usuário autenticado.
**Teste:** troque o ID por um ID de outro usuário. Se retornar dados, é vulnerável.
UUID v4 dificulta enumeração mas não substitui a autorização — é defense in depth.

### API3 — Mass Assignment

```typescript
// VULNERÁVEL: req.body pode conter { isAdmin: true, role: "admin" }
app.patch('/api/users/:id', async req => {
  await db.update('users', req.body, { id: req.params.id });
});

// CORRETO: whitelist explícita
app.patch('/api/users/:id', async req => {
  const { name, email, bio } = req.body;
  await db.update('users', { name, email, bio }, { id: req.params.id });
});
```

Em Prisma/TypeORM: nunca passe `req.body` diretamente para `create`/`update`.

### API4 — Unrestricted Resource Consumption

```typescript
// CORRETO: cap no limit + paginação obrigatória
app.get('/api/users', async req => {
  const limit = Math.min(Number(req.query.limit) || 20, 100);
  const offset = Number(req.query.offset) || 0;
  return db.query('SELECT * FROM users LIMIT $1 OFFSET $2', [limit, offset]);
});
```

### Rate Limiting — Sliding Window com Redis

```typescript
async function rateLimitLogin(ip: string): Promise<{ allowed: boolean; remaining: number }> {
  const key = `rate:login:${ip}`;
  const limit = 5;
  const windowSeconds = 300;

  const current = await redis.incr(key);
  if (current === 1) await redis.expire(key, windowSeconds);

  return {
    allowed: current <= limit,
    remaining: Math.max(0, limit - current)
  };
}

app.post('/auth/login', async (req, res) => {
  const { allowed, remaining } = await rateLimitLogin(req.ip);
  res.setHeader('X-RateLimit-Remaining', remaining);

  if (!allowed) {
    return res.status(429).json({ error: 'Too many attempts. Try again in 5 minutes.' });
  }
  // lógica de login
});
```

**Headers padrão (RFC 6585):**
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 43
X-RateLimit-Reset: 1640000000
Retry-After: 30
```

### Estratégias de Rate Limiting

```
Fixed Window:   100 req/min por IP
  Problema: burst no boundary (99 no fim + 99 no início = 198 em 2s)

Sliding Window: janela deslizante — mais preciso, mais memória

Token Bucket:   tokens adicionados a taxa constante, consumidos por request
  Vantagem: permite burst natural (bom para usuários reais)

Leaky Bucket:   saída uniforme — bom para proteger backends downstream
```

**Credential stuffing** contorna rate limit por IP com requests distribuídos.
Defesa: device fingerprinting + behavioral analysis (taxa de sucesso baixa, requests sem cookies/JS, user-agents repetidos).
Serviços especializados: Cloudflare Bot Management, AWS WAF Bot Control, DataDome.

### GraphQL Security

| Risco | Ataque | Defesa |
|---|---|---|
| Introspection | Atacante mapeia toda a schema | Desabilitar em produção |
| Query Depth | Queries aninhadas explodem o DB | `depthLimit(5)` |
| Query Complexity | Queries custosas em 1 request | `createComplexityLimitRule(1000)` |
| Batch Query | 1000 logins em 1 request HTTP | `allowBatchedHttpRequests: false` |
| Authz em resolvers | Verificar só no root, não nos filhos | `graphql-shield` por field |

```typescript
// Apollo Server — proteções básicas
const server = new ApolloServer({
  introspection: process.env.NODE_ENV !== 'production',
  allowBatchedHttpRequests: false,
  validationRules: [
    depthLimit(5),
    createComplexityLimitRule(1000)
  ]
});
```

### gRPC Security

```typescript
// mTLS — serviços se autenticam mutuamente
const credentials = grpc.credentials.createSsl(
  fs.readFileSync('ca.crt'),
  fs.readFileSync('client.key'),
  fs.readFileSync('client.crt')
);

// Limitar tamanho de mensagem — sem limite por padrão é DoS
const server = new grpc.Server({
  'grpc.max_receive_message_length': 4 * 1024 * 1024,
  'grpc.max_send_message_length': 4 * 1024 * 1024,
});
```

**Desabilitar Reflection Service em produção** (equivalente à introspection do GraphQL).

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| BOLA fix | Elimina a vuln mais comum de APIs | Todas as queries precisam de filtro por owner |
| Rate limiting com Redis | Consistente em múltiplas instâncias | Latência extra + dependência do Redis |
| GraphQL restrictions | Previne DoS via queries complexas | Pode bloquear queries legítimas |
| gRPC mTLS | Autenticação mútua por padrão | Complexidade de gestão de certificados |

## Quando Usar / Quando Evitar

**Sempre aplique BOLA fix** — é a vulnerabilidade mais prevalente em APIs REST.
**Rate limiting:** obrigatório em qualquer endpoint de autenticação, criação de conta e ações de negócio.
**GraphQL restrictions:** obrigatórias em produção — sem depth limit e sem introspection, a API está exposta.

## Conceitos Relacionados

[[owasp-top10]] · [[autenticacao-segura]] · [[input-validation-output-encoding]] · [[zero-trust]] · [[secure-design-patterns]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-01*
