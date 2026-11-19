---
type: concept
title: "Área clicável"
aliases: ["touch target", "alvo de toque", "target size", "área de toque", "hit area", "altura mínima de 44 px"]
date_created: 2026-11-13
date_updated: 2026-11-19
source_count: 3
tags: [ui, ux, acessibilidade, mobile, responsividade, botoes, wcag]
skill: ux-ui-mentor
status: stub
---

# Área clicável

O espaço que responde ao clique ou ao toque de um elemento interativo. Pode ser maior que o desenho visível do elemento.

## Por que importa

"A precisão que eu tenho no mouse é muito maior do que a que eu tenho com o meu dedo, no meu smartphone." Botão pequeno dificulta o clique no mobile e prejudica quem tem problema de visão ([[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]). Por isso é questão de [[wiki/concepts/design-responsivo]] e de acessibilidade.

## A regra da aula

- **Altura mínima de 44 px**, "com base em vários guidelines"; ele usa 56 px ([[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]).
- No modo celular do DevTools, os botões da [[wiki/entities/apple]] "pelo menos mantiveram o mesmo tamanho para uma tela menor".

## O que dizem os guias

`[external]`

| Guia | Mínimo |
|---|---|
| Apple HIG | 44 × 44 pt |
| Material Design | 48 × 48 dp |
| WCAG 2.5.5 (AAA) | 44 × 44 px CSS |
| WCAG 2.5.8 (AA, WCAG 2.2) | 24 × 24 px CSS, ou espaço equivalente em volta |

Fonte da WCAG: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html. A área vale para largura e altura; links dentro de texto corrido são exceção. `[skill: ux-ui-mentor]` A skill usa 44 × 44 em mobile e pede espaçamento entre alvos vizinhos.

## Olhar de dev

`[skill: ux-ui-mentor]` Aumentar a área sem mudar o visual: `padding` no elemento, ou `min-height` / `min-width`. Ícone sem texto também precisa de `aria-label`.

## Na prática

A aula prática repete a regra ("coloque um mínimo de 44 pixels") e constrói o botão com 56 ([[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]]).

## O "xzinho" do anúncio (FrontPUSH, otimização aula 05)

Em [[wiki/sources/frontpush-google-pagespeed-core-web-vitals-acessibilidade-meta-tags]], o X pequeno de fechar anúncio ("área de contato muito pequena") aparece junto da mudança de layout. É problema de alvo de toque, não de CLS; o PageSpeed cobra "tamanho mínimo de botão, tamanho mínimo de input".

## Key Sources

- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]] — altura mínima de 44 px; mouse x dedo
- [[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]] — mínimo de 44 px repetido; botão de 56 no Figma
- [[wiki/sources/frontpush-google-pagespeed-core-web-vitals-acessibilidade-meta-tags]]: FrontPUSH, otimização aula 05: X de fechar pequeno
