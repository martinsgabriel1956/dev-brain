---
type: entity
title: "Vue.js"
aliases: ["Vue", "Vue 3", "Vue.js"]
date_created: 2026-11-12
date_updated: 2026-11-12
source_count: 3
tags: [frontend, framework, javascript, vue, reatividade]
skill: tech-mentor-frontend
status: stub
---

# Vue.js

Framework JavaScript de UI. Usa [[wiki/concepts/virtual-dom]] na renderização e reatividade por proxies (`ref`/`reactive`), parecida com [[wiki/concepts/signals]] ([[wiki/sources/10-conceitos-internos-frameworks-frontend]]). A linha atual é a 3.x (3.5.45 no npm em 12/11/2026, [external](https://registry.npmjs.org/vue/latest)).

## Ambiente e criação de projeto

Pré-requisitos: [[wiki/entities/nodejs]] e um [[wiki/concepts/gerenciador-de-pacotes]]. O caminho oficial atual é `npm create vue@latest` (`create-vue`, com Vite). O Vue CLI (`@vue/cli`, comando `vue`) está em modo de manutenção ([external](https://cli.vuejs.org/guide/)), embora cursos ainda o ensinem ([[wiki/sources/configurando-ambiente-vue-node-npm-vue-cli]]). O número que `vue --version` mostra é do CLI, não do framework. Ver [[wiki/concepts/scaffolding-de-projeto]].

## Key sources

- [[wiki/sources/configurando-ambiente-vue-node-npm-vue-cli]]
- [[wiki/sources/clean-architecture-frontend-vue-diagrama-camadas-login]]
- [[wiki/sources/10-conceitos-internos-frameworks-frontend]]
