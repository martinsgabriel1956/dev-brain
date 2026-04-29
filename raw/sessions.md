---
date: 2026-04-17
tags: [tech-mentor, backend, auth, sessions, redis, cookies, mfa, webauthn, passkeys]
skill: tech-mentor-backend/references/auth
level: intermediário
---

# Auth Avançado — Sessions, MFA, WebAuthn/Passkeys e Workload Identity

## Contexto

JWT stateless tem limitações reais: revogação imediata é impossível sem state. Sessions server-side resolvem isso ao custo de state — que o Redis torna horizontal. MFA com TOTP é o mínimo aceitável hoje; WebAuthn/Passkeys é o padrão futuro sem senha. Workload Identity (SPIFFE/SPIRE) resolve autenticação serviço-a-serviço sem segredos compartilhados.

---

## Sessions Server-Side com Redis

```typescript
import express from "express";
import session from "express-session";
import RedisStore from "connect-redis";
import { Redis } from "ioredis";
import { randomBytes } from "crypto";

const redis = new Redis(process.env.REDIS_URL!);
const app = express();

// Session store no Redis — horizontal, persistente, revogável
app.use(session({
  store: new RedisStore({ client: redis, prefix: "sess:" }),
  secret: process.env.SESSION_SECRET!,  // mínimo 32 bytes aleatórios
  name: "__Host-session",               // __Host- prefix = Secure + Path=/ obrigatório
  resave: false,
  saveUninitialized: false,
  cookie: {
    httpOnly: true,          // inacessível via JavaScript — previne XSS
    secure: true,            // apenas HTTPS
    sameSite: "strict",      // previne CSRF em requisições cross-site
    maxAge: 7 * 24 * 60 * 60 * 1000,  // 7 dias
    path: "/"
  }
}));

// Declarar tipos para a sessão
declare module "express-session" {
  interface SessionData {
    userId: string;
    role: string;
    mfaVerified: boolean;
    createdAt: number;
    lastActivity: number;
  }
}

// Login — criar sessão
async function handleLogin(
  req: express.Request,
  res: express.Response
): Promise<void> {
  const { email, password } = req.body;

  const user = await authenticateUser(email, password);
  if (!user) {
    res.status(401).json({ error: "Invalid credentials" });
    return;
  }

  // Session fixation prevention — regenerar ID antes de escrever dados
  await new Promise<void>((resolve, reject) => {
    req.session.regenerate(err => err ? reject(err) : resolve());
  });

  req.session.userId = user.id;
  req.session.role = user.role;
  req.session.mfaVerified = false;
  req.session.createdAt = Date.now();
  req.session.lastActivity = Date.now();

  res.json({ success: true, requiresMfa: user.mfaEnabled });
}

// Middleware de autenticação
function requireAuth(req: express.Request, res: express.Response, next: express.NextFunction): void {
  if (!req.session.userId) {
    res.status(401).json({ error: "Unauthorized" });
    return;
  }

  // Absolute timeout — sessão não pode existir mais que 30 dias
  const SESSION_ABSOLUTE_TIMEOUT = 30 * 24 * 60 * 60 * 1000;
  if (Date.now() - req.session.createdAt > SESSION_ABSOLUTE_TIMEOUT) {
    req.session.destroy(() => {});
    res.status(401).json({ error: "Session expired" });
    return;
  }

  // Idle timeout — 2h sem atividade
  const SESSION_IDLE_TIMEOUT = 2 * 60 * 60 * 1000;
  if (Date.now() - req.session.lastActivity > SESSION_IDLE_TIMEOUT) {
    req.session.destroy(() => {});
    res.status(401).json({ error: "Session timed out" });
    return;
  }

  req.session.lastActivity = Date.now();
  next();
}

// Logout — destruir sessão no Redis imediatamente (revogação real)
async function handleLogout(req: express.Request, res: express.Response): Promise<void> {
  await new Promise<void>((resolve) => req.session.destroy(() => resolve()));
  res.clearCookie("__Host-session");
  res.json({ success: true });
}

// Revogar todas as sessões de um usuário (ex: "sair de todos os dispositivos")
async function revokeAllUserSessions(userId: string): Promise<void> {
  const keys = await redis.keys(`sess:*`);
  const pipeline = redis.pipeline();

  for (const key of keys) {
    pipeline.get(key);
  }

  const sessions = await pipeline.exec();

  const deleteOps = redis.pipeline();
  sessions?.forEach(([, value], index) => {
    if (!value) return;
    try {
      const sessionData = JSON.parse(value as string);
      if (sessionData.userId === userId) {
        deleteOps.del(keys[index]);
      }
    } catch {}
  });

  await deleteOps.exec();
}

async function authenticateUser(email: string, password: string): Promise<{ id: string; role: string; mfaEnabled: boolean } | null> {
  return null; // implementação real com bcrypt + prisma
}
```

