---
type: source
title: "Propriedade transform, parte 1: translate, scale, rotate, skew, matrix e perspectiva (FrontPUSH)"
aliases: ["FrontPUSH motion, básico CSS aula 01", "Propriedade transform pt.1", "transform parte 1", "CSS Animations, básico CSS, aula 01"]
date_created: 2026-11-20
date_updated: 2026-11-20
source_count: 0
tags: [css, transform, translate, scale, rotate, skew, matrix, perspective, 3d, box-sizing, motion-design, animacao, curso, frontend]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-20
---

# Propriedade transform, parte 1: translate, scale, rotate, skew, matrix e perspectiva (FrontPUSH)

## TL;DR

Primeira aula do módulo "Básico CSS" do mini curso de CSS Animations do [[wiki/entities/frontpush|FrontPUSH]], cerca de 21 minutos, com um slide e código ao vivo. É o tópico "propriedades de CSS voltadas ao motion" da grade da aula 01 e o "próximo módulo de básico CSS" prometido na aula 04. [[wiki/entities/nasser|Násser]] não diz o nome; autoria pela sequência e pelo estilo. O módulo cobrirá `transform`, `transition`, `opacity`, `position` e `animation`; esta aula fica com as funções de `transform` ([[wiki/concepts/transition-e-transform-css]]).

- **rotate** em `deg`, em torno do centro (o "ponto de ancoragem", tema da próxima aula). Gradiente no fundo para ver o giro; negativo gira ao contrário.
- **translate** em px, relativo à posição inicial; serve até de "hack" de layout no flexbox. **Eixo Y invertido**: positivo desce. Z sozinho não aparece sem perspectiva.
- **scale** como juros: 1,2 = +20%, 2 = +100%, 0,7 = −30%; `scaleX`/`scaleY` separam os eixos.
- **skew** entorta em X, em Y ou nos dois. Várias funções juntas, separadas por espaço.
- **matrix** resume tudo em seis números (scaleX, skewY, skewX, scaleY, translateX, translateY); "não é muito intuitivo", aparece em SVG e ferramentas ([[wiki/concepts/transform-matrix-css]]).
- **Perspectiva** no elemento pai (`perspective: 400px` no body) faz o `rotateX` parecer um flip 3D; sem ela, `rotateX(50deg)` parece `scaleY(0,7)` ([[wiki/concepts/perspective-css]]).
- Antes do transform: reset com `*` (margin, padding, `box-sizing: border-box`) e body em flex centralizado ([[wiki/concepts/box-model]], [[wiki/concepts/estilos-padrao-do-navegador-e-reset]], [[wiki/concepts/flexbox]]).

## Key Claims

### O módulo e o material de apoio

- "É um básico diferente daquele que a gente viu na codificação front-end", que é "pré-requisito": aqui o foco são as propriedades "mais voltadas para motion, então é transform, transition, opacity, position, animation". Ver [[wiki/concepts/motion-design]] e [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]].
- "O nosso material de apoio é o W3C [...] um órgão que regulamenta", com "mais exemplos e [...] maiores explicações". Ver [[wiki/entities/w3c]] e Precisões.

### O slide

"Básico CSS" → "Transform": `matrix(n,n,n,n,n,n)` e `matrix3d(n × 16)` ("Resumo das propriedades"); `translate(x,y)`, `translate3d(x,y,z)` → `translateX/Y/Z`; `scale(x,y)`, `scale3d(x,y,z)` → `scaleX/Y/Z`; `rotate(angle)`, `rotate3d(x,y,z,angle)` → `rotateX/Y/Z(angle)`; `skew(x-angle,y-angle)` → `skewX/skewY(angle)`; `perspective(n)`. "Esse matrix e esse matrix 3D [...] trata-se de um resumo das propriedades aqui de baixo."

### Teoria rápida

- translate: "literalmente mover o objeto para o lado ou para o outro, para cima ou para baixo", "nos três eixos, inclusive no eixo Z".
- scale: "tratar do tamanho do objeto", aumentar ou diminuir "nas três coordenadas".
- "O scale é quando eu quero deitar o objeto, esticar o objeto. Então eu deixo, por exemplo, a base fixa e a parte de cima eu translado." Pela ordem do slide é o **skew**; lapso ou ASR, deixado literal (o mesmo "scale" no lugar de skew apareceu na aula 04).
- Perspectiva: "nós temos aqui um ambiente 2D [...] Quando a gente quer simular algum elemento 3D, a gente tem que colocar a perspectiva, tem que colocar uma distância do eixo Z".

### Preparação: Sass, reset e flex

