---
type: source
title: "HIPAA & SOX"
aliases: ["hipaa", "sox", "phi", "hipaa compliance", "sox compliance", "segregation of duties", "change management sox"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/hipaa-sox.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [hipaa, sox, phi, compliance, audit-trail, segregation-of-duties, change-management, healthcare, financial]
skill: tech-mentor-security
status: stable
---

## TL;DR

HIPAA: protege PHI (Protected Health Information) em sistemas de saúde. BAA (Business Associate Agreement) obrigatório com todos os vendors. Encryption at rest (KMS) e em trânsito. De-identificação Safe Harbor remove 18 identificadores para liberar dados para analytics. SOX: controles de TI para sistemas financeiros. 4 pilares: Change Management auditável, Segregação de Funções, Access Reviews trimestrais, Audit Trail imutável (7 anos, S3 Object Lock COMPLIANCE).

## Key Claims

**Claim:** HIPAA exige BAA com todos os vendors que processam PHI — sem BAA, o vendor não pode ser usado.
**Evidence:** BAA: contrato que responsabiliza o vendor a proteger PHI sob as mesmas obrigações do HIPAA. AWS, Google Cloud, Azure oferecem BAA. Slack standard: sem BAA. Slack Enterprise Grid: com BAA. Usar Slack standard para comunicação com PHI = violação HIPAA. Lista de BAAs necessários: todo serviço que toca dados de pacientes.
**Confidence:** alta

**Claim:** SOX requer audit trail imutável de 7 anos — S3 Object Lock COMPLIANCE é o padrão correto.
**Evidence:** SOX Seção 404: controles internos sobre relatórios financeiros devem ser auditáveis. Audit trail mutável (pode ser deletado por admin) não atende. S3 Object Lock modo COMPLIANCE: nem o root AWS pode deletar antes da retenção expirar. `retention_mode = "COMPLIANCE"` + `years = 7`. CloudTrail com validação de integridade.
**Confidence:** alta

**Claim:** Segregação de Funções (SoD) no SOX impede que o mesmo engenheiro escreva e aprove deploys em produção.
**Evidence:** SoD: quem desenvolve código não deve poder deployar diretamente em produção sem aprovação. GitHub: branch protection com required reviewers. Pipeline: deploy em prod requer aprovação de um segundo engenheiro. Auditoria SOX verifica que não há "single point of trust" no caminho código → produção.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/hipaa]]
- [[concepts/sox]]
- [[concepts/phi]]
- [[concepts/baa]]
- [[concepts/segregation-of-duties]]
- [[concepts/change-management]]
- [[concepts/audit-trail]]
- [[entities/aws]]

## Open Questions

- HIPAA em sistemas de IA/LLM — quando PHI pode ser enviado para modelos de linguagem e com quais salvaguardas?
- SOX em startups pré-IPO — em que momento começar a implementar controles SOX sem paralisar velocidade de desenvolvimento?
