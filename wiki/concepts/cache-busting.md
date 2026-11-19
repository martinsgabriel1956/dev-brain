---
type: concept
title: "Cache busting"
aliases: ["fingerprinting de assets", "hash no nome do arquivo", "versionamento de assets", "hard refresh"]
date_created: 2026-11-19
date_updated: 2026-11-19
source_count: 1
tags: [cache, http-caching, build, performance, deploy]
skill: tech-mentor-frontend
status: stub
---

# Cache busting

Mudar a URL de um arquivo estático sempre que o conteúdo muda, para o navegador baixar a versão nova sem esperar o cache expirar. Com isso, o arquivo pode ter cache longo e o deploy aparece na hora. Ver [[wiki/concepts/http-caching]].

## Formas

- **Hash no nome** (`app.3f2a1c.js`): o [[wiki/concepts/bundler]] (Vite, Webpack) gera o nome a partir do conteúdo e reescreve o HTML. Permite `Cache-Control: max-age=31536000, immutable`.
- **Versão na query** (`style.css?v=2`): manual, funciona sem build; alguns proxies antigos não cacheiam URLs com query.
- **Versão no caminho** (`/gsap@3.12.2/gsap.min.js`): o padrão das [[wiki/concepts/cdn|CDNs]] de bibliotecas.

O HTML, que aponta para os nomes novos, fica com cache curto ou revalidação (`no-cache`), para o navegador sempre saber qual versão pedir.

## Sem cache busting

Quem atualiza o `style.css` com o mesmo nome depende do usuário fazer hard refresh (Ctrl+Shift+R) ou do cache expirar. Em [[wiki/sources/frontpush-cache-e-cdn-css-js-inline-incorporado-externo]], [[wiki/entities/nasser|Násser]] usa esse sintoma como prova de que o navegador cacheia CSS externo, sem mostrar a solução.

## Key sources

- [[wiki/sources/frontpush-cache-e-cdn-css-js-inline-incorporado-externo]]: FrontPUSH, otimização aula 02: hard refresh depois de subir CSS novo
