---
type: concept
title: "Design Responsivo"
aliases: ['responsive design', 'media queries']
date_created: 2026-10-14
date_updated: 2026-11-15
source_count: 16
tags: [css, responsivo, mobile, historia]
skill: tech-mentor-frontend
status: draft
---

# Design Responsivo

Layout que se adapta automaticamente ao dispositivo. Raízes: media types do Opera (anos 2000), media queries (rascunhos 1997, oficiais no CSS3 em 2012), fim do layout por tabelas e fixação em 1024×768; acelerado pelo iPhone (320×480, telas verticais) e pelo toque, que originou a pesquisa de UX. Vem junto do minimalismo (Bauhaus) trazido pela Apple e dos frameworks de CSS ([[wiki/entities/twitter-bootstrap]]). Ver [[wiki/concepts/css]], [[wiki/concepts/mobile-layouts-responsivos]].

## Imagens por tamanho de tela

Exportar a mesma imagem em várias escalas (2x/1x desktop, 0,5x/0,3x mobile) e deixar o código escolher qual carregar evita baixar no celular a imagem grande que só seria redimensionada ([[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]]). Ver [[wiki/concepts/otimizacao-de-imagens]] (`srcset`, `<picture>`).

## Pensar nas outras telas

"Você já tem que pensar sempre não só na tela que você está projetando, mas também quais são as outras telas": imagem de ponta a ponta precisa aguentar um monitor 4K, ou o designer precisa explicar ao desenvolvedor o comportamento ([[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]]).

## Área clicável no mobile

Em [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]: "a precisão que eu tenho no mouse é muito maior do que a que eu tenho com o meu dedo". O botão não pode encolher na tela pequena; na [[wiki/entities/apple]], eles mantêm o tamanho. Ver [[wiki/concepts/area-clicavel]].

## Mesmo conteúdo, vários dispositivos

O grid serve para "o mesmo conteúdo estar disposto em vários dispositivos garantindo a acessibilidade e o consumo do conteúdo da melhor forma possível" ([[wiki/sources/interfaces-web-introducao-workflow-grids-pagemap-wireframes-style-guide]]). O [[wiki/concepts/style-guide]] documenta tipografia separada para desktop e mobile. Ver [[wiki/concepts/grid-de-colunas]].

## Dizer responsivo sem a palavra

Em [[wiki/sources/wireframes-pratica-2-page-map-por-referencias-hero-processo-cta]], Násser elogia o site de [[wiki/entities/jonas-miller]] por escrever "funciona em qualquer dispositivo" em vez de "design responsivo", porque muita gente não sabe o que a palavra quer dizer. `[skill: ux-ui-mentor]` É o princípio "claro" de UX writing: a palavra do ofício vira a do cliente.

## Fixo, fluido, adaptativo, responsivo

Em [[wiki/sources/grids-parte-1-colunas-bootstrap-8pt-fixo-fluido-adaptativo-responsivo]]: o responsivo "mistura o melhor de todos os mundos". Junta o fluido (larguras em porcentagem, seções que encolhem com a tela) e o adaptativo (media query que troca o estilo num [[wiki/concepts/breakpoint]], como 960 px). O fixo serve a uma tela só. Com tantos modelos de aparelho, fazer adaptativo "é praticamente suicídio", e o responsivo é "o queridinho". Mesmo assim, "isso nunca vai invalidar sempre você testar em vários tipos de dispositivos". Ver [[wiki/concepts/layout-fixo-fluido-adaptativo-responsivo]].

## Grid por dispositivo e resolução

