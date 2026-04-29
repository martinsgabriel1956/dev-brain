---
date: 2026-03-30
tags: [tech-mentor, security, secure-design, defense-in-depth, least-privilege, fail-secure, attack-surface]
skill: tech-mentor-security/references/appsec-sdlc
level: intermediário
---

# Secure Design Patterns

## Contexto

Secure design patterns são princípios arquiteturais que tornam a segurança uma propriedade emergente do sistema — não um conjunto de controles adicionados no final. A diferença entre um sistema que "tem segurança" e um sistema que "é seguro" está no design.

Esses princípios precedem qualquer decisão de tecnologia. Um sistema mal desenhado não pode ser tornado seguro por patches, firewalls ou ferramentas de monitoramento.

---

## 1. Defense in Depth

Múltiplas camadas de controle independentes. Se uma falha, as outras contêm o dano.

```
Camada 1: Firewall / WAF              → bloqueia tráfego malicioso
Camada 2: Autenticação + MFA          → verifica identidade
Camada 3: Autorização (RBAC/ABAC)     → verifica permissão por operação
Camada 4: Input validation            → rejeita inputs maliciosos
Camada 5: Parameterized queries       → previne SQL injection mesmo com input inválido
Camada 6: Encryption at rest          → dados inúteis se storage for comprometido
Camada 7: Audit log                   → detecta e documenta o que passou
```

**Por que importa**: nenhuma camada é suficiente sozinha. Um atacante que bypassa o WAF ainda enfrenta autenticação. Quem obtém credenciais ainda enfrenta autorização por recurso. Quem compromete o banco encontra dados cifrados.

**Armadilha**: defense in depth não significa duplicar controles idênticos. Camadas diferentes devem ser *independentes* — uma falha em uma não deve causar falha em outra. WAF e validação de input no código são independentes; dois firewalls do mesmo vendor com a mesma configuração não são.

---

## 2. Least Privilege

Cada componente tem acesso apenas ao mínimo necessário para sua função. Nada mais.

```typescript
// ❌ service account com acesso total ao banco
// CREATE USER app_user SUPERUSER;

// ✅ acesso apenas às tabelas e operações necessárias
// CREATE USER app_user WITH LOGIN;
// GRANT SELECT, INSERT, UPDATE ON users, orders TO app_user;
// GRANT SELECT ON products TO app_user;
// -- sem DELETE, sem acesso a tabelas de audit, sem acesso a outros schemas
```

```yaml
# ❌ IAM Role com AdministratorAccess para uma Lambda
# ✅ IAM Role com apenas o que a Lambda precisa
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::my-bucket/uploads/*"
    },
    {
      "Effect": "Allow",
      "Action": ["secretsmanager:GetSecretValue"],
      "Resource": "arn:aws:secretsmanager:us-east-1:123:secret:prod/myapp/db-*"
    }
  ]
}
```

**Aplicação por camada**:

| Camada | Least privilege significa |
|---|---|
| Usuário de banco | SELECT/INSERT/UPDATE apenas nas tabelas necessárias |
| IAM Role | Apenas as actions necessárias, apenas nos recursos específicos |
| Container | `runAsNonRoot: true`, capabilities mínimas, volume mounts read-only |
| Microserviço | Acesso apenas aos serviços que precisa chamar (network policy) |
| Token de API | Scopes mínimos — read-only se só precisar ler |

**Por que importa**: se um componente for comprometido, o blast radius é limitado ao que aquele componente podia acessar. Um service account com acesso a tudo significa que comprometer um serviço = comprometer tudo.

---

## 3. Secure Defaults

O comportamento padrão do sistema deve ser o comportamento seguro. O caminho de menor resistência deve ser o caminho seguro.

```typescript
// ❌ default inseguro — requer ação explícita para tornar seguro
function createUser(data: UserDTO, options = { sendVerificationEmail: false, isAdmin: false }) { ... }

// ✅ default seguro — requer ação explícita para relaxar
function createUser(data: UserDTO, options = { sendVerificationEmail: true, isAdmin: false }) { ... }
```

```typescript
// ❌ CORS aberto por default
app.use(cors()); // permite qualquer origem

// ✅ CORS restrito por default
app.use(cors({
  origin: process.env.ALLOWED_ORIGINS.split(","),
  credentials: true
}));
```

**Exemplos de secure defaults em frameworks**:

| Decisão | Default inseguro | Default seguro |
|---|---|---|
| Headers de segurança | Ausentes | `helmet()` ativo |
| Cookies de sessão | `httpOnly: false` | `httpOnly: true, secure: true, sameSite: "lax"` |
| Serialização JSON | Inclui todos os campos | Allowlist explícita de campos retornados |
| Logs | Log completo do body | Body sanitizado (sem senhas, tokens) |
| CORS | `*` | Lista explícita de origens permitidas |
| Banco de dados | Acesso sem TLS | TLS obrigatório |

**Regra de design**: se o desenvolvedor não fizer nada especial, o sistema deve ser seguro. Se precisar de ação explícita para ativar segurança, ela não será ativada.

---

## 4. Fail Secure (Fail Closed)

Em caso de erro, negar acesso — nunca conceder.

```typescript
// ❌ Fail open — erro = acesso concedido
function canAccessResource(userId: string, resourceId: string): boolean {
  try {
    return checkPermission(userId, resourceId);
  } catch {
    return true; // erro = acesso livre → NUNCA
  }
}

// ✅ Fail secure — erro = acesso negado
function canAccessResource(userId: string, resourceId: string): boolean {
  try {
    return checkPermission(userId, resourceId);
  } catch (error) {
    logger.error({ message: "Permission check failed", userId, resourceId, error });
    return false; // em caso de dúvida, negar
  }
}
```

