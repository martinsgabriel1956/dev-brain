---
type: concept
title: "LDAP"
aliases: ["LDAP", "Lightweight Directory Access Protocol", "diretório corporativo", "Active Directory"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 1
tags: [ldap, autenticacao, active-directory, identity-management, seguranca]
skill: tech-mentor-security
status: draft
---

# LDAP

Protocolo para consultar e manter **diretórios** de informação distribuídos — na prática, a base de dados que cadastra todos os usuários de uma organização e vira um provedor de autenticação corporativo. O LDAP moderno (versão 3) é definido em um conjunto de RFCs (RFC 4510 e correlatas).

## "chmod corporativo"

Uma analogia útil: assim como o `chmod` do Unix concede permissões em diretórios de arquivos numa máquina local, o LDAP concede permissões dentro de "diretórios" corporativos — uma estrutura hierárquica de usuários, grupos e recursos. Ver [[wiki/concepts/permissoes-unix]] para a analogia do lado do sistema operacional.

## Uso histórico e atual

Muito comum entre o final dos anos 90 e meados dos anos 2000, período da explosão de sistemas web internos (intranets, portais corporativos). Ainda hoje é amplamente usado como base de autenticação corporativa — mais notavelmente integrado ao **Microsoft Active Directory** — além de uso em VPNs, proxies, acesso a e-mail e outros serviços internos.

## O que o LDAP resolve — e o que não resolve

Uma base LDAP única resolve a fragmentação de bases de usuários: um único conjunto de credenciais para toda a organização, em vez de uma base por sistema. O que o LDAP **não** resolve sozinho é o problema de múltiplas autenticações: mesmo com login/senha únicos, o usuário ainda precisava se autenticar em cada sistema individualmente — o LDAP fornece a base de identidade, mas não um mecanismo de "autenticar uma vez e propagar" entre sistemas. Esse passo seguinte é o papel de protocolos como [[wiki/concepts/kerberos]] (rede local) e depois [[wiki/concepts/saml]]/[[wiki/concepts/openid-connect]] (web).

## Relação com outros conceitos

- [[wiki/concepts/kerberos]] — frequentemente coexistem em ambientes Active Directory: LDAP como diretório de usuários, Kerberos como protocolo de autenticação
- [[wiki/concepts/saml]] — o IdP de um fluxo SAML corporativo tipicamente autentica o usuário consultando uma base LDAP/Active Directory por trás
- [[wiki/concepts/sso-single-sign-on]] — LDAP é a camada de identidade sobre a qual protocolos de SSO são construídos, não um protocolo de SSO em si

## Key Sources

- [[wiki/sources/autenticacao-federada-sso-saml-bernardo-lobato]] — LDAP como "chmod corporativo", contexto histórico (fim anos 90 – meados anos 2000), integração com Active Directory
