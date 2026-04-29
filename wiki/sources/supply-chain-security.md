---
type: source
title: "Supply Chain Security"
aliases: ["supply chain security", "sbom", "slsa", "sigstore", "cosign", "software bill of materials", "dependency security"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/supply-chain-security.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [supply-chain-security, sbom, slsa, sigstore, cosign, dependency-pinning, sca, provenance]
skill: tech-mentor-security
status: stable
---

## TL;DR

Supply Chain Security protege 3 vetores: dependências (SCA + SBOM + hash pinning), artefatos de build (assinatura com Sigstore/Cosign + SLSA provenance), runtime (admission controller verifica assinaturas). SBOM: inventário de dependências. SLSA: framework de níveis de confiança de build (0-3). Sigstore keyless: assinatura sem gerenciar chaves privadas — OIDC token do CI.

## Key Claims

**Claim:** SBOM (Software Bill of Materials) é o inventário obrigatório para resposta a CVEs — sem ele, "somos afetados pelo Log4Shell?" leva dias.
**Evidence:** Log4Shell (2021): empresa sem SBOM gastou semanas identificando quais sistemas usavam Log4j. Com SBOM (CycloneDX/SPDX): query `sbom.components where name == "log4j"` responde em segundos quais sistemas, versões e artefatos estão afetados. `syft image:app:latest -o syclonedx-json > sbom.json` gera o SBOM automaticamente no CI.
**Confidence:** alta

**Claim:** Sigstore keyless elimina gestão de chaves privadas em assinatura de artefatos — OIDC token do CI autentica.
**Evidence:** Assinatura tradicional: manter chave privada de assinatura, rotacionar, proteger. Sigstore: `cosign sign --identity-token=$CI_TOKEN image:sha256@...`. Sigstore usa o OIDC token (GitHub Actions, Google, etc.) para emitir certificado temporário via Fulcio. Assinatura registrada em Rekor (append-only transparency log). Verificação: `cosign verify --certificate-identity=..`.
**Confidence:** alta

**Claim:** SLSA Level 2 é o baseline prático — provenance de build verificável sem infra complexa.
**Evidence:** SLSA 0: sem garantias. SLSA 1: build scripted, provenance gerado. SLSA 2: build em CI hosted, provenance assinado. SLSA 3: build hermeticamente isolado, sem acesso à internet durante build. Para maioria dos times, SLSA 2 com GitHub Actions + provenance gerado pelo `slsa-framework/slsa-github-generator` é atingível em 1 sprint.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/supply-chain-security]]
- [[concepts/sbom]]
- [[concepts/slsa]]
- [[entities/sigstore]]
- [[entities/cosign]]
- [[concepts/provenance]]
- [[concepts/dependency-pinning]]

## Open Questions

- SLSA Level 3 (hermetic build) em prática — qual stack de CI/CD suporta isso nativamente sem infraestrutura customizada?
- SBOM em sistemas com 500+ dependências transitivas — como priorizar patches sem afogar o time de segurança?
