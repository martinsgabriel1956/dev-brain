---
type: concept
title: "HTTP Caching (Browser)"
aliases: ["cache do browser", "cache HTTP"]
date_created: 2026-07-28
date_updated: 2026-11-19
source_count: 4
tags: [http, cache, browser, critical-rendering-path, performance]
skill: tech-mentor-frontend
status: stub
---
# HTTP Caching (Browser)

Primeira checagem do browser ao processar uma URL, antes de qualquer etapa de rede: se a página já foi visitada e o cache ainda é válido, o browser usa a versão salva diretamente, pulando [[wiki/concepts/dns]], [[wiki/concepts/tcp-three-way-handshake]], [[wiki/concepts/tls-handshake]] e o request HTTP inteiramente.

**Nota em aberto**: a fonte original trata "cache" de forma genérica, sem distinguir cache HTTP comum (headers `Cache-Control`, `ETag`) de bfcache (back/forward cache, mecanismo separado para navegação para trás/frente que preserva o estado JS da página). Ver open question em [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]] — vale expandir esta página distinguindo os dois mecanismos numa futura ingestão.

Em [[wiki/sources/frontpush-axios-cdn-get-then-encapsulamento-xhr]], o `cache-control` aparece na resposta da API do GitHub vista pelo Axios, descrito como "configurações de metadata": é a instrução do servidor sobre quanto tempo a resposta pode ser reaproveitada.

## Arquivo externo × CSS no HTML (FrontPUSH, otimização aula 02)

Em [[wiki/sources/frontpush-cache-e-cdn-css-js-inline-incorporado-externo]]: "por padrão, os arquivos CSS e JS são armazenados em cache pelo browser", e CSS inline ou incorporado "está na própria página do HTML", que "o browser sempre vai ler de novo". O "por padrão" é dos headers (`Cache-Control`, `ETag`; sem eles, cache heurístico), e o HTML também cacheia, mas costuma ser revalidado a cada visita. O hard refresh depois de subir CSS novo é o sintoma que o [[wiki/concepts/cache-busting]] resolve.

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — `Cache-Control` como header que define se a resposta pode ser guardada e reaproveitada (ver [[wiki/concepts/http-headers]])
- [[wiki/sources/frontpush-axios-cdn-get-then-encapsulamento-xhr]]: FrontPUSH, JavaScript aula 16: cache-control na resposta do GitHub
- [[wiki/sources/frontpush-cache-e-cdn-css-js-inline-incorporado-externo]]: FrontPUSH, otimização aula 02: CSS/JS externos cacheiam, CSS no HTML não
