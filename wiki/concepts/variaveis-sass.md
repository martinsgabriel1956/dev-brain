---
type: concept
title: "Variáveis no Sass ($variável)"
aliases: ["variáveis Sass", "variáveis SCSS", "$variável", "!default", "Sass variables"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 5
tags: [css, sass, scss, variaveis, design-tokens]
skill: tech-mentor-frontend
status: stub
---

# Variáveis no Sass ($variável)

`$nome: valor;`, usada depois como `color: $nome;`. Resolvida na compilação: o CSS gerado só tem o valor. Guarda cores, medidas, fontes e propriedades inteiras, como um `box-shadow` de várias camadas. É a forma mais simples de levar os [[wiki/concepts/design-tokens]] de um [[wiki/concepts/style-guide]] para o código. Ver [[wiki/concepts/pre-processador-css]].

## No FrontPUSH

- [[wiki/sources/frontpush-import-e-partials-sass]]: variáveis de cor (`branco`, `cinza`, `preto`) num `_colors.scss` importado no topo.
- [[wiki/sources/frontpush-variaveis-sass]]: a aula dedicada. "Um dólar, como se fosse em PHP"; consistência como motivo (a mesma cor do style guide em todo lugar, sem matizes trocadas por descuido); uma variável `box-shadow purple` com a sombra do Smooth Shadow, aplicada no `:hover` e trocada num lugar só.

## Regras que a aula não cobre

`[external]` (https://sass-lang.com/documentation/variables/)
- **Escopo:** declarada dentro de um bloco, é local; `!global` força a global (desaconselhado).
- **`!default`:** só atribui se a variável ainda não existir. É o mecanismo de bibliotecas configuráveis: `@use "lib" with ($primaria: purple)`.
- **Hífen = underline** nos nomes: `$box-shadow` e `$box_shadow` são a mesma variável.
- **Valores são expressões:** `$base: 8px; $gap: $base * 3;`; listas e mapas (`$cores: (primaria: #8A05BE)`) com `map.get`.
- Com `@use`, as variáveis ganham namespace: `colors.$branco` ([[wiki/concepts/import-e-partials-sass]]).

## Sass × custom properties

| | `$variável` (Sass) | `--variavel` (CSS) |
|---|---|---|
| Existe em | compilação | navegador |
| Muda em tempo de execução / por tema | não | sim (`.dark { --cor: ... }`) |
| Herda na cascata | não | sim |
| Contas e mapas | sim | só `calc()` |

`[skill: tech-mentor-frontend]` Combinação usual: Sass (ou JSON de tokens) gera as custom properties em `:root`, e o código usa `var(--...)`. Ver [[wiki/concepts/variaveis-css]].

## Argumentos de mixin (FrontPUSH, aula 06)

Em [[wiki/sources/frontpush-mixin-e-content-sass]], `$cor: #FAFAFA` no parâmetro do mixin funciona como variável local com valor padrão; `@include nome_mixin(#FFF)` sobrescreve.

## Escopo dentro do @if (FrontPUSH, aula 07)

Em [[wiki/sources/frontpush-if-else-sass]], `$bg-color` declarada só dentro do `@if` deu "undefined variable" fora dele. Declarar o padrão antes resolve: a atribuição no bloco passa a alterar a variável de fora.

## Listas, mapas e interpolação (FrontPUSH, aula 08)

Em [[wiki/sources/frontpush-for-while-each-sass]]: `$sizes: 40px, 50px, 80px` (lista) e `$icons: ("eye": "\f112", ...)` (mapa) percorridos com `@each`; `#{$i}` para pôr o valor de uma variável num seletor, porque `$i` sozinho sai literal.

## Key sources

- [[wiki/sources/frontpush-variaveis-sass]]: aula de variáveis; consistência; sombra numa variável
- [[wiki/sources/frontpush-import-e-partials-sass]]: arquivo de cores importado
- [[wiki/sources/frontpush-mixin-e-content-sass]]: argumento de mixin com valor padrão
- [[wiki/sources/frontpush-if-else-sass]]: escopo de variável em `@if`
- [[wiki/sources/frontpush-for-while-each-sass]]: listas, mapas e `#{}`
