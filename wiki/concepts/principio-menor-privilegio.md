---
type: concept
title: "Princípio do Menor Privilégio"
aliases: ["Least Privilege", "PoLP", "Principle of Least Privilege"]
date_created: 2026-05-06
date_updated: 2026-05-06
source_count: 1
tags: ["segurança", "iam", "aws", "autorização", "zero-trust", "hardening"]
skill: tech-mentor-infra
status: stable
---

# Princípio do Menor Privilégio

Conceder a cada identidade (usuário, serviço, processo) **apenas as permissões estritamente necessárias** para executar sua função — nada mais.

## Por que importa

- Reduz o blast radius de comprometimento de credenciais
- Limita movimento lateral em caso de breach
- Facilita auditoria — permissões excessivas são sinal de risco
- Requisito de compliance (SOC 2, ISO 27001, PCI-DSS, LGPD)

## Na Prática (AWS IAM)

- Iniciar com zero permissões e adicionar conforme necessário
- Evitar políticas `*` (wildcard) em Actions e Resources
- Preferir grupos sobre permissões diretas em usuários
- Usar IAM Roles para workloads automatizados (nunca access keys hardcoded)
- Revisar periodicamente permissões via AWS IAM Access Analyzer

## Conexões

- [[aws-iam]] — contexto principal de aplicação na AWS
- [[zero-trust]] — o menor privilégio é um dos pilares do Zero Trust
- [[rbac-abac-rebac]] — modelos de autorização que implementam o princípio

## Key Sources

- [[wiki/sources/iam-introduction-users-groups-policies]]
