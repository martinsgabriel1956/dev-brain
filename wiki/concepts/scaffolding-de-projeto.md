---
type: concept
title: "Scaffolding de Projeto (Vue CLI vs. create-vue)"
aliases: ["scaffold", "gerador de projeto", "create-vue", "Vue CLI", "npm create"]
date_created: 2026-11-12
date_updated: 2026-11-12
source_count: 1
tags: [vue, vue-cli, create-vue, vite, tooling, frontend]
skill: tech-mentor-frontend
status: stub
---

# Scaffolding de Projeto (Vue CLI vs. create-vue)

Ferramenta que gera a estrutura inicial de um projeto: pastas, `package.json`, configuração de build e servidor de desenvolvimento. No [[wiki/entities/vue]] há duas gerações:

| | Vue CLI (`@vue/cli`) | create-vue |
|---|---|---|
| Como roda | `npm install -g @vue/cli`, depois `vue create` | `npm create vue@latest`, sem instalação global |
| Build | webpack | Vite |
| Status | modo de manutenção ([external](https://cli.vuejs.org/guide/)) | recomendado pelo guia oficial ([external](https://vuejs.org/guide/quick-start.html)) |

Cursos ainda ensinam o Vue CLI: o curso de [[wiki/sources/configurando-ambiente-vue-node-npm-vue-cli]] segue com ele nas aulas seguintes, segundo o usuário. Quem estuda por um curso desses aprende o Vue em si sem problema; o que muda é a camada de build (`vue.config.js` e webpack contra `vite.config.js`), as variáveis de ambiente (`VUE_APP_*` contra `VITE_*`) e o servidor de desenvolvimento (`npm run serve` contra `npm run dev`) `[skill: tech-mentor-frontend]`. Para projeto novo, a documentação recomenda o `create-vue`. O `npm create <x>` executa o pacote `create-<x>` sob demanda, e com isso evita a deriva de versão de uma [[wiki/concepts/instalacao-global-vs-local|instalação global]].

## Key sources

- [[wiki/sources/configurando-ambiente-vue-node-npm-vue-cli]]
