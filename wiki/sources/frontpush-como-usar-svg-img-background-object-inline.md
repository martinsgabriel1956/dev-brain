---
type: source
title: "Como usar o SVG: tag img, background-image, iframe/object/embed e inline (FrontPUSH)"
aliases: ["FrontPUSH motion, propriedades SVG aula 02", "Como usar os SVG's", "Como usar o SVG?", "CSS Animations, propriedades SVG, aula 02"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 0
tags: [svg, svg-inline, img, background-image, object, iframe, embed, data-uri, can-i-use, sass, prefixo-de-fornecedor, requisicao-http, dom, curso, frontend]
skill: tech-mentor-frontend
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-como-usar-svg-img-background-object-inline.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-21
---

# Como usar o SVG: tag img, background-image, iframe/object/embed e inline (FrontPUSH)

## TL;DR

Segunda aula do módulo "Propriedades SVG's" do mini curso de CSS Animations do [[wiki/entities/frontpush|FrontPUSH]], cerca de 13,5 minutos, com slide e código no [[wiki/entities/vs-code|VS Code]]. [[wiki/entities/nasser|Násser]] não diz o nome; autoria pela sequência ("na primeira aula", a "aulinha de sass lá no meu YouTube"). Apresenta "as quatro principais formas" de pôr um SVG na página, "acredito que são as únicas quatro", com quais usa e por quê ([[wiki/concepts/formas-de-inserir-svg]]).

- **Projeto:** SVG exportado do [[wiki/entities/figma|Figma]] com fundo transparente, `index.html`, `style.scss` compilado pelo Sass, que "gera [...] o arquivo CSS um pouco mais otimizado com relação à inserção de WebKit" ([[wiki/concepts/pre-processador-css]], [[wiki/concepts/prefixo-de-fornecedor]]); reset com `border-box` e fundo `#1A1A1A`.
- **[[wiki/entities/can-i-use|Can I Use]]**, "uma coisa que eu esqueci [...] na primeira aula": SVG roda em quase tudo; ficam de fora o Android browser antigo e o Internet Explorer 6 a 8, com 0% e 0,09% de uso.
- **Peso:** o SVG tem 8KB (7,47); o mesmo desenho em PNG, 728KB: "91 vezes mais leve" ([[wiki/concepts/formato-png]]).
- **1. `<img>`:** `src` relativo ao HTML; `width: 100%` deixa fluido. Usa para ícones e imagens que não vai animar. Desvantagem: "não tem edição no DOM, não tem como ter interação com o CSS [...] não é o SVG puro".
- **2. `background-image`:** `url()` relativo ao CSS ("tenho que voltar uma pasta"), `background-size: cover`; precisa de "um height fixo, porque senão ele não vai aparecer" (100vh) ([[wiki/concepts/background-css]], [[wiki/concepts/caminho-relativo]]).
- **3. `iframe`/`object`/`embed`:** "muito ruim", "pode ser interpretado de forma diferente", "lento"; não demonstra e manda pesquisar "data URI", "só vi desvantagem" ([[wiki/concepts/base64-encoding]]).
- **4. Inline:** "o módulo que eu mais utilizo", "literalmente o SVG puro": edição no DOM, CSS em cada parte, animação, e "não precisa fazer request HTTP" ([[wiki/concepts/dom]], [[wiki/concepts/requisicao-http]]). Ctrl A, Ctrl C, Ctrl V no HTML. Desvantagem: "o volume de código", "manchando o seu código"; uma biblioteca JavaScript ou o PHP faz o "include".
- **Foco do curso:** o inline, "porque é a que permite a gente fazer animação e interação"; `<img>` e background nos "outros projetos".

## Key Claims

### Abertura

- "Nós vamos ver as quatro principais formas, acredito que são as únicas quatro [...] mas se houver, por favor me avise para poder atualizar a aula." Vai dizer "quais que eu utilizo, quais que eu não utilizo e qual a vantagem e desvantagem de cada uma".
- "Trabalhar com SVG pode ser um pouquinho mais complicado, no sentido de inserir isso, principalmente quando você tem uma página com muitas ilustrações."

### Preparando o projeto

- Reexporta o SVG "com o fundo transparente"; pasta `SVG` no Visual Studio Code; renomeia "o meu AppMessages" para `app`.
- `index.html` com a estrutura de HTML5, "a aula SVG"; o Google Chrome "lado a lado".
- "Aquele clássico CSS, esse aqui não pode faltar": pasta `CSS`, `style.scss`, "tem a aulinha de sass lá no meu YouTube"; Sass é "um pré-processador só para poder a gente dar um boost no nosso alcance, com relação à compatibilidade dos comandos".
- Reset sem padding e margem, `box-size` em `border-box`, body com `width` 100%, `height` 100 e `background-color` "aquele hashtag 1A1A1A que eu sempre estou utilizando" ([[wiki/concepts/estilos-padrao-do-navegador-e-reset]]).
- O Sass "compila, gera para mim o arquivo CSS um pouco mais otimizado com relação à inserção de WebKit, que traz mais compatibilidade entre os browsers, então ele fica mais performático" ([[wiki/entities/live-sass-compiler]]).

### Compatibilidade

- No Can I Use, o SVG "está compatível com a grande maioria de browsers". "Tem o Android browser, que ele não está sendo suportado, mas ele é muito antigo", e "o Internet Explorer 6 e 8", "0% de total de uso" e "0,09% do uso do Internet Explorer".

### SVG × PNG

- "É assim que é um código SVG"; a estrutura fica para as próximas aulas.
- "Olha só quanto está pesando esse arquivo SVG, 8KB [...] tamanho 7,47, tamanho de disco 8KB." O PNG exportado "do mesmo jeito", transparente, "728KB": "728 e dividido por 8, então 91 vezes mais leve".

### 1. Tag img

- `<img>` com `src` "como eu estou no index.html, eu já entro direto na pasta SVG, app.svg". Para responsivo, `img` com "100% do tamanho do pai", e o pai é o `body`, também 100%.
- "Eu utilizo esse jeito, geralmente quando eu estou utilizando algum tipo de ícone que eu não estou querendo animar ou fazer muitas modificações."
- "A desvantagem dela é que não tem edição no DOM, não tem como ter interação com o CSS, porque está dentro da tag img, não é o SVG puro, por assim dizer."

### 2. background-image

- `div.box` com `background-image: url(...)`; "como a minha array está sendo no CSS, eu tenho que voltar uma pasta". Remete ao "script-fe, onde eu expliquei [...] essas propriedades de background" (provável módulo de CSS do curso; mantido literal).
- `background-size: cover` "para poder ele pegar o tamanho da caixa" e `width: 100%`. "Eu tenho que definir [...] um height fixo, porque senão ele não vai aparecer": 100vh.
- Slide: "Sem edição no DOM", "Não dá pra ter interação com CSS", "Criar classes com background e chamar no HTML".

### 3. iframe, object, embed

- "Eu não vou nem exemplificar [...] porque ele é muito ruim": em `iframe`, `object` ou `embed`, "ele pode ser interpretado de forma diferente, ele é lento, é quando eu gero um código gigantesco para poder traduzir esse SVG".
- "Se vocês tiverem curiosidade, depois vocês pesquisem sobre data URI, essa forma, só que ela é lenta, só vi desvantagem e nem cheguei a considerar."

### 4. Inline

- "O módulo que eu mais utilizo, que é o inline, que é literalmente o SVG puro, onde ele permite a edição no DOM, na árvore de elementos", com CSS "para interagir com cada uma dessas partes", "animação e interação HTML".
- "Não precisa fazer request HTTP, então isso aqui é uma vantagem porque não precisa ficar renderizando a página e pesando mais ainda."
- "Ctrl A, seleciono, Ctrl C e colo direto no meu HTML, Ctrl V." Com 100%, "fica responsivo do mesmo jeito" (trecho de cerca de 11 s sem fala antes disso).
- "A desvantagem [...] é o volume de código": um SVG "com muitas sombras ou então com vários elementos [...] fica bem maior"; "imagina você colocar vários blocos desse no seu código, tipo manchando o seu código", "você precisa de técnicas para poder deixar isso mais organizado".
- "Tem uma biblioteca do JavaScript que faz isso, meio que dá um include [...] se você utiliza PHP também dá para fazer [...] para poder inserir o SVG de forma inline." Promete mostrar.

### Fechamento

- "Nós vamos dar muito enfoque nessa aqui porque é a que permite a gente fazer animação e interação, mas nos outros projetos a gente também vai utilizar essas duas formas aqui" (`<img>` e background). Próxima aula: "a estrutura do SVG".

## Slide

"Como usar o SVG?", com o logo triangular do mini curso. Quatro blocos: "Utilizar como uma imagem: tag <img>" (sem edição no DOM; não dá pra ter interação com CSS); "Utilizar como background-image" (sem edição no DOM; não dá pra ter interação com CSS; criar classes com background e chamar no HTML); "Utilizar como iframe/object/embed" (lento; pode ser interpretado de forma diferente); "Utilizar inline" (permite edição no DOM; animações e interações HTML; não precisa de fazer request HTTP).

## Entities

- [[wiki/entities/nasser]]: instrutor (inferido).
- [[wiki/entities/frontpush]]: curso.
- [[wiki/entities/can-i-use]]: suporte ao SVG.
- [[wiki/entities/live-sass-compiler]]: provável compilador que insere o WebKit.
- [[wiki/entities/vs-code]], [[wiki/entities/figma]]: editor e origem do SVG.

## Concepts

- [[wiki/concepts/formas-de-inserir-svg]]: as quatro formas e os trade-offs (novo).
- [[wiki/concepts/formato-svg]]: peso, suporte, inline.
- [[wiki/concepts/background-css]]: SVG como fundo, altura fixa, `cover`.
- [[wiki/concepts/caminho-relativo]]: `src` parte do HTML, `url()` do CSS.
- [[wiki/concepts/pre-processador-css]], [[wiki/concepts/prefixo-de-fornecedor]]: "inserção de WebKit".
- [[wiki/concepts/formato-png]]: 728KB × 8KB.
- [[wiki/concepts/requisicao-http]], [[wiki/concepts/cache]]: inline economiza a requisição e perde o cache.
- [[wiki/concepts/base64-encoding]]: data URI.
- [[wiki/concepts/dom]]: "edição no DOM".
- [[wiki/concepts/estilos-padrao-do-navegador-e-reset]]: reset de sempre.

## Precisões e tensões com a wiki

`[skill: tech-mentor-frontend]` (`references/frontend-performance-deep.md`: imagens, requisições; `references/frontend-animations.md`) ou `[external]` sem fetch, por conhecimento prévio da especificação SVG, do HTML Living Standard e do MDN.

- **Não são as únicas quatro.** Faltam `<use href="sprite.svg#icone">` (sprite externo com `<symbol>`, cacheável, recolorível por `currentColor` e variáveis CSS), `mask-image`/`mask` com SVG (ícone que herda `background-color`) e a importação em build (SVGR no React, plugins do Vite). Detalhes em [[wiki/concepts/formas-de-inserir-svg]]. Confiança alta.
- **`<img>` não é tão mudo.** O CSS da página não entra, mas um `<style>` com `@keyframes` dentro do arquivo anima mesmo via `<img>`; scripts e recursos externos é que não rodam. E o `<img>` traz `alt`, `loading="lazy"`, `decoding` e cache próprio. Para responsivo, o SVG precisa de `viewBox` ([[wiki/sources/frontpush-propriedades-svg-introducao-o-que-e-por-que-usar]]). Confiança alta.
- **`cover` corta.** `background-size: cover` preenche a caixa e recorta o excesso; para mostrar a ilustração inteira, `contain`. A altura fixa é a mesma regra da aula de background: a caixa vazia não ganha altura pela imagem ([[wiki/concepts/background-css]]). Confiança alta.
- **`object`, `iframe` e data URI são coisas diferentes, e não "lentas" por natureza.** `<object>`/`<iframe>` carregam o SVG como documento separado (uma requisição, cache, scripts internos rodam; o JS da página alcança via `contentDocument` na mesma origem; CSS da página não entra). `<embed>` é legado. Data URI é outra coisa: o SVG escrito dentro do `url()` ou do `src`, sem requisição. Em base64 incha cerca de 33%; codificado como URL (`data:image/svg+xml,%3Csvg...`), é a forma usual de ícones pequenos no CSS. O "código gigantesco" descreve o base64, não o `object`. Confiança alta.
- **"Não precisa fazer request HTTP" tem o outro lado.** O SVG inline vem dentro do HTML: sem requisição extra, mas sem cache separado, repetido em cada página e em cada uso, e aumentando o HTML e o DOM. "Não precisa ficar renderizando a página" não procede: o inline é renderizado junto com o resto. Com HTTP/2 e cache, um arquivo externo reutilizado costuma ganhar ([[wiki/concepts/requisicao-http]], [[wiki/concepts/cache]], [[wiki/sources/frontpush-relatorio-pagespeed-imagens-render-blocking-dom-regra-80-20]]). Confiança alta.
- **IDs duplicados ao colar vários SVGs do Figma.** Gradientes, filtros e máscaras são referenciados por `id` (`url(#paint0_linear...)`). Colados na mesma página, IDs iguais colidem e um SVG pega o gradiente do outro. As versões recentes do Figma acrescentam o ID do nó, o que reduz, mas não elimina, o risco; SVGO com `prefixIds` resolve. Confiança média-alta.
- **O "include" por JavaScript** (bibliotecas como SVGInject) busca o arquivo e troca o `<img>` pelo SVG inline depois do carregamento: volta a requisição, depende de JS e pode piscar. O `include` no servidor (PHP) ou no build não tem esses custos. Biblioteca não nomeada na aula. Confiança alta.
- **WebKit vem do Autoprefixer, não do Sass,** e prefixo não deixa o CSS "mais performático". Já registrado em [[wiki/concepts/pre-processador-css]] e [[wiki/concepts/prefixo-de-fornecedor]]. Confiança alta.
- **8KB × 728KB depende do export.** O PNG saiu de um frame grande em escala alta; um PNG 1x do tamanho exibido seria bem menor, e WebP menor ainda. O SVG também comprime mais com gzip/Brotli. A ordem de grandeza a favor do SVG vale para ilustração plana. Confiança média-alta.
- **IE 6 a 8 e Android 2.x.** O IE 9 já tinha suporte básico; o Android browser sem SVG era o 2.x. Confiança alta.
- **Acessibilidade das quatro formas.** `<img>` pede `alt`; background é decorativo (sem texto para o leitor de tela); inline pede `role="img"` + `<title>`/`aria-label`, ou `aria-hidden="true"` quando decorativo. Ausente na aula. Confiança alta.

## Open Questions

- "index.html de fora": provável "default"/snippet `html:5` do Emmet; deixado literal.
- "Web.svg" depois de renomear para `app`: erro de ASR para "app.svg" ou outro arquivo? Deixado literal.
- "Como a minha array está sendo no CSS": provável "como o meu arquivo está"; deixado literal.
- "Lá no script-fe": o mesmo "Script FE" de outras aulas do FrontPUSH, módulo de CSS; deixado literal.
- "O segundo jeito que eu também coloquei aqui no Figma, estou esquecendo aqui onde está a aula": ele perde o slide e volta à tag img antes de passar ao background.
- Qual biblioteca JavaScript de "include" ele vai mostrar?

## Continuação

Segue [[wiki/sources/frontpush-propriedades-svg-introducao-o-que-e-por-que-usar]], que prometeu "como é que a gente insere o SVG nas nossas páginas HTML" e a desvantagem do inline. A próxima aula promete "a estrutura do SVG".

Cumprido em [[wiki/sources/frontpush-estrutura-svg-viewport-viewbox-formas-basicas-path-defs]]: viewport × viewBox, formas básicas, path, `defs` e a confirmação dos IDs repetidos (`filter0_d`).

## Raw quotes

- "acredito que são as únicas quatro"
- "não tem edição no DOM, não tem como ter interação com o CSS, porque está dentro da tag img"
- "eu tenho que definir [...] um height fixo, porque senão ele não vai aparecer"
- "só vi desvantagem e nem cheguei a considerar"
- "o módulo que eu mais utilizo, que é o inline, que é literalmente o SVG puro"
- "imagina você colocar vários blocos desse no seu código, tipo manchando o seu código"
