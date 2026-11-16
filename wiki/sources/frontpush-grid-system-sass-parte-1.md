---
type: source
title: "Grid system com Sass, parte 1: por que um grid de classes e o container fluido (FrontPUSH)"
aliases: ["Grid system com SASS", "FrontPUSH grid system Sass", "módulo de CSS Sass, aula 10", "grid system parte 1"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, sass, scss, grid-system, grid-de-colunas, container, max-width, layout-fluido, breakpoint, bootstrap, flexbox, responsividade, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-grid-system-sass-parte-1.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Grid system com Sass, parte 1 (FrontPUSH)

## TL;DR

Aula 10 do módulo de CSS Sass do [[wiki/entities/frontpush|FrontPUSH]], primeira das "aulas práticas", com [[wiki/entities/nasser|Násser]] ("Ah, Násser, por que você [...] não adapta ao tamanho da tela"). Primeira parte da construção do [[wiki/concepts/grid-system]] dele, "muitíssimo parecida com o Grid System do próprio Bootstrap" ([[wiki/entities/twitter-bootstrap]]). A biblioteca será deixada como anexo.

- **O problema do Flexbox:** no projeto [[wiki/entities/nubank]], os blocos foram feitos com `flex-grow` (2 e 1) e ajustados "no olho": "ele se aproxima, mas não tem a exatidão e precisão que [...] o sistema de grids traz". Com grid, diz-se "essa div tem 5 colunas, essa tem 7" ([[wiki/concepts/flex-grow-shrink-basis]]).
- **O princípio:** 12 colunas de 96 px e gutter de 24 = container de 1416 px; cada div tem `width` em **porcentagem** do container, para o conjunto "apertar" de forma fluida até o breakpoint, onde as colunas empilham ([[wiki/concepts/grid-de-colunas]], [[wiki/concepts/layout-fixo-fluido-adaptativo-responsivo]]).
- **Por que `max-width` fixo:** em monitores 21:9 (ultrawide), um layout 100% fluido "iria esticar em toda a tela" ([[wiki/concepts/aspect-ratio]]).
- **Mixin `responsive($device)`** do projeto Nubank: `xl` > 1440, `l` 1140–1440, `m` 960–1140, `s` < 960, `xs` < 540, escolhidos por `@if`, com `@content`. Na prática ele usa quase só o `max-width: 960px` ([[wiki/concepts/mixin-sass]], [[wiki/concepts/breakpoint]]).
- **Código até aqui:** `.container` com `max-width: $container` (variável em 1200), `margin: 48px auto`, `padding: 48px 16px`, borda vermelha de teste. Sem Flexbox nem Grid Layout. Continua na parte 2.

## Key Claims

### Flexbox × grid de colunas

- "Eu vou falar sobre responsividade, não utilizando o Flexbox ou o Grid Layout, que são dois recursos maravilhosos do próprio CSS [...] Mas eu vou falar hoje sobre o sistema de grids que eu utilizo nas minhas aplicações."
- O projeto Nubank: um container verde e duas divs azuis (texto e ilustração); `display: flex` transforma os filhos diretos em flex-items ([[wiki/concepts/flex-container-e-flex-item]]). "Eu defino um flex-grow 2 para esse e 1 para esse, eu verifico a responsividade e vejo no olho mesmo."
- "A gente não fala: 'eu quero que, no tamanho normal de Full HD, ele tenha 816 pixels [...] e [...] 576 pixels'." Com grid: "essa div tenha o tamanho de X grids [...] levando também em consideração o gutter."
- Quatro cards de 3 colunas "dá para fazer [...] com o flexbox? Lógico que dá", porque têm o mesmo tamanho; o grid facilita quando os tamanhos diferem.

### Container e breakpoints

- O padrão "que eu mais utilizo é o 1.400, aquele que se aproxima da resolução de 1.400 de container, porque eu consigo abraçar tanto resoluções maiores quanto resoluções menores" (remete à aula de grids do módulo de UI Design, [[wiki/sources/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos]]).
- "Se eu fosse fazer ele fluido, ele iria esticar em toda a tela [...] por isso eu utilizo os containers com tamanho máximo fixo e depois ele se torna fluido."
- "O sistema de grids se baseia com relação ao width em porcentagem para poder justamente o nosso sistema ficar fluido."
- Breakpoints: "se você pegar números próximos, 1200 ou então 980, não faz diferença, mas são boas divisões com base no próprio sistema de grids do Bootstrap [...] e eu adaptei para mim."
- "Na maioria das vezes, eu simplesmente aplico de 960 pixels para baixo, porque eu acho um bom breakpoint [...] que é os que eu tenho menos dor de cabeça." `@media screen and (max-width: 960px)` = "tenha um teto de 960 pixels".

### Código

- Seção `.container` com divs filhas diretas; "a gente não vai utilizar nem flexbox, nem grid layout".
- `max-width: $container` ("a variável que eu defini [...] de 1200, você pode colocar 1400 ou também que você quiser"), `margin: 48px auto` para centralizar, `padding: 48px 16px` "para que o nosso container não fique colado na nossa janela".

## Entities

- [[wiki/entities/nasser]]: instrutor (diz o nome).
- [[wiki/entities/frontpush]]: curso; aula 10 do módulo de CSS Sass, primeira prática.
- [[wiki/entities/nubank]]: projeto feito com Flexbox, contraexemplo de precisão; dono do mixin `responsive`.
- [[wiki/entities/twitter-bootstrap]]: modelo do grid system e dos breakpoints.

## Concepts

- [[wiki/concepts/grid-system]]
- [[wiki/concepts/grid-de-colunas]]
- [[wiki/concepts/layout-fixo-fluido-adaptativo-responsivo]]
- [[wiki/concepts/breakpoint]]
- [[wiki/concepts/mixin-sass]]
- [[wiki/concepts/if-else-sass]]
- [[wiki/concepts/flexbox]]
- [[wiki/concepts/flex-grow-shrink-basis]]
- [[wiki/concepts/flex-container-e-flex-item]]
- [[wiki/concepts/css-grid]]
- [[wiki/concepts/aspect-ratio]]
- [[wiki/concepts/largura-do-texto]]
- [[wiki/concepts/design-responsivo]]

## Precisões e tensões com a wiki

- **540, 960 e 1140 são larguras de container do Bootstrap 4, não breakpoints.** `[external]` No Bootstrap 4, os breakpoints são 576, 768, 992 e 1200 px, e os containers correspondentes têm `max-width` de 540, 720, 960 e 1140 (https://getbootstrap.com/docs/4.6/layout/overview/). O Bootstrap 5 acrescentou 1400 → 1320. Os números dele vêm daí, adaptados como pontos de quebra. Funciona ("não faz diferença"), mas não é o que o Bootstrap chama de breakpoint.
- **1416 ou 1200?** A conta do grid dá 1416 px, mas a variável `$container` no código vale 1200 ("você pode colocar 1400"). Com 1200, as colunas de 96 + 24 não cabem: a porcentagem continua certa, mas cada coluna fica com cerca de 81 px. A [[wiki/sources/frontpush-funcoes-sass|aula 09]] e o Figma usam 1416.
- **Sem Flexbox nem Grid, sobra float ou inline-block.** `[skill: tech-mentor-frontend]` Divs lado a lado com `width` em % e sem flex/grid só se alinham com `float` (Bootstrap 2/3) ou `inline-block`. A aula de conclusão do módulo de CSS já anunciava "Grid System com Sass, utilizando float" ([[wiki/sources/frontpush-conclusao-modulo-css-estilo-layout-animacao-documentacao]]). Floats exigem clearfix e somam o gutter na mão. O Bootstrap trocou float por flexbox na v4, em 2018.
- **Ultrawide: o motivo certo, e mais um.** Além de não esticar em 21:9, o `max-width` limita o comprimento das linhas de texto, que fica ruim de ler acima de ~75 caracteres ([[wiki/concepts/largura-do-texto]]).
- **Hoje.** `[skill: tech-mentor-frontend]` `margin-inline: auto; width: min(1416px, 100% - 32px)` faz o container numa linha; `display: grid; grid-template-columns: repeat(12, 1fr); gap: 24px` dá colunas fluidas com gutter exato; e container queries deixam um componente quebrar pelo próprio espaço, não pela janela ([[wiki/concepts/css-grid]]).
- **"Com relação à tela."** O `max-width` do container compete com o `padding` de 16 px: sem `box-sizing: border-box`, a caixa passa do teto em 32 px.

## Open Questions

- "Lá na parte de UI design do scriptwd": nome de outro módulo ou do curso? Aparece também como "Script F" na [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app|aula 02]].
- Os 17 segundos sem legenda (00:12:11–00:12:28) devem ser ele apagando o código.
- A parte 2 vai usar float, inline-block ou a função `grid()` da aula 09?

## Raw quotes

- "ele se aproxima, mas não tem a exatidão e precisão que [...] o sistema de grids traz"
- "se eu fosse fazer ele fluido, ele iria esticar em toda a tela"
- "eu simplesmente aplico de 960 pixels para baixo [...] que é os que eu tenho menos dor de cabeça"
