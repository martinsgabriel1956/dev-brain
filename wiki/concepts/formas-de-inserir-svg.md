---
type: concept
title: "Formas de inserir SVG na página (img, background, object, inline, sprite)"
aliases: ["como usar o svg", "svg inline", "inline svg", "svg em img", "svg como background", "svg sprite", "object svg", "data uri svg"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 2
tags: [svg, svg-inline, img, background-image, object, sprite, data-uri, dom, cache, frontend]
skill: tech-mentor-frontend
status: stub
---

# Formas de inserir SVG na página

Onde o SVG mora decide o que se pode fazer com ele: se o CSS e o JS da página alcançam cada forma, se o arquivo tem cache próprio, se conta como requisição e como nó do DOM.

| Forma | CSS/JS da página alcança as partes? | Requisição / cache | Uso típico |
|---|---|---|---|
| `<img src="a.svg">` | Não (só o `<img>` inteiro); `<style>` interno anima | 1 requisição, cache | Ícone, ilustração estática; `alt`, `loading="lazy"` |
| `background-image: url(a.svg)` | Não | 1 requisição, cache | Decoração; a caixa precisa de altura |
| `<object data="a.svg">` / `<iframe>` / `<embed>` | JS via `contentDocument` (mesma origem); CSS não | 1 requisição, documento separado | Raro; SVG com script próprio; fallback no `<object>` |
| Data URI (`url("data:image/svg+xml,...")`) | Não | Nenhuma; sem cache separado | Ícone pequeno dentro do CSS; base64 incha ~33% |
| Inline (`<svg>` no HTML) | Sim: cada `<path>` é nó do DOM | Nenhuma; repetido em cada página | Animação e interação |
| Sprite: `<use href="s.svg#id">` | Parcial: `currentColor`, variáveis CSS, sem seletores no interior | 1 requisição, cache | Sistema de ícones reutilizados |
| Build/servidor (SVGR, `include` PHP) | Sim (resulta em inline) | Nenhuma no navegador | Componentes; inline sem colar à mão |

`[external]` sem fetch, por conhecimento prévio do MDN e do HTML Living Standard. Confiança alta.

## Na aula do FrontPUSH

[[wiki/entities/nasser|Násser]] apresenta quatro formas, "acredito que são as únicas quatro" ([[wiki/sources/frontpush-como-usar-svg-img-background-object-inline]]):

- `<img>` para ícones que não vai animar; "não tem edição no DOM, não tem como ter interação com o CSS".
- `background-image`, com "um height fixo, porque senão ele não vai aparecer" ([[wiki/concepts/background-css]]).
- `iframe`/`object`/`embed`, "muito ruim", "lento"; data URI, "só vi desvantagem".
- Inline, "o módulo que eu mais utilizo": DOM, CSS por parte, animação, "não precisa fazer request HTTP"; preço: "volume de código", resolvido com uma biblioteca JS ou PHP que faz "include".

## Precisões

- O sprite com `<use>` e a máscara CSS (`mask-image` com SVG + `background-color: currentColor`) ficam de fora da aula e resolvem o caso "muitos ícones" sem colar SVG em todo lugar.
- Inline tem custo: HTML maior, DOM maior ([[wiki/sources/frontpush-relatorio-pagespeed-imagens-render-blocking-dom-regra-80-20]]), sem [[wiki/concepts/cache]] separado; e IDs de gradiente repetidos entre SVGs colados colidem.
- Data URI não é `object`: é o SVG escrito dentro do `url()`. Codificado como URL é menor que em base64 ([[wiki/concepts/base64-encoding]]).
- Acessibilidade: `<img>` com `alt`; inline com `role="img"` + `<title>` ou `aria-hidden="true"`.

## Ver também

- [[wiki/concepts/formato-svg]]
- [[wiki/concepts/dom]]
- [[wiki/concepts/requisicao-http]]
- [[wiki/concepts/stroke-svg]]

## IDs repetidos confirmados (FrontPUSH, propriedades SVG aula 03)

Em [[wiki/sources/frontpush-estrutura-svg-viewport-viewbox-formas-basicas-path-defs]]: "esse filter0_d aplica esse mesmo ID quando eu faço o export de outro SVG, isso pode dar conflito"; vários SVGs inline no mesmo HTML pedem renomear IDs (ou SVGO `prefixIds`).

## Key sources

- [[wiki/sources/frontpush-como-usar-svg-img-background-object-inline]]: FrontPUSH, mini curso de CSS Animations, propriedades SVG aula 02: as quatro formas e o inline como padrão para animar
- [[wiki/sources/frontpush-estrutura-svg-viewport-viewbox-formas-basicas-path-defs]]: FrontPUSH, mini curso de CSS Animations, propriedades SVG aula 03: filter0_d repetido entre exports
