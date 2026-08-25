---
type: concept
title: "OAuth 2.0"
aliases: ["OAuth", "OAuth 2.0", "delegação de acesso", "authorization code flow"]
date_created: 2026-07-27
date_updated: 2026-08-24
source_count: 10
tags: [oauth2, autorizacao, autenticacao, seguranca, delegacao-de-acesso]
skill: tech-mentor-security
status: draft
---

# OAuth 2.0

Framework de **autorização** (não autenticação) criado em 2006-2007 por um grupo de empresas da web (incluindo o Twitter) para resolver um problema específico: como deixar um aplicativo acessar dados de outro serviço em nome do usuário, **sem** o usuário compartilhar sua senha com esse aplicativo.

## O problema que resolve: o antipadrão da senha

Antes do OAuth, se um app de agendamento quisesse acessar sua Google Agenda, a única forma seria você dar sua senha do Google para o app. Isso é o que hoje se chama [[wiki/concepts/antipadrao-da-senha|antipadrão da senha]], e é péssimo por dois motivos: o app ganha acesso a tudo (não só à agenda), e você não consegue revogar o acesso sem trocar a senha — o que quebraria o acesso de todos os outros apps que também usam essa senha.

OAuth introduz **delegação de acesso com escopo limitado**: o app recebe um token que só serve para o que foi autorizado, e pode ser revogado independentemente da senha.

## Origem: Blaine Cook, Larry Halff e a linha do tempo até a RFC 6749

O grupo de discussão OAuth começou em abril de 2007, do encontro entre [[wiki/entities/blaine-cook]] ([[wiki/entities/twitter|Twitter]], já trabalhando numa implementação do OpenID original) e [[wiki/entities/larry-halff]] (Magnolia, buscando conectar widgets de macOS à API do serviço sem exigir senha) — ambos sentindo, por caminhos diferentes, a falta de um padrão aberto de delegação de acesso. Pouco depois o [[wiki/entities/google]] se junta às discussões. Linha do tempo formal:

- **Julho de 2007** — primeiro rascunho da especificação.
- **Abril de 2010** — [[wiki/entities/ietf|IETF]] publica a **RFC 5849**, o **OAuth 1.0**: exigia assinatura criptográfica em cada requisição e canonicalização de parâmetros, complexo de implementar e manter interoperável entre provedores — por isso pouco usado hoje.
- **2012** — IETF publica a **RFC 6749**, o **OAuth 2.0**: troca a complexidade criptográfica por HTTPS como base de segurança, introduz o token Bearer, e define fluxos muito mais simples de adotar em APIs modernas, SPAs e mobile. É a versão amplamente usada hoje, e a única detalhada neste documento.

Ver [[wiki/sources/historia-oauth2-antipadrao-senha-bernardo-lobato]] para o relato completo.

## Os quatro pilares

- **Resource Owner** — o usuário dono do recurso a ser compartilhado.
- **Client** — a aplicação que quer acessar o recurso em nome do usuário.
- **Authorization Server** — valida a identidade/consentimento e emite os tokens.
- **Resource Server** — a API que guarda o recurso protegido e confia no token emitido.

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

## Grant Types

O **Grant Type** define como a aplicação obtém o token:

- **Authorization Code** — o descrito acima; para login humano via redirecionamento no browser (web, SPA, mobile), com consentimento explícito. Se não há como redirecionar o usuário pelo navegador, este não é o grant type certo. Hoje exige [[wiki/concepts/pkce|PKCE]].
- **Client Credentials** — sem usuário humano: sistema conversando com sistema (integrações back-end, jobs agendados). A aplicação se autentica com seu próprio `client_id`/`client_secret` — como login/senha, mas para aplicações.
- **Refresh Token** — renova um access token expirado/inválido sem exigir novo login. Ver [[wiki/concepts/refresh-token-rotation]].

## Formato do Token: Opaco vs. Autoassinado

O access token OAuth 2 é **opaco para o cliente** por especificação — o padrão não obriga formato, mas na prática muitos provedores usam JWT ([[wiki/concepts/jwt]]). O resource server valida o token de duas formas: **introspecção** (stateful — consulta o Authorization Server a cada requisição) ou **validação local** (o token é autoassinado e carrega a própria verificação embutida, sem round-trip).

## Caso real: escopo aceito sem validação via URL

Em [[wiki/sources/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]], um pentest voluntário no SaaS "Find My SaaS" encontrou um fluxo de login via Google OAuth que aceitava parâmetros extras de escopo/permissão passados pela URL sem validação server-side — permitindo montar um link malicioso que solicitava permissões além do escopo padrão do app (e-mail, nome, foto) e, se aceito pela vítima, expunha o token de autenticação na URL de retorno. O autor original atribuiu o erro a "confiar demais no input do usuário"; tecnicamente é uma falha de validação de parâmetros do Authorization Request no próprio Authorization Server/app — a mesma classe de problema de não tratar `scope`/`redirect_uri` como entrada não confiável, adjacente ao mecanismo descrito em [[wiki/concepts/open-redirect]].

