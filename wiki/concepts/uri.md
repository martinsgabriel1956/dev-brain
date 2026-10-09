---
type: concept
title: "URI — Uniform Resource Identifier"
aliases: ["uri", "uniform resource identifier", "identificador de recurso"]
date_created: 2026-10-09
date_updated: 2026-10-09
source_count: 1
tags: [uri, url, http, redes, networking]
skill: tech-mentor-networking
status: draft
---

# URI — Uniform Resource Identifier

**O conceito mais amplo: identificar um recurso** (página, imagem, endpoint de API, arquivo...). Não promete dizer onde ele está nem como obtê-lo. Segundo [[wiki/sources/url-vs-uri-diferenca-urn-identificacao-localizacao]]: "URI é sobre identificação; URL é especificamente sobre localizar".

## Relação com URL e URN

```
URI  ── identifica um recurso
 ├─ URL  ── identifica E diz onde/como acessar (https://…)
 └─ URN  ── identifica por nome persistente (urn:isbn:…)
```

Toda URL é URI; nem toda URI é URL. Na prática, o vocabulário de dev mistura tudo ("API URL", "endpoint URL", "URI"): num endpoint HTTP comum o termo é intercambiável, pois a string é URI **e** URL.

## Referência relativa

Uma URI não precisa trazer localização de rede completa: dentro de um site, um recurso pode ser citado por [[wiki/concepts/referencia-relativa-de-uri|referência relativa]].

## Mnemônico da fonte

Nome identifica a pessoa; endereço diz onde encontrá-la. URI = identidade; URL = identidade + meio de localizar.

## Sintaxe e normas

- [external] RFC 3986 (IETF, 2005) define a sintaxe genérica: `scheme:[//authority]path[?query][#fragment]`; ver [[wiki/concepts/fragment-identifier-url]] e [[wiki/entities/ietf]]. https://www.rfc-editor.org/rfc/rfc3986
- [external] A própria RFC 3986 trata "URL" e "URN" como classificações informais; hoje o WHATWG URL Standard usa só "URL" para tudo. Isso explica o uso cotidiano frouxo. https://url.spec.whatwg.org/

## Key sources
- [[wiki/sources/url-vs-uri-diferenca-urn-identificacao-localizacao]] — definição, relação URI ⊃ URL/URN, analogia nome/endereço
