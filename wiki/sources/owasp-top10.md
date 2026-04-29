---
type: source
title: "OWASP Top 10 & API Security"
aliases: ["owasp top 10", "broken access control", "injection", "xss", "ssrf", "api security"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/owasp-top10.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [owasp, injection, xss, ssrf, broken-access-control, security-misconfiguration, mass-assignment, rate-limiting, timing-attack, cors]
skill: tech-mentor-security
status: stable
---

## TL;DR

OWASP Top 10 Web: Broken Access Control (#1 mais crítico), Injection (SQL/NoSQL/Command), XSS, SSRF, Cryptographic Failures, Security Misconfiguration, Path Traversal. OWASP API Top 10: BOLA (IDOR), Mass Assignment, Unrestricted Resource Consumption. Rate limiting é defesa de segurança, não só performance.

## Key Claims

**Claim:** SSRF em cloud pode dar acesso total à AWS — o metadata endpoint é o alvo principal.
**Evidence:** POST com URL `http://169.254.169.254/latest/meta-data/iam/security-credentials/ec2-role` retorna credenciais IAM temporárias se o servidor fizer fetch sem validação. IMDSv2 mitiga requerendo token de sessão, mas a defesa principal é validar/blocklist de IPs privados.
**Confidence:** alta

**Claim:** Broken Access Control é o vuln #1 — verificação de autorização ausente em endpoints.
**Evidence:** BOLA (IDOR): `GET /orders/456` sem verificar se o pedido pertence ao usuário autenticado. Solução: `WHERE id = $1 AND user_id = $2` em toda query que acessa recursos por ID.
**Confidence:** alta

**Claim:** Mass Assignment permite que atacante defina campos que não deveria — como `role: "admin"`.
**Evidence:** `Object.assign(user, req.body)` sem whitelist de campos permitidos. Atacante envia `{ "role": "admin", "verified": true }`. Solução: whitelist explícita de campos aceitos por endpoint.
**Confidence:** alta

**Claim:** Timing attacks permitem enumerar usuários válidos — usar `timingSafeEqual` em comparações.
**Evidence:** `if (hash === storedHash)` retorna mais rápido quando os primeiros bytes diferem. Atacante mede o tempo de resposta para descobrir se o usuário existe. `crypto.timingSafeEqual()` garante comparação em tempo constante.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/broken-access-control]]
- [[concepts/injection]]
- [[concepts/xss]]
- [[concepts/ssrf]]
- [[concepts/mass-assignment]]
- [[concepts/owasp]]
- [[concepts/timing-attack]]

## Open Questions

- Como testar BOLA automaticamente em CI sem um scanner de segurança pago?
- CSP (Content Security Policy) — como definir uma policy que não quebre funcionalidades legítimas?
