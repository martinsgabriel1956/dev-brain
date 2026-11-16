---
type: source
title: "Order e align-self: mudar a ordem e o alinhamento de um flex-item (FrontPUSH, módulo de Flexbox)"
aliases: ["FrontPUSH flexbox aula 09", "Order & Align-self FrontPUSH", "aula 09 módulo Flexbox FrontPUSH"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, flexbox, order, align-self, acessibilidade, design-responsivo, flex-item, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-order-e-align-self.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Order e align-self: mudar a ordem e o alinhamento de um flex-item (FrontPUSH, módulo de Flexbox)

## TL;DR

Aula 09 do módulo de [[wiki/concepts/flexbox]] do [[wiki/entities/frontpush|FrontPUSH]], de [[wiki/entities/nasser|Násser]]. As "duas últimas propriedades dos flex-itens antes de a gente partir para a prática" ([[wiki/concepts/flex-container-e-flex-item]]):

- **`order`**: "literalmente modifica a ordem dos flex-itens". Padrão `0` = a ordem do HTML. Caso de uso: no desktop, ilustração e depois texto; no mobile, "às vezes é melhor aparecer primeiro o texto explicando e depois a ilustração" ([[wiki/concepts/design-responsivo]]). Muda só a ordem visual (ver Precisões e [[wiki/concepts/acessibilidade]]).
- **`align-self`**: os mesmos valores do `align-items`, mas para um item só: "se você quiser que algum dos itens saia desse padrão".
- Próximo passo: "uma parte mais prática, aplicando todos os conceitos".

## Key Claims

### Order

- "Essa propriedade aqui é muito simples, mas também muito funcional, que literalmente modifica a ordem dos flex-itens."
- Caso de uso: "no modelo desktop [...] eu ter a ilustração primeiro aparecendo, por exemplo, na parte esquerda e o texto depois". No mobile, "às vezes é melhor aparecer primeiro o texto explicando e depois a ilustração vem e ajuda".
- "O order zero [...] que é o valor padrão, apareça a ordem que está no HTML. Essa é a regra básica."
- Demo: o item 2 em primeiro e o 1 em segundo; depois o 4 em primeiro e o 2 por último; "quando eu quebro, ele segue essa mesma ordem".
- "É funcional quando a gente está tratando de melhorar a responsividade e o flow das informações, o fluxo de informações."
- Slide (print enviado com a transcrição): "Sempre do menor para o maior, assim order: 1, aparece na frente de order: 5." O número "pode ser negativo". "Se você quiser colocar um item do meio da lista no início da mesma, sem modificar os demais, o ideal é utilizar um valor negativo para este item, já que todos os outros são 0."

### Align-self

- "Ele traz justamente os mesmos valores, flex-start, flex-end, center", que no container "aplicava a todos os flex-itens [...] Se você quiser que algum dos itens saia desse padrão, você aplica o align-self."
- Demo: container com `align-items: flex-start` e itens com `max-height`; item 1 com `align-self: center`, depois `flex-start` ("vai subir") e `flex-end` ("vai descer"). `stretch` não completa "porque eu coloquei o minimum-height aqui para todos"; também mostra `baseline`.
- "É literalmente aplicar os estilos de alinhamento que a gente já conhecia, só que para itens específicos."
- Slide: `align-self` "passará por cima do que for atribuído no align-items do container"; `auto` é o "valor inicial padrão" e "vai respeitar o que for definido pelo align-items"; "quando em colunas, alinha o item ao início (esquerda) da coluna".

## Entities

- [[wiki/entities/nasser]]: instrutor.
- [[wiki/entities/frontpush]]: curso; módulo de Flexbox.

## Concepts

- [[wiki/concepts/flex-container-e-flex-item]]
- [[wiki/concepts/flexbox]]
- [[wiki/concepts/acessibilidade]]
- [[wiki/concepts/design-responsivo]]
- [[wiki/concepts/html-semantico]]
- [[wiki/concepts/box-model]]

## Precisões e tensões com a wiki

- **`order` muda só o que se vê.** `[external]` Leitores de tela e a navegação por Tab seguem a ordem do HTML. Se o texto vem antes no mobile por ser mais importante, o melhor é escrever o HTML nessa ordem e reordenar visualmente no desktop, não o contrário. Uma ordem visual que contradiz a do código pode falhar nos critérios de sequência significativa e de ordem de foco da WCAG: https://developer.mozilla.org/en-US/docs/Web/CSS/order#accessibility e https://www.w3.org/WAI/WCAG21/Understanding/meaningful-sequence.html. A wiki já anota isso em [[wiki/concepts/acessibilidade]] e [[wiki/concepts/flex-container-e-flex-item]].
- **Empates.** `[external]` Itens com o mesmo `order` mantêm a ordem do HTML entre si; os valores são inteiros.
- **Não existe `justify-self` no flexbox.** `[external]` `align-self` age só no eixo cruzado. Para empurrar um item sozinho no eixo principal (por exemplo, o último link do menu para a direita), usa-se `margin-left: auto`: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_box_alignment/Box_alignment_in_flexbox. Ver [[wiki/concepts/box-model]].
- **O que segurava o `stretch`.** Na demo, foi o `max-height` (ele mesmo se corrige: "o max-height, aliás"), não o `min-height`, como ele repete depois.
- **"As mesmas características de quando a gente está falando sobre flex-item".** Lapso: as características são as do `align-items`, no container.

## Open Questions

- `date_published` vazio (~2022, inferido pelo resto do curso).

## Raw quotes

- "literalmente modifica a ordem dos flex-itens"
- "às vezes é melhor aparecer primeiro o texto explicando e depois a ilustração vem e ajuda"
- "só que para itens específicos"
