---
type: concept
title: "Mixin no Sass (@mixin, @include, @content)"
aliases: ["mixin", "@mixin", "@include", "@content", "mixin de responsividade", "mixin de breakpoint"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 7
tags: [css, sass, scss, mixin, reuso, media-query, responsividade]
skill: tech-mentor-frontend
status: stub
---

# Mixin no Sass (@mixin, @include, @content)

Bloco de declarações reaproveitável do [[wiki/concepts/pre-processador-css|Sass]]: `@mixin nome($arg: padrão) { ... }` define, e `@include nome(valor)` despeja o conteúdo no lugar. `@content` marca onde entra o bloco que quem chama passou entre chaves. É o [[wiki/concepts/dry]] do CSS: escrever uma vez, usar em vários seletores e projetos.

## No FrontPUSH

- [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]]: "funções, que são chamadas mixins", para montar bibliotecas.
- [[wiki/sources/frontpush-import-e-partials-sass]]: o arquivo que define o mixin tem de ser importado antes do que o usa.
- [[wiki/sources/frontpush-mixin-e-content-sass]]: a aula dedicada. Mixin de título com argumento padrão (`$cor: #FAFAFA`) e `@content`; um mixin `responsive` com `font-variant: small-caps` fixo e `@content` dentro de `@media (max-width: 960px)`, chamado dentro do próprio `h1`. Depois `responsive-tablet` (960) e `responsive-mobile` (720).

## Mixin × função

`[external]` (https://sass-lang.com/documentation/at-rules/mixin/, https://sass-lang.com/documentation/at-rules/function/)

| | `@mixin` | `@function` |
|---|---|---|
| Uso | `@include` | dentro de um valor: `width: largura(3)` |
| Produz | declarações e regras | um valor, via `@return` |
| Aceita `@content` | sim | não |

O curso chama os dois de "função"; só o mixin foi mostrado.

## Padrão de breakpoint

`[skill: tech-mentor-frontend]`
```scss
@use "sass:map";
$bps: (tablet: 960px, mobile: 720px);
@mixin bp($nome) {
  @media (max-width: map.get($bps, $nome)) { @content; }
}
h1 { font-size: 72px; @include bp(tablet) { font-size: 48px; } @include bp(mobile) { font-size: 36px; } }
```
Um mixin, um mapa de [[wiki/concepts/breakpoint]]s, e a ordem dos includes decide quem vence abaixo de 720 px. Para mobile-first, troca-se por `min-width` ([[wiki/concepts/mobile-first]]).

## Quando o CSS nativo basta

- Media query aninhada dentro do seletor já é CSS nativo ([[wiki/concepts/aninhamento-css]]).
- Tipografia fluida com `clamp()` tira boa parte dos degraus ([[wiki/concepts/escala-tipografica]]).
- Mixins de prefixo perderam o sentido com o Autoprefixer ([[wiki/concepts/prefixo-de-fornecedor]]).
- O que continua exclusivo do Sass: argumentos, `@content` com lógica (`@if`, `@each`) e bibliotecas de mixins.

## Mixins com @if (FrontPUSH, aula 07)

Em [[wiki/sources/frontpush-if-else-sass]], o `@if` dá "mais elasticidade aos mixins": no projeto Nubank, `typeface-1`/`typeface-2` recebem tamanho (`h1`–`h5`) e dispositivo (`desktop`/`mobile`) e escolhem `font-size` e `line-height`; um mixin de layout recebe `xl`/`l`/`m`/`s`/`xs` e aplica a media query com `@content`. Ver [[wiki/concepts/if-else-sass]].

## A diferença dita certo (FrontPUSH, aula 08)

Em [[wiki/sources/frontpush-for-while-each-sass]]: "mixins é uma coisa e funções é outra. A função tem por característica trazer algum tipo de retorno, já o mixin eu posso simplesmente dar um include". Corrige o "funções, que são chamadas mixins" da aula 01. Exemplo de função: `scale-below` com `@while` ([[wiki/concepts/loops-sass]]).

## "Ctrl+C, Ctrl+V" (FrontPUSH, aula 09)

Em [[wiki/sources/frontpush-funcoes-sass]]: mixin "é basicamente um Ctrl+C, Ctrl+V" via `@include`; função "vai te retornar algo, seja um array, seja um valor". Ver [[wiki/concepts/funcoes-sass]].

## responsive($device) (FrontPUSH, aula 10)

Em [[wiki/sources/frontpush-grid-system-sass-parte-1]], o mixin do projeto Nubank recebe um `device` (`xl`/`l`/`m`/`s`/`xs`) e, por `@if`, escolhe a media query; o bloco entra por `@content`. "Um dos recursos que eu mais utilizo."

## Key sources

- [[wiki/sources/frontpush-mixin-e-content-sass]]: sintaxe, `@content`, mixin de responsividade
- [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]]: mixins como base de bibliotecas
- [[wiki/sources/frontpush-import-e-partials-sass]]: importar quem define o mixin antes de quem usa
- [[wiki/sources/frontpush-if-else-sass]]: mixins de tipografia e layout com `@if` (projeto Nubank)
- [[wiki/sources/frontpush-for-while-each-sass]]: mixin × função explicado corretamente
- [[wiki/sources/frontpush-funcoes-sass]]: mixin = Ctrl+C/Ctrl+V; função retorna valor
- [[wiki/sources/frontpush-grid-system-sass-parte-1]]: `responsive($device)` com `@if` e `@content`
