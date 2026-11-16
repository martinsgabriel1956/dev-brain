---
type: source
title: "Estruturas de repetição no Sass: @for, @while e @each (FrontPUSH)"
aliases: ["Estruturas de repetição @for, @while e @each", "loops Sass FrontPUSH", "módulo de CSS Sass, aula 08", "interpolação Sass"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, sass, scss, for, while, each, interpolacao, function, grid, grid-de-colunas, icones, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-for-while-each-sass.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Estruturas de repetição no Sass: @for, @while e @each (FrontPUSH)

## TL;DR

Aula 08 do módulo de CSS Sass do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]] ("Ah, Násser, o que significa essa estrutura de grid?"). Assunto: [[wiki/concepts/loops-sass]].

- **`@for $i from 1 through 12`** soma de 1 em 1. Para pôr o valor no seletor, `#{$i}` (interpolação, "o mesmo artifício [...] no JavaScript"); sem ela, sai `grid-$i`. Slide: `.grid-#{$i} { width: 72px * $i; }` → `.grid-1 { width: 72px }`, `.grid-2 { width: 144px }`.
- **Por quê:** um sistema de classes de [[wiki/concepts/grid-de-colunas]] (12 colunas de 96 px, gutter 24) é "bem mais fiel ao layout projetado" que estimar `flex-grow` "no olho". 2 colunas = 216 px; 5 = 576; 7 = 816. Escrever `.grid1`…`.grid12` à mão é o que o loop evita. O sistema completo fica para as aulas práticas.
- **Documentação:** "indico vocês demais a sempre estarem verificando a documentação" (At-Rules → Flow Control). Exemplos lidos de lá: `@for` com `nth-child(3n + #{$i})` e `lighten()`; `@while` numa `@function scale-below`; `@each` numa lista de tamanhos e num mapa de ícones.
- **Mixin × função**, agora explicado certo: "a função tem por característica trazer algum tipo de retorno, já o mixin eu posso simplesmente dar um include" ([[wiki/concepts/mixin-sass]]).
- **Resumo dele:** `@for` sequencial com início e fim; `@each` percorre "um vetor sem precisar você estabelecer nada"; `@while` repete "enquanto algo estiver diferente de outro".

## Key Claims

### @for e interpolação

- "Se você já estudou alguma linguagem de programação, seja ela C, seja ela JavaScript, seja ela PHP, você já se deparou com essas estruturas" ([[wiki/concepts/logica-de-programacao]]).
- "Aqui, literalmente, a gente vai ver que ele modifica de 1 em 1"; `$i`, `$j`, `$k` vêm de "índices de matrizes"; `through` = "de um lado até o outro".
- "Se eu simplesmente colocar $i, como ele não está estabelecido dentro de uma propriedade, ele vai meio que reproduzir grid-$i [...] para forçar que o Sass entenda que eu quero que ele me mostre o valor da variável i naquele momento do loop [...] eu coloco ele entre chaves e uma hashtag."
- Na demo: `@for $i from 1 through 12 { .grid-#{$i} { width: 96px * $i; } }`, "sem considerar o gutter", que fica para a aula prática. "Nada impede de você, por exemplo, começar do 5."

### Sistema de grids

- "Os grids são de suma importância para poder a gente alinhar os nossos elementos e distribuir o conteúdo, e até facilitar na responsividade."
- Com [[wiki/concepts/flexbox]]: "a gente precisa estar utilizando o flex grow, e aí a gente vai verificando no olho [...] não é uma divisão muito exata" ([[wiki/concepts/flex-grow-shrink-basis]]).
- "Um grid tem o tamanho de 96 pixels [...] 96 mais 96, porém tem o gutter [...] 216 pixels." "Eu preciso fazer isso de 1 até 12, porque é o padrão que eu utilizo, são 12 colunas."

### @while e @function

- "Mixins é uma coisa e funções é outra. A função tem por característica trazer algum tipo de retorno, já o mixin eu posso simplesmente dar um include e ele vai puxar todo o código do que eu escrevi para outro lugar."
- `scale-below($value, $base, $ratio: 1.618)`: "enquanto o valor que você está me passando nesse parâmetro for maior que a base [...] divida a value pelo ratio e retorne value". Calculadora: 10 com base 12 → 10; 16 com base 12 → 16 / 1.618; no exemplo, `scale-below(20px, 16px)` → 12.36 ([[wiki/concepts/escala-tipografica]]).
- "O for [...] é mais sequencial, já do while ele te traz mais algumas possibilidades, porque tem como você comparar [...] meio que um if encadeado aí dentro" ([[wiki/concepts/if-else-sass]]).

### @each

