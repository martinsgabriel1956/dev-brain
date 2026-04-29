---
type: source
title: "Deep Links — Universal Links / App Links"
aliases: ["deep links mobile", "universal links ios", "app links android", "deferred deep links"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-deep-links.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, deep-links, universal-links, app-links, deferred-deep-links]
skill: tech-mentor-mobile
status: stable
---

# Deep Links — Mobile

## TL;DR

Universal Links (iOS) e App Links (Android) usam HTTPS — abrem o app se instalado, fallback para browser. Requerem arquivo de verificação hospedado no domínio (`apple-app-site-association` / `assetlinks.json`). Deferred deep links funcionam mesmo quando o app não está instalado — Branch.io ou Firebase Dynamic Links. Esquemas proprietários (`myapp://`) inseguros — qualquer app pode registrar o mesmo scheme.

## Claims Principais

| Claim | Confiança |
|---|---|
| Universal Links/App Links são verificados pelo OS — mais seguros que custom schemes | Alta |
| `apple-app-site-association` deve estar em `/.well-known/` com Content-Type `application/json` | Alta |
| Deferred deep links sobrevivem ao install — usuário abre a tela correta após instalar via link | Alta |
| Custom schemes (`myapp://`) vulneráveis a hijacking — outro app pode registrar o mesmo scheme | Alta |

## Conceitos Abordados

- [[mobile-deep-links]] · [[mobile-navegacao]] · [[mobile-push-notifications]] · [[mobile-seguranca]]
