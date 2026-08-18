---
type: concept
title: "AWS IAM"
aliases: ["IAM", "Identity and Access Management", "AWS Identity"]
date_created: 2026-05-06
date_updated: 2026-08-17
source_count: 2
tags: ["aws", "iam", "segurança", "identidade", "permissões", "autorizacao"]
skill: tech-mentor-infra
status: draft
---

# AWS IAM

Serviço da AWS para gerenciar **identidades** (quem pode acessar) e **permissões** (o que pode fazer). Gratuito, global e obrigatório em qualquer conta AWS.

## Conceitos Centrais

| Conceito | Descrição |
|---|---|
| Root Account | Conta criada automaticamente ao abrir conta AWS. Acesso irrestrito — usar só para tarefas de setup inicial. |
| User | Identidade individual dentro da organização. Pode ter credenciais de console (senha) e/ou programáticas (access key). |
| Group | Coleção de usuários. **Não aceita grupos aninhados.** Facilita gestão coletiva de permissões. |
| Policy | Objeto JSON que define permissões. Pode ser anexada a grupos, usuários ou roles. |
| Role | Identidade temporária assumida por serviços AWS, usuários de outras contas ou workloads automatizados. |

## Hierarquia de Identidades

```
Conta AWS
└── Grupos (contêm apenas usuários)
    └── Usuários
Usuários podem pertencer a múltiplos grupos.
Usuários sem grupo são válidos, mas não recomendados.
```

## Políticas (Policies)

Policies são JSONs com estrutura `Effect / Action / Resource`:

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["s3:GetObject"],
    "Resource": "arn:aws:s3:::meu-bucket/*"
  }]
}
```

Tipos principais:
- **AWS Managed** — criadas e mantidas pela AWS
- **Customer Managed** — criadas pelo cliente, reutilizáveis
- **Inline** — embutidas diretamente em um usuário/grupo/role

## Princípio do Menor Privilégio

Ver [[principio-menor-privilegio]]. Prática mandatória na AWS: conceder apenas as permissões estritamente necessárias para a tarefa.

## Least Privilege — Exemplo Prático de Escopo Mínimo

Ilustração concreta do princípio: se uma instância só precisa ler de um bucket S3 específico, a role dela deve conter exatamente `s3:GetObject` nesse bucket — nada mais amplo. Se a instância for comprometida, o dano do atacante fica limitado a essa única permissão. Reforça que IAM é o primeiro serviço a configurar, antes de qualquer rede ([[wiki/concepts/vpc]]) ou computação ([[wiki/concepts/ec2]]). Ver [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]].

## Key Sources

- [[wiki/sources/iam-introduction-users-groups-policies]]
- [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]] — reforço de least privilege com exemplo de escopo mínimo (S3 read-only) e recomendação de MFA + não usar conta root no dia a dia