- "Ele é mais utilizado para quando você está [...] querendo percorrer dentro de um array. O que é um array? Literalmente é um vetor com vários valores dentro" ([[wiki/concepts/array]]).
- `$sizes: 40px, 50px, 80px; @each $size in $sizes { .icon-#{$size} { font-size; height; width } }` → `.icon-40px`, `.icon-50px`, `.icon-80px`.
- Mapa de ícones: `$icons: ("eye": "\f112", "start": "\f12e", "stop": "\f12f")` e `@each $name, $glyph in $icons { .icon-#{$name}:before { font-family: ...; content: $glyph; } }`: "name é o nome do ícone, glyph é o código do ícone" ([[wiki/concepts/icones-em-interfaces]]).

## Entities

- [[wiki/entities/nasser]]: instrutor (diz o nome).
- [[wiki/entities/frontpush]]: curso; aula 08 do módulo de CSS Sass.
- [[wiki/entities/nubank]]: layout de exemplo do grid de colunas.

## Concepts

- [[wiki/concepts/loops-sass]]
- [[wiki/concepts/mixin-sass]]
- [[wiki/concepts/funcoes-sass]]
- [[wiki/concepts/if-else-sass]]
- [[wiki/concepts/variaveis-sass]]
- [[wiki/concepts/grid-de-colunas]]
- [[wiki/concepts/grid-system]]
- [[wiki/concepts/css-grid]]
- [[wiki/concepts/flexbox]]
- [[wiki/concepts/flex-grow-shrink-basis]]
- [[wiki/concepts/array]]
- [[wiki/concepts/logica-de-programacao]]
- [[wiki/concepts/escala-tipografica]]
- [[wiki/concepts/icones-em-interfaces]]
- [[wiki/concepts/pre-processador-css]]

## Precisões e tensões com a wiki

- **O `@while` divide até ficar abaixo da base, não uma vez só.** `[external]` O comentário da documentação diz: "Divides `$value` by `$ratio` until it's below `$base`" (https://sass-lang.com/documentation/at-rules/control/while/). Com 20 e 16 basta uma divisão (12.36). Com 50 e 16 seriam três: 50 → 30.9 → 19.1 → 11.8. A explicação dele ("divida a value pelo ratio e retorne") só cobre o caso de uma volta.
- **`through` × `to`.** `[external]` `from 1 through 12` inclui o 12; `from 1 to 12` para no 11 (https://sass-lang.com/documentation/at-rules/control/for/).
- **Funções globais deprecadas.** `[external]` O exemplo da documentação que ele mostra usa `lighten()`, e o do `@while` usa `/`. No Dart Sass atual, as funções globais estão deprecadas em favor dos módulos (`color.adjust($c, $lightness: 5%)` ou `color.scale`), e a divisão com `/` virou `math.div()` (https://sass-lang.com/documentation/breaking-changes/slash-div/). Prefira os módulos (`@use "sass:math"`, `@use "sass:color"`).
- **A conta do grid sem gutter.** `width: 96px * $i` só serve para mostrar o loop. A conta certa é `$i * 96px + ($i - 1) * 24px` (1 → 96, 2 → 216, 5 → 576, 7 → 816, 12 → 1416). Bate com o grid 12 × 96 + 24 de [[wiki/concepts/grid-de-colunas]] e da [[wiki/sources/frontpush-flexbox-pratica-1-layout-youtube-estrutura-html|prática 1 de Flexbox]].
- **Classes `.grid-N` × CSS Grid.** `[skill: tech-mentor-frontend]` Gerar `.grid-1`…`.grid-12` com largura fixa em px é o modelo dos frameworks de 2010 (960.gs, Bootstrap 2/3). Hoje o [[wiki/concepts/css-grid]] faz isso nativamente: `grid-template-columns: repeat(12, 1fr)` no container, `gap: 24px` e `grid-column: span 5` no item, fluido e sem conta de gutter. O loop continua útil para gerar utilitários (`.col-span-#{$i}`).
- **72 × 96.** O slide usa colunas de 72 px; a demo, de 96 px (o grid do curso).
- **Fonte de ícones.** `[skill: tech-mentor-frontend]` O exemplo `content: "\f112"` é de icon font (estilo Font Awesome). Leitor de tela pode anunciar o caractere do `::before`, e a fonte falha se não carregar. Hoje o padrão é SVG inline ou sprite com `aria-hidden="true"` ([[wiki/concepts/icones-em-interfaces]]).
- **O código dos ícones.** Ele lê "F112e" e "F112f" na primeira vez; os valores são `\f12e` e `\f12f`, que ele lê certo depois.
- **`@while` arrisca loop infinito.** Se a condição nunca fica falsa, a compilação trava. A própria documentação recomenda `@each` ou `@for` quando possível.

## Open Questions

- "Aqui no próprio set da Nubank": o arquivo do Figma do projeto (o "set")? Mantido como na legenda.
- O terceiro exemplo do `@each` (lista com desestruturação) ficou "para vocês também descobrirem".

## Raw quotes

- "não é uma divisão muito exata, mas a gente, com o olho, consegue ter uma boa aproximação"
- "mixins é uma coisa e funções é outra"
- "indico vocês demais a sempre estarem verificando a documentação do próprio Sass"
