---
type: source
title: "Justify-content e align-items: alinhar os flex-itens, e um parêntese sobre box-sizing (FrontPUSH, módulo de Flexbox)"
aliases: ["FrontPUSH flexbox aula 04", "Justify-content & Align-items FrontPUSH", "aula 04 módulo Flexbox FrontPUSH"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, flexbox, justify-content, align-items, box-sizing, alinhamento, centralizar, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-justify-content-align-items-box-sizing.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Justify-content e align-items: alinhar os flex-itens, e um parêntese sobre box-sizing (FrontPUSH, módulo de Flexbox)

## TL;DR

Aula 04 do módulo de [[wiki/concepts/flexbox]] do [[wiki/entities/frontpush|FrontPUSH]], de [[wiki/entities/nasser|Násser]]. Mais duas propriedades do flex-container ([[wiki/concepts/flex-container-e-flex-item]]):

- **Errata da aula 03**: "eu coloquei inverse e o certo é reverse" (`flex-wrap: wrap-reverse`).
- **`justify-content`** ("quesito horizontal"): `flex-start` (padrão), `center`, `flex-end`, `space-between`, `space-around`. Ele usa mais `center` e `space-between`; recomenda `space-around` para menu responsivo porque "você não precisa colocar o padding".
- **`align-items`** ("caráter vertical"): `stretch`, `flex-start`, `center`, `flex-end`, `baseline`. Diz que o padrão é `flex-start`; o padrão é `stretch` (ver Precisões).
- **"O combo desses três"**: `display: flex` + `justify-content: center` + `align-items: center` no `body` para centralizar tudo, como "naqueles meus projetos do YouTube".
- **Parêntese de `box-sizing: border-box`**, que ele põe "em todos os projetos" para "dar prioridade para a caixa e não para o conteúdo" ([[wiki/concepts/box-model]]).

## Key Claims

### Errata: wrap-reverse

- "Eu fui lá ver minha aula, que eu sempre dou uma confere [...]: aqui eu coloquei inverse e o certo é reverse." Com `wrap-reverse`, "ele só quebra de maneira reversa". Corrige [[wiki/sources/frontpush-flex-direction-flex-wrap-flex-flow]].

### Justify-content

- "Você vai dizer para os flex-itens como eles têm que se organizar no quesito horizontal."
- Padrões ao ligar o `display: flex`: "a gente sabe que flex-direction é sempre row, e aqui o justify-content é sempre flex-start".
- Demo com 4 itens e `max-height: 100px` em vez de `height: 100%`. `flex-start`, `center` e `flex-end`: "alinha à esquerda, alinha ao centro, alinha à direita".
- "A que eu mais utilizo do justify-content de cara é o center aqui e o space-between."
- `space-around` "deixa justamente um espacinho aqui, você não precisa colocar o padding"; "quando você está construindo um menu responsivo, é interessante você pensar no space-around".
- `space-between` "vai [...] literalmente deixar o máximo de espaço entre os flex-itens. Ele cola lá no canto", e aí "tem que colocar algum tipo de padding". Ver [[wiki/concepts/espaco-em-branco]].
- Menus responsivos voltam "tanto no caso da Nubank como nos nossos projetinhos" ([[wiki/entities/nubank]]).
- Slide (print enviado com a transcrição): "Alinha os itens flex no container de acordo com a direção. A propriedade só funciona se os itens atuais não ocuparem todo o container"; `space-around` tem espaços do meio "duas vezes maiores que o inicial e final".

### Align-items e o combo de centralizar

- "Se o justify-content ele tratava mais do caráter horizontal, o align-items ele trata mais do caráter vertical."
- "Naqueles meus projetos do YouTube, que eu quero que tudo fique no centro [...] o que eu sempre faço? Display flex. Eu venho aqui no body": o body vira flex-container, os filhos diretos viram flex-itens, e com `justify-content: center` e `align-items: center` "eu quero que você centralize na horizontal e centralize na vertical". "Sempre é o combo desses três aqui."
- Valores: `stretch` ("não está acontecendo nada [...] porque eu defini o [...] max-height"), `flex-start` ("sempre fica alinhado ao topo"), `center` ("está alinhando, gente, verticalmente"), `flex-end` ("na parte de baixo"), `baseline` ("ajusta de acordo com a baseline do conteúdo"), mostrado com `font-size: 50px` inline no item 1 e uma fonte menor no item 2. Ver [[wiki/concepts/tipografia]].
- "O padrão do sistema é o flex-start no align-items também." Ver Precisões.
- Slide: "Essa propriedade permite o tão sonhado alinhamento central no eixo vertical, algo que antes só era possível com diferentes hacks"; `stretch` é marcado como "valor padrão".

### Parêntese: box-sizing

- Com padding de 20 px em cima e embaixo e 50 px dos lados, a caixa fica "mais retangular".
- `box-sizing: border-box` diz "para a caixa meio que [...] não aumentar de tamanho a minha caixa de acordo com o tamanho do conteúdo". Tirando a propriedade, "não mudou nada" até ele mudar o texto de um item.
- "Eu sempre deixo como referência o tamanho da caixa [...] eu quero que a minha caixa fique do tamanho que eu estabeleci. Então, em todos os projetos eu sempre coloco box-sizing border-box." "O conteúdo tem que quebrar se for necessário." Ver [[wiki/concepts/box-model]] e [[wiki/concepts/estilos-padrao-do-navegador-e-reset]].

### Método

- "Sempre leia a teoria para poder entender ele da melhor forma possível." Explica as propriedades "em duplas, porque acredito que o entendimento facilita um pouquinho mais". Ver [[wiki/concepts/pratica-deliberada]].

## Entities

- [[wiki/entities/nasser]]: instrutor ("Ah, Násser", 3×).
- [[wiki/entities/frontpush]]: curso; módulo de Flexbox.
- [[wiki/entities/nubank]]: projeto em que o menu responsivo vai aparecer.
- YouTube: o canal de Násser, onde ele usa o "combo" de centralizar; sem página.

## Concepts

- [[wiki/concepts/flexbox]]
- [[wiki/concepts/flex-container-e-flex-item]]
- [[wiki/concepts/box-model]]
- [[wiki/concepts/estilos-padrao-do-navegador-e-reset]]
- [[wiki/concepts/espaco-em-branco]]
- [[wiki/concepts/tipografia]]
- [[wiki/concepts/pratica-deliberada]]

## Precisões e tensões com a wiki

- **O padrão de `align-items` é `stretch`, não `flex-start`.** `[external]` https://developer.mozilla.org/en-US/docs/Web/CSS/align-items. O próprio slide marca `stretch` como "valor padrão". Na demo, `stretch` parece não fazer nada porque o `max-height: 100px` limita a altura; sem limite (e sem `height`), os itens esticariam até a altura do contêiner.
- **Horizontal e vertical só em `row`.** Mesma ressalva da aula 02 ([[wiki/sources/frontpush-display-flex-flex-container-filhos-diretos]]): `justify-content` age no eixo principal e `align-items` no cruzado. Em `column`, se invertem.
- **`box-sizing` não trava a caixa contra o conteúdo.** `[external]` `border-box` faz `width` e `height` incluírem padding e borda; `content-box` (padrão) soma os dois por fora: https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing. Se a caixa não tem `width` declarada, ela cresce com o conteúdo nos dois modos; é o que a demo mostra ao trocar o texto do item. Texto que não cabe numa caixa de largura fixa transborda (`overflow`), não "estica" nem "quebra" por causa do `box-sizing`. O hábito de pôr `border-box` em todo projeto (geralmente em `*, *::before, *::after`) é comum e correto.
- **`space-around` para menu.** `[external]` Para espaço igual também nas pontas, `space-evenly`; para espaço fixo entre itens sem depender da largura do contêiner, `gap`: https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content.
- **"O justify-content por padrão é o flex-direction, start".** Lapso de fala: o padrão é `flex-start`, como ele diz minutos antes.
- **O combo no `body`.** Sem altura no `body` (`min-height: 100vh`), o `align-items: center` não centraliza na vertical. Ver a aula 02.

## Open Questions

- "Eu defini o minimum-height aqui, o max-height aqui": a demo só mostra `max-height: 100px`. Ficou literal no raw ("minimum-height" pode ser ASR de `min-height`).
- A legenda termina no meio da frase ("facilita um pouquinho mais,").
- `date_published` vazio (~2022, inferido pelo resto do curso).

## Raw quotes

- "Alinha à esquerda, alinha ao centro, alinha à direita"
- "sempre é o combo desses três aqui"
- "dar prioridade para a caixa e não para o conteúdo"
