---
type: concept
title: "SAML 2.0"
aliases: ["SAML", "Security Assertion Markup Language", "SAMLRequest", "SAMLResponse"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 1
tags: [saml, sso, federated-identity, xml, seguranca, identity-provider]
skill: tech-mentor-security
status: draft
---

# SAML 2.0

Protocolo de **autenticação federada** baseado em XML, criado no início dos anos 2000 para estender identidade além dos limites de uma rede local — projetado para a era da web, permitindo que empresas compartilhem autenticação com parceiros externos. A versão 2.0 (2005) consolidou o padrão e é a espinha dorsal do SSO corporativo moderno.

## As três partes do protocolo

- **Identity Provider (IdP)** — autentica o usuário de fato (ex.: Okta, Google Workspace, Microsoft Entra ID).
- **Service Provider (SP)** — o sistema que o usuário quer acessar.
- **Browser do usuário** — carrega as mensagens entre IdP e SP via redirecionamentos HTTP. O protocolo depende inteiramente do navegador para esse transporte.

## Setup: troca de metadados

Antes de qualquer login, IdP e SP trocam metadados: o IdP entrega ao SP um **certificado X.509** com sua chave pública. O SP salva essa chave e passa a confiar no IdP. A **chave privada nunca sai do IdP** — é o segredo usado para assinar as assertions.

## Fluxo (SP-initiated)

```
1. Usuário tenta acessar o SP, ainda não autenticado
2. SP gera uma SAMLRequest e redireciona o browser ao IdP
3. Usuário autentica no IdP (login+senha, possivelmente MFA)
   — o SP nunca vê a senha, tudo acontece na tela do IdP
4. IdP gera uma SAMLResponse: XML assinado digitalmente contendo
   assertions (e-mail, grupos, validade da sessão)
5. Browser redireciona a SAMLResponse de volta ao SP
6. SP valida a assinatura com a chave pública do IdP e concede acesso
```

Se a chave pública do IdP consegue validar a assinatura da `SAMLResponse`, o SP tem certeza de que só o dono da chave privada (o IdP) poderia ter gerado aquele documento — garantia de integridade e autenticidade sem que IdP e SP precisem de uma conexão direta servidor-a-servidor.

## Por que ainda domina o SSO corporativo legado

SAML pressupõe acordos formais de confiança entre organizações que já se conhecem — encaixa no modelo real de adoção corporativa, com times internos absorvendo a complexidade do XML. Continua sendo o padrão exigido por sistemas enterprise como Salesforce, SAP, Workday, e por integrações com Active Directory. Ver [[wiki/concepts/sso-single-sign-on]] para o contraste histórico com o OpenID original, que tentou resolver o mesmo problema com uma premissa de confiança oposta (qualquer site aceitando qualquer IdP) e não sobreviveu.

## Limitação: XML e dependência de browser

SAML é verboso (XML) e depende de redirecionamentos no navegador para funcionar — mal adequado a APIs REST e Single Page Applications, que não têm esse ciclo de redirect natural. Nesses casos, [[wiki/concepts/openid-connect]] (JSON/JWT, nativo para mobile e SPA) é a recomendação padrão.

## Ponte com OAuth

Uma assertion SAML pode ser apresentada a um Authorization Server [[wiki/concepts/oauth2|OAuth]] como credencial: o servidor valida a assinatura XML e, em troca, emite um access token (podendo ser um JWT). Essa ponte permite que APIs REST modernas consumam identidades vindas de diretórios corporativos legados sem reimplementar SAML no lado da API — unindo a robustez da federação empresarial à agilidade de tokens leves no ecossistema de microsserviços.

## Relação com outros conceitos

- [[wiki/concepts/sso-single-sign-on]] — SAML é uma das duas gerações de protocolo de SSO (a outra é OIDC)
- [[wiki/concepts/kerberos]] — antecessor conceitual (confiar em terceiro/ticket), mas protocolo tecnicamente independente, pensado para rede local
- [[wiki/concepts/ldap]] — frequentemente a base de usuários que o IdP consulta para autenticar (ex.: Active Directory)
- [[wiki/concepts/federated-identity]] — SAML é uma implementação concreta do conceito de identidade federada
- [[wiki/concepts/oauth2]] — pode receber uma assertion SAML como credencial e emitir um access token
- [[wiki/concepts/openid-connect]] — alternativa moderna, recomendada para SPA/mobile/API

## Key Sources

- [[wiki/sources/autenticacao-federada-sso-saml-bernardo-lobato]] — fluxo completo do protocolo, troca de metadados, ponte com OAuth
- [[wiki/sources/openid-connect-oidc-autenticacao-alem-do-oauth]] — contraste SAML vs. OpenID original vs. OIDC
- [[wiki/sources/federated-identity]] — SAML no contexto de Identity Router para múltiplos IdPs
