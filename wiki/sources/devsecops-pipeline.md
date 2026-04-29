---
type: source
title: "DevSecOps Pipeline"
aliases: ["devsecops", "sast", "dast", "sca", "supply chain security", "policy as code", "security pipeline"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/devsecops-pipeline.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [devsecops, sast, dast, sca, container-scanning, policy-as-code, opa, conftest, kyverno, ci-cd-security]
skill: tech-mentor-security
status: stable
---

## TL;DR

DevSecOps integra segurança no pipeline CI/CD em 4 gates: SAST (análise estática — Semgrep), SCA (dependências vulneráveis — npm audit, Snyk), Container Scanning (Trivy), DAST (dinâmico em staging — OWASP ZAP). Policy as Code (OPA/Conftest/Kyverno) valida IaC e K8s manifests antes de aplicar. Security gates em PR, não só em produção.

## Key Claims

**Claim:** SAST com Semgrep detecta padrões inseguros no código sem executar — integra em PR como qualquer linter.
**Evidence:** Semgrep: regex-based rules sobre AST. Regras OWASP Top 10 pré-configuradas. Detecta: SQL injection por concatenação, eval() com input de usuário, hardcoded secrets, SSRF patterns. Falsos positivos ajustáveis via `.semgrepignore`. Roda em < 30s para codebase médio. Falha o PR se severity >= ERROR.
**Confidence:** alta

**Claim:** SCA é o gate mais impactante em custo/benefício — detecta CVEs em dependências sem esforço.
**Evidence:** 60-80% dos ataques exploram vulnerabilidades conhecidas em dependências (Log4Shell, event-stream). `npm audit --audit-level=high` em CI: sem custo adicional, detecta CVEs com CVSS >= 7. Snyk adiciona fix automático via PR. Dependabot monitora continuamente. ROI imediato.
**Confidence:** alta

**Claim:** Policy as Code com OPA/Conftest valida Terraform e K8s manifests antes de aplicar — shift-left de compliance.
**Evidence:** Conftest: `conftest test terraform-plan.json --policy security.rego`. Rego policy: "deny se Security Group tem porta 22 aberta para 0.0.0.0/0". Kyverno: policy K8s nativa que bloqueia Pods sem `readOnlyRootFilesystem`. Falha o pipeline antes de criar infra insegura — mais barato que remediar em produção.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/devsecops]]
- [[concepts/sast]]
- [[concepts/dast]]
- [[concepts/sca]]
- [[concepts/policy-as-code]]
- [[entities/semgrep]]
- [[entities/trivy]]
- [[entities/opa]]
- [[entities/kyverno]]

## Open Questions

- DAST em pipelines com autenticação complexa (OAuth2 flows) — como configurar ZAP para testar endpoints autenticados?
- Como priorizar SAST findings sem afogar o time com falsos positivos?
