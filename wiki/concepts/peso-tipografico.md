---
type: concept
title: "Peso tipográfico"
aliases: ["font-weight", "negrito", "bold", "itálico", "estilo falso", "faux bold"]
date_created: 2026-11-15
date_updated: 2026-11-16
source_count: 5
tags: [ui, ui-design, tipografia, font-weight, negrito, italico, contraste, css]
skill: ux-ui-mentor
status: stub
---

# Peso tipográfico

Espessura do traço da fonte (light, regular, bold...), no CSS `font-weight`. Junto com o itálico, é o jeito de criar [[wiki/concepts/contraste]] dentro de um texto sem mudar tamanho nem cor. Parte de [[wiki/concepts/tipografia]].

## Negrito e itálico destacam por contraste

Em [[wiki/sources/tipografia-negrito-italico-tracking-kerning-maiusculas]], [[wiki/entities/nasser|Násser]]: num texto de peso uniforme, uma palavra em negrito é "um pingo em meio a um universo diferente", e o olho vai até ela; o itálico faz o mesmo, de forma "um pouco mais sutil". Por isso vale "em detalhes, em pontos importantes": um período inteiro em negrito perde o contraste. Negrito "principalmente em títulos"; itálico em "e-mails, endereços".

`[skill: ux-ui-mentor]` Peso é o recurso de "destaque dentro do mesmo tamanho"; itálico, para "citações, ênfase, metadados".

## Número ou nome

No Inspect do [[wiki/entities/figma]], trocar a fonte para Medium muda `font-weight` para 500. Násser prefere o número, ou `bold` (700). Ele diz que o peso vai "de 100 até 700"; `[external]` o CSS aceita de 1 a 1000 e as fontes costumam ir até 900 (https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight). A Mukta, exemplo da aula, vai de extra light (200) a extra bold (800).

## Estilo falso

No Google Fonts ou no Adobe Fonts só vêm os pesos selecionados. Se o CSS pede um peso que não foi carregado, "ele vai se tornar falso". O Figma "se preocupa em ser real" e só oferece os pesos que a fonte tem. `[external]` O navegador sintetiza negrito e itálico ausentes engrossando ou inclinando o glifo; a propriedade `font-synthesis` controla isso (https://developer.mozilla.org/en-US/docs/Web/CSS/font-synthesis).

## font-weight no código

Em [[wiki/sources/principais-propriedades-css-color-background-font]], com só regular e bold carregados do [[wiki/entities/google-fonts]], `font-weight: 500` "não mudou ainda" e 700 ficou negrito. É o lado do código do estilo falso: o navegador cai no peso carregado mais próximo (500 → 400) `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight#fallback_weights).

## Na NLW #2, dia 1 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]], `font-weight` vai de 100 ("mais leves") a 700 ("mais fortes como bold"); o Proffy usa 500. *Weight* é "no inglês, peso".

## Na NLW #2, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]], o `h2` da landing vem em bold pelo navegador e Mayk o leva a 500. No botão do card, o layout pede 600, mas o Archivo foi importado só em 400 e 700; sem o arquivo, o navegador usa o peso mais próximo ou sintetiza.

## Key Sources

- [[wiki/sources/tipografia-negrito-italico-tracking-kerning-maiusculas]] — negrito e itálico como contraste; font-weight no Inspect; estilo falso
- [[wiki/sources/principais-propriedades-css-color-background-font]]: 500 sem efeito, 700 negrito, com só regular e bold carregados
- [[wiki/sources/frontpush-layout-css-botao-hover-flexbox-media-query]]: `font-weight: bold` para "um peso tipográfico maior"
- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: NLW #2, dia 1: font-weight 100 a 700
- [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]: NLW #2, dia 2: 500 no h2; 600 não importado
