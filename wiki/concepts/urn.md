---
type: concept
title: "URN — Uniform Resource Name"
aliases: ["urn", "uniform resource name", "nome de recurso"]
date_created: 2026-10-09
date_updated: 2026-10-09
source_count: 1
tags: [uri, url, http, redes, networking]
skill: tech-mentor-networking
status: draft
---

# URN — Uniform Resource Name

**Um tipo de [[wiki/concepts/uri|URI]] que identifica o recurso por um nome persistente, sem dizer onde ele está nem como obtê-lo pela rede.** Exemplo da fonte: o **ISBN** de um livro identifica a obra, mas não informa ao computador como buscá-la.

Contraste: [[wiki/concepts/url|URL]] localiza (*onde/como*); URN nomeia (*quem é*). Ambas são URIs porque ambas identificam um recurso.

- [external] Forma textual: `urn:<NID>:<NSS>`, ex.: `urn:isbn:9780131103627` (RFC 8141, que atualiza a RFC 2141). https://www.rfc-editor.org/rfc/rfc8141
- Nota: o vídeo diz que o ISBN "se aproxima" de uma URN — não que seja uma por si só; a forma `urn:isbn:…` é o que o torna URI.

## Key sources
- [[wiki/sources/url-vs-uri-diferenca-urn-identificacao-localizacao]] — ISBN como exemplo de identificação por nome
