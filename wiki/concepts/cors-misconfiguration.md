---
type: concept
title: "CORS Mal Configurado"
aliases: ["cors misconfiguration", "cors permissivo demais", "access-control-allow-origin wildcard"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
tags: [cors, seguranca, api-security, csrf]
skill: tech-mentor-security
status: stub
---

# CORS Mal Configurado

CORS (Cross-Origin Resource Sharing) é o mecanismo pelo qual um browser decide se uma página em um domínio pode fazer requisições a uma API em outro domínio. Mal configurado, vira uma falha de segurança em vez de proteção.

## O erro clássico

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
```

Combinar um `Allow-Origin` que aceita **qualquer origem** com `Allow-Credentials: true` (que permite enviar cookies/credenciais na requisição cross-origin) significa que **qualquer site na internet** pode fazer requisições autenticadas contra a API — o navegador da vítima anexa os cookies de sessão automaticamente, e a API responde normalmente.

Na prática, a especificação CORS já proíbe `Allow-Origin: *` junto com `Allow-Credentials: true` na maioria dos browsers modernos — mas configurações que **refletem dinamicamente** a origem da requisição (`Access-Control-Allow-Origin: <origin do request>`) sem checar contra uma allowlist caem na mesma armadilha, já que se comportam como um wildcard efetivo.

## Mitigação

Definir explicitamente uma **allowlist** de origens permitidas, validada no servidor antes de ecoar o header — nunca aceitar a origem da requisição sem checagem, e nunca combinar aceitação irrestrita de origem com credenciais habilitadas.

## Relação com outros conceitos

- [[wiki/concepts/sessoes-http-cookies]] — CORS mal configurado neutraliza parte da proteção que `SameSite` oferece contra requisições cross-origin com credenciais
- [[wiki/concepts/sql-injection]] / [[wiki/concepts/xss]] — mesma família de falha: confiar em input/origem externa sem validação explícita na fronteira do sistema

## Key Sources

- [[wiki/sources/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys]]
