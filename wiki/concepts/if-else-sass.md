---
type: concept
title: "@if e @else no Sass (controle de fluxo)"
aliases: ["@if", "@else", "@else if", "if else Sass", "controle de fluxo Sass", "operadores Sass"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [css, sass, scss, if-else, controle-de-fluxo, mixin]
skill: tech-mentor-frontend
status: stub
---

# @if e @else no Sass (controle de fluxo)

Regras do [[wiki/concepts/pre-processador-css|Sass]] que escolhem o que entra no CSS, conforme valores conhecidos **na compilação**: `@if cond { } @else if cond { } @else { }`. Junto com `@each`, `@for` e `@while`, formam o controle de fluxo. O uso típico é dentro de [[wiki/concepts/mixin-sass|mixins]], para que um parâmetro mude o resultado. É a [[wiki/concepts/logica-de-programacao]] de sempre, aplicada ao CSS.

## No FrontPUSH

[[wiki/sources/frontpush-if-else-sass]]:
- `$layout: dark | light` decide `$bg-color` e `$text-color`. O "undefined variable" some quando as variáveis são declaradas antes, fora do `@if`.
- No projeto Nubank: mixins de tipografia com tamanho (`h1`–`h5`) e dispositivo (`desktop`/`mobile`), e um mixin de layout com breakpoints `xl`/`l`/`m`/`s`/`xs`, ambos com `@if` em cadeia.

## Regras

`[external]` (https://sass-lang.com/documentation/at-rules/control/if/, https://sass-lang.com/documentation/operators/)
- **Verdadeiro/falso:** só `false` e `null` são falsos; `0`, `""` e `()` são verdadeiros.
- **Operadores:** `==` e `!=`; `and`, `or` e `not`; `<`, `>`, `<=` e `>=` para números. `light` e `"light"` são iguais.
- **Escopo:** variável criada pela primeira vez dentro do `@if` é local ao bloco; se já existia fora, a atribuição a altera ([[wiki/concepts/variaveis-sass]]).
- **`@else if`** com espaço (`@elseif` é sintaxe antiga, deprecada).
- **`if($cond, $a, $b)`** é a função ternária para valores curtos.

## Limites

- Roda na compilação: não reage a clique, tela ou preferência do usuário. Para tema que troca em tempo de execução, use custom properties com `[data-theme]` ou `prefers-color-scheme` ([[wiki/concepts/variaveis-css]]).
- `[skill: tech-mentor-frontend]` Uma cadeia longa de `@if` por chave (tamanho × dispositivo) costuma ficar melhor como mapa + `map.get`, que é o formato dos [[wiki/concepts/design-tokens]].
- `[skill: tech-mentor-frontend]` O CSS nativo ganhou `if()` (Chromium primeiro, ainda em adoção), avaliado no navegador. Ver [[wiki/concepts/pre-processador-css]].

## Irmãos: os loops (FrontPUSH, aula 08)

Em [[wiki/sources/frontpush-for-while-each-sass]], `@for`, `@while` e `@each` completam o controle de fluxo; o `@while` é "meio que um if encadeado". Ver [[wiki/concepts/loops-sass]].

## Key sources

- [[wiki/sources/frontpush-if-else-sass]]: tema light/dark; mixins de tipografia e layout do projeto Nubank
- [[wiki/sources/frontpush-for-while-each-sass]]: `@while` como "if encadeado"
