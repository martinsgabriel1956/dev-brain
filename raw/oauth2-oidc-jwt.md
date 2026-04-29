---
date: 2026-04-13
tags: [tech-mentor, auth, oauth2, oidc, jwt, autenticacao]
skill: tech-mentor-security/references/auth
level: intermediário
---
# OAuth2, OIDC e JWT

## Contexto

**OAuth2** é um protocolo de **autorização** (delegação de acesso) — não de autenticação. Permite que um app acesse recursos em nome de um usuário sem ver a senha.

**OIDC (OpenID Connect)** é uma camada de **autenticação** sobre OAuth2 — adiciona o ID Token (quem é o usuário).

**JWT** é o formato de token usado por ambos — mas é um detalhe de implementação, não o protocolo em si.

A confusão comum: "Login com Google usa OAuth2" — na verdade usa OIDC (que é OAuth2 + autenticação).

## OAuth2 — Os Flows

### Authorization Code (com PKCE) — Para SPAs e Mobile

O fluxo mais seguro para apps que não podem guardar secrets:

```
User → [clica "Login com Google"]
  ↓
App → GET /authorize?
        client_id=abc
        &redirect_uri=https://app.com/callback
        &scope=openid email profile
        &response_type=code
        &code_challenge=BASE64(SHA256(verifier))   ← PKCE
        &code_challenge_method=S256
  ↓
Google → autenticação + consentimento
  ↓
Google → redirect para https://app.com/callback?code=XYZ
  ↓
App → POST /token
        code=XYZ
        &code_verifier=original_verifier            ← PKCE
        &client_id=abc
        &grant_type=authorization_code
  ↓
Google → { access_token, id_token, refresh_token }
```

**Por que PKCE?** Impede que um código de autorização interceptado seja trocado por token — o `code_verifier` só o app original tem.

### Client Credentials — Para M2M (serviço → serviço)

```typescript
// Service A autenticando com Service B
async function getServiceToken(): Promise<string> {
  const response = await fetch(`${env.AUTH_SERVER}/oauth/token`, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      grant_type: "client_credentials",
      client_id: env.CLIENT_ID,
      client_secret: env.CLIENT_SECRET,
      scope: "orders:read orders:write"
    })
  });

  const { access_token, expires_in } = await response.json();
  return access_token;
}
```

### Device Flow — Para dispositivos sem browser (TV, CLI)

```
1. Device → POST /device/code → { device_code, user_code: "ABCD-1234", verification_uri }
2. Device → mostra "Acesse example.com/device e digite ABCD-1234"
3. User → acessa no celular, digita código, autentica
4. Device → polling: POST /token?device_code=... até receber o token
```

## JWT — Estrutura e Segurança

### Anatomia

```
header.payload.signature

Header:  { "alg": "RS256", "typ": "JWT", "kid": "key-id-2024" }
Payload: {
  "sub": "user-uuid-123",           ← subject (user ID)
  "iss": "https://auth.example.com", ← issuer
  "aud": "https://api.example.com",  ← audience
  "exp": 1704067200,                 ← expiration (Unix timestamp)
  "iat": 1704063600,                 ← issued at
  "jti": "unique-token-id",          ← JWT ID (para revogação)
  "email": "alice@example.com",
  "roles": ["user", "admin"]
}
Signature: RS256(base64(header) + "." + base64(payload), private_key)
```

### Validação Correta

```typescript
import { jwtVerify, createRemoteJWKSet } from "jose";

// Busca chaves públicas do Identity Provider (rotação automática)
const JWKS = createRemoteJWKSet(new URL("https://auth.example.com/.well-known/jwks.json"));

async function validateToken(token: string): Promise<JWTClaims> {
  const { payload } = await jwtVerify(token, JWKS, {
    issuer: "https://auth.example.com",    // valida iss
    audience: "https://api.example.com",   // valida aud
    algorithms: ["RS256"]                  // RS256, não HS256 (assimétrico)
  });

  // jose valida exp automaticamente
  return payload as JWTClaims;
}
```

