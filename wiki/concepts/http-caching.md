---
type: concept
title: "HTTP Caching (Browser)"
aliases: ["cache do browser", "cache HTTP"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [http, cache, browser, critical-rendering-path, performance]
skill: tech-mentor-frontend
status: stub
---
# HTTP Caching (Browser)

Primeira checagem do browser ao processar uma URL, antes de qualquer etapa de rede: se a página já foi visitada e o cache ainda é válido, o browser usa a versão salva diretamente, pulando [[wiki/concepts/dns]], [[wiki/concepts/tcp-three-way-handshake]], [[wiki/concepts/tls-handshake]] e o request HTTP inteiramente.

**Nota em aberto**: a fonte original trata "cache" de forma genérica, sem distinguir cache HTTP comum (headers `Cache-Control`, `ETag`) de bfcache (back/forward cache, mecanismo separado para navegação para trás/frente que preserva o estado JS da página). Ver open question em [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]] — vale expandir esta página distinguindo os dois mecanismos numa futura ingestão.

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
