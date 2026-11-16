---
type: source
title: "Box model no CSS: margin, padding, bloco e inline, width, height e unidades de medida (FrontPUSH, módulo de front-end)"
aliases: ["FrontPUSH box model aula 05", "aula 05 módulo front-end FrontPUSH", "Box Model CSS FrontPUSH"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, box-model, margin, padding, shorthand-css, display, inline-block, unidades-de-medida, viewport, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-box-model-margin-padding-display-unidades.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Box model no CSS: margin, padding, bloco e inline, width, height e unidades de medida (FrontPUSH, módulo de front-end)

## TL;DR

Aula 05 do módulo de front-end do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]], depois da de [[wiki/sources/frontpush-seletores-css-filho-irmao-atributo-nth-child-pseudo-elements|seletores]]. Tese: "tudo aqui é caixa", porque cada marcação tem a sua tag e "a sua tag é uma caixinha" ([[wiki/concepts/box-model]]). Monta uma `section.container` com três `div.item`, cada uma com um `h1` ("caixa um", "caixa dois", "caixa três"), e repete o conselho "coloca borda na div para poder você enxergar o elemento".

- **margin**: "espaçamento fora da caixa". `margin-top` em todos os itens, depois só no primeiro com `:nth-child`. Shorthand `margin: 12px 24px`.
- **padding**: "espaçamento da parte de dentro", com 1, 2 ou 4 valores "no sentido horário" (top, right, bottom, left), igual às quatro propriedades separadas ([[wiki/concepts/shorthand-css]]).
- **display**: block, inline e inline-block, que "pega dos dois mundos" ([[wiki/concepts/display-css]]).
- **width e height**.
- **Unidades** ([[wiki/concepts/unidades-de-medida-css]]): fixas (px, que ele prefere; pt; polegadas) e relativas (`%` do pai, `vw`/`vh` da tela, "100vh [...] pega a tela inteira", ver [[wiki/concepts/unidades-de-viewport]]).

Erro principal: chama `h1` de elemento de linha. Mesmo tema da aula de box model do módulo Básico CSS ([[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]]), com outro exemplo.

## Key Claims

### Tudo são caixinhas

- O CSS serve para modificar "a cor, [...] o posicionamento, [...] o espaçamento, [...] a fonte, tipografia". "Pelo fato do HTML ser uma linguagem de marcação, toda marcação tem a sua respectiva tag, e a sua tag é uma caixinha, é uma div." Ver [[wiki/concepts/box-model]].
- "Independente de ser section, independente de ser div, independente de ser texto, sempre é uma caixinha."

### Montando o exemplo

- `<section class="container">` com três `<div class="item">`, cada um com um `<h1>`. Estilo em `section .container` e `.item` com `border: solid green`. "Eu sempre falo isso para todos os meus alunos, coloca borda na div para poder você enxergar o elemento." Uma `div` vazia aparece como uma linha, porque "não tem conteúdo nenhum dentro dela".

### margin

- **"Espaçamento fora da caixa"**, por lado: `margin-top`, `-right`, `-bottom`, `-left`. `margin-top: 24px` no `.item` espaça todas as caixas ("Nossa, eu não entendi, porque todos espaçaram"); com `:nth-child` só a primeira recebe, depois com 48 px ([[wiki/concepts/pseudo-classe-css]]).
- **"Modelo contraído"**: `margin: 12px 24px` = 12 px em cima e embaixo, 24 px dos lados. Ver [[wiki/concepts/shorthand-css]].

### padding e o sentido horário

- **"Espaçamento da parte de dentro"**, "segue a mesma lógica". Borda `1px solid pink` no `h1` para mostrar o efeito.
- **Valores**: um (`48px`) vale para os quatro lados; dois (`48px 12px`), 48 em cima e embaixo, 12 dos lados; quatro (`48px 12px 24px 32px`), "o primeiro é top, o segundo é right, o terceiro é bottom e esse aqui é left, ele sempre faz assim, no círculo, no sentido horário". É "a mesma coisa" que `padding-top: 48px; padding-right: 12px; padding-bottom: 24px; padding-left: 32px` (ele se confunde ao digitar e corrige o bottom).
- "Tem formas contraídas, [...] e formas completas"; "de tanto você fazer, você vai pegar isso aqui", porque o box model "você está fazendo o tempo inteiro".

### Bloco, inline e inline-block

- **Bloco x linha**: "tem alguns elementos que são elementos de bloco, e tem alguns elementos que são padrões de linha", os de texto, que "seguem um pouco o fluxo de texto"; propriedades de caixa nesses "não vão funcionar direito". Exemplos que ele dá de "elemento de linha": "um h1, é um link, é um span". Ver Tensões.
- **display** "nada mais é de como a caixinha se comporta"; `display: block` "é a imensa maioria" e aceita margin e padding "normal". Em `inline`, "eles ignoraram as características de bloco, que são as características de espaçamento"; em `inline-block`, "ele meio que pega dos dois mundos" e o espaçamento volta. Ver [[wiki/concepts/display-css]].
- **Link com width**: dar 250 px a um link "é complicado"; "é melhor deixar o link do tamanho do conteúdo", porque ele segue "a linha de conteúdo, por isso que ele é mais inline".

