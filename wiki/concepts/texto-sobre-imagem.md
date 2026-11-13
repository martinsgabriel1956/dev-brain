---
type: concept
title: "Texto sobre imagem (capa de gradiente)"
aliases: ["como escrever em imagens", "texto em cima de imagem", "overlay de gradiente", "capa de gradiente", "scrim", "linear gradient sobre imagem"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 4
tags: [ui, ui-design, imagens, contraste, legibilidade, gradiente, acessibilidade, css]
skill: ux-ui-mentor
status: stub
---

# Texto sobre imagem

Escrever em cima de uma foto pede garantir [[wiki/concepts/contraste]], porque o fundo varia de ponto a ponto. A técnica de Násser é uma "capa de gradiente" entre a foto e o texto ([[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]]).

## Regras da aula

- **Letra branca "99% das vezes".** Outra cor só por contraste: em fundo "super amarelo", cinza escuro. "Salvo se o fundo não for muito claro da sua imagem, utilize branco."
- **Capa de gradiente linear** em preto com transparência, mais forte onde está o texto ("régua de contraste").
- **A ponta clara não precisa ir a zero:** 30% ou 40% bastam; na demonstração, 50% em cima e 90% embaixo.
- **Gradiente na cor do background** (nos posts dele, o mesmo azul do fundo a 100% na base) acopla a imagem à interface e faz a foto "ir revelando aos poucos".
- **Começar o gradiente um pouco acima da base** para abrir espaço ao texto.
- **Só onde precisa:** imagem já escura e com bom contraste dispensa a capa.
- **Critério final:** "se eu não preciso garantir legibilidade é porque não precisa ler".

## Olhar de dev

`[external]` Em CSS, o gradiente vai como camada antes da imagem no mesmo `background`:

```css
.hero {
  background:
    linear-gradient(to top, rgb(0 0 0 / 0.9), rgb(0 0 0 / 0.5)),
    url("hero.jpg") center / cover;
  color: white;
}
```

(https://developer.mozilla.org/en-US/docs/Web/CSS/gradient/linear-gradient)

`[skill: ux-ui-mentor]` WCAG AA: 4.5:1 para texto normal, 3:1 para texto grande. Sobre foto, meça no pior ponto atrás do texto e teste com texto real, não só com hexadecimais.

## Conferir com checker

Na parte 3, Násser passa a cor do card do blog com gradiente pelo [[wiki/entities/who-can-use]] (conta-gotas, hexadecimal, "nota 3A") ([[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]]). O checker compara cores sólidas, então vale medir no pior ponto da foto atrás do texto.

## Capa preta, saturação e brilho

Na edição "W7" o texto branco é "um coringa", e outras cores são exceção. Se a imagem é clara demais: diminuir saturação, diminuir brilho ou pôr "uma capa preta com opacidade na frente da imagem" ([[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]]). É a mesma regra da parte 2 com outra técnica de capa (lá, gradiente).

## Retângulo preto a 20%

Na prática da edição "W7", em vez de baixar a exposição da foto, ele deixa a foto original, desenha um retângulo preto com 20% de opacidade e traz o título branco para a frente (bring to front) ([[wiki/sources/imagens-e-ilustracoes-pratica-figma-importar-editor-plugins-exportacao]]). `[skill: ux-ui-mentor]` Os 20% são ponto de partida: conferir 4,5:1 no pior ponto da foto atrás do texto.

## Key Sources

- [[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]] — letra branca, capa de gradiente, gradiente na cor do fundo
- [[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]] — card do blog com linear-gradiente conferido no Who Can Use
- [[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]] — edição "W7": texto branco como coringa; capa preta com opacidade, saturação e brilho
- [[wiki/sources/imagens-e-ilustracoes-pratica-figma-importar-editor-plugins-exportacao]] — prática "W7": retângulo preto a 20% de opacidade atrás do título
