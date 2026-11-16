---
type: source
title: "Position no CSS: relative no pai, absolute no filho e o sistema de coordenadas (FrontPUSH, módulo de front-end)"
aliases: ["FrontPUSH position aula 07", "aula 07 módulo front-end FrontPUSH", "Position CSS FrontPUSH"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, position, relative, absolute, bloco-de-contencao, layout, elementos-de-composicao, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-position-css-relative-absolute-coordenadas.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Position no CSS: relative no pai, absolute no filho e o sistema de coordenadas (FrontPUSH, módulo de front-end)

## TL;DR

Aula 07 do módulo de front-end do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]], depois da de [[wiki/sources/frontpush-layout-css-botao-hover-flexbox-media-query|layout]]. `position` também constrói layout, mas "não é muito comum": para layout, o curso usa flexbox, grid layout ou grid system com Sass ([[wiki/concepts/flexbox]]). Posição é para "essas coisas mais exóticas".

Demonstração: um `.container` com borda vermelha e um `.item` com borda verde e `max-width: 400px` ("é melhor" que `width`). Com o item em `position: absolute`, ele "fica flutuando" num "sistema de coordenadas" X/Y, desenhado no [[wiki/entities/figma]], cuja origem é o elemento relativo. Sem pai `relative`, um `top: 0` o leva ao topo da janela, ignorando o `padding-top: 100px` do container. Para ele, isso acontece porque "o body [...] vem por padrão como position relative", o que está errado. Com o container em `relative`, `top`, `left`, `right` e `bottom` contam a partir dele. Resumo: "relative fica no pai, absolute fica no filho".

Exemplos no site do FrontPUSH: as bolinhas que mudam de `top`/`left` (50/50 → 80/80 → 30/30), um "nzinho" na descrição e um selo, todos `absolute` ([[wiki/concepts/elementos-de-composicao]]). Mesmo tema da aula 06 do Básico CSS ([[wiki/sources/position-css-static-relative-absolute-fixed-sticky]]), aqui só com relative e absolute. Ver [[wiki/concepts/css-position]].

## Key Claims

### Position também é layout, mas não o comum

- O CSS, "linguagem de estilização", também é "uma linguagem de layout", com flexbox e grid. Position é "uma nova forma", mas "não é muito comum para poder a gente fazer layout assim".

### Container relative e item absolute

- `.container` com borda vermelha, `padding: 8px` ("espaçadinho, bonitinho") e `height: 300px`; `.item` com borda verde e `max-width: 400px`. Ver [[wiki/concepts/box-model]].
- Sem `top`, o item `absolute` continua respeitando o `padding-top: 100px` do container. Com `top: 0`, "por mais que eu tenha dado um padding-top [...] ele topou lá no meio". Ver Tensões.

### Um sistema de coordenadas

- `absolute` "fica flutuando, e ele sempre tem um relativo para quem ele olha, então é como se fosse um sistema de coordenadas". No [[wiki/entities/figma]], desenha eixos X e Y: o elemento relativo é "o ponto zero", e "o pai do elemento tem que ser relativo para poder ele dar o eixo de referência". Ver [[wiki/concepts/css-position]].

### Sem pai relative, a referência é a janela

- Sem `relative` no container, "quem é que ele pega como referência? O body, ou seja, essa tag aqui vem por padrão como position relative [...] a própria tela tem como position relative". Ver Tensões.
- `top: 50px` desloca 50 px do topo; `left: 50px`, 50 px da esquerda.

### Pai relative, filho absolute

- "Eu tenho que saber onde está o relativo para poder definir como absoluto." Com `position: relative` no container, ele "vai estar olhando agora para o container, que é para o pai dele", e o deslocamento passa a contar do container vermelho. Com `margin: 40px` no container, o item só acompanha quando o pai é `relative`.

### Quando usar: as bolinhas do FrontPUSH

- No site do FrontPUSH, bolinhas que passam de `top`/`left` 50/50 para 80/80 e 30/30, "livre no eixo de coordenadas", para "controlar melhor, com mais precisão". Ver [[wiki/concepts/elementos-de-composicao]] e [[wiki/concepts/transition-e-transform-css]].
- "Isso é muito comum para você construir layout? Não, é mais para construir essas coisas mais exóticas": um elemento "nessa distância específica de um outro elemento".

