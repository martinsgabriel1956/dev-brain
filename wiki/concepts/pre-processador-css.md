---
type: concept
title: "Pré-processador CSS (Sass)"
aliases: ["Sass", "SCSS", "pré-processador", "preprocessor CSS", "Live Sass Compiler"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 3
tags: [css, sass, scss, pre-processador, frontend, build]
skill: tech-mentor-frontend
status: stub
---

# Pré-processador CSS (Sass)

Linguagem que compila para [[wiki/concepts/css]] e acrescenta recursos de programação. Para [[wiki/entities/nasser|Násser]], o CSS "é uma linguagem de estilo, [...] de layout" sem "recursos de otimização voltados à programação"; o Sass "adiciona propriedades de programação [...] dentro do nosso CSS" sem mudar nada no CSS, que continua sendo escrito do mesmo jeito. O exemplo dele é uma condicional `if/else`, "não consigo fazer isso" no CSS nativo. No [[wiki/entities/vs-code]], a extensão Live Sass Compiler compila os arquivos; o detalhe fica para a aula de Sass do [[wiki/entities/frontpush]] ([[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]).

## O que o CSS já faz sozinho

`[skill: tech-mentor-frontend]` Boa parte do que justificava o Sass virou CSS nativo: aninhamento (nesting, Chrome 112+, Firefox 117+, Safari 16.5+), [[wiki/concepts/variaveis-css|variáveis]] (custom properties, que mudam em tempo de execução, ao contrário das `$variáveis` do Sass) e `if()`, que apareceu primeiro no Chromium e ainda está em adoção. O Sass continua comum em projetos legados e com ITCSS + BEM, onde mixins e funções organizam a camada Tools. Ver [[wiki/concepts/compatibilidade-entre-navegadores]].

## Key sources

- [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]: Sass como pré-processador, `if/else`, Live Sass Compiler
- [[wiki/sources/frontpush-layout-css-botao-hover-flexbox-media-query]]: "Grid System com Sass, utilizando float" citado como forma de layout, com módulo próprio no curso
- [[wiki/sources/frontpush-conclusao-modulo-css-estilo-layout-animacao-documentacao]]: grid system com float em Sass, "seguindo o grid que a gente desenha no Figma"
