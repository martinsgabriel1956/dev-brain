---
type: concept
title: "Botões em interfaces"
aliases: ["botões", "botões e links", "button", "botão primário", "botão secundário", "primary button", "secondary button", "CTA"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 2
tags: [ui, ui-design, botoes, links, hierarquia-visual, consistencia, acessibilidade, design-system]
skill: ux-ui-mentor
status: stub
---

# Botões em interfaces

Elemento interativo que **guia o usuário na jornada**: leva de um ponto A a um ponto B e mostra os principais caminhos, funcionalidades e ações da interface, ou a finalidade de um formulário ("cadastre-se") ([[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]). É um dos [[wiki/concepts/elementos-da-interface]]; "link é diferente de botão" ([[wiki/sources/elementos-da-interface-introducao-ui-design]]).

## O botão nasce do objetivo

Primeiro vem o [[wiki/concepts/objetivo-da-interface|objetivo]], depois o botão. No [[wiki/entities/frontpush]], o aluno quer a grade (botão "grade do curso") e o dono quer a inscrição ("inscreva-se"). No [[wiki/entities/sketch]], preço ("See pricing") e teste ("tente de graça"). Na [[wiki/entities/apple]], o botão está onde ela quer que se veja o preço ([[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]).

## Primário e secundário

- **Primário:** preenchido, na cor de [[wiki/concepts/contraste]] da paleta; o "ímã" da tela.
- **Secundário:** "vazio, entre aspas, sem background" (só borda).
- A diferença cria [[wiki/concepts/hierarquia-visual]] entre ações. "Cinco tipos de botão [...] nunca é uma decisão legal" ([[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]).
- `[skill: ux-ui-mentor]` Design systems costumam ter primary, secondary, ghost e destructive, com no máximo um primary por seção. Estados: default, hover, focus, active, disabled, loading.

## Anatomia

| Parte | Regra da aula |
|---|---|
| Altura | Fixa; mínimo de 44 px (ele usa 56). Ver [[wiki/concepts/area-clicavel]] |
| Largura | Varia com o texto |
| Padding | Igual em todos, tirado da [[wiki/concepts/escala-de-espacamento]] |
| Radius | O mesmo em todos ([[wiki/concepts/border-radius]]; 16 px no slide) |
| Label | Curto e objetivo; nunca "clique aqui para ir para tal seção" |
| Fundo | Cor de contraste da paleta |
| Hover | Cresce, ganha sombra da cor do botão ou muda a opacidade ([[wiki/concepts/feedback-do-sistema]]) |

## Consistência

"Escolheu um botão para sua interface, utilize o mesmo botão do mesmo jeito durante toda a sua interface" ([[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]). Ver [[wiki/concepts/consistencia-visual]].

## Olhar de dev

`[skill: ux-ui-mentor]` `<button>` para ação, `<a href>` para navegação. A anatomia vira tokens (altura, padding, radius, cor, sombra) e um componente com variantes (`variant="primary" | "secondary"`). Hover pede par: focus visível para teclado e active para toque.

## Formas

A forma do botão comunica: retangular (seriedade), arredondado (amigável, "coringa"), circular (cativante, aproxima), chanfrado (futurista), diagonal (movimento) e hexagonal (gamificado). Catálogo em [[wiki/concepts/formas-de-botoes]] ([[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]]).

## Key Sources

- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]] — aula teórica de botões e links (edição "W7")
- [[wiki/sources/elementos-da-interface-introducao-ui-design]] — "link é diferente de botão"
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — botão preenchido acima do vazio
- [[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]] — formas: reto, arredondado, circular, chanfrado, diagonal, hexagonal
