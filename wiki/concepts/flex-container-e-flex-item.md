---
type: concept
title: "Flex container e flex items"
aliases: ["flex-container", "flex-item", "flex-itens", "flex container", "flex items", "propriedades do flex-container", "propriedades do flex-item"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 9
tags: [frontend, css, flexbox, layout]
skill: tech-mentor-frontend
status: stub
---

# Flex container e flex items

No [[wiki/concepts/flexbox]], o elemento com `display: flex` (ou `inline-flex`) é o **flex container**; seus filhos diretos viram **flex items**. Cada grupo tem suas propriedades: o contêiner decide direção, quebra de linha e distribuição; o item decide quanto cresce, encolhe, sua base, sua ordem e seu próprio alinhamento.

| Flex container | Flex item |
|---|---|
| `display: flex` | `flex-grow` |
| `flex-direction` | `flex-shrink` |
| `flex-wrap` | `flex-basis` |
| `flex-flow` (direction + wrap) | `flex` (grow + shrink + basis) |
| `justify-content` | `order` |
| `align-items` | `align-self` (sobrescreve o `align-items` do pai) |
| `align-content` (só com várias linhas) | |

A lista é a do slide de abertura do módulo de Flexbox do [[wiki/entities/frontpush]] ([[wiki/sources/frontpush-intro-flexbox-flex-container-flex-item]]), em que [[wiki/entities/nasser|Násser]] divide o estudo em "propriedades que remetem ao flex-container e [...] aos flex-itens". As anotações entre parênteses são `[external]`: https://www.w3.org/TR/css-flexbox-1/.

## Precisões

- `gap` também vale no contêiner flex e substitui margens entre itens `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/gap).
- `order` muda só a ordem visual, não a do leitor de tela nem a do Tab `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/order). Ver [[wiki/concepts/acessibilidade]].
- Só os filhos diretos viram itens; netos seguem o fluxo normal, a menos que o filho também seja flex. Já dito por Násser na aula 06 do módulo de front-end ([[wiki/sources/frontpush-layout-css-botao-hover-flexbox-media-query]]).

## Filhos diretos (FrontPUSH, aula 02)

Em [[wiki/sources/frontpush-display-flex-flex-container-filhos-diretos]], [[wiki/entities/nasser|Násser]] define o container como "literalmente a div da parte de fora" e mostra que só os filhos diretos viram flex-items: um span dentro do item "não é filho direto, então ela não é um flex-item". `[external]` Qualquer elemento pode ser o contêiner, e o filho direto tem o `display` "blockificado" (https://www.w3.org/TR/css-flexbox-1/#flex-items).

## align-content x align-items

Em [[wiki/sources/frontpush-align-content-linhas-flex-wrap]], o slide resume: `align-content` "alinha as linhas do container" e "só funciona se existir mais de uma linha de flex-itens" (`flex-wrap: wrap`). `align-items` alinha os itens dentro da linha. `[external]` Valor inicial `normal`, que age como `stretch` (https://developer.mozilla.org/en-US/docs/Web/CSS/align-content). Fecha a lista do contêiner; a aula seguinte começa os itens com `flex-grow`.

## order e align-self (FrontPUSH, aula 09)

Em [[wiki/sources/frontpush-order-e-align-self]], [[wiki/entities/nasser|Násser]] fecha as propriedades dos itens: `order` (padrão 0, a ordem do HTML; aceita negativos) para pôr o texto antes da ilustração no mobile, e `align-self`, que sobrescreve o `align-items` do contêiner para um item só. `[external]` Não há `justify-self` no flexbox; no eixo principal, usa-se `margin: auto`.

## Key sources

- [[wiki/sources/frontpush-intro-flexbox-flex-container-flex-item]]: os "dois estudos" do módulo; slide com as propriedades de cada lado
- [[wiki/sources/frontpush-display-flex-flex-container-filhos-diretos]]: aula 02: container é "a div da parte de fora"; só filhos diretos viram itens
- [[wiki/sources/frontpush-flex-direction-flex-wrap-flex-flow]]: aula 03: `flex-direction`, `flex-wrap` e `flex-flow`, as três primeiras do contêiner depois do `display`
- [[wiki/sources/frontpush-justify-content-align-items-box-sizing]]: aula 04: `justify-content` e `align-items`; errata `wrap-reverse`
- [[wiki/sources/frontpush-align-content-linhas-flex-wrap]]: aula 05: align-content, última propriedade do contêiner
- [[wiki/sources/frontpush-flex-grow-crescer-espaco-disponivel]]: aula 06: fim das propriedades do contêiner; `flex-grow` abre as dos itens; ver [[wiki/concepts/flex-grow-shrink-basis]]
- [[wiki/sources/frontpush-order-e-align-self]]: aula 09: order e align-self, as últimas dos itens
- [[wiki/sources/frontpush-flexbox-pratica-2-desafio-estrutura-de-divs]]: prática 2: itens internos "precisam ser filhos direto" do pai flex; um filho só, `display: block`
- [[wiki/sources/frontpush-mentoria-pratica-com-css-grid]]: mentoria de grid: mesma lógica de pai e filhos diretos, agora grid container e grid itens
