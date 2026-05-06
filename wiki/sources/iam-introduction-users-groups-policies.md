---
type: source
title: "IAM Introduction — Users, Groups, Policies"
aliases: ["Aula 01 IAM", "IAM Introdução"]
date_created: 2026-05-06
date_updated: 2026-05-06
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/Aula 01 - IAM Introduction - Users, Groups, Policies.md"
source_url: ""
author: ""
date_published: 2026
date_ingested: 2026-05-06
source_count: 0
tags: ["aws", "iam", "segurança", "identidade", "permissões", "cloud"]
skill: tech-mentor-infra
status: stable
---

# IAM Introduction — Users, Groups, Policies

## TL;DR

IAM (Identity and Access Management) é o serviço AWS para gerenciar identidades e permissões. Ao criar uma conta AWS, a conta raiz é gerada automaticamente. A partir dela, cria-se usuários organizacionais, agrupáveis em grupos. Permissões são concedidas via _policies_ — objetos JSON que definem o que cada identidade pode fazer. A prática recomendada é o princípio do menor privilégio.

---

## Principais Afirmações

| Claim | Evidência | Confiança |
|---|---|---|
| Um grupo só pode conter usuários, não outros grupos | Documentação do curso | Alta |
| Um usuário pode não pertencer a nenhum grupo | Documentação do curso | Alta |
| Um usuário pode pertencer a múltiplos grupos simultaneamente | Documentação do curso | Alta |
| Policies são objetos JSON de permissionamento | Documentação do curso | Alta |
| Princípio do menor privilégio é a prática recomendada na AWS | Documentação do curso | Alta |

---

## Conceitos Introduzidos ou Aprofundados

- [[aws-iam]] — serviço de identidade e controle de acesso da AWS
- [[principio-menor-privilegio]] — conceder apenas o mínimo de permissões necessárias
- [[amazon-web-services]] — plataforma que hospeda o IAM

---

## Estrutura do IAM

```
Conta AWS
└── Root Account (criada automaticamente)
    ├── Grupos
    │   ├── Usuário A
    │   └── Usuário B (pode estar em múltiplos grupos)
    └── Usuário C (sem grupo — não recomendado)

Policies (JSON) → atribuídas a grupos e/ou usuários individuais
```

**Regra crítica:** grupos contêm apenas usuários — não é possível aninhar grupos.

---

## Questões em Aberto

- Como o IAM se integra com AWS Organizations para múltiplas contas?
- Qual é a diferença entre IAM Policies e Service Control Policies (SCPs)?
- Como funcionam as IAM Roles vs. IAM Users para workloads automatizados?
