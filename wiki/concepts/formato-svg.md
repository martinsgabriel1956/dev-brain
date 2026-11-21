---
type: concept
title: "SVG (Scalable Vector Graphics)"
aliases: ["svg", "scalable vector graphics", "imagem vetorial", "vector image"]
date_created: 2026-07-29
date_updated: 2026-11-21
source_count: 24
tags: [formatos-de-imagem, svg, vetorial, frontend]
skill: cs-fundamentals
status: stub
---

# SVG

Formato criado pelo W3C em 2001, estruturalmente diferente de todos os formatos raster (JPEG, PNG, GIF, WebP, HEIC, AVIF). Em vez de armazenar uma grade de pixels, armazena **instruções matemáticas** — linhas, curvas, formas geométricas e preenchimentos. É essencialmente uma "receita de desenho" em vez de uma foto do resultado já pronto.

## Por que isso importa

Como o conteúdo é reconstruído a partir de equações, um SVG pode ser ampliado infinitamente sem perda de nitidez — o mesmo arquivo serve para um ícone de 32px ou para um outdoor. É por isso que a maioria dos sites modernos usa SVG para logotipos, ícones e elementos de interface: ocupa pouco espaço e se adapta a qualquer resolução de tela sem precisar de múltiplos assets por densidade de pixel.

## Ver também

- [[wiki/concepts/formato-png]], [[wiki/concepts/formato-jpeg]] — contraponto raster: pixels fixos, escala com perda de nitidez

## Na prática de UI

[[wiki/entities/nasser|Násser]] manda usar SVG para ícones, ilustrações e backgrounds, e reserva a fotografia realista para formatos raster. Demonstração no [[wiki/entities/figma]]: um ícone de 64×64 escalado para 96 mantém as proporções, e o SVG exportado, aberto no VS Code, é "somente alguns números" num plano cartesiano, um arquivo de bytes. No [[wiki/entities/frontpush]] todas as animações são SVG ([[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]]).

Na parte 2, ele chama ícone em PNG de "modelo mais arcaico": se dá para fazer no Figma e não é foto realista, vetorize, "principalmente logo"; logo de cliente em baixa definição se refaz com a Pen Tool ([[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]]).

`[skill: ux-ui-mentor]` Trade-off de implementação: SVG inline renderiza no navegador junto do HTML; via `<img>` ganha cache.

## Ilustrações e cor da marca

Na parte 4, SVG é "o formato mais adequado para ilustrações" e "imprescindível" porque permite trocar as cores: no [[wiki/entities/undraw]], o hexadecimal da marca recolore todas as ilustrações ([[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]]). Ver [[wiki/concepts/ilustracoes-em-interfaces]].

## Tamanho de ícone

Na parte 2 da aula de ícones ([[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]]): "o tamanho não é a coisa que mais importa" porque o ícone "deve ser exportado como SVG" e o vetor escala; pode desenhar em 24×24 e usar em 56. Ressalva: o Material 3 pede desenhar para 100% e oferece tamanhos ópticos (20, 24, 40, 48dp), porque o stroke escala junto (inferência do agente; https://m3.material.io/styles/icons/designing-icons).

## Caminhos manipuláveis por CSS e motion

Para [[wiki/entities/nasser|Násser]], SVG é "o grande queridinho" e "só alegria": não perde resolução, é leve e cada elemento é um caminho separado que o CSS manipula. Quase todas as ilustrações e animações dele (site, landing page, criações do FrontPUSH no Instagram) são SVG, com o caminho já traçado no Figma pensando na animação ([[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]]). `[external]` O CSS da página só alcança os `<path>` com o SVG inline; via `<img>` ou `background-image` ele é opaco.

## O SVG por dentro

Na edição "W7", [[wiki/entities/nasser|Násser]] abre no VS Code um mockup exportado do Figma (2KB): `defs` com o gradiente linear, filtros "inclusive de sombra" configurados via código, um ID ("paint-linear") aplicado aos caminhos (círculos, retângulos) e preenchimentos em hex. "Por isso que é leve", e por ter tags o CSS manipula: "a magia do Motion surgiu daqui" ([[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]]). `[external]` Filtros SVG são rasterizados pelo navegador e custam mais que caminhos simples.

## Vetorizar à mão

Na edição "W7", [[wiki/entities/nasser|Násser]] mostra que os ícones animados dele são vetores traçados no Figma com a [[wiki/concepts/vetorizacao-com-pen-tool|Pen Tool]] e a Bend Tool sobre uma imagem de referência, com o mínimo de pontos, e depois exportados "tudo, tudo, tudo para SVG" ([[wiki/sources/imagens-e-ilustracoes-vetorizar-icones-figma-pen-tool-bend-tool]]).

## Legibilidade de ícones

Na aula teórica de ícones "W7" ([[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia]]), o SVG é metade da legibilidade (a outra é a simplicidade): o ícone "pode ser colocado em vários tamanhos e resoluções diferentes" sem perder resolução.

## Na NLW #1 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa SVG para fundo e ícones do Ecoleta: o arquivo "é todo escrito em formato de texto" e "se adapta a telas de diversos tamanhos".

## Na NLW #1, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] edita o SVG à mão para colorir um ícone: a seta de voltar herda preto porque o `stroke` é `currentColor`, e ele cola o `stroke` verde do `log-in.svg`.

## Na NLW #2, dia 4 (Diego Fernandes)

O RN "não lê SVG" sem `react-native-svg`, então o app usa PNG; o SVG faria falta para tingir ícones, o que a aula resolve com fonte de ícones. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]].

