---
date: 2026-03-30
tags: [tech-mentor, security, appsec, owasp, vulnerabilidades]
skill: tech-mentor-security/references/appsec-owasp
level: fundamento
---

# OWASP Top 10 & API Security

## Contexto

OWASP (Open Worldwide Application Security Project) mantém as listas das vulnerabilidades mais críticas em aplicações web e APIs. Não são teóricas — são as que aparecem em breaches reais, relatórios de pentest e bug bounty toda semana. Conhecê-las é o mínimo para não introduzir vulnerabilidades no código que você escreve.

Existem dois Top 10 distintos: o **Web Top 10** (aplicações web) e o **API Top 10** (APIs REST/GraphQL). Este documento cobre os mais relevantes na prática diária.

---

## OWASP Web Top 10 — Os que mais importam

### 1. Broken Access Control ← o mais crítico

Autenticação verifica *quem você é*. Autorização verifica *o que você pode fazer*. A maioria dos sistemas verifica autenticação e esquece a autorização em operações individuais.

```typescript
// ❌ qualquer usuário autenticado pode deletar qualquer pedido
app.delete("/orders/:id", async (req, res) => {
  await db.query("DELETE FROM orders WHERE id = $1", [req.params.id]);
});

// ✅ verificar que o recurso pertence ao usuário autenticado
app.delete("/orders/:id", async (req, res) => {
  const result = await db.query(
    "DELETE FROM orders WHERE id = $1 AND user_id = $2",
    [req.params.id, req.user.id]  // user.id vem do token validado
  );
  if (result.rowCount === 0) return res.status(404).send();
});
```

**Regra**: toda query que acessa recurso por ID deve incluir o `owner_id` (ou verificação de role) do usuário autenticado. Nunca confie em IDs vindos do body/params sem verificar ownership.

---

### 2. Injection (SQL, NoSQL, Command)

Input do usuário interpretado como código pelo interpretador.

```typescript
// ❌ SQL Injection clássico
const query = `SELECT * FROM users WHERE email = '${email}'`;
// email = "' OR '1'='1" → retorna todos os usuários

// ✅ parameterized query — sempre
const result = await db.query("SELECT * FROM users WHERE email = $1", [email]);
```

**ORMs não são imunes** — Prisma e TypeORM têm vetores específicos:

```typescript
// ❌ Prisma $queryRaw com template literal direto
const users = await prisma.$queryRaw`SELECT * FROM users WHERE name = '${userInput}'`;

// ✅ Prisma parametriza variáveis interpoladas automaticamente
const users = await prisma.$queryRaw`SELECT * FROM users WHERE name = ${userInput}`;

// ❌ TypeORM QueryBuilder com interpolação direta
await repo.createQueryBuilder("user")
  .where(`user.name = '${userInput}'`)
  .getMany();

// ✅ TypeORM com parâmetros nomeados
await repo.createQueryBuilder("user")
  .where("user.name = :name", { name: userInput })
  .getMany();
```

**ORDER BY — vetor frequentemente esquecido** (não pode ser parametrizado):

```typescript
const ALLOWED_SORT = ["name", "createdAt", "price"] as const;
type SortField = typeof ALLOWED_SORT[number];

function sanitizeSortField(field: string): SortField {
  if (!ALLOWED_SORT.includes(field as SortField)) {
    throw new Error("Invalid sort field");
  }
  return field as SortField;
}
```

---

### 3. XSS — Cross-Site Scripting

Script malicioso executado no browser da vítima. React escapa HTML por padrão — mas há vetores específicos.

```typescript
// ✅ React escapa automaticamente — seguro
return <div>{userContent}</div>;

// ❌ dangerouslySetInnerHTML sem sanitização
return <div dangerouslySetInnerHTML={{ __html: userContent }} />;

// ✅ sanitizar com DOMPurify antes de renderizar HTML
import DOMPurify from "dompurify";
return <div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(userContent) }} />;

// ❌ href com javascript: protocol (React não sanitiza href)
const url = "javascript:alert(1)";
return <a href={url}>Click</a>;

// ✅ validar protocol antes de usar
function SafeLink({ href, children }: { href: string; children: React.ReactNode }) {
  const safeUrl = href.startsWith("http") || href.startsWith("/") ? href : "#";
  return <a href={safeUrl}>{children}</a>;
}
```

**Stored vs Reflected vs DOM-based**:
- **Stored**: payload persiste no banco, afeta todos os usuários que veem o conteúdo — mais crítico
- **Reflected**: payload na URL, afeta quem clica no link
- **DOM-based**: payload manipula o DOM via JS sem passar pelo servidor

---

### 4. SSRF — Server-Side Request Forgery

Seu servidor faz requests para URLs controladas pelo atacante. Em cloud, o alvo mais comum é o metadata endpoint da instância.

