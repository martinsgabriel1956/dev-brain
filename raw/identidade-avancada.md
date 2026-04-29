---
date: 2026-04-17
tags: [tech-mentor, auth, identidade, sso, mfa, workload-identity, iam]
skill: tech-mentor-security/references/identity
level: avançado
---

# Identidade Avançada — SSO, MFA, Workload Identity, IAM, Casbin, SCIM

## SSO — Single Sign-On

### Contexto
SSO permite que o usuário autentique uma única vez e acesse múltiplos sistemas sem re-login. O protocolo SAML 2.0 é o padrão enterprise; OIDC Federation é a alternativa moderna.

```
SAML 2.0 Flow:
User → SP (Service Provider) → IdP (Identity Provider: Okta, ADFS)
                              ← SAML Assertion (XML assinado)
     ← Sessão criada

OIDC Federation (moderno):
User → App → Authorization Server → /authorize
                                  ← code
          → /token com code
          ← id_token + access_token
```

**Provider linking:** um usuário pode ter múltiplos identity providers vinculados à mesma conta.

```typescript
// Vinculação de providers (ex: Google + GitHub → mesma conta)
type LinkedProvider = {
  provider: "google" | "github" | "saml";
  externalId: string;
  linkedAt: Date;
};

// Ao fazer login com Google:
async function handleOAuthCallback(provider: string, externalId: string, email: string) {
  // Verifica se já existe uma conta com esse email
  let user = await userRepo.findByEmail(email);

  if (user) {
    // Vincula o provider à conta existente (se ainda não vinculado)
    await userRepo.addLinkedProvider(user.id, { provider, externalId });
  } else {
    user = await userRepo.create({ email });
    await userRepo.addLinkedProvider(user.id, { provider, externalId });
  }

  return issueTokens(user);
}
```

---

## MFA — Multi-Factor Authentication

### TOTP (Time-based One-Time Password)

```typescript
import { authenticator } from "otplib";

// Geração do segredo (ao ativar MFA)
async function setupMFA(userId: string) {
  const secret = authenticator.generateSecret();
  
  // Salvar criptografado no banco
  await userRepo.saveMFASecret(userId, await encrypt(secret));

  // Retornar QR code URI para o app autenticador
  const otpauthUrl = authenticator.keyuri(userEmail, "MyApp", secret);
  return { secret, otpauthUrl };
}

// Verificação do código TOTP
async function verifyTOTP(userId: string, code: string): Promise<boolean> {
  const encryptedSecret = await userRepo.getMFASecret(userId);
  const secret = await decrypt(encryptedSecret);
  return authenticator.check(code, secret);
}
```

### WebAuthn/FIDO2 — Passkeys

Passkeys substituem senha + TOTP por criptografia de chave pública. O autenticador (dispositivo) armazena a chave privada; o servidor armazena apenas a chave pública.

```typescript
import { generateRegistrationOptions, verifyRegistrationResponse } from "@simplewebauthn/server";

// 1. Registrar passkey
async function startPasskeyRegistration(userId: string, userEmail: string) {
  const options = await generateRegistrationOptions({
    rpName: "MyApp",
    rpID: "myapp.com",
    userID: userId,
    userName: userEmail,
    attestationType: "none",
    authenticatorSelection: {
      residentKey: "required",      // armazenar na chave — passkey completo
      userVerification: "required"  // exige biometria/PIN
    }
  });
  
  await redis.setEx(`webauthn:challenge:${userId}`, 120, options.challenge);
  return options;
}

// 2. Verificar e salvar credencial
async function finishPasskeyRegistration(userId: string, response: unknown) {
  const challenge = await redis.get(`webauthn:challenge:${userId}`);
  const verification = await verifyRegistrationResponse({
    response, expectedChallenge: challenge!, expectedOrigin: "https://myapp.com", expectedRPID: "myapp.com"
  });

  if (verification.verified) {
    await credentialRepo.save(userId, verification.registrationInfo!);
  }
  return verification.verified;
}
```

