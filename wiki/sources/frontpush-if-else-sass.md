---
type: source
title: "@if e @else no Sass: tema light/dark e tipografia do projeto Nubank (FrontPUSH)"
aliases: ["Propriedades @if & @else", "if else Sass FrontPUSH", "módulo de CSS Sass, aula 07", "operadores Sass"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, sass, scss, if-else, controle-de-fluxo, mixin, variaveis, tema-escuro, tipografia, breakpoint, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-if-else-sass.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-16
---

# @if e @else no Sass (FrontPUSH)

## TL;DR

Aula 07 do módulo de CSS Sass do [[wiki/entities/frontpush|FrontPUSH]] (instrutor inferido: [[wiki/entities/nasser|Násser]]). Assunto: [[wiki/concepts/if-else-sass]].

- **Para quê:** "estruturas encadeadas de programação" que dão "mais elasticidade aos mixins" e criam "cenários diferentes de estilização" ([[wiki/concepts/logica-de-programacao]]).
- **Slide:** `@if $layout == light { $bg-color: #EFEFEF; $text-color: #101010; } @else if $layout == dark { $bg-color: #101010; $text-color: #EFEFEF; }`.
- **Demo:** `$layout: dark;` no topo; `body` usa `$bg-color`, `h1` e parágrafo `$text-color`. Primeiro deu **"undefined variable"**: as variáveis precisavam existir fora do `@if`. Depois de declarar o padrão fora, troca entre `dark` e `light` e recompila ([[wiki/concepts/variaveis-sass]]).
- **No projeto Nubank:** mixins `typeface-1` (Sora, títulos) e `typeface-2` (Source Sans Pro, texto) com parâmetros tamanho (`h1`…`h5`) e dispositivo (`desktop` padrão, ou `mobile`), e um `@if` que escolhe `font-size` e `line-height`. Mais um mixin de layout com breakpoints `xl`/`l`/`m`/`s`/`xs` (acima de 1440, 1140–1440, 960–1140, abaixo de 960, abaixo de 540) e `@content` ([[wiki/concepts/mixin-sass]], [[wiki/concepts/breakpoint]]).

## Key Claims

### O recurso

- "Como o próprio nome já grita para quem conhece a linguagem de programação, esses comandos servem para criar estruturas encadeadas."
- "Se eu quiser emendar mais estruturas, mais de duas, eu posso colocar else if [...] se eu não quiser, eu simplesmente fecho com else."
- Com só duas opções, "eu simplesmente poderia colocar aqui a estrutura else, e ela seria a mais indicada".

### Light × dark

- "A gente precisa fazer um toggle entre a cor de background e a cor de texto, de cor clara para cor escura, e aí a gente troca os dois."
- Light: fundo `#EFEFEF` ("um branquinho"), texto `#101010` (ou `#1A1A1A`, "um cinza mais escuro"); dark: os dois invertidos.
- O erro: "bg-color, undefined variable. Simplesmente, pessoal, é porque eu preciso defini-las primeiro sem ser na estrutura encadeada, por mais que seja o valor padrão. Depois ele pode simplesmente modificar."
- "Posso mudar para dark e para light, dark, light [...] trocar literalmente as cores do meu sistema", e o mesmo vale para padding e espaçamento. "Isso aqui vinculado aos mixins é de um resultado incrível."

### Tipografia e layout do projeto Nubank

- "Eu criei um mixin de typefaces de tipografia, ou seja, typeface 1 é mais voltada para títulos, utilizando a font-family Sora, e a typeface 2 é voltada para corpo de texto, utilizando o font-family Source Sans Pro" ([[wiki/concepts/combinacao-de-fontes]]).
- Parâmetros: tamanho (`h1` maior, `h5` menor) e dispositivo (`desktop` ou `mobile`, padrão `desktop`); "uma estrutura encadeada aqui dentro, onde vai modificar o font-size e o line-height de acordo com a opção" ([[wiki/concepts/escala-tipografica]]).
- Uso: no `h1`, `@include typeface-1(h1, desktop)` e, dentro de um mixin de responsividade (`small`), `typeface-1(h1, mobile)`, "para todos, h1, h2, h3, h4, h5". "Basta eu modificar alguma coisa aqui que automaticamente toda a minha estrutura textual vai ser modificada."
- Layout: "xl, l, m, s e xs [...] extra large, large, medium, small, extra small: aqui para resoluções acima de 1440, aqui entre 1140 e 1440, entre 960 e 1140, menor que 960 e menor que 540". "Desde que elas sejam combinadas, isso aqui é de um poder inimaginável."

## Entities

- [[wiki/entities/nasser]]: instrutor (inferido).
- [[wiki/entities/frontpush]]: curso; aula 07 do módulo de CSS Sass.
- [[wiki/entities/nubank]]: projeto com os mixins de tipografia e de layout.
- [[wiki/entities/google-fonts]]: Sora e Source Sans Pro (inferido: as duas são do Google Fonts).

## Concepts

- [[wiki/concepts/if-else-sass]]
- [[wiki/concepts/mixin-sass]]
- [[wiki/concepts/variaveis-sass]]
- [[wiki/concepts/variaveis-css]]
- [[wiki/concepts/logica-de-programacao]]
- [[wiki/concepts/escala-tipografica]]
- [[wiki/concepts/combinacao-de-fontes]]
- [[wiki/concepts/breakpoint]]
- [[wiki/concepts/design-tokens]]
- [[wiki/concepts/pre-processador-css]]

## Precisões e tensões com a wiki

- **O tema do Sass não troca no navegador.** `[skill: tech-mentor-frontend]` O `@if $layout == dark` roda na compilação: o CSS gerado tem só um tema, e trocar exige recompilar. Para o usuário alternar (ou seguir o sistema), as cores precisam ser custom properties: `:root { --bg: #EFEFEF; } [data-theme="dark"] { --bg: #101010; }` e/ou `@media (prefers-color-scheme: dark)` ([[wiki/concepts/variaveis-css]]). O Sass pode gerar os dois blocos a partir de um mapa, mas quem troca é o CSS.
- **Por que deu "undefined variable".** `[external]` No Sass, uma variável declarada pela primeira vez dentro de `@if` é local àquele bloco. Se ela já existe fora, a atribuição dentro do bloco altera a de fora, sem sombrear (https://sass-lang.com/documentation/variables/#flow-control-scope). O conserto dele, declarar o padrão antes, é o certo; a regra só não foi dita.
- **Operadores.** `[external]` `==` e `!=` comparam; `and`, `or` e `not` combinam; `<`, `>`, `<=` e `>=` são para números. `light` sem aspas e `"light"` com aspas são iguais para `==` (https://sass-lang.com/documentation/operators/). A aula promete "operadores" no título, mas só mostra `==`.
- **Mapa no lugar de `@if` em cadeia.** `[skill: tech-mentor-frontend]` Cinco tamanhos × dois dispositivos viram dez ramos de `@if`. Um mapa (`$type: (h1: (desktop: 72px 1.1, mobile: 48px 1.1), ...)` + `map.get`) faz o mesmo em uma linha e dá erro claro para chave inexistente ([[wiki/concepts/mixin-sass]]). É também o formato natural de [[wiki/concepts/design-tokens]].
- **Breakpoints do Nubank × do módulo.** A escala `xs` < 540, `s` < 960, `m` 960–1140, `l` 1140–1440, `xl` > 1440 inclui o 960 do curso, mas não o 720 da [[wiki/sources/frontpush-mixin-e-content-sass|aula 06]] ([[wiki/concepts/breakpoint]]).
- **Contraste.** `#101010` sobre `#EFEFEF` passa folgado no WCAG: 16,5:1, calculado pela fórmula de luminância relativa, contra o mínimo de 4,5:1 para texto normal.

## Open Questions

- "Eu demonstro com mais ênfase e mudou lá no projeto": "e tudo lá no projeto"? Mantido.
- A aula do projeto Nubank com esses mixins ainda não está na wiki; os nomes exatos (`typeface-1` ou `typeface1`) vêm da fala.

## Raw quotes

- "dá mais elasticidade aos mixins"
- "eu preciso defini-las primeiro sem ser na estrutura encadeada"
- "isso aqui vinculado aos mixins é de um resultado incrível"
