---
date: 2026-04-01
tags: [tech-mentor, security, zero-trust, ztna, mtls, spiffe, beyondcorp]
skill: tech-mentor-security/references/ztna-advanced
level: intermediário
---

# Zero Trust

## Contexto

O modelo tradicional (castle-and-moat) assume que tudo dentro da rede é confiável. Zero Trust elimina essa premissa — **nunca confie, sempre verifique**, independente de onde a requisição vem.

**Por que o modelo antigo falha:**
- VPN é um túnel, não controle de acesso — qualquer device na rede tem acesso irrestrito
- SaaS colocou os dados fora da rede corporativa
- Supply chain attacks: o atacante já está "dentro" antes de você perceber
- Uma credencial comprometida → lateral movement livre pela rede

## Como Funciona

### Os 7 Pilares (CISA)

| Pilar | O que significa na prática |
|---|---|
| Identidade | MFA obrigatório + SSO + acesso condicional |
| Dispositivo | Postura do device validada antes do acesso (MDM, antivírus, disco criptografado) |
| Rede | Micro-segmentação — serviços só falam com quem precisam |
| Aplicação | Autorização por workload, não por rede |
| Dados | Classificação + proteção dos dados em si |
| Visibilidade | Tudo logado, anomalias detectadas |
| Automação | Resposta a incidentes automatizada |

### Acesso Condicional — a lógica central

```
Permitir acesso SE:
  ✅ Usuário autenticado com MFA (FIDO2 para sistemas críticos)
  AND ✅ Dispositivo gerenciado (MDM) + postura COMPLIANT
  AND ✅ Horário e localização dentro do esperado
  AND ✅ IP não em lista de bloqueio

Caso contrário: negar ou exigir step-up auth
```

Isso é o que o **BeyondCorp** do Google implementou em 2011 após o Operation Aurora — eliminaram a VPN e basearam tudo em identidade + postura do device.

## Código de Referência

### Usuários → Apps internas: Cloudflare Access

Em vez de expor apps internas ao público, o Cloudflare fica na frente como proxy e define políticas por identidade:

```yaml
# Terraform: policy para app interna
resource "cloudflare_access_application" "internal_app" {
  name             = "Dashboard Interno"
  domain           = "dashboard.internal.company.com"
  session_duration = "8h"
}

resource "cloudflare_access_policy" "employees_only" {
  application_id = cloudflare_access_application.internal_app.id
  name           = "Apenas Funcionários"
  decision       = "allow"

  include {
    email_domain        = ["company.com"]
    identity_provider_id = var.okta_idp_id
  }
  require {
    auth_method = "mfa"
  }
  exclude {
    country = ["CN", "RU", "KP"]
  }
}
```

### Engenheiros → Infra: Tailscale

Substitui VPN corporativa com mesh baseada em identidade. Default deny — tudo não listado é bloqueado:

```json
{
  "acls": [
    { "action": "accept", "src": ["group:developers"], "dst": ["tag:staging:*"] },
    { "action": "accept", "src": ["group:sre"],        "dst": ["tag:production:22", "tag:production:5432"] }
  ]
}
```

### Serviço → Serviço: mTLS com SPIFFE/SPIRE + Istio

Sem segredos compartilhados — identidade criptográfica por workload.

**SPIFFE ID format:**
```
spiffe://company.com/ns/payments/sa/checkout-service
```

```yaml
# Força mTLS em todo o namespace payments
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: payments
spec:
  mtls:
    mode: STRICT

---
# Checkout só aceita chamadas de order-service
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: checkout-authz
  namespace: payments
spec:
  selector:
    matchLabels:
      app: checkout-service
  rules:
    - from:
        - source:
            principals:
              - "cluster.local/ns/orders/sa/order-service"
      to:
        - operation:
            methods: ["POST"]
            paths: ["/v1/checkout"]
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Segurança | Lateral movement quase impossível | Complexidade operacional alta |
| Usabilidade | SSO centralizado é melhor que múltiplas senhas | Onboarding de dispositivos tem atrito |
| Custo | Reduz blast radius de incidentes | Ferramentas (Okta, Cloudflare Access) têm custo |
| Observabilidade | Tudo logado por design | Volume de logs aumenta muito |

## Modelo de Maturidade (CISA ZTM)

| Pilar | Traditional | Initial | Advanced | Optimal |
|---|---|---|---|---|
| Identidade | Senha + VPN | MFA básico | Acesso condicional | Adaptive auth contínuo |
| Dispositivo | Sem gestão | Inventário básico | MDM + compliance | Attestation contínuo |
| Rede | Perímetro | Macro-segmentação | Micro-segmentação | Software-defined, dinâmica |
| Aplicação | Acesso implícito | SSO | Authz por recurso | Just-in-time access |

## Quando Usar / Quando Evitar

**Use quando:**
- Empresa com trabalho remoto ou híbrido
- Múltiplos ambientes cloud + SaaS
- Requisitos de compliance (SOC 2, ISO 27001)
- Microserviços com comunicação service-to-service

**Evite ou adie quando:**
- Time pequeno sem capacidade operacional — a complexidade pode superar o benefício
- Ambiente monolítico simples

## Conceitos Relacionados

[[autenticacao-segura]] · [[kubernetes-security]] · [[cloud-security]] · [[identity-iam-avancado]] · [[secure-design-patterns]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-01*
