---
type: concept
title: "AJAX"
aliases: ['Asynchronous JavaScript and XML']
date_created: 2026-10-14
date_updated: 2026-11-16
source_count: 3
tags: [ajax, javascript, web, historia]
skill: tech-mentor-frontend
status: draft
---

# AJAX

Requisições assíncronas do navegador ao servidor sem recarregar a página. Garoto-propaganda: [[wiki/entities/gmail]] (2004). Base técnica das [[wiki/concepts/single-page-application|SPAs]]. [external] `XMLHttpRequest` foi criado pela Microsoft (IE5); o termo "AJAX" foi cunhado por Jesse James Garrett em 2005 (de memória, sem URL verificada). Ver [[wiki/concepts/historia-do-front-end]].

Em [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]], [[wiki/entities/nasser|Násser]] abre a lista de exemplos de JavaScript assíncrono com o AJAX, e a vantagem que dá é a dele: "carregar seção [...] sem precisar recarregar a página inteira" (o miolo do produto num e-commerce). Ver [[wiki/concepts/javascript-assincrono]].

Em [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]], [[wiki/entities/nasser|Násser]] define AJAX como "Asynchronous JavaScript XML [...] o uso do objeto XML HTTP request" e mostra na prática: `new XMLHttpRequest()`, `open`/`send` contra a API do GitHub, `onreadystatechange` e `JSON.parse(responseText)`. Vende como alternativa ao "clássico do F5". O nome completo tem "and", e a técnica não é "simplesmente o JavaScript assíncrono". Ver [[wiki/concepts/xmlhttprequest]].

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
- [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]]: FrontPUSH, JavaScript aula 12: AJAX como primeiro exemplo de assíncrono
- [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]]: FrontPUSH, JavaScript aula 14: AJAX na prática com XHR
