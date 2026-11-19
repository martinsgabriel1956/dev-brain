---
type: source
title: "Otimização de imagens, parte 2: imagem para mobile e para desktop (FrontPUSH)"
aliases: ["FrontPUSH otimização aula 04", "Otimização de Imagens pt.2", "módulo de otimização, aula 04"]
date_created: 2026-11-19
date_updated: 2026-11-19
source_count: 0
tags: [performance, web-performance, imagens, imagens-responsivas, srcset, picture, sass, mixin, breakpoint, display-none, pagespeed, curso, frontend]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-otimizacao-de-imagens-mobile-desktop-classes-mixin.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-19
---

# Otimização de imagens, parte 2: imagem para mobile e para desktop (FrontPUSH)

## TL;DR

Aula 04 do módulo de otimização do [[wiki/entities/frontpush|FrontPUSH]], cerca de 10 min, complemento "que eu esqueci de falar na aula passada" ([[wiki/sources/frontpush-otimizacao-de-imagens-svg-webp-lazy-loading]]). [[wiki/entities/nasser|Násser]] (não diz o nome nesta aula; autoria confirmada pelo usuário) trata do aviso do PageSpeed para servir imagens "de acordo com o tamanho do dispositivo".

- **O problema:** uma imagem horizontal de 1920×1080 serve ao desktop; no celular, "o Google [...] pode reclamar". Ideal: horizontal para desktop, vertical e menor para mobile. Redimensionar por CSS não adianta: "continua pesando a mesma coisa".
- **Nem sempre vale:** "às vezes dá muito trabalho fazer essa transformação para todas as imagens".
- **Forma 1, classes `.desktop` e `.mobile`:** com o mixin `responsive` do [[wiki/concepts/pre-processador-css|Sass]] e breakpoint em 960 px (abaixo do contêiner M), cada classe dá `display: none` no outro tamanho. Serve para imagem, menu ou "mil coisas": duas imagens (drone desktop e mobile) ou dois menus no HTML, um escondido.
- **Forma 2, [[wiki/concepts/mixin-sass|mixin]] dentro da regra:** a estilização do desktop em cima e a do mobile no `@include responsive(S)`, cada uma carregando a sua imagem. "No fundo elas são iguais", mas a primeira generaliza.
- **Imagens são "70%" do trabalho** de performance; o resto (SEO, indexação, animações, frames) vem depois. Próxima aula: o PageSpeed Insights ponto a ponto.

## Key Claims

- **O PageSpeed pede imagem por dispositivo.** Ele "fala muito sobre, por exemplo, disponibilize imagens que são de acordo com o tamanho do dispositivo". Evidência: o relatório citado, não mostrado nesta aula.
- **O Google deduz o dispositivo pela resolução.** "Automaticamente, pelos padrões, o Google já entende que essa resolução [1920 por 1080] é mais voltada para quando você acessa o website em um desktop."
- **Mobile pede outra imagem.** "Carregar uma imagem em formato horizontal para o desktop e uma imagem em formato vertical para o mobile [...] e, consequentemente, com uma resolução menor, porque os celulares são telinhas menores."
- **Diminuir na tela não diminui o arquivo.** "Às vezes você simplesmente diminui, redimensiona aquela imagem, só que ela continua pesando a mesma coisa [...] você poderia literalmente diminuir [...] a resolução daquela imagem, consequentemente diminuindo o peso."
- **É escolha, não regra fixa.** "Nem sempre eu realizo esse passo, nem sempre dá para realizar esse passo, porque depende da imagem."
- **Classes de visibilidade.** "Eu crio uma classe [...] chamada desktop", com o breakpoint "S, não, é 960. Eu deixo aqui menos que o contêiner M"; "eu dou include display none, ele vai simplesmente desaparecer". Retoma o mixin `responsive` de [[wiki/sources/frontpush-mixin-e-content-sass]] e os contêineres de [[wiki/sources/frontpush-grid-system-sass-parte-1]] ([[wiki/concepts/breakpoint]]).
- **Solução genérica.** "Dá pra fazer com imagem, dá pra fazer com programação, dá pra fazer com menu, dá pra fazer com mil coisas." Exemplo: `div.menu desktop` e `div.menu mobile`, cada um com a sua classe; imagens "drone desktop 1.jpg" e "mobile".
- **Mixin na própria regra.** "Estilização do desktop e aqui vai ser a estilização do mobile. E aqui você carrega a imagem que é do mobile e aqui em cima você carrega a imagem que é do desktop."
- **Imagens são a maior parte.** "Se você fizer o dever de casa das imagens, eu acredito que 70% já está feito", repetindo o "60%, 70%" da aula 03.

## Entities

