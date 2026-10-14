---
type: concept
title: "CGI (Common Gateway Interface)"
aliases: ['CGI', 'Common Gateway Interface']
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [web, backend, cgi, historia, perl]
skill: tech-mentor-frontend
status: draft
---

# CGI (Common Gateway Interface)

Padrão em que o servidor web, ao receber um pedido de **executável** em vez de arquivo, roda o programa no servidor e devolve a saída (esperada como HTML) ao navegador. Para o navegador nada muda; para a web, nasce o conteúdo **dinâmico** (vs. estático).

- Primeiros CGIs eram binários em C ("canhão para matar mosca" para gerar HTML); **Perl**, melhor com strings e [[wiki/concepts/regex-expressao-regular|regex]], virou a linguagem principal.
- Limitação: um processo externo por requisição. PHP e ASP responderam embutindo o interpretador no servidor ([[wiki/entities/apache-http-server|Apache]], IIS) — ver [[wiki/concepts/servidor-web-vs-servidor-de-aplicacao]].
- [external] RFC 3875 formaliza o CGI (https://www.rfc-editor.org/rfc/rfc3875).

Contexto: [[wiki/concepts/historia-do-front-end]].

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