### top, left, right e bottom

- Ele usa quase sempre `top` e `left`, "porque eu sempre vou ficar nesse quadrante aqui", mas `right` cola à direita e `bottom` embaixo. Trocar o `20, 50` de top/left para bottom/right leva o item ao canto oposto.

### Resumo: relative no pai, absolute no filho

- "Relative fica no pai, absolute fica no filho, se você não definir quem é o relative, ele sempre vai pegar como referência a própria janela." "Isso aqui não é feito para fazer layout em si."
- No FrontPUSH, o "nzinho" da descrição e o selo são `absolute`; "o resto todo, eu utilizo o flexbox [...] ou o grid layout, ou o grid system com o Sass". "É mais como curiosidade."

## Entities

- [[wiki/entities/nasser]]: instrutor; diz o nome.
- [[wiki/entities/frontpush]]: curso; aula 07 do módulo de front-end; as bolinhas, o "nzinho" e o selo do site como exemplos de `absolute`.
- [[wiki/entities/figma]]: onde ele desenha o sistema de coordenadas.

## Concepts

- [[wiki/concepts/css-position]]
- [[wiki/concepts/box-model]]
- [[wiki/concepts/flexbox]]
- [[wiki/concepts/elementos-de-composicao]]
- [[wiki/concepts/transition-e-transform-css]]
- [[wiki/concepts/design-responsivo]]

## Tensões com a wiki

- **O `body` não é `relative` por padrão.** `[external]` Todo elemento nasce `position: static`, o `body` também. Sem ancestral posicionado, o `absolute` usa o *initial containing block*, um retângulo do tamanho da viewport na origem do documento: https://developer.mozilla.org/en-US/docs/Web/CSS/Containing_block. Mesma correção já feita para a aula do Básico CSS em [[wiki/concepts/css-position]] ("sem nenhum chega ao `body`"). Na prática ele acerta o efeito ("a própria janela"), não a causa.
- **Não precisa ser o pai, nem `relative`.** `[external]` A referência é o ancestral **posicionado mais próximo**, com qualquer valor diferente de `static` (`relative`, `absolute`, `fixed`, `sticky`) ou com `transform`/`filter`; pode ser um avô. "Relative no pai" é a convenção mais simples, porque `relative` sem deslocamento não move o pai.
- **Por que o padding valia sem `top`.** `[external]` Sem `top`/`left`, o `absolute` fica na sua *static position*, onde estaria no fluxo, por isso o padding do container ainda o afeta; definido o `top`, passa a contar do bloco de contenção. Ele observa isso sem explicar.
- **O eixo Y do CSS cresce para baixo.** Diferente do plano cartesiano "da escola", o `top` aumenta descendo; a origem é o canto superior esquerdo (da padding box do bloco de contenção).
- **Animar `top`/`left` custa layout.** `[skill: tech-mentor-frontend]` As bolinhas do site trocam `top`/`left`, o que refaz o layout a cada quadro; `transform: translate()` faz o mesmo movimento no compositor. Ver [[wiki/concepts/transition-e-transform-css]] e a seção de precisões de [[wiki/concepts/css-position]].
- **`absolute` sai do fluxo.** `[external]` O container não cresce com o filho `absolute`, por isso a demo precisou de `height: 300px`. Também não é mencionado.

## Open Questions

- "Aqui no front" (2×) ficou literal: provável "aqui no FrontPUSH" (o site mostrado), cortado na fala.
- "Esse nzinho aqui" e "esse selo" são elementos do site do FrontPUSH sem descrição na aula.
- Esta aula cobre só relative e absolute; fixed e sticky estão na aula do Básico CSS.
- `date_published` vazio (~2022, inferido pelas aulas vizinhas).

## Raw quotes

- "relative fica no pai, absolute fica no filho"
- "é como se fosse um sistema de coordenadas"
- "isso aqui não é feito para fazer layout em si"
