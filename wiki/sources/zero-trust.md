---
type: source
title: "Zero Trust"
aliases: ["zero trust", "never trust always verify", "ztna", "spiffe spire", "conditional access"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/zero-trust.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [zero-trust, ztna, spiffe, spire, mtls, cloudflare-access, tailscale, conditional-access, microsegmentacao, identity-first]
skill: tech-mentor-security
status: stable
---

## TL;DR

Zero Trust: "nunca confie, sempre verifique" — nenhum acesso é implicitamente confiável só por estar na rede interna. 7 pilares CISA: Identity, Device, Network, Workload, Data, Automation, Visibility. Acesso condicional: decisão por cada request baseada em identidade + postura do dispositivo + contexto. mTLS com SPIFFE/SPIRE para service-to-service.

## Key Claims

**Claim:** VPN tradicional cria uma zona de confiança plana — comprometer um endpoint = acesso à rede inteira.
**Evidence:** VPN: "dentro da VPN = confiável". Zero Trust: cada acesso verifica identidade + postura do dispositivo + contexto do request. Um notebook comprometido dentro da VPN não obtém acesso implícito a todos os recursos.
**Confidence:** alta

**Claim:** Cloudflare Access + Tailscale são as implementações mais práticas de Zero Trust para acesso humano.
**Evidence:** Cloudflare Access: usuário → IdP (Google/Okta) → policy engine → app interna. Zero exposição de portas na internet. Tailscale: mesh VPN com ACLs granulares, engenheiros acessam infra via identidade, não IP.
**Confidence:** alta

**Claim:** SPIFFE/SPIRE + mTLS é o padrão para autenticação service-to-service em Zero Trust.
**Evidence:** SPIFFE (Secure Production Identity Framework for Everyone) define SVID (identidade para workloads). SPIRE emite SVIDs como certificados X.509 de curta duração. mTLS: ambos os lados autenticam via certificado — IP não é suficiente. Istio implementa isso automaticamente.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/zero-trust]]
- [[concepts/conditional-access]]
- [[concepts/spiffe-spire]]
- [[concepts/ztna]]
- [[concepts/mtls]]
- [[entities/cloudflare]]
- [[entities/tailscale]]

## Open Questions

- Zero Trust para workloads serverless (Lambda) — SPIFFE não funciona sem processo persistente. Qual a alternativa?
- Modelo de maturidade CISA ZTM: como priorizar em qual pilar investir primeiro?
