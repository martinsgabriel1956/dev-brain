---
type: source
title: "Policy as Code"
aliases: ["policy as code", "opa", "open policy agent", "rego", "kyverno", "conftest", "opa gatekeeper"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/policy-as-code.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [policy-as-code, opa, rego, kyverno, conftest, opa-gatekeeper, admission-control, compliance-automation]
skill: tech-mentor-infra
status: stable
---

## TL;DR

Policy as Code: policies de segurança e compliance como código versionado e testável. OPA: engine de avaliação com Rego (DSL). Kyverno: K8s-native, policies em YAML sem Rego. OPA Gatekeeper: OPA como K8s admission webhook. Conftest: valida Terraform/YAML/JSON em CI. Use case principal: impedir deploy de configuração insegura antes de chegar em produção.

## Key Claims

**Claim:** Policy as Code transforma compliance em automação — não é checklist manual, é pipeline que falha.
**Evidence:** Checklist manual: "verificar se todos os pods têm readOnlyRootFilesystem" antes de cada deploy. Esquece em 30% dos PRs. Policy as Code: Kyverno ClusterPolicy rejeita Pods sem `readOnlyRootFilesystem: true` na admission. 100% de cobertura, zero overhead manual. Evidência para auditores: logs do admission controller.
**Confidence:** alta

**Claim:** Kyverno é mais acessível que OPA Gatekeeper para times sem expertise em Rego.
**Evidence:** OPA Gatekeeper: policy em Rego (DSL funcional com curva de aprendizado alta). Kyverno: policy em YAML com `spec.rules.validate/mutate/generate`. Time sem background de PL funcional produz Kyverno policies em horas, Rego em dias. OPA Gatekeeper vence para policies complexas com lógica avançada que Kyverno YAML não expressa.
**Confidence:** alta

**Claim:** Conftest valida Terraform plans antes de `apply` — detecta infraestrutura insegura antes de criar.
**Evidence:** `terraform plan -out=plan.tfplan && terraform show -json plan.tfplan > plan.json && conftest test plan.json --policy policies/`. Rego policy: `deny["Security Group abre porta 22 para 0.0.0.0/0"]` se recurso AWS SG tem `from_port=22` e `cidr=0.0.0.0/0`. Falha o pipeline antes de criar infra.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/policy-as-code]]
- [[entities/opa]]
- [[concepts/rego]]
- [[entities/kyverno]]
- [[entities/conftest]]
- [[entities/opa-gatekeeper]]
- [[concepts/admission-control]]

## Open Questions

- OPA como authorization service para aplicações (não só K8s) — overhead de latência de chamada externa por request?
- Styra DAS vs auto-hosted OPA para gestão de policies em múltiplos clusters — quando o overhead operacional vale?
