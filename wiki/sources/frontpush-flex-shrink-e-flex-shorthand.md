---
type: source
title: "Flex-shrink e flex: a redução dos itens e o atalho grow, shrink e basis (FrontPUSH, módulo de Flexbox)"
aliases: ["FrontPUSH flexbox aula 08", "Flex-shrink & Flex FrontPUSH", "aula 08 módulo Flexbox FrontPUSH"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, flexbox, flex-shrink, flex, shorthand, flex-item, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-flex-shrink-e-flex-shorthand.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Flex-shrink e flex: a redução dos itens e o atalho grow, shrink e basis (FrontPUSH, módulo de Flexbox)

## TL;DR

Aula 08 do módulo de [[wiki/concepts/flexbox]] do [[wiki/entities/frontpush|FrontPUSH]], de [[wiki/entities/nasser|Násser]]. Fecha as propriedades de tamanho dos itens ([[wiki/concepts/flex-grow-shrink-basis]]):

- **`flex-shrink`**: "a capacidade de redução do item". Padrão `1` (pode encolher); `0` mantém o `flex-basis` ("mantenha esse 300 pixels forever"); números maiores encolhem "proporcional[mente]" mais.
- **Quase invisível**: com 1, 5, 6, 7 ou 10, "basicamente a gente não enxerga nada"; só no extremo, com a janela bem estreita. "Na maioria das vezes, o flex-shrink vai ficar igual a 1 e você nem vai perceber." O motivo real é o `flex-wrap: wrap` da demo (ver Precisões).
- **`flex`** ([[wiki/concepts/shorthand-css]]): "um atalho das propriedades flex-grow, flex-shrink e flex-basis", na ordem grow, shrink, basis; padrão `0 1 auto`; `flex: 1` = `1 1 0`; "o próprio W3C fala que é legal definir o flex dessa forma" ([[wiki/entities/w3c]]).
- **A fórmula dele**: "é sempre 1, 1, 300" (`flex: 1 1 300px`), com um grow diferente por classe ou inline quando quer que um item cresça mais.

## Key Claims

### Flex-shrink

- "Basicamente, ele vai definir a capacidade de redução do item." Os itens "tendam a se ajustar para poder manter todas as regras que a gente estabeleceu", "a regra de grow e a regra de basis".
- Padrão `1`: "eu permito que o item meio que diminua [...] para poder caber dentro do container".
- `0`: "é para ficar fixo com o flex-basis que foi estabelecido, para manter esse valor fixo, pronto, acabou."
- Números maiores: "se eu colocar [...] um flex-shrink igual a quatro, ele vai permitir que quatro vezes ele diminua mais do que o flex-shrink um".
- Slide (print enviado com a transcrição): `1` "permite que os itens tenham os seus tamanhos (seja esse tamanho definido a partir de width ou flex-basis) reduzidos para caber no container"; `0` "não permite a diminuição dos itens, assim um item com flex-basis: 300px; nunca diminuirá menos do que 300px, mesmo que o conteúdo não ocupe todo esse espaço"; "um item com shrink: 3 diminuirá 3 vezes mais que um item com 1".

### Por que não se vê

- "É muito difícil vocês perceberem a diferença do flex-shrink [...] quase a gente não presta atenção nesse cara quando a gente está construindo layout."
- Testes com 0, 5, 6, 7, 10: "não mudou absolutamente nada". Explicação dele: "como o container está em um tamanho ainda legal, ele não sentiu ainda essa necessidade", e "a diferença do flex-shrink 6 para o 1 é tão pequena que também você não percebe".
- No extremo (inspecionar, janela no mínimo), o conteúdo começa a quebrar, até que "não consegue mais diminuir [...] por ser um conteúdo contínuo".
- Com `flex-shrink: 0` e base de 300 px, "os 300 pixels estão mantidos". "Como é difícil você encontrar até mesmo tela de celular a 320 pixels, por isso que a gente não percebe muito."

### O atalho flex

- "De cara é o que eu mais utilizo": "um atalho das propriedades flex-grow, flex-shrink e flex-basis, isso em um comando só". "A ordem é o grow, o shrink e o basis"; o padrão "sempre vem setado como flex 0 1 auto".
- "O próprio W3C fala que é legal definir o flex dessa forma [...] porque ela é inteligente, então meio que é mais difícil você errar." Ver Precisões.
- `flex: 1` = `flex-grow: 1`, `flex-shrink: 1`, `flex-basis: 0`: com base 0, os itens ficam "muito parecidos uns dos outros mesmo estando com o grow aqui diferente".
- `flex: 2` "mantém exatamente as mesmas coisas", só com grow 2.
- "Essa de cara é a [...] fórmula que eu mais utilizo, é sempre 1, 1, 300, e quando eu quero aplicar algum flex-grow diferente, eu vou lá e aplico de forma inline ou aplicando alguma classe." "Eu gosto do flex-basis para poder a gente ter um melhor controle dos nossos flex-itens."
- Slide: "Para melhor consistência entre os browsers, é recomendado utilizar a propriedade flex ao invés de cada propriedade separada." `flex: 1` define basis `0` ("em alguns browsers define como 0%, pois estes ignoram valores sem unidades"); `flex: 3 2 300px` = grow 3, shrink 2, basis 300px.

## Entities

- [[wiki/entities/nasser]]: instrutor.
- [[wiki/entities/frontpush]]: curso; módulo de Flexbox.
- [[wiki/entities/w3c]]: citado como quem recomenda o shorthand `flex`.

## Concepts

- [[wiki/concepts/flex-grow-shrink-basis]]
- [[wiki/concepts/flexbox]]
- [[wiki/concepts/shorthand-css]]
- [[wiki/concepts/compatibilidade-entre-navegadores]]
- [[wiki/concepts/design-responsivo]]

## Precisões e tensões com a wiki

- **Por que o shrink não aparecia: o `wrap`.** `[external]` Com `flex-wrap: wrap`, o navegador monta cada linha só com os itens que cabem pelo tamanho base, então quase nunca falta espaço e o `flex-shrink` não tem o que fazer. A exceção é um item sozinho mais largo que o contêiner, que foi o "extremo" da demo. Para ver o shrink, use `nowrap`: aí a linha fica com déficit e os fatores agem: https://www.w3.org/TR/css-flexbox-1/#resolve-flexible-lengths.
- **"4 vezes mais" só com bases iguais.** `[external]` O encolhimento é proporcional a `flex-shrink × flex-basis`: um item de base 300 px com shrink 1 cede tanto quanto um de 100 px com shrink 3. O slide e a fala ignoram o peso da base: https://developer.mozilla.org/en-US/docs/Web/CSS/flex-shrink.
- **O limite do conteúdo contínuo.** É o `min-width: auto` (mínimo do conteúdo), o mesmo da aula 07 ([[wiki/sources/frontpush-flex-basis-tamanho-base-flex-itens]]): nenhum fator de shrink passa dele.
- **O W3C recomenda o `flex`.** Confirmado `[external]`: a especificação diz que os autores são encorajados a controlar a flexibilidade pelo shorthand `flex`, que reseta os componentes omitidos para valores que atendem os usos comuns: https://www.w3.org/TR/css-flexbox-1/#flex-components. Outros atalhos: `flex: auto` = `1 1 auto`, `flex: none` = `0 0 auto`.
- **"Alguns browsers [...] 0%".** `[external]` A especificação define que o basis omitido em `flex: 1` vale `0` (os navegadores mostram `0%`). O problema histórico de `0` sem unidade era do IE10/11. Ver [[wiki/concepts/compatibilidade-entre-navegadores]].
- **"1, 1, 300".** `flex: 1 1 300px` com `flex-wrap: wrap` é o padrão de cards da aula 07; mesma ressalva da última linha esticada e da alternativa em grid ([[wiki/concepts/css-grid]]).
- **Telas de 320 px.** Ainda existem viewports CSS de 320 a 360 px em celulares pequenos (a WCAG usa 320 px como referência de reflow); o `flex-shrink: 0` com base de 300 px fica perto do limite: https://www.w3.org/WAI/WCAG21/Understanding/reflow.html.

## Open Questions

- "Mais difícil você errar quando você utiliza o flex total" e "a tipa fórmula que eu mais utilizo": ficaram literais no raw ("flex total" pode ser "flex, o atalho"; "tipa" pode ser "típica").
- `date_published` vazio (~2022, inferido pelo resto do curso).

## Raw quotes

- "mantenha esse 300 pixels forever"
- "Na maioria das vezes, o flex-shrink vai ficar igual a 1 e você nem vai perceber"
- "é sempre 1, 1, 300"
