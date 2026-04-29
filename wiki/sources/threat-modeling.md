---
type: source
title: "Threat Modeling"
aliases: ["threat modeling", "stride", "pasta", "dfd", "attack trees", "trust boundaries"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/threat-modeling.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [threat-modeling, stride, pasta, dfd, attack-trees, trust-boundaries, sdlc, risk-register]
skill: tech-mentor-security
status: stable
---

## TL;DR

Threat Modeling identifica ameaças antes de construir. STRIDE (Microsoft): Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege — rápido, 2–4h. PASTA: 7 estágios orientado a risco de negócio — para sistemas críticos. DFD (Data Flow Diagram) é a base para qualquer método. Trust Boundaries são onde o risco concentra.

## Key Claims

**Claim:** Threat Modeling no design custa 10× menos do que corrigir vulnerabilidades em produção.
**Evidence:** Vulnerabilidade de design (ex: "não planejamos autenticação entre serviços internos") identificada em sessão de TM: 2h de discussão + mudança de arquitetura. Mesma vuln em produção: semanas de refactoring + risco de exposição + patches emergenciais.
**Confidence:** alta

**Claim:** STRIDE é o framework mais prático para times de desenvolvimento — 6 categorias cobrindo ~80% das ameaças comuns.
**Evidence:** S(Spoofing) → autenticação. T(Tampering) → integridade. R(Repudiation) → audit log. I(Info Disclosure) → confidencialidade. D(DoS) → disponibilidade. E(Elevation) → autorização. Qualquer dev consegue aplicar em 2–4h com o DFD do sistema.
**Confidence:** alta

**Claim:** Trust Boundaries são onde ameaças concentram — cruzar boundary = verificar identidade e integridade.
**Evidence:** Internet → Load Balancer: validar TLS, rate limit. Load Balancer → App: validar JWT. App → DB: credenciais autenticadas. App → serviço externo: mTLS ou API key. Toda crossing de boundary é um ponto de verificação.
**Confidence:** alta

**Claim:** DFD (Data Flow Diagram) é obrigatório — sem ele, o threat model é especulação.
**Evidence:** DFD mostra: onde dados entram, como fluem, onde são armazenados, quais processos os transformam, quais boundaries cruzam. Sem DFD, a sessão vira brainstorming genérico que não identifica ameaças específicas do sistema real.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/threat-modeling]]
- [[concepts/stride]]
- [[concepts/pasta]]
- [[concepts/dfd]]
- [[concepts/attack-trees]]
- [[concepts/trust-boundaries]]

## Open Questions

- Como fazer threat modeling de features em time que não tem security engineer dedicado?
- Attack Trees em sistemas com 50+ componentes — como manter manejável sem perder cobertura?
