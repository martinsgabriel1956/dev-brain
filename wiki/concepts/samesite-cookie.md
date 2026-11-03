---
type: concept
title: "Atributo SameSite de Cookie"
aliases: ["samesite", "samesite cookie", "SameSite=Lax", "SameSite=Strict", "SameSite=None"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_count: 3
tags: [samesite, cookies, csrf, navegador, seguranca]
skill: tech-mentor-security
status: draft
---

# Atributo SameSite de Cookie

Atributo que diz ao navegador quando enviar um cookie em requisições vindas de outro site. Com `lax` ou `strict`, pode impedir [[wiki/concepts/csrf]], porque a requisição crítica deixa de sair autenticada ([[wiki/sources/csrf-cross-site-request-forgery]]).

## Valores

[external] Segundo a [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie):

| Valor | Envio entre sites |
|---|---|
| `Strict` | nunca |
| `Lax` | só em navegação top-level com método seguro; não em iframe, `fetch()`, subrecursos ou POST |
| `None` | sempre; exige `Secure` |

[[wiki/sources/browser-security]] registra o trade-off de `Strict`: quem chega por um link externo parece deslogado.

## Padrão quando o atributo falta

Varia por navegador. [external] A MDN diz que alguns usam `Lax`, numa versão mais permissiva que também envia o cookie em POST se ele foi definido há no máximo dois minutos. A [PortSwigger](https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions) diz que o Chrome faz isso desde 2021 e os demais usam `None`, mas trata a adoção pelos outros como futura, sem data. O estado atual por navegador não foi confirmado nesta ingestão. Definir o atributo explicitamente evita depender disso (recomendação da wiki).

## Não é defesa suficiente sozinho

O vídeo apresenta `SameSite` lado a lado com o [[wiki/concepts/csrf-token|token]]. [external] O [cheat sheet da OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) o coloca em defesa em profundidade, e a PortSwigger documenta bypasses:

- **GET com efeito de estado:** se a ação aceita GET, uma navegação top-level passa por `Lax`. Inclui frameworks com override de método. Ver [[wiki/concepts/metodos-http]].
- **Gadget no próprio site:** um redirecionamento no cliente, controlado pelo atacante, gera um pedido same-site e passa por `Strict`. Redirecionamento no servidor não produz o mesmo efeito.
- **Domínio irmão:** o atributo compara site, não [[wiki/concepts/same-origin-policy|origem]], então um XSS em `blog.exemplo.com` pode atacar `app.exemplo.com`.

## Relação com outros conceitos

- [[wiki/concepts/sessoes-http-cookies]] — os outros atributos de cookie de sessão (`HttpOnly`, `Secure`)
- [[wiki/concepts/cross-site-websocket-hijacking]] — a mesma família de ataque no handshake de WebSocket

## Key sources

- [[wiki/sources/csrf-cross-site-request-forgery]] — `lax`/`strict` como segunda defesa, sem ressalvas
- [[wiki/sources/browser-security]] — trade-off de `Strict` com links externos
- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]] — `SameSite=Strict` em cookies de sessão reais
