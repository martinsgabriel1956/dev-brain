---
type: concept
title: "Listas no HTML (ul, ol, li) e list-style"
aliases: ["ul", "ol", "li", "lista não ordenada", "lista ordenada", "list-style", "list-style-type"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 6
tags: [html, css, listas, menu, acessibilidade, frontend]
skill: tech-mentor-frontend
status: stub
---

# Listas no HTML (ul, ol, li) e list-style

`ul` é a lista não ordenada (marcador de bolinha ou quadradinho), `ol` a ordenada (números, romanos, letras), e cada item é um `li`. Para [[wiki/entities/nasser|Násser]], é "diferença semântica de tags", com pré-definições que o CSS muda depois. O menu típico é `header` > `nav` > `ul` > `li` > `a` ([[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]). Ver [[wiki/concepts/html-semantico]].

## list-style

`list-style: none` tira o marcador, `square` troca por quadrado, e sem nada volta a bolinha; numa `ol`, aparece 1, 2, 3 ([[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]). O marcador vem da folha padrão do navegador ([[wiki/concepts/estilos-padrao-do-navegador-e-reset]]).

`[external]` O Safari com VoiceOver deixa de anunciar como lista uma `ul` com `list-style: none`; quando a contagem de itens importa, repõe-se com `role="list"`: https://developer.mozilla.org/en-US/docs/Web/CSS/list-style#accessibility. Ver [[wiki/concepts/acessibilidade]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]], `ul.items-grid > li` gerado com `items.map(item => <li key={item.id}>...)`.

## Menu como lista aninhada no Sass (FrontPUSH)

Em [[wiki/sources/frontpush-nesting-aninhamento-sass]], `ul.list` > `li` > `a` é a estrutura do menu, estilizada com `list-style: none` e aninhamento no SCSS.

## Na NLW #2, dia 3 (Diego Fernandes)

`options.map(...)` gerando `<option key value>`, `teachers.map(...)` gerando `TeacherItem key={teacher.id}`; key duplicada no `scheduleItems` por usar o dia da semana. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]].

## Key sources

- [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]: ul x ol, menu com ul/li, list-style none/square
- [[wiki/sources/frontpush-seletores-css-filho-irmao-atributo-nth-child-pseudo-elements]]: `li:nth-child(n)` numa `ul` de três itens
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: ul/li gerados por map com key
- [[wiki/sources/frontpush-flexbox-pratica-1-layout-youtube-estrutura-html]]: menu como `ul.nav-menu` > `li.nav-item` > `a.nav-link`
- [[wiki/sources/frontpush-nesting-aninhamento-sass]]: menu `ul > li > a` no Sass
- [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]]: NLW #2, Diego, dia 3: map com key no Proffy
