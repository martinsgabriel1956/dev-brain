---
type: concept
title: "Box Model (CSS)"
aliases: ["CSS box model", "content-padding-border-margin"]
date_created: 2026-07-28
date_updated: 2026-11-16
source_count: 2
tags: [browser, css, box-model, layout, html-semantico, shorthand-css, padding, margin]
skill: tech-mentor-frontend
status: draft
---
# Box Model (CSS)

Todo elemento renderizado é uma caixa composta por quatro camadas, de dentro para fora: **content**, **padding**, **border** e **margin**. Durante a etapa de [[wiki/concepts/reflow-layout|layout]], o browser calcula o tamanho final de cada caixa considerando essas camadas e o fluxo do documento — unidades relativas (`%`, `auto`) viram valores absolutos em pixels nesse momento.

## Tudo é caixa (aula de Básico CSS)

Em [[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]], [[wiki/entities/nasser|Násser]] faz do box model a tese do módulo: "tudo é caixa", toda tag "são caixas, são box, são divs". As propriedades de caixa são width, height, padding ("espaçamento interno", do conteúdo até a borda), margin ("a distância entre uma caixa e outra"), border e [[wiki/concepts/border-radius]]. Como a caixa tem quatro lados, padding e margin têm `-top`, `-right`, `-bottom`, `-left`, e o [[wiki/concepts/shorthand-css|shorthand]] segue o sentido horário a partir do topo. Medidas em [[wiki/concepts/unidades-de-medida-css|unidades]] fixas ou relativas. Mesma ideia do "tudo é div" da aula de grids ([[wiki/sources/grids-pratica-figma-12-colunas-alinhamento-blocos-equilibrio-menu]]).

`[external]` O que a aula não cobre (https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Box_model): (1) **`box-sizing`**: no padrão `content-box`, width e height não incluem padding e border, então padding aumenta a caixa; `border-box` inclui, e é o reset mais comum. (2) **Colapso de margens**: margens verticais de blocos adjacentes se fundem na maior, não se somam. (3) **Inline**: span, a e strong ignoram width e height. Confiança alta.

## Key sources
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]]
- [[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]] — tudo é caixa; width, height, padding, margin, border, radius; quatro lados; sem box-sizing
