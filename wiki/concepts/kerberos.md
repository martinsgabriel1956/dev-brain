---
type: concept
title: "Kerberos"
aliases: ["Kerberos", "Kerberos V5", "protocolo Kerberos", "cérberos"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 1
tags: [kerberos, autenticacao, sso, active-directory, seguranca]
skill: tech-mentor-security
status: draft
---

# Kerberos

Protocolo de autenticação criado no MIT nos anos 80, com o objetivo de permitir que qualquer usuário se autenticasse em qualquer máquina de uma rede local usando seu login de rede, sem nunca expor a senha na rede. É o antecessor conceitual direto do modelo de Identity Provider usado no SSO moderno.

## O modelo do "cão de guarda"

Em vez de provar sua identidade separadamente para cada servidor (o que exigiria múltiplas senhas), o usuário prova sua identidade uma vez para um terceiro confiável — o **Key Distribution Center (KDC)** — e recebe um **ticket** (equivalente a um token). Esse ticket é apresentado aos demais servidores, que confiam no KDC e concedem acesso sem exigir nova autenticação.

O nome vem do cão de três cabeças da mitologia grega que guardava a entrada do mundo dos mortos. As três cabeças do protocolo representam seus três pilares: o cliente, o servidor, e o KDC.

## Adoção pela Microsoft

O momento divisor de águas para o Kerberos ocorreu no final dos anos 90/início dos anos 2000, quando a [[wiki/entities/microsoft]] adotou o **Kerberos V5** como protocolo de autenticação padrão do Windows 2000 e do Active Directory. É definido pela **RFC 4120** e ainda hoje é o mecanismo padrão de autenticação em redes locais corporativas Windows.

## Limitação: pensado para rede local

Kerberos opera com tickets e sessões persistentes, assumindo conexão direta com o servidor (o KDC) dentro de uma rede local fechada. Quando a autenticação precisou atravessar a fronteira da internet — aplicações web corporativas acessadas de fora da intranet — esse modelo deixou de ser suficiente, abrindo espaço para protocolos baseados em **tokens e claims verificáveis por assinatura digital** (como [[wiki/concepts/saml]] e, mais tarde, [[wiki/concepts/openid-connect]]). O princípio central — confiar em um terceiro para não reautenticar em cada sistema — se manteve; o mecanismo de transporte mudou.

## Relação com outros conceitos

- [[wiki/concepts/saml]] — protocolo web que resolve o mesmo problema (autenticação federada) fora dos limites de uma rede local; não é sucessor técnico direto do Kerberos, mas compartilha o princípio de "confiar em um terceiro"
- [[wiki/concepts/sso-single-sign-on]] — Kerberos é um antecessor histórico do conceito moderno de SSO
- [[wiki/concepts/ldap]] — frequentemente usado junto do Kerberos em ambientes Active Directory (LDAP como diretório de usuários, Kerberos como protocolo de autenticação)

## Key Sources

- [[wiki/sources/autenticacao-federada-sso-saml-bernardo-lobato]] — origem no MIT, modelo do ticket, adoção pela Microsoft, transição para o SSO baseado em token