Em [[wiki/sources/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos]]: 12 colunas no desktop, 6 no tablet, 4 (ou 6 em paisagem) no mobile ([[wiki/concepts/grid-de-colunas]]); blocos "na horizontal" que quebram "na vertical" são "a técnica do design fluido". Resolução não é polegada (iMac de 27" com Retina 5K); teto de 1440 para desktop, 1600 para TV. Ver [[wiki/concepts/breakpoint]].

## O horizontal que quebra na vertical

Em [[wiki/sources/grids-pratica-2-material-de-apoio-bootstrap-material-design-flexbox-grid]]: "aquele design que é horizontal e a gente sempre projeta ele para ele quebrar na vertical". Duas caixas lado a lado no desktop viram coluna no tablet; no mobile o formulário da home vira "um botãozinho", porque um formulário grande "pode atrapalhar o fluir". Exemplos: [[wiki/entities/dropbox]], [[wiki/entities/dribbble]]. Responsivo e adaptativo são "dois conceitos diferentes"; ver [[wiki/concepts/design-adaptativo]] e [[wiki/concepts/breakpoint]].

## Desenhar já pensando nos breakpoints

Em [[wiki/sources/grids-pratica-figma-12-colunas-alinhamento-blocos-equilibrio-menu]], a escolha do grid é de responsividade. Ele usa grid centralizado com max-width (1260) em vez de esticado, porque o esticado pede "uma série de breakpoints maior". E desenha em blocos: "eu já vou desenhando a minha interface interpretando como é que vai ser a caixinha, como é que vai ser a responsividade". Blocos iguais viram uma classe com flex-basis; pares viram flexbox dentro de flexbox. Ilustração deslocada para preencher a tela "é algo que você tem que se atentar depois que você voltar para o mobile".

## Escala de fonte por tela

"Tamanho versus espaço": o Framer cai de 106/32 px para 45/23 px em tela menor; o style guide do [[wiki/entities/nubank]] em produção define h1–h3 em versão desktop e mobile ([[wiki/sources/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma]]). Ver [[wiki/concepts/escala-tipografica]]. `[skill: ux-ui-mentor]` `clamp()` faz isso sem breakpoints.

## Escala de texto por tela

"Se você deixar uma escala justamente muito grande, uma tela muito pequena, fica muito ruim" ([[wiki/sources/altura-de-linha-e-largura-do-texto]]). A [[wiki/concepts/largura-do-texto]] também depende da tela: em telas largas, um container segura a coluna, como no NYT.

## Texto à esquerda

Em [[wiki/sources/alinhamento-e-espacamento-de-texto]], um dos porquês do [[wiki/concepts/alinhamento-de-texto|alinhamento à esquerda]] é a responsividade: "em todos os dispositivos móveis" a borda esquerda fica fixa e a direita é que se move, então o texto não muda de ponto de partida.

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
- [[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]] — uma imagem por tamanho de tela
- [[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]] — imagem de ponta a ponta até 4K; explicar o comportamento ao dev
- [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]] — ícone de quadrado maior + menor para responsividade (desktop e mobile)
- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] — grid de 12 colunas para desktop; ver [[wiki/concepts/grid-de-colunas]] para colunas por breakpoint
- [[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]] — edição "W7": exportar tamanhos diferentes e carregar por media query; mobile, tablet e desktop
- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]] — mouse x dedo; botões não encolhem no mobile
- [[wiki/sources/interfaces-web-introducao-workflow-grids-pagemap-wireframes-style-guide]] — grid para o mesmo conteúdo em vários dispositivos; tipografia desktop e mobile no style guide
- [[wiki/sources/wireframes-pratica-2-page-map-por-referencias-hero-processo-cta]] — "funciona em qualquer dispositivo" no lugar de "responsivo"
- [[wiki/sources/grids-parte-1-colunas-bootstrap-8pt-fixo-fluido-adaptativo-responsivo]] — fixo, fluido, adaptativo e responsivo; breakpoint de 960; testar em vários aparelhos
- [[wiki/sources/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos]] — 12/6/4 colunas; blocos horizontais que quebram na vertical; resolução x tamanho; teto 1440
- [[wiki/sources/grids-pratica-2-material-de-apoio-bootstrap-material-design-flexbox-grid]] — empilhar no tablet, suprimir no mobile; responsivo x adaptativo
- [[wiki/sources/grids-pratica-figma-12-colunas-alinhamento-blocos-equilibrio-menu]] — Center (max-width) para reduzir breakpoints; blocos que já viram classe e flexbox
- [[wiki/sources/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma]] — escalas tipográficas desktop e mobile
- [[wiki/sources/altura-de-linha-e-largura-do-texto]] — escala grande em tela pequena; container limita a largura
- [[wiki/sources/alinhamento-e-espacamento-de-texto]] — esquerda fica fixa entre telas; texto à esquerda facilita a responsividade
