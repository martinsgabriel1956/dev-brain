---
date: 2026-04-01
tags: [tech-mentor, security, supply-chain, sbom, sigstore, cosign, slsa, trivy, sca]
skill: tech-mentor-security/references/supply-chain-security
level: intermediário
---

# Supply Chain Security

## Contexto

Você pode ter código interno perfeito e ser comprometido via:
- Uma dependência npm com malware
- Uma imagem base Docker backdoored
- Um pipeline de CI/CD comprometido
- Typosquatting de um pacote popular (`lodahs` em vez de `lodash`)

O ataque mais famoso: **SolarWinds** — o build pipeline foi comprometido, malware injetado nos artefatos assinados e distribuídos para clientes.

## Como Funciona

Supply chain security protege três vetores:

```
1. Dependências        → SCA + SBOM + pinning por hash
2. Artefatos de build  → Assinatura com Sigstore + provenance SLSA
3. Runtime             → Admission controller verifica assinaturas
```

## Código de Referência

### SBOM — Software Bill of Materials

Inventário machine-readable de todos os componentes: dependências, versões, licenças, hashes. Pense como "lista de ingredientes" do produto.

**Formatos:**
- **CycloneDX** (OWASP) — mais rico, recomendado para segurança
- **SPDX** (Linux Foundation) — padrão ISO, focado em licenças

```bash
# Gerar SBOM de imagem Docker
syft meu-app:latest -o cyclonedx-json > sbom.json

# Escanear o SBOM por CVEs
grype sbom:./sbom.json --fail-on high

# Trivy — all-in-one
trivy image --format cyclonedx --output sbom.json meu-app:latest
```

```yaml
# GitHub Actions: gerar e escanear SBOM no CI
- name: Generate SBOM
  uses: anchore/sbom-action@v0
  with:
    image: meu-app:${{ github.sha }}
    format: cyclonedx-json
    output-file: sbom.cyclonedx.json

- name: Scan SBOM for vulnerabilities
  uses: anchore/scan-action@v3
  with:
    sbom: sbom.cyclonedx.json
    fail-build: true
    severity-cutoff: high
```

SBOM é requisito em contratos enterprise e na regulação americana (Executive Order 14028).

### Sigstore — Assinatura sem Gerenciar Chaves

**Problema clássico:** assinar artefatos exige gerenciar chaves privadas de longa duração. Se a chave vazar, todos os artefatos assinados por ela são comprometidos.

**Sigstore resolve com keyless signing:**

```
1. CI autentica no Fulcio via OIDC (token do GitHub Actions)
2. Fulcio emite certificado efêmero de 10 minutos vinculado à identidade OIDC
3. Cosign assina a imagem com esse certificado
4. Assinatura + certificado são publicados no Rekor (transparency log imutável)
5. Certificado expira — não há chave para roubar
6. Verificador consulta o Rekor para confirmar autenticidade
```

```bash
# Assinar imagem no CI (keyless)
cosign sign \
  --certificate-identity-regexp="https://github.com/empresa/projeto" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com" \
  ghcr.io/empresa/projeto:${GITHUB_SHA}

# Verificar — vai ao Rekor, sem precisar de chave pública
cosign verify \
  --certificate-identity-regexp="https://github.com/empresa/projeto/.github/workflows/release.yml" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com" \
  ghcr.io/empresa/projeto:v1.2.3
```

```yaml
# GitHub Actions: assinar imagem automaticamente
- name: Install Cosign
  uses: sigstore/cosign-installer@v3

- name: Sign image
  env:
    COSIGN_EXPERIMENTAL: "true"
  run: |
    cosign sign \
      ghcr.io/${{ github.repository }}:${{ github.sha }}
```

**Kyverno rejeita pods com imagens não assinadas:**

```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-signed-images
spec:
  validationFailureAction: Enforce
  rules:
    - name: check-image-signature
      match:
        any:
        - resources:
            kinds: ["Pod"]
      verifyImages:
        - imageReferences:
            - "ghcr.io/empresa/*"
          attestors:
            - count: 1
              entries:
                - keyless:
                    subject: "https://github.com/empresa/*/.github/workflows/*.yml@refs/heads/main"
                    issuer: "https://token.actions.githubusercontent.com"
```

### SLSA Framework

Define 4 níveis de maturidade em supply chain security.

| Nível | Requisito | O que previne |
|---|---|---|
| SLSA 1 | Build documentado, provenance gerada | Erros não intencionais |
| SLSA 2 | Build service gerenciado (GitHub Actions), provenance assinada | Build comprometido |
| SLSA 3 | Build em ambiente hardened, não influenciável pelo dev | Insider threats |
| SLSA 4 | Two-party review, hermetic builds | Ataques sofisticados |

**Provenance** = metadados assinados sobre como o artefato foi construído: qual commit, qual workflow, quando, por quem.

```yaml
# Gerar provenance SLSA 3 automaticamente no GitHub Actions
- uses: slsa-framework/slsa-github-generator/.github/workflows/builder_go_slsa3.yml@v1
  with:
    go-version: "1.21"
```

## Checklist Mínimo

```
CI/CD Pipeline:
  ✅ Dependências pinadas com hash (não só versão semântica)
  ✅ SCA automático a cada PR (Trivy/Snyk)
  ✅ Secrets scanning (Gitleaks, TruffleHog)
  ✅ SBOM gerado em cada release

Artefatos:
  ✅ Imagens assinadas com Cosign
  ✅ Provenance SLSA gerada
  ✅ Imagem base mínima (distroless ou alpine)

Runtime:
  ✅ Admission controller verifica assinaturas (Kyverno/OPA)
  ✅ Alertas de novas CVEs em imagens em produção
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| SBOM | Visibilidade total de dependências | Gera volume que precisa de gestão |
| Sigstore keyless | Sem gestão de chaves privadas | Depende de serviços externos (Fulcio, Rekor) |
| SLSA 3+ | Previne insider threats | Complexidade de infra de build significativa |
| Admission controller | Enforcement em runtime | Pode bloquear deploys legítimos sem tuning |

## Quando Usar / Quando Evitar

**Use quando:**
- Produto distribui software para clientes externos (binários, imagens, pacotes)
- Requisitos de compliance enterprise (SOC 2, NIST SSDF)
- Ambiente com múltiplos times contribuindo — risk surface cresce com o tamanho

**Comece simples:** pinning de dependências por hash + Trivy no CI são 80% do valor com 20% do esforço.

## Conceitos Relacionados

[[devsecops-pipeline]] · [[secret-scanning]] · [[container-hardening]] · [[kubernetes-security]] · [[secrets-management]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-01*
