---
type: concept
title: "HTML e Hipertexto"
aliases: ['HTML', 'hipertexto', 'href']
date_created: 2026-10-14
date_updated: 2026-11-16
source_count: 7
tags: [html, web, hipertexto, historia, html5, html-semantico]
skill: tech-mentor-frontend
status: draft
---

# HTML e Hipertexto

HTML marca **estrutura** (cabeçalho, parágrafo, lista), herdando a ideia do SGML; a apresentação cabia ao navegador/usuário (daí as páginas cinza/preto/azul do começo). O `<a href>` (âncora + *hypertext reference*) criou o **hipertexto** e, com ele, a WWW. O `style` inline foi o primeiro controle rudimentar; [[wiki/concepts/css]] separou estilo de conteúdo. HTML 4 trouxe DHTML; XML/XHTML ([[wiki/concepts/xml-extensible-markup-language]]) estruturam dados; HTML5 só foi oficializado em 2014 ([[wiki/entities/w3c]]). Ver [[wiki/concepts/dom]], [[wiki/concepts/historia-do-front-end]].

## Atributos class e id

Em [[wiki/sources/classes-e-ids-no-css]], os elementos HTML recebem `class` (vários elementos, várias classes separadas por espaço) e `id` (um elemento só, "o seu CPF") para o CSS e o JavaScript os encontrarem. A aula os chama de "tags"; `[external]` são atributos globais: https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes.
## Estrutura básica do HTML5

Em [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]], o Emmet do [[wiki/entities/vs-code]] gera a estrutura do HTML5: `<html>` engloba tudo, `<head>` é o cabeçalho com as tags meta e o `<title>` (texto da aba), `<body>` recebe o conteúdo. HTML puro dá uma página "extremamente arcaica"; o [[wiki/concepts/css]] entra para personalizar. O atributo `style` inline continua existindo e é a forma de maior prioridade na [[wiki/concepts/cascata-css]].
## Antes do HTML5, tudo era div

Segundo a aula de box model do [[wiki/entities/frontpush|FrontPUSH]], antes do HTML5 "basicamente todo o site era composto por divs", além das tags "desde a fundação do HTML" (link, parágrafo, título, body, head). section, article e as demais [[wiki/concepts/html-semantico|tags semânticas]] vieram com o HTML5 ([[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]]).
## Tags semânticas

Em [[wiki/sources/position-css-static-relative-absolute-fixed-sticky]], `section` em vez de `div` "para poder ficar um pouco mais interessante na questão da semântica", e o menu é `nav` com `ul`/`li` ("lista não ordenada, só com pontinhos"). `[external]` `section` e `nav` são elementos do HTML5 que leitores de tela anunciam como regiões: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav.

## O navegador entende três coisas

Para [[wiki/entities/nasser|Násser]] ([[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]), "todo o navegador, ele entende três coisas, HTML, CSS e JavaScript", por isso só um editor basta para começar. HTML é "uma linguagem de marcação". As diferenças de interpretação entre navegadores ficam em [[wiki/concepts/compatibilidade-entre-navegadores]].

## Linguagem de marcação e tags (aula 02 do FrontPUSH)

Em [[wiki/sources/frontpush-o-que-e-html-linguagem-de-marcacao-tags-semantica]], [[wiki/entities/nasser|Násser]] lê a sigla: "é uma linguagem, só que é uma linguagem de marcação", e marcação são "labels, ou seja, etiquetas" para "marcar o conteúdo". O HTML "é responsável pelo conteúdo das páginas web"; o estilo vem do [[wiki/concepts/css]]. Uma tag "abre e fecha", e as tags podem ficar "uma dentro das outras" (use tabulação para enxergar o aninhamento). `<html>` engloba tudo, `<head>` traz os [[wiki/concepts/head-html-metadados|metadados]] e `<body>` o conteúdo. Uma tag inventada (`<tiririca>`) "ele não conhece". `[external]` Tag abre com `<` (a aula diz "sinal de maior"); tag desconhecida vira `HTMLUnknownElement` inline, e tags próprias válidas são custom elements com hífen: https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_custom_elements.

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
- [[wiki/sources/classes-e-ids-no-css]] — atributos class e id
- [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]] — estrutura do HTML5, `<head>`, `<title>`, `style` inline
- [[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]] — antes do HTML5, interfaces feitas de divs; tags semânticas vieram com o HTML5
- [[wiki/sources/position-css-static-relative-absolute-fixed-sticky]]: `section` e `nav` por semântica
- [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]: o navegador entende HTML, CSS e JavaScript; só um editor basta
- [[wiki/sources/frontpush-o-que-e-html-linguagem-de-marcacao-tags-semantica]]: marcação como etiquetas; tags, aninhamento, html/head/body; tag inventada