### width e height

- "Width, como o próprio nome já diz, largura, height, altura": 250 px de altura no exemplo.

### Medidas fixas e relativas

- **Fixas**: pixel "é o que eu mais utilizo", porque "a gente está em uma tela bem mais próxima"; `pt` "também funciona"; "eu acredito que tem polegadas também" (a caixa fica "bem maior"). Ver [[wiki/concepts/unidades-de-medida-css]].
- **Porcentagem** é relativa "do pai": o `h1` "é filho da div class-item, ele vai pegar 250% do pai".
- **Viewport units**: `vw` é a largura da tela ("375 pixels" num celular), `vh` a altura. "Em muitas divs eu coloco, por exemplo, 100vh [...] pega a tela inteira"; com `80vh` "ela ficou 80%". Ver [[wiki/concepts/unidades-de-viewport]].
- **Fecho**: um panorama sem "flodar vocês de informações"; um "projetinho prático" virá para exercitar.

## Entities

- [[wiki/entities/nasser]]: instrutor; diz o nome.
- [[wiki/entities/frontpush]]: curso; aula 05 do módulo de front-end.

## Concepts

- [[wiki/concepts/box-model]]
- [[wiki/concepts/shorthand-css]]
- [[wiki/concepts/display-css]]
- [[wiki/concepts/unidades-de-medida-css]]
- [[wiki/concepts/unidades-de-viewport]]
- [[wiki/concepts/pseudo-classe-css]]

## Tensões com a wiki

- **`h1` não é inline.** `[external]` Os títulos `h1`–`h6` são de bloco por padrão; o link (`a`) e o `span` é que são inline: https://developer.mozilla.org/en-US/docs/Glossary/Block-level_content. A própria demo da aula usa `h1` dentro das caixas e aplica padding nele sem problema. A aula anterior do mesmo curso já os tratava como bloco ([[wiki/sources/frontpush-o-que-e-html-linguagem-de-marcacao-tags-semantica]]).
- **Inline não "ignora o espaçamento" todo.** `[external]` Num elemento inline, `width` e `height` não valem e a `margin` vertical é ignorada; a `margin` e o `padding` horizontais funcionam, e o `padding` vertical é pintado mas não empurra as linhas vizinhas: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_display/Block_and_inline_layout_in_normal_flow. É por isso que o link-botão costuma virar `inline-block`, como já registra [[wiki/concepts/display-css]].
- **`%` de altura precisa de pai com altura.** `[external]` `height: 250%` só tem efeito se o pai tiver altura definida; senão vira `auto`. E `padding`/`margin` em `%` se calculam sobre a **largura** do bloco que contém, até nos lados de cima e de baixo: https://developer.mozilla.org/en-US/docs/Web/CSS/percentage.
- **Polegada CSS não é polegada física.** `[external]` `1in` = 96 px CSS = 72 pt, um valor fixo, não medido na tela; `pt`, `in` e `cm` fazem sentido em folhas de impressão. Para tela, `px` e as relativas (`rem`, `%`, `vw`): https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Values_and_units.
- **Padding aumenta a caixa.** `[external]` Com o `box-sizing: content-box` padrão, `width: 250px` + `padding: 48px` dá 346 px de largura visível; o reset `* { box-sizing: border-box }` das aulas de CSS do mesmo curso evita isso ([[wiki/concepts/box-model]]). Esta aula não fala de `box-sizing`.
- **Margens verticais colapsam.** `[external]` Entre irmãos, `margin-bottom` de um e `margin-top` do seguinte se fundem na maior das duas, em vez de somar; padding e borda não colapsam: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_box_model/Mastering_margin_collapsing. Não aparece na aula e explica espaçamentos "que não somam" no projeto prático.
- **`100vh` no celular.** Já registrado em [[wiki/concepts/unidades-de-viewport]]: a barra do navegador faz `100vh` passar da tela visível; `100dvh` resolve.

## Open Questions

- "Deixe-me colocar aqui errado" e "scoop bottom" ficaram literais; o sentido não é claro (prováveis "deixa eu corrigir" e "isso, bottom").
- O "projetinho prático" prometido ainda não está na wiki.
- `date_published` vazio (~2022, inferido pelas aulas vizinhas).

## Raw quotes

- "coloca borda na div para poder você enxergar o elemento"
- "ele sempre faz assim, no círculo, no sentido horário"
- "ele meio que pega dos dois mundos"
