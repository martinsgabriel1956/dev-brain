---
type: concept
title: "CSS (Cascading Style Sheets)"
aliases: ['CSS', 'folhas de estilo em cascata']
date_created: 2026-10-14
date_updated: 2026-11-16
source_count: 7
tags: [css, frontend, web, historia, box-model, shorthand-css]
skill: tech-mentor-frontend
status: draft
---

# CSS (Cascading Style Sheets)

Linguagem **declarativa** que separa estilo de conteúdo: regras visuais aplicadas ao HTML, resolvidas em **cascata** (árvore de atributos de estilo). Surgiu ~1995–96; IE implementou melhor o primeiro CSS que a Netscape ([[wiki/concepts/guerra-dos-navegadores]]). CSS2/2.1: web fonts, i18n, posicionamento relativo/absoluto, migração de layouts de tabelas para elementos flutuantes; CSS3 (oficial em 2012 segundo o autor) trouxe media queries ([[wiki/concepts/design-responsivo]]). Pré-processadores: Sass/Less ([[wiki/concepts/transpilador]]); frameworks: [[wiki/entities/twitter-bootstrap]]. Ver [[wiki/concepts/cssom]], [[wiki/concepts/html-hipertexto]].

## CSS sobre SVG

Por ser código com tags, um [[wiki/concepts/formato-svg|SVG]] inline pode ter os caminhos estilizados e animados pelo CSS; para [[wiki/entities/nasser|Násser]], é daí que "a magia do Motion surgiu" ([[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]]). `[external]` Via `<img>` ou `background-image` o CSS da página não alcança os caminhos.

## CSS a partir do Figma

A aba inspect do [[wiki/entities/figma]] dá o CSS do elemento. background, box-shadow e border-radius servem; width, height, top e left dependem da arquitetura (flexbox, position). Os nomes do style guide seguem o CSS (`card-hover`), e a paleta vai para variáveis Sass ou CSS ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]). `[external]` A aula chama hover de pseudo-element; `:hover` é pseudo-classe (https://developer.mozilla.org/en-US/docs/Web/CSS/:hover).

## Tipografia no CSS

O módulo de tipografia do curso de UI fecha com as propriedades de texto no CSS: `font-family`, pesos (light, normal, bold), e o vínculo da fonte com `<link>` (preferido, "mais performático") ou `@import` ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]). Ver [[wiki/concepts/webfonts]].

## Propriedades tipográficas

Em [[wiki/sources/tipografia-negrito-italico-tracking-kerning-maiusculas]], o Inspect do [[wiki/entities/figma]] traduz o design em `letter-spacing` ([[wiki/concepts/tracking]]), `font-family`, `font-style` e `font-weight` ([[wiki/concepts/peso-tipografico]]). Peso usado no CSS sem ter sido carregado do Google Fonts ou Adobe Fonts vira estilo "falso".

## Alinhamento padrão

Em [[wiki/sources/alinhamento-e-espacamento-de-texto]], alinhar à esquerda é "o padrão do CSS": as tags de texto e de título já vêm assim. `[external]` Mais precisamente, o valor inicial de `text-align` é `start`, que segue a direção do idioma: https://developer.mozilla.org/en-US/docs/Web/CSS/text-align. Ver [[wiki/concepts/alinhamento-de-texto]].

## Classes e IDs

Em [[wiki/sources/classes-e-ids-no-css]], o CSS externo (arquivo `.css` ligado por `<link>`) é a forma "mais utilizada" das três, porque escala o estilo e mantém organização e consistência. A aula apresenta os [[wiki/concepts/seletores-css|seletores]] universal, de tipo, de classe (`.`) e de ID (`#`). A diferença de peso entre eles é a [[wiki/concepts/especificidade-css]], que a aula não aborda.
## Seletores e pseudo-classes

Em [[wiki/sources/seletores-e-pseudo-elements-css]], Násser defende seletores para criar "a menor quantidade de classes possíveis" e percorre o Try CSS Selector do [[wiki/entities/w3schools]]: classe, ID, vírgula, descendente, filho, adjacente, universal, atributo, e uma lista de estados que ele chama de pseudo-elements. Ver [[wiki/concepts/seletores-css]], [[wiki/concepts/pseudo-classe-css]] e [[wiki/concepts/pseudo-elemento-css]]. A troca de nomes da aula de style guide (hover como pseudo-element) se repete aqui.
## O básico: três famílias e três formas de aplicar

Em [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]], o CSS é "Cascading Style Sheets, ou seja, folhas de estilo", e "o poder está na junção" com o HTML. O autor divide as propriedades em estilo, layout e motion. A [[wiki/concepts/regra-css|regra]] é `elemento { propriedade: valor; }`, aplicada por arquivo externo (`<link>`, a forma mais usada), `<style>` no `<head>` ou atributo `style`, com prioridade resolvida pela [[wiki/concepts/cascata-css]]. `[external]` A aula o chama de linguagem de "marcação"; o MDN o classifica como linguagem de folha de estilo: https://developer.mozilla.org/en-US/docs/Web/CSS.
## Box model e propriedades resumo

O módulo "Básico CSS" do [[wiki/entities/frontpush|FrontPUSH]] ensina que "tudo é caixa" ([[wiki/concepts/box-model]]) e que muitas propriedades resumem outras: `padding`, `margin`, `border` e `background` ([[wiki/concepts/shorthand-css]]). Para consultar a ordem dos valores, o autor indica o "W3C" com "try it yourself" (na verdade o W3Schools, ver [[wiki/entities/w3c]]). Unidades em [[wiki/concepts/unidades-de-medida-css]] ([[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]]).
## Propriedades básicas na prática

Em [[wiki/sources/principais-propriedades-css-color-background-font]], primeira aula de código do [[wiki/entities/frontpush|FrontPUSH]] na wiki, [[wiki/entities/nasser|Násser]] percorre as propriedades principais: `color` (texto) e `background-color` (fundo); imagem por `<img>` ou por [[wiki/concepts/background-css|background-image]]; `margin: 0 auto` com largura em % para centralizar; [[wiki/concepts/display-css|display]] block x inline; `font-family`, `font-size`, `font-weight`, `font-variant`; `line-height`, `text-align`, `vertical-align`, `text-shadow`, `box-shadow`, `letter-spacing`, `text-decoration`. A atitude: aprender as principais e descobrir o resto no [[wiki/entities/w3schools]], e depurar com `border: 1px solid red`, "como se fosse um printf".

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
- [[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]] — SVG é código com tags, então o CSS manipula seus caminhos (base do motion)
- [[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]] — CSS do inspect; nomes iguais ao CSS; hover é pseudo-classe
- [[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]] — tipografia: font-family, pesos, `<link>` x `@import`
- [[wiki/sources/tipografia-negrito-italico-tracking-kerning-maiusculas]] — letter-spacing, font-weight e estilo falso
- [[wiki/sources/alinhamento-e-espacamento-de-texto]] — text-align à esquerda como padrão (inicial `start`)
- [[wiki/sources/classes-e-ids-no-css]] — classe x ID, CSS externo como padrão, `.btn` com variações
- [[wiki/sources/seletores-e-pseudo-elements-css]] — seletores para menos classes; lista de pseudo-classes chamada de pseudo-elements
- [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]] — três famílias (estilo, layout, motion); regra; externo, incorporado e inline
- [[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]] — box model, shorthand (TRBL), unidades, W3Schools como referência
- [[wiki/sources/principais-propriedades-css-color-background-font]]: primeiras propriedades: color, background, display, font, texto; border como printf
