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

## Estrutura básica do HTML5

Em [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]], o Emmet do [[wiki/entities/vs-code]] gera a estrutura do HTML5: `<html>` engloba tudo, `<head>` é o cabeçalho com as tags meta e o `<title>` (texto da aba), `<body>` recebe o conteúdo. HTML puro dá uma página "extremamente arcaica"; o [[wiki/concepts/css]] entra para personalizar. O atributo `style` inline continua existindo e é a forma de maior prioridade na [[wiki/concepts/cascata-css]].

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
- [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]] — estrutura do HTML5, `<head>`, `<title>`, `style` inline
