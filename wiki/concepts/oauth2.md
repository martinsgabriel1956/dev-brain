---
type: concept
title: "OAuth 2.0"
aliases: ["OAuth", "OAuth 2.0", "delegação de acesso", "authorization code flow"]
date_created: 2026-07-27
date_updated: 2026-08-03
source_count: 4
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

**PKCE** (Proof Key for Code Exchange): obrigatório para SPAs e apps mobile, previne interceptação do `authorization_code`. **Implicit Flow** está deprecated — expunha tokens diretamente na URL. Ver [[wiki/concepts/pkce]] para o mecanismo completo (`code_verifier`/`code_challenge`) e por que o Implicit Flow foi abandonado.

## Open Redirect: Validar a `redirect_uri` Caractere por Caractere

Se o Authorization Server não valida a `redirect_uri` de forma exata — aceitando wildcard ou comparação parcial —, um atacante consegue trocar o domínio de retorno e receber o `authorization_code` no próprio servidor. Ver [[wiki/concepts/open-redirect]] para o mecanismo completo do ataque e a mitigação.

## O Parâmetro `state` Contra CSRF

Sem um `state` aleatório vinculado à sessão do usuário e verificado no retorno, o fluxo OAuth fica vulnerável a CSRF: o atacante inicia um login com a própria conta e induz a vítima a completar o callback — se a vítima não perceber, a conta do atacante fica vinculada ao perfil dela. `state` é o que garante que o callback recebido corresponde a um fluxo que o próprio usuário iniciou.

## Device Flow

Variante para dispositivos sem browser (CLIs, Smart TVs): o dispositivo mostra um código curto, o usuário abre o browser em outro aparelho para autorizar, e o dispositivo faz polling até receber o token.

## O limite do OAuth

OAuth responde "o que este app pode fazer" (autorização), mas não foi desenhado para responder "quem é este usuário" (autenticação) de forma padronizada — essa lacuna é o motivo de existir o [[wiki/concepts/openid-connect]], construído como uma camada de identidade em cima do OAuth.

## Relação com outros conceitos

- [[wiki/concepts/openid-connect]] — camada de autenticação construída sobre o OAuth 2.0
- [[wiki/concepts/jwt]] — formato comum do access token emitido no fluxo OAuth
- [[wiki/concepts/sso-single-sign-on]] — OAuth/OIDC é a base técnica do SSO moderno via login social
- [[wiki/concepts/token-relay-pattern]] — propagação do access token por serviços internos após obtido via OAuth
- [[wiki/concepts/open-redirect]] — ataque específico contra validação frouxa da redirect_uri

## Key Sources

- [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]]
- [[wiki/sources/pkce-proof-key-code-exchange-spa-mobile]] — detalha por que o Implicit Flow falhou e como o PKCE resolve, com foco em SPA/mobile
- [[wiki/sources/rfc-7636-pkce-oauth-public-clients]] — texto normativo do RFC que estende o Authorization Code Grant do OAuth 2.0 com PKCE
- [[wiki/sources/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys]] — open redirect por validação frouxa de redirect_uri; state contra CSRF no fluxo de login social
