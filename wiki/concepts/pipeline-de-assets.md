---
type: concept
title: "Pipeline de Assets (minificação e concatenação)"
aliases: ['asset pipeline', 'minify', 'bundling']
date_created: 2026-10-14
date_updated: 2026-11-17
source_count: 6
tags: [build, minificacao, webpack, performance, historia]
skill: tech-mentor-frontend
status: draft
---

# Pipeline de Assets (minificação e concatenação)

Cadeia que leva fontes legíveis (Sass, CoffeeScript, vários arquivos) a poucos arquivos otimizados: [[wiki/concepts/transpilador|transpilar]] → **concatenar** (menos requisições) → **minificar** (tirar espaços, encurtar nomes). Nasceu como *asset pipeline* do Rails (2009: 2G/3G); no JS: Grunt/Gulp, depois Babel + **Webpack**. [[wiki/concepts/http2]] reduziu a necessidade de concatenar. Ver [[wiki/concepts/gerenciador-de-pacotes]], [[wiki/concepts/pipeline-de-compilacao]].

## Sass em modo compressed (FrontPUSH)

Em [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]], o [[wiki/entities/scout-app]] alterna entre expandido (desenvolvimento) e `compressed` (produção), que "tira os enters, as quebras de linha, os espaços" e deixa o arquivo "bem menor, melhorando o tempo de requisição". O mesmo compilador gera um `.map` (source map) para ligar o CSS ao `.scss`. `[skill: tech-mentor-frontend]` Com bundler, o Sass vira uma etapa do build e a minificação fica com Lightning CSS ou esbuild; o servidor ainda comprime com gzip/brotli.

## Um CSS só (FrontPUSH, Sass aula 03)

Em [[wiki/sources/frontpush-import-e-partials-sass]]: dividir em vários `.scss` e compilar para um só é "a maneira mais otimizada [...] porque tem menos arquivos para carregar"; vincular vários CSS "prejudica a otimização", com "vários requests". É a concatenação desta página. `[skill: tech-mentor-frontend]` Com HTTP/2, o ganho de juntar tudo diminuiu; hoje se divide por página ou rota.

## Na NLW #2, dia 1 (Diego Fernandes)

No `react-scripts`, o Webpack "faz a automatização desse processo" e permite importar SVG e CSS pelo JavaScript (`import logoImg from '.../logo.svg'`, `import './styles.css'`). Ver [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]].

Em [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]], Webpack e Babel aparecem como se fossem novidades do ES6+; são etapas deste pipeline, populares porque a sintaxe nova saiu antes do suporte dos navegadores ([[wiki/concepts/ecmascript]]).

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
- [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]]: Sass `compressed` e `.map`
- [[wiki/sources/frontpush-import-e-partials-sass]]: Sass aula 03: concatenação por `@import`
- [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]: NLW #2, Diego, dia 1: Webpack do CRA: imagem e CSS por import
- [[wiki/sources/frontpush-introducao-javascript-es6-ecmascript]]: FrontPUSH, JavaScript aula 01: Webpack e Babel no ES6+
- [[wiki/sources/frontpush-jsx-webpack-babel-react-createelement-create-react-app]]: FrontPUSH, React aula 06: Webpack importando CSS e imagens no lugar do pipeline
