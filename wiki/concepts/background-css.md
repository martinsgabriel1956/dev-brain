---
type: concept
title: "Background no CSS (background-image, size, repeat, position)"
aliases: ["background", "background-image", "background-size", "background-repeat", "background-position", "background-color", "cover x contain", "imagem de fundo"]
date_created: 2026-11-16
date_updated: 2026-11-21
source_count: 7
tags: [frontend, css, background, background-image, background-size, imagem]
skill: tech-mentor-frontend
status: stub
---

# Background no CSS

Família de propriedades que pinta o fundo de uma caixa: cor (`background-color`) ou imagem (`background-image: url(...)`), com controle de tamanho, repetição e posição. É a segunda forma de pôr imagem na página, ao lado de `<img>`. Ver [[wiki/concepts/css]].

## img x background-image

Em [[wiki/sources/principais-propriedades-css-color-background-font]], [[wiki/entities/nasser|Násser]] mostra as duas formas:

- **`<img src>`**: a imagem é conteúdo, o caminho parte do HTML e o elemento ganha altura pela própria imagem.
- **`background-image`**: a imagem é decoração da caixa, o caminho parte do arquivo CSS ([[wiki/concepts/caminho-relativo]]) e a caixa não cresce por causa dela. "Porque está como background, não tem nada de conteúdo aqui dentro", então é preciso dar uma altura fixa.

`[external]` Regra prática: imagem com significado (foto de produto, gráfico) vai em `<img>` com `alt`, que o leitor de tela e o buscador enxergam; imagem decorativa vai no background (https://developer.mozilla.org/en-US/docs/Web/CSS/background-image#accessibility).

## Propriedades

| Propriedade | O que faz | Na aula |
|---|---|---|
| `background-size` | `cover` preenche a caixa e corta o excesso; `contain` mostra a imagem inteira e sobra espaço; ou medidas | cover cortou o passarinho numa section de 80% × 500; contain deixou inteiro e repetiu |
| `background-repeat` | `repeat` (padrão), `repeat-x`, `repeat-y`, `no-repeat`, `space`, `round` | `no-repeat` para não repetir no contain |
| `background-position` | palavras-chave (top, bottom, left, right, center), %, px; primeiro valor x, segundo y | center, bottom, left; `100px 50px` |

A escolha entre cover e contain é o mesmo dilema do [[wiki/concepts/aspect-ratio]]: cortar ou deixar sobra, nunca distorcer. `[external]` Para `<img>` o equivalente é `object-fit: cover | contain` (https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit).

## Na NLW #1 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa `background: url("../assets/home-background.svg") no-repeat` (sem `no-repeat` o fundo "vai querer ficar repetindo"), `height: 100vh` para a imagem não sair cortada e `background-position: 35vw bottom`, que vira `background-position-x: 70vw` abaixo de 900 px. Ele escreve `background-url` por engano e corrige no ícone: "não era não, era image".

## Gradiente para ver o giro (FrontPUSH, básico CSS aula 01)

Em [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]], com cor sólida "você não sabe se ele girou", então entra um `linear-gradient` "bem feio, o clássico blue-red", copiado do [[wiki/entities/figma]], para ver o `rotate`.

## O gradiente esconde a cor animada (FrontPUSH, básico CSS aula 05)

Em [[wiki/sources/frontpush-propriedade-animation-pratica-keyframes-parent-box-varias-animacoes]], ao animar `background-color` de red a blue, "esse linear-gradiente aqui está meio que me atrapalhando". `[external]` O gradiente é `background-image` e fica por cima da cor. Gradientes não interpolam sem `@property`.

## SVG como background (FrontPUSH, propriedades SVG aula 02)

Em [[wiki/sources/frontpush-como-usar-svg-img-background-object-inline]]: SVG em `background-image` numa `div.box`, `url()` voltando uma pasta, `background-size: cover` e "um height fixo, porque senão ele não vai aparecer" (100vh). Sem DOM nem CSS nas partes. Precisão: `cover` recorta; para a ilustração inteira, `contain` ([[wiki/concepts/formas-de-inserir-svg]]).

## background × fill no SVG (FrontPUSH, propriedades SVG aula 03)

Em [[wiki/sources/frontpush-estrutura-svg-viewport-viewbox-formas-basicas-path-defs]]: "no CSS quando você quer mudar o fundo de alguma coisa é background"; numa forma SVG por classe, "talvez mude, se não me engano, muda". Precisão: não muda; `rect`/`circle`/`path` não são caixas CSS, só `fill` os pinta. `background` funciona no `<svg>` externo.

## Key Sources

- [[wiki/sources/principais-propriedades-css-color-background-font]]: img x background, cover x contain, no-repeat, position, altura fixa
- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: fundo SVG, no-repeat, 100vh, position em vw
- [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]: `background-color: #0f0f0f` no `body` ("eu gosto de fundo dark"); `pink`, `green` para enxergar caixas
- [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 01: linear-gradient para ver o rotate
- [[wiki/sources/frontpush-propriedade-animation-pratica-keyframes-parent-box-varias-animacoes]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 05: gradiente cobre background-color animado
- [[wiki/sources/frontpush-como-usar-svg-img-background-object-inline]]: FrontPUSH, mini curso de CSS Animations, propriedades SVG aula 02: SVG como fundo; altura fixa; cover × contain
- [[wiki/sources/frontpush-estrutura-svg-viewport-viewbox-formas-basicas-path-defs]]: FrontPUSH, mini curso de CSS Animations, propriedades SVG aula 03: background não pinta formas SVG
