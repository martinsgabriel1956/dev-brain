---
type: concept
title: "flex-grow, flex-shrink e flex-basis"
aliases: ["flex-grow", "flex-shrink", "flex-basis", "fator de crescimento", "fator de encolhimento", "tamanho base flex", "espaço livre flex"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 6
tags: [frontend, css, flexbox, flex-item, layout]
skill: tech-mentor-frontend
status: stub
---

# flex-grow, flex-shrink e flex-basis

As três propriedades de tamanho do flex item ([[wiki/concepts/flex-container-e-flex-item]]). O navegador parte do tamanho base (`flex-basis`; `auto` usa `width`/`height` ou o conteúdo), soma os tamanhos base da linha e compara com o contêiner:

- **Sobra espaço**: a sobra é dividida entre os itens na proporção dos `flex-grow` (padrão `0`, não cresce).
- **Falta espaço**: o déficit é tirado na proporção dos `flex-shrink` (padrão `1`, ponderado pelo tamanho base), até o mínimo do conteúdo.

O shorthand `flex` junta os três: `flex: 1` = `1 1 0%`. `[external]` https://www.w3.org/TR/css-flexbox-1/#flexibility e https://developer.mozilla.org/en-US/docs/Web/CSS/flex.

## flex-grow no FrontPUSH (aula 06 do módulo de Flexbox)

Em [[wiki/sources/frontpush-flex-grow-crescer-espaco-disponivel]], [[wiki/entities/nasser|Násser]]: "o grow não é necessariamente aumentar, é aumentar quando está disponível". Com o mesmo fator em todos, "nada" muda; a graça é ter fatores diferentes. Na demo 1, 2, 4, ele diz que o item com 4 fica "4 vezes maior". `[external]` O que é 4 vezes maior é a fatia da sobra; a largura final só segue a proporção com `flex-basis: 0`.

## flex-basis no FrontPUSH (aula 07 do módulo de Flexbox)

Em [[wiki/sources/frontpush-flex-basis-tamanho-base-flex-itens]], [[wiki/entities/nasser|Násser]] mostra três modos: `auto` (padrão; o item segue o conteúdo), `0` (os itens ficam "o mais uniforme possível", menos o que uma palavra inteira impede) e valor fixo, que ele chama de "o mínimo que você pode ir". `[external]` A base é o tamanho inicial, não um mínimo: com `wrap`, os itens descem de linha antes de encolher, e por isso parece mínimo; sem `wrap`, encolhem (`flex-shrink: 1`). Com base 0, quem limita a uniformidade é o `min-width: auto` (a maior palavra). Ele também diz que o `flex-grow` "é mais ligado ao padding"; não é, ele reparte o espaço livre.

## flex-shrink e o atalho flex no FrontPUSH (aula 08 do módulo de Flexbox)

Em [[wiki/sources/frontpush-flex-shrink-e-flex-shorthand]], [[wiki/entities/nasser|Násser]] mostra que o `flex-shrink` (padrão 1) quase não aparece: com 1, 5, 6 ou 10, "a gente não enxerga nada"; `0` mantém a base ("esse 300 pixels forever"). `[external]` O motivo é o `flex-wrap: wrap` da demo: as linhas se formam pelo tamanho base, então não falta espaço para encolher; com `nowrap` o efeito aparece. E o encolhimento pesa `flex-shrink × flex-basis`, não só o fator. Depois apresenta `flex` (grow, shrink, basis; padrão `0 1 auto`; `flex: 1` = `1 1 0`) e a fórmula que mais usa: `flex: 1 1 300px`.

## flex-grow "no olho" (FrontPUSH, Sass)

Em [[wiki/sources/frontpush-for-while-each-sass]]: para reproduzir um bloco de 5 colunas do layout, com flexbox "a gente precisa estar utilizando o flex grow, e aí a gente vai verificando no olho [...] não é uma divisão muito exata". O argumento a favor de classes de grid.

## flex-grow 2 e 1 no projeto Nubank (FrontPUSH)

Em [[wiki/sources/frontpush-grid-system-sass-parte-1]]: os blocos do Nubank receberam `flex-grow` 2 e 1, conferidos "no olho mesmo"; "ele se aproxima, mas não tem a exatidão e precisão" de colunas de grid. `[skill: tech-mentor-frontend]` `flex-basis` em % (ou `flex: 0 0 41.66%`) teria dado a mesma precisão sem sair do flexbox.

## Key sources

- [[wiki/sources/frontpush-flex-grow-crescer-espaco-disponivel]]: flex-grow só age com espaço livre; demo 1, 2, 4
- [[wiki/sources/frontpush-flex-basis-tamanho-base-flex-itens]]: aula 07: flex-basis auto, 0 e fixo; base fixa + wrap como "mínimo" dos cards
- [[wiki/sources/frontpush-flex-shrink-e-flex-shorthand]]: aula 08: flex-shrink (só aparece sem wrap) e o shorthand flex; "sempre 1, 1, 300"
- [[wiki/sources/frontpush-flexbox-pratica-2-desafio-estrutura-de-divs]]: prática 2: `flex-wrap` + `flex-basis` como alternativa à media query para quebrar três colunas
- [[wiki/sources/frontpush-for-while-each-sass]]: "no olho" × classes de grid
- [[wiki/sources/frontpush-grid-system-sass-parte-1]]: flex-grow 2/1 "no olho" × grid