- Página `index.html` com `<link>` para o CSS. Usa um arquivo [[wiki/concepts/pre-processador-css|Sass]] "porque ele adiciona o WebKit nos meus comandos de forma automática", por um plugin do [[wiki/entities/vs-code]] ([[wiki/entities/live-sass-compiler]], [[wiki/concepts/prefixo-de-fornecedor]]).
- "Sempre aplique esse hack aqui": `*` em "todas as tags HTML", zera padding e margin "porque [...] algumas tags do HTML [...] por padrão vem com o margin e com o padding", e `box-sizing: border-box` "para poder ele ter como referência a borda e não o conteúdo" ([[wiki/concepts/seletores-css]], [[wiki/concepts/estilos-padrao-do-navegador-e-reset]]).
- Demonstração com `.box` de 100 px: com `border-box` o texto grande "passa da minha caixa"; com `content-box` e `padding: 0 20px`, "ele vai permitir que o conteúdo se adeque". "Eu sempre deixo como border-box." Ver [[wiki/concepts/box-model]] e Precisões.
- `display: flex` no body centraliza o filho direto `.box` na horizontal e na vertical ([[wiki/concepts/flexbox]]).

### rotate

- "Um valor em graus [...] em inglês a gente escreve degrees [...] a gente coloca como deg." `rotate(50deg)` gira "com relação ao seu eixo principal"; "o seu ponto de ancoragem está no centro", e "na próxima aula [...] a gente vai ver como é que a gente muda esse ponto de ancoragem" (`transform-origin`).
- "Ele vai até 360"; a 270 "como está certinho no eixo, você não vai perceber". Com cor sólida "você não sabe se ele girou", então põe "um gradiente bem feio, o clássico blue-red", copiado do [[wiki/entities/figma]] ([[wiki/concepts/background-css]]). "Pode colocar número negativo também": −30deg "vai inverter".

### translate

- `translate(200px, 100px)`, depois 50 e 100: "transladou primeiro 50 para cá e depois 100 para baixo". `translate3d(50px, 0, 0)`; "ele sempre vai ter como referência a posição inicial dele".
- Uso em layout: "um deslocamento bem pequenininho [...] como se fosse um hack, quando [...] ela foge demais no flexbox, tem como eu forçar ele voltar para o lugar utilizando o translate".
- "Para a direita o eixo x é positivo [...] só que aqui o eixo y é invertido, não é como a gente vê lá na escola": 50 px "vai descer ao invés de subir". "Tudo na física depende do referencial."
- `translateZ(50px)`: "você não vai descobrir nada [...] porque é o eixo que está saindo da tela, então ele meio que se aproximou de você", e "a gente precisa utilizar a propriedade de perspectiva".
- Exemplos dos sites dele: uma seta que transita entre pontos de translate "com a velocidade diferente" ([[wiki/concepts/easing]]) e bolinhas e links que sobem no hover: "simplesmente um translate no eixo y" ([[wiki/concepts/microinteracao]]).

### scale

- "Se eu colocar 1,2, ele vai dar 20% de aumento [...] se eu colocar 2, ele vai dar 100% de aumento." "É como se fosse aplicar desconto [...] 1 menos a taxa [...] 1 mais a taxa": +50% é 1,5; −30% é 0,7.
- Vale para x, y e z; só no x "ele meio que vai ficar achatadinho". "Tudo que é remetido ao 3D [...] é quando a gente aplica perspectiva."

### skew e funções combinadas

- `skewX(20deg)` "vai entortar só no eixo x"; −20deg entorta para o outro lado; `skewY` entorta em y; com 50deg nos dois "ele vai esticar mais ainda". "Se eu colocar apenas skew, vamos ver o que acontece": a legenda não diz o resultado. "Não deixem de treinar."
- "Tem como aplicar muitas propriedades ao mesmo tempo, é só você dar um espaço": `rotate(45deg)` com `scale(1.5)`.

### matrix

- "Quase você não vai aplicar, porque não é muito intuitivo, são mais ferramentas que utilizam o matrix." Ordem: "o scale no x, a segunda [...] é o skew y, a terceira [...] é o skew x, a quarta [...] é o scale y [...] aqui translate x e aqui translate y". Ver [[wiki/concepts/transform-matrix-css]].
- Serve para reconhecer: "quando você bater o olho nessa propriedade matrix, em algum objeto SVG, você já fala, ele está aplicando a propriedade transform" ([[wiki/concepts/formato-svg]]). "É só uma fórmula de resumir essas propriedades."

### Perspectiva e 3D

