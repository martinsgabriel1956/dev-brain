---
type: concept
title: "Autenticação e Autorização"
aliases: ["authn authz", "authentication vs authorization", "quem é você vs o que você pode fazer"]
date_created: 2026-07-09
date_updated: 2026-07-31
source_count: 3
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

## Teste de Logout como Verificação de Autenticação

[[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]] descreve um teste concreto e frequentemente esquecido: confirmar que, após logout, a sessão antiga de fato deixa de dar acesso a rotas autenticadas — não basta a UI parecer deslogada, o backend precisa invalidar a sessão de verdade. A fonte trata isso como a primeira das perguntas de segurança de um autopentest guiado por IA ("você é quem diz ser?"), anterior ao teste de autorização propriamente dito (a pergunta seguinte: "você pode fazer isso?", tratada em [[wiki/concepts/idor]]).

## Credencial de API Aceita Sem Segundo Fator Como Falha de Autenticação

[[wiki/sources/vibe-coding-env-exposto-idor-account-takeover-rce-loja-ia]] mostra uma variação da falha de autenticação: um endpoint (`POST /api/login`) aceita apenas uma "chave de integração" — sem senha, sem MFA — e devolve um cookie de sessão totalmente válido. Não é implementação incorreta de um mecanismo de autenticação, é um mecanismo de autenticação de fator único e alto risco (posse de uma string) sendo tratado com o mesmo nível de confiança que um login completo. Combinado com o [[wiki/concepts/idor]] que vazava essa chave de outros usuários, o resultado foi [[wiki/concepts/account-takeover]] completo.

## Relação com outros conceitos

- [[wiki/concepts/requisicao-resposta]] — a credencial normalmente viaja num header da requisição
- [[wiki/concepts/validacao-de-entrada]] — autorização é um caso específico de validação, aplicado à identidade do requisitante
- [[wiki/concepts/idor]] — falha clássica de autorização: usuário autenticado agindo sobre recurso de outro usuário
- [[wiki/concepts/account-takeover]] — quando uma falha de autenticação (credencial de fator único aceita sem verificação adicional) se combina com uma falha de autorização (IDOR expondo essa credencial)
- Ver detalhamento de OAuth2/OIDC/JWT/RBAC/ABAC em `references/auth-authz.md` (tech-mentor-backend)

## Key Sources

- [[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]]
- [[wiki/sources/vibe-coding-env-exposto-idor-account-takeover-rce-loja-ia]] — chave de integração de fator único aceita como credencial completa de login

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-backend]]
- [[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]]
