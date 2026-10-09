---
type: concept
title: "URL — Uniform Resource Locator"
aliases: ["url", "uniform resource locator", "endereço web", "localizador de recurso"]
date_created: 2026-10-09
date_updated: 2026-10-09
source_count: 1
tags: [uri, url, http, redes, networking]
skill: tech-mentor-networking
status: draft
---

# URL — Uniform Resource Locator

**Um tipo de [[wiki/concepts/uri|URI]] que, além de identificar o recurso, diz onde ele está e como acessá-lo**: qual protocolo usar, qual host contatar e qual recurso alcançar. Por identificar um recurso, toda URL é também URI.

## No dia a dia

- Barra de endereço, "parâmetros de URL", "roteamento de URL" — o uso coloquial de "URL" para qualquer endereço web é normal; tecnicamente o termo é mais específico que URI.
- Pergunta "qual a URL desta página?" = **onde** o recurso pode ser encontrado.
- Em APIs, o caminho identifica o [[wiki/concepts/recurso-rest|recurso]] e um query parameter pode filtrar/selecionar (ex.: um cliente específico); a string toda é URI e URL ao mesmo tempo (ver [[wiki/concepts/requisicao-http]]).
- A parte de protocolo liga a URL a [[wiki/concepts/http-vs-https]]; a de host, a [[wiki/concepts/dns]].

## Contraste com URN

URL = *onde/como*; [[wiki/concepts/urn|URN]] = *nome persistente*.

## Key sources
- [[wiki/sources/url-vs-uri-diferenca-urn-identificacao-localizacao]] — URL como URI com localização; uso coloquial vs. técnico
