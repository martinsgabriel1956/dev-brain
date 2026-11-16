---
type: source
title: "Funções no Sass: @function, @return, grid em porcentagem e funções de cor (FrontPUSH)"
aliases: ["Funções @functions", "@function Sass FrontPUSH", "módulo de CSS Sass, aula 09", "função grid Sass"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, sass, scss, function, return, grid, grid-de-colunas, layout-fluido, porcentagem, cores, operadores, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-funcoes-sass.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-16
---

# Funções no Sass (FrontPUSH)

## TL;DR

Aula 09 do módulo de CSS Sass do [[wiki/entities/frontpush|FrontPUSH]] (instrutor inferido: [[wiki/entities/nasser|Násser]]). Assunto: [[wiki/concepts/funcoes-sass]].

- **Função × mixin:** a função "é um bloco que retorna sempre um valor", depois de "algum tipo de conta [...] verificação, alguma tomada de decisão"; o mixin "é basicamente um Ctrl+C, Ctrl+V" com `@include` ([[wiki/concepts/mixin-sass]]).
- **Slide:** `@function grid($col, $total: 12) { @return ($col / $total) * 100%; }`; `grid(3)` → `width: 25%`.
- **Por que porcentagem:** o layout do Nubank foi desenhado para 1920 × 1080, o grid tem 1416 px, e há notebooks de 1366 px. O grid tem de ser "uma sanfona em que ele vai lá e dá uma apertadinha [...] antes de quebrar para a versão mobile". 5 de 12 colunas = 41,67%; 7 = 58,33% ([[wiki/concepts/layout-fixo-fluido-adaptativo-responsivo]], [[wiki/concepts/grid-de-colunas]]).
- **Funções de cor prontas** (slide): `darken(#5fe36a, 50%)`, `lighten(#5fe36a, 20%)`, `transparentize(#5fe36a, 0.7)`, a que ele "mais utiliza". Do módulo `sass:color`: `adjust-hue`, `blackness`, `complement`, `desaturate`, `grayscale`, `mix`, `opacify`/`fade-in`. Ele quase não usa as de clarear e escurecer: as variações saem prontas do Figma ([[wiki/concepts/variacao-de-cores]]).
- **Exemplos da documentação:** `pow($base, $exponent)` com `@for` e `invert($color, $amount)` com `mix`. Operadores de comparação, aritméticos (incluindo resto) e de string (`+`, `#{}`).
- **Sem gutter:** "estou fazendo só com colunas para vocês entenderem o princípio".

## Key Claims

### Função × mixin

- "A função [...] é um bloco que retorna sempre um valor [...] na grande maioria das linguagens de programação, ele sempre vai retornar alguma coisa" ([[wiki/concepts/funcoes-javascript]]).
- "O que você faz no mixin é basicamente um Ctrl+C, Ctrl+V. Você estabelece aqui o nome do mixin, é um conjunto de pré-propriedades que você sempre vai estar aplicando, e aí você dá o include."
- "Ela vai fazer algum tipo de conta, algum tipo de cálculo, alguma verificação, alguma tomada de decisão que vai te retornar algo, seja um array, seja um valor."

### Grid fluido

- "Quando a gente está trabalhando com responsividade, o caráter ser responsivo precisa ser adaptável e ele precisa ser fluido."
- "O meu website foi desenhado, por exemplo, para resoluções de 1920 por 1080 [...] tem, por exemplo, pessoas que utilizam o notebook com resoluções menores, por exemplo, de 1366."
- "Pensa o seu grid como se fosse uma sanfona [...] Para poder ser fluido, ele precisa utilizar porcentagem" ([[wiki/concepts/unidades-de-medida-css]]).
- "Cinco grids correspondem a quanto de 12? [...] cinco dividido por 12 [...] 41,6% é o tamanho dessa div com relação ao grid maior."
- Na demo: `@return ($col / $total) * 100%`. "Se eu colocasse só 100, ele iria me devolver o valor, mas, como eu coloquei uma unidade, 100%, ele também vai me devolver 100%." `grid(3)` = 25%; `grid(5)` = 41.66667%.

### Funções prontas e exemplos

- `darken` "50% mais escuro", `lighten` "20% mais claro". "O que eu mais utilizo, de fato, é o transparentize, porque ele converte o hexadecimal [...] que não possui transparência" em RGBA.
- `adjust-hue` gira a matiz em graus no [[wiki/concepts/circulo-cromatico]] (60deg no exemplo) ([[wiki/concepts/modelo-de-cor-hsb]]).
- `pow`: resultado começa em 1 e é multiplicado pela base "quantas vezes tem um expoente": 2³ → 2, 4, 8 ([[wiki/concepts/loops-sass]]).
- Operadores: comparar, "maior, menor, maior ou igual", "somar, subtrair, dividir, resto"; strings concatenadas com `+`, "muito parecido com o JavaScript".

## Entities

- [[wiki/entities/nasser]]: instrutor (inferido).
- [[wiki/entities/frontpush]]: curso; aula 09 do módulo de CSS Sass.
- [[wiki/entities/nubank]]: layout de 1920 × 1080 com grid de 1416 px.
- [[wiki/entities/figma]]: variações de cor feitas no design, não no Sass.

## Concepts

- [[wiki/concepts/funcoes-sass]]
- [[wiki/concepts/mixin-sass]]
- [[wiki/concepts/loops-sass]]
- [[wiki/concepts/if-else-sass]]
- [[wiki/concepts/grid-de-colunas]]
- [[wiki/concepts/grid-system]]
- [[wiki/concepts/layout-fixo-fluido-adaptativo-responsivo]]
- [[wiki/concepts/unidades-de-medida-css]]
- [[wiki/concepts/variacao-de-cores]]
- [[wiki/concepts/modelo-de-cor-hsb]]
- [[wiki/concepts/circulo-cromatico]]
- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/pre-processador-css]]

