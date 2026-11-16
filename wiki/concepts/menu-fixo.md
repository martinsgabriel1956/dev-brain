---
type: concept
title: "Menu fixo (fixed e sticky header)"
aliases: ["menu fixo no topo", "sticky header", "fixed header", "header fixo", "navbar fixa", "menu grudado"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 3
tags: [ui, ux, css, navegacao, menu, position, sticky, padroes-de-interface]
skill: tech-mentor-frontend
status: stub
---

# Menu fixo

Menu de navegação que continua visível enquanto a página rola. É um padrão de interface consolidado: na aula de [[wiki/concepts/usabilidade]] do [[wiki/entities/frontpush|FrontPUSH]], o "menu fixo no topo" do site da [[wiki/entities/apple]] aparece como exemplo de não reinventar a roda ([[wiki/sources/usabilidade-facilmente-tres-esferas-boas-praticas-auxilio-emergencial]], [[wiki/concepts/padroes-de-interface]]).

## Como se faz no CSS

Em [[wiki/sources/position-css-static-relative-absolute-fixed-sticky]], o autor mostra dois caminhos com [[wiki/concepts/css-position]]:

- **`position: fixed`** "é muito utilizado para menus": fica preso à tela e sai do fluxo. `[external]` Por sair do fluxo, cobre o começo do conteúdo; é preciso compensar com `padding-top` no conteúdo, ou com `scroll-padding-top` para âncoras.
- **`position: sticky; top: 0`** numa `nav`: o menu fica no fluxo e gruda no topo quando o scroll chega até ele. Antes "só era implementada com o JavaScript".
- **Menu mobile que entra e sai**: `relative` com valor negativo grande, zero no clique e `transition`. `[skill: tech-mentor-frontend]` Prefira `transform: translateX(-100%)` → `translateX(0)`, que não refaz o layout.

## Cuidados `[external]`

- Em tela pequena, um cabeçalho fixo alto rouba área de leitura. Vale encolher o menu ou escondê-lo ao rolar para baixo.
- `sticky` para de funcionar se um ancestral tiver `overflow: hidden`/`auto`, e só gruda enquanto o pai está visível (https://developer.mozilla.org/en-US/docs/Web/CSS/position).
- WCAG 2.2, critério 2.4.11 (Focus Not Obscured): o cabeçalho fixo não pode esconder o elemento focado pelo teclado (https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html).

## Estrutura do menu no Sass (FrontPUSH)

Em [[wiki/sources/frontpush-nesting-aninhamento-sass]]: menu → itens → links, "sempre um debaixo do outro, um dentro do outro", e uma classe `.active` no link da página atual, "até mesmo em um próprio menu responsivo".

## Key Sources

- [[wiki/sources/position-css-static-relative-absolute-fixed-sticky]]: fixed para menus, demonstração do sticky numa `nav`, truque do menu mobile
- [[wiki/sources/usabilidade-facilmente-tres-esferas-boas-praticas-auxilio-emergencial]]: menu fixo da Apple como padrão de usabilidade
- [[wiki/sources/frontpush-nesting-aninhamento-sass]]: estrutura e `.active` do menu no Sass
