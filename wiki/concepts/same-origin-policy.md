---
type: concept
title: "Same-Origin Policy"
aliases: ["same-origin policy", "sop", "política de mesma origem", "cross-origin read", "cross-origin write"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_count: 2
tags: [same-origin-policy, navegador, seguranca, origem, cross-origin]
skill: tech-mentor-security
status: draft
---

# Same-Origin Policy

Política do navegador que limita como uma origem interage com outra. Duas URLs têm a mesma origem quando protocolo, domínio e porta são iguais ([[wiki/sources/csrf-cross-site-request-forgery]], [[wiki/sources/browser-security]]).

## Os três cenários

| Cenário | Exemplos | Padrão |
|---|---|---|
| **Cross-origin write** | envio de formulário, redirect | geralmente permitido |
| **Cross-origin embedding** | imagem, style sheet, iframe | geralmente permitido |
| **Cross-origin read** | ler a resposta de uma requisição | bloqueado |

[external] A classificação é a da [MDN](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy), que faz duas ressalvas: alguns pedidos exigem preflight, e o embedding vaza parte da informação, como as dimensões de uma imagem incorporada.

## O que a política não impede

A escrita passa. É por isso que [[wiki/concepts/csrf]] funciona sem violar a política: a requisição autenticada chega ao servidor, e o atacante não precisa ler a resposta ([[wiki/sources/csrf-cross-site-request-forgery]]). [external] A própria MDN indica um token imprevisível para bloquear escritas entre origens ([[wiki/concepts/csrf-token]]).

## Origem não é site

Origem compara protocolo, domínio e porta. [[wiki/concepts/samesite-cookie|`SameSite`]] compara **site**, que é mais amplo: `app.exemplo.com` e `blog.exemplo.com` são origens diferentes, mas o mesmo site. [external] Definição em [PortSwigger](https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions). A MDN também avisa que cookies usam uma definição própria de origem.

## Relação com outros conceitos

- [[wiki/concepts/cors]] — relaxa a política de forma controlada, a partir do servidor
- [[wiki/concepts/cors-misconfiguration]] — quando esse relaxamento é amplo demais
- [[wiki/concepts/xss]] — o script injetado roda na própria origem da vítima, então a política não o contém `[external — conhecimento geral]`

## Key sources

- [[wiki/sources/csrf-cross-site-request-forgery]] — os três cenários e por que CSRF não quebra a política
- [[wiki/sources/browser-security]] — a política como base da segurança do navegador (scheme + host + port)