```typescript
// ❌ JWT validation — fail open
function getUser(token: string): User | null {
  try {
    return verify(token, secret) as User;
  } catch {
    return null; // null pode ser tratado como "usuário anônimo com acesso"
  }
}

// ✅ JWT validation — fail secure com erro explícito
function getUser(token: string): User {
  try {
    return verify(token, process.env.JWT_SECRET, { algorithms: ["RS256"] }) as User;
  } catch (error) {
    throw new UnauthorizedError("Invalid or expired token");
    // upstream middleware retorna 401 — sem acesso
  }
}
```

**Fail secure vs fail safe**: em segurança, "safe" e "secure" são diferentes.
- **Fail safe** (engenharia): o sistema falha de forma que não causa dano físico (porta corta-fogo abre em incêndio)
- **Fail secure** (segurança): o sistema falha de forma que não concede acesso (porta de data center fecha em falha de energia)

O contexto determina qual é o comportamento correto — em sistemas críticos de segurança física, fail safe pode ser obrigatório.

---

## 5. Minimização de Superfície de Ataque

Cada serviço exposto, porta aberta, endpoint, dependência e funcionalidade é superfície de ataque potencial. Exponha apenas o necessário.

```
Reduzir superfície:
  → Desabilitar endpoints não utilizados
  → Remover dependências não usadas (cada lib é superfície potencial)
  → Fechar portas não necessárias no security group
  → Desabilitar features de debug em produção
  → Usar imagens base mínimas (distroless, alpine)
  → Não expor metadados internos em respostas de API
```

```typescript
// ❌ resposta com campos internos expostos
app.get("/users/:id", async (req, res) => {
  const user = await db.users.findById(req.params.id);
  res.json(user); // inclui passwordHash, internalFlags, sensitiveFields
});

// ✅ projeção explícita — só o que o cliente precisa
app.get("/users/:id", async (req, res) => {
  const user = await db.users.findById(req.params.id, {
    select: { id: true, name: true, email: true, createdAt: true }
  });
  res.json(user);
});
```

```yaml
# ❌ security group aberto
ingress:
  - from: 0.0.0.0/0
    port: 5432  # PostgreSQL exposto para internet

# ✅ acesso apenas de dentro da VPC
ingress:
  - from: 10.0.0.0/8
    port: 5432
```

**Regra para APIs**: não retorne dados que o cliente não precisa. Cada campo retornado é uma informação que pode ser usada em reconnaissance ou combinada com outros dados.

---

## 6. Separação de Responsabilidades

Nenhum componente único deve ter poder suficiente para comprometer o sistema sozinho.

```
❌ Uma service account pode:
   - Ler dados de usuários
   - Escrever no banco de dados
   - Acessar o secrets manager
   - Fazer deploy de nova versão

✅ Separação:
   - App service account: ler/escrever no banco da aplicação
   - Deploy pipeline: acesso ao ECS/ECR apenas
   - Secrets rotation Lambda: acesso apenas ao secrets manager
   - Audit service: acesso read-only ao banco de audit
```

Aplicado a humanos: o desenvolvedor que escreve o código não deveria ter acesso direto ao banco de produção. O processo de deploy não deveria ser manual.

---

## 7. Assuma Comprometimento (Assume Breach)

Projete o sistema como se partes dele já estivessem comprometidas. A pergunta não é "como evitar comprometimento?" — é "quando houver comprometimento, como contemos o dano?"

```
Implicações arquiteturais:
  → Cifre dados em repouso — disco comprometido ≠ dados expostos
  → Log audit trail imutável — atacante com acesso ao app não pode apagar rastros
  → Segmente a rede — comprometer um serviço não dá acesso a todos
  → Tokens de curta duração — credencial roubada expira em minutos
  → Detecção de anomalias — comportamento fora do padrão gera alerta
```

```typescript
// Mesmo dentro da mesma VPC, autenticar inter-serviços
// Não assumir que tráfego interno é confiável — isso é Zero Trust

// Cada microserviço valida o token recebido
app.use(async (req, res, next) => {
  const token = req.headers["x-service-token"];
  if (!token) return res.status(401).send();

  // Valida que veio de um serviço legítimo com SPIFFE/mTLS ou JWT assinado
  const caller = await validateServiceIdentity(token);
  req.caller = caller;
  next();
});
```

---

## Padrões em Decisões de Design

```
Nova feature com dados sensíveis?
  → Qual camada de defense in depth protege esses dados?
  → Qual é o least privilege mínimo para operar?
  → O default da feature é seguro sem configuração extra?
  → Se a validação de permissão falhar, o comportamento nega acesso?
  → Quais campos expostos na API são estritamente necessários?

Nova integração com serviço externo?
  → Quais dados mínimos enviar? (minimização de superfície)
  → O que acontece se o serviço externo for comprometido? (assume breach)
  → A autenticação falha de forma segura?

Novo serviço de infraestrutura?
  → Qual é o menor IAM role possível?
  → Está acessível apenas de onde precisa estar?
  → Tem audit log habilitado?
```

---

## Conceitos Relacionados

[[threat-modeling]] · [[zero-trust]] · [[owasp-top10]] · [[criptografia-fundamentos]] · [[api-security]]

---

*Fonte: tech-mentor skill · tech-mentor-security · 2026-03-30*