## O limite do OAuth

OAuth responde "o que este app pode fazer" (autorização), mas não foi desenhado para responder "quem é este usuário" (autenticação) de forma padronizada — essa lacuna é o motivo de existir o [[wiki/concepts/openid-connect]], construído como uma camada de identidade em cima do OAuth.

### "Autenticação de Gambiarra" Antes do OIDC Existir

Antes de 2014, com a explosão das APIs e a ascensão do OAuth como padrão de fato, muitas empresas — diante da complexidade do [[wiki/concepts/openid-legado|OpenID original]] — improvisaram autenticação **sobre** o OAuth, com protocolos proprietários e ad-hoc para devolver dados do usuário. Cada grande provedor de identidade tinha sua própria forma de fazer isso, forçando integrações diferentes por provedor — cenário que só foi padronizado quando a OpenID Foundation lançou o [[wiki/concepts/openid-connect|OpenID Connect]] em cima do próprio OAuth 2, reaproveitando o formato JWT já usado pelo OAuth. Ver [[wiki/sources/openid-connect-oidc-autenticacao-alem-do-oauth]].

## Ponte com SAML: Assertion como Credencial

Em ambientes corporativos que já usam [[wiki/concepts/saml|SAML]] para federação, uma assertion SAML pode ser apresentada a um Authorization Server OAuth como credencial: o servidor valida a assinatura XML da assertion e, em troca, emite um access token — potencialmente um JWT leve. Isso permite que APIs REST/microsserviços modernos consumam identidades vindas de diretórios legados (Active Directory via SAML) sem reimplementar SAML do lado da API, unindo a robustez da federação empresarial à agilidade de tokens no ecossistema de microsserviços. Ver [[wiki/sources/autenticacao-federada-sso-saml-bernardo-lobato]].

## Relação com outros conceitos

- [[wiki/concepts/openid-connect]] — camada de autenticação construída sobre o OAuth 2.0
- [[wiki/concepts/saml]] — pode alimentar um fluxo OAuth como credencial (assertion → access token) em pontes entre identidade corporativa legada e APIs modernas
- [[wiki/concepts/jwt]] — formato comum do access token emitido no fluxo OAuth
- [[wiki/concepts/sso-single-sign-on]] — OAuth/OIDC é a base técnica do SSO moderno via login social
- [[wiki/concepts/token-relay-pattern]] — propagação do access token por serviços internos após obtido via OAuth
- [[wiki/concepts/open-redirect]] — ataque específico contra validação frouxa da redirect_uri
- [[wiki/concepts/ropc-resource-owner-password-credentials]] — antipadrão de contornar o fluxo de autorização correto pedindo senha diretamente
- [[wiki/concepts/antipadrao-da-senha]] — o problema original que o OAuth resolve: compartilhar a própria senha com um serviço terceiro

## Key Sources

- [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]]
- [[wiki/sources/pkce-proof-key-code-exchange-spa-mobile]] — detalha por que o Implicit Flow falhou e como o PKCE resolve, com foco em SPA/mobile
- [[wiki/sources/rfc-7636-pkce-oauth-public-clients]] — texto normativo do RFC que estende o Authorization Code Grant do OAuth 2.0 com PKCE
- [[wiki/sources/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys]] — open redirect por validação frouxa de redirect_uri; state contra CSRF no fluxo de login social
- [[wiki/sources/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]] — caso real de escopo/permissão aceito sem validação via URL, achado por pentest voluntário
- [[wiki/sources/openid-connect-oidc-autenticacao-alem-do-oauth]] — "autenticação de gambiarra" improvisada sobre o OAuth antes do OIDC padronizar o formato
- [[wiki/sources/refresh-token-pattern-access-token-de-curta-duracao]] — authorization server como componente que valida/revoga o refresh token no padrão access+refresh token
- [[wiki/sources/historia-e-evolucao-das-apis-bernardo-lobato]] — OAuth situado na linha do tempo geral das APIs: consolidação nos anos 2020 como resposta de governança/segurança à escala de consumo de API alcançada pelas duas ondas de [[wiki/concepts/api-economy]] das décadas anteriores
- [[wiki/sources/autenticacao-federada-sso-saml-bernardo-lobato]] — ponte SAML→OAuth: assertion SAML validada por um Authorization Server em troca de um access token
- [[wiki/sources/historia-oauth2-antipadrao-senha-bernardo-lobato]] — origem histórica exata (Blaine Cook/Twitter, Larry Halff/Magnolia, RFC 5849/6749), antipadrão da senha nomeado, os quatro pilares, grant types (Authorization Code/Client Credentials/Refresh Token) e distinção token opaco (introspecção) vs. autoassinado (validação local)
