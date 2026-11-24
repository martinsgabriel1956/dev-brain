---
type: concept
title: "Grid de Colunas"
aliases: ["column grid", "layout grid", "grid de 12 colunas", "12-column grid", "gutter", "calha"]
date_created: 2026-11-13
date_updated: 2026-11-24
source_count: 14
tags: [ui, ui-design, layout, grid, grid-de-colunas, alinhamento, consistencia, figma]
skill: ux-ui-mentor
status: draft
---

# Grid de Colunas

Divisões verticais da página ("colunas, réguas") em que o conteúdo se alinha. É a primeira coisa a acertar antes de mexer em espaçamento ([[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]]).

## Por que 12 colunas

No desktop, "por padrão sempre 12 colunas": 12 divide por 2, 3, 4 e 6, então o mesmo grid acomoda layouts de duas, três, quatro ou seis partes iguais.

## A configuração da aula

12 colunas de 72, gutter de 32 ("o espaço entre cada coluna"), centralizado no frame do [[wiki/entities/figma]]. Largura total do conteúdo: 12 × 72 + 11 × 32 = 1216 (conta do agente). O headline encosta na primeira coluna; os blocos distribuídos na horizontal terminam alinhados ao grid.

## Anatomia

`[skill: ux-ui-mentor]` Margem | coluna | gutter | coluna | ... | margem. Grids típicos por breakpoint na skill:

| Breakpoint | Colunas | Gutter | Margem |
|---|---|---|---|
| Mobile (< 768 px) | 4 | 16 | 16 |
| Tablet (768–1024 px) | 8 | 24 | 24 |
| Desktop (1024–1440 px) | 12 | 24 | 32 |
| Wide (> 1440 px) | 12 | 32 | auto (max-width centralizado) |

O gutter de 32 da aula corresponde à linha "wide" da skill. Os valores de coluna, gutter e margem saem da [[wiki/concepts/escala-de-espacamento]] (72 = 9 × 8; 32 e 16 também são múltiplos de 8), o que junta o grid de colunas ao [[wiki/concepts/grid-de-8-pontos]].

`[skill: ux-ui-mentor]` No código, o equivalente direto é `display: grid; grid-template-columns: repeat(12, 1fr); gap: 32px;` dentro de um container com max-width e `margin-inline: auto`.

## Grid como esqueleto

Em [[wiki/sources/grids-parte-1-colunas-bootstrap-8pt-fixo-fluido-adaptativo-responsivo]]: grids "criam a estrutura básica, o esqueleto para o seu design", colunas onde os elementos são colocados e alinhados. Servem ao designer (alinhamento, "consistência de distância") e ao dev (resoluções, [[wiki/concepts/breakpoint|breakpoints]]). Na landing page do [[wiki/entities/frontpush]], 12 colunas imaginárias se dividem em 7–8 + 4–5 no site e 4 + 8 no design. No wireframe, o conteúdo pega as seis colunas centrais e sobram três de cada lado. A coluna vira unidade de distância: "quanto que tem de distância de um elemento para o outro? Ah, é uma coluna."

