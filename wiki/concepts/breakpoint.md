---
type: concept
title: "Breakpoint"
aliases: ["breakpoints", "ponto de quebra", "media query breakpoint", "small medium large extra-large", "sm md lg xl xxl"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 3
tags: [ui, ui-design, layout, grid, responsividade, design-responsivo, breakpoint, breakpoints, media-query, resolucao, css]
skill: ux-ui-mentor
status: stub
---

# Breakpoint

Largura de tela em que o layout muda: número de colunas, margens, max-width do conteúdo, disposição e empilhamento dos blocos. Cada faixa entre dois breakpoints tem seu próprio [[wiki/concepts/grid-de-colunas|grid]]. É o mecanismo do [[wiki/concepts/design-responsivo]].

Em [[wiki/sources/grids-parte-1-colunas-bootstrap-8pt-fixo-fluido-adaptativo-responsivo]]: "é um valor de resolução onde eu falo para ele ler determinados estilos para poder aplicar a minha página". No CSS, vira uma media query, "uma cláusula para ele começar a ler determinada folha de estilo quando ele estiver abaixo de 960 pixels". Na landing page do [[wiki/entities/frontpush]], as colunas "quebraram justamente naquele breakpoint" ao passar para tablet ou celular.

## Quais valores

As aulas e as referências externas dão números diferentes:

| Origem | Valores |
|---|---|
| Grids parte 1 ([[wiki/sources/grids-parte-1-colunas-bootstrap-8pt-fixo-fluido-adaptativo-responsivo]]) | 960 px como exemplo de media query |
| Grids parte 2, slide ([[wiki/sources/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos]]) | small <576, medium 720, large 960, extra-large 1200 (na fala, "até 1440"); 1600 para TV |
| `[external]` Bootstrap 5 | breakpoints `sm` 576, `md` 768, `lg` 992, `xl` 1200, `xxl` 1400; containers de 540, 720, 960, 1140, 1320 |
| `[skill: ux-ui-mentor]` Escala comum da skill | 480, 768, 1024, 1280, 1536 |

### As faixas da aula

Em [[wiki/sources/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos]] (slide):

| Faixa | Largura | Dispositivo |
|---|---|---|
| Small | <576 | smartphones |
| Medium | 720 | tablets |
| Large | 960 | notebooks |
| Extra-large | 1200 (na fala, "até 1440") | PCs, desktops |

Acima disso, 1600 para TV; o teto que ele adota para desktop é 1440. O slide e a fala divergem no extra-large: 1200 no slide, "até 1440" na fala.

### Bootstrap

Em [[wiki/sources/grids-pratica-2-material-de-apoio-bootstrap-material-design-flexbox-grid]], o autor manda olhar os breakpoints do [[wiki/entities/material-design]] e do iOS, e diz que usou os do [[wiki/entities/twitter-bootstrap|Bootstrap]] ("o large, o extra large") nas aulas, "por ser muito utilizado na web".

`[external]` Bootstrap 5: `sm` 576, `md` 768, `lg` 992, `xl` 1200, `xxl` 1400 (o `xxl` é novo em relação ao 4.x); containers de 540, 720, 960, 1140, 1320 (https://getbootstrap.com/docs/5.3/layout/breakpoints/, https://getbootstrap.com/docs/5.0/layout/breakpoints/). O 720 e o 960 da aula batem com containers, não com breakpoints: os números do slide da parte 2 não são os breakpoints do Bootstrap 5, embora a aula diga seguir o Bootstrap.

## Colunas por faixa

"Oito colunas, 12 colunas, quatro colunas, então você percebe que sempre são esses números que a gente está sempre circundando" ([[wiki/sources/grids-pratica-2-material-de-apoio-bootstrap-material-design-flexbox-grid]]). Na parte 2, 12 / 6 / 4 colunas conforme a faixa ([[wiki/sources/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos]]).

`[skill: ux-ui-mentor]` A tabela da skill: 4 colunas abaixo de 768 px (mobile), 8 entre 768 e 1024 (tablet), 12 acima de 1024 (desktop). Ver [[wiki/concepts/grid-de-colunas]]. A contagem intermediária difere: 6 colunas na parte 2, 8 na skill.

## Resolução não é polegada

"Muita coisa se deve à resolução, não só a tamanho de tela": um monitor de 26" em Full HD tem menos pixels que um iMac de 27" com Retina 5K ([[wiki/entities/apple]]). O breakpoint olha para a largura em pixels, não para o tamanho físico ([[wiki/sources/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos]]).

`[external]` No CSS, o que conta são pixels CSS: uma tela Retina com `devicePixelRatio` 2 reporta metade da largura física às media queries (https://developer.mozilla.org/en-US/docs/Web/API/Window/devicePixelRatio). Por isso o iMac 5K se comporta como uma tela de cerca de 2560 px de largura.

## Decisão de conteúdo

`[skill: ux-ui-mentor]` "Breakpoints não são tamanhos de device — são pontos onde o layout quebra." Adicione um "quando o conteúdo pede, não para cobrir todos os devices". É a mesma razão da aula para preferir o responsivo ao adaptativo ([[wiki/concepts/layout-fixo-fluido-adaptativo-responsivo]]).

## Mobile-first x desktop-first

`[skill: ux-ui-mentor]` Mobile-first escreve o estilo base para a tela pequena e acrescenta com `@media (min-width: ...)`, por exemplo `@media (min-width: 768px)`; a skill o prefere ao desktop-first (`max-width`). O exemplo da aula ("abaixo de 960") é desktop-first, com `max-width`.

## Relação com outros conceitos

- [[wiki/concepts/design-responsivo]]: media queries e histórico; breakpoints são onde a resposta acontece, e o layout fluido muda de forma neles.
- [[wiki/concepts/layout-fixo-fluido-adaptativo-responsivo]]: o adaptativo vive de breakpoints; o fluido vive entre eles.
- [[wiki/concepts/design-adaptativo]]: um layout distinto para cada breakpoint.
- [[wiki/concepts/grid-de-colunas]]: colunas, gutter e margem mudam por breakpoint.
- [[wiki/concepts/mobile-layouts-responsivos]]: o equivalente nativo (WindowSizeClass, size classes).

## Key Sources

- [[wiki/sources/grids-parte-1-colunas-bootstrap-8pt-fixo-fluido-adaptativo-responsivo]] — definição, media query abaixo de 960 px, quebra na landing page do FrontPUSH
- [[wiki/sources/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos]] — faixas small/medium/large/extra-large; resolução x tamanho; teto de 1440, 1600 para TV
- [[wiki/sources/grids-pratica-2-material-de-apoio-bootstrap-material-design-flexbox-grid]] — breakpoints do Material Design, iOS e Bootstrap; 4, 8 e 12 colunas
