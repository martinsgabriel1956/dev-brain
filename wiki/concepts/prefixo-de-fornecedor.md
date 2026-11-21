---
type: concept
title: "Prefixo de fornecedor (vendor prefix)"
aliases: ["vendor prefix", "prefixos CSS", "-webkit-", "-moz-", "-ms-", "-o-", "Autoprefixer"]
date_created: 2026-11-16
date_updated: 2026-11-20
source_count: 4
tags: [css, compatibilidade, navegador, vendor-prefix, autoprefixer, postcss]
skill: tech-mentor-frontend
status: stub
---

# Prefixo de fornecedor (vendor prefix)

Prefixo que um navegador põe na frente de uma propriedade ainda experimental: `-webkit-` (Safari, Chrome e Opera atuais), `-moz-` (Firefox), `-ms-` (IE e Edge antigo), `-o-` (Opera Presto). Escreve-se a versão com prefixo e depois a padrão: `-webkit-transform: ...; transform: ...;`.

## Na introdução ao Sass do FrontPUSH

Em [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]], [[wiki/entities/nasser|Násser]] abre o Can I use em `transform` ([[wiki/concepts/transition-e-transform-css]]): versões antigas de Firefox, IE e Safari pedem `-moz-`, `-ms-` e `-webkit-`; o suporte sobe de 96% para 98% com prefixo. Digitar todos à mão "fica chato", e no projeto o CSS compilado já sai com `-webkit-` nos `@keyframes`. Ele atribui isso ao Sass.

## Precisões

- `[external]` Quem gera os prefixos é o **Autoprefixer** (plugin do PostCSS), a partir dos dados do Can I use e do alvo em `browserslist`, não o compilador Sass (https://github.com/postcss/autoprefixer). O Live Sass Compiler o roda depois de compilar, pela opção `autoprefix` (https://github.com/glenn2223/vscode-live-sass-compiler).
- `[external]` Os fabricantes abandonaram os prefixos para recursos novos e usam flags; hoje quase tudo funciona sem eles (https://developer.mozilla.org/en-US/docs/Glossary/Vendor_Prefix). Exceções ainda vistas: `-webkit-line-clamp`, `-webkit-background-clip: text`, alguns pseudo-elementos de formulário.
- `[skill: tech-mentor-frontend]` Lightning CSS e os bundlers modernos fazem o mesmo trabalho lendo o `.browserslistrc`. Ver [[wiki/concepts/compatibilidade-entre-navegadores]] e [[wiki/concepts/pre-processador-css]].

## Gerados pela extensão (FrontPUSH, aula 02)

Em [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]], o primeiro Watch Sass do [[wiki/entities/live-sass-compiler]] já gera CSS "com os traços webkit, com o traço ms, para poder melhorar a compatibilidade com browsers antigos", sem configuração: é o Autoprefixer embutido da extensão.

## Mixin de prefixo (FrontPUSH, Sass aula 06)

Em [[wiki/sources/frontpush-mixin-e-content-sass]], "a facilidade de adicionar aqueles prefixos, traço webkit, traço moz" é listada como uso de mixin. Era o padrão antes do Autoprefixer; hoje fica com a ferramenta.

## WebKit automático no transform (FrontPUSH, básico CSS aula 01)

Em [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]], [[wiki/entities/nasser|Násser]] usa Sass "porque ele adiciona o WebKit nos meus comandos de forma automática". Quem adiciona é o Autoprefixer da extensão ([[wiki/entities/live-sass-compiler]]); para `transform`, o prefixo é desnecessário há anos.

## Key sources

- [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]]: Can I use com `transform`; `-webkit-` gerado no CSS compilado
- [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]]: `-webkit-` e `-ms-` gerados pelo Live Sass Compiler
- [[wiki/sources/frontpush-mixin-e-content-sass]]: mixin para prefixos (prática antiga)
- [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 01: "o Sass adiciona o WebKit"; prefixo de transform já desnecessário
