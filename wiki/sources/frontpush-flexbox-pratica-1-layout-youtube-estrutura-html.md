---
type: source
title: "Flexbox, prática 1: o layout do YouTube, do grid do design à estrutura HTML (FrontPUSH, módulo de Flexbox)"
aliases: ["FrontPUSH flexbox aula 10", "Flexbox Prática 1 FrontPUSH", "layout do YouTube com flexbox"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, html, flexbox, html-semantico, grid-de-colunas, naming, reset-css, projeto-pratico, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-flexbox-pratica-1-layout-youtube-estrutura-html.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Flexbox, prática 1: o layout do YouTube, do grid do design à estrutura HTML (FrontPUSH, módulo de Flexbox)

## TL;DR

Aula 10 do módulo de [[wiki/concepts/flexbox]] do [[wiki/entities/frontpush|FrontPUSH]], de [[wiki/entities/nasser|Násser]], e a primeira prática: reproduzir uma página de vídeo "do YouTube" (menu, vídeo principal, sugeridos) "utilizando apenas Flexbox". Esta aula só planeja e escreve o HTML; o CSS fica para a próxima.

- **Grid do design**: 12 colunas de 96 px com gutter de 24 px, "próximo de 1440px", que vira a largura do container ([[wiki/concepts/grid-de-colunas]], [[wiki/entities/figma]]).
- **Desenhar as caixas antes de codar**: retângulos coloridos sobre o design. Regra: "se é um fundo diferente desse fundo aqui, eu preciso colocar uma div" de ponta a ponta; dentro, um container centralizado; dentro, as linhas e colunas do flex. "Como em flexbox a gente sempre pensa em linhas", primeiro duas colunas (vídeo principal e sugeridos), depois imagem + texto em cada vídeo.
- **Setup**: pasta no [[wiki/entities/vs-code]], `index.html` + `css/style.css`, Live Server; reset de `margin`/`padding` e `border-box` ([[wiki/concepts/estilos-padrao-do-navegador-e-reset]]); `body` com `width: 100%` e `height: 100vh`; fundo `#0c0c0c`. O Chrome forçava o tema escuro.
- **HTML**: `header` > `.nav` > `.nav-logo` + `ul.nav-menu` > `li.nav-item` > `a.nav-link`; `section.container` > `.container-item1` (`.video-main`, `h3`, descrição) + `.container-item2` (vários `.video-side` com `.thumb` + `h4` + `p`). "Sempre utilizando HTML semântico" ([[wiki/concepts/html-semantico]]).
- **"Árvore de classes"**: o filho leva o nome do pai como prefixo (`nav` → `nav-item` → `nav-link`); e nada de misturar português com inglês nos nomes ([[wiki/concepts/naming]]).

## Key Claims

### O exercício

- Exercícios "com um design um pouquinho mais genérico, porque acredito que é mais fácil a gente estar reproduzindo e exercitando toda a teoria".
- "Eu estou propondo aqui o layout do YouTube [...] literalmente passar para o código utilizando apenas Flexbox." Primeiro "a parte do menuzinho e depois a parte do conteúdo".

### O grid do design

- "Esse design aqui eu apliquei um grid, um grid de 1440p." Remete às aulas de grid: "é importante a gente estabelecer o layout dessa forma [...] alguns padrões que a gente consegue passar para o código de maneira mais fácil". Ver [[wiki/concepts/grid-de-colunas]].
- "96px, 12 colunas, padrão de desktop, [...] e um gutter, ou seja, um espaço entre as colunas de 24px." "Isso aqui vai servir para poder a gente definir o container, e a soma [...] dá próximo de 1440px, que é um bom padrão."

### Desenhar as divs antes do código

- "Eu vou pegar aqui uma div vermelhinha e voltar traçando para poder a gente entender como é que vai se dar primeiro a estrutura HTML, para depois a gente codar."
- Regra do fundo: "o nosso menu tem um fundinho preto [...] Se é um fundo diferente desse fundo aqui, eu preciso colocar uma div, então literalmente vai ser uma div de ponta a ponta."
- Dentro, "a estrutura de container, tanto no conteúdo como no menu": uma div "literalmente centralizando o nosso conteúdo", com uma div para a logo e outra para o menu (lista com três links).
- Conteúdo: container de 1440 de largura, centralizado. "Como em flexbox a gente sempre pensa em linhas, a gente vai dividir primeiro aqui em duas colunas": vídeo principal e sugeridos. Cada vídeo tem uma div para a imagem (a thumbnail) e outra para o texto.

### Setup do projeto

- Pasta "Flexbox aula" no VS Code, `index.html`, `css/style.css`, estrutura HTML5, `link` para o CSS, Live Server. Ver [[wiki/entities/vs-code]].
- Fundo preto "por causa do tema do Google Chrome [...] o próprio Google Chrome força o tema escuro"; "ele força apenas os temas claros a converterem para o escuro".
- "Padding, margin: a gente zera os primeiros itens [...] e coloca sempre o border-size em border-box." Ver [[wiki/concepts/estilos-padrao-do-navegador-e-reset]] e [[wiki/concepts/box-model]].
- `body` com `width: 100%`, `height: 100vh` ("tela inteira") e borda verde de teste. Fundo: `#1a1a1a` era "o pretinho básico", mas "eu sempre estou colocando agora 0c, 0c, 0c".

### HTML do menu

- "Sempre utilizando HTML semântico": `header` de ponta a ponta; dentro, `.nav`, com `.nav-logo` e `.nav-menu`, que vira a própria lista (`ul`); `li.nav-item`; `a.nav-link`. Links: produtos, sobre, contato. Ver [[wiki/concepts/html-semantico]] e [[wiki/concepts/listas-html]].
- "Essa aqui é uma boa prática, onde você constrói uma árvore de classes: se a pai é nav, a filho faço nav, traço, o nome dela, bem específico e intuitivo." Ver [[wiki/concepts/naming]].

### HTML do conteúdo

- `section.container` com `.container-item1` (vídeo principal) e `.container-item2` (sugeridos).
- Item 1: `.video-main`, um `h3` com o título e uma descrição ("5000 visualizações há um mês").
- Item 2: vários `.video-side`, cada um com `.thumb` e descrição (`h4` + `p`).
- "Eu estou colocando aqui português junto com o inglês, isso aqui não é legal", e troca "vídeo sugerido" por `video-side`.

## Entities

- [[wiki/entities/nasser]]: instrutor.
- [[wiki/entities/frontpush]]: curso; primeira prática do módulo de Flexbox.
- [[wiki/entities/vs-code]]: editor do projeto, com Live Server.
- [[wiki/entities/figma]]: onde está o design com o grid (inferido pelo resto do curso; a aula não diz o nome).
- YouTube (layout reproduzido) e Google Chrome (tema escuro forçado): sem página.

## Concepts

- [[wiki/concepts/flexbox]]
- [[wiki/concepts/grid-de-colunas]]
- [[wiki/concepts/html-semantico]]
- [[wiki/concepts/listas-html]]
- [[wiki/concepts/naming]]
- [[wiki/concepts/estilos-padrao-do-navegador-e-reset]]
- [[wiki/concepts/box-model]]
- [[wiki/concepts/css-grid]]

## Precisões e tensões com a wiki

- **Semântica além do `header`.** `[external]` O menu pode ser `<nav>` (não `div.nav`); o conteúdo, `<main>`; os sugeridos, `<aside>` com cada vídeo em `<article>`. A página não tem `h1`: o título do vídeo principal deveria ser o `h1`, e os sugeridos `h2`/`h3`, sem pular de `h3` para `h4` sem um `h2` antes: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements. A thumb e o vídeo podem ser `<img>`/`<video>`, não `div`s de fundo. Ver [[wiki/concepts/html-semantico]].
- **A "árvore de classes" tem nome.** `[external]` O prefixo do pai no filho é a ideia do BEM (`block__element--modifier`): https://getbem.com/naming/. A versão da aula usa só hífen, o que não distingue elemento de modificador.
- **"border-size".** Lapso: a propriedade é `box-sizing: border-box` (a aula 04 do módulo explicou: [[wiki/sources/frontpush-justify-content-align-items-box-sizing]]).
- **`height: 100vh` no body.** `[external]` Com mais conteúdo que a tela, o `body` fica menor que a página; `min-height: 100vh` (ou `100dvh` no celular, por causa da barra do navegador) cobre os dois casos: https://developer.mozilla.org/en-US/docs/Web/CSS/length#dynamic_viewport_units.
- **"Apenas Flexbox".** É o exercício. Para o esqueleto de duas colunas, `grid-template-columns` também serve ([[wiki/concepts/css-grid]]); flexbox resolve bem cada linha (menu, card de vídeo).
- **As contas do grid.** 12 × 96 + 11 × 24 = 1416 px; com as margens laterais, chega aos 1440 do frame.
- **Tema escuro forçado.** É o "Auto Dark Mode" do Chrome (flag ou configuração do usuário), não o comportamento padrão do navegador. Uma página pode declarar `color-scheme` para dizer quais temas suporta: https://developer.mozilla.org/en-US/docs/Web/CSS/color-scheme.

## Open Questions

- "1440p": ficou literal no raw (ele também diz "1440px").
- "Portanto chamada de nav-menu" e "ficar em também da tela": literais.
- `date_published` vazio (~2022, inferido pelo resto do curso).

## Raw quotes

- "Se é um fundo diferente desse fundo aqui, eu preciso colocar uma div"
- "Como em flexbox a gente sempre pensa em linhas"
- "eu estou colocando aqui português junto com o inglês, isso aqui não é legal"
