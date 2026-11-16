---
type: concept
title: "Funções no Sass (@function, @return e módulos embutidos)"
aliases: ["@function", "@return", "funções Sass", "sass:color", "sass:math", "darken", "lighten", "transparentize", "math.div"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [css, sass, scss, function, cores, math, modulos]
skill: tech-mentor-frontend
status: stub
---

# Funções no Sass (@function, @return e módulos embutidos)

`@function nome($arg, $opcional: padrão) { ...; @return valor; }` define um cálculo reaproveitável, usado **dentro de um valor**: `width: grid(5)`. Diferente do [[wiki/concepts/mixin-sass|mixin]], que despeja declarações com `@include`. Dentro da função valem variáveis, [[wiki/concepts/if-else-sass]] e [[wiki/concepts/loops-sass]].

## No FrontPUSH

- [[wiki/sources/frontpush-for-while-each-sass]]: a primeira explicação certa de função × mixin; exemplo `scale-below` com `@while`.
- [[wiki/sources/frontpush-funcoes-sass]]: a aula dedicada. `grid($col, $total: 12)` devolve `($col / $total) * 100%` para um [[wiki/concepts/grid-de-colunas|grid]] fluido (sem gutter); funções de cor `darken`, `lighten`, `transparentize` ("o que eu mais utilizo"), `adjust-hue`, `mix`; exemplos `pow` e `invert` da documentação; operadores.

## Módulos embutidos (Sass atual)

`[external]` (https://sass-lang.com/documentation/modules/)
- `@use "sass:math";`: `math.div`, `math.percentage`, `math.round`, `math.pow`, `math.clamp`. A `/` como divisão está deprecada.
- `@use "sass:color";`: `color.adjust` (soma: `$lightness: -10%`, `$alpha: -0.3`), `color.scale` (proporcional), `color.change` (define: `$alpha: 0.7`), `color.mix`, `color.complement`, `color.grayscale`. As formas globais (`darken`, `lighten`, `transparentize`, `adjust-hue`) são legado.
- `sass:map`, `sass:list`, `sass:string`, `sass:meta` para estruturas, texto e introspecção.

**Armadilha:** `transparentize($c, 0.7)` **tira** 0.7 do alfa e deixa 30% de opacidade. Para fixar a opacidade, use `color.change($c, $alpha: 0.7)`.

## Quando o CSS nativo basta

`[skill: tech-mentor-frontend]`
- Proporções: `calc(5 / 12 * 100%)`, ou nenhuma conta com [[wiki/concepts/css-grid]].
- Cor: `color-mix(in oklch, var(--cor) 70%, transparent)` e cor relativa (`rgb(from var(--cor) r g b / 0.3)`) funcionam com custom properties e reagem a temas em tempo de execução; as funções do Sass só veem valores fixos da compilação ([[wiki/concepts/variaveis-css]]).
- O Sass continua útil para cálculos que geram tokens na compilação (escalas, mapas de cores).

## Key sources

- [[wiki/sources/frontpush-funcoes-sass]]: `grid()` em porcentagem; funções de cor; operadores
- [[wiki/sources/frontpush-for-while-each-sass]]: função × mixin; `scale-below`
