---
type: source
title: "Layout no CSS: estilo de um botão, hover e transition, flexbox e media query (FrontPUSH, módulo de front-end)"
aliases: ["FrontPUSH layout CSS aula 06", "aula 06 módulo front-end FrontPUSH", "Layout CSS FrontPUSH"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, layout, flexbox, media-query, responsivo, hover, transition, transform, border-radius, botoes, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-layout-css-botao-hover-flexbox-media-query.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Layout no CSS: estilo de um botão, hover e transition, flexbox e media query (FrontPUSH, módulo de front-end)

## TL;DR

Aula 06 do módulo de front-end do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]], curta e panorâmica: o [[wiki/concepts/css]] tem duas funções, **estilo** e **layout**.

**Estilo.** Ele monta um `button` passo a passo: `border: 0`, `background-color: blue`, `padding: 10px`, `margin-top: 10px` e [[wiki/concepts/border-radius]] de 4 px ("chanfradinho") ou 50% ("circunferência"). No `button:hover` (que ele chama de "pseudo-element"), `transform: scale` mais `transition` (1 s, depois 300 ms, `ease`) fazem o botão crescer "de maneira suave" ([[wiki/concepts/transition-e-transform-css]]). Também mostra `font-family` (Courier New) e `font-weight: bold`. Com isso, dá para "pegar o que a gente fez aqui no Figma e conseguir traduzir para o CSS de maneira plena" ([[wiki/concepts/handoff-design-dev]]).

**Layout.** "Um layout para o desktop e um layout para o mobile" também é CSS. Ele cita Flexbox, Grid Layout e "Grid System com Sass, utilizando float". Depois aplica `display: flex` num container (os filhos diretos viram itens, `flex-direction` padrão `row`) e, num `@media screen and (max-width: 960px)`, troca para `column` ([[wiki/concepts/flexbox]], [[wiki/concepts/breakpoint]]). "É assim que eu faço responsividade" ([[wiki/concepts/design-responsivo]]). O detalhe fica para os módulos de Flexbox, Grid Layout e Grid System.

## Key Claims

### Estilizando um botão

- Seleciona o `button` "utilizando os seletores das aulas que a gente já fez" ([[wiki/concepts/seletores-css]]). `border: 0` "tirou a borda"; `background-color: blue`; `padding: 10px` porque "o button está muito apertado"; `margin-top: 10px` porque "está colado ali" ([[wiki/concepts/box-model]]).
- **Cantos**: 4 px "para ele chanfrar"; 50% para "uma circunferência". Ver [[wiki/concepts/border-radius]] e Tensões.
- `color: white`. Ver [[wiki/concepts/botoes-em-interfaces]].

### Hover, transform e transition

- **Hover**: "quando eu passe o mouse em cima desse botão, ele cresça de tamanho", com `button:hover`, que "vai especificar quais são as características do botão que você quer que modifique". Ver [[wiki/concepts/pseudo-classe-css]].
- **transform**: a escala "aumente 5%, 0.05", depois 1.2. Ver [[wiki/concepts/transition-e-transform-css]].
- **transition**: "para poder isso acontecer de maneira suave", 1 s `ease`, depois 300 ms.

### Do Figma ao CSS

- O CSS tem "a característica de estilizar tudo", então dá para traduzir o design do [[wiki/entities/figma]] "de maneira plena, porque é espaçamento, são caixinhas", com fundo de cor, de imagem ([[wiki/concepts/background-css]]) ou `linear-gradient`, e tipografia (`font-family: Courier New`; `font-weight: bold` para "um peso tipográfico maior", ver [[wiki/concepts/peso-tipografico]]). Ver [[wiki/concepts/handoff-design-dev]].

### Layout: desktop e mobile

- "Esse lance de a gente construir um layout para o desktop e um layout para o mobile [...] você também faz com o CSS". Ferramentas: "CSS Flexbox e o CSS Grid Layout, ou Grid System com Sass, utilizando float" ([[wiki/concepts/pre-processador-css]], [[wiki/concepts/grid-de-colunas]]). Cada uma tem módulo próprio no curso.
- Exemplo: `div.container` com `div.item`, que "estão um embaixo do outro"; ele quer lado a lado no desktop e "em coluna" no mobile, "esse toggle".

### display: flex

- `display: flex` no container: "pega todos os seus filhos diretos, eles vão virar flex-itens e o container é o flex pai", e "automaticamente um vai ficar do lado do outro". O `flex-direction` padrão é `row`, "linha em inglês". Ver [[wiki/concepts/flexbox]].

### Media query: coluna abaixo de 960 px

