---
type: source
title: "GitOps — ArgoCD e Flux"
aliases: ["gitops", "argocd", "flux", "applicationset", "sync waves"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/gitops-argocd.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [gitops, argocd, flux, applicationset, sync-waves, pull-based-deployment, multi-cluster, pre-sync-hooks]
skill: tech-mentor-infra
status: stable
---

## TL;DR

GitOps é o modelo de deploy onde o Git é a fonte de verdade — o cluster sincroniza automaticamente com o repo (pull-based). ArgoCD: UI rica, ApplicationSet para multi-cluster/multi-env. Flux: mais modular, controller compostos, melhor para GitOps puro sem UI. Sync Waves ordenam recursos (migração antes da app). Pre-Sync Hooks para jobs únicos.

## Key Claims

**Claim:** GitOps pull-based é mais seguro que push-based — o cluster puxa do Git, não recebe push externo.
**Evidence:** Push-based (CI faz kubectl apply): CI tem credenciais de cluster, blast radius enorme se CI for comprometido. Pull-based: ArgoCD/Flux dentro do cluster puxam do Git. Apenas o operator precisa de acesso ao cluster. Auditoria completa no Git history.
**Confidence:** alta

**Claim:** ApplicationSet elimina duplicação de Application yaml para múltiplos ambientes.
**Evidence:** Um ApplicationSet com `List generator` ou `Git generator` cria automaticamente Applications para dev/staging/prod. Mudança no template = atualiza todos os ambientes. Sem copiar/colar yaml por ambiente.
**Confidence:** alta

**Claim:** Sync Waves + Pre-Sync Hooks resolvem dependências de ordem (migração antes da app).
**Evidence:** `argocd.argoproj.io/sync-wave: "1"` para job de migração, `sync-wave: "2"` para o Deployment. Pre-Sync Hook roda antes do sync principal. Hook-delete-policy: deleta o Job após sucesso.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/gitops]]
- [[concepts/argocd]]
- [[concepts/flux]]
- [[concepts/pull-based-deployment]]
- [[concepts/applicationset]]
- [[concepts/sync-waves]]

## Open Questions

- ArgoCD vs Flux para times multi-cloud (AWS + GCP) — qual tem melhor suporte a múltiplos providers?
- Drift detection: ArgoCD detecta drift mas não auto-corrige por padrão — quando habilitar auto-sync é seguro?
