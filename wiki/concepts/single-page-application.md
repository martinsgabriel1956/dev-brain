---
type: concept
title: "SPA (Single Page Application)"
aliases: ['SPA', 'single page apps']
date_created: 2026-10-14
date_updated: 2026-11-16
source_count: 4
tags: [spa, frontend, estado, historia]
skill: tech-mentor-frontend
status: draft
---

# SPA (Single Page Application)

Aplicação carregada uma vez (JS, CSS, imagens) que muda de estado via [[wiki/concepts/ajax]] **sem trocar de página**. Move o controle de estado dos servidores de aplicação para perto da tela; a UI se organiza em **componentes** com estado (playlist, dashboard de playback no Spotify). Exemplos: Google Docs, Slack, Spotify. Frameworks: Backbone, Ember (origem no SproutCore da Apple), AngularJS/Polymer (Google), React + [[wiki/concepts/virtual-dom|Virtual DOM]], Vue. Usa Web Storage para estado local. Comparar com [[wiki/concepts/renderizacao-ssr-vs-csr]] e [[wiki/concepts/hydration]]; ver [[wiki/entities/react]], [[wiki/concepts/estado]].

Na NLW #1 com [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]): da listagem para a edição, "eu não preciso ter um recarregamento completo da tela". Cabeçalho, menu e rodapé ficam, e só o conteúdo muda. O SPA também divide responsabilidades: o back-end vira uma [[wiki/concepts/api-rest]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: `<a href>` recarrega tudo e `<Link to>` do React Router troca de tela sem nenhuma requisição na aba Network.

## Na NLW #2, dia 1 (Diego Fernandes)

"Uma aplicação que não precisa ser recarregada do zero toda vez que o usuário navega." A demonstração é a aba Network: `<a href>` recarrega tudo, `<Link to>` não carrega nada. A origem atribuída ao Angular ("lá em 2011") não procede: o AngularJS é de 2010, e SPAs com XHR são anteriores. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]].

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: SPA no React, sem recarregar a página; divisão com a API
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: Link x a href na prática
- [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]: NLW #2, Diego, dia 1: SPA na aba Network; origem atribuída ao Angular
