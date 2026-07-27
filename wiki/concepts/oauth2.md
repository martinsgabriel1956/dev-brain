---
type: concept
title: "OAuth 2.0"
aliases: ["OAuth", "OAuth 2.0", "delegação de acesso", "authorization code flow"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_count: 1
tags: [oauth2, autorizacao, autenticacao, seguranca, delegacao-de-acesso]
skill: tech-mentor-security
status: draft
---

# OAuth 2.0

Framework de **autorização** (não autenticação) criado em 2006 por um grupo de empresas da web (incluindo o Twitter) para resolver um problema específico: como deixar um aplicativo acessar dados de outro serviço em nome do usuário, **sem** o usuário compartilhar sua senha com esse aplicativo.

## O problema que resolve

Antes do OAuth, se um app de agendamento quisesse acessar sua Google Agenda, a única forma seria você dar sua senha do Google para o app. Isso é péssimo por dois motivos: o app ganha acesso a tudo (não só à agenda), e você não consegue revogar o acesso sem trocar a senha — o que quebraria o acesso de todos os outros apps que também usam essa senha.

OAuth introduz **delegação de acesso com escopo limitado**: o app recebe um token que só serve para o que foi autorizado, e pode ser revogado independentemente da senha.

## Authorization Code Flow

```
1. App redireciona o usuário para o Authorization Server com:
   client_id, redirect_uri, scope, state (anti-CSRF), code_challenge (PKCE)

2. Usuário autentica no provedor e aprova as permissões (scope)

3. Authorization Server redireciona de volta com um authorization_code

4. App troca o authorization_code por um access_token (+ refresh_token)
   — essa troca acontece server-side, nunca no browser

5. App usa o access_token para acessar o recurso (ex.: a agenda)
```

**PKCE** (Proof Key for Code Exchange): obrigatório para SPAs e apps mobile, previne interceptação do `authorization_code`. **Implicit Flow** está deprecated — expunha tokens diretamente na URL.

## Device Flow

Variante para dispositivos sem browser (CLIs, Smart TVs): o dispositivo mostra um código curto, o usuário abre o browser em outro aparelho para autorizar, e o dispositivo faz polling até receber o token.

## O limite do OAuth

OAuth responde "o que este app pode fazer" (autorização), mas não foi desenhado para responder "quem é este usuário" (autenticação) de forma padronizada — essa lacuna é o motivo de existir o [[wiki/concepts/openid-connect]], construído como uma camada de identidade em cima do OAuth.

## Relação com outros conceitos

- [[wiki/concepts/openid-connect]] — camada de autenticação construída sobre o OAuth 2.0
- [[wiki/concepts/jwt]] — formato comum do access token emitido no fluxo OAuth
- [[wiki/concepts/sso-single-sign-on]] — OAuth/OIDC é a base técnica do SSO moderno via login social
- [[wiki/concepts/token-relay-pattern]] — propagação do access token por serviços internos após obtido via OAuth

## Key Sources

- [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]]
