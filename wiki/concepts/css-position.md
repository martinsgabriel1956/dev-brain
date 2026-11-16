---
type: concept
title: "Position no CSS (static, relative, absolute, fixed, sticky)"
aliases: ["position", "CSS position", "position absolute", "position relative", "position fixed", "position sticky", "position static", "posicionamento CSS"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 3
tags: [css, frontend, position, layout, containing-block, sticky]
skill: tech-mentor-frontend
status: draft
---

# Position no CSS

A propriedade `position` define de onde contam as distâncias `top`, `right`, `bottom` e `left` e se o elemento continua no fluxo do documento. Ela não substitui flexbox ou grid como ferramenta de layout. Serve ao que eles não fazem: sobrepor, fixar na tela, grudar no topo durante o scroll ([[wiki/sources/position-css-static-relative-absolute-fixed-sticky]]).

| Valor | Referência das distâncias | Fica no fluxo? | Uso típico |
|---|---|---|---|
| `static` (padrão) | nenhuma; `top`/`left` e `z-index` não fazem efeito | sim | tudo que não precisa de posição especial |
| `relative` | a própria posição original | sim, o espaço original fica reservado | pequenos ajustes; referência para filhos `absolute` |
| `absolute` | ancestral posicionado mais próximo (sem nenhum: a viewport inicial) | não, os irmãos ocupam o espaço | badges, overlays, ícones dentro de cards |
| `fixed` | a viewport | não | [[wiki/concepts/menu-fixo]], botão flutuante |
| `sticky` | flui normal até o limite (`top: 0`), depois gruda no ancestral que rola | sim | cabeçalho e menu que grudam no scroll |

## Como a aula do FrontPUSH ensina

Em [[wiki/sources/position-css-static-relative-absolute-fixed-sticky]], com dois quadrados dentro de uma caixa de 500 px:

- **relative** é "em relação a ele mesmo": imagine o contorno tracejado da posição original e só o quadrado se movendo.
- **absolute** procura "o elemento pai que tem o position relative"; o slide diz melhor, "primeiro elemento pai com posição diferente de static", e sem nenhum chega ao `body`.
- **fixed** "só olha para a sua tela" e por isso serve a menus.
- **sticky** "faz a transição do position sticky para o position fixed" ao rolar.
- Truque do menu mobile: `relative` com valor negativo grande para esconder, zero para mostrar, `transition` para animar.

## Precisões `[external]`

- **Bloco de contenção.** A referência do `absolute` é o ancestral posicionado mais próximo (qualquer valor diferente de `static`). `transform`, `perspective`, `filter`, `contain` e `will-change` também criam bloco de contenção para `absolute` e `fixed`. Sem ancestral posicionado, vale o *initial containing block*, com o tamanho da viewport, e não o `body`: https://developer.mozilla.org/en-US/docs/Web/CSS/Containing_block.
- **Sticky tem limite.** Fica grudado só enquanto o pai está visível: "até encontrar a borda oposta do seu bloco de contenção". Precisa de `top` (ou outro lado) definido, e um ancestral com `overflow` diferente de `visible` vira o contêiner de scroll: https://developer.mozilla.org/en-US/docs/Web/CSS/position.
- **Camadas.** Elementos posicionados pintam acima dos não posicionados; entre posicionados sem `z-index`, quem vem depois no DOM fica por cima. `z-index` só age em elementos posicionados (e em itens de flex e grid): https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_positioned_layout/Stacking_context.
- **Animação.** Animar `top`/`left` refaz o layout a cada quadro; `transform: translate()` alcança o mesmo efeito só no composite `[skill: tech-mentor-frontend]`. Ver [[wiki/concepts/reflow-layout]] e [[wiki/concepts/paint-composite]].

## Relação com outros conceitos

- [[wiki/concepts/box-model]]: `top`/`left` deslocam a caixa inteira; `margin` desloca empurrando os vizinhos.
- [[wiki/concepts/handoff-design-dev]]: o `position: absolute` que o Figma gera para frames sem Auto Layout não deve ir para o código.
- [[wiki/concepts/css]]: posicionamento relativo e absoluto chegaram com o CSS2.

## No módulo de front-end do FrontPUSH (aula 07)

Em [[wiki/sources/frontpush-position-css-relative-absolute-coordenadas]], [[wiki/entities/nasser|Násser]] explica `absolute` como um "sistema de coordenadas" X/Y cuja origem é o elemento relativo, e resume "relative fica no pai, absolute fica no filho". Sem pai `relative`, um `top: 0` leva o item ao topo da janela, porque, segundo ele, "o body [...] vem por padrão como position relative". A precisão acima vale de novo: o `body` é `static`, e a referência é o *initial containing block*. Sem `top`, o item fica na *static position* e ainda sente o padding do pai. Uso no site do FrontPUSH: bolinhas animadas por `top`/`left`, um "nzinho" e um selo; o resto é flexbox ou grid.

## Key Sources

- [[wiki/sources/position-css-static-relative-absolute-fixed-sticky]]: os cinco valores com dois quadrados, menu fixed e menu sticky
- [[wiki/sources/frontpush-seletores-css-filho-irmao-atributo-nth-child-pseudo-elements]]: `relative` no pai e `absolute` + `top/left: 0` no `::after`, "adiantando" a aula de position
- [[wiki/sources/frontpush-position-css-relative-absolute-coordenadas]]: sistema de coordenadas; "relative fica no pai, absolute fica no filho"; body chamado de relative
