---
type: source
title: "Secure Design Patterns"
aliases: ["secure design patterns", "defense in depth", "least privilege", "fail secure", "attack surface minimization", "assume breach"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/secure-design-patterns.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [secure-design, defense-in-depth, least-privilege, fail-secure, attack-surface, assume-breach, secure-defaults, separation-of-duties]
skill: tech-mentor-security
status: stable
---

## TL;DR

7 padrões de design seguro: Defense in Depth (múltiplas camadas independentes), Least Privilege (permissão mínima necessária), Secure Defaults (configuração padrão é segura), Fail Secure/Closed (falha fecha o acesso), Minimização de Superfície de Ataque (menos código = menos bugs), Separação de Responsabilidades (uma função = um propósito), Assume Breach (se comprometido, o dano é limitado).

## Key Claims

**Claim:** Defense in Depth requer camadas independentes — duplicar o mesmo controle não é defense in depth.
**Evidence:** Dois firewalls do mesmo vendor com mesma configuração: vulnerabilidade no vendor compromete ambos simultaneamente. WAF + validação de input no código + parameterized queries: camadas independentes, cada uma com superfície de ataque diferente. Falha no WAF não elimina proteção no código. Independência é o requisito central.
**Confidence:** alta

**Claim:** Fail Secure significa que a falha fecha o acesso — não "falha e deixa passar".
**Evidence:** Autenticação com timeout de 5s: se o serviço de identidade não responder, o que fazer? Fail Open: deixa o usuário entrar — falha expõe o sistema. Fail Secure: retorna 503 ou 401 — falha bloqueia o acesso. Para sistemas de segurança (acesso físico, pagamentos): sempre Fail Secure. Para UX (read-only features): pode-se considerar Fail Open com degradação controlada.
**Confidence:** alta

**Claim:** Assume Breach é o mindset correto para design — "quando comprometido" não "se comprometido".
**Evidence:** Design sem Assume Breach: toda proteção na borda, base de dados sem criptografia ("o banco está na rede interna, está protegido"). Assume Breach: mesmo que atacante passe pela rede, encontra criptografia at-rest, isolamento por serviço, audit logs, zero standing privilege. Breach contida, não catastrófica.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/defense-in-depth]]
- [[concepts/least-privilege]]
- [[concepts/fail-secure]]
- [[concepts/secure-defaults]]
- [[concepts/attack-surface-minimization]]
- [[concepts/assume-breach]]
- [[concepts/separation-of-duties]]

## Open Questions

- Assume Breach em startups sem budget para segmentação de rede — quais controles têm melhor custo/benefício?
- Secure Defaults em frameworks Node.js — quais são os padrões inseguros mais comuns que frameworks populares habilitam por default?
