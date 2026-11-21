---
type: concept
title: "Pré-processador CSS (Sass)"
aliases: ["Sass", "SCSS", "pré-processador", "preprocessor CSS", "Live Sass Compiler", "mixin", "Less", "Dart Sass"]
date_created: 2026-11-16
date_updated: 2026-11-21
source_count: 16
tags: [css, sass, scss, pre-processador, frontend, build]
skill: tech-mentor-frontend
status: draft
---

# Pré-processador CSS (Sass)

Linguagem que compila para [[wiki/concepts/css]] e acrescenta recursos de programação. Para [[wiki/entities/nasser|Násser]], o CSS "é uma linguagem de estilo, [...] de layout" sem "recursos de otimização voltados à programação"; o Sass "adiciona propriedades de programação [...] dentro do nosso CSS" sem mudar nada no CSS, que continua sendo escrito do mesmo jeito. O exemplo dele é uma condicional `if/else`, "não consigo fazer isso" no CSS nativo. No [[wiki/entities/vs-code]], a extensão Live Sass Compiler compila os arquivos; o detalhe fica para a aula de Sass do [[wiki/entities/frontpush]] ([[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]).

## O que o CSS já faz sozinho

`[skill: tech-mentor-frontend]` Boa parte do que justificava o Sass virou CSS nativo: aninhamento (nesting, Chrome 112+, Firefox 117+, Safari 16.5+), [[wiki/concepts/variaveis-css|variáveis]] (custom properties, que mudam em tempo de execução, ao contrário das `$variáveis` do Sass) e `if()`, que apareceu primeiro no Chromium e ainda está em adoção. O Sass continua comum em projetos legados e com ITCSS + BEM, onde mixins e funções organizam a camada Tools. Ver [[wiki/concepts/compatibilidade-entre-navegadores]].

## Introdução do módulo de Sass

Em [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]], [[wiki/entities/nasser|Násser]] abre o módulo: o Sass "não é lido pelo browser", é "um meio de campo" que "cospe" CSS; não faz "algo além do que o CSS já é capaz de fazer", só aumenta a produtividade. Vantagens do slide: funções (que ele chama de mixins) para bibliotecas reaproveitáveis, variáveis com valores inteiros (um `box-shadow` de várias camadas), facilidades com pseudo-elementos e estados, e prefixos automáticos ([[wiki/concepts/prefixo-de-fornecedor]]). Escolhe o Sass, e não o Less, pela comunidade maior.

**Sass vs SCSS.** A sintaxe indentada (`.sass`, sem chaves nem ponto e vírgula, "próximo da linguagem Python") é "prejudicial" porque afasta do CSS puro: "a tecnologia é maior que a ferramenta" ([[wiki/concepts/apego-a-ferramentas]]). O curso escreve SCSS (`.scss`), "muitíssimo parecido com o CSS puro", com [[wiki/concepts/aninhamento-css|aninhamento]]. `[external]` SCSS é superconjunto do CSS: todo CSS válido é SCSS válido (https://sass-lang.com/documentation/syntax/).

**Precisões.** `[external]` `@mixin`/`@include` despejam declarações; `@function`/`@return` devolvem valor; a aula mistura os dois. O compilador não põe prefixos: é o Autoprefixer, que o Live Sass Compiler roda pela opção `autoprefix`. O LibSass foi descontinuado em 2020; a implementação atual é o Dart Sass (https://sass-lang.com/blog/libsass-is-deprecated/).

## Instalação: extensão, app ou CLI (FrontPUSH)

Em [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]], duas formas: a extensão [[wiki/entities/live-sass-compiler]] no [[wiki/entities/vs-code]] (a do curso, botão "Watch Sass") e o [[wiki/entities/scout-app]], gráfico e multiplataforma. A linha de comando ficou de fora por pedir mais conhecimento de terminal. `[external]` Hoje a CLI do Dart Sass (`npm install -D sass`, `sass --watch scss:css --style=compressed`) é o caminho portátil; o Scout-App e a extensão original usavam LibSass, descontinuado.

## @import e partials (FrontPUSH, aula 03)

Em [[wiki/sources/frontpush-import-e-partials-sass]], primeiro "fundamento do Sass": `@import` para juntar arquivos por categoria num CSS só, e partials (`_colors.scss`) para não gerar um CSS por arquivo. `[external]` `@import` está deprecado desde o Dart Sass 1.80; o substituto é `@use`/`@forward`. Ver [[wiki/concepts/import-e-partials-sass]].

## Variáveis (FrontPUSH, aula 04)

Em [[wiki/sources/frontpush-variaveis-sass]]: `$nome: valor`, "como se fosse em PHP", para cores, tipografia e propriedades inteiras, em nome da consistência do style guide. Ver [[wiki/concepts/variaveis-sass]].

## Nesting (FrontPUSH, aula 05)

Em [[wiki/sources/frontpush-nesting-aninhamento-sass]]: aninhamento de tags, `&` para colar (`:hover`, `.active`, `::before`) e aninhamento de propriedades. Ver [[wiki/concepts/aninhamento-css]].

## @mixin e @content (FrontPUSH, aula 06)

Em [[wiki/sources/frontpush-mixin-e-content-sass]]: mixin como "função" com argumento padrão e `@content`; aplicação principal é um mixin de responsividade chamado dentro do próprio seletor. Ver [[wiki/concepts/mixin-sass]].

## @if e @else (FrontPUSH, aula 07)

Em [[wiki/sources/frontpush-if-else-sass]]: estruturas condicionais na compilação, para tema light/dark por variável e para os mixins de tipografia e layout do projeto Nubank. Ver [[wiki/concepts/if-else-sass]].

## @for, @while e @each (FrontPUSH, aula 08)

Em [[wiki/sources/frontpush-for-while-each-sass]]: loops para gerar classes (`.grid-1`…`.grid-12`), interpolação `#{}` e a distinção, agora dita certo, entre `@function` (retorna valor) e `@mixin` (inclui código). Ver [[wiki/concepts/loops-sass]].

## @function e @return (FrontPUSH, aula 09)

Em [[wiki/sources/frontpush-funcoes-sass]]: funções que devolvem valor (`grid($col, $total: 12)` em %), funções de cor prontas e operadores. Ver [[wiki/concepts/funcoes-sass]].

## Sass como otimização (FrontPUSH, otimização aula 01)

Em [[wiki/sources/frontpush-introducao-otimizacao-web-minificacao-css-js]]: "a gente já estava fazendo otimização de CSS desde o começo, e vocês não percebiam". O Sass deixa escrever com espaços e partials (acordeon, animações, botões, tipografia, layout) e "cospe" um CSS único. A minificação na aula é feita num site externo, embora o modo `compressed` do Sass já faça isso.

## Sass na otimização de imagens (FrontPUSH, otimização aula 04)

Em [[wiki/sources/frontpush-otimizacao-de-imagens-mobile-desktop-classes-mixin]], o mixin `responsive` das aulas de Sass vira ferramenta de otimização: classes de visibilidade e imagem por breakpoint. Ver [[wiki/concepts/mixin-sass]].

## Sass só pelos prefixos (FrontPUSH, básico CSS aula 01)

Em [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]]: "eu estou utilizando apenas CSS, o Sass eu estou utilizando porque ele adiciona o WebKit". Os prefixos vêm do Autoprefixer da extensão, não do Sass ([[wiki/concepts/prefixo-de-fornecedor]]).

