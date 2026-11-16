---
type: concept
title: "Design Responsivo"
aliases: ['responsive design', 'media queries']
date_created: 2026-10-14
date_updated: 2026-11-15
source_count: 8
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

## Desenhar já pensando nos breakpoints

Em [[wiki/sources/grids-pratica-figma-12-colunas-alinhamento-blocos-equilibrio-menu]], a escolha do grid é de responsividade. Ele usa grid centralizado com max-width (1260) em vez de esticado, porque o esticado pede "uma série de breakpoints maior". E desenha em blocos: "eu já vou desenhando a minha interface interpretando como é que vai ser a caixinha, como é que vai ser a responsividade". Blocos iguais viram uma classe com flex-basis; pares viram flexbox dentro de flexbox. Ilustração deslocada para preencher a tela "é algo que você tem que se atentar depois que você voltar para o mobile".

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
- [[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]] — uma imagem por tamanho de tela
- [[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]] — imagem de ponta a ponta até 4K; explicar o comportamento ao dev
- [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]] — ícone de quadrado maior + menor para responsividade (desktop e mobile)
- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] — grid de 12 colunas para desktop; ver [[wiki/concepts/grid-de-colunas]] para colunas por breakpoint
- [[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]] — edição "W7": exportar tamanhos diferentes e carregar por media query; mobile, tablet e desktop
- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]] — mouse x dedo; botões não encolhem no mobile
- [[wiki/sources/grids-pratica-figma-12-colunas-alinhamento-blocos-equilibrio-menu]] — Center (max-width) para reduzir breakpoints; blocos que já viram classe e flexbox