- `rotateX(30deg)` "não mudou praticamente nada"; 50deg "só diminuiu": "se eu aplicar no y de 0,7, ou aplicar um rotate x de 50deg [...] meio que tem o mesmo efeito". No DevTools, mudando o ângulo pelas setas, "ele está girando, só que pelo fato de não ter perspectiva, você não está entendendo muito bem".
- "A gente nunca aplica na div que a gente está olhando [...] Perspectiva depende de quão longe está um objeto do outro, isso se aplica ao nosso olho": o celular girado perto ou longe. "Eu sempre aplico a perspectiva no elemento pai [...] no caso é o body": `perspective: 400px`. Ver [[wiki/concepts/perspective-css]] e Precisões.
- Com perspectiva, "essa parte que teoricamente está mais longe, ela está menor, então dá a ideia de que ele literalmente está fazendo um flip 3D".
- Exercício: mudar o valor da perspectiva; "a perspectiva menor se adequa ao tamanho do objeto", e com ela menor "a distância de aumento foi aumentar".

## Entities

- [[wiki/entities/nasser]]: instrutor (inferido).
- [[wiki/entities/frontpush]]: curso; módulo "Básico CSS" do mini curso de CSS Animations.
- [[wiki/entities/w3c]]: indicado como material de apoio.
- [[wiki/entities/figma]]: de onde copia o gradiente.
- [[wiki/entities/vs-code]] e [[wiki/entities/live-sass-compiler]]: o "plugin" que compila o Sass e põe os prefixos.

## Concepts

- [[wiki/concepts/transition-e-transform-css]]: as funções de `transform`.
- [[wiki/concepts/perspective-css]]: perspectiva e 3D no CSS (página criada nesta ingestão).
- [[wiki/concepts/transform-matrix-css]]: `matrix()` e `matrix3d()` (página criada nesta ingestão).
- [[wiki/concepts/transform-origin-css]]: o "ponto de ancoragem" prometido.
- [[wiki/concepts/box-model]], [[wiki/concepts/estilos-padrao-do-navegador-e-reset]], [[wiki/concepts/seletores-css]]: o reset com `*`.
- [[wiki/concepts/flexbox]]: centralizar a caixa.
- [[wiki/concepts/prefixo-de-fornecedor]], [[wiki/concepts/pre-processador-css]]: o "WebKit automático".
- [[wiki/concepts/background-css]]: `linear-gradient` para ver o giro.
- [[wiki/concepts/motion-design]], [[wiki/concepts/easing]], [[wiki/concepts/microinteracao]]: os exemplos dos sites dele.
- [[wiki/concepts/css-puro-vs-biblioteca-de-animacao]]: o flip 3D sai em CSS puro.
- [[wiki/concepts/formato-svg]]: onde `matrix` costuma aparecer.

## Precisões e tensões com a wiki

Todas `[skill: tech-mentor-frontend]` ou `[external]` sem fetch, por conhecimento prévio da especificação CSS Transforms (w3.org/TR/css-transforms-1 e css-transforms-2) e do MDN.