## "Inserção de WebKit" de novo (FrontPUSH, propriedades SVG aula 02)

Em [[wiki/sources/frontpush-como-usar-svg-img-background-object-inline]]: Sass "é um pré-processador só para poder a gente dar um boost no nosso alcance, com relação à compatibilidade dos comandos"; compila um CSS "mais otimizado com relação à inserção de WebKit [...] mais performático". Mesma confusão da básico CSS aula 01: o prefixo é do Autoprefixer da extensão, e prefixo não acelera nada.

## Key sources

- [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]: Sass como pré-processador, `if/else`, Live Sass Compiler
- [[wiki/sources/frontpush-layout-css-botao-hover-flexbox-media-query]]: "Grid System com Sass, utilizando float" citado como forma de layout, com módulo próprio no curso
- [[wiki/sources/frontpush-conclusao-modulo-css-estilo-layout-animacao-documentacao]]: grid system com float em Sass, "seguindo o grid que a gente desenha no Figma"
- [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]]: aula 01 do módulo de Sass: o que é, vantagens, prefixos, Sass vs SCSS
- [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]]: aula 02 do módulo de Sass: Live Sass Compiler, Scout-App, `compressed`
- [[wiki/sources/frontpush-import-e-partials-sass]]: aula 03: `@import`, ordem e partials
- [[wiki/sources/frontpush-variaveis-sass]]: aula 04: variáveis
- [[wiki/sources/frontpush-nesting-aninhamento-sass]]: aula 05: nesting
- [[wiki/sources/frontpush-mixin-e-content-sass]]: aula 06: @mixin e @content
- [[wiki/sources/frontpush-if-else-sass]]: aula 07: @if/@else
- [[wiki/sources/frontpush-for-while-each-sass]]: aula 08: loops e interpolação
- [[wiki/sources/frontpush-funcoes-sass]]: aula 09: funções
- [[wiki/sources/frontpush-introducao-otimizacao-web-minificacao-css-js]]: FrontPUSH, otimização aula 01: partials e CSS único como otimização
- [[wiki/sources/frontpush-otimizacao-de-imagens-mobile-desktop-classes-mixin]]: FrontPUSH, otimização aula 04: mixin `responsive` reaproveitado
- [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 01: Sass usado só pelos prefixos
- [[wiki/sources/frontpush-como-usar-svg-img-background-object-inline]]: FrontPUSH, mini curso de CSS Animations, propriedades SVG aula 02: Sass = WebKit, de novo
