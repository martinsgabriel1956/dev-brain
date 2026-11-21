---
type: entity
title: "Can I Use"
aliases: ["caniuse", "caniuse.com"]
date_created: 2026-11-19
date_updated: 2026-11-21
source_count: 2
tags: [ferramenta, compatibilidade, navegadores, html, css, javascript]
skill: tech-mentor-frontend
status: stub
---

# Can I Use

Site (caniuse.com) com tabelas de suporte de recursos de HTML, CSS e JavaScript por navegador e versão, com a porcentagem de uso global. É a consulta padrão antes de usar algo novo; os dados também alimentam o `browserslist`, que diz ao build quais navegadores atender ([[wiki/concepts/compatibilidade-entre-navegadores]]). O selo Baseline (web.dev, MDN) resume a mesma informação em "disponível em todos os navegadores principais" ou não.

## No FrontPUSH

Em [[wiki/sources/frontpush-otimizacao-de-imagens-svg-webp-lazy-loading]], [[wiki/entities/nasser|Násser]] busca "lazy" e mostra "Loading via attribute for images and iframes" para conferir o `loading="lazy"` ([[wiki/concepts/lazy-vs-eager-loading]]).

## Suporte ao SVG (FrontPUSH, propriedades SVG aula 02)

Em [[wiki/sources/frontpush-como-usar-svg-img-background-object-inline]]: "uma coisa que eu esqueci [...] de falar na primeira aula": o SVG é "compatível com a grande maioria de browsers"; fora o Android browser antigo e o Internet Explorer 6 a 8, com 0% e 0,09% de uso. `[external]` O IE 9 já tinha suporte básico; o Android sem SVG era o 2.x.

## Key sources

- [[wiki/sources/frontpush-otimizacao-de-imagens-svg-webp-lazy-loading]]: FrontPUSH, otimização aula 03: suporte do `loading="lazy"`
- [[wiki/sources/frontpush-como-usar-svg-img-background-object-inline]]: FrontPUSH, mini curso de CSS Animations, propriedades SVG aula 02: suporte ao SVG; IE 6–8 e Android antigo