## Vetorizar antes de tudo (FrontPUSH, otimização aula 03)

Em [[wiki/sources/frontpush-otimizacao-de-imagens-svg-webp-lazy-loading]]: "é texto, texto é muito mais leve", estica sem perder resolução e "é manipulável pelo CSS"; logo da Adidas vetorizado pelo plugin Image Tracer do Figma. Precisões: o tamanho depende do número de pontos (tracer gera pontos demais; usar SVGO e o SVG oficial da marca), e o CSS só alcança o SVG inline, não o `<img src>`.

## SVG inline infla o DOM (FrontPUSH, otimização aula 06)

Em [[wiki/sources/frontpush-relatorio-pagespeed-imagens-render-blocking-dom-regra-80-20]]: "um SVG que está com mil camadas de gradiente" dispara o aviso de DOM grande. Só o SVG inline entra no DOM (cada `<path>`, `<g>`, `<stop>` é um nó); via `<img>` ou `background-image` é um nó só. Sprite com `<symbol>` + `<use>` e SVGO reduzem o markup.

## SVG como base do motion (FrontPUSH, motion aula 01)

Em [[wiki/sources/frontpush-introducao-motion-design-css-animations-grade-do-curso]], a "esmagadora maioria" das animações do site de Násser é SVG, "animações vetorizadas", e o SVG "no fundo é tags HTML", por isso o CSS o manipula. Precisão: SVG é XML com namespace próprio; inline, vira nós do DOM e o CSS da página alcança `fill`, `stroke`, `stroke-dasharray` e `transform`. Propriedades do SVG são um módulo do mini curso ([[wiki/concepts/motion-design]]).

## SVG para otimizar e desenhar no scroll (FrontPUSH, motion aula 02)

Em [[wiki/sources/frontpush-como-usar-o-motion-vantagens-boas-praticas-pontos-de-atencao]], Násser compensa o site pesado de motion com "SVGs em todas as minhas páginas" e o mínimo de imagens, e mostra SVG desenhado em linhas no scroll (técnica usual: `stroke-dasharray` + `stroke-dashoffset`). Tensão com a aula 06 de otimização: SVG inline com muitos nós infla o DOM.

## matrix no SVG (FrontPUSH, básico CSS aula 01)

Em [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]]: "quando você bater o olho nessa propriedade matrix, em algum objeto SVG, você já fala, ele está aplicando a propriedade transform" ([[wiki/concepts/transform-matrix-css]]). `[external]` Em elementos SVG, o `transform-origin` padrão é `0 0`, não o centro: o `rotate` gira em torno do canto.

## transform-origin em SVG (FrontPUSH, básico CSS aula 02)

Em [[wiki/sources/frontpush-propriedade-transform-parte-2-transform-origin-transform-style-preserve-3d]], o `transform-origin` "é muito importante para quando a gente estiver falando de SVGs". `[external]` Em SVG o padrão é `0 0`; `transform-box: fill-box` + `transform-origin: center` gira a forma no lugar ([[wiki/concepts/transform-origin-css]]).

## Definição e por que usar (FrontPUSH, propriedades SVG aula 01)

Em [[wiki/sources/frontpush-propriedades-svg-introducao-o-que-e-por-que-usar]], [[wiki/entities/nasser|Násser]] abre o módulo de SVG: "vetorial no formato XML que suporta animações", "adimensional", "pense como um espelho do Figma" (export "não muda em nada"), elementos separados manipuláveis pelo CSS, filtros ("Liquid Motion"), árvore no DOM, "Photoshop da web" e [[wiki/concepts/stroke-svg|stroke]] com pontas redondas e dash array. Única desvantagem citada: "precisa estar no estilo inline". Precisões: "mais leve" depende do número de pontos; o export do Figma não é responsivo por causa de `width`/`height` fixos (manter o `viewBox`); background blur não tem filtro SVG equivalente; *gooey* = `feGaussianBlur` + `feColorMatrix`.

