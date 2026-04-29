---
date: 2026-04-23
tags: [tech-mentor, security, identity, saml, oidc, sso, scim]
skill: tech-mentor-security/references/federated-identity
level: avançado
---

# Federated Identity

## Contexto

Federated identity resolve o problema de múltiplos sistemas precisando autenticar o mesmo usuário sem que cada sistema gerencie suas próprias credenciais. O usuário tem uma identidade em um Identity Provider (IdP) — Google, Okta, Azure AD — e os sistemas (Service Providers / Relying Parties) confiam nessa identidade via protocolo padronizado.

É a base de SSO (Single Sign-On) enterprise e de login social. Sem federação, cada aplicação tem seu próprio silo de credenciais — um pesadelo operacional e de segurança.

## Como Funciona

### SAML 2.0 vs OIDC — Quando Usar Cada Um

| Critério | SAML 2.0 | OIDC |
|---|---|---|
| Formato | XML assinado | JWT (JSON) |
| Contexto dominante | Enterprise legacy (SAP, Salesforce, Workday) | APIs modernas, mobile, SPAs |
| Complexidade | Alta (XML, metadata, bindings) | Baixa (JSON, REST) |
| Mobile | Ruim | Nativo |
| Iniciação | IdP-initiated ou SP-initiated | SP-initiated (padrão) |
| Quando escolher | Integrar com sistema enterprise legado | Tudo novo |

### SAML 2.0 — Fluxo SP-Initiated

```
1. Usuário acessa app (SP)
2. SP gera AuthnRequest e redireciona para IdP
3. Usuário autentica no IdP
4. IdP gera SAML Assertion (XML assinado) e POST para SP
5. SP valida assinatura e extrai atributos (email, groups, roles)
6. SP cria sessão local
```

```xml
<!-- SAML Assertion — estrutura simplificada -->
<samlp:Response>
  <saml:Assertion>
    <saml:Subject>
      <saml:NameID Format="emailAddress">user@company.com</saml:NameID>
    </saml:Subject>
    <saml:AttributeStatement>
      <saml:Attribute Name="groups">
        <saml:AttributeValue>engineering</saml:AttributeValue>
        <saml:AttributeValue>admin</saml:AttributeValue>
      </saml:Attribute>
    </saml:AttributeStatement>
    <!-- Assinado com chave privada do IdP -->
  </saml:Assertion>
</samlp:Response>
```

### OIDC — Federação Moderna

OIDC sobre OAuth 2.0: o Authorization Code Flow com PKCE é o padrão para federação segura.

```typescript
// Relying Party (RP) — iniciar federação OIDC
const config = await fetch(`${IDP_URL}/.well-known/openid-configuration`);
// Retorna: authorization_endpoint, token_endpoint, jwks_uri, userinfo_endpoint

// Redirect para IdP
const authUrl = new URL(config.authorization_endpoint);
authUrl.searchParams.set("client_id", CLIENT_ID);
authUrl.searchParams.set("redirect_uri", CALLBACK_URL);
authUrl.searchParams.set("scope", "openid email profile");
authUrl.searchParams.set("response_type", "code");
authUrl.searchParams.set("code_challenge", codeChallenge);      // PKCE
authUrl.searchParams.set("code_challenge_method", "S256");
authUrl.searchParams.set("state", csrfToken);

// Após callback — trocar code por tokens
const tokens = await fetch(config.token_endpoint, {
  method: "POST",
  body: new URLSearchParams({
    grant_type: "authorization_code",
    code: callbackCode,
    code_verifier: codeVerifier,  // PKCE
    client_id: CLIENT_ID,
    redirect_uri: CALLBACK_URL
  })
});

// ID Token: JWT com claims do usuário
// { sub, email, name, groups, iat, exp, iss, aud }
```

### SSO Federado — Múltiplos IdPs

```
Cenário enterprise: empresa tem Okta (colaboradores) + Azure AD (parceiros) + Google (clientes)

Arquitetura:
  Cliente → App → Identity Router (ex: Auth0, Keycloak)
                        ↓
           ┌────────────┼────────────┐
         Okta      Azure AD      Google
         (SAML)     (OIDC)      (OIDC)

Identity Router:
- Normaliza identidades de múltiplos IdPs para um formato único
- Gerencia home realm discovery (qual IdP usar?)
- Mantém sessão federada unificada
```

### SCIM — Provisionamento Automático

SCIM (System for Cross-domain Identity Management) automatiza criação/atualização/desativação de usuários entre IdP e apps.

```http
# SCIM 2.0 — criar usuário
POST /scim/v2/Users
{
  "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
  "userName": "joao.silva@company.com",
  "name": { "givenName": "João", "familyName": "Silva" },
  "emails": [{ "value": "joao.silva@company.com", "primary": true }],
  "groups": [{ "value": "engineering" }],
  "active": true
}

# Desativar ao sair da empresa (triggered pelo IdP)
PATCH /scim/v2/Users/{id}
{ "Operations": [{ "op": "replace", "path": "active", "value": false }] }
```

**Sem SCIM:** offboarding manual — ex-funcionário pode manter acesso por dias/semanas. Com SCIM: desativação no IdP propaga para todas as apps em minutos.

### Entra External ID / CIAM

Para B2C (Customer Identity): Azure Entra External ID, Auth0, Cognito.

```
CIAM resolve:
- Login social (Google, Facebook, Apple)
- Self-service registration com email verification
- MFA opcional/obrigatório por risk score
- Branding customizado
- Escalabilidade (milhões de usuários)
- Compliance (GDPR consent flows built-in)
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| SSO | Uma credencial, menos phishing | Single point of failure (IdP down = tudo down) |
| SCIM | Offboarding automático | Implementação requer suporte no app |
| SAML | Suporte universal legacy | XML verboso, debugging difícil |
| OIDC | Simples, mobile-friendly | Menos suporte em sistemas legados |
| IdP externo (Okta/Auth0) | Maturidade, compliance pronto | Vendor lock-in, custo por MAU |

## Quando Usar / Quando Evitar

**SAML:** integração com sistemas enterprise já existentes (Workday, Salesforce, ServiceNow). Não escolher para sistemas novos.

**OIDC:** tudo novo — APIs, SPAs, mobile. Padrão a seguir.

**SCIM:** qualquer empresa com > 50 usuários em múltiplas apps. Offboarding manual não escala e é risco de segurança.

**Próprio IdP vs terceiro:** construir IdP próprio só faz sentido em escala massiva (> 100M MAU) ou requisitos regulatórios que impedem terceiros. Nos outros casos, usar Auth0/Okta/Entra.

## Conceitos Relacionados

[[autenticacao-segura]] · [[oauth2-oidc-jwt]] · [[identity-iam-avancado]] · [[passkeys-webauthn]] · [[rbac-abac-rebac]] · [[zero-trust]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-23*
