---
type: source
title: "Flex-direction, flex-wrap e flex-flow: direção, quebra de linha e o princípio do responsivo (FrontPUSH, módulo de Flexbox)"
aliases: ["FrontPUSH flexbox aula 03", "Flex-direction & Flex-wrap FrontPUSH", "aula 03 módulo Flexbox FrontPUSH"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, flexbox, flex-direction, flex-wrap, flex-flow, media-query, design-responsivo, max-width, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-flex-direction-flex-wrap-flex-flow.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Flex-direction, flex-wrap e flex-flow: direção, quebra de linha e o princípio do responsivo (FrontPUSH, módulo de Flexbox)

## TL;DR

Aula 03 do módulo de [[wiki/concepts/flexbox]] do [[wiki/entities/frontpush|FrontPUSH]], de [[wiki/entities/nasser|Násser]]. Três propriedades do flex-container ([[wiki/concepts/flex-container-e-flex-item]]):

- **`flex-direction`**: `row` (padrão), `row-reverse`, `column`, `column-reverse`. Trocar `row` por `column` numa media query (`max-width: 960px`) é "o princípio do sistema responsivo" ([[wiki/concepts/design-responsivo]], [[wiki/concepts/breakpoint]]).
- **`flex-wrap`**: `nowrap` (padrão, os itens transbordam e aparece barra de rolagem), `wrap` (quebra no limite do container) e `wrap-reverse` (quebra "da maneira contrária"). Resolve o gancho da aula 02.
- **`max-width` em vez de `width`**: o container com `max-width: 700px` "ajusta"; com `width: 700px`, não. "É uma boa prática" usar `max-width`, `min-width`, `max-height` e `min-height`.
- **`flex-flow`**: "simplesmente um atalho" de `flex-direction` + `flex-wrap` ([[wiki/concepts/shorthand-css]]); ele prefere escrever as duas.
- Pedido recorrente: refazer "sem colar de mim, olhando a teoria" ([[wiki/concepts/pratica-deliberada]]).

## Key Claims

### Flex-direction

- O `flex-direction` diz "literalmente, a direção dos flex-itens. Por padrão ela é row, que é linha". Por isso, com `display: flex`, os itens ficam lado a lado, e declarar `row` "meio que não vai mudar nada".
- `row-reverse`: "como o próprio nome já diz, ele vai inverter a ordem dos itens". `column`: "ele meio que volta a ser display-block". `column-reverse` inverte a coluna.
- Slide (print enviado com a transcrição): "Define a direção dos flex itens. Por padrão ele é row (linha), por isso quando o display: flex; é adicionado, os elementos ficam em linha, um do lado do outro", com diagramas dos quatro valores.

### Flex-direction e media query

- "É extremamente utilizada, pelo menos por mim, é uma das formas que eu faço para poder conseguir uma boa responsividade": itens "em linha, totalmente enfileirados, e depois eles ficam enfileirados em coluna". Ver [[wiki/concepts/design-responsivo]].
- Media query é "literalmente um recurso do CSS, onde eu consigo aplicar estilos para uma determinada faixa de resolução". Demo: `@media (max-width: 960px)` com o `.container` em `flex-direction: column`, um estilo "que eu quero que ele leia e sobrescreva o estilo que está antes". Com 720 px, "ele vai demorar um pouquinho mais" para quebrar. Ver [[wiki/concepts/breakpoint]].
- "É esse o princípio que a gente vai aplicar para poder construir sistemas responsivos, então superguarde essa propriedade aqui."

### Flex-wrap

- "Ele vai definir se os itens devem quebrar ou não." Com vários itens, "eles passam do meu container [...] porque eu não falei que era para eles quebrarem".
- Padrões: `flex-direction: row` e `flex-wrap: nowrap`, "ou seja, não quebre". Sem `wrap`, "ele vai criar uma barra de rolagem aqui".
- Com `wrap`, "quando ele chega no limite do container e percebe que o conteúdo não consegue mais quebrar", o item desce de linha. O tamanho mínimo de cada item vem do texto ("item 1, 2, 3 e 4") mais o padding de 20 px.
- `wrap-reverse` ("wrap inverso", na fala) "simplesmente vai quebrar da maneira contrária".
- Slide: "Por padrão eles não quebram linha, isso faz com que os flex itens sejam compactados além do limite do conteúdo"; `wrap` "quebra a linha assim que um dos flex itens não puder mais ser compactado"; `wrap-reverse` quebra "na direção contrária, ou seja para a linha acima".

### Max-width em vez de width

- "O meu container vai ficar responsivo, por quê? Porque eu defini o max-width, eu não defini um comprimento específico." Com `width: 700`, "ele não vai mudar o tamanho dele [...] ele vai entrar junto com a minha barra de rolagem".
- "É uma boa prática você utilizar o max-width, o min-width, o max-height e o min-height." Ver [[wiki/concepts/layout-fixo-fluido-adaptativo-responsivo]] e [[wiki/concepts/unidades-de-medida-css]].

### Flex-flow

- "Eu não utilizo muito, porque ele é simplesmente um atalho das propriedades flex-direction e flex-wrap." "Eu prefiro utilizar flex-direction e flex-wrap." Ver [[wiki/concepts/shorthand-css]].
- Slide: "Você não verá muito o seu uso, pois geralmente quando mudamos o flex-direction para column, mantemos o padrão do flex-wrap que é nowrap"; exemplos `row nowrap`, `row wrap`, `column nowrap`.

### Método

- "Faça esse mesmo exercício aqui, mas sem colar de mim, olhando a teoria e aplicando"; "não deixem eu fazendo sozinho e vocês ficam de boa"; "sempre leia a teoria". Ver [[wiki/concepts/pratica-deliberada]].

## Entities

- [[wiki/entities/nasser]]: instrutor.
- [[wiki/entities/frontpush]]: curso; módulo de Flexbox.

## Concepts

- [[wiki/concepts/flexbox]]
- [[wiki/concepts/flex-container-e-flex-item]]
- [[wiki/concepts/design-responsivo]]
- [[wiki/concepts/breakpoint]]
- [[wiki/concepts/shorthand-css]]
- [[wiki/concepts/layout-fixo-fluido-adaptativo-responsivo]]
- [[wiki/concepts/unidades-de-medida-css]]
- [[wiki/concepts/acessibilidade]]
- [[wiki/concepts/pratica-deliberada]]

## Precisões e tensões com a wiki

- **Desktop-first.** `max-width: 960px` parte do desktop e sobrescreve para telas menores, como na aula 06 do módulo de front-end ([[wiki/sources/frontpush-layout-css-botao-hover-flexbox-media-query]]). `[external]` O padrão mais comum hoje é mobile-first, com `min-width`, o que deixa o CSS base mais simples: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries. Ver [[wiki/concepts/breakpoint]].
- **`-reverse` muda só a ordem visual.** `[external]` `row-reverse` e `column-reverse` invertem o que se vê, não a ordem do HTML que leitores de tela e o Tab seguem: https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction#accessibility. Ver [[wiki/concepts/acessibilidade]].
- **`column` "volta a ser display-block".** Parece, porque `align-items: stretch` (padrão) estica os itens na largura. Mas eles seguem sendo flex items: as margens verticais não colapsam, e `justify-content` passa a agir na vertical.
- **"wrap-inverse".** O rótulo do slide está errado: o valor é `wrap-reverse`; ele diz "wrap inverso". Ele mesmo corrige na abertura da aula 04 ([[wiki/sources/frontpush-justify-content-align-items-box-sizing]]): "eu coloquei inverse e o certo é reverse". `[external]` https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap.
- **"Compactados além do limite do conteúdo".** `[external]` Com `nowrap`, os itens encolhem (`flex-shrink: 1`) até o tamanho mínimo do conteúdo e só então transbordam. A barra de rolagem é da página: o container mantém `overflow: visible`.
- **Os gatilhos da quebra.** Com `max-width: 960px`, a regra vale a partir de 960 px para baixo (inclusive), não "quando atingiu" 960.

## Open Questions

- "flex-direction para column, column-normal": não existe valor `column-normal`. Ele parece corrigir a si mesmo para `column` "normal" (sem reverse). Ficou literal no raw.
- `date_published` vazio (~2022, inferido pelo resto do curso).

## Raw quotes

- "é deste princípio que parte a gente quebrar os blocos no sistema responsivo"
- "superguarde essa propriedade aqui"
- "ele é simplesmente um atalho das propriedades flex-direction e flex-wrap"
