---
type: source
title: "Fraud & Abuse Detection"
aliases: ["fraud detection", "abuse prevention", "device fingerprinting", "velocity checks", "fraud scoring", "account takeover"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/fraud-abuse.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [fraud-detection, abuse-prevention, device-fingerprinting, velocity-checks, fraud-scoring, account-takeover, bot-detection]
skill: tech-mentor-security
status: stable
---

## TL;DR

Fraud & Abuse: múltiplas camadas. Device Fingerprinting (FingerprintJS) identifica dispositivos mesmo sem cookies. Velocity Checks detectam padrões anômalos (N tentativas em X segundos). Fraud Scoring combina sinais para decisão de risco (aprovar/revisar/bloquear). Account Takeover: monitorar login de IP/device novo. Bot Detection: Cloudflare Turnstile/hCaptcha.

## Key Claims

**Claim:** Device Fingerprinting é mais resiliente que cookies para identificar fraude — persiste entre sessões e navegação anônima.
**Evidence:** FingerprintJS: combina User-Agent, timezone, resolução de tela, canvas fingerprint, WebGL, fontes instaladas. Gera visitorId estável. Diferente de cookie: não é apagado pelo usuário, funciona em modo anônimo (parcialmente). Para fraude: mesmo device com múltiplas contas = red flag. Limitação: fingerprint muda com atualizações do browser.
**Confidence:** alta

**Claim:** Velocity Checks em Redis são o gate mais eficiente contra credential stuffing e fraude de pagamento.
**Evidence:** Redis: `INCR login:ip:{ip}` + `EXPIRE 60` = contador por minuto. Threshold: >5 tentativas/min de mesmo IP = bloqueio temporário. Para pagamento: >3 cartões diferentes por usuário em 1 hora = revisar manualmente. Implementação simples, impacto imediato contra ataques automatizados.
**Confidence:** alta

**Claim:** Fraud Scoring permite tratar casos ambíguos com revisão manual — não é apenas bloquear ou aprovar.
**Evidence:** Score 0-100: 0-30 aprovar automaticamente, 31-70 revisão manual (challenge MFA ou human review), 71-100 bloquear. Sinais: email domain novo, IP de proxy/VPN, device não reconhecido, valor acima do padrão histórico, velocidade de typing atípica. Threshold configurável por contexto de risco.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/fraud-detection]]
- [[concepts/device-fingerprinting]]
- [[concepts/velocity-checks]]
- [[concepts/fraud-scoring]]
- [[concepts/account-takeover]]
- [[concepts/bot-detection]]
- [[entities/fingerprintjs]]

## Open Questions

- Fraud scoring com ML vs regras determinísticas — quando o custo de modelo ML justifica sobre regras simples?
- False positives em fraude: como calibrar thresholds para minimizar fricção para usuários legítimos?
