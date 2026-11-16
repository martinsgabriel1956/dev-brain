---
type: concept
title: "Loops no Sass (@for, @each, @while) e interpolação #{}"
aliases: ["@for", "@each", "@while", "loops Sass", "estruturas de repetição Sass", "interpolação Sass", "#{}"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [css, sass, scss, loops, interpolacao, function, controle-de-fluxo]
skill: tech-mentor-frontend
status: stub
---

# Loops no Sass (@for, @each, @while) e interpolação #{}

Regras do [[wiki/concepts/pre-processador-css|Sass]] que repetem um bloco na compilação para gerar muitas regras de CSS a partir de poucas linhas. Fazem parte do controle de fluxo, junto com [[wiki/concepts/if-else-sass]].

| Regra | Forma | Quando usar |
|---|---|---|
| `@for` | `@for $i from 1 through 12` (`to` exclui o fim) | contagem fixa: classes numeradas, colunas |
| `@each` | `@each $x in $lista` / `@each $chave, $valor in $mapa` | percorrer [[wiki/concepts/array|listas]] e mapas: tamanhos, cores, ícones, tokens |
| `@while` | `@while $cond { ... }` | só quando não há lista nem contagem; cuidado com loop infinito |

**Interpolação `#{}`:** necessária para pôr um valor em seletor, nome de propriedade ou string: `.grid-#{$i}`. Em valores comuns (`width: 96px * $i`), não precisa. É o equivalente do `${}` das template strings do JavaScript.

**`@function` × `@mixin`:** função devolve um valor com `@return` e entra numa propriedade (`font-size: scale-below(20px, 16px)`); mixin despeja declarações com `@include` ([[wiki/concepts/mixin-sass]]).

## No FrontPUSH

[[wiki/sources/frontpush-for-while-each-sass]]: `@for` gerando `.grid-1`…`.grid-12` (96 px por coluna, gutter fora da conta); os exemplos da documentação de `@for` (`nth-child` + `lighten`), `@while` (`scale-below` com razão áurea 1.618) e `@each` (lista de tamanhos e mapa de ícones). As classes de grid são a base do "sistema de grids" prometido para as aulas práticas ([[wiki/concepts/grid-de-colunas]]).

## Hoje

- `[external]` Use os módulos: `math.div()` em vez de `/`, e `color.adjust`/`color.scale` em vez de `lighten`/`darken` globais (https://sass-lang.com/documentation/breaking-changes/slash-div/).
- `[skill: tech-mentor-frontend]` Gerar dezenas de classes de largura fixa é a era pré-[[wiki/concepts/css-grid]]. Os loops continuam bons para utilitários a partir de mapas de [[wiki/concepts/design-tokens]] (`@each $nome, $cor in $cores { .text-#{$nome} { color: $cor; } }`), que é como bibliotecas de utilitários eram geradas antes do Tailwind.
- Cada iteração vira CSS de verdade: um loop grande infla o arquivo final.

## Loops dentro de funções (FrontPUSH, aula 09)

Em [[wiki/sources/frontpush-funcoes-sass]], o exemplo `pow($base, $exponent)` da documentação usa `@for` para multiplicar a base "quantas vezes tem um expoente" (2³ → 2, 4, 8). Ver [[wiki/concepts/funcoes-sass]].

## Key sources

- [[wiki/sources/frontpush-for-while-each-sass]]: `@for` para classes de grid; `@while` em `@function`; `@each` em lista e mapa
- [[wiki/sources/frontpush-funcoes-sass]]: `@for` dentro de `pow`
