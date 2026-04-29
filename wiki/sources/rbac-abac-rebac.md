---
type: source
title: "RBAC, ABAC e ReBAC — Modelos de Autorização"
aliases: ["rbac", "abac", "rebac", "openfga", "opa", "zanzibar", "authorization models"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/rbac-abac-rebac.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [rbac, abac, rebac, opa, openfga, zanzibar, authorization, access-control, relationship-based, attribute-based]
skill: tech-mentor-security
status: stable
---

## TL;DR

3 modelos de autorização: RBAC (roles simples, escalona mal), ABAC (atributos contextuais, flexível, complexo), ReBAC (baseado em relacionamentos — Google Zanzibar). OPA é ABAC em produção. OpenFGA é ReBAC open source. Escolha pelo caso: RBAC para admin/user simples; ABAC para policies contextuais; ReBAC para "quem pode ver o documento X".

## Key Claims

**Claim:** RBAC não escala para autorização granular — role explosion quando regras são por recurso.
**Evidence:** Sistema simples: admin/user. Sistema real: `order:read`, `order:write`, `order:cancel`, `payment:refund`... 50 roles distintas. Manter matriz de permissões vira overhead. ReBAC ou ABAC resolvem de forma mais sustentável.
**Confidence:** alta

**Claim:** ABAC com OPA separa policy de código — policies como código versionado.
**Evidence:** OPA: policy em Rego (DSL declarativa). Decisão de autorização é uma query ao OPA. Policy muda sem redeploy da aplicação. Auditável: log de cada decisão. Trade-off: Rego tem curva de aprendizado alta.
**Confidence:** alta

**Claim:** ReBAC (Google Zanzibar) é o melhor modelo para permissões baseadas em relacionamentos — "Alice pode ler o doc porque é membro do time que tem acesso à pasta".
**Evidence:** Zanzibar armazena tuples (`user:alice`, `member`, `org:company`). Check de permissão resolve a cadeia de relacionamentos. OpenFGA (open source, Okta) implementa Zanzibar. Casos: Google Drive, GitHub, Dropbox.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/rbac]]
- [[concepts/abac]]
- [[concepts/rebac]]
- [[concepts/zanzibar]]
- [[entities/openfga]]
- [[entities/opa]]

## Open Questions

- OPA vs CASL (Node.js) — quando o overhead de um servidor OPA separado vale vs biblioteca local?
- ReBAC com OpenFGA em produção — qual a latência de check de permissão para grafos de relacionamento grandes (100M+ tuples)?
