---
date: 2026-04-23
tags: [tech-mentor, security, identity, iam, pam, oauth]
skill: tech-mentor-security/references/identity-iam-avancado
level: avançado
---

# Identity & IAM Avançado

## Contexto

IAM básico (username + password + RBAC simples) não escala para sistemas com múltiplos atores: usuários humanos, service accounts, workers, pipelines de CI, lambdas, e APIs de parceiros. Cada ator tem necessidades diferentes de autenticação, autorização, e ciclo de vida de credencial.

IAM avançado resolve: como dar acesso mínimo, por tempo limitado, com auditoria completa, para qualquer tipo de identidade — humana ou máquina.

## Como Funciona

### Privileged Access Management (PAM)

PAM controla o acesso privilegiado — aquele que pode causar dano sistêmico (root, DBA, prod access).

```
Engenheiro solicita acesso ao banco de produção
  ↓
PAM system (HashiCorp Boundary, CyberArk, AWS SSM)
  ↓
Aprova com base em policy (horário, aprovação de manager, razão)
  ↓
Gera credencial temporária com TTL (ex: 1h)
  ↓
Sessão gravada em audit log
  ↓
Credencial expirada automaticamente
```

**Just-in-Time (JIT) Access:** zero standing privilege — ninguém tem acesso permanente a sistemas críticos. Acesso solicitado, aprovado, concedido por tempo limitado, revogado.

```yaml
# HashiCorp Boundary — target de acesso ao banco
resource "boundary_target" "postgres_prod" {
  name         = "postgres-prod"
  type         = "tcp"
  default_port = 5432
  session_max_seconds       = 3600   # 1h máximo
  session_connection_limit  = 1
  host_set_ids = [boundary_host_set.postgres.id]
}
```

### Machine Identity

Service accounts, lambdas e containers precisam de identidade — mas não podem ter senha hardcoded.

```
Opções por plataforma:
- AWS:   IAM Roles for Service Accounts (IRSA) / EC2 Instance Profiles
- GCP:   Workload Identity Federation
- Azure: Managed Identity
- K8s:   ServiceAccount + OIDC token projetion
- CI/CD: OIDC token do provider (GitHub Actions → AWS sem secret)
```

**GitHub Actions → AWS sem secret permanente:**
```yaml
jobs:
  deploy:
    permissions:
      id-token: write  # permite gerar OIDC token
    steps:
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789:role/github-deploy
          aws-region: us-east-1
          # Sem AWS_SECRET_ACCESS_KEY — usa OIDC token temporário
```

### OAuth 2.1 Avançado

OAuth 2.1 consolida as melhores práticas do 2.0 e torna obrigatório o que antes era opcional:

| Mudança | OAuth 2.0 | OAuth 2.1 |
|---|---|---|
| PKCE | Opcional | **Obrigatório** para todos os flows |
| Implicit flow | Permitido | **Removido** |
| Resource Owner Password | Permitido | **Removido** |
| Redirect URI | Partial match | **Exact match** obrigatório |
| Refresh token rotation | Opcional | **Obrigatório** |

**DPoP (Demonstrating Proof of Possession):** vincula o access token à chave privada do cliente — token roubado é inútil sem a chave.

```typescript
// DPoP header — prova de posse da chave
const dpopProof = await createDpopProof({
  method: "POST",
  url: "https://api.example.com/resource",
  privateKey: clientPrivateKey  // nunca sai do cliente
});

fetch("https://api.example.com/resource", {
  headers: {
    Authorization: `DPoP ${accessToken}`,
    DPoP: dpopProof
  }
});
```

**Token Exchange (RFC 8693):** permite trocar um token por outro com escopo diferente — útil para service-to-service com impersonation controlado.

```http
POST /token
grant_type=urn:ietf:params:oauth:grant-type:token-exchange
subject_token=<user_token>
subject_token_type=urn:ietf:params:oauth:token-type:access_token
requested_token_type=urn:ietf:params:oauth:token-type:access_token
scope=downstream-service:read
```

### SPIFFE / SPIRE — Workload Identity

SPIFFE (Secure Production Identity Framework for Everyone) dá identidade criptográfica a workloads — independente de IP, hostname ou rede.

```
Cada workload recebe um SVID (SPIFFE Verifiable Identity Document):
  spiffe://example.org/ns/prod/sa/payment-service

SPIRE agent atesta a identidade do workload via:
- Kubernetes: ServiceAccount token
- AWS: EC2 metadata / EKS IRSA
- On-prem: node attestation

SVID é um certificado X.509 ou JWT com TTL curto (minutos/horas)
Renovado automaticamente — zero intervenção humana
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| JIT vs standing access | Superfície de ataque mínima | Latência no acesso (aprovação) |
| SPIFFE/SPIRE | Identity agnóstica de infra | Complexidade operacional do SPIRE server |
| DPoP | Tokens roubados são inúteis | Implementação mais complexa no cliente |
| Machine identity (OIDC) | Zero secrets hardcoded | Dependência do provider de OIDC |

## Quando Usar / Quando Evitar

**JIT Access:** qualquer sistema com acesso privilegiado a prod. Zero standing privilege é o padrão em empresas com compliance maduro.

**SPIFFE/SPIRE:** microserviços que precisam de mTLS automático sem gerenciar certificados manualmente. Alternativa ao service mesh para identity layer.

**DPoP:** APIs públicas high-value onde token theft é ameaça real. Não vale o overhead para APIs internas.

## Conceitos Relacionados

[[autenticacao-segura]] · [[oauth2-oidc-jwt]] · [[zero-trust]] · [[secrets-management]] · [[rbac-abac-rebac]] · [[federated-identity]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-23*
