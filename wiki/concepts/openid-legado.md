---
type: concept
title: "OpenID (protocolo original, 2005–2014)"
aliases: ["OpenID 1.0", "OpenID 2.0", "OpenID original", "URL-based identity"]
date_created: 2026-08-13
date_updated: 2026-08-13
source_count: 1
tags: [openid, identidade-federada, historia, descontinuado, autenticacao, seguranca]
skill: tech-mentor-security
status: stub
---

# OpenID (protocolo original, 2005–2014)

Primeiro padrão aberto de identidade federada na web, criado por volta de 2005 — **não deve ser confundido com o** [[wiki/concepts/openid-connect|OpenID Connect]] (2014), que reaproveitou o nome mas abandonou completamente a especificação técnica original.

## A ideia: identidade como URL

Em vez de usuário/senha em cada site, a identidade do usuário era uma **URL controlada por ele** (ex.: `usuario.myopenid.com`). O site de destino (Relying Party) descobria dinamicamente, a partir dessa URL, qual provedor de identidade (Identity Provider) era responsável por autenticar aquele usuário: fazia um `GET` na URL, e o HTML de resposta continha tags `<link>` ocultas apontando para o provedor real.

## Fluxo

Inteiramente por redirecionamento de navegador: usuário informa a URL → site descobre o provedor via HTML → navegador é redirecionado ao provedor para login → provedor redireciona de volta com uma mensagem assinada (baseada em XML) confirmando a autenticação → site valida a assinatura e cria a sessão. O Relying Party nunca via login/senha do usuário diretamente.

## Por que não vingou

Comparado ao [[wiki/concepts/sso-single-sign-on|SAML]] — nascido quase na mesma época com objetivo parecido —, o OpenID original apostou numa visão aberta e descentralizada: qualquer site aceitando qualquer provedor de identidade. Isso é elegante em teoria, mas sem governança nem relação de confiança pré-estabelecida entre provedores e sites, aceitar logins de provedores aleatórios era um risco prático. O SAML, ao contrário, pressupunha acordos formais entre organizações que já se conheciam — o que se encaixava no modelo real de adoção corporativa da época.

Descontinuado por volta de 2014, coincidindo com o lançamento do OpenID Connect. Hoje só aparece em sistemas legados — usuários de WordPress, Blogger, AOL ou Yahoo desse período provavelmente têm uma URL OpenID esquecida. É difícil reproduzir o protocolo original mesmo para fins didáticos hoje: praticamente só via bibliotecas antigas já descontinuadas.

## Relação com outros conceitos

- [[wiki/concepts/openid-connect]] — sucessor que reaproveita o nome mas é tecnicamente outro protocolo, construído sobre OAuth 2 em vez de URL+HTML
- [[wiki/concepts/sso-single-sign-on]] — SAML como contraponto contemporâneo que prosperou por ter confiança formal pré-estabelecida

## Key Sources

- [[wiki/sources/openid-connect-oidc-autenticacao-alem-do-oauth]]
