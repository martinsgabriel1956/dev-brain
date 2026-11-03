---
type: concept
title: "Token CSRF"
aliases: ["csrf token", "anti-csrf token", "synchronizer token"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_count: 1
tags: [csrf, csrf-token, seguranca, formularios, appsec]
skill: tech-mentor-security
status: draft
---

# Token CSRF

Valor único e imprevisível gerado pelo backend, compartilhado com o cliente e exigido em toda ação sensível. O site do atacante consegue disparar a requisição, mas não consegue preencher o token, porque teria de adivinhá-lo ([[wiki/sources/csrf-cross-site-request-forgery]]). É a defesa direta contra [[wiki/concepts/csrf]].

Tira do ataque uma das condições de que ele precisa. [external] A [PortSwigger](https://portswigger.net/web-security/csrf) lista três: ação relevante, sessão só por cookie e nenhum parâmetro imprevisível.

## Exemplo na fonte

No laboratório, o formulário de troca de e-mail envia apenas o novo e-mail. A correção proposta é o backend inserir o valor do token no próprio formulário.

## O que a fonte não diz

[external] Segundo o [cheat sheet da OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html):

- Primeiro, use a proteção embutida do framework, se houver. Só na falta dela se implementa token à mão.
- O token deve ser único por sessão, secreto e imprevisível.
- Software com estado usa *synchronizer token*; sem estado, *double-submit cookie* assinado. A versão ingênua do double-submit é desaconselhada.
- [[wiki/concepts/xss]] derruba todas as mitigações de CSRF, porque o script injetado roda na origem da aplicação. Inferência da wiki: é ele que consegue ler o token do formulário.

## Relação com outros conceitos

- [[wiki/concepts/samesite-cookie]] — defesa complementar, no navegador
- [[wiki/concepts/oauth2]] — o parâmetro `state` cumpre papel análogo no fluxo de login (inferência da wiki; a fonte não trata de OAuth)
- [[wiki/concepts/sessoes-http-cookies]] — o envio automático de cookies é o que torna o token necessário

## Key sources

- [[wiki/sources/csrf-cross-site-request-forgery]] — o token como primeira defesa; ausência dele no laboratório
