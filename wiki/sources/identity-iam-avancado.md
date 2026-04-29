---
type: source
title: "Identity & IAM Avançado"
aliases: ["identity iam avancado", "pam", "privileged access management", "machine identity", "oauth 2.1", "jit access"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/identity-iam-avancado.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [iam, pam, machine-identity, oauth2-1, spiffe, jit-access, least-privilege, workload-identity]
skill: tech-mentor-security
status: stable
---

## TL;DR

Identity & IAM Avançado: PAM (Privileged Access Management) com JIT para zero standing privilege. Machine Identity: certificados X.509 com curto TTL via SPIFFE/SPIRE em vez de API keys. OAuth 2.1 consolida best practices (PKCE obrigatório, refresh token rotation). Least privilege como requisito não-funcional mensurável, não aspiração.

## Key Claims

**Claim:** PAM com JIT é a evolução de least privilege — zero standing privilege como meta operacional.
**Evidence:** Least privilege estático: role com permissões mínimas permanentes. JIT: sem permissões permanentes em sistemas críticos. Acesso concedido on-demand, por tempo limitado, com audit trail completo. HashiCorp Boundary, CyberArk, AWS SSM Session Manager implementam sessões auditadas. Reduz blast radius de compromisso de credencial de "acesso ilimitado" para "acesso nulo após TTL".
**Confidence:** alta

**Claim:** Machine Identity via certificados X.509 de curto TTL é mais seguro que API keys de longa duração.
**Evidence:** API key: se vazada, válida indefinidamente até rotação manual. X.509 com TTL de 24h: chave comprometida expira em horas. SPIFFE/SPIRE rotaciona automaticamente antes do TTL expirar — zero overhead operacional. Para service-to-service authentication em K8s, mTLS com SPIRE é o padrão.
**Confidence:** alta

**Claim:** OAuth 2.1 torna PKCE obrigatório e elimina implicit flow — consolidação de 10 anos de CVEs.
**Evidence:** OAuth 2.0 tinha implicit flow (token no fragment da URL — interceptável) e authorization code sem PKCE (code interception attack). OAuth 2.1: implicit flow removido, PKCE obrigatório para todos os clients, refresh token rotation obrigatória. BCPs (Best Current Practices) viraram padrão.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/pam]]
- [[concepts/jit-access]]
- [[concepts/machine-identity]]
- [[concepts/spiffe]]
- [[concepts/oauth2-1]]
- [[concepts/least-privilege]]
- [[entities/hashicorp-boundary]]

## Open Questions

- PAM em startups pequenas — qual a solução mais leve para JIT sem overhead de CyberArk ou HashiCorp?
- OAuth 2.1 adoption timeline — quando os grandes providers (Google, GitHub) darão suporte completo?
