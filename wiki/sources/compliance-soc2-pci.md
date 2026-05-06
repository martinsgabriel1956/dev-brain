---
type: source
title: "Compliance — SOC 2, PCI-DSS, ISO 27001"
aliases: ["soc2", "pci dss", "iso 27001", "compliance", "tokenização", "audit log", "trust service criteria"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/compliance-soc2-pci.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [soc2, pci-dss, iso-27001, compliance, tokenization, audit-log, evidence-collection]
skill: tech-mentor-security
status: stable
---

## TL;DR

SOC 2 Type II: controles operando efetivamente por 6-12 meses (não só existindo). PCI-DSS: nunca armazenar CVV/PAN completo — tokenização via Stripe/Braintree é o caminho correto. ISO 27001: ISMS (Information Security Management System) com Risk Assessment formal. Audit logging estruturado é evidência universal para os três frameworks. Ferramentas de automação (Vanta, Drata) reduzem esforço de coleta de evidências.

## Key Claims

**Claim:** SOC 2 Type II exige que controles operem efetivamente por 6-12 meses — Type I é insuficiente para enterprise.
**Evidence:** Type I: auditoria fotográfica — "em 15/Jan os controles existiam". Type II: auditoria de filme — "de Jan a Dez os controles operaram consistentemente". Enterprise B2B exige Type II. Type I serve como marco intermediário, nunca como entrega final para clientes que processam dados sensíveis.
**Confidence:** alta

**Claim:** PCI-DSS: nunca armazenar CVV, CVV2, PIN — tokenização é o único caminho seguro para dados de cartão.
**Evidence:** PCI proíbe armazenar: CVV2, PIN, dados de trilha magnética. PAN (número do cartão) pode ser armazenado apenas com truncamento + hash ou criptografia forte. Solução: Stripe/Braintree Token que mapeia para o cartão real armazenado pelo processador. Sua aplicação só vê o token — fora do escopo PCI.
**Confidence:** alta

**Claim:** Audit logging estruturado é evidência universal para SOC 2, PCI e ISO 27001 — invista uma vez, use para todos.
**Evidence:** SOC 2 Control CC7.2: log de acesso a dados sensíveis. PCI Req 10: log de acesso a sistema de cartões. ISO 27001 A.12.4: log de eventos de segurança. Estrutura: timestamp ISO8601, user_id, action, resource, ip, result. Imutável (S3 Object Lock ou append-only). Retento mínimo 1 ano.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/soc2]]
- [[concepts/pci-dss]]
- [[concepts/iso-27001]]
- [[concepts/audit-log]]
- [[concepts/tokenization]]
- [[concepts/isms]]
- [[sources/compliance]]

## Open Questions

- Vanta vs Drata para automação de evidências — qual tem melhor cobertura para startups AWS-native?
- ISO 27001 vs SOC 2 para empresa brasileira com clientes europeus — qual certificação priorizar?
