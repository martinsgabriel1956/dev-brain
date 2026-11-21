---
type: source
title: "Introdução às propriedades SVG: o que é o SVG e por que usar (FrontPUSH)"
aliases: ["FrontPUSH motion, propriedades SVG aula 01", "Intro Propriedades SVG", "CSS Animations, propriedades SVG, aula 01", "SVG espelho do Figma"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 0
tags: [svg, xml, vetorial, densidade-de-pixels, figma, export, stroke, stroke-dasharray, filtros-svg, dom, svg-inline, motion-design, curso, frontend]
skill: tech-mentor-frontend
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-propriedades-svg-introducao-o-que-e-por-que-usar.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-21
---

# Introdução às propriedades SVG: o que é o SVG e por que usar (FrontPUSH)

## TL;DR

Primeira aula do módulo "Propriedades SVG's" do mini curso de CSS Animations do [[wiki/entities/frontpush|FrontPUSH]], cerca de 11,5 minutos, conceitual, com slide, [[wiki/entities/figma|Figma]] e zoom no próprio site. [[wiki/entities/nasser|Násser]] não diz o nome; autoria pela sequência e pelo "meu site [...] feito com SVGs". Promete que o SVG "vai completar esse combo" com o módulo de CSS "para poder a gente começar literalmente a animar" ([[wiki/concepts/formato-svg]], [[wiki/concepts/motion-design]]).

- **O que é:** "Scalable Vector Graphics", "vetorial no formato XML que suporta animações", "literalmente código", "formado por coordenadas" e "adimensional": "a dimensão é simplesmente a que eu dou para ele" ([[wiki/concepts/xml-extensible-markup-language]]).
- **"Pense como um espelho do Figma"** (texto do slide): o export em SVG "não muda em nada"; layer blur, background blur, inner shadow, "todas as propriedades e efeitos [...] a gente também consegue fazer no SVG" ([[wiki/entities/figma]]).
- **Responsivo:** o SVG exportado "não está responsivo", mas dá para deixá-lo "fluido para poder pegar o tamanho de um div pai" ([[wiki/concepts/design-responsivo]]).
- **Densidade de pixels:** zoom na única imagem do site pixela; no SVG, "não interessa o zoom". Sem exportar 1x, 1,5x, 2x para mobile, tablet e desktop ([[wiki/concepts/densidade-de-pixels]], [[wiki/concepts/formato-png]], [[wiki/concepts/formato-jpeg]]).
- **Elementos separados:** com Ctrl-Shift-G no ícone, cada vetor é um elemento; no export "vão de maneira separada para o código", e o CSS manipula cada um.
- **Efeitos, filtros e DOM:** "aquele efeito de Liquid Motion" vem de efeitos do SVG; "possui árvore no DOM", logo JavaScript também manipula ([[wiki/concepts/dom]], [[wiki/entities/javascript]]).
- **Propriedades específicas:** demo de `stroke` com pontas redondas e "dash array" (5 10, 20 10, 40 70); dá "mais liberdade que as próprias propriedades do CSS"; "o Photoshop da web" ([[wiki/concepts/stroke-svg]]).
- **Desvantagem:** "ele precisa estar no estilo inline para poder ter todas essas vantagens"; como inserir o SVG no HTML fica para a próxima aula.

## Key Claims

### Abertura

- "Vamos iniciar o módulo de propriedades dos SVGs." Muitas "das minhas criações são com base em SVGs"; o módulo anterior "discorreu sobre as principais propriedades do CSS" e "os SVGs vão completar esse combo".
- Aula "introdutória [...] de uma forma um pouco mais conceitual", também "para você também conscientizar outras pessoas para poder utilizar esse queridinho", que dá desempenho por "ser mais leve" e é manipulável com "as propriedades de animação do CSS".

### O que é o SVG

- "Ele significa Scalable Vector Graphics [...] uma imagem vetorial, então são ilustrações, só que tem esse porém aqui, ele é vetorial no formato XML que suporta animações." Mesmo texto do slide.
- "Acredite em mim que ele é literalmente código, é um documento XML." XML é "uma linguagem de marcação, assim como o PHP" (ver Precisões). "Composto por tags [...] basicamente é só código, por isso que torna ele tão vantajoso, porque ele é mais leve que uma imagem normal, ele não é um PNG, um JPG."
- "Qualidade muito superior justamente por ser vetor, porque ele é formado por coordenadas." "Pelo fato dele ser adimensional, a dimensão é simplesmente a que eu dou para ele", então serve a "telas maiores ou em telas menores".

### Espelho do Figma

- Slide: "O que dá pra fazer com SVG? Pense como um espelho do Figma." "Por isso que o Motion e o UI Design se encaixam tão bem."
- No painel de export do Figma: "o PNG, o JPG, o SVG e o PDF, são as quatro principais formas", "principalmente PNG, JPG e SVG" na web. Exportado para a área de trabalho, "é o mesmo elemento, ele não muda em nada, é um espelho de fato".
- Há "propriedades que tem no Figma e não necessariamente tem no CSS": "manipulação melhor de bordas", "elementos em perspectiva feita de forma mais fácil", efeitos. "Layer blur, background blur, inner shadow, todas as propriedades e efeitos [...] a gente também consegue fazer no SVG", "por isso que você saber o Figma e fazer o estudo do SVG é um encaixe tão perfeito".

### Responsivo e o site do autor

- "Ele não está responsivo porque ele exporta com algumas características que vocês vão ver, mas tem como deixar ele responsivo também, ou seja, fluido para poder pegar o tamanho de um div pai."
- "Todo o meu site é feito com SVGs"; até "uns dois anos ou até um ano" atrás usava imagens, mas "só tem vantagens para poder até deixar o meu site mais performático".

### Por que usar: densidade de pixels

- Na "única parte que tem imagem" do site, o zoom pixela, "vai começar a perder qualidade"; no SVG, "não interessa o zoom que eu der, ele vai continuar em uma definição perfeita".
- "Olha só como o uso do SVG melhora a performance do browser" e evita "ficar exportando vários tamanhos de imagens para poder ajustar um ao mobile, o outro ao desktop e o outro ao tablet". O export de PNG no Figma tem "essa variação aqui de um X", "duas vezes o tamanho original, um e meio vezes".
- JPG e PNG "não vão desaparecer"; para eles, "imagens menores em mobile e imagens maiores em desktop", "uma preocupação que eu não preciso ter quando eu trabalho com SVGs".

### Integração com a prototipagem e elementos separados

- "Integração total com a ferramenta de prototipagem." "A gente vai conseguir manipular com tudo que foi feito lá de CSS [...] com cada elemento específico."
- "Se eu der um Ctrl-Shift-G aqui nesse ícone": o balãozinho é um vetor, o background outro, "esse cara aqui atrás é a união de vários outros elementos". No export, "eles vão de maneira separada para o código e [...] eu consigo manipular eles de forma individual com o CSS".

### Efeitos, filtros, DOM

- "Dá para aplicar efeitos e filtros, aquele efeito de Liquid Motion, a gente se dá aplicando alguns efeitos do SVG." "Ele é performático e possui árvore no DOM, o que é isso? Eu posso manipular ele com JavaScript também."

### Propriedades específicas

- "A propriedade de stroke [...] tem muitas propriedades aqui para poder ele deixar redondinho nas pontas." Numa reta no Figma: "está vendo que ele é quadradinho", e há como deixar "redondo nas pontas".
- "Dash array, que é colocar, por exemplo, 5 e 10 [...] 20 e 10 [...] porque como ele está round, você não enxerga direito, mas 40, 70." Ver [[wiki/concepts/stroke-svg]].
- "Tem propriedades do CSS que eles compartilham, tem propriedades que são só do SVG." "O SVG também é chamado meio que o Photoshop da web."

### Desvantagem

- "O SVG tem algumas poucas, mas existem também, porque ele precisa estar no estilo inline para poder ter todas essas vantagens." Como inserir no HTML "é coisa da próxima aula".

## Slide

"Propriedades SVG's", com o logo triangular do mini curso. "O que é SVG?": "Scalable Vector Graphics (SVG)"; "É uma imagem vetorial no formato XML que suporta animações"; "Formada por coordenadas, por vetores, ou seja, é adimensional". "Por que usar?": densidade de pixels; interativo com CSS; integração com ferramentas de prototipagem; animações avançadas; efeitos e filtros (Photoshop da web); performático; possui árvore no DOM. Destaques: "O que dá pra fazer com SVG? Pense como um espelho do Figma"; "SVG = 'Photoshop da web'"; "Propriedades específicas". "Animações avançadas" e "Interativo com CSS" não ganham trecho próprio na fala.

## Entities

- [[wiki/entities/nasser]]: instrutor (inferido).
- [[wiki/entities/frontpush]]: curso.
- [[wiki/entities/figma]]: o "espelho"; export, efeitos e Ctrl-Shift-G.
- [[wiki/entities/javascript]]: manipula o SVG pela árvore do DOM.
- [[wiki/entities/w3c]]: mantém a especificação SVG (não citado na fala).

## Concepts

- [[wiki/concepts/formato-svg]]: definição, vantagens, desvantagem do inline.
- [[wiki/concepts/stroke-svg]]: `stroke-linecap` e `stroke-dasharray` (novo).
- [[wiki/concepts/xml-extensible-markup-language]]: "documento XML".
- [[wiki/concepts/densidade-de-pixels]]: zoom e export 1x/1,5x/2x.
- [[wiki/concepts/formato-png]], [[wiki/concepts/formato-jpeg]]: "não vão desaparecer".
- [[wiki/concepts/design-responsivo]]: SVG fluido no "div pai".
- [[wiki/concepts/dom]]: "possui árvore no DOM".
- [[wiki/concepts/motion-design]]: SVG completa o "combo".
- [[wiki/concepts/vetorizacao-com-pen-tool]]: a reta e os vetores do ícone vêm do Figma.

## Precisões e tensões com a wiki

`[skill: tech-mentor-frontend]` (`references/frontend-animations.md`, `references/frontend-performance-deep.md` para `srcset`) ou `[external]` sem fetch, por conhecimento prévio das especificações SVG 1.1/SVG 2 do [[wiki/entities/w3c|W3C]], do MDN e da documentação do Figma.

- **XML não é "assim como o PHP".** PHP é linguagem de programação do lado do servidor, não de marcação. O par natural é o HTML (provável lapso ou erro de ASR). Mesmo padrão do lapso "CSS é linguagem de marcação" da aula 01 do mini curso ([[wiki/sources/frontpush-introducao-motion-design-css-animations-grade-do-curso]]). Confiança alta.
- **"Mais leve que uma imagem normal" depende.** Ícones, logos e ilustrações planas ficam menores em SVG; ilustração com milhares de pontos, gradientes ou imagens embutidas em base64 pode ficar maior que um WebP. O custo também muda de lugar: o SVG é desenhado pelo navegador a cada pintura, e filtros custam CPU/GPU. A wiki já registra a ressalva do Image Tracer e do DOM grande ([[wiki/concepts/formato-svg]]). Confiança alta.
- **"Melhora a performance do browser" mistura nitidez com desempenho.** O zoom sem perda prova independência de resolução, não velocidade. Confiança alta.
- **"Não responsivo" no export do Figma = `width`/`height` fixos.** O Figma escreve `width` e `height` em px junto do `viewBox`. Para ficar fluido, mantém-se o `viewBox` e usa-se `width: 100%; height: auto` (ou remove-se os atributos). Sem `viewBox`, não escala. Confiança alta.
- **Nem todo efeito do Figma vira SVG.** Drop shadow, inner shadow e layer blur saem como `<filter>` (`feGaussianBlur`, `feOffset`, `feColorMatrix`, `feBlend`). Background blur não tem equivalente em filtro SVG, que não enxerga o que está atrás; o análogo é `backdrop-filter` do CSS. Confiança média: o comportamento exato do export varia por versão do Figma.
- **"Liquid Motion" é o efeito *gooey*.** `feGaussianBlur` borra as formas e `feColorMatrix` corta o alfa, e as bolhas parecem se fundir. Confiança alta.
- **`stroke-linecap`:** `butt` (padrão, o "quadradinho"), `round`, `square`. Com `round`, cada traço ganha meia espessura em cada ponta e invade o intervalo do `stroke-dasharray`: com traço grosso, "5 10" vira bolinhas e os vãos somem; daí "você não enxerga direito" e ele aumenta os valores. Ver [[wiki/concepts/stroke-svg]]. Confiança alta.
- **"Precisa estar inline" vale para o CSS e o JS da página.** Via `<img>` ou `background-image`, o SVG não entra no DOM da página: sem seletores externos, sem JS. Mas um `<style>` com `@keyframes` dentro do próprio arquivo roda até via `<img>`. O preço do inline já está na wiki: markup no HTML, sem cache separado, DOM maior ([[wiki/concepts/formato-svg]], [[wiki/sources/frontpush-relatorio-pagespeed-imagens-render-blocking-dom-regra-80-20]]). Confiança alta.
- **Densidade de pixels × tamanho de tela.** O 1x/1,5x/2x do Figma serve a densidade (DPR), não mobile × desktop; para tamanho de tela, `srcset` com descritores `w` + `sizes` ou `<picture>` com `media`. A fala junta os dois. Confiança alta.
- **"Adimensional", mas não infinito.** O SVG é rasterizado na tela; traços finos em tamanho pequeno ficam borrados entre pixels, e `stroke-width` escala junto, salvo `vector-effect: non-scaling-stroke`. Ecoa o aviso dos tamanhos ópticos do Material 3 em [[wiki/concepts/formato-svg]]. Confiança alta.
- **Ctrl-Shift-G no Figma é desagrupar** (Ctrl-G agrupa). Confiança alta.
- **Acessibilidade de SVG inline segue ausente.** Decorativo pede `aria-hidden="true"`; informativo, `role="img"` + `<title>` ou `aria-label`. Animações de SVG também entram no `prefers-reduced-motion`. Confiança alta.

## Open Questions

- "Então o cabo aqui que eu vou mostrar na prática": provável "então, acabou aqui"/"vou mostrar"; deixado literal.
- "Basta vir aqui do Google Doc XML": busca no Google por "XML"; "Doc" sem sentido claro; deixado literal.
- "Sempre pense da pessoal como um espelho do Figma": o slide diz "Pense como um espelho do Figma"; provável "pensem, pessoal"; deixado literal.
- "Ele é dimensional" na seção de densidade contradiz o "adimensional" de antes: lapso ou "a" engolido pela legenda; deixado literal.
- "Nessas aulas bônus": a grade da aula 01 tem bônus; aqui sugere aulas de Figma para sombras e ícones.
- "Animações avançadas" e "Interativo com CSS" (slide) ficam para as próximas aulas.

## Continuação

Abre o módulo de SVG previsto na grade da aula 01 ([[wiki/sources/frontpush-introducao-motion-design-css-animations-grade-do-curso]]), depois do básico CSS que terminou em [[wiki/sources/frontpush-propriedade-animation-pratica-keyframes-parent-box-varias-animacoes]]. A próxima aula promete as formas de inserir o SVG no HTML e as desvantagens do inline.

Cumprido em [[wiki/sources/frontpush-como-usar-svg-img-background-object-inline]]: `<img>`, `background-image`, `iframe`/`object`/`embed` e inline, com o "volume de código" como preço do inline.

## Raw quotes

- "ele é vetorial no formato XML que suporta animações"
- "a dimensão é simplesmente a que eu dou para ele"
- "é o mesmo elemento, ele não muda em nada, é um espelho de fato"
- "não interessa o zoom que eu der, ele vai continuar em uma definição perfeita"
- "o SVG também é chamado meio que o Photoshop da web"
- "ele precisa estar no estilo inline para poder ter todas essas vantagens"
