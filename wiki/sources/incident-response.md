---
type: source
title: "Incident Response"
aliases: ["incident response", "ir", "runbook", "postmortem", "forensics", "siem", "soar", "nist 800-61"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/incident-response.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [incident-response, runbook, postmortem, forensics, siem, soar, nist-800-61, containment]
skill: tech-mentor-security
status: stable
---

## TL;DR

Incident Response (NIST SP 800-61): 4 fases — Preparação, Detecção & Análise, Contenção/Erradicação/Recuperação, Lições Aprendidas. Preparação: playbooks por tipo de incidente prontos ANTES do incidente. SIEM para correlação de eventos, SOAR para automação de resposta. Post-mortem blameless: foco em sistemas, não em pessoas. Notificação de breach: 72h para autoridade (GDPR/LGPD).

## Key Claims

**Claim:** Preparação antes do incidente determina o tempo de resposta — playbook não existe é playbook inútil.
**Evidence:** Incidente sem playbook: equipe discute quem notificar, como isolar, como preservar evidências — enquanto o atacante continua ativo. Com playbook: papéis definidos, escalation path documentado, ferramentas com acesso testado, canais de comunicação backup. Tempo médio de contenção cai de horas para minutos.
**Confidence:** alta

**Claim:** Post-mortem blameless é o único formato que produz aprendizado real — foco em sistemas, não em pessoas.
**Evidence:** Post-mortem com culpa: engenheiros omitem erros para não serem responsabilizados. Cultura de medo impede análise honesta. Blameless: "o sistema permitiu que X acontecesse" — investigação de causa-raiz sistêmica, não individual. Template: timeline, contributing factors, action items com owner e deadline. Sem conclusão "foi erro humano" sem ação sistêmica.
**Confidence:** alta

**Claim:** SOAR automatiza resposta repetível — bloquear IP, isolar pod, revogar credencial em segundos sem intervenção humana.
**Evidence:** SOAR (Security Orchestration, Automation and Response): playbook automatizado disparado por SIEM alert. Exemplo: alerta "login de IP de país de alto risco" → SOAR bloqueia IP no WAF, envia MFA challenge, cria ticket no Jira, notifica no Slack — tudo em < 30s. Human review para decisões complexas; automação para resposta inicial.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/incident-response]]
- [[concepts/runbook]]
- [[concepts/postmortem]]
- [[concepts/forensics]]
- [[concepts/siem]]
- [[concepts/soar]]
- [[concepts/containment]]

## Open Questions

- Forensics digital em containers efêmeros — como preservar evidências quando o pod já foi destruído?
- SOAR em times sem SOC dedicado — como implementar automação básica de IR sem expertise de segurança?
