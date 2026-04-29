---
type: source
title: "Federated Identity"
aliases: ["federated identity", "saml", "sso", "scim", "identity federation", "home realm discovery", "ciam"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/federated-identity.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [federated-identity, saml, oidc, sso, scim, home-realm-discovery, ciam, azure-ad, okta]
skill: tech-mentor-security
status: stable
---

## TL;DR

Federated Identity: autenticação delegada a um IdP externo. SAML 2.0 para integração enterprise legada (SAP, Workday). OIDC para sistemas modernos, mobile, APIs. SCIM para provisionamento automático de usuários. Identity Router (Auth0, Keycloak) normaliza múltiplos IdPs. CIAM (Customer Identity) separa identidade de clientes de colaboradores.

## Key Claims

**Claim:** OIDC substituiu SAML para sistemas novos — JSON/REST vs XML complexo, suporte nativo a mobile.
**Evidence:** SAML: XML assinado, complexidade alta (metadata, bindings, assertions), desenvolvido para browser flows. Mobile: SAML não funciona bem fora do browser. OIDC: JWT em JSON, Auth Code + PKCE para mobile, federation com Google/Apple/GitHub trivial. Apenas integrar com sistemas enterprise legados justifica SAML hoje.
**Confidence:** alta

**Claim:** SCIM automatiza provisionamento e desprovisionamento — sem SCIM, offboarding tem risco de contas órfãs.
**Evidence:** Sem SCIM: colaborador sai da empresa → RH desativa no AD → conta no SaaS permanece ativa por meses. Com SCIM: IdP (Okta/Azure AD) provisiona automaticamente ao criar no AD, desprovisiona ao desativar. Reduz janela de acesso indevido de semanas para minutos.
**Confidence:** alta

**Claim:** SSO com múltiplos IdPs requer Identity Router — normaliza identidades de fontes diferentes.
**Evidence:** Enterprise: Okta (colaboradores, SAML) + Azure AD (parceiros, OIDC) + Google (clientes, OIDC). Identity Router (Auth0, Keycloak) faz home realm discovery ("qual IdP para este email?"), normaliza claims para formato interno, gerencia sessão federada única. Sem router: cada app integra com N IdPs separadamente.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/federated-identity]]
- [[concepts/saml]]
- [[concepts/oidc]]
- [[concepts/sso]]
- [[concepts/scim]]
- [[concepts/home-realm-discovery]]
- [[entities/okta]]
- [[entities/azure-ad]]

## Open Questions

- SCIM com sync bidirecional (app → IdP) — como lidar com conflitos de atributos entre sistemas?
- CIAM para B2B com múltiplos tenants — como isolar identidades de clientes diferentes no mesmo sistema?