```
Atacante envia: POST /preview { "url": "http://169.254.169.254/latest/meta-data/iam/security-credentials/ec2-role" }
Seu servidor faz fetch(url) e retorna as credenciais IAM temporárias da EC2
→ Atacante tem acesso completo à sua AWS
```

```typescript
// ❌ fetch de URL do usuário sem validação
app.post("/preview", async (req, res) => {
  const html = await fetch(req.body.url).then(r => r.text());
  res.send(html);
});

// ✅ validar URL antes de fazer request
async function isSafeUrl(url: string): Promise<boolean> {
  const parsed = new URL(url);
  if (!["http:", "https:"].includes(parsed.protocol)) return false;
  if (["localhost", "127.0.0.1", "::1"].includes(parsed.hostname)) return false;

  const addresses = await dns.resolve4(parsed.hostname);
  return addresses.every(addr => !isPrivateIP(addr));
}

function isPrivateIP(ip: string): boolean {
  // 10.x, 172.16-31.x, 192.168.x, 169.254.x (AWS metadata)
  return /^(10\.|172\.(1[6-9]|2\d|3[01])\.|192\.168\.|169\.254\.)/.test(ip);
}
```

**Defense in depth para SSRF**:
- IMDSv2 na AWS — requer token de sessão, bloqueia SSRF simples
- Allowlist de domínios permitidos (melhor que blocklist)
- Firewall de egresso bloqueando tráfego para ranges privados

---

### 5. Cryptographic Failures

Dados sensíveis expostos por uso incorreto (ou ausência) de criptografia.

```
❌ Senhas com MD5 ou SHA1 — reversíveis por rainbow table
❌ HTTP sem TLS — dados em plaintext na rede
❌ Dados sensíveis em logs (senhas, tokens, CPFs, cartões)
❌ Tokens de API armazenados em plain text no banco

✅ Senhas: bcrypt (12 rounds) ou Argon2id
✅ HTTPS em tudo + HSTS
✅ Sanitizar body antes de logar (remover campos sensíveis)
✅ API keys: armazenar apenas o hash (bcrypt), nunca a key em plain text
```

---

### 6. Security Misconfiguration

Configuração padrão insegura deixada ativa.

```typescript
// ✅ helmet.js configura headers de segurança no Express/Fastify
import helmet from "helmet";
app.use(helmet());

// Headers que o helmet configura:
// Content-Security-Policy   → previne XSS
// X-Frame-Options           → previne clickjacking
// Strict-Transport-Security → força HTTPS
// X-Content-Type-Options    → previne MIME sniffing
```

**Checklist de misconfiguration**:
- CORS configurado como `*` em produção para APIs autenticadas → risco
- Stack traces expostos em respostas de erro → vaza informação interna
- Credenciais default não alteradas (banco, admin panels)
- Debug mode ativo em produção

---

### 7. Path Traversal

Input do usuário manipula caminhos de arquivo para acessar arquivos fora do diretório permitido.

```typescript
// ❌ path.join NÃO previne traversal
app.get("/file", (req, res) => {
  const filePath = path.join("/app/uploads", req.query.name);
  res.sendFile(filePath);
  // req.query.name = "../../../etc/passwd" → /etc/passwd
});

// ✅ verificar que o path resolvido está dentro do diretório base
app.get("/file", (req, res) => {
  const base = "/app/uploads";
  const requested = path.resolve(base, req.query.name as string);

  if (!requested.startsWith(base + path.sep)) {
    return res.status(403).send("Forbidden");
  }
  res.sendFile(requested);
});
```

---

## OWASP API Top 10 — Específico para APIs

### API1 — BOLA (Broken Object Level Authorization) = IDOR

O mais crítico e mais comum. Já coberto acima em Broken Access Control — merece destaque por ser a #1 em APIs.

```typescript
// ❌ /api/orders/42 acessível por qualquer usuário autenticado
// ✅ /api/orders/42 com AND user_id = $2 na query
```

### API3 — Mass Assignment

Aceitar propriedades do body sem whitelist — cliente pode elevar privilégio.

```typescript
// ❌ req.body pode ter { isAdmin: true, role: "admin" }
await prisma.user.update({ where: { id }, data: req.body });

// ✅ whitelist explícita dos campos permitidos
const { name, email, bio } = req.body;
await prisma.user.update({ where: { id }, data: { name, email, bio } });
```

**Regra**: nunca passe `req.body` diretamente para `create`/`update` em ORM. Sempre destructure os campos permitidos.

### API4 — Unrestricted Resource Consumption

APIs sem limites de paginação ou tamanho de request.

```typescript
// ✅ sempre limitar resultados e aceitar no máximo N por page
const limit = Math.min(Number(req.query.limit) || 20, 100);
const offset = Number(req.query.offset) || 0;
```

### API5 — Broken Function Level Authorization

