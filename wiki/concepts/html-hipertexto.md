---
type: concept
title: "HTML e Hipertexto"
aliases: ['HTML', 'hipertexto', 'href']
date_created: 2026-10-14
date_updated: 2026-11-16
source_count: 2
tags: [html, web, hipertexto, historia]
skill: tech-mentor-frontend
status: draft
---

# HTML e Hipertexto

HTML marca **estrutura** (cabeçalho, parágrafo, lista), herdando a ideia do SGML; a apresentação cabia ao navegador/usuário (daí as páginas cinza/preto/azul do começo). O `<a href>` (âncora + *hypertext reference*) criou o **hipertexto** e, com ele, a WWW. O `style` inline foi o primeiro controle rudimentar; [[wiki/concepts/css]] separou estilo de conteúdo. HTML 4 trouxe DHTML; XML/XHTML ([[wiki/concepts/xml-extensible-markup-language]]) estruturam dados; HTML5 só foi oficializado em 2014 ([[wiki/entities/w3c]]). Ver [[wiki/concepts/dom]], [[wiki/concepts/historia-do-front-end]].

## Tags semânticas

Em [[wiki/sources/position-css-static-relative-absolute-fixed-sticky]], `section` em vez de `div` "para poder ficar um pouco mais interessante na questão da semântica", e o menu é `nav` com `ul`/`li` ("lista não ordenada, só com pontinhos"). `[external]` `section` e `nav` são elementos do HTML5 que leitores de tela anunciam como regiões: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav.

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
- [[wiki/sources/position-css-static-relative-absolute-fixed-sticky]]: `section` e `nav` por semântica
