---
type: concept
title: "SPA (Single Page Application)"
aliases: ['SPA', 'single page apps']
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [spa, frontend, estado, historia]
skill: tech-mentor-frontend
status: draft
---

# SPA (Single Page Application)

Aplicação carregada uma vez (JS, CSS, imagens) que muda de estado via [[wiki/concepts/ajax]] **sem trocar de página**. Move o controle de estado dos servidores de aplicação para perto da tela; a UI se organiza em **componentes** com estado (playlist, dashboard de playback no Spotify). Exemplos: Google Docs, Slack, Spotify. Frameworks: Backbone, Ember (origem no SproutCore da Apple), AngularJS/Polymer (Google), React + [[wiki/concepts/virtual-dom|Virtual DOM]], Vue. Usa Web Storage para estado local. Comparar com [[wiki/concepts/renderizacao-ssr-vs-csr]] e [[wiki/concepts/hydration]]; ver [[wiki/entities/react]], [[wiki/concepts/estado]].

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
