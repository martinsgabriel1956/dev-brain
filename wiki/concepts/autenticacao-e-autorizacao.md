---
type: concept
title: "Autenticação e Autorização"
aliases: ["authn authz", "authentication vs authorization", "quem é você vs o que você pode fazer"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [autenticacao, autorizacao, seguranca, backend, jwt, sessao, rbac]
skill: tech-mentor-backend
status: stub
---

# Autenticação e Autorização

Duas perguntas diferentes que todo backend precisa responder antes de executar qualquer regra:

| | Pergunta | Exemplo de falha |
|---|---|---|
| **Autenticação** | Quem é você? | Token inválido/expirado não é rejeitado |
| **Autorização** | O que você pode fazer? | Usuário autenticado aprova o próprio pagamento |

Estar logado (autenticado) não implica ter permissão (autorizado) para uma ação específica — por exemplo, aprovar um pagamento. Tratar as duas coisas como sinônimos é uma fonte comum de falha de segurança.

## Na prática

O backend recebe uma credencial — cookie de sessão, JWT, token de API — que serve para duas coisas:

1. Confirmar que a requisição veio de alguém conhecido (autenticação)
2. Confirmar que essa pessoa tem permissão para o recurso pedido (autorização)

## Relação com outros conceitos

- [[wiki/concepts/requisicao-resposta]] — a credencial normalmente viaja num header da requisição
- [[wiki/concepts/validacao-de-entrada]] — autorização é um caso específico de validação, aplicado à identidade do requisitante
- Ver detalhamento de OAuth2/OIDC/JWT/RBAC/ABAC em `references/auth-authz.md` (tech-mentor-backend)

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-backend]]
