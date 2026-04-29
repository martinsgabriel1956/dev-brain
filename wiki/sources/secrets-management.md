---
type: source
title: "Secrets Management"
aliases: ["secrets management", "vault hashicorp", "dynamic secrets", "external secrets operator", "secret rotation"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/secrets-management.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [secrets-management, vault, aws-secrets-manager, dynamic-secrets, rotation, external-secrets, workload-identity, irsa, secret-scanning]
skill: tech-mentor-security
status: stable
---

## TL;DR

.env em produção é um anti-pattern — secrets em texto plano, sem auditoria, sem rotação. HashiCorp Vault e AWS Secrets Manager são as soluções padrão. Dynamic Secrets (Vault): credenciais geradas sob demanda com TTL — sem credenciais estáticas. Workload Identity (IRSA/GCP WI): zero static secrets para serviços em cloud. External Secrets Operator para K8s.

## Key Claims

**Claim:** Dynamic Secrets eliminam credenciais estáticas — Vault gera credentials temporárias com TTL.
**Evidence:** Vault PostgreSQL engine: `vault read database/creds/app-role` retorna username/password únicos, válidos por 1h, revogados automaticamente. Se vazar: expiram sem ação manual. Sem dynamic secrets: credencial vazada é válida indefinidamente.
**Confidence:** alta

**Claim:** Workload Identity (IRSA/GCP Workload Identity) elimina AWS_ACCESS_KEY em pods K8s.
**Evidence:** IRSA (IAM Roles for Service Accounts): pod K8s usa ServiceAccount vinculado a IAM Role via OIDC. AWS SDK detecta automaticamente e usa token do pod para assumir o role. Zero credenciais estáticas no pod.
**Confidence:** alta

**Claim:** .env files com secrets em texto plano são o vetor de vazamento mais comum em startups.
**Evidence:** .env commitado por acidente no git = histórico permanente do secret. `git-secrets`, `gitleaks`, `truffleHog` fazem scan do repositório. Pre-commit hooks bloqueiam antes de commitar. Secret scanning no GitHub/GitLab detecta patterns conhecidos.
**Confidence:** alta

**Claim:** External Secrets Operator é o padrão K8s para sincronizar secrets de qualquer provider.
**Evidence:** Um ESO SecretStore aponta para AWS/GCP/Vault. ExternalSecret define qual secret sincronizar e como transformar. O operator cria/atualiza K8s Secrets automaticamente. Rotação: quando o secret muda no provider, o K8s Secret é atualizado.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/dynamic-secrets]]
- [[concepts/workload-identity]]
- [[concepts/irsa]]
- [[concepts/external-secrets-operator]]
- [[concepts/secret-scanning]]
- [[concepts/vault]]
- [[concepts/rotation-secrets]]

## Open Questions

- Dynamic secrets com TTL muito curto (< 5min) — como lidar com conexões de banco que duram mais que o TTL?
- Secret scanning: como reduzir falsos positivos sem criar exceções que mascaram secrets reais?
