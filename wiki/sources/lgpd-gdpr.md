---
type: source
title: "LGPD / GDPR — Compliance Técnico"
aliases: ["lgpd", "gdpr", "data subject rights", "right to erasure", "data mapping", "breach notification", "lawful basis"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/lgpd-gdpr.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [lgpd, gdpr, data-subject-rights, right-to-erasure, data-mapping, breach-notification, lawful-basis, anpd]
skill: tech-mentor-security
status: stable
---

## TL;DR

LGPD (Brasil) e GDPR (Europa): mesmo framework de princípios. 6 bases legais principais (consentimento, contrato, legítimo interesse, etc). Direitos dos titulares: acesso, retificação, portabilidade, exclusão. Breach notification: 72h para ANPD/DPA nacional. Data Mapping: documentar para cada dado — base legal, finalidade, prazo de retenção. DPO/Encarregado obrigatório em casos específicos.

## Key Claims

**Claim:** Data Mapping é o primeiro passo obrigatório — sem saber onde estão os dados, não é possível cumprir LGPD/GDPR.
**Evidence:** Titular solicita portabilidade dos seus dados → sem data mapping, engenheiro percorre 5 bancos, 3 data warehouses, 2 sistemas legados manualmente. Com data mapping: tabela documentando cada tipo de dado, onde está armazenado, base legal, finalidade, TTL. Resposta em horas, não semanas.
**Confidence:** alta

**Claim:** Consentimento não é a única base legal — e frequentemente não é a mais adequada.
**Evidence:** 10 bases legais na LGPD, 6 no GDPR. Para contrato (checkout, cadastro): base "execução de contrato" — sem necessidade de consentimento separado. Para analytics: "legítimo interesse" pode bastar se proporcional. Basear tudo em consentimento cria obrigação de reter prova de consentimento e gerenciar retirada — desnecessário para dados de contrato.
**Confidence:** alta

**Claim:** Notificação de breach tem prazo de 72h para autoridade — implementar alertas automáticos de detecção é obrigatório.
**Evidence:** GDPR Art. 33: 72h para notificar DPA. LGPD Art. 48: "prazo razoável" — ANPD pratica 72h. Sem sistema de detecção, a empresa descobre a breach semanas depois. Obrigação começa no momento do CONHECIMENTO do breach, não da ocorrência. Implementar: alertas de volume anômalo de exports, acesso a dados sensíveis fora do padrão.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/lgpd]]
- [[concepts/gdpr]]
- [[concepts/data-mapping]]
- [[concepts/lawful-basis]]
- [[concepts/right-to-erasure]]
- [[concepts/breach-notification]]
- [[concepts/dpo]]
- [[entities/anpd]]
- [[sources/compliance]]

## Open Questions

- LGPD vs GDPR em empresa com usuários nos dois países — qual framework é mais restritivo e deve prevalecer?
- Right to erasure com backup tapes físicos — como lidar com dados em backup offline que não podem ser deletados seletivamente?
