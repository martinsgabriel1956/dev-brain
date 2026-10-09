---
type: source
title: "URL vs URI: qual é a diferença (e onde entra a URN)"
aliases: ["url vs uri", "diferença entre url e uri", "uri url urn"]
date_created: 2026-10-09
date_updated: 2026-10-09
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/url-vs-uri-diferenca-urn-identificacao-localizacao.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-10-09
source_count: 1
tags: [uri, url, urn, http, apis, redes, networking]
skill: tech-mentor-networking
status: stable
---

## TL;DR

Vídeo explicativo (EN, traduzido; autor não identificado) que desfaz a confusão URL/URI: [[wiki/concepts/uri]] é o conceito amplo de **identificar** um recurso; [[wiki/concepts/url]] é um tipo de URI que também diz **onde e como acessar**; [[wiki/concepts/urn]] é o tipo que identifica **por nome persistente** (ex.: ISBN). Toda URL é URI, nem toda URI é URL. Em APIs/web o endereço comum é URL, por isso os termos parecem intercambiáveis no dia a dia.

## Key Claims

**Claim:** URI identifica um recurso; URL identifica e localiza (protocolo + host + recurso); logo URL ⊂ URI.
**Evidence:** definição + exemplo de endereço web.
**Confidence:** alta. [external] RFC 3986 (https://www.rfc-editor.org/rfc/rfc3986).

**Claim:** URN identifica por nome, sem localização — o ISBN é o exemplo; URI é a categoria, URL e URN são formas dentro dela.
**Evidence:** analogia do ISBN do livro.
**Confidence:** média-alta. [external] O ISBN em si é um identificador; vira URN na forma `urn:isbn:…` (RFC 8141). Além disso, a RFC 3986 considera URL/URN classificações informais, e o WHATWG URL Standard só usa "URL" — a taxonomia do vídeo é a didática clássica, não a única visão atual.

**Claim:** Um endpoint de API com query parameter é URI e URL ao mesmo tempo; por isso "API URL", "endpoint URL" e "URI" se misturam.
**Evidence:** exemplo do recurso "cliente" (customer), sem a string literal.
**Confidence:** alta; liga a [[wiki/concepts/recurso-rest]] e [[wiki/concepts/requisicao-http]].

**Claim:** URI não precisa trazer localização de rede completa — referências relativas dentro de um site.
**Evidence:** menção breve.
**Confidence:** alta (ver [[wiki/concepts/referencia-relativa-de-uri]]); fonte não aprofunda.

**Claim:** Mnemônico — nome identifica a pessoa, endereço diz onde achá-la.
**Evidence:** analogia.
**Confidence:** alta como memorização; imprecisa ao pé da letra (um endereço de pessoa não é URL de nada).

**Claim:** No uso cotidiano "URL" serve para qualquer endereço web (barra de endereço, "URL routing"); tecnicamente é termo mais específico.
**Evidence:** observação do autor.
**Confidence:** alta.

## Entities

Nenhuma entidade central. [external] IETF/RFC 3986 aparece só como referência cruzada em [[wiki/entities/ietf]].

## Concepts

[[wiki/concepts/uri]], [[wiki/concepts/url]], [[wiki/concepts/urn]], [[wiki/concepts/referencia-relativa-de-uri]], [[wiki/concepts/recurso-rest]], [[wiki/concepts/requisicao-http]], [[wiki/concepts/fragment-identifier-url]], [[wiki/concepts/protocolo-de-rede]], [[wiki/concepts/dns]], [[wiki/concepts/http-vs-https]], [[wiki/concepts/debug-de-requisicao-http]].

## Open Questions

- O vídeo não cita a **sintaxe** (scheme, authority, path, query, fragment) nem a RFC 3986; query e fragment ficam implícitos.
- Nada sobre **data URIs** e outros esquemas não-localizáveis (`mailto:`, `data:`) — casos que testam a fronteira URL/URI.
- Não explica por que a distinção URL/URN perdeu relevância prática (ver nota WHATWG).
