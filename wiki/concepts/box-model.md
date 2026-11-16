---
type: concept
title: "Box Model (CSS)"
aliases: ["CSS box model", "content-padding-border-margin"]
date_created: 2026-07-28
date_updated: 2026-11-16
source_count: 13
tags: [browser, css, box-model, layout, html-semantico, shorthand-css, padding, margin]
skill: tech-mentor-frontend
status: draft
---
# Box Model (CSS)

Todo elemento renderizado é uma caixa composta por quatro camadas, de dentro para fora: **content**, **padding**, **border** e **margin**. Durante a etapa de [[wiki/concepts/reflow-layout|layout]], o browser calcula o tamanho final de cada caixa considerando essas camadas e o fluxo do documento — unidades relativas (`%`, `auto`) viram valores absolutos em pixels nesse momento.

## Reset e display na aula de classes e IDs

Em [[wiki/sources/classes-e-ids-no-css]], o reset `* { margin: 0; padding: 0; box-sizing: border-box }` vem antes de qualquer explicação do box model ("esses conceitos aqui eu vou explicar nas próximas aulas"). O link nasce `display: inline`, "de texto, que não é de caixa"; o `.btn` vira `display: block` para "virar uma caixinha" e aceitar width e height. `[external]` Com `border-box`, width e height incluem padding e borda: https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing.

## Reset de margin, padding e box-sizing

Em [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]], o primeiro `style.css` da aula zera `margin` e `padding` e aplica `box-sizing: border-box`; o espaço entre as tags diminui, porque some a margem padrão do navegador. `[external]` Com `border-box`, `width` e `height` passam a incluir padding e border: https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing.

## Tudo é caixa (aula de Básico CSS)

Em [[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]], [[wiki/entities/nasser|Násser]] faz do box model a tese do módulo: "tudo é caixa", toda tag "são caixas, são box, são divs". As propriedades de caixa são width, height, padding ("espaçamento interno", do conteúdo até a borda), margin ("a distância entre uma caixa e outra"), border e [[wiki/concepts/border-radius]]. Como a caixa tem quatro lados, padding e margin têm `-top`, `-right`, `-bottom`, `-left`, e o [[wiki/concepts/shorthand-css|shorthand]] segue o sentido horário a partir do topo. Medidas em [[wiki/concepts/unidades-de-medida-css|unidades]] fixas ou relativas. Mesma ideia do "tudo é div" da aula de grids ([[wiki/sources/grids-pratica-figma-12-colunas-alinhamento-blocos-equilibrio-menu]]).

`[external]` O que a aula não cobre (https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Box_model): (1) **`box-sizing`**: no padrão `content-box`, width e height não incluem padding e border, então padding aumenta a caixa; `border-box` inclui, e é o reset mais comum. (2) **Colapso de margens**: margens verticais de blocos adjacentes se fundem na maior, não se somam. (3) **Inline**: span, a e strong ignoram width e height. Confiança alta.

## Margin auto e display

Em [[wiki/sources/principais-propriedades-css-color-background-font]], `margin: 0 auto` zera a margem vertical e divide a horizontal, centralizando uma section de 80%. O autor força `display: block` no link-botão porque o link é inline e ele quer "aplicar sempre as propriedades de box-model" ([[wiki/concepts/display-css]]). `[external]` Elementos inline ignoram width, height e margem vertical; `inline-block` também resolve. A dica de depurar com `border` tem custo: a borda soma ao tamanho da caixa (com o `box-sizing: content-box` padrão); `outline` não soma (https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing).

## Deslocar a caixa sem mexer no fluxo

Em [[wiki/sources/position-css-static-relative-absolute-fixed-sticky]], `position: relative` com `top` desloca a caixa inteira, mas a posição original continua reservada ("imagine" o contorno tracejado). Já `absolute` tira a caixa do fluxo, e o irmão sobe para ocupar o espaço. A margem empurra os vizinhos; `top` e `left` não empurram. Ver [[wiki/concepts/css-position]].

## Na NLW #1 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]]: toda caixa tem largura, altura, padding, border, margin, cor e fundo, e "pode ter uma caixa dentro de outra caixa". Centraliza o conteúdo com `width: 90%; max-width: 1100px; margin: 0 auto` e zera os espaços do navegador com `* { margin: 0; padding: 0 }`. `[skill: tech-mentor-frontend]` o reset usual hoje é `box-sizing: border-box`, ausente na aula.

## Na NLW #1, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] mostra que, com o padrão `content-box`, o `padding: 64px` do formulário soma à largura: "ele tende a aumentar o tamanho da sua caixa". Com `box-sizing: border-box` a largura vai até a borda e o padding fica dentro, porque "uma caixa ela é medida nas suas bordas" (a caixa de papelão com uma garrafinha). Ele aplica `border-box` a `*` no `main.css`, "como se eu estivesse resetando o comportamento padrão do CSS", o reset que a skill recomendava no dia 1.

## Margin fora, padding dentro (módulo de front-end do FrontPUSH)

Em [[wiki/sources/frontpush-box-model-margin-padding-display-unidades]], [[wiki/entities/nasser|Násser]] repete "tudo são caixinhas" com uma `section.container` de três `div.item` e o conselho "coloca borda na div para poder você enxergar o elemento". `margin` é "espaçamento fora da caixa", `padding` "da parte de dentro", ambos por lado ou em [[wiki/concepts/shorthand-css|shorthand]] no sentido horário. A aula não fala de `box-sizing` nem de colapso de margens. `[external]` Com `content-box`, o padding soma à largura; margens verticais entre irmãos se fundem na maior em vez de somar: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_box_model/Mastering_margin_collapsing.

## Key sources

- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
- [[wiki/sources/classes-e-ids-no-css]] — reset universal com border-box; inline x block no link de botão
- [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]] — reset de margin/padding e `box-sizing: border-box`
- [[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]] — tudo é caixa; width, height, padding, margin, border, radius; quatro lados; sem box-sizing
- [[wiki/sources/principais-propriedades-css-color-background-font]]: margin 0 auto; link forçado a bloco para usar o box model; border como printf
- [[wiki/sources/position-css-static-relative-absolute-fixed-sticky]]: relative mantém o espaço da caixa; absolute o libera
- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: margin auto, max-width e reset com `*`
- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: content-box x border-box; reset global
- [[wiki/sources/frontpush-o-que-e-html-linguagem-de-marcacao-tags-semantica]]: "todas essas tags aqui são caixas" (section, header, footer, nav, div); "tudo no final são caixinhas"
- [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]: borda `2px solid green` mostra a caixa do `header`; "tudo são caixinhas, tudo é div"
- [[wiki/sources/frontpush-box-model-margin-padding-display-unidades]]: margin x padding com container e itens; borda para enxergar; sem box-sizing
- [[wiki/sources/frontpush-position-css-relative-absolute-coordenadas]]: `padding-top` do pai ainda empurra o filho `absolute` sem `top` (static position); com `top: 0`, não
