---
type: concept
title: "Pipeline de Assets (minificação e concatenação)"
aliases: ['asset pipeline', 'minify', 'bundling']
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [build, minificacao, webpack, performance, historia]
skill: tech-mentor-frontend
status: draft
---

# Pipeline de Assets (minificação e concatenação)

Cadeia que leva fontes legíveis (Sass, CoffeeScript, vários arquivos) a poucos arquivos otimizados: [[wiki/concepts/transpilador|transpilar]] → **concatenar** (menos requisições) → **minificar** (tirar espaços, encurtar nomes). Nasceu como *asset pipeline* do Rails (2009: 2G/3G); no JS: Grunt/Gulp, depois Babel + **Webpack**. [[wiki/concepts/http2]] reduziu a necessidade de concatenar. Ver [[wiki/concepts/gerenciador-de-pacotes]], [[wiki/concepts/pipeline-de-compilacao]].

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
