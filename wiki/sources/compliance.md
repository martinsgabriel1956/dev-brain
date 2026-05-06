---
type: source
title: "Compliance — Fundamentos para Engenheiros"
aliases: ["compliance", "lgpd", "gdpr", "pci-dss", "soc2", "hipaa", "iso27001", "audit log", "data residency", "dsar"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_file: /home/nemomartins/Documentos/new/dev-study/raw/compliance.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-05-05
source_count: 0
tags: [compliance, lgpd, gdpr, pci-dss, soc2, hipaa, iso-27001, audit-log, data-residency, dsar, security]
skill: tech-mentor-security
status: stable
---

## TL;DR

Compliance é a prova documentada de que você seguiu as regras. É diferente de segurança (estado real do sistema). Você pode ser compliant e inseguro, ou seguro e não-compliant. Do ponto de vista de engenharia, compliance vira problema de arquitetura quando exige: data residency (muda topologia multi-region), audit log em toda operação sensível (muda schema e fluxo de escrita), e DSAR (exige mapear onde cada dado do usuário vive em todos os sistemas).

## Key Claims

**Claim:** Compliance é diferente de segurança — são relacionados mas distintos.
**Evidence:** Segurança = estado real do sistema (quão difícil é comprometer). Compliance = prova documentada de que as regras foram seguidas. É possível ser compliant e inseguro (checklist sem substância). É possível ser seguro e não-compliant (sem documentação). O objetivo é os dois simultaneamente.
**Confidence:** alta

**Claim:** Compliance vira problema de engenharia real em três cenários específicos.
**Evidence:** (1) Data residency: dado do BR não pode sair do BR → muda arquitetura multi-region. (2) Audit log: toda operação sensível deve ser logada → muda schema de DB e fluxo de escrita. (3) DSAR (Data Subject Access Request): direito de acesso/deleção → você precisa mapear onde cada dado do usuário vive (DB, Redis, S3, backups).
**Confidence:** alta

**Claim:** Frameworks de compliance mais relevantes mapeiam para domínios específicos.
**Evidence:** LGPD/GDPR → dados pessoais de usuários (lei brasileira/europeia). PCI-DSS → dados de cartão de crédito (exigido pelas bandeiras). SOC 2 → segurança/disponibilidade/confidencialidade (clientes enterprise B2B). ISO 27001 → gestão de segurança da informação (mercado global). HIPAA → dados de saúde (regulação americana).
**Confidence:** alta

**Claim:** Audit log estruturado é evidência reutilizável para múltiplos frameworks.
**Evidence:** INSERT INTO audit_log com user_id, action, resource, timestamp é exigido por LGPD/SOC 2 (CC7.2), PCI-DSS (Req 10) e ISO 27001 (A.12.4). Invista uma vez, satisfaz múltiplos auditores.
**Confidence:** alta

**Claim:** DSAR (Art. 18 LGPD) exige deleção em cascata em múltiplos sistemas.
**Evidence:** Uma chamada deleteUserData não basta — o dado do usuário vive em: DB relacional, Redis, S3, backups. Cada sistema precisa de processo separado de deleção. A transação no DB é só o começo.
**Confidence:** alta

## Raw Quotes

> "Você pode ser compliant e inseguro (checklist sem substância). Pode ser seguro e não-compliant (sem documentação). O objetivo é os dois."

> "Evitar a armadilha de: tratar compliance como checklist burocrático sem substância técnica — isso cria falsa sensação de segurança."

## Entities & Concepts Touched

- [[concepts/compliance]]
- [[concepts/audit-log]]
- [[concepts/data-residency]]
- [[concepts/dsar]]
- [[sources/compliance-soc2-pci]]
- [[sources/lgpd-gdpr]]
- [[sources/hipaa-sox]]

## Open Questions

- Como implementar data residency em multi-tenant SaaS sem multiplicar custo de infra?
- Qual a estratégia de backup que satisfaz LGPD sem impossibilitar restore?
