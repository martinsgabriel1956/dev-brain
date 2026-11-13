---
type: concept
title: "Ponto focal em fotografia (regra dos terços)"
aliases: ["ponto focal", "regra dos terços", "rule of thirds", "grid de nove blocos", "pontos focais"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 3
tags: [ui, ui-design, imagens, fotografia, ponto-focal, regra-dos-tercos, composicao, hierarquia-visual]
skill: ux-ui-mentor
status: stub
---

# Ponto focal em fotografia

Toda imagem deve ter **um** ponto focal, posicionado nos cruzamentos de uma grade que divide a foto em nove blocos. É "noção de fotografia", mas Násser pede que se saiba o conceito para aplicar na interface ([[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]]).

## Como funciona

- As câmeras mostram "grades ou grids que geralmente dividem a sua foto em nove blocos".
- Os pontos focais são "o cruzar desses grids": quatro pontos.
- O assunto, por exemplo a cabeça de uma pessoa, deve ficar dentro ou ao redor desses pontos. Na aula, ele demonstra no [[wiki/entities/figma]] com uma elipse cinza num frame quadrado.
- Mais de um ponto focal, ou fugir da regra, "pode prejudicar a experiência".

`[external]` É a regra dos terços: duas linhas horizontais e duas verticais a um terço das bordas, com o assunto nas linhas ou nas interseções (https://en.wikipedia.org/wiki/Rule_of_thirds).

## Um só ponto focal

A comparação do autor é com a aula de [[wiki/concepts/espaco-em-branco|white space]]: dar ênfase a uma coisa. É o mesmo argumento de [[wiki/concepts/hierarquia-visual]] contra dois elementos com o mesmo peso, aplicado dentro da foto.

## Olhar de dev

`[external]` Quando a mesma foto é recortada em proporções diferentes (`object-fit: cover`), `object-position` controla qual parte fica visível e ajuda a manter o ponto focal no recorte (https://developer.mozilla.org/en-US/docs/Web/CSS/object-position). Ver [[wiki/concepts/aspect-ratio]].

## Ver também

- [[wiki/concepts/imagens-em-interfaces]]
- [[wiki/concepts/fotos-de-pessoas-reais]]

## Reforço do Material Design

Na parte 4, Násser aponta as diretrizes de imagem do [[wiki/entities/material-design]], que mostram ponto focal certo e errado: o principal da imagem "tem que estar naqueles quatro pontos lá" ([[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]]). O guia não pôde ser conferido.

## Ponto focal da tela inteira

Na aula de [[wiki/concepts/elementos-de-composicao]], "ponto focal" é usado para a tela: a logo e o nome do curso. A ambiência do fundo fica em baixo contraste para não tirar a atenção dele ([[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]]).

## Key Sources

- [[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]] — grid de nove blocos, quatro pontos, um ponto focal
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]] — Material Design reitera o ponto focal
- [[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]] — ponto focal da tela preservado pelo fundo em baixo contraste
