---
type: source
title: "Flex-basis: o tamanho base dos flex-itens, auto, 0 e valor fixo (FrontPUSH, módulo de Flexbox)"
aliases: ["FrontPUSH flexbox aula 07", "Flex-basis FrontPUSH", "aula 07 módulo Flexbox FrontPUSH"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, flexbox, flex-basis, flex-grow, flex-item, cards, design-responsivo, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-flex-basis-tamanho-base-flex-itens.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Flex-basis: o tamanho base dos flex-itens, auto, 0 e valor fixo (FrontPUSH, módulo de Flexbox)

## TL;DR

Aula 07 do módulo de [[wiki/concepts/flexbox]] do [[wiki/entities/frontpush|FrontPUSH]], de [[wiki/entities/nasser|Násser]]. Segunda propriedade dos itens: `flex-basis` ([[wiki/concepts/flex-grow-shrink-basis]]), que "quer padronizar o tamanho do flex-item". Três modos:

- **`auto`** (padrão): sem tamanho fixo, cada item "vai ajustar de acordo com o conteúdo"; conteúdo maior, item maior. Não "tenta padronizar".
- **`0`**: "agora ele vai começar a se importar"; quebra os textos para deixar os itens "o mais uniforme possível". Uma palavra longa sem espaço não quebra.
- **Valor fixo** (100 px, 200 px): "a base dos meus flex-itens é de 100 pixels, ou seja, é o mínimo que você pode ir". Com `wrap`, os itens descem de linha quando não cabem mais na base, e o `flex-grow` reparte a sobra. Daí "controlar o tamanho dos cards [...] em vários tamanhos de tela" ([[wiki/concepts/design-responsivo]]).
- Diz que o `flex-grow` "é mais ligado ao padding" do que ao conteúdo (ver Precisões).

## Key Claims

### O que é

- "O flex-basis, como o próprio nome já anuncia, ele quer definir uma unidade na base dos flex-itens, quer padronizar o tamanho do flex-item."
- Ponto de partida: a demo da aula 06, com o item 11 em `flex-grow: 2` e o 12 em `4` ([[wiki/sources/frontpush-flex-grow-crescer-espaco-disponivel]]). "Ele sempre vai aproveitar o espaço que está disponível, porque, por padrão, ele vem com o stretch."
- Slide (print enviado com a transcrição): "Indica o tamanho inicial do flex item antes da distribuição do espaço restante." `auto` "faz com que a largura da base seja igual a do item. Se o item não tiver tamanho especificado, o tamanho será de acordo com o conteúdo." `unidade` "pode ser em %, em, px e etc." `0`: "Se o grow for igual ou maior que 1, ele irá tentar manter todos os elementos com a mesma largura, independente do conteúdo (por isso 0 é o valor mais comum do flex-basis)."

### Flex-basis auto

- "O valor padrão dele é auto. [...] Se eu não definir tamanho fixo, ele vai ajustar de acordo com o conteúdo." "Item 2, item 3 e item 4 têm exatamente o mesmo tamanho, que é a palavra item e o algarismo"; enchendo o item 1 e o 5 de números, eles crescem.
- "Ele vai crescer sem se importar com o tamanho, a padronização ou a uniformidade dos flex-itens."

### Flex-grow x flex-basis

- "O flex-grow não é diretamente ligado ao conteúdo. Ele é mais ligado ao padding." Com o conteúdo maior, o espaço entre o texto e a borda "continuou do mesmo jeito": "os grows estão certinhos". Ver Precisões.
- Os itens 9 e 10, com o mesmo grow: "ele aumentou porque o conteúdo aumentou junto. E pelo fato do flex-basis estar no automático [...] ele não tenta padronizar o tamanho dos flex-itens."

### Flex-basis 0

- "Ele meio que vai fazer conta matemática para poder deixar o mais próximo possível", "tentar quebrar ao máximo".
- "Ele quebrou esse texto aqui para poder deixá-lo o mais curto possível. Como esse aqui é um string inteiro, ele não conseguiu quebrar de novo. Mas se eu [...] desse um espaço, ele ia quebrar de novo."
- "Por mais que esse aqui tenha um conteúdo muito maior em relação ao item 2, a discrepância entre eles diminuiu", com o mesmo `flex-grow`.

### Flex-basis com valor fixo

- `flex-basis: 100px`: "é o mínimo que você pode ir. Eu quero que você se esforce para deixar todos os meus flex-itens com um mínimo de 100 pixels." Com isso, "ele vai quebrar bem mais". Com 200, "todo mundo vai aumentar igual".
- "A gente começa a entender bem mais como a gente consegue controlar o tamanho dos cards e como eles conseguem variar em vários tamanhos de tela." Ver [[wiki/concepts/design-responsivo]].
- Com base 200 e grows diferentes: "não quer dizer que aqui tem 200, ele dividiu de forma que os flex-itens como um todo respeitem o flex-grow"; ele "respeita meio que ponderando agora as duas propriedades".
- Diminuindo a janela (com o inspecionar aberto), as diferenças entre 10, 11 e 12 encolhem ("4 pixels, [...] 2 pixels e [...] 1 ou 0"), até que "ele não vai mais conseguir manter a base de 200, aí vai quebrar".

### Método

- "É um conceito um pouco mais complexo [...] que eu aconselho fortemente a vocês treinarem", "buscarem mais referências tanto na W3C como em maiores exemplos". Ver [[wiki/concepts/pratica-deliberada]] e [[wiki/entities/w3c]].

## Entities

- [[wiki/entities/nasser]]: instrutor ("Mas, Násser").
- [[wiki/entities/frontpush]]: curso; módulo de Flexbox.
- [[wiki/entities/w3c]]: indicado como referência.

## Concepts

- [[wiki/concepts/flex-grow-shrink-basis]]
- [[wiki/concepts/flexbox]]
- [[wiki/concepts/design-responsivo]]
- [[wiki/concepts/css-grid]]
- [[wiki/concepts/unidades-de-medida-css]]
- [[wiki/concepts/pratica-deliberada]]

## Precisões e tensões com a wiki

- **O `flex-grow` não tem a ver com padding.** `[external]` Ele soma ao tamanho base de cada item uma fatia do espaço livre; o padding é parte do tamanho base. Como o texto está centralizado, a fatia extra aparece dos dois lados do texto e parece padding: https://developer.mozilla.org/en-US/docs/Web/CSS/flex-grow.
- **`flex-basis: 0` não faz "contas" para uniformizar.** `[external]` Com base 0, todo o espaço da linha vira espaço livre e é repartido pelos `flex-grow`; com fatores iguais, as larguras ficam iguais. O que impede a uniformidade total é o mínimo automático (`min-width: auto`): o item não fica menor que sua maior palavra, por isso "o string inteiro" não quebra: https://developer.mozilla.org/en-US/docs/Web/CSS/flex-basis. Com `min-width: 0` (ou `overflow` diferente de `visible`) a palavra transborda e as larguras se igualam.
- **Valor fixo não é mínimo.** `[external]` `flex-basis` é o tamanho *inicial*; com `flex-shrink: 1` (padrão), o item pode ficar menor que ele. Com `flex-wrap: wrap`, porém, as linhas são montadas pelos tamanhos base, então os itens descem de linha antes de precisar encolher, e na prática a base age como mínimo (menos um item sozinho maior que o contêiner). Sem `wrap`, eles encolhem. Para um mínimo de verdade, `min-width`.
- **Cards responsivos.** O padrão da demo é `flex: 1 1 200px` com `flex-wrap: wrap`. `[external]` Ele tem um efeito colateral: a última linha, com menos cards, estica mais que as outras. `grid-template-columns: repeat(auto-fit, minmax(200px, 1fr))` mantém as colunas iguais em todas as linhas: https://developer.mozilla.org/en-US/docs/Web/CSS/repeat. Ver [[wiki/concepts/css-grid]].
- **"Na W3C".** A referência técnica do W3C é a especificação (https://www.w3.org/TR/css-flexbox-1/); para estudo, a MDN costuma servir melhor. Em outras aulas do curso, "W3C" era o W3Schools ([[wiki/entities/w3schools]]); aqui não dá para saber qual.

## Open Questions

- "O 9 e o 10 têm a quantidade de grow diferente", e logo depois "o grow do 9 e do 10 está exatamente o mesmo": a segunda frase bate com a demo (só 11 e 12 têm grow diferente).
- `date_published` vazio (~2022, inferido pelo resto do curso).

## Raw quotes

- "quer padronizar o tamanho do flex-item"
- "Como esse aqui é um string inteiro, ele não conseguiu quebrar de novo."
- "ele respeita meio que ponderando agora as duas propriedades"
