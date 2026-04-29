---
date: 2026-04-01
tags: [tech-mentor, security, devsecops, sast, dast, sca, pipeline, ci-cd, opa, policy-as-code]
skill: tech-mentor-security/references/devsecops-pipeline
level: intermediário
---

# DevSecOps Pipeline

## Contexto

O modelo clássico faz pentest antes de ir pra prod — lento, caro e cria atrito. DevSecOps move os controles para dentro do pipeline: cada commit é verificado, cada dependência auditada, cada imagem escaneada. O princípio é **shift left**: encontrar vulnerabilidades no momento mais barato para corrigir.

## Como Funciona

### Modelo de Gates de Segurança

```
Commit → SAST → Dependency Scan → Build → Container Scan → Deploy Staging
  ↓         ↓            ↓           ↓             ↓               ↓
Code      Secrets     SCA/CVEs    IaC Scan     Image CVEs      DAST
```

Cada etapa pode bloquear o pipeline. Nenhum artefato com vulnerabilidade crítica chega em produção.

## Código de Referência

### SAST — Static Application Security Testing

Analisa código sem executar. Detecta: SQL injection, XSS, hardcoded secrets, path traversal.

| Linguagem | Ferramenta | Destaque |
|---|---|---|
| Multi | **Semgrep** | Muito rápido, regras customizáveis |
| JS/TS | ESLint security plugin | Integra no dev workflow |
| Python | Bandit | Simples, direto |
| Go | gosec | Alta qualidade |
| IaC | Checkov / tfsec | CIS benchmarks prontos |

```yaml
# GitHub Actions — Semgrep
- name: Semgrep SAST
  uses: returntocorp/semgrep-action@v1
  with:
    config: >-
      p/owasp-top-ten
      p/secrets
      p/javascript

# IaC com Checkov
- name: Checkov IaC Scan
  uses: bridgecrewio/checkov-action@master
  with:
    directory: terraform/
    framework: terraform
    soft_fail: false
```

### SCA — Software Composition Analysis

Vulnerabilidades em dependências de terceiros (CVEs). Também verifica licenças — GPL em produto comercial é problema jurídico.

**Política de CVEs:**
```
CRITICAL (CVSS ≥ 9.0): Bloqueia pipeline — fix obrigatório antes de merge
HIGH     (CVSS 7-8.9): Bloqueia pipeline — fix em 7 dias ou exceção documentada
MEDIUM   (CVSS 4-6.9): Warning — fix em 30 dias
LOW      (CVSS < 4):   Informativo — backlog
```

```yaml
# .github/dependabot.yml — PRs automáticos de update
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
```

```bash
# Trivy — CVEs + secrets + config (o mais completo open source)
trivy fs . --exit-code 1 --severity HIGH,CRITICAL

# npm nativo
npm audit --audit-level=high
```

### Container Image Scanning

```yaml
- name: Build Docker image
  run: docker build -t meu-app:${{ github.sha }} .

- name: Scan com Trivy
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: meu-app:${{ github.sha }}
    severity: CRITICAL,HIGH
    exit-code: '1'

- name: Upload SARIF (aparece na aba Security do GitHub)
  uses: github/codeql-action/upload-sarif@v3
  with:
    sarif_file: trivy-results.sarif
```

**Dockerfile hardening — reduz superfície de ataque:**

```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

# Distroless: sem shell, sem package manager, sem utils desnecessárias
FROM gcr.io/distroless/nodejs20-debian12 AS runtime
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
USER nonroot  # nunca root em prod
EXPOSE 3000
CMD ["dist/index.js"]
```

### DAST — Dynamic Application Security Testing

Executa contra a app rodando. Detecta vulnerabilidades que SAST não pega (lógica de negócio, runtime). Roda em staging, não em prod.

```yaml
- name: ZAP API Scan
  uses: zaproxy/action-api-scan@v0.7.0
  with:
    target: 'https://staging.meu-app.com/api/openapi.json'
    format: openapi
```

### Pipeline Completo de Referência

```yaml
# .github/workflows/security.yml
jobs:
  sast:
    steps:
      - uses: returntocorp/semgrep-action@v1
        with:
          config: p/owasp-top-ten p/secrets

  secrets:
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - uses: gitleaks/gitleaks-action@v2

  sca:
    steps:
      - run: npm audit --audit-level=high
      - uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          severity: 'HIGH,CRITICAL'
          exit-code: '1'

  container:
    needs: [sast, secrets, sca]  # só builda se os anteriores passarem
    steps:
      - run: docker build -t app:${{ github.sha }} .
      - uses: aquasecurity/trivy-action@master
        with:
          image-ref: app:${{ github.sha }}
          severity: CRITICAL,HIGH
          exit-code: '1'
      - run: docker push app:${{ github.sha }}
```

### Policy as Code — OPA / Conftest / Kyverno

Codificar políticas de segurança como regras versionadas no repositório, verificadas automaticamente no CI.

```rego
# policy/terraform/deny_public_s3.rego
package terraform.deny_public_s3

deny[msg] {
  resource := input.resource.aws_s3_bucket[name]
  resource.acl == "public-read"
  msg := sprintf("S3 bucket '%s' tem ACL public-read — proibido", [name])
}

deny[msg] {
  resource := input.resource.aws_s3_bucket[name]
  not resource.server_side_encryption_configuration
  msg := sprintf("S3 bucket '%s' sem criptografia — exigido por SOC 2 CC6.1", [name])
}
```

```bash
# Validar plano Terraform
terraform plan -out=plan.tfplan
terraform show -json plan.tfplan > plan.json
conftest test plan.json --policy policy/terraform/
```

**Kyverno** — políticas em YAML no admission webhook do K8s:

```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-non-root
spec:
  validationFailureAction: Enforce
  rules:
    - name: check-non-root
      match:
        any:
        - resources:
            kinds: ["Pod"]
      validate:
        message: "Pod deve rodar como non-root"
        pattern:
          spec:
            securityContext:
              runAsNonRoot: true
```

| Ferramenta | Onde aplica | Sintaxe |
|---|---|---|
| Conftest | CI — pre-deploy | Rego |
| OPA Gatekeeper | Runtime K8s | Rego |
| Kyverno | Runtime K8s | YAML (mais amigável) |
| Checkov | CI — IaC | 1000+ regras prontas |

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| SAST no CI | Detecta bugs antes de prod | Falsos positivos altos sem tuning |
| SCA automático | CVEs conhecidos nunca passam despercebidos | Atualizações frequentes geram ruído |
| Container distroless | Superfície de ataque mínima | Debugging em prod fica difícil (sem shell) |
| Policy as Code | Compliance verificável e versionado | Curva de Rego é íngreme |

## Quando Usar / Quando Evitar

**Comece com 3 ferramentas:** Gitleaks (secrets) + Trivy (CVEs) + Semgrep (SAST). Adicione o restante conforme maturidade.

**Evite over-engineering quando:** pipeline já demora 30+ min — segurança não pode ser o gargalo. Ferramentas com alto ruído de falsos positivos matam a adoção.

## Conceitos Relacionados

[[supply-chain-security]] · [[secret-scanning]] · [[container-hardening]] · [[kubernetes-security]] · [[secure-design-patterns]] · [[threat-modeling]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-01*
