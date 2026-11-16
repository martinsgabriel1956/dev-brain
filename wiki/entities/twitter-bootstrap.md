---
type: entity
title: "Twitter Bootstrap"
aliases: ['Bootstrap']
date_created: 2026-10-14
date_updated: 2026-11-15
source_count: 3
tags: [css, framework-css, twitter, historia]
skill: tech-mentor-frontend
status: draft
---

# Twitter Bootstrap

Framework de CSS (escrito em Less) do [[wiki/entities/twitter]]; por seu uso massivo, muitos sites "parecem feitos pelo mesmo designer". Ver [[wiki/concepts/design-responsivo]].

## Bootstrap Icons

O projeto também mantém o Bootstrap Icons, citado como plugin de ícones "muito legal" no Figma em [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]].

## Bootstrap Grid System

Em [[wiki/sources/grids-parte-1-colunas-bootstrap-8pt-fixo-fluido-adaptativo-responsivo]], um dos "dois mais utilizados" padrões de grid, ao lado da regra de oito pontos ([[wiki/concepts/grid-de-8-pontos]]): "estabelece grids em colunas para diferentes tipos de dispositivos e estabelece padrões de width". `[external]` No Bootstrap 5: 12 colunas e breakpoints em 576, 768, 992, 1200 e 1400 px (https://getbootstrap.com/docs/5.3/layout/breakpoints/). Ver [[wiki/concepts/grid-de-colunas]] e [[wiki/concepts/breakpoint]].

## Bootstrap Grid System

O grid de colunas que [[wiki/entities/nasser|Násser]] usa é "baseado no Bootstrap Grid System" ([[wiki/sources/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos]]): número de colunas por dispositivo para dar responsividade. `[external]` No Bootstrap 5, breakpoints de 576, 768, 992, 1200 e 1400 e containers de 540, 720, 960, 1140 e 1320 (https://getbootstrap.com/docs/5.3/layout/breakpoints/); o slide da aula parece misturar as duas listas. Ver [[wiki/concepts/grid-de-colunas]] e [[wiki/concepts/breakpoint]].

## Sistema de grids

Em [[wiki/sources/grids-pratica-2-material-de-apoio-bootstrap-material-design-flexbox-grid]], [[wiki/entities/nasser|Násser]] diz que baseou "alguns valores" das aulas no grid do Bootstrap ("o large, o extra large"), "por ser muito utilizado na web". O Bootstrap 5, comparado ao 4.5, adicionou "mais uma seção" e deixa mudar gutter e coluna. `[external]` Breakpoint `xxl` (≥ 1400 px) e classes `.g-*` de gutter: https://getbootstrap.com/docs/5.0/layout/grid/. A biblioteca Flexbox Grid implementa muitos desses conceitos com classes prontas. Ver [[wiki/concepts/breakpoint]].

## Grid de 12 colunas

Em [[wiki/sources/grids-pratica-figma-12-colunas-alinhamento-blocos-equilibrio-menu]], [[wiki/entities/nasser|Násser]] diz que prefere "o do Bootstrap" ao grid de 8 pontos padrão do Figma, e configura 12 colunas. As medidas dele (colunas fixas de 72, gutter de 36, max-width 1260) não são as do framework. `[external]` No Bootstrap 5, as colunas são fluidas, o gutter é de 1,5rem e o maior container tem 1320 (https://getbootstrap.com/docs/5.3/layout/containers/).

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]] — plugin Bootstrap Icons no Figma
- [[wiki/sources/grids-parte-1-colunas-bootstrap-8pt-fixo-fluido-adaptativo-responsivo]] — Bootstrap Grid System como padrão de colunas por dispositivo
- [[wiki/sources/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos]] — Bootstrap Grid System como base do grid de colunas
- [[wiki/sources/grids-pratica-2-material-de-apoio-bootstrap-material-design-flexbox-grid]] — grid de referência das aulas; 4.5 x 5
- [[wiki/sources/grids-pratica-figma-12-colunas-alinhamento-blocos-equilibrio-menu]] — "eu prefiro o do Bootstrap": 12 colunas no Figma