- [[wiki/entities/nasser]]: instrutor (autoria confirmada pelo usuário).
- [[wiki/entities/frontpush]]: curso; aula 04 do módulo de otimização; artigos no Notion ("11 dicas, 35 dicas, 8").
- [[wiki/entities/google]]: PageSpeed Insights.
- [[wiki/entities/twitter-bootstrap]]: as classes `d-none`/`d-md-block` fazem o mesmo que `.desktop` e `.mobile`.

## Concepts

- [[wiki/concepts/otimizacao-de-imagens]]: imagem por dispositivo, `srcset`, `<picture>`.
- [[wiki/concepts/design-responsivo]], [[wiki/concepts/breakpoint]]: o corte em 960 px.
- [[wiki/concepts/mixin-sass]], [[wiki/concepts/pre-processador-css]]: o mixin `responsive`.
- [[wiki/concepts/display-css]]: `display: none` esconde, não deixa de baixar.
- [[wiki/concepts/densidade-de-pixels]]: o celular pede mais pixels do que a largura sugere.
- [[wiki/concepts/core-web-vitals]]: a imagem principal costuma ser o LCP.
- [[wiki/concepts/html-semantico]]: dois menus no HTML.

## Precisões e tensões com a wiki

- **`display: none` não impede o download.** Uma `<img>` escondida por CSS é baixada do mesmo jeito: o navegador começa a buscar a imagem ao ler o HTML, antes de aplicar o CSS. Com as classes `.desktop`/`.mobile`, o celular baixa as duas imagens, e a página fica mais pesada que com uma só. É o contrário do que a aula quer. Confiança alta.
- **A ferramenta certa é do HTML.** Para a mesma imagem em tamanhos diferentes, `srcset` + `sizes` no `<img>`: o navegador escolhe pela largura da tela e pela densidade de pixels. Para recorte diferente (horizontal no desktop, vertical no mobile, a "direção de arte" da aula), `<picture>` com `<source media="(max-width: 959px)" srcset="drone-mobile.jpg">`. Nos dois casos só uma imagem é baixada. A wiki já registra os dois em [[wiki/concepts/otimizacao-de-imagens]]. `[skill: tech-mentor-frontend]` Confiança alta.
- **A forma 2 funciona se a imagem estiver no CSS.** Se "carregar a imagem" for `background-image` dentro do `@include responsive(S)`, o navegador só baixa a do media query que vale; aí as duas formas não são "iguais no fundo": a do mixin economiza e a das classes não. O custo do `background-image` é que o navegador só descobre a imagem depois do CSS, o que atrasa o LCP se for a imagem principal; e imagem de conteúdo perde o `alt`. Confiança alta.
- **O PageSpeed não lê a orientação.** A auditoria "Dimensione as imagens corretamente" (Properly size images) compara o tamanho do arquivo com o tamanho em que a imagem aparece na tela, multiplicado pela densidade de pixels. Não "entende" que 1920×1080 é de desktop; acusa qualquer imagem bem maior que o espaço onde é mostrada, em qualquer dispositivo. Confiança alta.
- **Celular não quer necessariamente "resolução menor".** Com densidade 2× ou 3× ([[wiki/concepts/densidade-de-pixels]]), uma imagem que ocupa 400 px de largura no celular precisa de 800 a 1200 px reais para ficar nítida. Menor que 1920, sim, mas não "de celular". O `srcset` com descritores `w` resolve isso sozinho. Confiança alta.
- **Dois menus no HTML.** Duplicar o menu e esconder um com CSS funciona para leitor de tela (o `display: none` some da árvore de acessibilidade), mas duplica links para buscador e o peso do HTML. O comum é um menu só, com o layout mudando por media query. `[skill: tech-mentor-frontend]` Confiança média.
- **As classes são utilitárias conhecidas.** `.desktop` e `.mobile` equivalem a `d-none d-lg-block` do [[wiki/entities/twitter-bootstrap|Bootstrap]] ou `hidden lg:block` do Tailwind; servem para layout, não para imagem pesada.
- **"Parte que a gente tá falando sobre hospedagem".** Lapso: o módulo é de otimização.
- **"S, 620 pixels. [...] S, não, é 960."** O próprio falante corrige o breakpoint; fica 960 px.

## Open Questions

- A forma 2 usa `background-image` ou `<img>`? A legenda não diz; a resposta muda se ela economiza bytes.
- O que vem nas "aulas de animações" deixadas "mais para o final"?
- Quais são os artigos do Notion ("11 dicas, 35 dicas, 8")? Não nomeados.

## Raw quotes

- "disponibilize imagens que são de acordo com o tamanho do dispositivo"
- "Nem sempre eu realizo esse passo, nem sempre dá para realizar esse passo"
- "eu dou include display none, ele vai simplesmente desaparecer"
- "Dá pra fazer com imagem, dá pra fazer com programação, dá pra fazer com menu, dá pra fazer com mil coisas."
- "ela continua pesando a mesma coisa que aquela imagem grande"
- "se você fizer o dever de casa das imagens, eu acredito que 70% já está feito"
