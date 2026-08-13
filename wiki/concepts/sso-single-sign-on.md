---
type: concept
title: "SSO — Single Sign-On"
aliases: ["SSO", "Single Sign-On", "Identity Provider", "IdP"]
date_created: 2026-07-27
date_updated: 2026-08-13
source_count: 2
tags: [sso, identity-provider, autenticacao, identidade-federada, seguranca]
skill: tech-mentor-security
status: draft
---

# SSO — Single Sign-On

Modelo em que o usuário autentica **uma única vez** em uma fonte confiável — o Identity Provider (IdP) — e, a partir daí, todos os sistemas de uma organização confiam nessa autenticação, sem pedir login de novo em cada um.

## O problema que resolve

Com a explosão de serviços na internet, uma única pessoa passa a ter contas em dezenas de sistemas. Sem SSO, um funcionário faria login separadamente em e-mail, CRM, sistema de RH, cada ferramenta interna — gerenciamento inviável em escala e superfície de ataque maior (mais senhas para vazar).

## Como funciona, em essência

```
1. Usuário autentica uma vez no IdP
2. IdP emite uma prova de identidade (assertion SAML ou ID Token OIDC)
3. Cada serviço (Service Provider) valida essa prova e libera acesso
   sem pedir credenciais novamente
```

## Duas gerações de protocolo

- **SAML 2.0** — protocolo XML dominante em SSO corporativo legado (Active Directory, Okta, Workday). Mais verboso, mas ainda é o padrão exigido por muitos sistemas enterprise.
- **[[wiki/concepts/openid-connect]] (OIDC)** — construído sobre [[wiki/concepts/oauth2|OAuth 2.0]], formato JSON/JWT, é a base do login social moderno ("Entrar com Google") e de CIAM (Customer Identity and Access Management).

SSO corporativo (SAML) é historicamente anterior ao OAuth/OIDC — a ideia de "autenticar uma vez, confiar em todo lugar" já existia no mundo enterprise antes de virar identidade federada aberta ao público via login social.

## Por Que o SAML Sobreviveu e o OpenID Original Não

O [[wiki/concepts/openid-legado|OpenID original]] (2005) tentou resolver o mesmo problema de identidade federada que o SAML, mas com uma premissa de confiança oposta: qualquer site aceitando qualquer provedor de identidade, sem governança nem relação de confiança pré-estabelecida. O SAML, ao contrário, pressupunha acordos formais entre organizações que já se conheciam — encaixando no modelo real de adoção corporativa da época, com implementação feita por times internos que absorviam a complexidade do XML sem problema. Resultado: o SAML prosperou resolvendo um problema real de federação entre empresas que já confiavam umas nas outras, enquanto o OpenID original — aberto demais, sem incentivo claro de adoção — foi descontinuado por volta de 2014, mesmo ano em que o OpenID Connect foi lançado (protocolo diferente, apesar do nome). Ver [[wiki/sources/openid-connect-oidc-autenticacao-alem-do-oauth]].

## Relação com outros conceitos

- [[wiki/concepts/openid-connect]] — implementação moderna de SSO/identidade federada
- [[wiki/concepts/oauth2]] — base de autorização sobre a qual o OIDC (e portanto o SSO moderno) é construído
- [[wiki/concepts/mfa-multifator-autenticacao]] — MFA costuma ser aplicado uma única vez no IdP central, beneficiando todos os serviços downstream
- [[wiki/concepts/openid-legado]] — predecessor homônimo do OIDC, tecnicamente não relacionado, contraponto histórico direto ao SAML

## Key Sources

- [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]]
- [[wiki/sources/openid-connect-oidc-autenticacao-alem-do-oauth]] — contraste de premissas de confiança entre SAML e OpenID original; JSON (OIDC) vs. XML (SAML)