- `@media screen and (max-width: 960px) { .container { flex-direction: column } }`. Leitura: "CSS, [...] você vai prestar atenção nesse trecho de código somente quando a tela do dispositivo for menor ou igual a 960 pixels [...] do contrário, ele só vai ler esse". Ver [[wiki/concepts/breakpoint]].
- Teste no Inspecionar do Chrome: com 1015 px os itens ficam em linha (fundo vermelho na demo); a 960, verde e em coluna. Um corte na gravação: "o Chrome estava salvando o arquivo no cache".
- "Uma das formas que eu faço responsividade com o CSS é dessa forma." No mobile também se ajusta o resto, como diminuir a imagem. Ver [[wiki/concepts/design-responsivo]].

### Estilo e layout

- "O CSS não tem só a função de estilização, mas ele também tem a função de layout do seu site." A aula só "enfatiza"; há aulas específicas.

## Entities

- [[wiki/entities/nasser]]: instrutor; diz o nome.
- [[wiki/entities/frontpush]]: curso; aula 06 do módulo de front-end; cita os módulos de Flexbox, Grid Layout e Grid System com Sass.
- [[wiki/entities/figma]]: origem do design a traduzir para CSS.

## Concepts

- [[wiki/concepts/transition-e-transform-css]] (novo)
- [[wiki/concepts/flexbox]]
- [[wiki/concepts/breakpoint]]
- [[wiki/concepts/design-responsivo]]
- [[wiki/concepts/border-radius]]
- [[wiki/concepts/pseudo-classe-css]]
- [[wiki/concepts/botoes-em-interfaces]]
- [[wiki/concepts/handoff-design-dev]]
- [[wiki/concepts/box-model]]
- [[wiki/concepts/peso-tipografico]]
- [[wiki/concepts/pre-processador-css]]
- [[wiki/concepts/grid-de-colunas]]
- [[wiki/concepts/css]]

## Tensões com a wiki

- **`:hover` não é pseudo-element.** É [[wiki/concepts/pseudo-classe-css|pseudo-classe]] (um dois-pontos, um estado). A aula 04 do mesmo módulo já separava os dois ([[wiki/sources/frontpush-seletores-css-filho-irmao-atributo-nth-child-pseudo-elements]]).
- **"Aumente 5%, 0.05".** `[external]` `transform: scale(0.05)` reduziria o botão a 5% do tamanho; aumentar 5% é `scale(1.05)`. Pelo "olha lá, ele está aumentando", o valor digitado deve ter sido 1.05 (inferência): https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/scale.
- **"Chanfradinho".** `border-radius` arredonda; chanfro é corte reto, que no CSS se faz com `clip-path` (ou `corner-shape: bevel`, ainda experimental). Na wiki, botão chanfrado é uma forma à parte ([[wiki/concepts/formas-de-botoes]]). E `50%` num botão retangular dá elipse, não circunferência; o "pill" vem de um raio grande em px ([[wiki/concepts/border-radius]]).
- **Desktop-first.** A demo usa `max-width` (o padrão é desktop, o mobile é exceção). `[skill: tech-mentor-frontend]` O recomendado é mobile-first, com `min-width`; e, quando o que importa é o espaço do componente e não a tela, container queries (`@container (min-width: …)`). Já registrado em [[wiki/concepts/breakpoint]] (seção Mobile-first x desktop-first). O 960 px é o mesmo breakpoint da aula de grids do curso.
- **Float para grid é legado.** `[external]` Float era o recurso para layouts em colunas antes do Flexbox e do Grid; hoje fica para texto em volta de imagem. Flexbox é unidimensional, Grid bidimensional: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Floats.
- **Animação e acessibilidade.** `[skill: tech-mentor-frontend]` Animar `transform` e `opacity` roda no compositor e não força layout, por isso a escolha da aula é boa; mas o hover que cresce deve respeitar `@media (prefers-reduced-motion: reduce)`. A aula não diz se a `transition` estava no `button` ou no `:hover`: no `:hover`, ela só vale na entrada, e a volta é instantânea.
- **"O Chrome estava salvando o arquivo no cache."** Provável cache do CSS durante a gravação; `[external]` Ctrl+Shift+R ou "Disable cache" no DevTools (aba Network, com o DevTools aberto) evitam isso.

## Open Questions

- "Essa caixa aqui tem um chão" ficou literal (talvez "um chanfro" ou "um chapado").
- Módulos de Flexbox, Grid Layout e Grid System com Sass ainda não estão na wiki.
- `date_published` vazio (~2022, inferido pelas aulas vizinhas).

## Raw quotes

- "o CSS não tem só a função de estilização, mas ele também tem a função de layout do seu site"
- "pega todos os seus filhos diretos, eles vão virar flex-itens"
- "somente quando a tela do dispositivo for menor ou igual a 960 pixels"
