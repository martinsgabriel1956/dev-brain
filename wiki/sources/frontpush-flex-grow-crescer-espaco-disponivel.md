---
type: source
title: "Flex-grow: quanto cada flex-item cresce no espaço disponível (FrontPUSH, módulo de Flexbox)"
aliases: ["FrontPUSH flexbox aula 06", "Flex-grow FrontPUSH", "aula 06 módulo Flexbox FrontPUSH"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, flexbox, flex-grow, flex-item, espaco-livre, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-flex-grow-crescer-espaco-disponivel.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Flex-grow: quanto cada flex-item cresce no espaço disponível (FrontPUSH, módulo de Flexbox)

## TL;DR

Aula 06 do módulo de [[wiki/concepts/flexbox]] do [[wiki/entities/frontpush|FrontPUSH]], de [[wiki/entities/nasser|Násser]]. Fechadas as propriedades do contêiner, começa a dos itens ([[wiki/concepts/flex-container-e-flex-item]]) com `flex-grow` ([[wiki/concepts/flex-grow-shrink-basis]]):

- **O que é**: "define a habilidade de um flex-item crescer". Padrão `0`; "quanto maior o número, maior em proporção ele vai crescer".
- **Só cresce se sobra espaço**: com todos em `flex-grow: 1`, 2, 3, 10 ou 50, "nada" muda, porque os itens "não tinha[m] quebrado". "O grow não é necessariamente aumentar, é aumentar quando está disponível."
- **Valores iguais = crescimento igual**: "a grande sacada do flex-grow é quando eu tenho flex-grows diferentes".
- **Demo 1, 2, 4**: com 12 itens em `wrap`, todos em 1, o item 11 em 2 e o 12 em 4. Ele diz que o 12 fica "4 vezes maior"; o que é 4 vezes maior é a fatia do espaço livre (ver Precisões).

## Key Claims

### Os dois pilares

- "Até agora, a gente entendeu como é que funcionam todas as propriedades sobre flex-container." Agora, "ao invés de aplicar as propriedades no flex-container, eu vou aplicar no flex-items".
- Depois de todas as propriedades, "vai ter alguns projetinhos práticos".

### O que é o flex-grow

- "Grow vem de crescimento, então ele define a habilidade de um flex-item crescer. Quanto ele vai crescer com relação ao outro?"
- "O número padrão que vem aqui no flex-grow é zero. E aí, quanto maior o número, maior em proporção ele vai crescer."
- Slide (print enviado com a transcrição): "Por padrão o valor é zero, assim os flex itens ocupam um tamanho máximo relacionado o conteúdo interno deles ou ao width definido." "Se você tiver uma linha com quatro itens, onde três são flex-grow: 1 e um flex-grow: 2, o flex-grow: 2 tentará ocupar 2 vezes mais espaço extra do que os outros elementos." `flex-grow: 0` "obedece o width do elemento ou o flex-basis". E uma observação: "justify-content não funciona em items com flex-grow definido".

### Preparação: stretch

- Sem padding e com `flex-direction: row`, "ele vem em padrão stretch, que é completando todo o espaço vazio"; com `height: 700`, os itens esticam na vertical. Ver [[wiki/sources/frontpush-justify-content-align-items-box-sizing]] (onde ele dizia que o padrão era `flex-start`).

### Flex-grow igual: nada muda

- `flex-grow` 0, 1, 2, 3, 10: "nada". "Ah, porque não tinha quebrado."
- Quando quebra, "o que realmente aumenta no flex-grow é a distância do conteúdo para a borda, de forma que preencha o container como um todo".
- "Como todos os flex-items têm justamente o mesmo [...] flex-grow, eles vão crescer de forma justamente igual. Então, eu colocar um flex-grow 50, não vai mudar nada."

### Flex-grows diferentes

- Com 8 itens a linha não quebra, "porque eu tenho uma outra propriedade chamada flex-basis, que eu vou ter que explicar depois". Volta a 12.
- Todos em 1 e o item 12 com `style="flex-grow: 4"` inline: "só no item 12, ele está crescendo mais que os outros". "O 12 está 4 vezes maior."
- O item 11 em 2: "ele sempre vai aumentar conforme o espaço que ele tem disponível. Quando ele está aqui, como não quebrou, não tem nada que aumentar."
- "O 12 tem maior prioridade que o 11, que [...] tem maior que o 10, que o 10 já é o flex-grow 1 normal. [...] 1, 2, 4."

## Entities

- [[wiki/entities/nasser]]: instrutor.
- [[wiki/entities/frontpush]]: curso; módulo de Flexbox.

## Concepts

- [[wiki/concepts/flex-grow-shrink-basis]] (nova)
- [[wiki/concepts/flexbox]]
- [[wiki/concepts/flex-container-e-flex-item]]

## Precisões e tensões com a wiki

- **Proporção do espaço livre, não do tamanho.** `[external]` `flex-grow` divide o *espaço livre* da linha entre os itens na proporção dos fatores; cada item fica com seu tamanho base mais a sua fatia: https://developer.mozilla.org/en-US/docs/Web/CSS/flex-grow. Com fatores 1, 2 e 4, a *sobra* recebida segue 1 : 2 : 4, mas a largura final só fica 4× maior se o tamanho base for zero (`flex-basis: 0`, como em `flex: 4`). O slide diz certo ("2 vezes mais espaço extra"); a fala ("4 vezes maior") não.
- **Por que "nada" mudava.** `[external]` Numa linha sem sobra (itens ocupando ou passando da largura, com `nowrap`), não há espaço livre para distribuir, qualquer que seja o fator. Com `wrap`, sobra espaço nas linhas que não enchem, e aí o grow age.
- **"Distância do conteúdo para a borda".** O que cresce é a largura do item no eixo principal. Como o texto está centralizado, parece que aumenta o espaço entre o conteúdo e a borda.
- **"Prioridade".** Não é prioridade, é proporção: todos os itens com fator > 0 crescem ao mesmo tempo.
- **OBS do slide.** `[external]` Mais preciso: se os itens com `flex-grow` absorvem toda a sobra, não resta espaço para o `justify-content` distribuir; ele volta a agir quando há sobra (por exemplo, itens com `max-width`).
- **Por que 8 itens não quebram.** Depende do tamanho base de cada item (`flex-basis`/`width` e o conteúdo), não de uma propriedade que falte. A aula seguinte cobre `flex-basis`.
- **NLW.** Na NLW #1, `flex: 1` aparece como "preenche automaticamente todo o espaço" ([[wiki/concepts/flexbox]]). `flex: 1` é `flex-grow: 1` com `flex-basis: 0%`.

## Open Questions

- `date_published` vazio (~2022, inferido pelo resto do curso).

## Raw quotes

- "O grow não é necessariamente aumentar, é aumentar quando está disponível."
- "A grande sacada do flex-grow é quando eu tenho flex-grows diferentes."
- "Ah, porque não tinha quebrado."
