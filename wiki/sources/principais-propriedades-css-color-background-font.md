---
type: source
title: "Principais propriedades CSS: color, background (img x background-image, cover x contain) e font"
aliases: ["aula principais propriedades CSS", "básico CSS aula 04", "FrontPUSH básico CSS propriedades", "background-size cover contain aula"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [frontend, css, basico-css, color, background, background-image, background-size, background-repeat, background-position, display, box-model, margin, caminho-relativo, font, font-family, font-weight, font-variant, google-fonts, line-height, letter-spacing, text-align, text-shadow, box-shadow, text-decoration, design-responsivo]
skill: tech-mentor-frontend
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/principais-propriedades-css-color-background-font.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-16
---

# Principais propriedades CSS: color, background (img x background-image, cover x contain) e font

## TL;DR

Aula 04 do módulo "Básico CSS" do [[wiki/entities/frontpush|FrontPUSH]] (autoria de [[wiki/entities/nasser|Násser]] inferida). É a primeira aula de código do curso na wiki: as anteriores são de UI no Figma. Tour pelas propriedades do slide, gravado enquanto o autor monta a aula ("estou montando as aulas enquanto eu gravo"). A tese: não decorar tudo antes de começar, aprender as principais e descobrir o resto fuçando no [[wiki/entities/w3schools|W3Schools]].

- **color** muda a cor do texto; **background-color**, a do fundo.
- **Imagem de duas formas.** Com `<img src>` (caminho a partir do `index.html`), `width: 100%` relativo ao pai e `margin: 0 auto` para centralizar a section ([[wiki/concepts/design-responsivo|responsivo]] por porcentagem). Ou com **[[wiki/concepts/background-css|background-image]]**, com caminho a partir do `style.css` (sobe uma pasta: [[wiki/concepts/caminho-relativo]]), altura fixa, `background-size` cover x contain, `background-repeat` e `background-position`.
- **[[wiki/concepts/display-css|display]]:** quase tudo é bloco, exceto span e link, que são inline. O autor força `display: block` no link-botão para aplicar o [[wiki/concepts/box-model]].
- **Depuração:** `border: 1px solid red` é "como se fosse um printf" do layout.
- **Fontes:** [[wiki/entities/google-fonts]] por `<link>`, `font-family` só no H1, `font-size`, `font-weight` (500 não muda, 700 fica negrito) e `font-variant: small-caps`.
- **Texto:** `line-height`, `text-align`, `vertical-align`, `text-shadow` / `box-shadow`, `letter-spacing` (5 px), `text-decoration` e text-transform.

## Key Claims

### Abertura

- **Não queira saber todas antes de começar.** "Comece mesmo sabendo poucas"; de tanto trabalhar, "você vai decorar as propriedades". O autor promete explicar passo a passo nas partes de flexbox e grid.
- **color = texto, background-color = fundo**, "geralmente em textos você vai modificar com o color".

### Imagem com `<img>`

- **Caminho relativo ao HTML.** O `index.html` está na pasta "CSS Basics", a mesma da pasta de imagens: basta entrar nela. Se o HTML estivesse em outra pasta, "eu tenho que voltar um diretório". Ver [[wiki/concepts/caminho-relativo]].
- **Imagem em alta resolução estoura a tela:** `width: 100%` a deixa "100% em relação ao elemento pai", a section.
- **`margin: 0 auto`** = 0 em cima e embaixo, automático à esquerda e à direita: a section de 80% fica centralizada "e meio que já se torna responsiva". "Porcentagem é muito importante para [...] elementos responsivos" ([[wiki/concepts/design-responsivo]]).
- **Uma imagem sobre a outra** porque "ela é em display block", o padrão do CSS; "exceto a span e o de link", que vêm inline. Ver [[wiki/concepts/display-css]] e a tensão abaixo.
- **Link vira bloco no botão:** "o link [...] é inline e eu quero aplicar sempre as propriedades de [[wiki/concepts/box-model|box-model]]".
- **Espaço entre imagens:** margem de 5 px em cima e embaixo, 0 nos lados.

### Imagem como background

- **`background-image: url(...)` com caminho a partir do CSS.** "Eu estou em style.css", então é preciso voltar para a pasta principal antes de entrar na de imagens ("ponto, ponto", isto é, `../`).
- **Sem conteúdo não há altura.** `height: auto` não mostra nada porque "não tem nada de conteúdo aqui dentro"; o autor fixa 500 px (depois 800).
- **`background-size`:** `cover` "literalmente se ajusta com o tamanho da nossa div" e corta parte do passarinho, porque a section (80% × 500) não é quadrada e a imagem é. `contain` deixa a imagem inteira na menor dimensão e repete para completar. Ver [[wiki/concepts/background-css]] e [[wiki/concepts/aspect-ratio]].
- **`background-repeat`:** `no-repeat` impede a repetição, que pode ser só no eixo X ou só no Y.
- **`background-position`:** porcentagem, pixels ou palavras-chave (center, top, bottom, left). Com a imagem a 20% do tamanho, center, bottom e left a movem; `100px 50px` dá distâncias fixas.
- **Border como printf:** "você dá um border de um px solid red para você enxergar a caixinha", em "todo e qualquer layout".
- **Estude por conta própria:** "vem aqui no W3Schools e pesquisa background-size" ([[wiki/entities/w3schools]]).

### Fontes e texto

- **[[wiki/entities/google-fonts]]:** "download family" baixa o zip para instalar; para o site, "select style", escolher regular e bold (o [[wiki/concepts/peso-tipografico]]) e colar o `<link>` no index, "como se fosse um CSS". Ver [[wiki/concepts/webfonts]].
- **`font-family` só no H1:** só o título muda.
- **`font-weight`:** 100 fica "mais fininho", 500 "não mudou ainda", 700 fica negrito.
- **`font-variant: small-caps`** deixaria tudo "em modo de caixa alta" (ver tensão abaixo); `font-style` também é citado.
- **`line-height`** é "aquela propriedade que a gente vê em UI", para "melhorar a leitura, a legibilidade" ([[wiki/concepts/altura-de-linha]]).
- **`text-align`** para ajuste horizontal, `vertical-align` para vertical ([[wiki/concepts/alinhamento-de-texto]]).
- **`text-shadow`** no texto, **`box-shadow`** na caixa ([[wiki/concepts/sombra-em-interfaces]]).
- **`letter-spacing: 5px`** afasta as letras, "eu sempre costumo estar aplicando" ([[wiki/concepts/tracking]]).
- **`text-decoration`** sublinha ou tacha; a transcrição fecha com "o texto se transforma", provavelmente `text-transform`.

## Entities

- [[wiki/entities/nasser]]: autor inferido. Pasta "FrontPush" da transcrição, logo do curso no slide; o nome não é dito.
- [[wiki/entities/frontpush]]: curso de origem; módulo "Básico CSS".
- [[wiki/entities/google-fonts]]: fonte da família aplicada ao H1.
- [[wiki/entities/w3schools]]: referência recomendada para descobrir valores de propriedades.

## Concepts

- [[wiki/concepts/css]]
- [[wiki/concepts/background-css]]
- [[wiki/concepts/display-css]]
- [[wiki/concepts/caminho-relativo]]
- [[wiki/concepts/box-model]]
- [[wiki/concepts/design-responsivo]]
- [[wiki/concepts/aspect-ratio]]
- [[wiki/concepts/webfonts]]
- [[wiki/concepts/peso-tipografico]]
- [[wiki/concepts/altura-de-linha]]
- [[wiki/concepts/tracking]]
- [[wiki/concepts/alinhamento-de-texto]]
- [[wiki/concepts/sombra-em-interfaces]]

## Tensões com a wiki e com a documentação

- **`<img>` não é bloco.** `[external]` `<img>` é um elemento inline substituído (https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img). As imagens da aula ficam empilhadas porque cada uma tem `width: 100%` e não cabe outra na linha, não por serem bloco. Por serem inline, ficam com um vão embaixo (alinhamento à linha de base); `display: block` resolve. A lista "exceto span e link" também é curta: `strong`, `em`, `code`, `label`, `img`, `input` etc. são inline (https://developer.mozilla.org/en-US/docs/Glossary/Inline-level_content).
- **line-height ≠ espaço entre letras.** A aula diz "espaçamento de uma letra da outra, que é a altura da linha"; a segunda metade está certa. Entre letras é `letter-spacing` ([[wiki/concepts/tracking]]); line-height é a altura da linha ([[wiki/concepts/altura-de-linha]]).
- **small-caps ≠ caixa alta.** `[external]` `font-variant: small-caps` desenha as minúsculas como versaletes (maiúsculas pequenas) e mantém as maiúsculas maiores; tudo em maiúsculas é `text-transform: uppercase` (https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant-caps).
- **`vertical-align` não centraliza bloco.** `[external]` Só vale para elementos inline, inline-block e células de tabela (https://developer.mozilla.org/en-US/docs/Web/CSS/vertical-align). Para centralizar um bloco na vertical se usa flexbox ou grid, que o autor promete para depois.
- **Center "sem efeito" com contain.** O autor explica que contain "já está preenchendo". `[external]` Com `contain` a imagem preenche só uma dimensão, e `background-position` ainda a move no eixo livre (https://developer.mozilla.org/en-US/docs/Web/CSS/background-position). Numa section larga com imagem quadrada, center deveria centralizar na horizontal. Hipótese do agente: o `no-repeat` e o valor foram aplicados em ordem ou seletor diferente; o vídeo não está disponível para conferir.
- **Ordem dos valores de position.** `[external]` Em `background-position: 100px 50px`, o primeiro é horizontal (x) e o segundo vertical (y). O autor mexe no valor e conclui "é na parte de cima, não é essa" por tentativa.
- **Peso 500 "não mudou".** Coerente com o [[wiki/concepts/peso-tipografico|estilo falso]]: só regular e bold foram carregados. `[external]` Pela regra de fallback, 500 cai em 400 quando não há 500 (https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight#fallback_weights). O 100 "mais fininho" pede um peso 100 carregado, ou é ilusão: não dá para conferir.
- **Border altera o tamanho da caixa.** `[skill: tech-mentor-frontend]` / `[external]` A dica do printf é boa, mas `border` soma ao [[wiki/concepts/box-model]] e pode mudar o layout que se quer depurar; `outline` não ocupa espaço (https://developer.mozilla.org/en-US/docs/Web/CSS/outline). O DevTools mostra a caixa sem mexer no CSS.
- **Slide com erros de cópia.** A descrição "Para criar uma tag ID no CSS basta colocar uma hashtag: #", repetida em color, background e font, é sobra de outro slide; o autor diz que esqueceu de tirar. O slide lista "underline" como valor de `font-style` (é de `text-decoration`) e só unidades para `background-size`, sem os `cover` e `contain` usados na aula. `font-variant` aparece fora da coluna.
- **Interface do Google Fonts.** "Select style" e "download family" são da interface antiga. `[external]` O site atual usa "Get font" e "Get embed code" (https://fonts.google.com). O fluxo é o mesmo: escolher pesos e colar o `<link>`.

## Open Questions

- "exceto a span e o de link": provavelmente "a [tag] `a`, de link"; mantido literal no raw.
- "meu index, follow aqui": ASR ambíguo, provavelmente "colo aqui" (colar o `<link>`); mantido literal.
- "aplicar center e aquilo é top, bottom": "stop" corrigido para top; "aquilo é" mantido.
- Aulas 01 a 03 do módulo "Básico CSS" (seletores, id com #, display) não estão na wiki; o slide sobrou de uma delas.
- `date_published` vazio.

## Raw Quotes

> "Não queira saber de todas antes para poder começar, comece mesmo sabendo poucas."

> "Você dá sempre um border [...] é como se fosse um printf lá na nossa programação."

> "Porque está como background, não tem nada de conteúdo aqui dentro, entende?"
