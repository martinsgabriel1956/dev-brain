---
type: concept
title: "Federated Identity"
aliases: ["identidade federada", "autenticação federada", "federation"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 2
tags: [federated-identity, sso, saml, oidc, identity-provider, seguranca]
skill: tech-mentor-security
status: draft
---

# Federated Identity

Modelo de **terceirização de confiança**: uma organização aceita a identidade de um usuário validada por outra organização, sem que ambas precisem compartilhar o mesmo banco de dados de senhas. Em vez de cada serviço exigir sua própria conta, a federação estabelece uma ponte de confiança — a prova de identidade emitida por uma entidade confiável (o Identity Provider) é aceita por terceiros (Service Providers).

## Exemplos do dia a dia

Login no Trello com a conta do Google. Acesso ao Slack via conta Microsoft Entra ID da empresa. Login num e-commerce usando o Facebook. Em todos os casos, o usuário nunca revela sua senda ao serviço que está acessando — apenas ao provedor de identidade original.

## Protocolos que implementam o conceito

- [[wiki/concepts/saml]] — federação corporativa legada, XML, dominante em SSO enterprise
- [[wiki/concepts/openid-connect]] — federação moderna, JSON/JWT, base do login social e de CIAM
- [[wiki/concepts/kerberos]] — antecessor histórico do modelo (rede local, não web)

## Identity Router para múltiplos IdPs

Em ambientes enterprise com múltiplos provedores de identidade simultâneos (ex.: Okta para colaboradores via SAML, Azure AD para parceiros via OIDC, Google para clientes via OIDC), um **Identity Router** (Auth0, Keycloak) normaliza as identidades: faz *home realm discovery* ("qual IdP corresponde a este e-mail?"), converte claims de formatos diferentes para um formato interno único, e gerencia a sessão federada. Sem esse componente, cada aplicação teria que integrar separadamente com N provedores.

## SCIM: o outro lado da federação

Autenticação federada resolve "quem pode logar", mas não resolve sozinha o **provisionamento/desprovisionamento** de contas — o problema descrito em [[wiki/sources/autenticacao-federada-sso-saml-bernardo-lobato]] de contas órfãs após desligamento de funcionários. O **SCIM** (System for Cross-domain Identity Management) automatiza essa parte: o IdP central provisiona a conta no SaaS ao criar o usuário no diretório, e desprovisiona automaticamente ao desativá-lo — reduzindo a janela de acesso indevido de semanas para minutos.

## Relação com outros conceitos

- [[wiki/concepts/sso-single-sign-on]] — SSO é a experiência do usuário (autenticar uma vez); federated identity é o modelo de confiança que a viabiliza entre organizações
- [[wiki/concepts/saml]] — implementação corporativa legada
- [[wiki/concepts/openid-connect]] — implementação moderna
- [[wiki/concepts/oauth2]] — camada de autorização sobre a qual o OIDC é construído

## Key Sources

- [[wiki/sources/federated-identity]] — SCIM, Identity Router, CIAM
- [[wiki/sources/autenticacao-federada-sso-saml-bernardo-lobato]] — definição do modelo de terceirização de confiança, exemplos, e o problema de revogação de acesso que a federação sozinha não resolve