## Precisões e tensões com a wiki

- **`transparentize(#5fe36a, 0.7)` deixa 30% de opacidade, não 70%.** `[external]` A função **subtrai** 0.7 do alfa: o resultado é `rgba(95, 227, 106, 0.3)` (https://sass-lang.com/documentation/modules/color/#transparentize). "Com esse caráter de opacidade 0.7" inverte o sentido. Para chegar a 70% de opacidade, `transparentize(#5fe36a, 0.3)` ou, no Sass moderno, `color.change(#5fe36a, $alpha: 0.7)`.
- **As funções globais de cor estão deprecadas.** `[external]` `darken`, `lighten`, `transparentize` e `adjust-hue` são formas antigas. O módulo `sass:color` usa `color.adjust($c, $lightness: -50%)`, `color.scale(...)` e `color.change(...)`, e o Dart Sass avisa no uso global. Além disso, `darken(#x, 50%)` tira 50 pontos absolutos de luminosidade, o que leva quase tudo ao preto. `color.scale` (proporcional) costuma dar o resultado esperado.
- **A divisão com `/` também está deprecada.** `[external]` `$col / $total` vira `math.div($col, $total)`. Também existe `math.percentage(math.div($col, $total))`, que já devolve em %.
- **Com gutter, as porcentagens mudam.** Com o grid do curso (96 px + 24 de gutter, 1416 no total), 3 colunas = 336 px = **23,73%**, não 25%; 5 = 576 px = **40,68%**, não 41,67%; 7 = 816 px = **57,63%**, não 58,33%. A função da aula serve para colunas sem gutter. Conta feita aqui com os números da aula.
- **O CSS nativo já calcula isso.** `[skill: tech-mentor-frontend]` `width: calc(5 / 12 * 100%)` resolve sem Sass. O [[wiki/concepts/css-grid]] (`repeat(12, 1fr)` + `gap`) elimina a conta e o gutter de uma vez. Para cor, o CSS tem `color-mix()` e a sintaxe de cor relativa (`rgb(from #5fe36a r g b / 0.3)`), avaliados no navegador e combináveis com custom properties ([[wiki/concepts/variaveis-css]]).
- **Unidade como multiplicador.** O "100%" funciona porque `0.25 * 100%` dá `25%`: o Sass carrega unidades nas contas. Multiplicar por `100` e concatenar `"%"` como string é o erro clássico que essa técnica evita.
- **"Arroba col".** Na fala, o parâmetro é "arroba col"; no slide e no Sass, `$col`.

## Open Questions

- "Ele está como RGBA, 23600 .3": provavelmente `rgba(236, 0, 0, 0.3)`, o vermelho de 30% do bloco no Figma; mantido como na legenda.
- "Por isso que eu decidi explicar para vocês, que é mais keywords": referência a argumentos de palavra-chave (`meta.keywords`) da documentação? Mantido.

## Raw quotes

- "o que você faz no mixin é basicamente um Ctrl+C, Ctrl+V"
- "pensa o seu grid como se fosse uma sanfona"
- "o que eu mais utilizo, de fato, é o transparentize"