---

## Workload Identity — SPIFFE/SPIRE

### Contexto
Como serviços autenticam uns nos outros sem segredos (senhas, API keys) que podem vazar? **SPIFFE** (Secure Production Identity Framework For Everyone) define identidades para workloads via certificados X.509 de curta duração. **SPIRE** é a implementação de referência.

```
SPIFFE URI: spiffe://trust-domain/ns/production/sa/order-service

Fluxo:
1. SPIRE Agent roda em cada node
2. Ao iniciar, o pod prova sua identidade ao Agent (via atestação de node: K8s SA token)
3. Agent emite SVID (SPIFFE Verifiable Identity Document) — certificado X.509 de 1h
4. O serviço usa o SVID para mTLS com outros serviços
5. Sem secrets, sem rotação manual — o SVID expira e é renovado automaticamente
```

```yaml
# K8s + SPIRE — anotação no Pod para obter SVID
metadata:
  annotations:
    spiffe.io/federatesWith: "spiffe://partner-domain.com"
```

---

## IAM Avançado — Least Privilege e Just-in-Time Access

```
Least Privilege: cada serviço/usuário tem apenas as permissões mínimas necessárias

Errado:
  order-service → IAM role com S3:* em todos os buckets

Certo:
  order-service → IAM role com S3:GetObject apenas no bucket "order-invoices"
  s3:PutObject apenas na prefix "orders/${orderId}/*"

Just-in-Time (JIT):
  Permissões elevadas são concedidas temporariamente via request + aprovação
  Ex: DBA precisa de acesso root → solicita → aprovado por um peer → acesso por 1h
  Implementação: AWS IAM Identity Center, HashiCorp Boundary, CyberArk
```

---

## Casbin — Policy Engine Flexível

```typescript
import { newEnforcer } from "casbin";

// Modelo PERM (Policy, Effect, Request, Matchers)
// model.conf
// [request_definition]
// r = sub, obj, act
//
// [policy_definition]
// p = sub, obj, act
//
// [policy_effect]
// e = some(where (p.eft == allow))
//
// [matchers]
// m = r.sub == p.sub && r.obj == p.obj && r.act == p.act

const enforcer = await newEnforcer("model.conf", "policy.csv");

// policy.csv:
// p, alice, /orders, read
// p, alice, /orders, write
// p, bob, /orders, read

const canRead = await enforcer.enforce("alice", "/orders", "read"); // true
const canWrite = await enforcer.enforce("bob", "/orders", "write"); // false
```

---

## SCIM — Provisionamento Automático

SCIM 2.0 sincroniza usuários/grupos entre o IdP (Okta, Azure AD) e a aplicação — ao criar/desativar usuário no IdP, a aplicação é automaticamente atualizada.

```typescript
// Endpoint SCIM que o IdP chama
app.post("/scim/v2/Users", async (req, res) => {
  const { userName, name, emails, active } = req.body;
  
  const user = await userRepo.create({
    email: emails[0].value,
    displayName: `${name.givenName} ${name.familyName}`,
    active
  });

  res.status(201).json({
    id: user.id,
    schemas: ["urn:ietf:params:scim:schemas:core:2.0:User"],
    userName,
    active
  });
});

// Desprovisionar ao desativar no IdP
app.patch("/scim/v2/Users/:id", async (req, res) => {
  const { Operations } = req.body;
  const deactivate = Operations.find(op => op.path === "active" && op.value === false);
  
  if (deactivate) {
    await userRepo.deactivate(req.params.id);
    await sessionRepo.revokeAll(req.params.id); // revoga todas as sessões
  }

  res.json({ id: req.params.id });
});
```

## Conceitos Relacionados
[[oauth2-oidc-jwt]] · [[rbac-abac-rebac]] · [[zero-trust]] · [[secrets-management]] · [[service-mesh]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-17*
