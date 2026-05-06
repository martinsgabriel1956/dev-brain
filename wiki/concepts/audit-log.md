---
type: concept
title: "Audit Log"
aliases: ["audit logging", "log de auditoria", "audit trail"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 2
tags: [audit-log, compliance, lgpd, soc2, pci-dss, security, logging]
skill: tech-mentor-security
status: stable
---

## Definição

Registro imutável e estruturado de toda operação sensível em um sistema. É a principal forma de evidência em auditorias de compliance (SOC 2, PCI-DSS, ISO 27001, LGPD) e em investigações de incidente.

## Por Que Importa

Um único schema de audit log satisfaz múltiplos frameworks simultaneamente:
- **SOC 2 CC7.2** — log de acesso a dados sensíveis
- **PCI-DSS Req 10** — log de acesso a sistema de cartões
- **ISO 27001 A.12.4** — log de eventos de segurança
- **LGPD Art. 37** — registro de operações de tratamento

## Schema Mínimo

```sql
CREATE TABLE audit_log (
  id          UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id     UUID NOT NULL,
  action      TEXT NOT NULL,          -- 'READ', 'CREATE', 'UPDATE', 'DELETE', 'LOGIN'
  resource    TEXT NOT NULL,          -- 'users.cpf', 'payments.card_number'
  ip_address  INET,
  result      TEXT NOT NULL,          -- 'SUCCESS', 'FAILURE'
  timestamp   TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

Imutável: use S3 Object Lock ou append-only. Retenção mínima: 1 ano (PCI-DSS exige 12 meses online).

## Invariantes

- Nunca edite ou delete registros de audit log
- Logar falhas tanto quanto sucessos (acesso negado é tão relevante quanto acesso concedido)
- Sanitizar dados sensíveis antes de logar (sem CPF, sem PAN, sem senha)

## Key Sources

- [[sources/compliance]] — cenários de engenharia onde audit log é obrigatório
- [[sources/compliance-soc2-pci]] — audit log como evidência universal para SOC 2/PCI/ISO 27001

## Conceitos Relacionados

[[concepts/compliance]] · [[concepts/data-privacy]] · [[concepts/lgpd-gdpr]]