---

## MFA com TOTP (Time-Based One-Time Password)

```typescript
import * as OTPAuth from "otpauth";
import QRCode from "qrcode";

// Gerar segredo TOTP para o usuário
async function setupMFA(userId: string, email: string): Promise<{ secret: string; qrCode: string; backupCodes: string[] }> {
  const totp = new OTPAuth.TOTP({
    issuer: "MyApp",
    label: email,
    algorithm: "SHA1",
    digits: 6,
    period: 30,
    secret: OTPAuth.Secret.generate(20)  // 160 bits — base32 encoded
  });

  const secret = totp.secret.base32;
  const otpAuthUrl = totp.toString();
  const qrCode = await QRCode.toDataURL(otpAuthUrl);

  // Backup codes — 10 códigos de uso único
  const backupCodes = Array.from({ length: 10 }, () =>
    randomBytes(5).toString("hex").toUpperCase()
  );

  // Salvar no banco (ANTES de confirmar com usuário)
  // secret + backupCodes criptografados com KMS/Vault
  await saveMFASetup(userId, secret, backupCodes);

  return { secret, qrCode, backupCodes };
}

// Verificar código TOTP durante login
async function verifyTOTP(userId: string, code: string): Promise<boolean> {
  const mfaData = await getMFAData(userId);
  if (!mfaData) return false;

  const totp = new OTPAuth.TOTP({
    algorithm: "SHA1",
    digits: 6,
    period: 30,
    secret: OTPAuth.Secret.fromBase32(mfaData.secret)
  });

  // delta = 1 → aceitar código do intervalo anterior/seguinte (clock drift de ±30s)
  const delta = totp.validate({ token: code, window: 1 });

  if (delta !== null) return true;

  // Tentar backup codes
  return verifyAndConsumeBackupCode(userId, code);
}

async function verifyAndConsumeBackupCode(userId: string, code: string): Promise<boolean> {
  const mfaData = await getMFAData(userId);
  if (!mfaData) return false;

  const codeIndex = mfaData.backupCodes.findIndex(bc => bc === code.toUpperCase());
  if (codeIndex === -1) return false;

  // Remover código usado — cada backup code é de uso único
  mfaData.backupCodes.splice(codeIndex, 1);
  await updateMFAData(userId, mfaData);
  return true;
}

async function saveMFASetup(userId: string, secret: string, backupCodes: string[]): Promise<void> {}
async function getMFAData(userId: string): Promise<{ secret: string; backupCodes: string[] } | null> { return null; }
async function updateMFAData(userId: string, data: { secret: string; backupCodes: string[] }): Promise<void> {}
```

---

## WebAuthn / Passkeys (FIDO2)

Autenticação sem senha — chave privada fica no dispositivo, nunca é transmitida:

```typescript
import {
  generateRegistrationOptions,
  verifyRegistrationResponse,
  generateAuthenticationOptions,
  verifyAuthenticationResponse
} from "@simplewebauthn/server";
import type {
  RegistrationResponseJSON,
  AuthenticationResponseJSON
} from "@simplewebauthn/types";

const RP_ID = "myapp.com";
const RP_NAME = "MyApp";
const ORIGIN = "https://myapp.com";

// REGISTRO — gerar challenge e registrar credencial
async function startRegistration(userId: string, userEmail: string) {
  const existingCredentials = await getUserCredentials(userId);

  const options = await generateRegistrationOptions({
    rpName: RP_NAME,
    rpID: RP_ID,
    userID: Buffer.from(userId),
    userName: userEmail,
    attestationType: "none",  // "direct" para verificar fabricante do autenticador
    excludeCredentials: existingCredentials.map(c => ({
      id: c.credentialId,
      type: "public-key"
    })),
    authenticatorSelection: {
      residentKey: "required",     // chave residente = passkey (sem username na autenticação)
      userVerification: "required" // biometria ou PIN obrigatório
    }
  });

  // Salvar challenge temporariamente (5 minutos)
  await redis.setex(`webauthn:challenge:${userId}`, 300, options.challenge);

  return options;
}

async function completeRegistration(
  userId: string,
  response: RegistrationResponseJSON
): Promise<void> {
  const expectedChallenge = await redis.get(`webauthn:challenge:${userId}`);
  if (!expectedChallenge) throw new Error("Challenge expired or not found");

  const verification = await verifyRegistrationResponse({
    response,
    expectedChallenge,
    expectedOrigin: ORIGIN,
    expectedRPID: RP_ID
  });

  if (!verification.verified || !verification.registrationInfo) {
    throw new Error("Registration verification failed");
  }

  const { credentialID, credentialPublicKey, counter } = verification.registrationInfo;

  // Salvar credencial — credentialPublicKey é a chave pública (segura de armazenar)
  await saveCredential(userId, {
    credentialId: Buffer.from(credentialID).toString("base64url"),
    publicKey: Buffer.from(credentialPublicKey).toString("base64url"),
    counter
  });

  await redis.del(`webauthn:challenge:${userId}`);
}

// AUTENTICAÇÃO
async function startAuthentication(userId?: string) {
  const allowCredentials = userId
    ? (await getUserCredentials(userId)).map(c => ({ id: c.credentialId, type: "public-key" as const }))
    : [];

  const options = await generateAuthenticationOptions({
    rpID: RP_ID,
    allowCredentials,
    userVerification: "required"
  });

  const challengeKey = userId
    ? `webauthn:auth:challenge:${userId}`
    : `webauthn:auth:challenge:${options.challenge}`;

  await redis.setex(challengeKey, 300, options.challenge);

  return options;
}

async function completeAuthentication(
  userId: string,
  response: AuthenticationResponseJSON
): Promise<boolean> {
  const expectedChallenge = await redis.get(`webauthn:auth:challenge:${userId}`);
  if (!expectedChallenge) throw new Error("Challenge expired");

  const credential = await getCredentialById(response.id);
  if (!credential) throw new Error("Credential not found");

  const verification = await verifyAuthenticationResponse({
    response,
    expectedChallenge,
    expectedOrigin: ORIGIN,
    expectedRPID: RP_ID,
    authenticator: {
      credentialID: Buffer.from(credential.credentialId, "base64url"),
      credentialPublicKey: Buffer.from(credential.publicKey, "base64url"),
      counter: credential.counter
    }
  });

  if (verification.verified) {
    // Atualizar counter — previne replay attacks
    await updateCredentialCounter(credential.credentialId, verification.authenticationInfo.newCounter);
    await redis.del(`webauthn:auth:challenge:${userId}`);
  }

  return verification.verified;
}

async function getUserCredentials(userId: string): Promise<Array<{ credentialId: string; publicKey: string; counter: number }>> { return []; }
async function saveCredential(userId: string, credential: { credentialId: string; publicKey: string; counter: number }): Promise<void> {}
async function getCredentialById(id: string): Promise<{ credentialId: string; publicKey: string; counter: number } | null> { return null; }
async function updateCredentialCounter(credentialId: string, counter: number): Promise<void> {}
```

---

## Workload Identity — SPIFFE/SPIRE (Serviço-a-Serviço sem Segredo)