**Por que RS256 e não HS256?**
- HS256: mesma chave para assinar e verificar → API precisa da chave secreta → risco de vazamento
- RS256: private key só no auth server, public key para qualquer API verificar → mais seguro

### Revogação de JWT

JWTs são stateless por design — não tem como "invalidar" um token antes do `exp`. Soluções:

```typescript
// Opção 1 — Token curto (1h) + Refresh Token (7d httpOnly cookie)
// Revogação "aproximada" — usuário espera até exp do access token

// Opção 2 — Denylist por JTI (para tokens críticos como admin)
async function validateToken(token: string): Promise<JWTClaims> {
  const claims = await verifySignature(token);

  // Verifica se JTI foi revogado
  const isRevoked = await redis.exists(`revoked:${claims.jti}`);
  if (isRevoked) throw new TokenRevokedError();

  return claims;
}

async function revokeToken(jti: string, remainingTtl: number): Promise<void> {
  await redis.setex(`revoked:${jti}`, remainingTtl, "1");
}
```

### Rotação de Chaves

```typescript
// JWK Set — permite múltiplas chaves ativas simultaneamente
// O header do JWT tem "kid" (key ID) para indicar qual chave usou

// Processo de rotação sem downtime:
// 1. Gere nova chave, adicione ao JWKS (mantendo a antiga)
// 2. Configure o auth server para assinar novos tokens com a nova chave
// 3. Aguarde expiração de todos os tokens assinados com a chave antiga
// 4. Remova a chave antiga do JWKS
```

## OIDC — Adicionando Autenticação ao OAuth2

```typescript
// ID Token — prova de autenticação (quem é o usuário)
// Diferente do Access Token (o que o usuário pode fazer)

type IDToken = {
  sub: string;         // user unique identifier
  iss: string;         // identity provider URL
  aud: string;         // client_id da sua aplicação
  exp: number;
  iat: number;
  nonce: string;       // anti-replay
  email: string;
  email_verified: boolean;
  name: string;
  picture: string;
};

// UserInfo endpoint — dados adicionais do usuário
async function getUserInfo(accessToken: string): Promise<UserProfile> {
  const response = await fetch("https://auth.example.com/userinfo", {
    headers: { Authorization: `Bearer ${accessToken}` }
  });
  return response.json();
}
```

## Session Management Seguro

```typescript
// Access Token: curto (1h), em memória no cliente (não localStorage)
// Refresh Token: longo (7d), httpOnly Secure cookie

// Backend — endpoint para renovar access token
app.post("/auth/refresh", async (req, res) => {
  const refreshToken = req.cookies.refresh_token;  // httpOnly cookie
  if (!refreshToken) return res.status(401).json({ error: "No refresh token" });

  const newTokens = await authServer.refreshAccessToken(refreshToken);

  // Rotation: invalida o refresh token antigo, emite novo
  res.cookie("refresh_token", newTokens.refreshToken, {
    httpOnly: true,
    secure: true,
    sameSite: "strict",
    maxAge: 7 * 24 * 60 * 60 * 1000  // 7 dias
  });

  res.json({ accessToken: newTokens.accessToken });
});
```

## Trade-offs

| Aspecto | JWT Stateless | Session (Redis) |
|---|---|---|
| Escala | Não precisa de shared store | Precisa de Redis compartilhado |
| Revogação | Difícil (esperar exp) | Instantânea (delete da sessão) |
| Tamanho | Maior (claims no token) | Menor (só session ID no cookie) |
| Latência | Sem I/O para validar | Round-trip ao Redis |
| Quando usar | APIs públicas, microsserviços | Admin panels, fluxos sensíveis |

## Conceitos Relacionados

[[rbac-abac]] · [[zero-trust]] · [[autenticacao-segura]] · [[api-security]] · [[secrets-management]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-13*