## Quatro formas de inserir (FrontPUSH, propriedades SVG aula 02)

Em [[wiki/sources/frontpush-como-usar-svg-img-background-object-inline]]: `<img>` (ícones estáticos, "não tem edição no DOM"), `background-image` (altura fixa), `iframe`/`object`/`embed` ("muito ruim") e inline ("o módulo que eu mais utilizo"; preço: "volume de código"). SVG de 8KB contra PNG de 728KB, "91 vezes mais leve"; suporte em quase tudo no Can I Use. Tabela completa, com sprite `<use>` e data URI, em [[wiki/concepts/formas-de-inserir-svg]].

## Estrutura por dentro (FrontPUSH, propriedades SVG aula 03)

Em [[wiki/sources/frontpush-estrutura-svg-viewport-viewbox-formas-basicas-path-defs]]: viewport × viewBox ([[wiki/concepts/viewbox-svg]]), formas básicas (`rect`, `circle`, `ellipse`, `line`, `polyline`, `polygon`), [[wiki/concepts/path-svg]] com `M`/`L`/`A`/`Z`, `fill` em vez de `background`, e `defs` com filtros e gradientes chamados por ID. Precisões: Y cresce para baixo; `background` não pinta formas SVG; `fill`/`stroke` no atributo são CSS de especificidade zero, que a folha de estilo sobrescreve; `filter0_d` repete entre exports.

## Key Sources

- [[wiki/sources/historia-dos-formatos-de-imagem]]
- [[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]] — SVG para ícones, ilustrações e backgrounds; ícone escalado no Figma
- [[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]] — ícone em SVG em vez de PNG; vetorizar logo de cliente com a Pen Tool
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]] — SVG para ilustrações; recolorir com o hexadecimal da marca
- [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]] — ícone em SVG escala, então o tamanho de desenho importa pouco
- [[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]] — SVG como base do motion do autor; caminhos manipuláveis por CSS
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-compreensao-consistencia-svg-tinyimage]] — preferir sites que exportam SVG; recolorir no unDraw com o hex da marca
- [[wiki/sources/imagens-e-ilustracoes-pratica-figma-importar-editor-plugins-exportacao]] — plugin de ondas que gera SVG; export de ícone dentro de frame
- [[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]] — SVG por dentro: defs com gradiente linear e filtros de sombra, ID aplicado aos caminhos, hex; manipulável por CSS; mockup exportado com 2KB
- [[wiki/sources/imagens-e-ilustracoes-vetorizar-icones-figma-pen-tool-bend-tool]] — vetorizar ícone de telefone com Pen Tool e Bend Tool e exportar em SVG
- [[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia]] — ícone legível = simples + SVG
- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]] — Feather exporta SVG ("sempre isso é muito bom"); ícone do módulo "propriedade do SVG"
- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: fundo e ícones do Ecoleta
- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: stroke currentColor trocado à mão
- [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]]: NLW #2, Diego, dia 4: PNG no lugar de SVG no app
- [[wiki/sources/frontpush-otimizacao-de-imagens-svg-webp-lazy-loading]]: FrontPUSH, otimização aula 03: SVG primeiro; Image Tracer
- [[wiki/sources/frontpush-relatorio-pagespeed-imagens-render-blocking-dom-regra-80-20]]: FrontPUSH, otimização aula 06: SVG inline e DOM grande
- [[wiki/sources/frontpush-introducao-motion-design-css-animations-grade-do-curso]]: FrontPUSH, mini curso de CSS Animations, aula 01: SVG como base do motion; "no fundo é tags HTML"
- [[wiki/sources/frontpush-como-usar-o-motion-vantagens-boas-praticas-pontos-de-atencao]]: FrontPUSH, mini curso de CSS Animations, aula 02: SVG como otimização e line drawing no scroll
- [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 01: matrix em SVG exportado; transform-origin 0 0 em SVG
- [[wiki/sources/frontpush-propriedade-transform-parte-2-transform-origin-transform-style-preserve-3d]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 02: transform-origin "muito importante" em SVG; transform-box
- [[wiki/sources/frontpush-propriedades-svg-introducao-o-que-e-por-que-usar]]: FrontPUSH, mini curso de CSS Animations, propriedades SVG aula 01: SVG XML adimensional; espelho do Figma; desvantagem do inline
- [[wiki/sources/frontpush-como-usar-svg-img-background-object-inline]]: FrontPUSH, mini curso de CSS Animations, propriedades SVG aula 02: quatro formas de inserir; 8KB × 728KB
- [[wiki/sources/frontpush-estrutura-svg-viewport-viewbox-formas-basicas-path-defs]]: FrontPUSH, mini curso de CSS Animations, propriedades SVG aula 03: estrutura: viewBox, formas, path, defs, fill
