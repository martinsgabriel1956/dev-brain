---
date: 2026-04-23
tags: [tech-mentor, security, identity, webauthn, passkeys, fido2]
skill: tech-mentor-security/references/passkeys-webauthn
level: intermediário
---

# Passkeys & WebAuthn

## Contexto

Senhas são o vetor de ataque mais explorado: phishing, credential stuffing, breach databases. MFA via SMS ou TOTP melhora, mas não elimina — SIM swapping e adversary-in-the-middle ainda funcionam.

WebAuthn (Web Authentication API) e passkeys eliminam a senha com criptografia assimétrica: a chave privada nunca sai do dispositivo do usuário, o servidor nunca vê credenciais — só verifica assinaturas. Phishing se torna tecnicamente impossível porque a credencial é vinculada ao domínio.

## Como Funciona

### Arquitetura Criptográfica

```
Registro:
  Dispositivo gera par de chaves (privada + pública)
  Chave privada → armazenada no authenticator (Secure Enclave / TPM / hardware key)
  Chave pública + credentialId → enviados ao servidor (Relying Party)
  Servidor armazena APENAS a chave pública

Autenticação:
  Servidor envia challenge (nonce aleatório)
  Authenticator assina o challenge com a chave privada
  Servidor verifica assinatura com a chave pública armazenada
  Chave privada nunca trafega na rede
```

**Por que phishing não funciona:** a assinatura inclui o `origin` (domínio). Uma credencial registrada em `bank.com` não pode ser usada em `bank-phishing.com` — o authenticator rejeita.

### Tipos de Authenticator

| Tipo | Exemplos | Característica |
|---|---|---|
| Platform | Face ID, Touch ID, Windows Hello | Vinculado ao dispositivo |
| Roaming | YubiKey, Google Titan | Portátil via USB/NFC/BT |
| Passkey (sincronizado) | iCloud Keychain, Google Password Manager | Multiplataforma via cloud |

### Implementação — Registro

```typescript
// Frontend — iniciar registro
async function registerPasskey(userId: string) {
  // 1. Buscar opções do servidor
  const options = await fetch("/auth/webauthn/register/options", {
    method: "POST",
    body: JSON.stringify({ userId })
  }).then(r => r.json());

  // 2. Criar credencial no dispositivo
  const credential = await navigator.credentials.create({
    publicKey: {
      challenge: base64ToBuffer(options.challenge),
      rp: { name: "Minha App", id: "app.example.com" },
      user: {
        id: base64ToBuffer(options.userId),
        name: options.email,
        displayName: options.name
      },
      pubKeyCredParams: [
        { type: "public-key", alg: -7 },   // ES256
        { type: "public-key", alg: -257 }  // RS256
      ],
      authenticatorSelection: {
        residentKey: "required",      // passkey sincronizável
        userVerification: "required"  // biometria ou PIN obrigatório
      },
      timeout: 60000
    }
  });

  // 3. Enviar resposta ao servidor para verificação e armazenamento
  await fetch("/auth/webauthn/register/verify", {
    method: "POST",
    body: JSON.stringify({
      credentialId: credential.id,
      response: {
        attestationObject: bufferToBase64(credential.response.attestationObject),
        clientDataJSON: bufferToBase64(credential.response.clientDataJSON)
      }
    })
  });
}
```

### Implementação — Autenticação

```typescript
// Frontend — autenticar com passkey
async function authenticateWithPasskey() {
  const options = await fetch("/auth/webauthn/login/options", {
    method: "POST"
  }).then(r => r.json());

  const assertion = await navigator.credentials.get({
    publicKey: {
      challenge: base64ToBuffer(options.challenge),
      rpId: "app.example.com",
      userVerification: "required",
      timeout: 60000
    }
  });

  // Servidor valida a assinatura
  const result = await fetch("/auth/webauthn/login/verify", {
    method: "POST",
    body: JSON.stringify({
      credentialId: assertion.id,
      response: {
        authenticatorData: bufferToBase64(assertion.response.authenticatorData),
        clientDataJSON: bufferToBase64(assertion.response.clientDataJSON),
        signature: bufferToBase64(assertion.response.signature)
      }
    })
  });

  const { sessionToken } = await result.json();
}
```

### Backend — Verificação (Node.js com @simplewebauthn/server)

```typescript
import { verifyRegistrationResponse, verifyAuthenticationResponse } from "@simplewebauthn/server";

// Verificar registro
const verification = await verifyRegistrationResponse({
  response: body,
  expectedChallenge: session.challenge,
  expectedOrigin: "https://app.example.com",
  expectedRPID: "app.example.com"
});

if (verification.verified) {
  await db.credential.create({
    data: {
      userId,
      credentialId: verification.registrationInfo.credentialID,
      publicKey: verification.registrationInfo.credentialPublicKey,
      counter: verification.registrationInfo.counter
    }
  });
}

// Verificar autenticação
const storedCredential = await db.credential.findUnique({
  where: { credentialId: body.credentialId }
});

const verification = await verifyAuthenticationResponse({
  response: body,
  expectedChallenge: session.challenge,
  expectedOrigin: "https://app.example.com",
  expectedRPID: "app.example.com",
  authenticator: {
    credentialPublicKey: storedCredential.publicKey,
    credentialID: storedCredential.credentialId,
    counter: storedCredential.counter  // detecta clonagem de authenticator
  }
});
```

### Schema de Banco

```sql
CREATE TABLE webauthn_credentials (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id       UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  credential_id TEXT NOT NULL UNIQUE,
  public_key    BYTEA NOT NULL,
  counter       BIGINT NOT NULL DEFAULT 0,  -- incrementa a cada autenticação
  device_type   TEXT,                        -- "platform" | "cross-platform"
  backed_up     BOOLEAN DEFAULT false,       -- é passkey sincronizado?
  name          TEXT,                        -- "MacBook Pro de João"
  created_at    TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  last_used_at  TIMESTAMP WITH TIME ZONE
);
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Phishing resistance | Vinculo criptográfico ao domínio | Não existe workaround para usuário cair em phishing |
| UX | Biometria é mais rápida que senha+OTP | Setup inicial pode confundir usuários não técnicos |
| Passkeys sincronizados | Funciona em múltiplos dispositivos | Depende de ecossistema (Apple/Google/Microsoft) |
| Hardware keys (YubiKey) | Máxima segurança, sem dependência cloud | Custo, pode ser perdida |
| Fallback | Necessário para device recovery | Fallback fraco (email link) é elo mais fraco |

## Quando Usar / Quando Evitar

**Usar quando:**
- Aplicações com dados sensíveis (financeiro, saúde, admin)
- Alto risco de phishing (executivos, times de segurança)
- Compliance que exige MFA phishing-resistant (NIST AAL3, FedRAMP High)

**Considerar:** manter senha+TOTP como fallback durante transição — usuários perdem acesso se único authenticator for perdido.

**Não substituir ainda se:** base de usuários em regiões/segmentos com pouco suporte a biometria — testar suporte antes de tornar obrigatório.

## Conceitos Relacionados

[[autenticacao-segura]] · [[oauth2-oidc-jwt]] · [[federated-identity]] · [[identity-iam-avancado]] · [[sessions]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-23*
