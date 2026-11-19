---
type: concept
title: "Breakpoint"
aliases: ["breakpoints", "ponto de quebra", "media query breakpoint", "small medium large extra-large", "sm md lg xl xxl"]
date_created: 2026-11-15
date_updated: 2026-11-19
source_count: 15
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

## Na NLW #1 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa um único breakpoint desktop-first, `@media (max-width: 900px)`: "de 0 até 900 pixels aplica-se regras específicas". Abaixo dele, a imagem de fundo sai para o lado, o conteúdo centraliza e o link do header desce. Depende da `meta viewport`. `[skill: tech-mentor-frontend]` mobile-first com `min-width` é o padrão recomendado.

## Na NLW #1, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] testa no Toggle Device Toolbar do DevTools (4K, laptop 1440, tablet, rotação) e cria duas regras novas: `@media (min-width: 1700px)` com o fundo em 40vw, achado olhando a tela "na hora que ele vai encostar", e `@media (max-height: 760px)` com `background-position-y: 200px`. É a primeira media query por altura da wiki. "Fizemos uma regra para altura e regras para largura."

## Na NLW #2, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]], os breakpoints do Proffy são 700 px (raiz 62,5% e página study no desktop) e 1100 px (landing em grid), todos com `min-width`. No Device Toolbar, a 1099 px nada muda e a 1100 px, "Puf!", o layout alarga.

## 960 e 720 num mixin (FrontPUSH, Sass)

Em [[wiki/sources/frontpush-mixin-e-content-sass]], os breakpoints do curso (960 para tablet, 720 para mobile, ambos `max-width`) viram mixins `responsive-tablet` e `responsive-mobile`. `[skill: tech-mentor-frontend]` Melhor um mapa `$bps` e um mixin parametrizado; abaixo de 720 as duas regras valem, e vence a que vem por último.

## Escala xl–xs do projeto Nubank (FrontPUSH)

Em [[wiki/sources/frontpush-if-else-sass]]: `xl` acima de 1440, `l` 1140–1440, `m` 960–1140, `s` abaixo de 960, `xs` abaixo de 540, escolhidos por `@if` num mixin de layout com `@content`.

## Na NLW #2, dia 1 (Diego Fernandes)

1100 px para a landing ("cada layout é um layout diferente", sem regra fixa) e 700 px para raiz, listagem e header. Diego cita 1366 px como a menor tela comum de desktop. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]].

## Mixin responsive do projeto Nubank (FrontPUSH, Sass aula 10)

Em [[wiki/sources/frontpush-grid-system-sass-parte-1]]: `xl` > 1440, `l` 1140–1440, `m` 960–1140, `s` < 960, `xs` < 540, "boas divisões com base no próprio sistema de grids do Bootstrap", mas "na maioria das vezes, eu simplesmente aplico de 960 pixels para baixo". `[external]` 540/720/960/1140 são as larguras de container do Bootstrap 4; os breakpoints dele são 576/768/992/1200.

## 960 px nas classes de visibilidade (FrontPUSH, otimização aula 04)

Em [[wiki/sources/frontpush-otimizacao-de-imagens-mobile-desktop-classes-mixin]], o corte das classes `.desktop`/`.mobile` é o tamanho S do mixin `responsive`, que o instrutor primeiro diz ser 620 px e corrige para 960 ("menos que o contêiner M").

## Key Sources

- [[wiki/sources/grids-parte-1-colunas-bootstrap-8pt-fixo-fluido-adaptativo-responsivo]] — definição, media query abaixo de 960 px, quebra na landing page do FrontPUSH
- [[wiki/sources/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos]] — faixas small/medium/large/extra-large; resolução x tamanho; teto de 1440, 1600 para TV
- [[wiki/sources/grids-pratica-2-material-de-apoio-bootstrap-material-design-flexbox-grid]] — breakpoints do Material Design, iOS e Bootstrap; 4, 8 e 12 colunas
- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: max-width 900px, desktop-first
- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: min-width 1700 e max-height 760; Device Toolbar
- [[wiki/sources/frontpush-layout-css-botao-hover-flexbox-media-query]]: `@media screen and (max-width: 960px)` com `flex-direction: column`; "somente quando a tela [...] for menor ou igual a 960 pixels" (desktop-first)
- [[wiki/sources/frontpush-flex-direction-flex-wrap-flex-flow]]: `@media (max-width: 960px)` troca `flex-direction` para `column` (desktop-first); 720 px demora mais para quebrar
- [[wiki/sources/frontpush-flexbox-pratica-2-desafio-estrutura-de-divs]]: media query para "sumir com os itens" do menu e trocar por hambúrguer quando há muitos links
- [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]: NLW #2, dia 2: 700 e 1100 px com min-width
- [[wiki/sources/frontpush-mentoria-pratica-com-css-grid]]: mentoria de grid: `max-width: 960px` (desktop-first, mesmo valor da aula de flex-direction) troca o `grid-template-areas`
- [[wiki/sources/frontpush-mixin-e-content-sass]]: 960/720 como mixins `responsive-tablet`/`-mobile`
- [[wiki/sources/frontpush-if-else-sass]]: escala xl/l/m/s/xs (1440/1140/960/540)
- [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]: NLW #2, Diego, dia 1: 1100 e 700 px no Proffy em React
- [[wiki/sources/frontpush-grid-system-sass-parte-1]]: escala xl–xs; 540/960/1140 são containers do Bootstrap 4
- [[wiki/sources/frontpush-otimizacao-de-imagens-mobile-desktop-classes-mixin]]: FrontPUSH, otimização aula 04: breakpoint de 960 px
