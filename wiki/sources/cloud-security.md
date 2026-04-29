---
type: source
title: "Cloud Security"
aliases: ["cloud security", "aws iam", "scp", "cspm", "workload identity federation", "guardduty", "prowler"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/cloud-security.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [cloud-security, iam, scp, cspm, workload-identity, guardduty, prowler, aws, least-privilege]
skill: tech-mentor-security
status: stable
---

## TL;DR

Cloud Security: IAM com least privilege, Permission Boundaries para delegação segura, SCPs para guardrails em toda a org AWS. CSPM (Prowler, Security Hub) audita misconfigurations continuamente. Workload Identity Federation elimina credenciais estáticas em CI/CD (OIDC token em vez de AWS keys). GuardDuty para detecção de ameaças em runtime.

## Key Claims

**Claim:** Workload Identity Federation elimina AWS access keys em CI/CD — OIDC token temporário por execução.
**Evidence:** GitHub Actions com OIDC: workflow recebe token temporário, assume role AWS via `sts:AssumeRoleWithWebIdentity`. Zero secrets estáticos no repositório. Token expira com o job. Impossível vazar credencial de longa duração. Mesmo padrão para GCP, Azure.
**Confidence:** alta

**Claim:** CSPM automatizado (Prowler + Security Hub) pega 80% dos problemas comuns sem esforço manual.
**Evidence:** Prowler: auditoria open source contra CIS AWS Foundations, NIST, PCI. Detecta: S3 públicos, SGs com 0.0.0.0/0, MFA desabilitado, CloudTrail inativo, RDS snapshots públicas. Security Hub agrega findings de GuardDuty, Inspector, Macie, IAM Analyzer em painel único.
**Confidence:** alta

**Claim:** Permission Boundaries em IAM permitem delegar criação de roles sem escalar privilégios.
**Evidence:** Sem boundary: se uma role tem `iam:CreateRole`, pode criar role com AdministratorAccess. Com Permission Boundary: `iam:CreateRole` só pode criar roles cujas policies cabem dentro do boundary definido. Times de produto criam suas próprias roles sem precisar de intervenção do time de segurança.
**Confidence:** alta

**Claim:** SCPs são o último guardrail — bloqueiam até o root da conta membro da AWS Organization.
**Evidence:** SCP `DenyLeaveOrganization` aplicado na OU: nenhuma conta membro consegue sair da organização, mesmo com acesso root. SCP `DenyRegionOutsideEU`: impossível criar recursos fora da Europa. SCPs não concedem permissões — apenas restringem o máximo que uma IAM policy pode fazer.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/cloud-security]]
- [[concepts/iam]]
- [[concepts/least-privilege]]
- [[concepts/workload-identity]]
- [[concepts/cspm]]
- [[entities/prowler]]
- [[entities/guardduty]]
- [[entities/aws]]

## Open Questions

- CSPM em multi-cloud (AWS + GCP) — como unificar findings de segurança em um único painel?
- IAM Access Analyzer: como integrar em PRs para detectar policy changes inseguras antes do merge?
