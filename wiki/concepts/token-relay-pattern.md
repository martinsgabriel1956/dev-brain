---
type: concept
title: "Token Relay Pattern"
aliases: ["token relay", "identity propagation", "propagação de identidade", "user context propagation"]
date_created: 2026-06-05
date_updated: 2026-07-27
source_count: 2
tags: [token-relay, identity, autorizacao, jwt, oauth, microsservicos, arquitetura-seguranca]
skill: tech-mentor-security
status: stable
---

# Token Relay Pattern

Padrão arquitetural que propaga a identidade do usuário original por todos os saltos internos de uma arquitetura distribuída. A identidade viaja junto com a requisição do início ao fim — cada serviço pode aplicar autorização fina baseada em quem é o usuário real.

## Problema que Resolve

Em arquiteturas com API Gateway, BFF e múltiplos microserviços, é comum que serviços internos confiem apenas em quem os chamou (autenticação serviço-a-serviço), sem saber quem é o usuário final. Isso cria uma distinção perigosa:

- **Autenticado** ≠ **Autorizado para aquele recurso específico**

O serviço sabe que veio do API Gateway (confiável), mas não sabe se o usuário tem permissão para aquela operação.

## Como Funciona

```
1. Usuário se autentica → recebe token
2. API Gateway/BFF valida o token na borda
3. Em vez de descartar o token, ele é repassado (relay) para os serviços internos
4. Cada serviço recebe o token do usuário + valida identidade + aplica suas próprias regras de autorização
```

O token pode ser:
- **Repassado diretamente** (JWT — o serviço valida a assinatura localmente)
- **Trocado por token interno** (Token Exchange — RFC 8693 — o serviço obtém um token de escopo menor)

## Diferença vs. Service-to-Service Auth

| Abordagem | O serviço sabe quem chamou? | O serviço sabe quem é o usuário? |
|---|---|---|
| Só service auth (mTLS / API key) | Sim | Não |
| Token Relay | Sim | Sim |

## Ganhos

- **Autorização distribuída:** cada serviço aplica suas regras sem depender cegamente do gateway
- **Rastreabilidade:** logs e audit trails carregam a identidade do usuário real em todos os níveis
- **Defense in depth:** a segurança não fica concentrada apenas na borda

## Relação com Defense in Depth

Token Relay é a implementação de [[concepts/defense-in-depth]] para identidade: a borda autentica, mas a autorização acontece em todos os serviços.

## Cuidados

- Tokens de longa duração repassados aumentam janela de comprometimento — preferir tokens de curta duração + refresh
- Em Token Exchange (RFC 8693), validar que o escopo do token interno é menor ou igual ao do token original
- Serviços internos não devem aceitar tokens de usuário direto da internet — só via gateway confiável

## Relação com JWT e Ciclo de Vida de Tokens

O token repassado costuma ser um [[wiki/concepts/jwt]] — Access Token de curta duração, obtido originalmente via [[wiki/concepts/oauth2]] ou [[wiki/concepts/openid-connect]]. A curta duração limita a janela de comprometimento mesmo quando o token viaja por múltiplos saltos internos; o Refresh Token correspondente nunca deveria ser repassado da mesma forma, já que sua exposição widening derrotaria o controle de revogação centralizado.

## Key Sources

- [[sources/padroes-arquiteturais-seguranca-gatekeeper-valet-key-token-relay]]
- [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]]
