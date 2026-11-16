---
type: source
title: "Flexbox, prática 2: um desafio de layout e as dicas de estrutura de divs (FrontPUSH, módulo de Flexbox)"
aliases: ["FrontPUSH flexbox aula 11", "Flexbox Prática 2 FrontPUSH", "desafio de flexbox FrontPUSH"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, flexbox, design-responsivo, media-query, menu, projeto-pratico, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-flexbox-pratica-2-desafio-estrutura-de-divs.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Flexbox, prática 2: um desafio de layout e as dicas de estrutura de divs (FrontPUSH, módulo de Flexbox)

## TL;DR

Aula 11 do módulo de [[wiki/concepts/flexbox]] do [[wiki/entities/frontpush|FrontPUSH]], de [[wiki/entities/nasser|Násser]]. Não tem código: é um layout-desafio, "um pouco mais acima desse aqui do YouTube", que "fica para exercício", com as "principais sacadas" de estrutura. O layout em si não é descrito na fala.

- **Menu**: o mesmo, com variações: links no centro, botões de call to action ([[wiki/concepts/botoes-em-interfaces]]); com muitos itens, media query para esconder e trocar por um ícone de hambúrguer, como no projeto do [[wiki/entities/nubank]] ([[wiki/concepts/mobile-navegacao]]).
- **Estrutura**: container no grid (1.200 ou 1.440 px) → div com três flex-itens (cards) → dentro de cada um, imagem e texto, ou tudo direto "orientad[o] em coluna" ([[wiki/concepts/flex-container-e-flex-item]]).
- **Responsivo**: "estrutura ABC [...] vai quebrar em ABC em coluna", trocando `row` por `column` numa media query, "ou simplesmente adiciona um flex-wrap e configura o flex-basis" ([[wiki/concepts/design-responsivo]], [[wiki/concepts/flex-grow-shrink-basis]]).
- **Flex dentro de flex**: os itens precisam ser "filhos direto" do pai flex; onde há um filho só, `display: block` resolve.

## Key Claims

### O desafio

- "Estou bolando alguns layouts que são mais difíceis de serem executados com o Flexbox, porque você tem que pensar de como você vai compor a estrutura de divs."
- "Se você quiser praticar o Flexbox, tente fazer esse carinha aqui." "Eu posso estar fazendo esse exercício aqui posteriormente, mas fica para exercício, para vocês treinarem." Ver [[wiki/concepts/pratica-deliberada]].

### O menu

- "A parte do menu não muda absolutamente nada"; dá para pôr os links "no centro" e "alguns botões de call to action".
- "Dá para fazer também só com o Flexbox, só que você tem que utilizar [...] media query para poder sumir com os itens." "Como tem poucos itens, não precisa [...] sumir e aparecer com um ícone de hambúrguer. Quanto mais coisas você coloca no menu, mais você precisa [...] tirar uma div e adicionar uma outra." Ver [[wiki/concepts/mobile-navegacao]] e [[wiki/concepts/breakpoint]].
- Referência: "o projeto do Nubank que eu fiz [...] eu já tenho mostrando como se dá isso" ([[wiki/entities/nubank]]).

### Estrutura HTML

- "Uma div container englobando todos os elementos de acordo com o grid que você estabeleceu, seja ele de 1.200 pixels, 1.440 pixels." Ver [[wiki/concepts/grid-de-colunas]].
- Dentro, "uma div [...] onde nós temos três flex-itens". Em cada item, uma div para "a imagem do thumb" e outra para o texto, "ou simplesmente coloca aqui as três direto e coloca elas orientadas em coluna".

### Colunas que quebram

- "Sempre pense no flexbox como em colunas primeiro": uma coluna para cada bloco, "de forma que, quando eles quebrem, [...] estrutura ABC, e vai quebrar em ABC em coluna".
- Dois caminhos: "troca de row para column, utilizando o media query, ou simplesmente adiciona um flex-wrap e configura o flex-basis desses três aqui". Ver [[wiki/sources/frontpush-flex-direction-flex-wrap-flex-flow]] e [[wiki/sources/frontpush-flex-basis-tamanho-base-flex-itens]].

### Flex dentro de flex

- Os três itens internos "precisam ser filhos direto desse azul aqui, para poder funcionar"; "aqui eu tenho dois filhos e aqui eu tenho três filhos". Ver [[wiki/concepts/flex-container-e-flex-item]].
- "Você pode colocar ele em display block, então um filho só consegue resolver isso aqui." "Uma div, uma aqui dentro da outra."
- "Depois no layout fica bem mais fácil de executar."

## Entities

- [[wiki/entities/nasser]]: instrutor.
- [[wiki/entities/frontpush]]: curso; segunda prática do módulo de Flexbox.
- [[wiki/entities/nubank]]: projeto em que o menu responsivo com hambúrguer já foi mostrado.

## Concepts

- [[wiki/concepts/flexbox]]
- [[wiki/concepts/flex-container-e-flex-item]]
- [[wiki/concepts/flex-grow-shrink-basis]]
- [[wiki/concepts/design-responsivo]]
- [[wiki/concepts/breakpoint]]
- [[wiki/concepts/mobile-navegacao]]
- [[wiki/concepts/botoes-em-interfaces]]
- [[wiki/concepts/grid-de-colunas]]
- [[wiki/concepts/pratica-deliberada]]

## Precisões e tensões com a wiki

- **Prometido x entregue.** A aula 10 terminou com "na próxima aula [...] a gente vai estar agora codando, estilizando" o layout do YouTube ([[wiki/sources/frontpush-flexbox-pratica-1-layout-youtube-estrutura-html]]). A aula 11 passa a um segundo layout, sem código. O CSS do YouTube pode estar em outra aula ou ter ficado de fora.
- **Linhas ou colunas primeiro?** Na aula 10, "em flexbox a gente sempre pensa em linhas"; aqui, "sempre pense no flexbox como em colunas primeiro". As duas falas descrevem o mesmo método (dividir a linha em colunas lado a lado); a wiki registra as duas.
- **`wrap` x media query.** `[external]` Com `flex-wrap` + `flex-basis`, a troca é intrínseca (depende do espaço, não de um breakpoint) e passa por um estado intermediário (dois em cima, um embaixo); com a media query, a troca é explícita, de três colunas para uma. Para três colunas que nunca ficam 2 + 1, grid com `auto-fit`/`minmax` ou uma media query são mais previsíveis ([[wiki/concepts/css-grid]]).
- **Menu hambúrguer.** `[external]` Esconder e mostrar os itens pede, além da media query, um controle que abra o menu: um `<button>` com `aria-expanded` e `aria-controls` (ou o truque do checkbox com `:checked`, que Násser já mostrou no YouTube, segundo [[wiki/entities/nasser]]): https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-expanded. Ver [[wiki/concepts/acessibilidade]].
- **"Melhor responsabilidade".** Provável lapso por "responsividade"; ficou literal no raw.

## Open Questions

- Como é o layout do desafio? A fala só o aponta na tela.
- "Inverte sobre produtos e contato" e "Está tô, pessoal": literais no raw.
- `date_published` vazio (~2022, inferido pelo resto do curso).

## Raw quotes

- "você tem que pensar de como você vai compor a estrutura de divs"
- "estrutura ABC, e vai quebrar em ABC em coluna"
- "depois no layout fica bem mais fácil de executar"
