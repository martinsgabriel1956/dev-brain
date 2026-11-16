---
type: concept
title: "Background no CSS (background-image, size, repeat, position)"
aliases: ["background", "background-image", "background-size", "background-repeat", "background-position", "background-color", "cover x contain", "imagem de fundo"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
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

## Key Sources

- [[wiki/sources/principais-propriedades-css-color-background-font]]: img x background, cover x contain, no-repeat, position, altura fixa
- [[wiki/sources/frontpush-css-classes-e-ids-seletores-link-style-css]]: `background-color: #0f0f0f` no `body` ("eu gosto de fundo dark"); `pink`, `green` para enxergar caixas
