---
type: concept
title: "Peso tipográfico"
aliases: ["font-weight", "negrito", "bold", "itálico", "estilo falso", "faux bold"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
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

## Key Sources

- [[wiki/sources/tipografia-negrito-italico-tracking-kerning-maiusculas]] — negrito e itálico como contraste; font-weight no Inspect; estilo falso
