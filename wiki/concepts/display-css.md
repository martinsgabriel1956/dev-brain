---
type: concept
title: "display no CSS (block x inline)"
aliases: ["display", "display block", "display inline", "elemento de bloco", "elemento inline", "inline-block"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [frontend, css, display, layout, box-model]
skill: tech-mentor-frontend
status: stub
---

# display no CSS (block x inline)

Propriedade que define como uma caixa participa do fluxo. **Bloco** (`block`) ocupa a linha inteira, empilha e aceita width, height e margem vertical. **Inline** fica na linha do texto e ignora width, height e margem vertical. `inline-block` fica na linha mas aceita as medidas. `flex` e `grid` organizam os filhos. Ver [[wiki/concepts/box-model]] e [[wiki/concepts/css]].

## Na aula

Em [[wiki/sources/principais-propriedades-css-color-background-font]], [[wiki/entities/nasser|Násser]]: a maioria das tags vem como bloco, "exceto a span e o [a] de link, que vem como display inline". Ele força `display: block` no link usado como botão porque quer "aplicar sempre as propriedades de box-model".

## Correções

- `[external]` `<img>` não é bloco: é inline substituído. Imagens com `width: 100%` só empilham porque não cabe outra na linha, e ficam com um vão embaixo, a linha de base do texto; `display: block` tira esse vão (https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img).
- `[external]` Além de span e a, são inline por padrão `strong`, `em`, `code`, `label`, `input`, `button` (inline-block) etc. (https://developer.mozilla.org/en-US/docs/Glossary/Inline-level_content).
- `[external]` Para o link-botão, `inline-block` mantém o botão do tamanho do texto; `block` o estica na largura do pai.

## Key Sources

- [[wiki/sources/principais-propriedades-css-color-background-font]]: bloco como padrão, span e link inline, link forçado a bloco no botão
