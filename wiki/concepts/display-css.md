---
type: concept
title: "display no CSS (block x inline)"
aliases: ["display", "display block", "display inline", "elemento de bloco", "elemento inline", "inline-block"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 7
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

## Na NLW #1 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]]: block "pega toda a linha e joga o próximo elemento para baixo"; inline fica "do tamanho dela", e dois `a` seguidos ficam lado a lado mesmo com quebra de linha no código. O display aparece na aba Computed do DevTools. Block e inline valem "para as caixas pelo seu lado de fora"; `flex` mexe nos filhos "pelo lado de dentro", e o elemento flex é block por fora. Um `span` vazio só mostra o ícone de fundo com width, height e `display: flex`.

## Nem toda tag é bloco

Em [[wiki/sources/frontpush-o-que-e-html-linguagem-de-marcacao-tags-semantica]], [[wiki/entities/nasser|Násser]] diz que `section`, `header`, `footer`, `nav` e `div` "são caixas, são elementos de bloco", o que vale para essas. `[external]` As tags de texto citadas logo depois (`span`, `strong`) e a `img` são inline por padrão: https://developer.mozilla.org/en-US/docs/Glossary/Inline-level_content.

## "Pega dos dois mundos" (módulo de front-end do FrontPUSH)

Em [[wiki/sources/frontpush-box-model-margin-padding-display-unidades]], `display` "nada mais é de como a caixinha se comporta"; `block` "é a imensa maioria", `inline` "ignoraram as características de bloco", `inline-block` "pega dos dois mundos". Um link com 250 px de largura "é complicado": "é melhor deixar o link do tamanho do conteúdo". `[external]` Dois reparos: `h1` é bloco, não "elemento de linha" como diz a aula; e o inline aceita margin e padding horizontais, ignorando só `width`, `height` e a margin vertical.

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] põe o `label` do modal em `display: block` para o `margin-bottom` funcionar: "o display do label é inline ele não pega". Usa `display: none` na classe `hide` do [[wiki/concepts/modal]] e `display: grid` nos itens e nos cards ([[wiki/concepts/css-grid]]).

## Do block ao flex (FrontPUSH, módulo de Flexbox)

Em [[wiki/sources/frontpush-display-flex-flex-container-filhos-diretos]], [[wiki/entities/nasser|Násser]] recapitula `inline` (span, link), `block` ("a grande maioria e esmagadoras das outras tags") e `inline-block`, e chega a `display: flex`. Diz também que "todas as tags são elementos de bloco", o que contradiz a própria lista.

## Key Sources

- [[wiki/sources/principais-propriedades-css-color-background-font]]: bloco como padrão, span e link inline, link forçado a bloco no botão
- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: block x inline no DevTools; flex por fora é block
- [[wiki/sources/frontpush-o-que-e-html-linguagem-de-marcacao-tags-semantica]]: tags de seção como bloco; span/strong/img são inline
- [[wiki/sources/frontpush-box-model-margin-padding-display-unidades]]: block, inline, inline-block; `h1` chamado de inline (é bloco)
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: label block para margem vertical; none no modal; grid
- [[wiki/sources/frontpush-intro-flexbox-flex-container-flex-item]]: `display: flex` como primeira propriedade do flex-container
- [[wiki/sources/frontpush-display-flex-flex-container-filhos-diretos]]: aula 02: inline, block, inline-block e flex; "todas as tags são elementos de bloco" (deslize)
