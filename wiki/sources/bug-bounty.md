---
type: source
title: "Bug Bounty"
aliases: ["bug bounty", "vdp", "responsible disclosure", "hackerone", "bugcrowd", "cvss", "security report"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/bug-bounty.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [bug-bounty, vdp, responsible-disclosure, cvss, hackerone, bugcrowd, pentest, appsec]
skill: tech-mentor-security
status: stable
---

## TL;DR

Bug Bounty: programa de recompensa por vulnerabilidades reportadas responsavelmente. VDP (Vulnerability Disclosure Program): sem pagamento, só reconhecimento. Plataformas: HackerOne, Bugcrowd, Intigriti. CVSS calcula severidade (0-10). Report de qualidade: título claro, steps to reproduce, impacto, PoC, sugestão de fix. Perspectiva empresa: definir escopo, triage SLAs, comunicação rápida.

## Key Claims

**Claim:** Report de qualidade acelera triage e pagamento — título, passos reproduzíveis e PoC são obrigatórios.
**Evidence:** Reports vagos ("encontrei um bug no login") ficam semanas em triage. Report completo: título descritivo ("IDOR em /api/users/:id permite acessar dados de qualquer usuário"), ambiente, passos numerados, resposta esperada vs observada, impacto de negócio, PoC funcional. Triage imediata, resolução mais rápida.
**Confidence:** alta

**Claim:** CVSS v3.1 é o padrão para calcular severidade — Attack Vector, Complexity, Privileges, User Interaction, Scope, Impact.
**Evidence:** CVSS Base Score: AV (Network/Adjacent/Local/Physical), AC (Low/High), PR (None/Low/High), UI (None/Required), S (Unchanged/Changed), C/I/A (None/Low/High). Score 9.0-10.0 = Critical. Score < 4.0 = Low. Empresas usam CVSS para priorizar patch. Pesquisadores usam para estimar bounty.
**Confidence:** alta

**Claim:** Escopo bem definido no programa reduz ruído e atrai pesquisadores de qualidade.
**Evidence:** Escopo vago ("nosso produto") → reports de infra de terceiros, spam de scanners automáticos, duplicatas. Escopo específico: domínios incluídos, domínios excluídos, vulnerabilidades out-of-scope (DoS, rate limiting, spam). Programa com bom escopo e SLA de resposta < 5 dias atrai pesquisadores sérios.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/bug-bounty]]
- [[concepts/responsible-disclosure]]
- [[concepts/cvss]]
- [[entities/hackerone]]
- [[entities/bugcrowd]]
- [[concepts/vdp]]
- [[concepts/pentest]]

## Open Questions

- Bug bounty privado vs público — como decidir quando um programa está maduro o suficiente para ser público?
- Como lidar com pesquisadores que extrapolam o escopo mas encontram vulnerabilidades críticas?
