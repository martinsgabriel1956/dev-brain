---
type: concept
title: "OpenID Connect (OIDC)"
aliases: ["OIDC", "OpenID Connect", "ID Token", "Entrar com Google", "login social"]
date_created: 2026-07-27
date_updated: 2026-08-13
source_count: 3
tags: [oidc, openid-connect, autenticacao, identidade-federada, jwt, seguranca]
skill: tech-mentor-security
status: draft
---

# OpenID Connect (OIDC)

Camada de **autenticação** construída em 2014 em cima do [[wiki/concepts/oauth2|OAuth 2.0]] — o protocolo real por trás dos botões "Entrar com Google/Facebook/GitHub". É a base técnica da identidade federada moderna: a identidade do usuário existe em um domínio (ex.: Google), e outros domínios confiam nela sem verificar por conta própria.

## Por que existe

OAuth 2.0 foi desenhado para autorização (o que um app pode fazer), não para autenticação (quem é o usuário). OIDC fecha essa lacuna acrescentando, ao fluxo de OAuth, um **ID Token** — um [[wiki/concepts/jwt|JWT]] assinado com claims padronizadas:

- `issuer` (`iss`) — quem emitiu o token
- `subject` (`sub`) — identificador único do usuário naquele provedor
- `audience` (`aud`) — para qual aplicação o token foi emitido

## Verificação sem confiança cega

O site que recebe o ID Token não precisa confiar na palavra de ninguém: busca a chave pública do emissor em um endpoint padronizado, o **JWKS** (JSON Web Key Set), e verifica a assinatura criptograficamente. Em milissegundos, sabe quem é o usuário — sem chamada adicional de rede além de buscar as chaves públicas (que podem ficar em cache).

## `nonce`: Proteção Contra Replay

O ID Token inclui opcionalmente um campo `nonce` — um valor único gerado pelo servidor a cada tentativa de login. Sem ele, um atacante que intercepta o tráfego de rede e copia o ID Token pode reenviá-lo depois e ser autenticado como a vítima. Com `nonce`, o servidor rejeita qualquer token cujo valor já tenha sido consumido antes, fechando essa janela de replay.

## Escopos e Princípio do Menor Privilégio

Cada escopo concedido define exatamente o que o app pode acessar (ex.: ler e-mail mas não deletar, ver contatos mas não editar). O princípio do menor privilégio determina que o app deve receber apenas o menor conjunto de escopos necessário para funcionar. Os escopos concedidos ficam embutidos no token, e a API checa se o token carrega o escopo exigido antes de responder — sem o escopo certo, a requisição é negada mesmo com um token assinado e válido.

## Não confundir com o OpenID Original

Apesar do nome, o OIDC não é uma evolução direta do protocolo **OpenID original** (2005) — é um protocolo tecnicamente diferente que reaproveitou o nome. O OpenID original usava uma URL como identidade, descoberta dinamicamente via HTML, e foi descontinuado por volta de 2014, mesmo ano em que o OIDC 1.0 foi lançado, construído do zero sobre o [[wiki/concepts/oauth2|OAuth 2]]. Ver [[wiki/concepts/openid-legado]] para o protocolo original e por que ele não vingou (em contraste com o SAML, que resolveu o mesmo problema com premissas de confiança mais formais).

## JSON vs. XML: Por Que o OIDC Suplantou o SAML Fora do Mundo Corporativo

O SAML tradicional (ver [[wiki/concepts/sso-single-sign-on]]) trafega XML pesado tanto no pedido quanto na resposta do Identity Provider, aumentando a complexidade de implementação — especialmente em single page applications e apps mobile. O OIDC trafega apenas JSON, mais leve e mais compatível com o ecossistema atual de APIs e clients modernos.

## Autenticação Sempre via Client/Navegador — Nunca a API Como Proxy

Para efetivamente usar OIDC (e SAML), a autenticação precisa acontecer via client/navegador, diretamente no provedor de identidade — nunca pela própria API atuando como intermediária que recebe login/senha do usuário. É a única forma de garantir que credenciais e MFA não sejam interceptados pela aplicação cliente. É por isso que "Entrar com Google/Facebook/GitHub" sempre abre uma instância do browser com a URL do provedor visível, mesmo em SPA ou app mobile. Uma API que recebe a senha do usuário para repassar ao provedor não está de fato implementando OIDC — está caindo no antipadrão [[wiki/concepts/ropc-resource-owner-password-credentials|ROPC]].

## Interceptação do `code` e PKCE

Se o `authorization_code` gerado pelo provedor de identidade no início do fluxo for interceptado, um atacante pode se passar pelo usuário legítimo junto à aplicação e obter os tokens. Em single page applications não há como embutir um `client_secret` estático com segurança — todo o código do front-end é visível no browser. O [[wiki/concepts/pkce|PKCE]] resolve exatamente esse problema, substituindo o segredo estático por um par `code_verifier`/`code_challenge` descartável a cada tentativa de login.

## Identidade federada

Esse modelo — identidade emitida por um provedor confiável, verificável criptograficamente por qualquer relying party — é o que se chama de **identidade federada**. Difere do [[wiki/concepts/sso-single-sign-on|SSO]] corporativo tradicional (ex.: SAML/Active Directory) por ser aberto a qualquer aplicação na web pública, não só a sistemas internos de uma organização.

## Relação com outros conceitos

- [[wiki/concepts/oauth2]] — protocolo de autorização sobre o qual OIDC é construído
- [[wiki/concepts/jwt]] — formato do ID Token
- [[wiki/concepts/sso-single-sign-on]] — OIDC é o mecanismo técnico moderno de SSO via login social/federado
- [[wiki/concepts/criptografia]] — verificação de assinatura via chave pública é assinatura digital clássica
- [[wiki/concepts/openid-legado]] — protocolo homônimo anterior e tecnicamente não relacionado
- [[wiki/concepts/ropc-resource-owner-password-credentials]] — antipadrão de não usar OIDC corretamente
- [[wiki/concepts/pkce]] — mitigação contra interceptação do `authorization_code` em clients públicos

## Key Sources

- [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]]
- [[wiki/sources/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys]] — nonce contra replay; escopos e princípio do menor privilégio
- [[wiki/sources/openid-connect-oidc-autenticacao-alem-do-oauth]] — contexto histórico do OpenID original vs. OIDC; JSON vs. XML; ROPC; fluxo completo
