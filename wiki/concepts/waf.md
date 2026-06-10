---
type: concept
title: "WAF (Web Application Firewall)"
aliases: ["waf", "web application firewall", "firewall de aplicação"]
date_created: 2026-06-05
date_updated: 2026-06-05
source_count: 1
tags: [waf, ddos, owasp, borda, attack-surface, cloud-security, aws-waf, cloudflare]
skill: tech-mentor-security
status: stable
---

# WAF (Web Application Firewall)

Filtro de borda que inspeciona e bloqueia tráfego HTTP malicioso antes de chegar na aplicação. Opera em nível de rede/protocolo — não conhece identidade do usuário nem regras de negócio.

## O que um WAF faz

- Bloqueia ataques conhecidos do OWASP Top 10 (SQLi, XSS, SSRF, etc.)
- Filtra tráfego malicioso por padrão de payload
- Previne DDoS volumétrico
- Protege contra bots e credential stuffing em nível de rede

## Diferença vs. Gatekeeper

| | WAF | [[concepts/gatekeeper-pattern]] |
|---|---|---|
| Nível de operação | Rede / HTTP | Aplicação |
| Conhece o usuário? | Não | Sim |
| Conhece serviços internos? | Não | Sim |
| Aplica autorização? | Não | Sim |
| Bloqueia ataques HTTP? | Sim | Depende da impl. |

O WAF complementa o Gatekeeper mas não o substitui. São camadas independentes de [[concepts/defense-in-depth]].

## Provedores Comuns

- **AWS WAF** — integra com CloudFront, ALB, API Gateway
- **Azure Web Application Firewall** — integra com Application Gateway e Front Door
- **Cloudflare WAF** — borda distribuída globalmente

## Key Sources

- [[sources/padroes-arquiteturais-seguranca-gatekeeper-valet-key-token-relay]]
- [[sources/cinco-praticas-seguranca-pragmatic-programmer]] — WAF como complemento ao SAST: SAST age no dev, WAF age em produção
