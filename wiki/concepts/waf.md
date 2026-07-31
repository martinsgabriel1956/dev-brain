---
type: concept
title: "WAF (Web Application Firewall)"
aliases: ["waf", "web application firewall", "firewall de aplicação"]
date_created: 2026-06-05
date_updated: 2026-07-31
source_count: 2
tags: [waf, ddos, owasp, borda, attack-surface, cloud-security, aws-waf, cloudflare, under-attack-mode, syn-flood]
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

## Estar na frente não é suficiente — o caso do modo Under Attack

Ter um WAF/CDN configurado na frente do domínio não bloqueia automaticamente um ataque volumétrico: a maioria dos provedores (ex.: Cloudflare) mantém a mitigação agressiva contra DDoS como um modo à parte — o **Under Attack Mode** — que precisa estar ativo (ou configurado para ativação automática). Sem ele, o tráfego malicioso passa pelo WAF/CDN normalmente até a origem, como proxy passivo, sem a camada extra de desafio.

Em [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]], um SaaS recebeu 260 milhões de requests em um único dia via [[wiki/concepts/ddos-syn-flood|SYN flood]] mesmo com Cloudflare na frente do domínio — porque o Under Attack Mode estava desativado. O autor só descobriu isso ao confirmar, no dashboard do próprio Cloudflare, que o tráfego malicioso tinha passado *pelo* WAF, não contornado ele indo direto ao IP de origem.

## Provedores Comuns

- **AWS WAF** — integra com CloudFront, ALB, API Gateway
- **Azure Web Application Firewall** — integra com Application Gateway e Front Door
- **Cloudflare WAF** — borda distribuída globalmente

## Key Sources

- [[sources/padroes-arquiteturais-seguranca-gatekeeper-valet-key-token-relay]]
- [[sources/cinco-praticas-seguranca-pragmatic-programmer]] — WAF como complemento ao SAST: SAST age no dev, WAF age em produção
- [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]] — Under Attack Mode desativado como falha real de configuração, não do produto
