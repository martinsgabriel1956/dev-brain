---
type: concept
title: "SSO — Single Sign-On"
aliases: ["SSO", "Single Sign-On", "Identity Provider", "IdP"]
date_created: 2026-07-27
date_updated: 2026-08-18
source_count: 3
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

- **[[wiki/concepts/saml|SAML 2.0]]** — protocolo XML dominante em SSO corporativo legado (Active Directory, Okta, Workday). Mais verboso, mas ainda é o padrão exigido por muitos sistemas enterprise. Fluxo: IdP e SP trocam metadados (certificado X.509) previamente; login gera `SAMLRequest`/`SAMLResponse` assinada, transportada via redirecionamentos no browser.
- **[[wiki/concepts/openid-connect]] (OIDC)** — construído sobre [[wiki/concepts/oauth2|OAuth 2.0]], formato JSON/JWT, é a base do login social moderno ("Entrar com Google") e de CIAM (Customer Identity and Access Management).

SSO corporativo (SAML) é historicamente anterior ao OAuth/OIDC — a ideia de "autenticar uma vez, confiar em todo lugar" já existia no mundo enterprise antes de virar identidade federada aberta ao público via login social. O antecessor conceitual mais antigo é o [[wiki/concepts/kerberos|Kerberos]] (MIT, anos 80): mesmo princípio de "provar identidade a um terceiro confiável e receber um ticket aceito por outros servidores", mas pensado para rede local — a transição para SSO web ocorreu quando esse modelo precisou atravessar a fronteira da internet, trocando tickets/chaves simétricas por tokens/claims verificados por assinatura digital. A base de usuários por trás do IdP costuma ser um diretório [[wiki/concepts/ldap|LDAP]] (ex.: Active Directory).

## Por Que o SAML Sobreviveu e o OpenID Original Não

O [[wiki/concepts/openid-legado|OpenID original]] (2005) tentou resolver o mesmo problema de identidade federada que o SAML, mas com uma premissa de confiança oposta: qualquer site aceitando qualquer provedor de identidade, sem governança nem relação de confiança pré-estabelecida. O SAML, ao contrário, pressupunha acordos formais entre organizações que já se conheciam — encaixando no modelo real de adoção corporativa da época, com implementação feita por times internos que absorviam a complexidade do XML sem problema. Resultado: o SAML prosperou resolvendo um problema real de federação entre empresas que já confiavam umas nas outras, enquanto o OpenID original — aberto demais, sem incentivo claro de adoção — foi descontinuado por volta de 2014, mesmo ano em que o OpenID Connect foi lançado (protocolo diferente, apesar do nome). Ver [[wiki/sources/openid-connect-oidc-autenticacao-alem-do-oauth]].

## Relação com outros conceitos

- [[wiki/concepts/openid-connect]] — implementação moderna de SSO/identidade federada
- [[wiki/concepts/oauth2]] — base de autorização sobre a qual o OIDC (e portanto o SSO moderno) é construído
- [[wiki/concepts/mfa-multifator-autenticacao]] — MFA costuma ser aplicado uma única vez no IdP central, beneficiando todos os serviços downstream
- [[wiki/concepts/openid-legado]] — predecessor homônimo do OIDC, tecnicamente não relacionado, contraponto histórico direto ao SAML
- [[wiki/concepts/saml]] — protocolo em detalhe (fluxo IdP/SP, troca de metadados, assertions)
- [[wiki/concepts/kerberos]] — antecessor conceitual do modelo de "terceiro confiável", pensado para rede local
- [[wiki/concepts/ldap]] — diretório de usuários tipicamente por trás do IdP em ambientes corporativos
- [[wiki/concepts/federated-identity]] — modelo de terceirização de confiança que o SSO implementa

## Key Sources

- [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]]
- [[wiki/sources/openid-connect-oidc-autenticacao-alem-do-oauth]] — contraste de premissas de confiança entre SAML e OpenID original; JSON (OIDC) vs. XML (SAML)
- [[wiki/sources/autenticacao-federada-sso-saml-bernardo-lobato]] — protocolo SAML em detalhe, origem em LDAP/Kerberos, ponte SAML→OAuth
