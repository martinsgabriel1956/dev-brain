---
type: concept
title: "head do HTML e metadados (meta charset, viewport, title)"
aliases: ["head", "<head>", "tags meta", "meta charset", "meta viewport", "metadados HTML", "title"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 3
tags: [html, head, meta, utf-8, viewport, responsivo, frontend]
skill: tech-mentor-frontend
status: stub
---

# head do HTML e metadados (meta charset, viewport, title)

O `<head>` guarda dados sobre a página, não conteúdo visível; o conteúdo vai no `<body>`. Para [[wiki/entities/nasser|Násser]], é "o cabeçalho do site", com "os dados inerentes ao site [...] os metadados, por isso que existem as tags meta" ([[wiki/sources/frontpush-o-que-e-html-linguagem-de-marcacao-tags-semantica]]). Não confundir com `<header>`, que é conteúdo visível ([[wiki/concepts/html-semantico]]).

## O que a estrutura do Emmet traz

- **`<meta charset="UTF-8">`**: como decodificar os bytes do arquivo. `[external]` Deve vir nos primeiros 1024 bytes; sem ele, acentos podem virar mojibake ("Ã§"): https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta#charset. Ver [[wiki/concepts/utf-8]]. A aula liga o charset ao teclado ABNT2, o que é um engano (ver a fonte).
- **`<meta name="viewport" content="width=device-width, initial-scale=1.0">`**: "como aparece na tela o seu HTML, se tem a versão responsiva, qual é a escala". `[external]` Sem ela, o celular renderiza a página numa largura virtual de cerca de 980 px e reduz, e as media queries não batem com a tela: https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag. Ver [[wiki/concepts/design-responsivo]].
- **`<title>`**: o texto da aba; o Emmet põe "Document". É elemento próprio, não meta.

`[external]` Outras coisas comuns no `head`: `<link>` para CSS e fontes ([[wiki/concepts/css]]), `<meta name="description">` (pode virar o snippet do buscador) e `<script defer>`.

## Na NLW #2, dia 1 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]], "todo o conteúdo visível na página deverá vir na tag body" e o head guarda "configurações do meu documento": `lang="pt-BR"`, `meta charset`, `meta viewport` e `title`. [[wiki/entities/mayk-brito|Mayk]] mostra que texto no head aparece e que um HTML sem head e body funciona, mas "está mal escrito".

## Na NLW #2, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]], o head ganha `<link rel="shortcut icon" href="images/favicon.png" type="image/png">` e `<meta name="theme-color" content="#8257E5">`. `rel="icon"` é o valor padrão; "shortcut" é legado. A repetição desses metadados em todas as páginas fica para ser resolvida no back-end.

## Key sources

- [[wiki/sources/frontpush-o-que-e-html-linguagem-de-marcacao-tags-semantica]]: head como cabeçalho de metadados; charset, viewport e title
- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: NLW #2, dia 1: head x body, lang, charset, viewport, title
- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: NLW #2, dia 3: favicon e theme-color
