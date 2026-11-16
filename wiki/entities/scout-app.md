---
type: entity
title: "Scout-App"
aliases: ["Scout App", "ScoutApp"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [ferramenta, sass, compilador, gui, open-source]
skill: tech-mentor-frontend
status: stub
---

# Scout-App

Aplicativo gráfico, gratuito e open source, para compilar Sass no Windows, Linux e Mac: escolhe-se uma pasta de entrada, uma de saída e o estilo (expandido ou `compressed`), e o play inicia o modo watch.

Na [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app|aula de instalação do Sass]] do [[wiki/entities/frontpush]], [[wiki/entities/nasser|Násser]] o ensina como plano B para quem não conseguiu rodar o [[wiki/entities/live-sass-compiler]]. Escolheu-o entre os aplicativos do site do Sass por ser "free e multiplataforma"; o Prepros funciona sem pagar, mas com pop-up de cobrança.

## Situação

`[external]` Parado: último commit em 21/06/2021; usa `node-sass` 4.x (LibSass, descontinuado), sem suporte a `@use` e aos módulos do Sass moderno (https://github.com/scout-app/scout-app). Já não aparece na página de instalação do Sass, que lista só CodeKit e Prepros (https://sass-lang.com/install/). Para projeto novo, a CLI do Dart Sass (`sass --watch`) é a alternativa multiplataforma. Ver [[wiki/concepts/pre-processador-css]].

## Key sources

- [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]]: alternativa à extensão do VS Code; modos expandido e compressed
