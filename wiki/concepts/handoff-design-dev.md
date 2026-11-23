---
type: concept
title: "Handoff design ↔ dev"
aliases: ["handoff", "handoff de design", "passagem para o desenvolvedor", "redlines", "spec de componente", "documentação para o dev"]
date_created: 2026-11-15
date_updated: 2026-11-23
source_count: 4
tags: [ui, ui-design, handoff, documentacao, figma, css, design-system, estados]
skill: ux-ui-mentor
status: stub
---

# Handoff design ↔ dev

Passagem do design para quem vai implementá-lo: que informações o desenvolvedor precisa para reproduzir a interface sem adivinhar. É a parte do [[wiki/concepts/style-guide]] voltada ao código.

## A regra da aula: refino sempre, posição nunca

Em [[wiki/sources/style-guide-pratica-parte-2-documentacao-para-dev-sombra-gradiente-estados]], Násser se põe no lugar do dev diante de um card:

- **Documentar sempre** o que é "refino das cores ou então de sombras": ângulo e paradas do gradiente, quantas camadas de `box-shadow` ([[wiki/concepts/sombra-em-interfaces]]), cor em RGBA e hex, [[wiki/concepts/border-radius]] por tamanho de card. O CSS do Inspect do [[wiki/entities/figma]] se copia e cola: "o Figma acerta muito".
- **Documentar quando importa:** dimensões e padding. No botão, o padding, porque a largura acompanha o texto ([[wiki/concepts/botoes-em-interfaces]]). No card, linhas-guia com setas marcando o tamanho.
- **Descartar** o `position` gerado pelo Figma: "tendo o flexbox e o grid", ninguém faz layout assim.
- **Estados:** normal, hover e clicável para card, ícone e input, dizendo o que muda de um para o outro ([[wiki/concepts/feedback-do-sistema]], [[wiki/concepts/maquina-de-estados-ui]]).

## O que um handoff completo tem

`[skill: ux-ui-mentor]` Cinco blocos: tokens com nome (não só "o botão é azul"); **todos** os estados (default, hover, focus, active, disabled, loading, error); comportamento ("o dropdown fecha ao clicar fora"); acessibilidade (roles, labels, teclado); edge cases (texto longo, sem dados, erro, mobile). Por elemento, os redlines anotam tamanho, espaçamentos, tipografia, cor com nome de token, borda, sombra e comportamento em hover e focus. A aula cobre bem a parte visual e deixa de fora focus, disabled, comportamento e acessibilidade.

## Olhar de dev

`[external]` O Auto Layout do Figma corresponde ao flexbox, e frames com Auto Layout saem como `display: flex` no CSS gerado; o `position` absoluto vem de frames sem Auto Layout (https://help.figma.com/hc/en-us/articles/360040451373). Desenhar com Auto Layout torna o próprio Inspect mais útil. O gradiente vira `background: linear-gradient(220deg, … 14.43%, … 85%)`; `background-linear-gradient` não existe como propriedade (https://developer.mozilla.org/en-US/docs/Web/CSS/gradient/linear-gradient).

## Quando position entra no código

A regra "posição nunca" vale para o `position` que o Figma gera. Na aula de CSS do mesmo curso ([[wiki/sources/position-css-static-relative-absolute-fixed-sticky]]), position é ferramenta para o que flexbox e grid não fazem: menu `fixed` ou `sticky`, um item `absolute` dentro de um card `relative`. O handoff deve dizer quando o elemento é fixo ou gruda no scroll. Isso é comportamento, e o Inspect não mostra. Ver [[wiki/concepts/css-position]], [[wiki/concepts/menu-fixo]].

## Key Sources

- [[wiki/sources/style-guide-pratica-parte-2-documentacao-para-dev-sombra-gradiente-estados]]: o que documentar para o dev num card e num botão; position descartado; três estados
- [[wiki/sources/position-css-static-relative-absolute-fixed-sticky]]: position como ferramenta de layout pontual (fixed, sticky, absolute)
- [[wiki/sources/frontpush-layout-css-botao-hover-flexbox-media-query]]: "pegar o que a gente fez aqui no Figma e conseguir traduzir para o CSS de maneira plena, porque é espaçamento, são caixinhas"
- [[wiki/sources/frontpush-monetizacao-freelancer-como-cobrar-hora-ou-projeto]]: saber o handoff evita "voltar no possível handoff" e perder dinheiro
