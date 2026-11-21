---
type: source
title: "Estrutura do SVG: plano cartesiano, viewport e viewBox, formas básicas, path e defs (FrontPUSH)"
aliases: ["FrontPUSH motion, propriedades SVG aula 03", "Estrutura dos SVG's", "Estrutura do SVG", "CSS Animations, propriedades SVG, aula 03"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 0
tags: [svg, viewbox, viewport, plano-cartesiano, rect, circle, path, fill, defs, filtros-svg, linear-gradient, stroke, ids-svg, figma, curso, frontend]
skill: tech-mentor-frontend
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-estrutura-svg-viewport-viewbox-formas-basicas-path-defs.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-21
---

# Estrutura do SVG: plano cartesiano, viewport e viewBox, formas básicas, path e defs (FrontPUSH)

## TL;DR

Terceira aula do módulo "Propriedades SVG's" do mini curso de CSS Animations do [[wiki/entities/frontpush|FrontPUSH]], cerca de 19,5 minutos, com dois slides, código no HTML e um SVG exportado do [[wiki/entities/figma|Figma]]. [[wiki/entities/nasser|Násser]] diz o nome ("Násser, por que é importante..."). Não é para escrever SVG à mão, é para "olhar para esse código [...] e pelo menos se guiar" na hora de manipular os elementos ([[wiki/concepts/formato-svg]]).

- **Plano cartesiano:** os quatro quadrantes, "muito se baseia nisso aqui" (ver Precisões: o SVG tem Y para baixo).
- **[[wiki/concepts/viewbox-svg|Viewport × viewBox]]**, "tela × resolução": viewport é `width`/`height` do `<svg>`, "a janelinha", e corta o que passa; `viewBox` (com B maiúsculo) é "zoom in e zoom out". Na prática ele não mexe no viewBox exportado, tira `width` e `height` e deixa o CSS dimensionar.
- **Formas básicas:** `<circle r cx cy>` (sem `fill` sai "uma bolinha preta"), `<rect x y width height>`, `line`, `polyline`; o slide traz também `ellipse` e `polygon`. Cor pelo `fill`, "muito parecido com o do Figma"; por `background` "talvez mude".
- **[[wiki/concepts/path-svg|path]]**, "um dos mais importantes": o que a [[wiki/concepts/vetorizacao-com-pen-tool|Pen Tool]] desenha. `M` move to, `L` line to, `A` arcs, `Z` close path; "aqui tem um C", que ele não sabe: "eu nunca entendi de fato [...] como se dá o caminho". O exemplo do Spotify faz transição de um path para outro.
- **`defs`:** filtros e efeitos do Figma (drop shadow, inner shadow, layer blur, background blur), `feBlend`, gradiente linear (`5DF777` → `1BC433`, `stop-color`, `x1 y1 x2 y2`) com ID chamado no `fill` do path ([[wiki/concepts/sombra-em-interfaces]]).
- **Propriedades exclusivas** (slide): `clip-rule`, `fill`, `fill-opacity`, `fill-rule`, `stroke`, `stroke-width`, `stroke-dasharray`, `stroke-linecap`, `stroke-dashoffset`, `stroke-opacity`; bordas são "um dos meus efeitos principais" ([[wiki/concepts/stroke-svg]]).
- **`transform` no SVG** "muito se assemelha" ao do CSS e está "na tag como propriedade direta" ([[wiki/concepts/transition-e-transform-css]]).
- **IDs repetidos:** "esse filter0_d aplica esse mesmo ID quando eu faço o export de outro SVG, isso pode dar conflito" ([[wiki/concepts/formas-de-inserir-svg]]).

## Key Claims

### Por que estudar a estrutura

- "Você deve se perguntar, Násser, por que é importante eu entender a estrutura do SVG se eu tenho o Figma [...] ele já vai cuspir o SVG prontinho [...] concordo plenamente com você."
- A aula é "para vocês entenderem os princípios e entender o que é cada tag": "isso aqui é o path, então caminho [...] isso aqui é um rect, então isso aqui é um quadrado, isso aqui é um grupo". Isso "vai agregar quando a gente estiver literalmente manipulando os elementos".
- "No SVG você vai ver que é um mundo tão vasto [...] muito difícil uma pessoa saber de todas as coisas"; "a maioria disso eu aprendi sozinho e não tenho medo de falar que eu tenho muito a aprender também, inclusive com vocês".

### Plano cartesiano

- "Ele é baseado em um plano cartesiano": primeiro quadrante com X e Y positivos, segundo com X negativo e Y positivo, terceiro com os dois negativos, quarto com X positivo e Y negativo. Slide com os quadrantes 1Q a 4Q.

### Viewport e viewBox

- `path`, `rect`, "elas não são do HTML, são próprias do SVG [...] só faz sentido se você as colocar dentro da tag SVG"; "existem algumas [...] compartilhado com o CSS".
- "Viewport [...] é literalmente a div, como se fosse uma caixinha": `<svg>` com `width` e `height` de 300 px e `style="border: 1px solid white"`, "a parte literalmente da janelinha do nosso SVG".
- `<circle>`: "primeiro tem que colocar o raio", depois `cx` e `cy`; raio 50 em (50, 50) fica "uma bolinha preta"; com raio 70, "a viewport como ele é uma janelinha, você vê que ele corta".
- `viewBox`: "o B tem que ser maiúsculo"; "o valor em X, o valor em Y e o tamanho da viewport multiplicado ou não". Com 300, 300, "não vai mudar absolutamente nada"; com 150, 150, "como se eu desse um zoom in"; com 600, 600, "zoom out".
- Analogia: "uma tela de 23 polegadas [...] Full HD [...] 2K [...] não está mudando o tamanho do viewport da tela, mas sim o zoom in e o zoom out". Slide: "Viewport vs. ViewBox ~ Tela vs. Resolução", "width & height", "zoom-in & zoom-out".
- "Quando exportar o SVG, ele vai estar sempre igual [...] 300, 300"; "não gosto de modificar esses valores". "Esse width e esse height aqui literalmente eu tiro e deixo ele sempre manipulado pelo CSS para poder ele se tornar fluido."

### Formas básicas e fill

- `<rect>`: "a posição em X, a posição em Y [...] e aí eu defino um width e um height"; com x negativo (menos 100) aparece onde está "o eixo 0 0".
- "Essas propriedades aqui de Fill não existem muito no CSS, porque no CSS quando você quer mudar o fundo de alguma coisa é background"; mudar por `background` com uma classe "talvez mude, se não me engano, muda"; "direto pela tag é pela propriedade Fill, que é muito parecido com o do Figma". "Aquele negócio de ser espelho do Figma [...] é muito real."
- `line` e `polyline` "para poder construir linhas"; "não vou dar muito ênfase em criar na mão as coisas, porque [...] a gente tem o Figma".

### O path

- "O path é quando você pega, por exemplo, um Pen Tool [...] coloca curva", "elementos retos [...] inclinados", "é na maioria dos elementos quando a gente está construindo [...] ilustrações livres".
- "O M significa move to, então literalmente pega dois pontos do plano cartesiano, percebe que sempre são pares, o X e o Y [...] vai de tal ponto a tal ponto [...] o ponto 711 e o ponto 435." "O L é o line to, o A é o arcs e o Z é closed path"; "aqui tem um C" e outras letras "que eu tenho que pesquisar".
- "Eu nunca entendi de fato [...] como se dá o caminho [...] eu faço pelo Figma", mas "todo o caminho é especificado aqui [...] descreve literalmente o desenho do objeto".
- Exemplo do Spotify, mais adiante no curso: "pego o código de um determinado caminho e peço para ele fazer a transição de um caminho para o outro, mas eu não entendo de fato o código".

### Defs, filtros, gradiente

- "Os defs ou símbolos": "geralmente são tags de filtro, são tags de efeito"; drop shadow, inner shadow, "layer blur e background blur são filtros, onde a gente muda a opacidade em conjunto com outro tipo de filtro". "Filtro, feBlend, para poder definir as sombras [...] effect, drop shadow".
- O "verdinho" é "um preenchimento gradiente", de `5DF777` para `1BC433` com `stop-color`; o gradiente "especifica o ID, ele especifica o X1, Y1, X2, Y2, ou seja, tudo no plano cartesiano". O path chama o ID no `fill`, "porque ele não é uma cor sólida".
- "Aqui em cima são colocados os elementos [...] um path, [...] um rect, [...] outro path, e aí para poder compor cada caminho desse com sombras, com efeitos, eles chamam todos aqui nos defs."

### Propriedades exclusivas e transform

- "A gente não mexe muito com o background, em SVG a gente mexe mais com o preenchimento", com propriedades "de rule, de opacidade, de preenchimento gradiente ou sólido e propriedade de stroke, que são as bordas"; "um dos meus efeitos principais que eu utilizo, sempre utilizo bordas".
- Método: "você vai colecionando exemplos na sua cabeça" ([[wiki/concepts/repertorio]]). Depois virão as propriedades de transform "quando você faz algum elemento que esteja em perspectiva".

### Vários SVGs no mesmo HTML

- "A gente vai precisar modificar alguns IDs aqui porque eles se coincidem [...] esse filter0_d aplica esse mesmo ID quando eu faço o export de outro SVG, isso pode dar conflito." Promete ensinar "essas substituições" (trecho de cerca de 11 s sem fala antes disso).

## Slides

**"Estrutura do SVG"** (logo triangular do mini curso): "Plano cartesiano" (eixos com 1Q, 2Q, 3Q, 4Q); "Viewport vs. ViewBox ~ Tela vs. Resolução" (width & height; zoom-in & zoom-out); "Formas básicas e Paths": `<rect x y width height>`, `<circle r cx cy>`, `<ellipse rx ry cx cy>`, `<line x1 y1 x2 y2 stroke="#333" stroke-width="2">`, `<polyline points="0,10 10,10 10,50" stroke="#333" stroke-width="2" fill="transparent">`, `<polygon points=...>`, `<path d="M45 L65 A65 ...">` com "M: Moveto, L: Lineto, A: Arcs, Z: ClosePath"; "Outros elementos: defs, symbols e etc."

**"Propriedades SVG's"**: "Algumas propriedades exclusivas SVGs": `clip-rule`, `fill`, `fill-opacity`, `fill-rule`, `stroke`, `stroke-width`, `stroke-dasharray`, `stroke-linecap`, `stroke-dashoffset`, `stroke-opacity`, "...".

## Entities

- [[wiki/entities/nasser]]: instrutor (diz o nome).
- [[wiki/entities/frontpush]]: curso.
- [[wiki/entities/figma]]: de onde vêm o SVG, os efeitos e os IDs.
- [[wiki/entities/cubic-bezier-com]]: o `C` do path é a mesma curva de Bézier cúbica das aulas de easing.

## Concepts

- [[wiki/concepts/viewbox-svg]]: viewport × viewBox (novo).
- [[wiki/concepts/path-svg]]: comandos do `d` (novo).
- [[wiki/concepts/formato-svg]]: estrutura geral, `fill`, `defs`.
- [[wiki/concepts/stroke-svg]]: propriedades de stroke no slide.
- [[wiki/concepts/formas-de-inserir-svg]]: IDs repetidos ao colar vários SVGs.
- [[wiki/concepts/sombra-em-interfaces]]: sombras do Figma viram filtros.
- [[wiki/concepts/background-css]]: `background` × `fill`.
- [[wiki/concepts/transition-e-transform-css]], [[wiki/concepts/transform-origin-css]]: atributo `transform` do SVG.
- [[wiki/concepts/unidades-de-viewport]]: "viewport" do SVG ≠ viewport da página.
- [[wiki/concepts/vetorizacao-com-pen-tool]]: Pen Tool gera paths.
- [[wiki/concepts/repertorio]]: "colecionando exemplos na sua cabeça".

## Precisões e tensões com a wiki

`[skill: tech-mentor-frontend]` (`references/frontend-animations.md`) ou `[external]` sem fetch, por conhecimento prévio das especificações SVG 1.1/SVG 2 e do MDN.

- **O SVG não usa o plano cartesiano da escola.** A origem é o canto superior esquerdo e o Y cresce para baixo: tudo que aparece na tela está no "quarto quadrante" com Y positivo. Mesma inversão que a aula de transform registrou ("aqui o eixo y é invertido") ([[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]]). Confiança alta.
- **`viewBox` tem quatro números:** `min-x min-y width height`, por exemplo `viewBox="0 0 300 300"`. Os dois primeiros deslocam a janela (pan); os dois últimos definem quantas unidades cabem no viewport (zoom). Não é "o tamanho da viewport multiplicado". O encaixe quando as proporções diferem é do `preserveAspectRatio` (padrão `xMidYMid meet`: centraliza e cabe inteiro), que explica o "ele só vai centralizar". Ver [[wiki/concepts/viewbox-svg]]. Confiança alta.
- **A analogia tela × resolução funciona com uma ressalva:** viewBox é um sistema de coordenadas, não pixels; mais unidades no mesmo viewport = desenho menor. Confiança alta.
- **Tirar `width`/`height` e manter o `viewBox`** é o que deixa o SVG fluido; sem viewBox não escala. Bate com a precisão da aula 01 ([[wiki/sources/frontpush-propriedades-svg-introducao-o-que-e-por-que-usar]]). Confiança alta.
- **`background` não pinta formas SVG.** `rect`, `circle` e `path` não são caixas CSS; só `fill` (e `stroke`) os pintam, com atributo ou com CSS (`.forma { fill: red }`). O `background` funciona no `<svg>` externo, que é uma caixa. O "talvez mude" não procede para as formas. Confiança alta.
- **Atributo × CSS.** `fill`, `stroke`, `opacity` e afins são *presentation attributes*: valem como CSS de especificidade zero, então qualquer regra CSS os sobrescreve. É por isso que o CSS da página consegue animar um SVG exportado com `fill="..."` no atributo. Confiança alta.
- **`M` não liga dois pontos.** `M711 435` move a "caneta" para **um** ponto (x 711, y 435) sem desenhar; o par é X e Y do mesmo ponto. Quem desenha são `L` (reta), `H`/`V` (horizontal/vertical), `C`/`S` (Bézier cúbica), `Q`/`T` (quadrática) e `A` (arco elíptico); `Z` fecha. Maiúscula = coordenada absoluta, minúscula = relativa. O `C` que ele não sabe é a Bézier cúbica: dois pontos de controle e o ponto final, a mesma curva do `cubic-bezier()` ([[wiki/concepts/path-svg]], [[wiki/entities/cubic-bezier-com]]). Confiança alta.
- **Morph de path (o exemplo do Spotify).** Interpolar um `d` em outro só funciona se os dois tiverem a mesma quantidade e o mesmo tipo de comandos; senão o navegador troca de uma vez. Hoje dá com a propriedade CSS `d: path("...")` em `@keyframes`/`transition` nos navegadores Chromium e no Firefox (no Safari, suporte a conferir), com SMIL `<animate attributeName="d">`, ou com bibliotecas (GSAP MorphSVG, flubber). Confiança média-alta.
- **`defs` guarda elementos, não "propriedades".** Tudo que não é desenhado direto: `linearGradient`/`radialGradient`, `filter`, `clipPath`, `mask`, `pattern`, `symbol`. É referenciado por `url(#id)` (`fill`, `filter`, `clip-path`) ou por `<use href="#id">`. `symbol` não precisa estar em `defs` e só aparece via `<use>`. Confiança alta.
- **O filtro de sombra do Figma** é uma cadeia: `feFlood`, `feColorMatrix` (pega o alfa: é o "muda a opacidade"), `feOffset`, `feGaussianBlur`, `feColorMatrix` (cor da sombra) e `feBlend` com resultados nomeados como `effect1_dropShadow` (o "effect, drop shadow" da fala). Confiança alta.
- **Background blur, refinando a aula 01.** Não existe primitivo de filtro SVG que borre o que está atrás. Versões recentes do Figma contornam com `<foreignObject>` + `backdrop-filter` do CSS dentro do SVG, o que só funciona inline e em navegadores que suportam. Confiança média.
- **Gradiente do Figma:** `linearGradient` com `gradientUnits="userSpaceOnUse"` e `x1 y1 x2 y2` nas coordenadas do desenho; cada `<stop>` tem `offset` e `stop-color`. Animar um gradiente pede mexer nos `stop-color` ou nos `x1…y2`, não no `fill` do path. Confiança alta.
- **`transform` como atributo ≠ CSS.** No atributo, números sem unidade e `rotate(ângulo cx cy)` com centro opcional; a origem é o `0 0` do SVG. Uma propriedade CSS `transform` no mesmo elemento substitui o atributo. Ver [[wiki/concepts/transform-origin-css]]. Confiança alta.
- **IDs repetidos: confirmado pelo autor.** O `filter0_d` (e `paint0_linear_...`) colide entre exports; a aula 02 já previa ([[wiki/sources/frontpush-como-usar-svg-img-background-object-inline]]). Renomear à mão, SVGO `prefixIds` ou componentes com IDs únicos. Confiança alta.
- **`fill-rule` e `clip-rule`:** `nonzero` (padrão) ou `evenodd`, decidem o que é "dentro" quando o path se cruza ou tem buracos (a letra "O"); `clip-rule` é o mesmo para `clipPath`. Confiança alta.
- **"Viewport" do SVG ≠ viewport da página.** O do SVG é a área do elemento `<svg>`; `vw`/`vh` medem a janela do navegador ([[wiki/concepts/unidades-de-viewport]]). Confiança alta.

## Open Questions

- "Quando você quiser mudar o viewport unity": provável "viewport ou o viewBox" (ou "units"); deixado literal.
- "É só seguir esse cronograma que eu escrevi aqui": provável "esquema" (o slide); deixado literal.
- "Meio que eu desce como se eu desse um zoom in": deixado literal.
- "O Z é closed path": o slide diz "ClosePath"; deixado literal.
- "Border" (legenda "drawKeyboarder") e "effect" (legenda "affection") são reconstruções de confiança média.
- O exemplo do Spotify e a técnica de troca de IDs ficam para aulas futuras.

## Continuação

Segue [[wiki/sources/frontpush-como-usar-svg-img-background-object-inline]], que prometeu "a estrutura do SVG". As próximas aulas continuam a estrutura "mais voltado à prática e exemplos".

## Raw quotes

- "você vai conseguir olhar para esse código aqui do SVG e pelo menos se guiar"
- "o viewport é o width e o height [...] e o viewbox é como se você desse um zoom in e um zoom out"
- "esse width e esse height aqui literalmente eu tiro e deixo ele sempre manipulado pelo CSS"
- "eu nunca entendi de fato, nossa, como se dá o caminho"
- "a maioria disso eu aprendi sozinho e não tenho medo de falar que eu tenho muito a aprender também"
- "esse filter0_d aplica esse mesmo ID quando eu faço o export de outro SVG, isso pode dar conflito"
