---
type: concept
title: "Data Residency"
aliases: ["residência de dados", "data sovereignty", "soberania de dados"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 1
tags: [data-residency, compliance, lgpd, gdpr, multi-region, architecture]
skill: tech-mentor-security
status: stub
---

## Definição

Restrição legal ou regulatória que determina em qual país ou região geográfica os dados devem ser armazenados e processados. Dado do Brasil, sob LGPD, pode não sair do território nacional dependendo da base legal e do tipo de dado.

## Impacto em Arquitetura

Quando data residency é um requisito, ele força mudanças estruturais:
- Topologia multi-region com replicação controlada (sem cross-region sync automático)
- Roteamento por tenant para garantir que dados de usuários BR fiquem em regiões BR
- Backups e logs também precisam respeitar a restrição — não basta proteger o banco principal

## Relação com Multi-Tenancy

Em SaaS multi-tenant, data residency por cliente exige separação de storage (DB-per-tenant ou schema-per-tenant com regiões distintas). Shared schema com todos os dados no mesmo cluster viola data residency para tenants de regiões específicas.

## Key Sources

- [[sources/compliance]] — data residency como um dos 3 cenários onde compliance muda arquitetura

## Conceitos Relacionados

[[concepts/compliance]] · [[concepts/multi-tenancy]] · [[concepts/db-sharding]]
