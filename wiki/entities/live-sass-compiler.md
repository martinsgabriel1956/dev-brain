---
type: entity
title: "Live Sass Compiler (extensão do VS Code)"
aliases: ["Live Sass Compiler", "Watch Sass", "glenn2223.live-sass", "ritwickdey.live-sass"]
date_created: 2026-11-16
date_updated: 2026-11-21
source_count: 6
tags: [ferramenta, vs-code, extensao, sass, scss, compilador]
skill: tech-mentor-frontend
status: stub
---

# Live Sass Compiler

Extensão do [[wiki/entities/vs-code]] que compila `.scss`/`.sass` para CSS ao salvar. Liga-se pelo botão "Watch Sass" na barra de status. É como o [[wiki/entities/frontpush]] compila o [[wiki/concepts/pre-processador-css|Sass]].

## No FrontPUSH

- Citada na aula de ambiente como extensão do curso ([[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]).
- Na [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss|introdução ao Sass]], o CSS gerado sai com `-webkit-` nos `@keyframes`.
- Na [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app|aula de instalação]], [[wiki/entities/nasser|Násser]] diz que "não consigo viver sem". O Watch Sass gera `style.css` e `style.css.map`, já com `-webkit-` e `-ms-`, e avisa erros. O "Open with Live Server", porta 5500, que ele atribui à mesma extensão, vem do Live Server, dependência da versão original. Para alunos em que ela não rodou, a alternativa é o [[wiki/entities/scout-app]].

## Situação

- `[external]` A versão de Ritwick Dey foi arquivada em 10/03/2022 e aponta para o fork mantido por Glenn Marks (`glenn2223.live-sass`) (https://github.com/ritwickdey/vscode-live-sass-compiler, https://github.com/glenn2223/vscode-live-sass-compiler).
- O prefixo automático vem do Autoprefixer embutido, configurável em `liveSassCompile.settings.autoprefix` ([[wiki/concepts/prefixo-de-fornecedor]]). Confiança média sobre o padrão.

## Partials na prática

Em [[wiki/sources/frontpush-import-e-partials-sass]], o Watch Sass gerou `colors.css` e `colors.css.map` para o arquivo de cores até ele virar `_colors.scss`: partials não viram CSS próprio.

## O "plugin" da aula de transform (FrontPUSH)

Em [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]], o Sass entra "porque ele adiciona o WebKit nos meus comandos de forma automática", por "um plugin que eu instalo aqui no VS Code": esta extensão e seu Autoprefixer.

## Aula de SVG (FrontPUSH, propriedades SVG aula 02)

Em [[wiki/sources/frontpush-como-usar-svg-img-background-object-inline]]: "eu aperto para poder rodar o sass, ele compila" o `style.scss`, com WebKit inserido: o botão e o autoprefixer da extensão, como nas aulas de transform.

## Key sources

- [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]: citada na aula de ambiente
- [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]]: CSS gerado com `-webkit-`
- [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]]: instalação, Watch Sass, `.map`, prefixos
- [[wiki/sources/frontpush-import-e-partials-sass]]: gera CSS para todo `.scss` que não é partial
- [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 01: Autoprefixer como motivo para usar Sass
- [[wiki/sources/frontpush-como-usar-svg-img-background-object-inline]]: FrontPUSH, mini curso de CSS Animations, propriedades SVG aula 02: compila o style.scss da aula de SVG
