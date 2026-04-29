---
type: source
title: "Data Privacy — LGPD/GDPR"
aliases: ["data privacy", "lgpd", "gdpr", "right to erasure", "pseudonimização", "privacy by design", "pii"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/data-privacy.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [data-privacy, lgpd, gdpr, pii, right-to-erasure, pseudonymization, privacy-by-design, crypto-shredding]
skill: tech-mentor-security
status: stable
---

## TL;DR

LGPD (Brasil) e GDPR (Europa): mesmos princípios — base legal, minimização, finalidade, direito ao esquecimento. Right to Erasure: dados devem ser deletados em 30 dias (GDPR) / razoável (LGPD). Crypto-shredding: deleta a chave de criptografia, dados existentes tornam-se ilegíveis. PII nunca em logs. Pseudonimização ≠ Anonimização (pseudonimizado é reversível). Privacy by Design: TTL definido na criação do campo.

## Key Claims

**Claim:** Crypto-shredding é a forma mais eficiente de "esquecer" dados em sistemas distribuídos — deleta a chave, não os dados.
**Evidence:** Right to erasure em sistema com backups: deletar do banco não remove dos backups. Crypto-shredding: cada usuário tem uma DEK (Data Encryption Key) única. Dados armazenados criptografados com a DEK. Para "esquecer": deleta apenas a DEK do KMS. Todos os dados criptografados do usuário tornam-se ilegíveis permanentemente, incluindo backups.
**Confidence:** alta

**Claim:** PII nunca pode aparecer em logs — vazamento de log = notificação de breach.
**Evidence:** Stack trace com `email: "user@example.com"` no log → CloudWatch → Datadog → potencialmente indexado. Sanitização obrigatória antes de logar: remover CPF, email, telefone, endereço, dados de saúde. Técnicas: masking (`u***@***.com`), substituição por ID. Detecção automática de PII em CI com ferramentas como Nightfall ou AWS Macie.
**Confidence:** alta

**Claim:** Pseudonimização ≠ Anonimização — dado pseudonimizado ainda é dado pessoal sob LGPD/GDPR.
**Evidence:** Pseudonimização: substituir nome por UUID gerado deterministicamente. Mantém relação user_id → dados reais em tabela separada. É dado pessoal porque pode ser reidentificado com a tabela de mapeamento. Anonimização real: irreversível por qualquer meio razoável. K-anonymity ou differential privacy. GDPR/LGPD não se aplicam a dados verdadeiramente anônimos.
**Confidence:** alta

**Claim:** Privacy by Design requer TTL definido para cada tipo de dado no momento da criação do campo.
**Evidence:** "Vamos definir retenção depois" = nunca define. Checklist: ao criar qualquer coluna com PII, responder: qual base legal? qual finalidade? qual prazo de retenção? Script de data retention automática (`DELETE WHERE created_at < NOW() - INTERVAL '2 years'`) executado como cron job documentado.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/lgpd]]
- [[concepts/gdpr]]
- [[concepts/pii]]
- [[concepts/right-to-erasure]]
- [[concepts/crypto-shredding]]
- [[concepts/pseudonymization]]
- [[concepts/privacy-by-design]]

## Open Questions

- Right to erasure em sistemas de event sourcing — como apagar eventos históricos sem quebrar o log imutável?
- LGPD e analytics com heatmaps (Hotjar) — como obter consentimento granular sem degradar UX?