```
Problema: como o serviço A prova para o serviço B que é quem diz ser, sem senha compartilhada?

SPIFFE: padrão de identidade para workloads — SPIFFE ID = "spiffe://trust-domain/workload"
SPIRE:  implementação de referência do SPIFFE

Fluxo:
1. SPIRE Agent roda em cada nó (como DaemonSet no K8s)
2. Workload se registra via Workload API (Unix domain socket)
3. SPIRE Agent verifica identidade via atestação (K8s SA token, AWS IAM role)
4. Emite SVID (SPIFFE Verifiable Identity Document) = certificado X.509 ou JWT
5. Workloads usam SVID para mTLS ou JWT Bearer — sem segredo estático
6. Certificados rotacionam automaticamente (por padrão a cada hora)

# Configuração SPIRE Server (simplificada)
server {
  bind_address = "0.0.0.0"
  bind_port = "8081"
  trust_domain = "mycompany.com"

  plugins {
    DataStore "sql" { connection_string = "postgres://..." }
    KeyManager "disk" { keys_path = "/run/spire/data/keys.json" }
    NodeAttestor "k8s_psat" {
      clusters = {
        "my-cluster" = {
          service_account_allow_list = ["spire:spire-agent"]
        }
      }
    }
  }
}

# SVID como JWT — usado como Bearer token em chamadas HTTP
```

```typescript
// Consumir SVID JWT em Node.js
import { WorkloadApiClient } from "@spiffe/spiffe-lib";

async function getServiceToken(targetService: string): Promise<string> {
  const client = new WorkloadApiClient();

  // audience = SPIFFE ID do serviço destino
  const jwtSvids = await client.fetchJWTSVIDs({
    audience: [`spiffe://mycompany.com/${targetService}`]
  });

  const svid = jwtSvids[0];
  return svid.token;
}

// Chamar outro serviço com identidade verificável
async function callPaymentService(orderId: string): Promise<void> {
  const token = await getServiceToken("payment-service");

  const response = await fetch("https://payment-service/process", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${token}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ orderId })
  });

  if (!response.ok) throw new Error(`Payment service error: ${response.status}`);
}

// Validar SVID no receptor (payment-service)
import { jose } from "jose";

async function validateSpiffeToken(token: string, expectedAudience: string): Promise<string> {
  const jwksUri = "https://spire-server:8081/keys";  // JWKS endpoint do SPIRE
  const JWKS = jose.createRemoteJWKSet(new URL(jwksUri));

  const { payload } = await jose.jwtVerify(token, JWKS, {
    audience: expectedAudience,
    issuer: "spiffe://mycompany.com"
  });

  return payload.sub as string;  // SPIFFE ID do caller: "spiffe://mycompany.com/order-service"
}
```

---

## Trade-offs

| Abordagem | Revogação | Estado | Escala | Complexidade |
|---|---|---|---|---|
| **JWT Stateless** | Impossível antes do TTL | Nenhum | Ilimitada | Baixa |
| **Session + Redis** | Imediata | Redis | Horizontal | Média |
| **TOTP MFA** | — | Nenhum | — | Baixa (lib) |
| **WebAuthn/Passkeys** | Revogar credencial no servidor | Credenciais no DB | Normal | Alta |
| **SPIFFE/SPIRE** | Certificado expira em horas | SPIRE Server | Alta | Alta |

## Quando Usar / Quando Evitar

**Sessions sobre JWT:** aplicações onde logout imediato é requisito de segurança (banking, healthcare), ou onde revogação de token é necessária.

**TOTP:** MFA mínimo aceitável. Vulnerável a phishing real-time (attacker faz relay do código). Usar WebAuthn quando possível.

**WebAuthn/Passkeys:** novos produtos onde UX superior e phishing-resistant são prioritários. Requer HTTPS, suporte do dispositivo.

**SPIFFE/SPIRE:** microsserviços com comunicação serviço-a-serviço frequente, ambientes K8s. Não usar em aplicações simples — a complexidade operacional é real.

**Evitar sessions in-memory:** múltiplos workers = sessões não compartilhadas. Sempre Redis.

## Conceitos Relacionados

[[distributed-locks]] · [[redis-avancado]] · [[zero-trust]] · [[jwt-oauth2]] · [[rate-limiting]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-17*