- **W3C ou W3Schools.** O W3C publica as especificações; "mais exemplos e maiores explicações" descreve melhor o W3Schools ou o MDN, padrão já anotado em [[wiki/entities/w3c]]. Confiança média.
- **"WebKit automático" hoje é desnecessário para `transform`.** Sem prefixo em todos os navegadores atuais há anos; quem põe os prefixos é o Autoprefixer da extensão, não o Sass ([[wiki/concepts/prefixo-de-fornecedor]]). Confiança alta.
- **A demonstração do box-sizing mistura duas coisas.** `border-box` inclui padding e borda na `width`; `content-box` soma o padding por fora (100 + 40 = 140 px). Texto que "passa da caixa" é transbordo (`overflow`), não efeito do box-sizing. O reset comum é `*, *::before, *::after`, porque `*` não pega pseudo-elementos ([[wiki/concepts/box-model]]). Confiança alta.
- **Centralizar no body pede altura.** `align-items: center` só centraliza na vertical se o body tiver altura (por exemplo `min-height: 100vh`); a aula não mostra. Confiança média (o código não aparece na legenda).
- **rotate:** ângulo positivo gira no sentido horário; negativo, anti-horário (não "inverte"). Não para em 360: `720deg` são duas voltas, o que importa em transições. Também há `turn` e `rad`. O quadrado parece igual a 90, 180 e 270 por simetria, como ele diz. Confiança alta.
- **`transform-origin` padrão** é o centro (`50% 50%`) em elementos HTML, mas `0 0` em elementos SVG, o que pesa quando o curso chegar ao SVG. Confiança alta.
- **`translate(50px, 100px)` não é "primeiro 50, depois 100".** É um deslocamento só, na diagonal. A ordem importa *entre funções*: `rotate(45deg) translateX(100px)` ≠ `translateX(100px) rotate(45deg)`. Porcentagem em `translate` é do próprio elemento, daí o `translate(-50%, -50%)` de centralização. Confiança alta.
- **"O eixo x ou o eixo y é negativo".** Para subir, só o Y é negativo; o X é lapso. O Y para baixo vem da origem no canto superior esquerdo da tela. Confiança alta.
- **translate como "hack" de layout:** `transform` não mexe no fluxo; os vizinhos não se movem e o espaço original fica reservado. Bom para animar, frágil como correção de layout. Confiança alta.
- **scale(2) dobra cada eixo**, logo a área quadruplica. `scaleZ` sozinho não aparece num elemento plano. Escala também o texto e a borda. Confiança alta.
- **skew nos dois eixos com 50deg não "estica mais", espelha.** A matriz de `skew(ax, ay)` tem determinante 1 − tan(ax)·tan(ay); com 50° dá cerca de −0,42, e a caixa vira do avesso (com 45° nos dois, achata numa linha). `skew()` com um valor só equivale a `skewX()`; a especificação o mantém por compatibilidade e recomenda `skewX`/`skewY`. A "base fixa" da teoria só vale com `transform-origin` embaixo; no centro, topo e base andam em sentidos opostos. Confiança alta na matemática, média-alta na nota da especificação.
- **Várias funções num `transform`:** uma segunda declaração `transform` substitui a primeira, não soma (o conflito da aula 03). Existem as propriedades individuais `translate`, `rotate` e `scale`, sem `skew`. Confiança alta.
- **Os números do `matrix` não são as funções.** Em `matrix(a, b, c, d, e, f)`, `b` e `c` são tangentes do skew (não ângulos), a rotação também mora em `a`–`d` (cos, sen) e `e`/`f` são px sem unidade. O lugar mais comum de vê-la é o estilo computado no DevTools, que devolve `matrix()` ([[wiki/concepts/transform-matrix-css]]). Confiança alta.
- **`rotateX(50deg)` sem perspectiva ≈ `scaleY(cos 50°)` = 0,64**, perto dos 0,7 dele; com 30° dá 0,87, por isso "não mudou praticamente nada". É projeção ortográfica. Confiança alta.
- **"Nunca aplica na div que a gente está olhando" vale para a propriedade, não para a função.** `perspective: 400px` vai no pai e dá um ponto de fuga comum aos filhos (`perspective-origin`); a função `perspective()` vai no próprio elemento, no começo do `transform`. Valor menor = câmera mais perto = distorção maior, que é o que o exercício final descreve. Para 3D aninhado: `transform-style: preserve-3d`; para cartas que viram: `backface-visibility` ([[wiki/concepts/perspective-css]]). Confiança alta.
- **Tensão com a aula 04 resolvida em parte.** Lá, com perspectiva e 3D "as bibliotecas JavaScript meio que são imprescindíveis"; aqui o flip 3D sai em CSS puro ([[wiki/concepts/css-puro-vs-biblioteca-de-animacao]]).
- `prefers-reduced-motion` segue ausente; flips 3D e grandes translações são os casos que a preferência mais visa.

## Open Questions

- "Lá no ScriptFA, em codificação": nome de plataforma ou erro de ASR? A "codificação front-end" parece ser o módulo de HTML/CSS do FrontPUSH ([[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]]). Deixado literal.
- "O trade dele é um pouquinho mais complicado": talvez "o tratamento"; deixado literal.
- "Você vai ver que a perspectiva é 1": sentido incerto; deixado literal.
- O resultado de "apenas skew" não aparece na legenda.
- O `matrix3d` foi prometido ("depois a gente dá uma olhadinha") e não veio nesta aula.

## Continuação

A próxima aula promete as "propriedades do transform", começando pelo ponto de ancoragem (`transform-origin`). Veio em [[wiki/sources/frontpush-propriedade-transform-parte-2-transform-origin-transform-style-preserve-3d]]: [[wiki/concepts/transform-origin-css]] e `transform-style: preserve-3d`.

## Raw quotes

- "o nosso material de apoio é o W3C"
- "aqui o eixo y é invertido, não é como a gente vê lá na escola"
- "é como se fosse aplicar desconto"
- "a gente nunca aplica na div que a gente está olhando"
- "dá a ideia de que ele literalmente está fazendo um flip 3D"
