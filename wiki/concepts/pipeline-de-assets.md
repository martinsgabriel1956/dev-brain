---
type: concept
title: "Pipeline de Assets (minificação e concatenação)"
aliases: ['asset pipeline', 'minify', 'bundling']
date_created: 2026-10-14
date_updated: 2026-11-16
source_count: 2
tags: [build, minificacao, webpack, performance, historia]
skill: tech-mentor-frontend
status: draft
---

# Pipeline de Assets (minificação e concatenação)

Cadeia que leva fontes legíveis (Sass, CoffeeScript, vários arquivos) a poucos arquivos otimizados: [[wiki/concepts/transpilador|transpilar]] → **concatenar** (menos requisições) → **minificar** (tirar espaços, encurtar nomes). Nasceu como *asset pipeline* do Rails (2009: 2G/3G); no JS: Grunt/Gulp, depois Babel + **Webpack**. [[wiki/concepts/http2]] reduziu a necessidade de concatenar. Ver [[wiki/concepts/gerenciador-de-pacotes]], [[wiki/concepts/pipeline-de-compilacao]].

## Sass em modo compressed (FrontPUSH)

Em [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]], o [[wiki/entities/scout-app]] alterna entre expandido (desenvolvimento) e `compressed` (produção), que "tira os enters, as quebras de linha, os espaços" e deixa o arquivo "bem menor, melhorando o tempo de requisição". O mesmo compilador gera um `.map` (source map) para ligar o CSS ao `.scss`. `[skill: tech-mentor-frontend]` Com bundler, o Sass vira uma etapa do build e a minificação fica com Lightning CSS ou esbuild; o servidor ainda comprime com gzip/brotli.

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
- [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]]: Sass `compressed` e `.map`
