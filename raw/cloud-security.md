---
date: 2026-04-01
tags: [tech-mentor, security, cloud, aws, iam, cspm, scp, oidc-federation, guardduty]
skill: tech-mentor-security/references/cloud_sec
level: intermediário
---

# Cloud Security

## Contexto

A maior fonte de incidentes em cloud não é exploração de zero-days — é **misconfiguration**. S3 bucket público, Security Group com `0.0.0.0/0`, CloudTrail desabilitado, IAM com `*` em resource. O modelo de responsabilidade compartilhada da AWS faz você responsável por tudo acima do hypervisor.

## Como Funciona

### Effective Permissions na AWS

A permissão efetiva é a interseção de três camadas:

```
Permissão efetiva = Identity Policy ∩ Permission Boundary ∩ SCP
```

## Código de Referência

### Permission Boundary — Delegação Segura

Teto de permissões de uma role. Mesmo que a policy permita mais, o boundary limita. Caso de uso: permitir que devs criem roles sem que possam escalar privilégios.

```json
// Boundary: dev pode criar roles, mas limitadas a S3 + DynamoDB
{
  "Effect": "Allow",
  "Action": ["s3:GetObject", "s3:PutObject", "dynamodb:*"],
  "Resource": "arn:aws:*:*:123456789:*"
}
// Policy da role criada: s3:* → efetivo é só GetObject + PutObject (∩ boundary)
```

### SCP — Service Control Policies

Controle no nível da organização — nenhuma conta filha escapa:

```json
// SCP na OU de produção — ninguém desabilita auditoria
{
  "Effect": "Deny",
  "Action": [
    "cloudtrail:DeleteTrail",
    "cloudtrail:StopLogging",
    "guardduty:DeleteDetector",
    "config:DeleteConfigRule"
  ],
  "Resource": "*"
}

// Bloquear todas as regiões exceto as autorizadas
{
  "Effect": "Deny",
  "Action": "*",
  "Resource": "*",
  "Condition": {
    "StringNotEquals": {
      "aws:RequestedRegion": ["us-east-1", "sa-east-1"]
    }
  }
}
```

### Workload Identity Federation — CI/CD sem credenciais estáticas

GitHub Actions não precisa de `AWS_SECRET_ACCESS_KEY` — troca OIDC token por credenciais temporárias:

```yaml
# GitHub Actions com OIDC Federation — zero secrets
jobs:
  deploy:
    permissions:
      id-token: write  # permite obter OIDC token do GitHub
    steps:
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789:role/GitHubActionsRole
          aws-region: us-east-1
```

**Trust policy da role:**
```json
{
  "Principal": { "Federated": "arn:aws:iam::123456789:oidc-provider/token.actions.githubusercontent.com" },
  "Action": "sts:AssumeRoleWithWebIdentity",
  "Condition": {
    "StringEquals": {
      "token.actions.githubusercontent.com:sub": "repo:myorg/myrepo:ref:refs/heads/main"
    }
  }
}
```

**Como funciona:**
1. GitHub emite JWT assinado com claims (`repo`, `ref`, `job_workflow_ref`)
2. AWS STS valida o JWT contra o OIDC provider
3. AWS verifica a trust policy da role
4. STS emite credenciais temporárias (15min–1h)

### CSPM — Cloud Security Posture Management

Auditoria contínua de misconfigurations. Pega 80% dos problemas comuns sem esforço.

```bash
# Prowler — auditoria open source da AWS
prowler aws --output-formats json html
prowler aws --compliance cis_aws_2.0

# Checks mais comuns que falham:
# - S3 buckets públicos
# - Security Groups com 0.0.0.0/0 na porta 22/3389
# - MFA não habilitado para root
# - CloudTrail desabilitado
# - RDS snapshots públicas
# - IAM policies com wildcard
```

**AWS Security Hub** — agrega findings de GuardDuty, Inspector, Config, IAM Analyzer, Macie:
```
Habilitar padrões:
  - AWS Foundational Security Best Practices
  - CIS AWS Foundations Benchmark

Integração automática:
  Finding crítico → EventBridge → Lambda → Slack/PagerDuty
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| SCPs | Guardrails que nenhuma conta escapa | Exige AWS Organizations |
| Permission Boundaries | Delegação segura de criação de roles | Raciocinar sobre permissão efetiva é complexo |
| OIDC Federation | Zero credenciais estáticas no CI | Configuração inicial mais complexa |
| CSPM | Visibilidade contínua de misconfigurations | Ruído de findings sem triagem adequada |

## Regras Práticas de IAM

```
✅ Nunca use * em Resource para dados — especifique ARNs
✅ Prefira roles temporárias (STS) a IAM users com chaves de longa duração
✅ Revise permissões mensalmente com AWS IAM Access Analyzer
✅ MFA obrigatório para root e usuários com permissões elevadas
✅ CloudTrail habilitado em todas as regiões, logs imutáveis (S3 Object Lock)
```

## Conceitos Relacionados

[[zero-trust]] · [[secrets-management]] · [[kubernetes-security]] · [[container-hardening]] · [[devsecops-pipeline]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-01*