Endpoints administrativos sem verificação de role.

```typescript
// ✅ middleware de verificação de role em todas as rotas admin
function requireRole(role: string) {
  return (req: Request, res: Response, next: NextFunction) => {
    if (!req.user.roles.includes(role)) {
      return res.status(403).json({ error: "Insufficient permissions" });
    }
    next();
  };
}

app.delete("/api/admin/users/:id", requireRole("admin"), deleteUser);
```

---

## Timing Attacks — `crypto.timingSafeEqual`

Comparação de strings com `===` retorna imediatamente ao encontrar o primeiro byte diferente — vaza informação sobre onde a diferença está. Com tentativas suficientes, um atacante reconstrói o token válido byte a byte.

```typescript
import { timingSafeEqual, createHmac } from "crypto";

function verifyWebhookSignature(payload: string, signature: string, secret: string): boolean {
  const expected = createHmac("sha256", secret)
    .update(payload)
    .digest("hex");

  const expectedBuffer = Buffer.from(expected, "hex");
  const receivedBuffer = Buffer.from(signature, "hex");

  if (expectedBuffer.length !== receivedBuffer.length) return false;

  // timingSafeEqual SEMPRE compara todos os bytes — tempo constante
  return timingSafeEqual(expectedBuffer, receivedBuffer);
}
```

**Regra**: qualquer comparação de segredo (token, HMAC, senha hash) deve usar `timingSafeEqual`. O `===` é para dados não-sensíveis.

---

## Rate Limiting como Segurança

Rate limiting não é só performance — é defesa contra brute force, credential stuffing e abuse de negócio.

```typescript
// Diferentes limites por endpoint por tipo de risco
const limits = {
  login:        { requests: 5,   window: "15m" }, // brute force
  createAccount:{ requests: 3,   window: "1h"  }, // account farming
  api:          { requests: 100, window: "1m"  }, // uso normal
  admin:        { requests: 20,  window: "1m"  }, // operações sensíveis
};
```

**Onde aplicar**: login, criação de conta, reset de senha, verificação de email, endpoints de busca — qualquer fluxo que possa ser abusado em volume.

---

## CORS em Profundidade

CORS é validado pelo **browser** — não protege contra ataques server-side (curl, scripts, Postman).

```typescript
// ✅ configuração restrita
app.register(cors, {
  origin: (origin, callback) => {
    const allowed = ["https://app.exemplo.com", "https://admin.exemplo.com"];
    if (!origin || allowed.includes(origin)) {
      callback(null, true);
    } else {
      callback(new Error("CORS not allowed"), false);
    }
  },
  credentials: true,  // necessário para cookies/Authorization header
  // ⚠️ com credentials: true, origin NÃO pode ser "*"
});
```

**Subdomínios dinâmicos** (multi-tenant):
```typescript
// ✅ regex para validar padrão de subdomínio
if (!origin || /^https:\/\/[a-z0-9-]+\.exemplo\.com$/.test(origin)) {
  callback(null, true);
}
```

---

## Input: Validação vs Sanitização

```
Validação:   rejeitar input que não corresponde ao formato esperado
Sanitização: transformar input para formato seguro

Ordem: Input → Sanitize → Validate → Use

Quando validar (rejeitar):  emails, UUIDs, números, enums — formato definido
Quando sanitizar (limpar):  HTML de usuário, nomes de arquivo, texto livre
```

```typescript
// Validação com Zod
const schema = z.object({
  email: z.string().email(),
  age: z.number().int().min(0).max(150),
  role: z.enum(["user", "editor"])
});

// Sanitização de HTML (rich text de usuário)
import DOMPurify from "dompurify";
const clean = DOMPurify.sanitize(dirty, {
  ALLOWED_TAGS: ["p", "br", "strong", "em", "ul", "ol", "li", "a"],
  ALLOWED_ATTR: ["href", "rel"],
  FORBID_ATTR: ["style", "onclick"]
});
```

---

## Checklist Rápido por Feature

Ao implementar qualquer endpoint novo:

```
[ ] Cada recurso acessado por ID tem verificação de ownership/role?
[ ] Inputs validados com Zod antes de usar?
[ ] Queries usam parâmetros, nunca interpolação?
[ ] HTML de usuário sanitizado com DOMPurify antes de renderizar?
[ ] Comparação de tokens usa timingSafeEqual?
[ ] Rate limiting no endpoint se for sensível?
[ ] Headers de segurança configurados (helmet)?
[ ] Dados sensíveis fora dos logs?
[ ] URLs do usuário validadas antes de fetch server-side?
```

---

## Conceitos Relacionados

[[autenticacao-segura]] · [[criptografia-fundamentos]] · [[secrets-management]] · [[input-validation-output-encoding]] · [[api-security]]

---

*Fonte: tech-mentor skill · tech-mentor-security · 2026-03-30*