O padrão citado para colunas por dispositivo é o Bootstrap Grid System ([[wiki/entities/twitter-bootstrap]]). `[external]` 12 colunas e seis faixas de breakpoint no Bootstrap 5 (https://getbootstrap.com/docs/5.3/layout/grid/).

## Relação com outros conceitos

- [[wiki/concepts/consistencia-visual]] — o grid é o mesmo em todas as telas, o que dá ritmo e alinhamento.
- [[wiki/concepts/grid-de-8-pontos]] — o grid de 8 decide os vãos; o de colunas decide onde as coisas começam e terminam.
- [[wiki/concepts/grid-de-icones]] — o mesmo princípio de "réguas", em escala de ícone.
- [[wiki/concepts/design-responsivo]] — o número de colunas cai em telas menores.

## Containers por dispositivo

Na abertura do módulo de interfaces web: "você precisa saber e desenhar containers de acordo com o dispositivo", seguindo "padrões [...] de colunas, de grids, de alinhamento", para "quebrar em blocos depois" e servir o mesmo conteúdo em vários dispositivos ([[wiki/sources/interfaces-web-introducao-workflow-grids-pagemap-wireframes-style-guide]]). Grids estão na etapa de wireframes do [[wiki/concepts/workflow-de-interface-web]] e no [[wiki/concepts/style-guide]]. `[skill: ux-ui-mentor]` Padrão típico: 4 colunas no mobile, 8 no tablet, 12 no desktop.

## Por dispositivo (aula de grids, parte 2)

Em [[wiki/sources/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos]], as quatro variáveis são **width** (coluna), **columns**, **gutter** e **max-width** (de ponta a ponta), "baseado no Bootstrap Grid System":

| | Colunas | Width | Gutter | max-width |
|---|---|---|---|---|
| Desktop | 12 | 72–96 | 24–36 | 1200–1440 |
| Tablet | 6 | 72–96 | 24–36 | 620–720 |
| Mobile | 4 (6 em paisagem) | 56–72 | 24–36 | 320–396 |

Conta: colunas × width + (colunas − 1) × gutter ≈ max-width (72 × 12 + 24 × 11 = 1.128 ≈ 1.200). O tablet é o desktop "dividido por 2". Ele prefere 4 ou 6 colunas no celular a 3 ou 2. 12 de novo pela divisão: "quando fica oito de um lado, eu sei que sobra quatro do outro". As faixas estão em [[wiki/concepts/breakpoint]].

`[external]` No Bootstrap, a coluna é porcentagem do container e o gutter padrão é 24 px (https://getbootstrap.com/docs/5.3/layout/gutters/); coluna de 72 é convenção de Figma. A skill dá 8 colunas no tablet; a aula, 6.

## Padrões prontos e calculadora

Em [[wiki/sources/grids-pratica-2-material-de-apoio-bootstrap-material-design-flexbox-grid]], a Grid System Library traz grids de iOS, Android e Bootstrap (de 6 a 12 colunas, até mobile com duas) e uma calculadora: largura 1.440, 12 colunas, gutter de 32 e margem viram a largura da coluna, "não chutando valores". Os padrões dela não são os da aula: "você desenha e vê qual o melhor padrão para você". 4, 8 e 12 colunas são "esses números que a gente está sempre circundando"; ver [[wiki/concepts/breakpoint]].

## Max-width: coluna + gutter

Em [[wiki/sources/grids-pratica-figma-12-colunas-alinhamento-blocos-equilibrio-menu]], o grid sai do Figma no tipo **Center** (coluna fixa, grid centralizado), e não Stretch. Stretch "sempre vai preencher a tela inteira", mas pede "uma série de breakpoints maior". Coluna e gutter definem o max-width do conteúdo (12 × coluna + 11 × gutter, conta do agente):

| Coluna | Gutter | Max-width |
|---|---|---|
| 72 | 32 | 1216 |
| 72 | 36 | **1260** (o que ele mais usa) |
| 96 | 24 | 1416 (rumo a 1440) |
| 96 | 32 | 1504 |
| 96 | 36 | 1548 (TV, rumo a 1600) |

O grid é "um guia", não uma régua de precisão: figuras de 88 ou ilustrações que saem da coluna são normais se o alinhamento continua no grid. Blocos do mesmo número de colunas viram a mesma classe no código ("tudo é div, tudo é bloco"). Onde 12 não divide (três elementos com sobras), agrupar e usar distribuir horizontal spacing. Ver também [[wiki/concepts/equilibrio-visual]]: o grid deixa contar o peso de cada lado.

`[external]` O Bootstrap 5, que ele cita como origem, usa colunas fluidas e gutter de 24 px; containers até 1320 (https://getbootstrap.com/docs/5.3/layout/containers/).

## Do grid do Figma ao container (FrontPUSH, módulo de Flexbox)

Em [[wiki/sources/frontpush-flexbox-pratica-1-layout-youtube-estrutura-html]], [[wiki/entities/nasser|Násser]] parte de um grid de 12 colunas de 96 px com gutter de 24 px, "próximo de 1440px", que define a largura do container. (12 × 96 + 11 × 24 = 1416 px; as margens completam os 1440.)

## Classes de grid geradas por loop (FrontPUSH, Sass)

Em [[wiki/sources/frontpush-for-while-each-sass]]: 12 colunas de 96 px e gutter de 24; 2 colunas = 216 px, 5 = 576, 7 = 816. Fazer `.grid1`…`.grid12` à mão "eu tenho que sempre vir aqui e modificar na mão"; o `@for` gera as doze. A fórmula com gutter é `$i * 96px + ($i - 1) * 24px` (12 colunas = 1416 px). Com grid, o código fica "bem mais fiel ao layout projetado" do que com `flex-grow` "no olho". `[skill: tech-mentor-frontend]` Hoje, `grid-template-columns: repeat(12, 1fr)` + `grid-column: span N` faz o mesmo de forma fluida ([[wiki/concepts/css-grid]]).

## Grid fluido em % (FrontPUSH, Sass aula 09)

Em [[wiki/sources/frontpush-funcoes-sass]]: o grid de 1416 px precisa "dar uma apertadinha" em notebooks de 1366, então as colunas viram %: `grid($col, $total: 12)` = `$col / $total * 100%` (5 → 41,67%). Sem gutter. Com o gutter do curso, 5 colunas = 576 / 1416 = 40,68%; 3 = 23,73%; 7 = 57,63%.

## Do Figma para um grid system (FrontPUSH, Sass aula 10)

Em [[wiki/sources/frontpush-grid-system-sass-parte-1]]: o grid de 12 × 96 + 24 (1416 px) vira uma biblioteca de classes "muitíssimo parecida com o Grid System do próprio Bootstrap", com largura em % e container de `max-width` fixo que fica fluido abaixo dele. Ver [[wiki/concepts/grid-system]]. No código, a variável do container está em 1200, não em 1416.

## Em dashboards: 12 colunas com offset

Na [[wiki/sources/frontpush-dashboards-grids-e-patterns|aula 03 do módulo de dashboards]], as mesmas 12 colunas das landing pages viram grid de dashboard: tipo Left, coluna de 70 ou 80 px, gutter de 30 e um offset de 120 a 280 px para a sidebar, num frame de 1440 × 900. Ver [[wiki/concepts/grid-de-dashboard]].

## Key Sources

- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] — 12 colunas de 72, gutter de 32, centralizado; 12 pelos bons múltiplos
- [[wiki/sources/interfaces-web-introducao-workflow-grids-pagemap-wireframes-style-guide]] — containers e colunas por dispositivo; grids no workflow e no style guide
- [[wiki/sources/grids-parte-1-colunas-bootstrap-8pt-fixo-fluido-adaptativo-responsivo]] — grid como esqueleto; 12 colunas no FrontPUSH (7–8 + 4–5; 4 + 8); seis colunas centrais no wireframe; "é uma coluna" de distância
- [[wiki/sources/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos]] — width, columns, gutter, max-width por dispositivo (12/6/4); contas na calculadora
- [[wiki/sources/grids-pratica-2-material-de-apoio-bootstrap-material-design-flexbox-grid]] — Grid System Library, Bootstrap, Material Design; 4/8/12 colunas
- [[wiki/sources/grids-pratica-figma-12-colunas-alinhamento-blocos-equilibrio-menu]] — 72 + 36 = 1260 (o principal), 1216, 1416, 1504, 1548; Center x Stretch; pensar em blocos; grid como guia; equilíbrio do menu
- [[wiki/sources/frontpush-conclusao-modulo-css-estilo-layout-animacao-documentacao]]: o grid do Figma levado ao código como grid system em Sass (hoje CSS Grid faz sem float)
- [[wiki/sources/frontpush-flexbox-pratica-1-layout-youtube-estrutura-html]]: 12 colunas de 96 px + gutter 24 px ≈ 1440 px viram o container
- [[wiki/sources/frontpush-flexbox-pratica-2-desafio-estrutura-de-divs]]: container de 1.200 ou 1.440 px "de acordo com o grid que você estabeleceu"
- [[wiki/sources/frontpush-mentoria-pratica-com-css-grid]]: mentoria de grid: container de 1.440 px; a malha 5 × 5 sai do menor card, não de um grid de 12 colunas
- [[wiki/sources/frontpush-for-while-each-sass]]: classes `.grid-N` geradas por `@for`; 96 + 24
- [[wiki/sources/frontpush-funcoes-sass]]: função `grid()` em %; valores com e sem gutter
- [[wiki/sources/frontpush-grid-system-sass-parte-1]]: grid de 1416 virando grid system de classes
- [[wiki/sources/frontpush-dashboards-grids-e-patterns]]: FrontPUSH, dashboards aula 03: 12 colunas deslocadas pela sidebar
