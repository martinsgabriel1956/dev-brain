---
type: concept
title: "Gatekeeper Pattern"
aliases: ["gatekeeper", "ponto único de entrada", "single entry point"]
date_created: 2026-06-05
date_updated: 2026-07-23
source_count: 2
tags: [gatekeeper, api-gateway, bff, attack-surface, arquitetura-seguranca, defense-in-depth]
skill: tech-mentor-security
status: stable
---

# Gatekeeper Pattern

Padrão arquitetural de segurança que define um único ponto obrigatório por onde todo tráfego externo deve passar. Serviços internos ficam completamente inacessíveis do exterior — só o Gatekeeper é exposto.

## Responsabilidades do Gatekeeper

- Autenticação e autorização de borda
- Rate limiting
- Registro de logs e auditoria
- Bloqueio de tráfego suspeito
- Roteamento para serviços internos

## Ganho Arquitetural

Com o Gatekeeper, serviços internos recebem chamadas já filtradas e não precisam reimplementar segurança de borda. Isso:
- Reduz [[concepts/attack-surface]] (menos pontos de entrada)
- Centraliza responsabilidade de segurança
- Diminui inconsistência — sem risco de um serviço esquecer de validar o token

## Relação com WAF

Um [[concepts/waf]] complementa mas não substitui o Gatekeeper. O WAF opera em nível de rede (bloqueia ataques HTTP conhecidos), mas não conhece identidade do usuário nem regras de negócio. O Gatekeeper opera em nível de aplicação.

## Implementações Comuns

- **API Gateway** (AWS API Gateway, Kong, Nginx) — roteamento + auth + rate limit. Ver [[wiki/concepts/api-gateway]] para a formalização arquitetural completa (roteamento, mapeamento de payload, edge functions, single point of failure).
- **BFF (Backend for Frontend)** — Gatekeeper especializado por tipo de cliente (web, mobile, parceiro). Ver [[wiki/concepts/bff-pattern]].
- **Ingress Controller** (Kubernetes) — Gatekeeper de borda no cluster

## Anti-patterns

- Serviços internos com porta diretamente exposta na internet
- Múltiplos pontos de entrada independentes para diferentes partes do sistema
- Gatekeeper que só redireciona sem aplicar segurança ("pass-through" puro)

## Key Sources

- [[sources/padroes-arquiteturais-seguranca-gatekeeper-valet-key-token-relay]]
- [[wiki/sources/api-gateway-padrao-essencial-arquiteturas-distribuidas]]
