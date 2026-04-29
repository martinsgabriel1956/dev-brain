---
date: 2026-03-30
tags: [tech-mentor, security, appsec, autenticação, jwt, oauth, mfa, passkeys]
skill: tech-mentor-security/references/appsec-runtime
level: fundamento
---

# Autenticação Segura

## Contexto

Autenticação é o ponto de entrada de qualquer sistema. Falhas aqui comprometem tudo que vem depois — não importa o quão seguro é o resto do código. JWT mal implementado, OAuth com flow inseguro, ou ausência de MFA em contas privilegiadas são os vetores de ataque mais explorados em breaches reais.

---

## Authn vs Authz — Distinção Fundamental

```
Authn (Authentication): quem é você?
  → Verificação de identidade: "sou o usuário ID 42"

Authz (Authorization): o que você pode fazer?
  → Verificação de permissão: "o usuário 42 pode deletar este recurso?"
```

Erro comum: validar que o token é válido (authn) e esquecer de verificar se o usuário tem permissão para aquela operação específica (authz). Broken Access Control (OWASP #1) é exatamente isso.

---

## JWT — O Que Ninguém Te Conta

JWT é stateless: o servidor valida o token sem consultar banco. O payload contém as claims assinadas com uma chave secreta.

### Anatomia

```
Header.Payload.Signature

Header:  { "alg": "HS256", "typ": "JWT" }
Payload: { "sub": "user-42", "role": "admin", "exp": 1234567890 }
Signature: HMAC-SHA256(base64(header) + "." + base64(payload), secret)
```

**Payload é Base64, não criptografado** — qualquer um com o token pode ler as claims. Nunca coloque senhas, PII sensível ou segredos no payload. Use JWE se precisar de confidencialidade.

### Problemas reais e mitigações

**1. Algoritmo `none` / algorithm confusion**:
```typescript
// ❌ não especificar algoritmo — parsers antigos aceitam alg: "none"
const payload = verify(token, secret);

// ✅ sempre especificar algoritmos permitidos
import { verify } from "jsonwebtoken";

const payload = verify(token, process.env.JWT_SECRET, {
  algorithms: ["HS256"],  // nunca vazio, nunca "none"
  issuer: "sua-api",
  audience: "seu-cliente"
});
```

**2. Revogação é difícil**:
JWT válido até expirar — não dá para invalidar antes sem manter denylist (o que torna o sistema stateful de novo).

```
Solução: tokens de curta duração + refresh tokens

Access Token:   TTL 15min–1h  → stateless, usado em cada request
Refresh Token:  TTL 7–30 dias → armazenado no banco (pode ser revogado)
                                 usado só para obter novo access token
```

**3. Onde armazenar**:
```
❌ localStorage    → acessível por XSS — qualquer script na página lê
❌ sessionStorage  → mesmo problema que localStorage

✅ httpOnly cookie → inacessível por JavaScript, enviado automaticamente
   + Secure flag  → só via HTTPS
   + SameSite=Lax → proteção contra CSRF
```

### Implementação correta de tokens

```typescript
// Access token — curta duração, stateless
function generateAccessToken(userId: string, role: string): string {
  return sign(
    { sub: userId, role },
    process.env.JWT_SECRET,
    { expiresIn: "15m", issuer: "sua-api", audience: "seu-cliente" }
  );
}

// Refresh token — longa duração, armazenado no banco para poder revogar
async function generateRefreshToken(userId: string): Promise<string> {
  const token = crypto.randomBytes(32).toString("hex");
  await db.refreshTokens.create({
    token: await bcrypt.hash(token, 10), // armazena hash, nunca plain text
    userId,
    expiresAt: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000) // 30 dias
  });
  return token;
}

// Refresh endpoint
app.post("/auth/refresh", async (req, res) => {
  const { refreshToken } = req.cookies;
  if (!refreshToken) return res.status(401).send();

  const stored = await db.refreshTokens.findValid(refreshToken);
  if (!stored) return res.status(401).send();

  // Rotação: invalidar o token usado, emitir novo par
  await db.refreshTokens.revoke(stored.id);
  const newRefresh = await generateRefreshToken(stored.userId);
  const newAccess = generateAccessToken(stored.userId, stored.user.role);

  res.cookie("refreshToken", newRefresh, { httpOnly: true, secure: true, sameSite: "lax" });
  res.json({ accessToken: newAccess });
});
```

---

## OAuth 2.1 / OIDC

**OAuth 2.0**: framework de *autorização* — permite que app A acesse recursos do usuário em app B sem revelar a senha.

**OIDC (OpenID Connect)**: camada de *autenticação* em cima do OAuth 2.0 — adiciona `id_token` com informações do usuário.

**OAuth 2.1** consolida melhores práticas: PKCE obrigatório para todos os flows, Implicit Flow removido, Resource Owner Password Credentials removido.

### Authorization Code Flow + PKCE — o único flow correto para web/mobile

```
1. App gera code_verifier (random) + code_challenge (SHA256 do verifier)

2. App redireciona usuário para Authorization Server:
   GET /authorize?
     client_id=...&
     redirect_uri=https://app.com/callback&
     response_type=code&
     scope=openid profile email&
     state={csrf_token}&      ← proteção anti-CSRF
     code_challenge={hash}&
     code_challenge_method=S256

3. Usuário autentica e autoriza

4. Authorization Server redireciona: /callback?code={auth_code}&state={csrf_token}
   App verifica que state bate com o gerado no passo 1

5. App troca code por tokens (server-side, nunca no browser):
   POST /token
     grant_type=authorization_code&
     code={auth_code}&
     code_verifier={original_verifier}  ← servidor verifica o hash
     redirect_uri=...
```

```typescript
// Geração do PKCE challenge
const codeVerifier = crypto.randomBytes(32).toString("base64url");
const codeChallenge = crypto
  .createHash("sha256")
  .update(codeVerifier)
  .digest("base64url");

// Armazenar code_verifier na sessão para usar no passo 5
req.session.codeVerifier = codeVerifier;
req.session.oauthState = crypto.randomBytes(16).toString("hex");
```

**Por que PKCE**: se o authorization_code for interceptado (MITM, redirect URI comprometida), o atacante não consegue trocá-lo por tokens — não tem o `code_verifier` original.

**Nunca use Implicit Flow**: tokens na URL ficam no histórico do browser, logs de servidor e referrer headers.

---

## RBAC vs ABAC — Modelo de Autorização

### RBAC (Role-Based Access Control)

Permissões associadas a roles; usuários recebem roles.

```typescript
// Simples e eficaz para a maioria dos SaaS B2B
function requireRole(...roles: string[]) {
  return (req: Request, res: Response, next: NextFunction) => {
    if (!roles.includes(req.user.role)) {
      return res.status(403).json({ error: "Insufficient permissions" });
    }
    next();
  };
}

app.delete("/admin/users/:id", requireRole("admin"), deleteUser);
app.get("/reports", requireRole("admin", "analyst"), getReports);
```

### ABAC (Attribute-Based Access Control)

Decisão baseada em atributos do usuário, recurso e contexto. Flexível mas complexo.

```
Política: ALLOW IF
  user.department == resource.department AND
  user.clearance >= resource.classification AND
  time.now BETWEEN 08:00 AND 18:00
```

### CASL — RBAC + ABAC em Node.js

```typescript
import { AbilityBuilder, createMongoAbility } from "@casl/ability";

function defineAbilitiesFor(user: User) {
  const { can, cannot, build } = new AbilityBuilder(createMongoAbility);

  if (user.role === "admin") {
    can("manage", "all");
  } else if (user.role === "editor") {
    can("read", "Post");
    can("update", "Post", { authorId: user.id }); // só os próprios posts
    cannot("delete", "Post");
  } else {
    can("read", "Post", { published: true }); // só posts publicados
  }

  return build();
}

// Verificação em qualquer camada
const ability = defineAbilitiesFor(req.user);
if (!ability.can("update", post)) {
  throw new ForbiddenError("Cannot update this post");
}
```

**Quando usar**:
- RBAC: papéis bem definidos, lógica simples → maioria dos SaaS
- ABAC: regras contextuais complexas → saúde, governo, financeiro
- Hybrid: RBAC para estrutura base + ABAC para exceções

---

## MFA — Multi-Factor Authentication

Autenticação com múltiplos fatores: algo que você sabe (senha) + algo que você tem (dispositivo) + algo que você é (biometria).

### TOTP — Time-based One-Time Password

Base do Google Authenticator, Authy, 1Password:

```typescript
import { authenticator } from "otplib";

// Setup — gerar secret por usuário (armazenar criptografado no banco)
const secret = authenticator.generateSecret();
const otpauthUrl = authenticator.keyuri(user.email, "Minha App", secret);
// otpauthUrl → QR code para o usuário escanear

// Verificação
function verifyTOTP(token: string, secret: string): boolean {
  return authenticator.verify({ token, secret });
}
```

**TOTP tem janela de tempo**: tokens válidos por 30s, com tolerância de ±1 janela (90s total) para compensar clock skew.

### WebAuthn / Passkeys — o futuro

Autenticação baseada em criptografia de chave pública. Chave privada nunca sai do dispositivo. Phishing-resistant por design — a chave é vinculada ao domínio.

```
Registro:
1. Browser gera par de chaves (privada no TPM/Secure Enclave do dispositivo)
2. Servidor armazena apenas a chave pública
3. Chave privada NUNCA sai do dispositivo — não vaza em breach do servidor

Autenticação:
1. Servidor envia challenge aleatório
2. Dispositivo assina challenge com chave privada (desbloqueado por biometria/PIN)
3. Servidor verifica assinatura com chave pública → autenticado

Por que é superior a senha:
  → Chave privada nunca exposta → zero credential stuffing
  → Vinculada ao domínio → phishing impossível (não funciona em domínio falso)
  → Sem senha para vazar em breach do servidor
```

```typescript
import { generateRegistrationOptions, verifyRegistrationResponse } from "@simplewebauthn/server";

// Gerar opções de registro
const options = await generateRegistrationOptions({
  rpName: "Minha App",
  rpID: "minhaapp.com",
  userID: user.id,
  userName: user.email,
  authenticatorSelection: {
    userVerification: "preferred",
    residentKey: "preferred"  // passkey sincronizável entre dispositivos
  }
});

// Verificar resposta do cliente após registro
const verification = await verifyRegistrationResponse({
  response: clientResponse,
  expectedChallenge,
  expectedOrigin: "https://minhaapp.com",
  expectedRPID: "minhaapp.com"
});

if (verification.verified) {
  await saveCredential(user.id, verification.registrationInfo);
}
```

**Passkey vs Security Key**:
- **Passkey**: sincroniza entre dispositivos (iCloud Keychain, Google Password Manager) — conveniente
- **YubiKey**: hardware dedicado, não sincroniza, mais seguro para contas de admin

---

## Senhas — Hashing Correto

```typescript
import bcrypt from "bcrypt";
import argon2 from "argon2";

// bcrypt — amplamente adotado, 12 rounds mínimo em produção
const hash = await bcrypt.hash(password, 12);
const valid = await bcrypt.compare(password, hash);

// Argon2id — recomendação atual do OWASP (mais resistente a GPU cracking)
const hash = await argon2.hash(password, {
  type: argon2.argon2id,
  memoryCost: 64 * 1024,  // 64MB
  timeCost: 3,
  parallelism: 1
});
const valid = await argon2.verify(hash, password);
```

**Nunca**: MD5, SHA1, SHA256 direto — sem salt, sem cost factor, reversíveis por rainbow table/GPU.

---

## Checklist de Autenticação

```
JWT:
[ ] algorithms: ["HS256"] ou ["RS256"] explicitamente definido
[ ] Access token: TTL de 15min a 1h
[ ] Refresh token: armazenado como hash no banco, revogável
[ ] Token armazenado em httpOnly Secure SameSite=Lax cookie

OAuth 2.0 / OIDC:
[ ] Authorization Code Flow + PKCE (nunca Implicit Flow)
[ ] state parameter para proteção anti-CSRF
[ ] redirect_uri em allowlist exata (sem wildcards)

Senhas:
[ ] bcrypt (12 rounds) ou Argon2id
[ ] Política mínima: 8 chars + maiúscula + número + especial
[ ] Reset de senha via token único de curta duração (15min)

MFA:
[ ] TOTP disponível para todos os usuários
[ ] Passkeys como opção (2025: suporte >95% dos browsers)
[ ] Contas admin: MFA obrigatório

Geral:
[ ] Rate limiting em login, signup, reset de senha
[ ] Account lockout após N tentativas falhas (com unlock por email)
[ ] Audit log de todos os eventos de autenticação
[ ] timingSafeEqual para comparação de tokens
```

---

## Conceitos Relacionados

[[owasp-top10]] · [[criptografia-fundamentos]] · [[secrets-management]] · [[zero-trust]] · [[api-security]]

---

*Fonte: tech-mentor skill · tech-mentor-security · 2026-03-30*
